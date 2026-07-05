#!/usr/bin/env python3
"""Capture desktop and mobile screenshots of a URL and dump page metrics."""
import asyncio, json, sys, os
from pathlib import Path
from playwright.async_api import async_playwright

URL = sys.argv[1] if len(sys.argv) > 1 else "https://www.deepseekv.pro/"
OUT_DIR = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parent.parent / "screenshots"
OUT_DIR.mkdir(parents=True, exist_ok=True)


async def capture(name: str, viewport: dict, device_scale_factor: float = 1.0):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context(
            viewport=viewport,
            device_scale_factor=device_scale_factor,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        await page.goto(URL, wait_until="networkidle", timeout=30000)

        # Full page screenshot
        await page.screenshot(path=str(OUT_DIR / f"{name}_full.png"), full_page=True)

        # Above-the-fold only (viewport clip)
        await page.screenshot(path=str(OUT_DIR / f"{name}_fold.png"), full_page=False)

        # Extract accessible name / AX tree summary
        ax_snapshot = await page.accessibility.snapshot()
        metrics = {
            "viewport": viewport,
            "url": page.url,
            "title": await page.title(),
            "h1_texts": await page.eval_on_selector_all("h1", "els => els.map(e => e.textContent?.trim())"),
            "h2_texts": await page.eval_on_selector_all("h2", "els => els.map(e => e.textContent?.trim())"),
            "viewport_meta": await page.eval_on_selector("meta[name='viewport']", "e => e?.content") or None,
            "above_fold_text": await page.evaluate("""() => {
                const vh = window.innerHeight;
                const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null);
                const texts = [];
                let node;
                while (node = walker.nextNode()) {
                    const rect = node.parentElement?.getBoundingClientRect?.();
                    if (rect && rect.top < vh && rect.bottom > 0 && rect.left < window.innerWidth && rect.right > 0) {
                        const t = node.textContent?.trim();
                        if (t) texts.push(t);
                    }
                }
                return texts.slice(0, 60);
            }"""),
            "tap_targets_small": await page.evaluate("""() => {
                const small = [];
                const els = document.querySelectorAll('a, button, [role="button"], input[type="submit"], .btn, [onclick]');
                els.forEach(el => {
                    const r = el.getBoundingClientRect();
                    if (r.width > 0 && r.height > 0 && (r.width < 48 || r.height < 48)) {
                        small.push({tag: el.tagName, text: el.textContent?.trim().slice(0,40), w: Math.round(r.width), h: Math.round(r.height)});
                    }
                });
                return small;
            }"""),
            "font_sizes_on_body": await page.evaluate("""() => {
                const sizes = new Set();
                const els = document.querySelectorAll('body, p, span, a, li, h1, h2, h3, h4');
                els.forEach(el => {
                    const s = window.getComputedStyle(el).fontSize;
                    sizes.add(s);
                });
                return [...sizes].sort();
            }"""),
            "images_without_dimensions": await page.evaluate("""() => {
                const imgs = [];
                document.querySelectorAll('img').forEach(img => {
                    if (!img.hasAttribute('width') && !img.hasAttribute('height')) {
                        imgs.push({src: img.src.slice(0, 80), naturalW: img.naturalWidth, naturalH: img.naturalHeight});
                    }
                });
                return imgs;
            }"""),
            "og_meta": await page.evaluate("""() => {
                const tags = {};
                ['og:title','og:description','og:image','og:url','og:type','twitter:card','twitter:image','twitter:title','twitter:description'].forEach(p => {
                    const el = document.querySelector(`meta[property="${p}"], meta[name="${p}"]`);
                    tags[p] = el?.content || null;
                });
                return tags;
            }"""),
            "favicon_links": await page.evaluate("""() => {
                const links = [];
                document.querySelectorAll('link[rel*="icon"], link[rel="apple-touch-icon"]').forEach(l => {
                    links.push({rel: l.rel, href: l.href});
                });
                return links;
            }"""),
            "accessibility_tree": ax_snapshot,
        }
        (OUT_DIR / f"{name}_metrics.json").write_text(json.dumps(metrics, indent=2, ensure_ascii=False))
        print(f"[{name}] Screenshots saved. Title: {metrics['title']}")
        await browser.close()


async def main():
    await capture("desktop", {"width": 1920, "height": 1080}, device_scale_factor=1.0)
    await capture("mobile", {"width": 375, "height": 812}, device_scale_factor=2.0)
    # Also capture tablet
    await capture("tablet", {"width": 768, "height": 1024}, device_scale_factor=1.0)
    print("All captures complete.")

asyncio.run(main())

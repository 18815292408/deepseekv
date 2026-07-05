#!/usr/bin/env python3
"""
精准清理 effectivecpmnetwork 错代码（不像上次撤过头了）：

- NativeBanner_1 (id=30113316): API direct_url 空 → Adsterra 自家 serve → CDN 是 profitabledisplaynetwork.com →
  现在的 effectivecpmnetwork.com zone script 是错的，**撤掉**，留 SPONSORED 占位 + min-height placeholder
- SocialBar_1 (id=30113319): API direct_url 空 → Adsterra 自家 serve → 同上 → **撤掉**
- Popunder_1 (id=30113317): API direct_url = effectivecpmnetwork.com → Adsterra 后端正式配的填充链路 → **保留**
- Smartlink_1 (id=30113318): API direct_url = effectivecpmnetwork.com → 同上 → **保留**
"""
import re
from pathlib import Path

PAGES = [
    'deepseek32-landing.html',
    'deepseek-v4.html',
    'deepseek-v3-to-v4-migration.html',
    'deepseek-v4-coding-benchmark.html',
    'deepseek-v4-long-context.html',
]

# 1) 底部 Native Banner 区块：撤掉 effectivecpmnetwork.com zone script + 容器 div，保留外层 + SPONSORED 占位
NATIVE_BANNER_OLD = re.compile(
    r'<!-- Ad: Native Banner \(effectivecpmnetwork\.com\) -->\s*'
    r'<div class="ad-native-banner"[^>]*>\s*'
    r'<div[^>]*>\s*'
    r'SPONSORED · 推广披露 · <a href="/advertising-disclosure\.html"[^>]*>Advertising Disclosure</a>\s*'
    r'</div>\s*'
    r'<script async="async" data-cfasync="false" src="https://pl30213815\.effectivecpmnetwork\.com/[^"]+/invoke\.js"></script>\s*'
    r'<div id="container-ebe954634f6c78466c5e14609e5dd149"[^>]*></div>\s*'
    r'</div>',
    re.MULTILINE
)

NATIVE_BANNER_NEW = '''<!-- Ad slot: Native Banner — awaiting Adsterra dashboard code
     Note: Adsterra API confirms NativeBanner_1 (id=30113316) has empty direct_url,
     meaning Adsterra serves it via their own CDN (profitabledisplaynetwork.com).
     Need to retrieve the proper code from beta.publishers.adsterra.com dashboard. -->
<div class="ad-native-banner" style="background: rgba(0,0,0,0.03); border: 1px dashed rgba(0,0,0,0.1); padding: 0.5rem; margin: 2rem auto; max-width: 1200px; border-radius: 8px;">
    <div style="font-size: 0.7rem; color: #888; text-transform: uppercase; letter-spacing: 0.05em; padding: 0.25rem 0; text-align: center;">
        SPONSORED · <a href="/advertising-disclosure.html" style="color: #888; text-decoration: underline;">Advertising Disclosure</a>
    </div>
    <div style="min-height: 60px;"></div>
</div>'''

# 2) 末尾 4 个 script 中，只撤 NativeBanner + SocialBar 那两行（保留 Popunder + Smartlink）
# 注意：保留 Popunder + Smartlink 是 Adsterra 官方在 API response 里配的 direct_url。
# 末尾区需要 pop + smart + social 三段中只撤错的那两段
TAIL_SOCIAL_BAR_OLD = re.compile(
    r'<script src="https://pl30213818\.effectivecpmnetwork\.com/[^"]+\.js"></script>\s*',
    re.MULTILINE
)

TAIL_SOCIAL_BAR_NEW = '''<!-- Social Bar (effectivecpmnetwork.com) — REMOVED.
       Adsterra API shows SocialBar_1 (id=30113319) has empty direct_url,
       meaning Adsterra serves it via profitabledisplaynetwork.com CDN.
       The pl30213818 zone script belonged to a different (incorrect) zone assignment. -->'''

for fname in PAGES:
    path = Path(fname)
    src = path.read_text(encoding='utf-8')
    new = src

    # Native Banner bottom block
    if NATIVE_BANNER_OLD.search(new):
        new = NATIVE_BANNER_OLD.sub(NATIVE_BANNER_NEW, new, count=1)
        print(f"  ✓ {fname}: cleaned bottom Native Banner block")
    else:
        print(f"  ⚠ {fname}: bottom Native Banner pattern not found")

    # Tail Social Bar script line
    if TAIL_SOCIAL_BAR_OLD.search(new):
        new = TAIL_SOCIAL_BAR_OLD.sub(TAIL_SOCIAL_BAR_NEW, new, count=1)
        print(f"  ✓ {fname}: removed tail Social Bar script")
    else:
        print(f"  ⚠ {fname}: tail Social Bar script not found")

    if new != src:
        path.write_text(new, encoding='utf-8')

print("\n--- VERIFICATION ---")
for fname in PAGES:
    path = Path(fname)
    content = path.read_text(encoding='utf-8')
    native_zone = content.count('pl30213815')
    popunder = content.count('pl30213816')
    smartlink = content.count('k6mwpc8t')
    socialbar = content.count('pl30213818')
    print(f"  {fname}:")
    print(f"    NativeBanner pl30213815={native_zone} (should be 0), Popunder pl30213816={popunder} (keep 1), Smartlink k6mwpc8t={smartlink} (keep 1), SocialBar pl30213818={socialbar} (should be 0)")

#!/usr/bin/env python3
'''Ad layout v1 (2026-10-19).

728x90  -> desktop only (.ad-728 hidden below 768px)
320x50  -> mobile only  (.ad-320 hidden from 768px up); Adsterra unit 31813454 / ed071f325355a48ba25384b8ff82138a
300x250 -> moved out of the footer into the content
native  -> moved out of the footer into the content

Run: python3 scripts/ad_mobile_layout.py [--dry]
'''
import os
import re
import sys

KEY_728 = 'ee8bc1e77d94a913b862ff8aaead0cca'
KEY_300 = '856aa80835ef4d5205c4bb07b7b9d37c'
KEY_320 = 'ed071f325355a48ba25384b8ff82138a'

# page -> (section index for the 300x250, section index for the native banner)
PLAN = {
    'deepseek32-landing.html': (2, 3),
    'deepseek-v4.html': (3, 5),
    'deepseek-v4-1-flash-1017.html': (3, 5),
    'deepseek-v4-vs-gpt5-vs-claude.html': (3, 5),
    'deepseek-v4-coding-benchmark.html': (2, 3),
    'deepseek-v4-long-context.html': (2, 4),
    'deepseek-v3-to-v4-migration.html': (3, 6),
    'deepseek-v4-vs-glm-5-3-prime.html': (3, 5),
    'claude-fable-5-5.html': (2, 4),
}

MARK_728 = '<!-- Ad: Banner 728x90'
MARK_300 = '<!-- Ad: Banner 300x250'
MARK_NATIVE = '<!-- Ad: Native Banner'

NL = chr(10)

STYLE_BLOCK = '''    <!-- Ad layout v1 (2026-10-19): 728 = desktop only, 320x50 = mobile only, 300x250 and native in content. -->
    <style id="ad-layout-v1">
        .ad-container { margin: 0; }
        @media (max-width: 767px) {
            .ad-container.ad-728 { display: none !important; }
        }
        @media (min-width: 768px) {
            .ad-container.ad-320 { display: none !important; }
        }
    </style>
'''

AD_320 = '''    <!-- Ad: Banner 320x50 (bauval.org - Adsterra CDN)
         320x50_1 (id=31813454) created 2026-10-19. Mobile only: .ad-320 is hidden from 768px up. -->
    <div class="container ad-container ad-320" style="padding: 0 2rem;">
    <div style="background: rgba(0,0,0,0.03); border: 1px dashed rgba(0,0,0,0.1); padding: 0.5rem; margin: 2rem auto; max-width: 1200px; border-radius: 8px; text-align: center;">
        <div style="font-size: 0.7rem; color: #888; text-transform: uppercase; letter-spacing: 0.05em; padding: 0.25rem 0;">
            SPONSORED &middot; <a href="/advertising-disclosure.html" style="color: #888; text-decoration: underline;">Advertising Disclosure</a>
        </div>
        <script>
            atOptions = {
                'key' : 'ed071f325355a48ba25384b8ff82138a',
                'format' : 'iframe',
                'height' : 50,
                'width' : 320,
                'params' : {}
            };
        </script>
        <script src="https://bauval.org/22/ed071f325355a48ba25384b8ff82138a"></script>
    </div>
    </div>'''

DIV = re.compile(r'<(/?)div\b')


def block_end(text, start):
    depth = 0
    for m in DIV.finditer(text, start):
        if m.group(1):
            depth -= 1
            if depth == 0:
                return text.index('>', m.start()) + 1
        else:
            depth += 1
    raise ValueError('unbalanced div at %d' % start)


def span(text, marker):
    i = text.index(marker)
    start = text.index('<div', i)
    end = block_end(text, start)
    e = end
    while e < len(text) and text[e] in ' \t' + NL:
        e += 1
    return i, e, text[start:end]


def section_starts(text):
    return [m.start() for m in re.finditer(r'<section\b', text)]


def line_start(text, pos):
    return text.rfind(NL, 0, pos) + 1


def add_class(block, cls):
    old = '<div class="container" style="padding: 0 2rem;">'
    new = '<div class="container %s" style="padding: 0 2rem;">' % cls
    return block.replace(old, new, 1)


def process(path, dry):
    text = open(path, encoding='utf-8').read()
    if 'ad-container ad-728' in text:
        print('SKIP (already done) %s' % path)
        return
    i728, e728, b728 = span(text, MARK_728)
    i300, e300, b300 = span(text, MARK_300)
    iNat, eNat, bNat = span(text, MARK_NATIVE)

    new728 = add_class(b728, 'ad-container ad-728')
    new300 = add_class(b300, 'ad-container ad-300')
    newNative = ('    <div class="container ad-container ad-native" style="padding: 0 2rem;">' + NL
                 + bNat + NL + '    </div>')

    for a, b in sorted([(i300, e300), (iNat, eNat)], reverse=True):
        text = text[:a] + text[b:]

    text = text[:i728] + new728 + NL + AD_320 + NL + text[e728:]

    s300, sNat = PLAN[path]
    secs = section_starts(text)
    if len(secs) <= max(s300, sNat):
        raise ValueError('%s: only %d sections, need index %d' % (path, len(secs), max(s300, sNat)))
    at = line_start(text, secs[sNat])
    text = text[:at] + newNative + NL + text[at:]
    secs = section_starts(text)
    at = line_start(text, secs[s300])
    text = text[:at] + new300 + NL + text[at:]

    if '<style id="ad-layout-v1">' not in text:
        text = text.replace('</head>', STYLE_BLOCK + '</head>', 1)

    msg = '%s sections=%d 300->%d native->%d' % (path, len(secs), s300, sNat)
    if dry:
        print('DRY   ' + msg)
        return
    open(path, 'w', encoding='utf-8').write(text)
    print('WROTE ' + msg)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(os.path.dirname(here))
    dry = '--dry' in sys.argv
    for p in PLAN:
        process(p, dry)


main()


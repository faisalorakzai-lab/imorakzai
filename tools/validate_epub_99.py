from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path('/home/ubuntu/imorakzai')
META = ROOT / 'book/metadata'
PAGE = ROOT / 'book/pages/page-099-identity-in-the-diaspora.html'

for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    ET.parse(META / name)
    print(f'valid_xml={name}')

html = PAGE.read_text(encoding='utf-8')
assert html.count('<svg') >= 70, 'Expected at least 70 original SVG graphics'
assert html.count('role="img"') >= 70, 'Expected accessible role metadata on SVG graphics'
assert html.count('<title id="g99-') == 69, 'Expected 69 atlas title nodes'
assert html.count('<desc id="g99-') == 69, 'Expected 69 atlas description nodes'
for phrase in ['IDENTITY IN THE DIASPORA', 'HOME', 'HOMELAND', 'PASHTUN', 'PAKISTANI', 'SELF-IDENTIFICATION', 'No single factor', 'not direct Orakzai diaspora evidence', 'AI', 'CONSENT', 'CHANGE ≠ DISAPPEARANCE']:
    assert phrase.lower() in html.lower(), f'Missing required phrase: {phrase}'
assert '[Internet Archive]' not in html and '](' not in html, 'Markdown-style links remain in HTML'
assert 'Orakzai diaspora percentages' not in html
print('page99_svg_and_content_checks=passed')

for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    text = (META / name).read_text(encoding='utf-8')
    assert 'page-099-identity-in-the-diaspora.html' in text, f'Page 99 missing from {name}'
    assert 'page-098-global-orakzai-communities.html' in text, f'Page 98 missing from {name}'
print('metadata_page99_checks=passed')

assert not list((ROOT / 'book/pages').glob('*100*')), 'Page 100 must not be created'
status = subprocess.run(['git', 'status', '--short'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.splitlines()
for line in status:
    path = line[3:]
    if path.startswith('book/pages/page-') and path not in {'book/pages/page-099-identity-in-the-diaspora.html'}:
        raise AssertionError(f'Unexpected earlier/later page change: {path}')
print('no_page100_and_page_scope_checks=passed')

from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path('/home/ubuntu/imorakzai')
META = ROOT / 'book/metadata'
PAGE = ROOT / 'book/pages/page-100-the-modern-orakzai.html'

for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    ET.parse(META / name)
    print(f'valid_xml={name}')

html = PAGE.read_text(encoding='utf-8')
svg_count = html.count('<svg')
assert svg_count >= 70, f'Expected at least 70 SVG graphics, found {svg_count}'
assert html.count('<title id="g100-') == 70, 'Expected 70 numbered atlas title nodes'
assert html.count('<desc id="g100-') == 70, 'Expected 70 numbered atlas description nodes'
assert html.count('role="img"') >= 73, 'Expected accessible role metadata on special and atlas graphics'
for phrase in ['THE MODERN ORAKZAI', 'Roots in the mountains', 'OPPORTUNITY — NOT GUARANTEE', 'ADMINISTRATIVE CHANGE', 'CULTURAL IDENTITY', '2018', '600', '52%', 'CAREER COUNSELLING', 'DOCUMENTED', 'EMERGING / POTENTIAL', 'The modern Orakzai should be documented through evidence, not assumption', '100 PAGES', 'UNFINISHED STORY', 'WILL NOT BE BUILT BY FORGETTING THE PAST']:
    assert phrase.lower() in html.lower(), f'Missing required phrase: {phrase}'
assert '](' not in html, 'Markdown-style links remain in HTML'
assert 'internet penetration' in html.lower(), 'Missing explicit data-gap boundary'
assert 'not a district-wide' in html.lower(), 'Missing programme-scope caveat'
assert 'page-101' not in html.lower(), 'Page 101 reference/file must not be created'
print(f'page100_svg_and_content_checks=passed svg_count={svg_count}')

for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    text = (META / name).read_text(encoding='utf-8')
    assert 'page-100-the-modern-orakzai.html' in text, f'Page 100 missing from {name}'
    assert 'page-099-identity-in-the-diaspora.html' in text, f'Page 99 missing from {name}'
print('metadata_page100_checks=passed')

assert not list((ROOT / 'book/pages').glob('*101*')), 'Page 101 must not be created'
status = subprocess.run(['git', 'status', '--short'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.splitlines()
for line in status:
    path = line[3:]
    if path.startswith('book/pages/page-') and path != 'book/pages/page-100-the-modern-orakzai.html':
        raise AssertionError(f'Unexpected earlier/later page change: {path}')
print('no_page101_and_page_scope_checks=passed')

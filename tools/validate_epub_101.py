from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path('/home/ubuntu/imorakzai')
META = ROOT / 'book/metadata'
PAGE = ROOT / 'book/pages/page-101-from-tribal-society-to-modern-society.html'

for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    ET.parse(META / name)
    print(f'valid_xml={name}')

html = PAGE.read_text(encoding='utf-8')
svg_count = html.count('<svg')
# One page-background SVG plus one hero and 65 substantive atlas cards.
assert svg_count >= 67, f'Expected at least 67 SVG elements including background, found {svg_count}'
assert html.count('<title id="g101-') == 65, 'Expected 65 numbered atlas title nodes'
assert html.count('<desc id="g101-') == 65, 'Expected 65 numbered atlas description nodes'
assert html.count('role="img"') >= 66, 'Expected accessible role metadata on hero and atlas graphics'
for phrase in ['FROM TRIBAL SOCIETY TO MODERN SOCIETY', 'CHANGE WITHOUT ERASURE', 'Modernity', 'WESTERNIZATION', 'FCR', '2018', 'JIRGA', 'HUJRA', 'not equivalent to Pakistan', 'Contemporary Orakzai research on how hujra', '700', '375', '600', '52%', 'DOCUMENTED', 'INTERPRETIVE', 'What still needs to be documented', 'MODERNITY IS NOT THE END OF TRADITION', 'continuing story of how people adapt']:
    assert phrase.lower() in html.lower(), f'Missing required phrase: {phrase}'
assert '](' not in html, 'Markdown-style links remain in HTML'
assert 'not district-wide' in html.lower() or 'not evidence' in html.lower(), 'Missing programme-scope caveat'
assert 'page-102' not in html.lower(), 'Page 102 reference/file must not be created'
print(f'page101_svg_and_content_checks=passed svg_count={svg_count}')

for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    text = (META / name).read_text(encoding='utf-8')
    assert 'page-101-from-tribal-society-to-modern-society.html' in text, f'Page 101 missing from {name}'
    assert 'page-100-the-modern-orakzai.html' in text, f'Page 100 missing from {name}'
print('metadata_page101_checks=passed')

assert not list((ROOT / 'book/pages').glob('*102*')), 'Page 102 must not be created'
status = subprocess.run(['git', 'status', '--short'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.splitlines()
for line in status:
    path = line[3:]
    if path.startswith('book/pages/page-') and path != 'book/pages/page-101-from-tribal-society-to-modern-society.html':
        raise AssertionError(f'Unexpected earlier/later page change: {path}')
print('no_page102_and_page_scope_checks=passed')

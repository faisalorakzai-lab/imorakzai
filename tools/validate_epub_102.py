from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path('/home/ubuntu/imorakzai')
META = ROOT / 'book/metadata'
PAGE = ROOT / 'book/pages/page-102-tradition-vs-modernity.html'

for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    ET.parse(META / name)
    print(f'valid_xml={name}')

html = PAGE.read_text(encoding='utf-8')
svg_count = html.count('<svg')
# One page-background SVG, one hero, and 69 atlas cards = 71 SVG elements.
assert svg_count >= 71, f'Expected at least 71 SVG elements including background, found {svg_count}'
assert html.count('<title id="g102-') == 69, 'Expected 69 numbered atlas title nodes plus hero'
assert html.count('<desc id="g102-') == 69, 'Expected 69 numbered atlas description nodes plus hero'
assert html.count('role="img"') >= 70, 'Expected accessible role metadata on hero and atlas graphics'
for phrase in ['TRADITION VS MODERNITY', 'CONTINUITY THROUGH CHANGE', 'Modernity', 'WESTERNIZATION', 'false choice', 'PRESERVE', 'ADAPT', 'INNOVATE', 'Pashto', 'Hujra', 'Jirga', 'AI', '2018', '25th Amendment', 'DOCUMENTED', 'INTERPRETIVE', 'What still needs to be documented', 'WE DO NOT HAVE TO CHOOSE BETWEEN OUR ROOTS AND OUR FUTURE', 'carry our roots into the future']:
    assert phrase.lower() in html.lower(), f'Missing required phrase: {phrase}'
assert '](' not in html, 'Markdown-style links remain in HTML'
for phrase in ['not automatically', 'not evidence', 'not claim', 'remains limited']:
    assert phrase.lower() in html.lower(), f'Missing evidence-boundary language: {phrase}'
assert 'page-103' not in html.lower(), 'Page 103 reference/file must not be created'
print(f'page102_svg_and_content_checks=passed svg_count={svg_count}')

for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    text = (META / name).read_text(encoding='utf-8')
    assert 'page-102-tradition-vs-modernity.html' in text, f'Page 102 missing from {name}'
    assert 'page-101-from-tribal-society-to-modern-society.html' in text, f'Page 101 missing from {name}'
print('metadata_page102_checks=passed')

assert not list((ROOT / 'book/pages').glob('*103*')), 'Page 103 must not be created'
status = subprocess.run(['git', 'status', '--short'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.splitlines()
for line in status:
    path = line[3:]
    if path.startswith('book/pages/page-') and path != 'book/pages/page-102-tradition-vs-modernity.html':
        raise AssertionError(f'Unexpected earlier/later page change: {path}')
print('no_page103_and_page_scope_checks=passed')

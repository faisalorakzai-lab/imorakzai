from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path('/home/ubuntu/imorakzai')
META = ROOT / 'book/metadata'
PAGE = ROOT / 'book/pages/page-098-global-orakzai-communities.html'

for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    ET.parse(META / name)
    print(f'valid_xml={name}')

for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    text = (META / name).read_text(encoding='utf-8')
    assert 'page-098-global-orakzai-communities.html' in text, f'Page 98 missing from {name}'
    assert 'page-097-orakzai-overseas.html' in text, f'Page 97 missing from {name}'
print('metadata_order_checks=passed')

html = PAGE.read_text(encoding='utf-8')
assert html.count('<svg') >= 77, 'Expected hero, map, and 75+ atlas SVGs'
assert len(re.findall(r'<title id="g98-[0-9]+-title">', html)) == 75
assert len(re.findall(r'<desc id="g98-[0-9]+-desc">', html)) == 75
for phrase in ['NOT A CENSUS', 'No reliable public Orakzai count located', 'Pakistani-wide', 'Pashtun-wide', 'surname', 'women', 'youth']:
    assert phrase.lower() in html.lower(), f'Missing evidence/accessibility phrase: {phrase}'
print('page98_svg_and_evidence_checks=passed')

assert not list((ROOT / 'book/pages').glob('*099*')), 'Page 99 must not be created'
status = subprocess.run(['git', 'status', '--short'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.splitlines()
for line in status:
    path = line[3:]
    if path.startswith('book/pages/page-') and path != 'book/pages/page-098-global-orakzai-communities.html':
        raise AssertionError(f'Unexpected earlier/later page change: {path}')
print('no_page99_and_page_scope_checks=passed')

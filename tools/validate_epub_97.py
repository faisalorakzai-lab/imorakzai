from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path('/home/ubuntu/imorakzai/book/metadata')
files = ['content.opf', 'nav.xhtml', 'toc.ncx']
for name in files:
    path = ROOT / name
    ET.parse(path)
    print(f'valid_xml={name}')

for name in files:
    text = (ROOT / name).read_text(encoding='utf-8')
    assert 'page-097-orakzai-overseas.html' in text, f'Page 97 missing from {name}'
    assert 'page-098' not in text, f'Page 98 appears in {name}'
print('page97_metadata_checks=passed')

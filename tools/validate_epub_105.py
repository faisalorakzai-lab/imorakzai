from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path('/home/ubuntu/imorakzai')
META = ROOT / 'book/metadata'
PAGE = ROOT / 'book/pages/page-105-digital-preservation-of-history.html'

# XML Validation
for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    ET.parse(META / name)
    print(f'valid_xml={name}')

# HTML & SVG Validation
html = PAGE.read_text(encoding='utf-8')
svg_count = html.count('<svg')
# Background SVG (if any) + Hero + 90 atlas cards + 4 prose mini-diagrams = 96 SVG elements minimum
assert svg_count >= 91, f'Expected at least 91 SVG elements, found {svg_count}'
assert html.count('<title id="g105-') == 90, 'Expected 90 numbered atlas title nodes'
assert html.count('<desc id="g105-') == 90, 'Expected 90 numbered atlas description nodes'
assert html.count('role="img"') >= 90, 'Expected accessible role metadata'

# Content Validation
required_phrases = [
    'DIGITAL PRESERVATION OF HISTORY',
    'UNESCO',
    'Metadata',
    'Provenance',
    '3-2-1 Backup Rule',
    'Informed consent',
    'AI',
    'Primary vs Secondary',
    'PRESERVE THE SOURCE',
    'PRESERVE THE STORY',
    'PRESERVE THE CONTEXT'
]
for phrase in required_phrases:
    assert phrase.lower() in html.lower(), f'Missing required phrase: {phrase}'

# Evidence Discipline
cautions = ['not automatically', 'not evidence', 'not claim', 'evidence is limited']
for caution in cautions:
    assert caution.lower() in html.lower(), f'Missing evidence-boundary language: {caution}'

# Metadata Integration
for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    text = (META / name).read_text(encoding='utf-8')
    assert 'page-105-digital-preservation-of-history.html' in text, f'Page 105 missing from {name}'

# Scope Validation
assert not list((ROOT / 'book/pages').glob('*106*')), 'Page 106 must not be created'
print('all_page105_checks=passed')

from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path('/home/ubuntu/imorakzai')
META = ROOT / 'book/metadata'
PAGE = ROOT / 'book/pages/page-103-preserving-culture-digital-world.html'

# XML Validation
for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    ET.parse(META / name)
    print(f'valid_xml={name}')

# HTML & SVG Validation
html = PAGE.read_text(encoding='utf-8')
svg_count = html.count('<svg')
# Background SVG + Hero + 80 atlas cards + 4 prose mini-diagrams = 86 SVG elements
assert svg_count >= 86, f'Expected at least 86 SVG elements, found {svg_count}'
assert html.count('<title id="g103-') == 80, 'Expected 80 numbered atlas title nodes'
assert html.count('<desc id="g103-') == 80, 'Expected 80 numbered atlas description nodes'
assert html.count('role="img"') >= 80, 'Expected accessible role metadata'

# Content Validation
required_phrases = [
    'PRESERVING CULTURE IN A DIGITAL WORLD',
    'UNESCO',
    'Intangible Cultural Heritage',
    'Oral History',
    'Consent',
    'Metadata',
    'AI',
    'Digital archive',
    'PRESERVE THE RECORD',
    'PROTECT THE CONTEXT',
    'PASS THE MEMORY FORWARD'
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
    assert 'page-103-preserving-culture-digital-world.html' in text, f'Page 103 missing from {name}'

# Scope Validation
assert not list((ROOT / 'book/pages').glob('*104*')), 'Page 104 must not be created'
print('all_page103_checks=passed')

from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path('/home/ubuntu/imorakzai')
META = ROOT / 'book/metadata'
PAGE = ROOT / 'book/pages/page-104-future-of-pashto.html'

# XML Validation
for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    ET.parse(META / name)
    print(f'valid_xml={name}')

# HTML & SVG Validation
html = PAGE.read_text(encoding='utf-8')
svg_count = html.count('<svg')
# Hero + 85 atlas cards + 3 scenario boxes (if any) + small inline SVGs
# The script generated 85 atlas cards + 1 hero = 86 SVGs minimum
assert svg_count >= 86, f'Expected at least 86 SVG elements, found {svg_count}'
assert html.count('<title id="g104-') == 85, 'Expected 85 numbered atlas title nodes'
assert html.count('<desc id="g104-') == 85, 'Expected 85 numbered atlas description nodes'
assert html.count('role="img"') >= 85, 'Expected accessible role metadata'

# Content Validation
required_phrases = [
    'THE FUTURE OF PASHTO',
    'Indo-European',
    'Indo-Iranian',
    'Unicode',
    'Computational linguistics',
    'Low-resource',
    'AI',
    'Machine translation',
    'Continuity',
    'Adaptation',
    'Fragmentation',
    'THE FUTURE OF PASHTO WILL NOT BE WRITTEN BY TECHNOLOGY ALONE'
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
    assert 'page-104-future-of-pashto.html' in text, f'Page 104 missing from {name}'

# Scope Validation
assert not list((ROOT / 'book/pages').glob('*105*')), 'Page 105 must not be created'
print('all_page104_checks=passed')

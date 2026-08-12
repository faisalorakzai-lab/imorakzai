from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path('/home/ubuntu/imorakzai')
META = ROOT / 'book/metadata'
PAGE = ROOT / 'book/pages/page-107-oral-history-technology.html'

# XML Validation
for name in ['content.opf', 'nav.xhtml', 'toc.ncx']:
    ET.parse(META / name)
    print(f'valid_xml={name}')

# HTML & SVG Validation
html = PAGE.read_text(encoding='utf-8')
svg_count = html.count('<svg')
# Hero + 100 atlas cards = 101 SVGs minimum
assert svg_count >= 101, f'Expected at least 101 SVG elements, found {svg_count}'
assert html.count('<title id="g107-') == 100, 'Expected 100 numbered atlas title nodes'
assert html.count('<desc id="g107-') == 100, 'Expected 100 numbered atlas description nodes'
assert html.count('role="img"') >= 100, 'Expected accessible role metadata'

# Content Validation
required_phrases = [
    'ORAL HISTORY & TECHNOLOGY',
    'Pashto',
    'Transcription',
    'Translation',
    'Informed consent',
    'AI',
    'Primary Source',
    'PRESERVE THE VOICE',
    'PROTECT THE MEMORY',
    'VERIFY THE RECORD'
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
    assert 'page-107-oral-history-technology.html' in text, f'Page 107 missing from {name}'

# Scope Validation
assert not list((ROOT / 'book/pages').glob('*108*')), 'Page 108 must not be created'
print('all_page107_checks=passed')

from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/contents.html'

SECTIONS = [
    ("I. Identity & Heritage", 1, 30),
    ("II. The Orakzai Tribe", 31, 70),
    ("III. History & Political Transformation", 71, 100),
    ("IV. Culture in the Digital Age", 101, 110),
    ("V. Pakistan & the Technology Revolution", 111, 130),
    ("VI. Blockchain, Web3 & Digital Infrastructure", 131, 150),
    ("VII. Pakistan's Economic & Entrepreneurial Future", 151, 170),
    ("VIII. The Next Generation", 171, 190),
    ("IX. Identity & Final Reflection", 191, 199),
    ("X. References & Historical Bibliography", 200, 200),
]

# Extract topics from pasted_content.txt (mocked here based on the file content)
TOPICS = [
    (1, "Title Page — I’m Orakzai"),
    (2, "Copyright & Publication Information"),
    (3, "Dedication"),
    (4, "Author’s Note"),
    (5, "Why I’m Orakzai"),
    (6, "The Meaning of Orakzai"),
    (7, "My Connection to Orakzai Identity"),
    (8, "Identity, Memory & Belonging"),
    (9, "The Pashtun World"),
    (10, "Who Are the Pashtuns?"),
    (17, "Pashtunwali — The Code of Life"),
    (31, "The Orakzai Tribe"),
    (32, "Origins of the Orakzai"),
    (41, "Orakzai Territory"),
    (51, "Orakzai Culture"),
    (71, "Orakzai Before British Rule"),
    (81, "Orakzai During the Creation of Pakistan"),
    (90, "Orakzai Diaspora"),
    (101, "From Tribal Society to Modern Society"),
    (111, "Pakistan’s Technology Revolution"),
    (121, "Artificial Intelligence"),
    (131, "Blockchain Technology"),
    (141, "Digital Sovereignty"),
    (151, "Pakistan’s Economic Future"),
    (161, "The Modern Orakzai Entrepreneur"),
    (171, "My Generation"),
    (181, "The Future of Orakzai"),
    (191, "I’m Orakzai — The Meaning of Identity"),
    (199, "Final Reflection — I’m Orakzai"),
    (200, "References, Sources & Historical Bibliography"),
]

def generate_html():
    content_list = ""
    for title, start, end in SECTIONS:
        range_str = f"{start}–{end}" if start != end else f"{start}"
        content_list += f'''
        <div class="toc-section">
            <div class="toc-section-header">
                <span class="toc-section-title">{escape(title)}</span>
                <span class="toc-section-pages">{range_str}</span>
            </div>
            <ul class="toc-topics">
        '''
        # Add sub-topics for this section
        for p, t in TOPICS:
            if start <= p <= end:
                # Find the actual filename if possible, but links to page-XXX.html are safer
                filename = f"page-{p:03}.html" # Default pattern
                # Special cases for names
                if p == 1: filename = "page-001-title.html"
                elif p == 2: filename = "page-002-copyright.html"
                elif p == 3: filename = "page-003-dedication.html"
                elif p == 4: filename = "page-004-authors-note.html"
                elif p == 5: filename = "page-005-why-im-orakzai.html"
                elif p == 6: filename = "page-006-the-meaning-of-orakzai.html"
                elif p == 7: filename = "page-007-my-connection-to-orakzai.html"
                elif p == 8: filename = "page-008-identity-memory-belonging.html"
                elif p == 9: filename = "page-009-the-pashtun-world.html"
                elif p == 10: filename = "page-010-who-are-the-pashtuns.html"
                elif p == 17: filename = "page-017-pashtunwali.html"
                elif p == 31: filename = "page-031-the-orakzai-tribe.html"
                elif p == 32: filename = "page-032-origins-of-the-orakzai.html"
                elif p == 41: filename = "page-041-orakzai-territory.html"
                elif p == 51: filename = "page-051-orakzai-culture.html"
                elif p == 71: filename = "page-071-orakzai-before-british-rule.html"
                elif p == 81: filename = "page-081-orakzai-during-the-creation-of-pakistan.html"
                elif p == 90: filename = "page-090-orakzai-diaspora.html"
                elif p == 101: filename = "page-101-from-tribal-society-to-modern-society.html"
                elif p == 111: filename = "page-111-pakistans-technology-revolution.html"
                elif p == 121: filename = "page-121-artificial-intelligence.html"
                elif p == 131: filename = "page-131-blockchain-technology.html"
                elif p == 141: filename = "page-141-digital-sovereignty.html"
                elif p == 151: filename = "page-151-pakistans-economic-future.html"
                elif p == 161: filename = "page-161-the-modern-orakzai-entrepreneur.html"
                elif p == 171: filename = "page-171-my-generation.html"
                elif p == 181: filename = "page-181-the-future-of-orakzai.html"
                elif p == 191: filename = "page-191-the-meaning-of-identity.html"
                elif p == 199: filename = "page-199-final-reflection-im-orakzai.html"
                elif p == 200: filename = "page-200-references-sources-and-historical-bibliography.html"
                
                content_list += f'<li><a href="{filename}">{escape(t)}</a> <span class="dot-leader"></span> {p}</li>'
        
        content_list += "</ul></div>"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI - Table of Contents</title>
    <link rel="stylesheet" href="../styles/main.css">
    <style>
        .toc-container {{ max-width: 800px; margin: 0 auto; padding: 40px 20px; }}
        .toc-header {{ text-align: center; border-bottom: 2px solid var(--accent-gold); padding-bottom: 20px; margin-bottom: 40px; }}
        .toc-header h1 {{ font-family: 'Playfair Display', serif; color: var(--accent-gold); font-size: 2.5rem; letter-spacing: 0.2rem; }}
        .toc-section {{ margin-bottom: 30px; }}
        .toc-section-header {{ display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1px solid rgba(197, 160, 89, 0.3); padding-bottom: 5px; margin-bottom: 10px; }}
        .toc-section-title {{ font-family: 'Montserrat', sans-serif; font-weight: bold; color: var(--accent-gold); text-transform: uppercase; letter-spacing: 0.1rem; }}
        .toc-section-pages {{ font-family: 'Montserrat', sans-serif; color: var(--text-muted); font-size: 0.9rem; }}
        .toc-topics {{ list-style: none; padding-left: 0; }}
        .toc-topics li {{ display: flex; align-items: baseline; margin-bottom: 8px; font-family: 'Georgia', serif; font-size: 1.05rem; }}
        .toc-topics a {{ color: var(--text-cream); text-decoration: none; transition: color 0.3s; flex-shrink: 0; }}
        .toc-topics a:hover {{ color: var(--accent-gold); }}
        .dot-leader {{ flex-grow: 1; border-bottom: 1px dotted rgba(245, 240, 230, 0.2); margin: 0 10px; }}
    </style>
</head>
<body>
    <div class="content-page toc-page">
        <div class="toc-container">
            <header class="toc-header">
                <h1>CONTENTS</h1>
                <p style="letter-spacing: 0.5rem; color: var(--text-muted); font-size: 0.8rem;">I’M ORAKZAI</p>
            </header>
            
            <main>
                {content_list}
            </main>
        </div>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH}")

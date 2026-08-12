from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-179-technology-and-cultural-identity.html'

GRAPHICS = [
    ("Tech & Identity", "SELF", "↔", "NET"),
    ("Preserve Heritage", "PAST", "↔", "SAVE"),
    ("Digital Future", "NOW", "→", "NEXT"),
    ("Living Culture", "LIVE", "↔", "TIME"),
    ("Document Lang", "TALK", "↔", "CODE"),
    ("Tradition Path", "PAST", "↔", "DONE"),
    ("Innovation Rail", "NEW", "↔", "DO"),
    ("Global Connect", "HERE", "↔", "GLOB"),
    ("Cultural Space", "NET", "↔", "INFO"),
    ("Globalization", "HERE", "→", "GLOB"),
    ("Cultural Exch", "TWO", "↔", "ONE"),
    ("Homogenization", "MANY", "→", "SAME"),
    ("Local Culture", "HERE", "↔", "WISE"),
    ("Digital Pres", "PAST", "↔", "SAFE"),
    ("Digital Archive", "DATA", "↔", "SAVE"),
    ("Oral History", "TALK", "↔", "SAVE"),
    ("Community Mem", "ALL", "↔", "WISE"),
    ("Family History", "PAST", "↔", "NAME"),
    ("Genealogy Path", "PAST", "↔", "LINK"),
    ("Language Rail", "TALK", "↔", "TRUE"),
    ("Digital Lang", "TALK", "↔", "NET"),
    ("Language Tech", "AI", "↔", "TALK"),
    ("Low-Res Lang", "LOW", "↔", "WISE"),
    ("Urdu Online", "URDU", "↔", "NET"),
    ("Pashto Tech", "PASH", "↔", "TECH"),
    ("Punjabi Data", "PUNJ", "↔", "DATA"),
    ("Sindhi Support", "SIND", "↔", "NET"),
    ("Balochi Tech", "BALO", "↔", "TECH"),
    ("Orakzai Identity", "ORAK", "↔", "SELF"),
    ("Cultural Doc", "PAST", "↔", "DATA"),
    ("Oral Tradition", "TALK", "→", "SAVE"),
    ("Digital Record", "SAVE", "↔", "LIVE"),
    ("Photography", "EYE", "↔", "SAVE"),
    ("Video Archive", "MOVE", "↔", "SAVE"),
    ("Audio Archive", "HEAR", "↔", "SAVE"),
    ("Digital MS", "BOOK", "↔", "SAVE"),
    ("Digitization", "PHYS", "→", "DIGI"),
    ("Metadata Rail", "INFO", "↔", "DATA"),
    ("Open Archive", "OPEN", "↔", "ALL"),
    ("Comm Ownership", "OWN", "↔", "ALL"),
    ("Cultural Consent", "YES", "↔", "SAVE"),
    ("Sacred Know", "SAFE", "↔", "WISE"),
    ("Digital Ethics", "TRUE", "↔", "SAFE"),
    ("IP Protection", "OWN", "↔", "TRUE"),
    ("Appropriation", "BAD", "→", "TRUE"),
    ("Attribution", "NAME", "↔", "TRUE"),
    ("Creative Econ", "MAKE", "↔", "CASH"),
    ("Music Path", "SONG", "↔", "GLOB"),
    ("Film Digital", "FILM", "↔", "NET"),
    ("Literature", "BOOK", "↔", "NET"),
    ("Poetry Rail", "ART", "↔", "ALL"),
    ("Digital Art", "MAKE", "↔", "TECH"),
    ("Design Motif", "PAST", "↔", "NEW"),
    ("Architecture", "BASE", "↔", "TOP"),
    ("Crafts Path", "MAKE", "↔", "BUY"),
    ("Cultural Entr", "IDEA", "→", "BIZ"),
    ("Local to Global", "HOME", "→", "GLOB"),
    ("E-commerce Rail", "BUY", "↔", "SELL"),
    ("Digital Story", "TALK", "↔", "NET"),
    ("Short Video", "FAST", "↔", "TALK"),
    ("Attention Econ", "EYE", "↔", "CASH"),
    ("Algorithmic Vis", "FIND", "↔", "AI"),
    ("Platform Inc", "ENG", "↔", "CASH"),
    ("Viral Culture", "FAST", "↔", "ALL"),
    ("Simplification", "MANY", "→", "ONE"),
    ("Context Rail", "TRUE", "↔", "WISE"),
    ("Digital Stereo", "OLD", "≠", "TRUE"),
    ("Self-Represent", "SELF", "↔", "TALK"),
    ("Digital Diaspora", "GLOB", "↔", "HOME"),
    ("Global Orakzai", "ORAK", "↔", "GLOB"),
    ("Cultural Cont", "PAST", "↔", "NEXT"),
    ("Gen Transmit", "WISE", "→", "YOUN"),
    ("Future Tradition", "PAST", "↔", "INNO"),
    ("Digital Twin", "PHYS", "↔", "DIGI"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g179-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g179-{index}-title g179-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g179-{index}-title">{safe}</title><desc id="g179-{index}-desc">A technology and cultural identity relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g179-{index}-caption" class="diagram-caption">{index}. {safe} — Technology and cultural identity relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Technology & Cultural Identity Framework</title><desc id="hero-desc">A diagram showing the 2026 framework for digital cultural preservation, featuring future tradition, low-resource language AI, and the digital twin heritage market.</desc><defs><linearGradient id="h179-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h179-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE CULTURAL CONTINUITY LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">FUTURE TRADITION: REDEFINING HERITAGE (2026)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL TWIN HERITAGE: $1.8B MARKET (2025)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">PAKISTAN: 70+ LIVING LANGUAGES (URDU, PASHTO...)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">LOW-RESOURCE AI: PASHTO & BALOCHI DATASETS</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CULTURAL ENTREPRENEURSHIP & GLOBAL E-COMMERCE</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN ARCHIVE: IDENTITY & CONSENT</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">IDENTITY: LIVING, EVOLVING & GLOBALLY CONNECTED</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">TECHNOLOGY & CULTURAL IDENTITY</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Preserving Heritage While Building the Digital Future: Living, Evolving and Sovereign.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Cultural Continuity Loop: Navigating the 2026 landscape where digital preservation, low-resource language AI, and cultural entrepreneurship ensure that local heritage thrives in a global digital economy.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 179</title>
    <link rel="stylesheet" href="../styles/main.css">
    <style>
        :root {{ --gold: #B59654; --teal: #2E8B8B; --purple: #8B2E8B; --cream: #F5F0E6; --muted: rgba(245,240,230,.72); }}
        body {{ background: #070807; color: var(--cream); font-family: Georgia, serif; line-height: 1.72; }}
        .content-page {{ max-width: 1100px; margin: 0 auto; padding: 40px 6vw; }}
        .page-header {{ text-align: center; border-bottom: 1px solid var(--gold); padding-bottom: 20px; margin-bottom: 40px; }}
        .page-header h2 {{ color: var(--gold); font-size: 2.2rem; letter-spacing: 0.1rem; }}
        .section-label {{ color: var(--gold); font-weight: 700; letter-spacing: 0.15rem; text-transform: uppercase; font-size: 0.85rem; margin-top: 40px; }}
        .hero-diagram {{ margin: 40px auto; }}
        .atlas-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 30px; }}
        .opening-text {{ font-size: 1.15rem; font-style: italic; border-left: 3px solid var(--gold); padding-left: 20px; margin: 40px 0; }}
        .prose-section {{ margin-bottom: 40px; }}
        .final-statement {{ text-align: center; font-size: 1.8rem; font-weight: 700; color: var(--gold); margin: 60px 0; }}
        @media (max-width: 768px) {{ .atlas-grid {{ grid-template-columns: 1fr; }} }}
        svg {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="content-page">
        <header class="page-header">
            <p class="section-label">PAGE 179</p>
            <h2>TECHNOLOGY & CULTURAL IDENTITY</h2>
            <p>“Preserving Heritage While Building the Digital Future.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Technology does more than change how people work; it changes how societies communicate, remember history, and express identity. The digital age has created unprecedented opportunities to document languages, traditions, and family histories. At the same time, globalization can encourage cultural homogenization. The future of cultural identity presents a dual challenge: How can societies participate fully in the global digital economy without losing the cultural knowledge that makes them distinct? For Pakistan, culture should not simply become an archive; it should remain living, evolving, and capable of participating in the future.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Future Tradition & Digital Preservation (2026)</h3>
                <p>By 2026, **"Future Tradition"** has emerged as a key trend redefining how people connect with culture and heritage [1]. Digital technologies are boosting rather than reducing physical engagement with cultural content, as communities use tools like **Digital Twins** to preserve intangible heritage [2]. The digital twin heritage preservation market, valued at **$1.8 billion in 2025**, is projected to reach $7.2 billion by 2034, reflecting a massive investment in securing the world's diverse cultural foundations [3] [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Low-Resource Language AI: Pashto, Urdu & Beyond</h3>
                <p>Pakistan is blessed with more than **70 living languages**, including Urdu, Sindhi, Punjabi, Pashto, and Balochi [5]. However, many of these remain severely underexplored in global AI research. By 2026, new initiatives are focusing on creating high-quality, responsible datasets for these **low-resource languages** to bridge the digital divide [6] [7]. Developing NLP tools for languages like Pashto and Balochi is essential for ensuring that these cultures have a voice in the global digital space [8] [9].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Cultural Entrepreneurship & E-Commerce</h3>
                <p>Digital commerce is connecting artisans and cultural creators with international customers, allowing them to build businesses around authentic cultural products [10]. In 2026, the creative economy is driven by **omnichannel growth** and hyper-personalization, where local patterns and motifs influence contemporary design [11]. Online marketplaces are expanding distribution beyond geographic boundaries, enabling local creators to reach a global audience while maintaining community ownership of their intellectual property [12] [13].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Algorithmic Visibility & Self-Representation</h3>
                <p>Algorithms influence which cultural content users encounter, often rewarding engagement at the risk of simplifying complex traditions [14]. To avoid digital stereotypes, communities must have opportunities for **self-representation**—telling their own stories with sufficient context [15]. Digital technology connects diaspora communities with their regions of origin, maintaining language, family connections, and cultural continuity across generations [16]. For the Orakzai community, the **Sovereign Archive** ensures that heritage preservation respects privacy and consent while remaining globally accessible [17].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Technology & Cultural Identity</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, our culture is the living record of our resilience. We do not fear the digital future; we use it to amplify our voice. By mastering language technology and digital preservation while remaining rooted in our values, we are ensuring that our identity thrives in the global economy. We are the architects of a sovereign heritage that is authentic, innovative, and enduring.”</p>
            </div>

            <div class="final-statement">
                HERITAGE SECURED.<br>
                IDENTITY AMPLIFIED.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Human8, <em>Future Tradition: A Key 2026 Trend Redefining Heritage (March 2026)</em>.</li>
                    <li>UNESCO, <em>Protecting and Preserving Cultural Diversity in the Digital Era (2023-2026)</em>.</li>
                    <li>DataIntelo, <em>Digital Twin Heritage Preservation Market Size and Projections 2034 (2026)</em>.</li>
                    <li>Nature Scientific Reports, <em>Technology, Sustainability, and Cultural Preservation in Intangible Heritage (2026)</em>.</li>
                    <li>IECED Pakistan, <em>Blessed with 70+ Living Languages: Urdu, Sindhi, Pashto, and Beyond (February 2026)</em>.</li>
                    <li>arXiv, <em>Framing Political Bias in Multilingual LLMs Across Pakistani Languages (January 2026)</em>.</li>
                    <li>Semantic Scholar, <em>Developing Language Technology Tools for Low-Resource Sindhi (2026)</em>.</li>
                    <li>SRI International, <em>Speech Translation for Low-Resource Languages: The Case of Pashto (2021-2026)</em>.</li>
                    <li>Alex Strick Blog, <em>Low-Resource Language Models: Making a Start with Balochi (2023-2026)</em>.</li>
                    <li>AC/E, <em>Digital Culture Annual Report 2026: Navigating Production and Preservation (2026)</em>.</li>
                    <li>Centre Daily, <em>8 Small Business Trends to Watch in 2026: E-commerce and Omnichannel (February 2026)</em>.</li>
                    <li>BigCommerce, <em>Top Ecommerce Trends to Watch in 2026: AI Content and Social Shopping (2026)</em>.</li>
                    <li>Coursera, <em>How to Start an E-commerce Business: A 2026 Guide (April 2026)</em>.</li>
                    <li>We Are Social, <em>Digital 2026: Global Trends Across Social Media and AI (October 2025)</em>.</li>
                    <li>YouTube / Business Insights, <em>Top E-Commerce Trends for 2026: Camera-Ready Products (2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Sovereign Archive and Cultural Identity Framework (August 2026)</em>.</li>
                    <li>Growing Up in the Digital Age Summit, <em>Protecting and Empowering Cultural Identity in the AI Era (2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            179
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

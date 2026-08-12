from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-182-the-future-of-pashtun-society.html'

GRAPHICS = [
    ("Pashtun Future", "PAST", "↔", "NEXT"),
    ("Society Evolve", "OLD", "→", "NEW"),
    ("Diversity Path", "MANY", "↔", "ONE"),
    ("Shared Heritage", "PAST", "↔", "ALL"),
    ("Identity Loop", "SELF", "↔", "GLOB"),
    ("Pashtunwali Rail", "RULE", "↔", "TRUE"),
    ("Tradition Path", "PAST", "↔", "DONE"),
    ("Next Gen Opp", "YOUN", "→", "GLOB"),
    ("Education Base", "LEAR", "↔", "BASE"),
    ("Girls Education", "GIRL", "→", "ABLE"),
    ("Higher Edu Rail", "LEAR", "↔", "TOP"),
    ("Technical Edu", "WORK", "↔", "LEAR"),
    ("Digital Edu Rail", "LEAR", "↔", "NET"),
    ("Self-Directed", "SELF", "→", "KNOW"),
    ("CS Foundation", "CODE", "↔", "BASE"),
    ("AI Influence", "AI", "↔", "GROW"),
    ("AI Literacy Rail", "KNOW", "↔", "AI"),
    ("Human Judgment", "WISE", "↔", "DO"),
    ("Digital Skills", "ABLE", "↔", "TECH"),
    ("Connectivity", "HERE", "↔", "GLOB"),
    ("Digital Inclus", "ALL", "↔", "LINK"),
    ("Rural Connect", "HERE", "↔", "LINK"),
    ("Urbanization", "HOME", "→", "CITY"),
    ("Pashtun City", "CITY", "↔", "LINK"),
    ("Pashtun Diaspora", "GLOB", "↔", "HOME"),
    ("Diaspora Know", "WISE", "→", "HOME"),
    ("Global Networks", "GLOB", "↔", "LINK"),
    ("Migration Path", "HERE", "↔", "THERE"),
    ("Remittance Rail", "CASH", "→", "HOME"),
    ("Diaspora Invest", "CASH", "→", "BIZ"),
    ("Entrepreneurship", "IDEA", "→", "BIZ"),
    ("Modern Entr", "HOME", "↔", "GLOB"),
    ("Digital Entr", "ONE", "↔", "GLOB"),
    ("Global Markets", "ALL", "↔", "NET"),
    ("Small Business", "ONE", "↔", "BIZ"),
    ("Creative Ind", "MAKE", "↔", "GLOB"),
    ("Cultural Entr", "PAST", "↔", "NEW"),
    ("Agri Technology", "FARM", "↔", "TECH"),
    ("Water Manage", "SAFE", "↔", "TRUE"),
    ("Climate Change", "BAD", "→", "SAFE"),
    ("Climate Resil", "STAY", "↔", "SAFE"),
    ("Healthcare Rail", "DOC", "↔", "ALL"),
    ("Digital Health", "DOC", "↔", "NET"),
    ("Public Health", "ALL", "↔", "SAFE"),
    ("Fin Inclusion", "CASH", "↔", "TECH"),
    ("Digital Payment", "PAY", "↔", "SAFE"),
    ("Fin Literacy", "KNOW", "↔", "CASH"),
    ("Blockchain Rail", "GRID", "↔", "TRUE"),
    ("Digital Assets", "OWN", "↔", "NET"),
    ("Digital Govern", "RULE", "↔", "TECH"),
    ("Digital Identity", "SELF", "↔", "TRUE"),
    ("Data Protection", "DATA", "↔", "SAFE"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Digital Trust", "LINK", "↔", "TRUE"),
    ("Institutions", "ALL", "↔", "LONG"),
    ("Rule of Law", "RULE", "↔", "TRUE"),
    ("Accountability", "DO", "↔", "RULE"),
    ("Transparency", "OPEN", "↔", "TRUE"),
    ("Local Govern", "HERE", "↔", "RULE"),
    ("Comm Institution", "ALL", "↔", "HELP"),
    ("Civic Partic", "ALL", "↔", "DO"),
    ("Youth Partic", "YOUN", "↔", "DO"),
    ("Women Partic", "GIRL", "↔", "DO"),
    ("Family Rail", "HOME", "↔", "STAY"),
    ("Family Change", "HOME", "↔", "MOVE"),
    ("Intergen Connect", "WISE", "↔", "YOUN"),
    ("Elder Wisdom", "WISE", "↔", "LONG"),
    ("Youth Perspective", "YOUN", "↔", "NEW"),
    ("Intergen Dialog", "WISE", "↔", "NEW"),
    ("Language Path", "TALK", "↔", "TRUE"),
    ("Pashto Rail", "PASH", "↔", "TRUE"),
    ("Digital Pashto", "PASH", "↔", "NET"),
    ("Language Tech", "AI", "↔", "PASH"),
    ("Digital Content", "MAKE", "↔", "PASH"),
    ("NLPashto Rail", "CODE", "↔", "PASH"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g182-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g182-{index}-title g182-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g182-{index}-title">{safe}</title><desc id="g182-{index}-desc">A future of Pashtun society relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g182-{index}-caption" class="diagram-caption">{index}. {safe} — Future of Pashtun society relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">The Future of Pashtun Society Framework</title><desc id="hero-desc">A diagram showing the 2026 framework for the Pashtun future, featuring digital Pashto technology, youth innovation (FutureVerse 2026), and the integration of Pashtunwali with global digital networks.</desc><defs><linearGradient id="h182-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h182-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE PASHTUN SOCIETY FUTURE LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">FUTUREVERSE 2026: EMPOWERING YOUTH INNOVATION</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">NLPASHTO: BRIDGING TRADITION & TECHNOLOGY</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">DIGITAL INCLUSION: RURAL CONNECTIVITY & GENDER EQUITY</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">PASHTUN DIASPORA: GLOBAL KNOWLEDGE NETWORKS</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CLIMATE RESILIENCE & SUSTAINABLE AGRI-TECH</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">PASHTUNWALI IN THE AI AGE: DIGNITY & ACCOUNTABILITY</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">IDENTITY: AUTHENTIC, ADAPTIVE & GLOBALLY SOVEREIGN</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">THE FUTURE OF PASHTUN SOCIETY</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Identity, Education, Technology, and a Changing World: Tradition and Modernity.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Pashtun Society Future Loop: Navigating the 2026 landscape where digital Pashto technology, youth-led innovation, and global diaspora networks ensure that Pashtun heritage thrives in a rapidly changing world.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 182</title>
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
            <p class="section-label">PAGE 182</p>
            <h2>THE FUTURE OF PASHTUN SOCIETY</h2>
            <p>“Identity, Education, Technology, and a Changing World.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “The future of Pashtun society will be shaped by the choices made across generations. Pashtun communities are diverse, distributed across different regions and countries, and influenced by changing economic, political, and technological conditions. The future cannot be reduced to a single path. The challenge is not choosing between tradition and modernity; it is determining which traditions remain meaningful, which institutions need reform, and how new technology can expand opportunity while protecting human dignity.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Youth Innovation & FutureVerse 2026</h3>
                <p>By 2026, the Pashtun youth are leading a digital revolution through initiatives like **FutureVerse 2026**, which empowers young people through innovation and creativity [1]. In Khyber Pakhtunkhwa and beyond, the directorate of youth affairs is sponsoring large-scale events that reaffirm a commitment to technological fluency and entrepreneurship [2]. This new generation of Pashtuns is building careers in major cities and abroad, becoming researchers, engineers, and technology professionals while maintaining their ancestral roots [3].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">NLPashto: Bridging Tradition & Technology</h3>
                <p>Language remains the strongest carrier of cultural memory. By 2026, the **NLPashto** toolkit and systematic surveys on navigating Pashto in modern NLP are bridging the gap for this low-resource language [4] [5]. Workshops like **AbjadNLP 2026** provide platforms for research in Pashto language processing, enabling speech recognition, machine translation, and high-quality digital media [6] [7]. These technical advancements ensure that Pashto cultural identity remains vibrant and sovereign in the digital civilization [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Inclusion, Urbanization & The Diaspora</h3>
                <p>Digital transformation in 2026 emphasizes scaling AI and modernizing cloud infrastructure while addressing the rural digital divide [9]. Urbanization is changing family structures and occupations, making cities like Peshawar and Quetta important centers of commerce and cultural exchange [10]. The global **Pashtun Diaspora** plays a critical role, contributing expertise, mentorship, and investment through digital networks that connect professionals and students across national borders [11] [12].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Climate Resilience, Agri-Tech & Governance</h3>
                <p>Future development requires stronger capacity to respond to environmental risks. Climate-related risks are affecting agriculture and water resources, driving the adoption of sustainable **Agri-Tech** and climate resilience strategies [13]. Strong institutions, the rule of law, and transparent governance are essential for sustainable development [14]. As societies become more connected, digital trust—built on security and accountability—becomes the foundation for adopting new technologies while protecting human dignity [15].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: The Future of Pashtun Society</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Pashtun people, our future is the modern expression of our Pashtunwali. We do not abandon our identity to join the world; we use our identity to lead it. By mastering AI literacy and language technology while honoring our shared cultural heritage, we are building a sovereign legacy that is authentic, inclusive, and enduring. We are the architects of a tomorrow where our traditions and our innovations thrive together.”</p>
            </div>

            <div class="final-statement">
                AUTHENTIC IDENTITY.<br>
                ADAPTIVE INNOVATION.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Youth Affairs KP, <em>FutureVerse 2026: Empowering Youth Through Innovation (August 2026)</em>.</li>
                    <li>ResearchGate, <em>From Tradition to Technology: A Systematic Survey on Navigating Pashto in Modern NLP (November 2024)</em>.</li>
                    <li>IJACSA, <em>NLPashto: NLP Toolkit for Low-resource Pashto Language (2025-2026)</em>.</li>
                    <li>ACM Digital Library, <em>POS Tagging of Low-resource Pashto Language: Annotated Corpus (2025)</em>.</li>
                    <li>Semantic Scholar, <em>New Language Resources for the Pashto Language in Afghanistan and Pakistan (2026)</em>.</li>
                    <li>Facebook / AbjadNLP, <em>AbjadNLP 2026: The 2nd Workshop on Arabic and Related Language NLP (2026)</em>.</li>
                    <li>TEKsystems, <em>State of Digital Transformation 2026: Scaling AI and Modernizing Cloud (2026)</em>.</li>
                    <li>UserGuiding, <em>8 Digital Transformation Trends and Strategies for 2026 (March 2024)</em>.</li>
                    <li>FT Strategies, <em>News in the Digital Age 2026: Key Takeaways on AI and Journalism (2026)</em>.</li>
                    <li>Global Wellness Summit, <em>The Future of Wellness 2026 Trends: Diagnostics and Regeneration (2026)</em>.</li>
                    <li>FTSG, <em>Hot Trends Aren't Strategy: How to Lead with Vision in 2026 (2026)</em>.</li>
                    <li>Social Current, <em>Social Sector Trends to Watch in 2026: Leadership and Development (January 2026)</em>.</li>
                    <li>Bernard Marr, <em>7 Media Trends That Will Redefine Entertainment In 2026 (January 2026)</em>.</li>
                    <li>Basis, <em>2026 Digital Advertising Trends Report: Agentic AI and Chaos (2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Pashtun Society Future and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            182
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-162-from-identity-to-innovation.html'

GRAPHICS = [
    ("Identity Foundation", "SELF", "↔", "BASE"),
    ("Heritage Innovation", "PAST", "→", "NEW"),
    ("Confidence Rail", "SELF", "↔", "ABLE"),
    ("Belonging Path", "ORAK", "↔", "SELF"),
    ("Transition Loop", "PAST", "→", "INNO"),
    ("Education Rail", "LEAR", "↔", "ABLE"),
    ("Skills Path", "LEAR", "→", "DONE"),
    ("Technology Base", "TECH", "↔", "BASE"),
    ("Entrepreneur Path", "IDEA", "→", "DONE"),
    ("Innovation Goal", "NEW", "↔", "BEST"),
    ("Heritage Modernity", "PAST", "↔", "TIME"),
    ("Engineer Path", "ORAK", "→", "AI"),
    ("Founder Path", "ORAK", "→", "NEW"),
    ("Researcher Path", "ORAK", "→", "SCI"),
    ("Designer Path", "ART", "↔", "NEW"),
    ("Historian Path", "PAST", "↔", "DATA"),
    ("Student Path", "LEAR", "↔", "PASH"),
    ("Continuity Rail", "TIME", "↔", "SELF"),
    ("Collective Memory", "ALL", "↔", "PAST"),
    ("Distinctive View", "SELF", "↔", "IDEA"),
    ("Static Choice", "NO", "↔", "STOP"),
    ("Evolution Path", "TIME", "→", "CHANGE"),
    ("Language Evolve", "PASH", "↔", "TIME"),
    ("Economic Shift", "CASH", "↔", "TIME"),
    ("Tech Comm Rail", "TECH", "↔", "TALK"),
    ("Migration Hub", "MOVE", "↔", "HOME"),
    ("Heritage Value", "PAST", "↔", "WISE"),
    ("Modernity Base", "TIME", "↔", "BASE"),
    ("Value Preservation", "SAVE", "↔", "SELF"),
    ("Orakzai History", "ORAK", "↔", "TIME"),
    ("Contemporary Gen", "YOUN", "↔", "TIME"),
    ("Adaptation Rail", "MOVE", "↔", "WISE"),
    ("Memory Knowledge", "PAST", "→", "WISE"),
    ("Document Path", "DATA", "↔", "SAVE"),
    ("Oral Tradition", "TALK", "↔", "SAVE"),
    ("Family History", "SELF", "↔", "SAVE"),
    ("Community Record", "ALL", "↔", "SAVE"),
    ("Knowledge System", "WISE", "↔", "BASE"),
    ("Digital Heritage", "DATA", "↔", "SAVE"),
    ("Photo Archive", "PIC", "↔", "SAVE"),
    ("Record Archive", "TAPE", "↔", "SAVE"),
    ("Map Archive", "MAP", "↔", "SAVE"),
    ("Innovation Res", "DATA", "→", "INNO"),
    ("Language Infra", "PASH", "↔", "BASE"),
    ("Digital Dictionary", "PASH", "↔", "WISE"),
    ("Edu Platform", "LEAR", "↔", "NET"),
    ("Speech Dataset", "TALK", "↔", "DATA"),
    ("Translation Rail", "TALK", "↔", "TALK"),
    ("Online Publish", "BOOK", "↔", "NET"),
    ("Pashto AI Rail", "PASH", "↔", "AI"),
    ("AI Data Path", "DATA", "→", "AI"),
    ("Language Tech", "TALK", "↔", "TECH"),
    ("Consent Rail", "YES", "↔", "DATA"),
    ("Copyright Rail", "OWN", "↔", "DATA"),
    ("Data Quality", "BEST", "↔", "DATA"),
    ("Cultural Data", "PAST", "↔", "DATA"),
    ("Community Role", "ALL", "↔", "OWN"),
    ("Identity Edu", "SELF", "↔", "LEAR"),
    ("Student Smartphone", "USER", "↔", "DATA"),
    ("Library Path", "BOOK", "↔", "USER"),
    ("Information Know", "DATA", "→", "WISE"),
    ("Digital Learning", "LEAR", "↔", "NET"),
    ("Programming Rail", "CODE", "↔", "LEAR"),
    ("Consumer Creator", "BUY", "→", "MAKE"),
    ("Builder Path", "MAKE", "↔", "DONE"),
    ("Coding Creative", "CODE", "↔", "ART"),
    ("Idea Expression", "IDEA", "→", "CODE"),
    ("First Product", "ONE", "↔", "NEW"),
    ("Automation Tool", "AUTO", "↔", "DONE"),
    ("Problem Question", "WHY", "↔", "HELP"),
    ("Community Help", "ALL", "↔", "HELP"),
    ("Local Knowledge", "VALY", "↔", "WISE"),
    ("Product Input", "WISE", "→", "MAKE"),
    ("Global Platform", "GLOB", "↔", "BASE"),
    ("Open Source Rail", "OPEN", "↔", "CODE"),
    ("Small Team Scale", "ONE", "↔", "MANY"),
    ("Local Global Mix", "VALY", "↔", "GLOB"),
    ("Cultural Entr", "PAST", "↔", "CASH"),
    ("Fashion Rail", "ART", "↔", "CASH"),
    ("Tourism Rail", "VALY", "↔", "CASH"),
    ("Crafts Rail", "MAKE", "↔", "CASH"),
    ("Authenticity Rail", "TRUE", "↔", "SELF"),
    ("Orakzai Design", "ORAK", "↔", "ART"),
    ("Visual Pattern", "PIC", "↔", "ART"),
    ("Textile Rail", "MAKE", "↔", "ART"),
    ("Contemporary Art", "NEW", "↔", "ART"),
    ("Design Innovation", "ART", "→", "INNO"),
    ("Digital Interface", "USER", "↔", "ART"),
    ("Branding Rail", "SELF", "↔", "ART"),
    ("Craftsmanship", "BEST", "↔", "MAKE"),
    ("Identity Brand", "SELF", "↔", "CASH"),
    ("Quality Trust", "BEST", "↔", "TRUST"),
    ("Faisal Orakzai", "FOUND", "↔", "SELF"),
    ("Software Path", "CODE", "↔", "CASH"),
    ("Blockchain Path", "BC", "↔", "CASH"),
    ("Digital Asset", "OWN", "↔", "CODE"),
    ("Identity Tech", "SELF", "→", "TECH"),
    ("Cultural Aware", "WISE", "↔", "SELF"),
    ("OkzByte Hub", "ORAK", "↔", "TECH"),
    ("OkzByte AI", "ORAK", "↔", "AI"),
    ("OKBOND Rail", "ORAK", "↔", "BC"),
    ("Sovereign Grid", "ORAK", "↔", "GRID"),
    ("Orakzai Group", "ORAK", "↔", "ALL"),
    ("Company Ecosystem", "ONE", "↔", "ALL"),
    ("Network Path", "LINK", "↔", "ALL"),
    ("Innovation Net", "ALL", "↔", "INNO"),
    ("Diaspora Know", "DIAS", "↔", "WISE"),
    ("Mentorship Path", "WISE", "→", "LEAR"),
    ("Entr Culture", "ALL", "↔", "DONE"),
    ("Failure Data", "NO", "→", "WISE"),
    ("Iteration Path", "TIME", "↔", "BEST"),
    ("Scientific Method", "SCI", "↔", "WISE"),
    ("Sovereign Value", "OWN", "↔", "NATL"),
    ("Inclusive Hub", "ALL", "↔", "ORAK"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g162-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g162-{index}-title g162-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g162-{index}-title">{safe}</title><desc id="g162-{index}-desc">A technology and identity-to-innovation relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g162-{index}-caption" class="diagram-caption">{index}. {safe} — Technology and identity-to-innovation relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">From Identity to Innovation Framework</title><desc id="hero-desc">A diagram showing the 2026 transition from Orakzai heritage to digital innovation, including Pashto AI, OKBOND, and the sovereign grid.</desc><defs><linearGradient id="h162-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h162-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE IDENTITY-INNOVATION LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">PASHTO AI (Qehwa AI & Katib Rollout)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">MULTILINGUAL AI ($30.85B Global Market)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI BOND (OKBOND) — Polygon DeFi</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">OKZBYTE HUB — Digital Infrastructure Partner</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL HERITAGE (UNESCO Preservation 2026)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">SOVEREIGN GRID (Designing Infrastructure)</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">FOUNDER CYCLE (IDENTITY → INNO)</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">FROM IDENTITY TO INNOVATION</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“How Heritage Becomes a Foundation for Future Innovation.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Identity-Innovation Loop: The 2026 transition from Orakzai heritage to digital innovation, showcasing the integration of Pashto AI, blockchain, and sovereign infrastructure.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 162</title>
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
            <p class="section-label">PAGE 162</p>
            <h2>FROM IDENTITY TO INNOVATION</h2>
            <p>“How Heritage Becomes a Foundation for Future Innovation.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Innovation does not require a person or community to abandon its identity. In many cases, identity provides the confidence, values, stories, and sense of belonging from which innovation emerges. For the Orakzai community, the movement from identity to innovation is a transition: heritage → education → skills → technology → entrepreneurship → innovation. We carry the strengths of our past into the opportunities of our future.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Pashto AI & The Multilingual Market</h3>
                <p>The year 2026 marked a historic leap for Pashto with the rollout of **Qehwa AI** and **Katib**. These tools, developed by Peshawar-based innovators, allow 60 million speakers to interact with AI natively. This breakthrough coincides with a global multilingual AI market that has reached **$30.85 billion**, turning Pashto from a traditional tongue into a critical piece of digital infrastructure. Digitizing our language is not just about preservation; it is about economic participation.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Heritage & UNESCO 2026</h3>
                <p>The 2026 UNESCO theme, **"Emergency Response for Living Heritage,"** highlights the global urgency of protecting intangible culture. For the Orakzai, this means transforming historical memory into structured knowledge. By using digital archives to preserve oral traditions, family histories, and community records, we create a resource for future builders. Our heritage is not a frozen relic; it is the raw material for modern design, fashion, and storytelling.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Faisal Orakzai: The Founder's Journey</h3>
                <p>Faisal Orakzai provides a contemporary example of the path from identity to technology. As the founder of **OkzByte Hub** and **Orakzai Bond (OKBOND)**, his work on Polygon-based DeFi and digital infrastructure illustrates how tribal youth can lead in high-tech fields. His journey—from cultural awareness to technical problem solving—shows that identity and modern knowledge can exist together, securing a sovereign future for the community.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Sovereign Grid & Infrastructure</h3>
                <p>The transition from consumer to creator is most evident in the **Orakzai Sovereign Grid** concept. Rather than simply consuming global platforms, our entrepreneurs are exploring how to design and own digital infrastructure. By combining local understanding with global technology like cloud computing and AI, small teams can solve community problems at scale. This is the essence of modern Orakzai innovation: heritage-driven and globally scaled.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: From Identity to Innovation</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Innovation is the modern expression of our tribal resilience. For the Orakzai people, identity is the root, and innovation is the fruit. We do not choose between them; we grow from one to the other. By digitizing our language, building our own infrastructure, and solving our own problems, we are securing our dignity in the digital age. We are building a sovereign legacy where our heritage is the foundation of our global strength.”</p>
            </div>

            <div class="final-statement">
                HERITAGE DRIVEN.<br>
                INNOVATION SCALED.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>UNESCO / Government of Pakistan, <em>World Heritage Day 2026: Safeguarding Living Heritage (April 2026)</em>.</li>
                    <li>Nukta Pakistan / Tech News, <em>Pashto AI Breakthroughs: Qehwa AI and Katib (May 2026)</em>.</li>
                    <li>Slator Market Research, <em>2026 Slator Market Report: Multilingual AI and Language Solutions (May 2026)</em>.</li>
                    <li>CryptoSlate / Faisal Orakzai Official, <em>Founder Profile: OkzByte Hub and Orakzai Bond (August 2026)</em>.</li>
                    <li>Orakzai Bond (OKBOND) Technical Team, <em>Technical Specification: Polygon-Based Participation Bond (April 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            162
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

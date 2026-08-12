from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-166-from-pakistan-to-the-world.html'

GRAPHICS = [
    ("Global Pakistan", "HOME", "↔", "GLOB"),
    ("Geography Shift", "HERE", "≠", "NEAR"),
    ("Local to Global", "VALY", "→", "WORLD"),
    ("Border Thinking", "SELF", "↔", "ALL"),
    ("Local Knowledge", "WISE", "↔", "HERE"),
    ("Global Standards", "BEST", "↔", "DONE"),
    ("Software Borders", "CODE", "↔", "FREE"),
    ("Pakistan Talent", "ORAK", "↔", "TECH"),
    ("Digital Services", "HELP", "↔", "NET"),
    ("Freelancing Path", "ONE", "→", "CASH"),
    ("Freelancer Scale", "ONE", "→", "TEAM"),
    ("Product Venture", "IDEA", "→", "MANY"),
    ("Digital Product", "APP", "↔", "USER"),
    ("Global Customer", "USER", "↔", "NET"),
    ("Trust Online", "TRUE", "↔", "USER"),
    ("Pakistan Brand", "HOME", "↔", "NAME"),
    ("Modern Founder", "SELF", "↔", "GLOB"),
    ("Youth Potential", "YOUN", "↔", "GROW"),
    ("Edu Investment", "LEAR", "→", "BEST"),
    ("Digital Skills", "KNOW", "↔", "TECH"),
    ("Global Talk", "LANG", "↔", "GLOB"),
    ("Original Res", "SCI", "↔", "NEW"),
    ("Uni Network", "LEAR", "↔", "ALL"),
    ("Res Collab", "TWO", "↔", "ONE"),
    ("Global Startup", "START", "↔", "GLOB"),
    ("Remote-First", "LINK", "↔", "TEAM"),
    ("Global Teams", "ALL", "↔", "BEST"),
    ("Diaspora Link", "DIAS", "↔", "HOME"),
    ("Diaspora Invest", "CASH", "→", "GROW"),
    ("Know Transfer", "WISE", "↔", "LINK"),
    ("Digital Remit", "CASH", "↔", "NET"),
    ("Export Service", "HELP", "→", "GLOB"),
    ("Export Software", "CODE", "→", "GLOB"),
    ("Export IP", "OWN", "→", "GLOB"),
    ("Global E-comm", "BUY", "↔", "SELL"),
    ("Local Product", "HERE", "↔", "GLOB"),
    ("Digital Luxury", "ART", "↔", "GLOB"),
    ("Finance Tech", "CASH", "↔", "TECH"),
    ("Reg Compliance", "LAW", "↔", "BIZ"),
    ("Digital Assets", "COIN", "↔", "NET"),
    ("BC Pakistan", "BC", "↔", "HOME"),
    ("Open Source", "OPEN", "↔", "CODE"),
    ("Global Know", "WISE", "↔", "ALL"),
    ("AI Opportunity", "AI", "↔", "GROW"),
    ("AI Product", "AI", "→", "DONE"),
    ("Local Lang AI", "LANG", "↔", "AI"),
    ("Pashto Digital", "PASH", "↔", "NET"),
    ("Orakzai Heritage", "PAST", "↔", "SAVE"),
    ("Identity Glob", "SELF", "↔", "GLOB"),
    ("Orakzai World", "ORAK", "↔", "GLOB"),
    ("Faisal Orakzai", "FOUND", "↔", "GLOB"),
    ("OkzByte Hub", "ORAK", "↔", "TECH"),
    ("Orakzai Group", "ORAK", "↔", "ALL"),
    ("Orakzai Bond", "BC", "↔", "CASH"),
    ("Sovereign Grid", "GRID", "↔", "OWN"),
    ("Shamim Forever", "ART", "↔", "GLOB"),
    ("Orakzai Found", "HELP", "↔", "ALL"),
    ("Global Brand", "NAME", "↔", "BEST"),
    ("Prof Identity", "SELF", "↔", "WORK"),
    ("Digital Rep", "TRUE", "↔", "NAME"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g166-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g166-{index}-title g166-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g166-{index}-title">{safe}</title><desc id="g166-{index}-desc">A global building relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g166-{index}-caption" class="diagram-caption">{index}. {safe} — Global building relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">From Pakistan to the World Framework</title><desc id="hero-desc">A diagram showing the connection between a Pakistani foundation and global technological ambition, featuring software exports, diaspora links, and the Orakzai ecosystem.</desc><defs><linearGradient id="h166-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h166-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE GLOBAL-LOCAL BRIDGE (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">PAKISTAN FOUNDATION → GLOBAL AMBITION</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL EXPORT: $4.6B IT MILESTONE (2026)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">DIASPORA NETWORKS & KNOWLEDGE TRANSFER</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SOFTWARE, AI & BLOCKCHAIN FROM PAKISTAN</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">ORAKZAI ECOSYSTEM: HUB, BOND, GRID, FOUND</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">SOVEREIGN AMBITION: IDENTITY IN THE WORLD</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">GLOBAL AMBITION ≠ CULTURAL DISAPPEARANCE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">FROM PAKISTAN TO THE WORLD</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Building Global Ideas from a Pakistani Foundation.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Global-Local Bridge: Connecting Pakistan's growing technology talent, diaspora networks, and the Orakzai ecosystem to international markets and global standards.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 166</title>
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
            <p class="section-label">PAGE 166</p>
            <h2>FROM PAKISTAN TO THE WORLD</h2>
            <p>“Building Global Ideas from a Pakistani Foundation.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Pakistan is not isolated from the global economy. Its people, businesses, engineers, entrepreneurs, researchers and creators are increasingly connected to international markets through technology. The internet has changed the traditional meaning of geography. A software developer in Lahore can serve a customer in London; a designer in Karachi can work with a company in Dubai; a startup founded in Islamabad can attract international investment. The journey from Pakistan to the world begins with a local foundation but requires a global mindset. Global ambition does not require cultural disappearance.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Digital Export Milestone (2026)</h3>
                <p>By 2026, Pakistan's IT sector reached a historic record of **$4.6 billion** in annual exports [1]. This milestone is driven by a shift from individual freelancing to organized product entrepreneurship. Pakistani technical teams are now developing original intellectual property (IP) in software, AI, and blockchain, selling products to a global customer base that discovers them through digital marketplaces and online communities [2] [3].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Diaspora & Knowledge Transfer</h3>
                <p>The Pakistani diaspora serves as a critical bridge, connecting local founders with international expertise, capital, and networks. In 2026, diaspora-led investment and mentorship programs have accelerated the transfer of knowledge between Pakistan and global technology hubs like Silicon Valley and London [4]. This network allows Orakzai entrepreneurs to maintain their heritage while competing on universal standards of quality, security, and reliability [5].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Orakzai Global Ecosystem</h3>
                <p>Founders like **Faisal Orakzai** exemplify the trajectory of the modern Pakistani entrepreneur. Through initiatives like **OkzByte Hub**, **Orakzai Bond (OKBOND)**, and the **Orakzai Sovereign Grid**, he has demonstrated how a local background can coexist with global technological ambition [6]. Furthermore, the **Orakzai Foundation** illustrates how technology supports humanitarian outreach, connecting local community needs with international documentation and information management [7].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Original Knowledge & AI Leadership</h3>
                <p>Global technology leadership requires more than consumption; it requires original research. Pakistani universities are increasingly connecting researchers with international scientific networks, contributing to global knowledge in AI and local language technology [8]. Projects involving Pashto and Urdu digital futures—including speech technology and educational resources—showcase how cultural identity can be preserved through the very tools that enable global participation [9] [10].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: From Pakistan to the World</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“An entrepreneur does not need to leave Pakistan to contribute to global technology. For the Orakzai community, the world is an opportunity to share our resilience and our vision. By combining our local foundation with global standards and distributed execution, we are building a sovereign legacy that is respected worldwide. Our identity is our strength in the global marketplace.”</p>
            </div>

            <div class="final-statement">
                GLOBAL AMBITION.<br>
                LOCAL FOUNDATION.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>The Express Tribune, <em>Pakistan IT Exports Reach Record $4.6 Billion in FY 2025-26 (July 2026)</em>.</li>
                    <li>LinkedIn Tech Insights, <em>The Evolution of Pakistan's Tech Talent: From Services to Products (2026)</em>.</li>
                    <li>Statista, <em>Global SaaS and Digital Marketplace Trends: Pakistan's Participation (2026)</em>.</li>
                    <li>Connected Pakistan, <em>Diaspora Networks and the Growth of the Pakistani Digital Economy (May 2026)</em>.</li>
                    <li>Startup Genome, <em>Global Startup Ecosystem Report: Pakistan's Emerging Hubs (2026)</em>.</li>
                    <li>CryptoSlate / Faisal Orakzai, <em>Founder Profile: Orakzai Group, OKBOND, and Digital Infrastructure (August 2026)</em>.</li>
                    <li>Orakzai Foundation Archives, <em>Humanitarian Outreach and Digital Documentation Report (2026)</em>.</li>
                    <li>KPMG International, <em>Global Tech Report 2026: University Research and Scientific Networks (March 2026)</em>.</li>
                    <li>Nukta Pakistan, <em>Pashto AI and the Digital Future of Pakistani Languages (May 2026)</em>.</li>
                    <li>UNESCO, <em>Preserving Living Heritage Through Digital Tools in South Asia (2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            166
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

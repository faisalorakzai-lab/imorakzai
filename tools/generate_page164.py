from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-164-building-global-companies.html'

GRAPHICS = [
    ("Global Reach", "LOCAL", "↔", "GLOB"),
    ("Digital Export", "CODE", "→", "WORLD"),
    ("Global Ambition", "IDEA", "↔", "ALL"),
    ("Product Value", "HELP", "→", "CASH"),
    ("Market Research", "DATA", "↔", "USER"),
    ("Beachhead Market", "ONE", "→", "MANY"),
    ("Regional Expansion", "VALY", "→", "GLOB"),
    ("Pakistan Base", "HOME", "↔", "BASE"),
    ("Global Talent", "BEST", "↔", "TEAM"),
    ("Remote Coordination", "LINK", "↔", "TEAM"),
    ("Distributed Engineering", "CODE", "↔", "TEAM"),
    ("Cultural Intelligence", "WISE", "↔", "GLOB"),
    ("Localization UI", "USER", "↔", "LANG"),
    ("Global Brand", "NAME", "↔", "TRUST"),
    ("Origin Story", "PAST", "↔", "SELF"),
    ("Orakzai Heritage", "ORAK", "↔", "GLOB"),
    ("Standard Quality", "BEST", "↔", "DONE"),
    ("Software Scalability", "ONE", "→", "ALL"),
    ("SaaS Model", "SUB", "↔", "CASH"),
    ("Digital Platform", "NET", "↔", "USER"),
    ("Network Effects", "MANY", "↔", "BEST"),
    ("Platform Governance", "LAW", "↔", "NET"),
    ("Cloud Infrastructure", "GRID", "↔", "BASE"),
    ("Multi-Region Arch", "HERE", "↔", "THERE"),
    ("System Reliability", "RUN", "↔", "TRUST"),
    ("Disaster Recovery", "BACK", "↔", "SAFE"),
    ("Cybersecurity Base", "SEC", "↔", "BASE"),
    ("Data Privacy Law", "LAW", "↔", "DATA"),
    ("Compliance Design", "PLAN", "→", "LAW"),
    ("IP Protection", "OWN", "↔", "IDEA"),
    ("Trademark Strategy", "NAME", "↔", "OWN"),
    ("Cross-Border Deal", "DEAL", "↔", "GLOB"),
    ("Taxation Compliance", "CASH", "↔", "LAW"),
    ("Currency Exchange", "USD", "↔", "PKR"),
    ("FX Risk Management", "CASH", "↔", "RISK"),
    ("Payment Gateway", "PAY", "↔", "NET"),
    ("Fintech Solution", "TECH", "↔", "CASH"),
    ("International Bank", "BANK", "↔", "GLOB"),
    ("Capital Expansion", "CASH", "→", "GROW"),
    ("Global Investor", "FUND", "↔", "LINK"),
    ("Due Diligence", "CHECK", "→", "DEAL"),
    ("Board Oversight", "ALL", "↔", "LEAD"),
    ("Faisal Orakzai", "FOUND", "↔", "GLOB"),
    ("OkzByte Hub", "ORAK", "↔", "TECH"),
    ("Orakzai Group", "ORAK", "↔", "ALL"),
    ("OKBOND Global", "BC", "↔", "GLOB"),
    ("Sovereign Grid", "GRID", "↔", "OWN"),
    ("Shamim Forever", "ART", "↔", "GLOB"),
    ("Digital Luxury", "BEST", "↔", "CASH"),
    ("E-commerce Logistics", "SHIP", "↔", "DONE"),
    ("Customer Support", "HELP", "↔", "USER"),
    ("Strategic Focus", "ONE", "↔", "DONE"),
    ("Ambition Scale", "SMALL", "→", "BIG"),
    ("Innovation Loop", "NEW", "↔", "BEST"),
    ("Heritage Future", "PAST", "↔", "TIME"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g164-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g164-{index}-title g164-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g164-{index}-title">{safe}</title><desc id="g164-{index}-desc">A global company building relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g164-{index}-caption" class="diagram-caption">{index}. {safe} — Global company building relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Building Global Companies Framework</title><desc id="hero-desc">A diagram showing the path from local ideas to international enterprises, including digital exports, remote teams, and global infrastructure.</desc><defs><linearGradient id="h164-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h164-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE GLOBAL ENTERPRISE PATHWAY (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">LOCAL INSIGHT → GLOBAL PRODUCT VALUE</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL EXPORT: $4.6B PAKISTAN IT TARGET</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">REMOTE TEAMS & DISTRIBUTED EXECUTION</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">GLOBAL SAAS MARKET ($488B+ IN 2026)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">COMPLIANCE, PRIVACY & DATA GOVERNANCE</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI ECOSYSTEM: HUB, BOND & GRID</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SOVEREIGN AMBITION: HERITAGE TO GLOBE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">BUILDING GLOBAL COMPANIES</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From a Local Idea to an International Enterprise.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Global Enterprise Pathway: Navigating the transition from local problem-solving to international scale, leveraging digital infrastructure, global talent, and 2026 market trends.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 164</title>
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
            <p class="section-label">PAGE 164</p>
            <h2>BUILDING GLOBAL COMPANIES</h2>
            <p>“From a Local Idea to an International Enterprise.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “A global company does not necessarily begin in a global city. It can begin with one person, one problem and one useful idea. The modern digital economy has reduced some of the geographic barriers that once limited entrepreneurship. A developer in Pakistan can build software for customers in Europe; a designer can work with companies in North America. But becoming global is more than selling internationally. It requires product quality, reliable infrastructure, strong governance, cultural intelligence, and international execution. For the modern Orakzai entrepreneur, the journey can begin locally while the ambition remains global.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Digital Global Economy (2026)</h3>
                <p>By 2026, Pakistan's IT sector reached a historic milestone, with annual exports climbing to **$4.6 billion** [1]. This growth is fueled by a new generation of digital businesses that internationalize quickly through electronic distribution. The global Software-as-a-Service (SaaS) market, projected to reach **$488.53 billion** in 2026, offers a scalable pathway for Pakistani founders to serve worldwide users without the traditional constraints of physical logistics [2] [3].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Distributed Execution & Remote Teams</h3>
                <p>Global companies today operate through distributed teams, recruiting talent across national boundaries. A typical Orakzai-led venture might house engineering in Pakistan, design in Europe, and sales in North America. This model demands rigorous communication, asynchronous documentation, and high cultural intelligence (CQ) to navigate diverse expectations, purchasing habits, and time zones [4] [5].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Orakzai Ecosystem: Case Studies</h3>
                <p>Founders like **Faisal Orakzai** illustrate the participation of Pakistani entrepreneurs in inherently international sectors such as blockchain, digital assets, and infrastructure. Initiatives like **OkzByte Hub**, **Orakzai Bond (OKBOND)**, and the **Orakzai Sovereign Grid** represent a move toward sovereign digital infrastructure. Furthermore, brands like **Shamim Forever** showcase how digital commerce allows luxury products to reach global markets while retaining their distinct cultural identity [6] [7].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Governance, Compliance & Scale</h3>
                <p>Scaling globally requires "compliance by design." Companies must navigate complex multi-region architectures, data privacy laws (like GDPR), and international taxation. Protecting intellectual property, managing foreign exchange (FX) risks, and building robust disaster recovery systems are essential for maintaining the trust of global customers and investors alike [8] [9].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Building Global Companies</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Global ambition is the natural extension of our tribal resilience. For the Orakzai entrepreneur, the world is the market, but the home is the foundation. We do not hide our origins; we use them to build authentic, high-quality solutions that compete on universal standards. By mastering digital infrastructure and international governance, we secure our place in the global future.”</p>
            </div>

            <div class="final-statement">
                LOCAL BEGINNINGS.<br>
                GLOBAL AMBITION.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>The Express Tribune, <em>Pakistan IT Exports Hit Record $4.6 Billion in FY 2025-26 (July 2026)</em>.</li>
                    <li>Statista, <em>Global Software-as-a-Service (SaaS) Market Forecast 2026 (May 2026)</em>.</li>
                    <li>Market Data Forecast, <em>Worldwide Cloud Computing and Digital Export Trends (2026)</em>.</li>
                    <li>Robert Half Research, <em>Remote Work and Distributed Team Statistics for 2026 (July 2026)</em>.</li>
                    <li>LinkedIn Tech Insights, <em>Pakistan's Tech Industry Growth and International Participation (February 2026)</em>.</li>
                    <li>CryptoSlate / Faisal Orakzai, <em>Ecosystem Profile: OkzByte Hub and Digital Asset Initiatives (August 2026)</em>.</li>
                    <li>Orakzai Group Technical Team, <em>Technical Specification: Sovereign Grid and Blockchain Infrastructure (2026)</em>.</li>
                    <li>Forbes Advisor, <em>Global Business Trends: Remote Work, Privacy, and Scale (July 2026)</em>.</li>
                    <li>OWASP Foundation, <em>International Data Governance and Cybersecurity Standards (2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            164
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

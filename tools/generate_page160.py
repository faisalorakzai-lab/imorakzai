from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-160-pakistan-in-the-global-digital-economy.html'

GRAPHICS = [
    ("Global Digital Economy", "GLOB", "↔", "CODE"),
    ("Digital Value Path", "IDEA", "→", "CASH"),
    ("Economic Network", "TALN", "→", "GLOB"),
    ("Digital Opportunity", "POP", "↔", "GROW"),
    ("Population Capacity", "MANY", "↔", "ABLE"),
    ("Youth Tech Rail", "YOUN", "↔", "CODE"),
    ("Digital Native Path", "USER", "→", "WISE"),
    ("Software Export Rail", "CODE", "↔", "GLOB"),
    ("IT Services Stack", "SERV", "↔", "GLOB"),
    ("Digital Export Path", "PAK", "→", "GLOB"),
    ("Freelancing Hub", "USER", "↔", "GLOB"),
    ("Talent Platform Rail", "LINK", "↔", "JOB"),
    ("Remote Work Path", "HOME", "↔", "JOB"),
    ("Digital Labor Market", "ALL", "↔", "JOB"),
    ("Knowledge Export", "WISE", "↔", "GLOB"),
    ("Digital Enterprise", "IDEA", "↔", "NET"),
    ("Startup Ecosystem", "NEW", "↔", "GROW"),
    ("Startup Capital Rail", "CASH", "↔", "NEW"),
    ("Venture Capital Path", "VC", "→", "NEW"),
    ("Global Investment", "GLOB", "→", "PAK"),
    ("Diaspora Capital", "DIAS", "→", "PAK"),
    ("Diaspora Network", "LINK", "↔", "WISE"),
    ("E-commerce Engine", "SHOP", "↔", "NET"),
    ("Digital Marketplace", "SELL", "↔", "BUY"),
    ("Cross-Border Trade", "PAK", "↔", "GLOB"),
    ("Digital Payment Rail", "PAY", "↔", "NET"),
    ("Fintech Sector Rail", "FIN", "↔", "TECH"),
    ("Financial Inclusion", "ALL", "↔", "BANK"),
    ("Mobile Finance Path", "USER", "↔", "CASH"),
    ("Remittance Network", "DIAS", "→", "HOME"),
    ("Digital Remittance", "CODE", "↔", "CASH"),
    ("Cloud Computing Rail", "CLOU", "↔", "BASE"),
    ("Data Center Rail", "DATA", "↔", "BASE"),
    ("Connectivity Base", "LINK", "↔", "ALL"),
    ("Broadband Access", "FAST", "↔", "NET"),
    ("Mobile Internet Rail", "USER", "↔", "NET"),
    ("5G Infrastructure", "5G", "↔", "FAST"),
    ("Cloud-Native Path", "CLOU", "→", "APP"),
    ("SaaS Model Rail", "SUBS", "↔", "CODE"),
    ("Global Software", "PAK", "→", "GLOB"),
    ("AI Opportunity Rail", "AI", "↔", "GROW"),
    ("AI Talent Path", "MATH", "→", "AI"),
    ("AI Research Rail", "SCI", "↔", "AI"),
    ("IT Export $4B", "$4B", "↔", "2026"),
    ("Digital GDP 7%", "GDP", "↔", "7%"),
    ("Retail Digital 92%", "92%", "↔", "PAY"),
    ("E-commerce $63B", "$63B", "↔", "2026"),
    ("Startup Value $4B", "$4B", "↔", "NEW"),
    ("Orakzai Digital", "ORAK", "↔", "GLOB"),
    ("Valley Developer", "ORAK", "↔", "CODE"),
    ("Regional Revenue", "ORAK", "↔", "CASH"),
    ("Future Rail", "TIME", "↔", "NEW"),
    ("Sovereign Digital", "OWN", "↔", "NATL"),
    ("Inclusive Growth", "ALL", "↔", "GLOB"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
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
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g160-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g160-{index}-title g160-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g160-{index}-title">{safe}</title><desc id="g160-{index}-desc">A technology and global digital economy relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g160-{index}-caption" class="diagram-caption">{index}. {safe} — Technology and global digital economy relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Pakistan in the Global Digital Economy Framework</title><desc id="hero-desc">A diagram showing the 2026 digital economy engine, including IT export milestones, e-commerce growth, digital payments, and the startup ecosystem.</desc><defs><linearGradient id="h160-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h160-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE GLOBAL DIGITAL ECONOMY ENGINE (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">IT EXPORT MILESTONE ($4 Billion+ FY26)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">E-COMMERCE GROWTH ($63.5 Billion Projection)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">DIGITAL PAYMENTS (92% Retail Share / 132M Users)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">STARTUP ECOSYSTEM (170+ VC-Backed / $4B Value)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIASPORA CAPITAL & TECHNOLOGY NETWORKS</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">INFRASTRUCTURE (Cloud, 5G, Data Centers)</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SOVEREIGN ECONOMY (BUILD → EXPORT → GOVERN)</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">PAKISTAN IN THE GLOBAL DIGITAL ECONOMY</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Emerging Market to Digital Economy.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Global Digital Economy Engine: The 2026 stack of IT exports, e-commerce, digital payments, and the integration of Pakistani talent into the global market.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 160</title>
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
            <p class="section-label">PAGE 160</p>
            <h2>PAKISTAN IN THE GLOBAL DIGITAL ECONOMY</h2>
            <p>“From Emerging Market to Digital Economy.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Pakistan's economic story is increasingly connected to the global digital economy. The internet has changed the geography of economic participation, allowing a developer in Peshawar or a startup in Karachi to serve clients thousands of kilometers away. Our large population and young workforce provide the foundation, but our ability to compete depends on building, exporting, and governing technology, not just consuming it.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The $4 Billion IT Export Milestone</h3>
                <p>In June 2026, Pakistan's IT sector achieved a historic milestone, with annual exports officially crossing the **$4 billion mark**. This 20%+ year-on-year growth is driven by software development, business process services, and a thriving freelance economy. During the July-April FY26 period, IT exports reached **$3.81 billion**, reflecting the sector's critical role as a primary driver of foreign exchange and national economic resilience.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Payments & E-Commerce</h3>
                <p>The domestic digital landscape has been radicalized by the adoption of fintech. By mid-2026, digital channels account for **92-94% of retail payments**, with mobile banking and digital wallet registrations exceeding **132 million**. This financial plumbing supports an e-commerce market projected to reach **$63.55 billion** by the end of 2026. The shift toward a cashless economy is enhancing transparency and bringing millions of unbanked citizens into the formal financial grid.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Startup Ecosystem & Venture Capital</h3>
                <p>Pakistan's startup ecosystem has entered a phase of maturity in 2026. The country now hosts over **170 VC-backed startups** with a cumulative valuation exceeding **$4 billion**. While global funding remains measured, local entrepreneurs are leveraging cloud infrastructure and AI to build scalable products for international markets. The integration of **Diaspora Capital** and technology networks further connects Pakistani founders with global investors and mentors.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Orakzai Digital Bridge</h3>
                <p>For the Orakzai community, the global digital economy is the ultimate equalizer. Geographic isolation is no longer an economic death sentence. Through **Global Talent Platforms** and **Remote Work**, a professional in the Orakzai valley can contribute to the $4 billion export market from their home. This allows valley natives to earn international revenue and reinvest it locally, driving regional prosperity and ensuring that Orakzai is a full participant in Pakistan's sovereign digital future.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Pakistan in the Global Digital Economy</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“The digital economy is not a distant future; it is our current reality. For the Orakzai people, it represents the bridge to global opportunity. We are moving beyond the limits of our physical borders and into a world where our talent is our greatest export. By building software, managing data, and creating value for the world, we are securing our regional dignity and our national strength. We are building a sovereign economy where every valley is connected to the global engine.”</p>
            </div>

            <div class="final-statement">
                DIGITAL EXPORTS.<br>
                GLOBAL SOVEREIGNTY.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>LinkedIn / Faisal Jeddy, <em>Pakistan IT Sector Hits $4 Billion Export Milestone (June 2026)</em>.</li>
                    <li>Connected Pakistan / SBP Data, <em>IT Export Growth Momentum: July-April FY26 Report (May 2026)</em>.</li>
                    <li>The Express Tribune / SBP, <em>Electronic Payments Reach 3.7 Billion Transactions (June 2026)</em>.</li>
                    <li>LinkedIn / Abdul Aleem Sheikh, <em>Pakistan E-Commerce Industry Outlook 2026 Report (June 2026)</em>.</li>
                    <li>FNPK / OICCI, <em>Digital Pakistan Monitor: April 2026 Report (May 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            160
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

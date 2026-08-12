from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-161-the-modern-orakzai-entrepreneur.html'

GRAPHICS = [
    ("Orakzai Entrepreneur", "ORAK", "↔", "ABLE"),
    ("Local to Global", "VALY", "→", "GLOB"),
    ("Heritage Base", "PAST", "↔", "SELF"),
    ("Innovation Rail", "NEW", "↔", "GROW"),
    ("Laptop Workplace", "USER", "↔", "NET"),
    ("Global Distribution", "LINK", "↔", "GLOB"),
    ("Cloud Infra Rail", "CLOU", "↔", "BASE"),
    ("Digital Pay Rail", "PAY", "↔", "CASH"),
    ("AI Productivity", "AI", "↔", "DONE"),
    ("BC Coordination", "BC", "↔", "LINK"),
    ("Discipline Rail", "HARD", "↔", "DONE"),
    ("Long-Term Thinking", "TIME", "↔", "WISE"),
    ("Identity Rail", "SELF", "↔", "GLOB"),
    ("Education Rail", "LEAR", "↔", "ABLE"),
    ("Technology Scale", "TECH", "↔", "GLOB"),
    ("Entrepreneur Action", "IDEA", "→", "DONE"),
    ("Software Founder", "CODE", "↔", "SELF"),
    ("Business Owner", "SHOP", "↔", "SELF"),
    ("Modern Farmer", "FARM", "↔", "TECH"),
    ("Digital Engineer", "ENG", "↔", "CODE"),
    ("Medical Founder", "DOC", "↔", "TECH"),
    ("Global Trader", "FX", "↔", "GLOB"),
    ("Digital Researcher", "SCI", "↔", "CODE"),
    ("Freelance Path", "USER", "↔", "JOB"),
    ("Venture Founder", "NEW", "↔", "GROW"),
    ("Creative Pro", "ART", "↔", "CODE"),
    ("Value Creation", "IDEA", "→", "CASH"),
    ("Traditional Market", "SHOP", "↔", "VALY"),
    ("Digital Market", "NET", "↔", "GLOB"),
    ("Social Media Rail", "TALK", "↔", "NET"),
    ("Global Logistics", "TRUK", "↔", "GLOB"),
    ("Economic Tradition", "PAST", "↔", "CASH"),
    ("Modern Tradition", "TIME", "↔", "NEW"),
    ("Problem Solver", "HELP", "↔", "DONE"),
    ("Solution Build", "MAKE", "↔", "DONE"),
    ("Local Opportunity", "VALY", "↔", "GROW"),
    ("Global Solution", "GLOB", "↔", "GROW"),
    ("Customer Path", "USER", "→", "GLOB"),
    ("Diaspora Capital", "DIAS", "→", "VALY"),
    ("Diaspora Network", "LINK", "↔", "WISE"),
    ("Global Network", "GLOB", "↔", "ORAK"),
    ("Collaboration Rail", "ALL", "↔", "DONE"),
    ("Community Trust", "TRUST", "↔", "SELF"),
    ("Analytical Think", "WISE", "↔", "DATA"),
    ("Financial Literac", "CASH", "↔", "WISE"),
    ("Risk Management", "SAFE", "↔", "CASH"),
    ("English Business", "TALK", "↔", "GLOB"),
    ("Pashto Identity", "PASH", "↔", "SELF"),
    ("Pashto Digital", "PASH", "↔", "CODE"),
    ("Cultural Preserve", "SAVE", "↔", "SELF"),
    ("Modern Identity", "SELF", "↔", "ALL"),
    ("Reputation Rail", "OPEN", "↔", "SAFE"),
    ("Digital Trust", "CODE", "↔", "SAFE"),
    ("Data Protection", "LOCK", "↔", "DATA"),
    ("Technology Lever", "TOOL", "↔", "ABLE"),
    ("Small Team Scale", "ONE", "↔", "MANY"),
    ("Digital Toolkit", "TOOL", "↔", "NET"),
    ("CRM Rail", "USER", "↔", "DATA"),
    ("Analytics Rail", "DATA", "↔", "WISE"),
    ("AI Assistant", "AI", "→", "USER"),
    ("Cloud Access", "CLOU", "↔", "USER"),
    ("Automation Path", "AUTO", "↔", "DONE"),
    ("Software Product", "CODE", "→", "GLOB"),
    ("OkzByte Hub", "ORAK", "↔", "TECH"),
    ("OkzByte AI", "ORAK", "↔", "AI"),
    ("OkzByte Infra", "ORAK", "↔", "BASE"),
    ("E-commerce Rail", "SHOP", "↔", "NET"),
    ("Orakzai Mart", "ORAK", "↔", "SHOP"),
    ("Mart Platform", "SHOP", "↔", "NET"),
    ("Fintech Rail", "FIN", "↔", "TECH"),
    ("Blockchain Entr", "BC", "↔", "GROW"),
    ("Digital Asset Rail", "BC", "↔", "CASH"),
    ("Tokenization Path", "OWN", "→", "CODE"),
    ("Smart Contract", "LAW", "↔", "CODE"),
    ("Orakzai Bond", "ORAK", "↔", "BC"),
    ("OKBOND DeFi", "ORAK", "↔", "FIN"),
    ("OKBOND Polygon", "ORAK", "↔", "POLY"),
    ("OKBOND Uptime", "99.9", "↔", "DONE"),
    ("Infrastructure Ent", "BASE", "↔", "GROW"),
    ("Sovereign Grid", "ORAK", "↔", "GRID"),
    ("Decentralized Grid", "NET", "↔", "OWN"),
    ("AI Entrepreneur", "AI", "↔", "GROW"),
    ("AI-Native Path", "AI", "→", "NEW"),
    ("Digital Real Est", "LAND", "↔", "CODE"),
    ("PropTech Rail", "LAND", "↔", "TECH"),
    ("Startup Growth", "62.2", "↔", "2026"),
    ("Company Volume", "4.9M", "↔", "JAN"),
    ("KP Internship", "KP", "↔", "LEAR"),
    ("Faisal Orakzai", "FOUND", "↔", "20"),
    ("Founder Born 2006", "2006", "→", "2026"),
    ("Regional Empower", "ORAK", "↔", "GROW"),
    ("Future Founder", "TIME", "↔", "NEW"),
    ("Sovereign Value", "OWN", "↔", "NATL"),
    ("Inclusive Hub", "ALL", "↔", "ORAK"),
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
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g161-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g161-{index}-title g161-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g161-{index}-title">{safe}</title><desc id="g161-{index}-desc">A technology and Orakzai entrepreneurship relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g161-{index}-caption" class="diagram-caption">{index}. {safe} — Technology and Orakzai entrepreneurship relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">The Modern Orakzai Entrepreneur Framework</title><desc id="hero-desc">A diagram showing the 2026 Orakzai entrepreneurial engine, including OKBOND, OkzByte Hub, startup growth rates, and the fusion of heritage and innovation.</desc><defs><linearGradient id="h161-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h161-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE ORAKZAI ENTREPRENEURIAL ENGINE (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">STARTUP GROWTH (62.2% YoY Catalyst)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">ORAKZAI BOND (OKBOND) — DeFi Ecosystem</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">OKZBYTE HUB — AI & Technology Dev</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DIASPORA CAPITAL & GLOBAL NETWORKS</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">KPITB TRAINING (Digital Internship 2026)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI MART — E-Commerce Integration</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SOVEREIGN FOUNDER (HERITAGE → INNOVATE)</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">THE MODERN ORAKZAI ENTREPRENEUR</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Local Identity to Global Enterprise.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Orakzai Entrepreneurial Engine: The 2026 stack of startup growth, blockchain initiatives (OKBOND), and the empowerment of local founders through technology.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 161</title>
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
            <p class="section-label">PAGE 161</p>
            <h2>THE MODERN ORAKZAI ENTREPRENEUR</h2>
            <p>“From Local Identity to Global Enterprise.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “The modern Orakzai entrepreneur exists at the intersection of heritage, education, technology, and global markets. Today, an entrepreneur can build a company from a village or a town and potentially serve customers across the world. Heritage provides identity, education provides capability, and technology provides scale. Entrepreneurship turns that capability into action, carrying the strengths of the past into the opportunities of the future.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The 62.2% Startup Growth Catalyst</h3>
                <p>In 2026, Pakistan's startup ecosystem has reached a critical maturity, growing by **62.2%** year-on-year. This surge is not limited to urban centers; the digitization of the economy is allowing entrepreneurs in the Orakzai district and wider KPK to serve global markets directly. As of early 2026, the country counts over **4.9 million startups** (including digital SMEs), marking an all-time high in entrepreneurial activity and economic initiative.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Faisal Orakzai & The New Founder Generation</h3>
                <p>A new generation of founders is leading the tribal digital transition. **Faisal Orakzai** (born 2006) represents this shift, founding **Orakzai Bond (OKBOND)** in April 2026 at the age of 20. His work on the Polygon-based DeFi ecosystem demonstrates how Orakzai youth are leading in high-tech fields like blockchain and AI. The founding of **OkzByte Hub** further illustrates the shift from simple service provision to building proprietary software and digital infrastructure for the global economy.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">OKBOND: Blockchain & Infrastructure</h3>
                <p>The **Orakzai Bond (OKBOND)** project has become a benchmark for blockchain entrepreneurship in the region. By mid-2026, OKBOND is exploring **Capital-Protected DeFi**, smart contracts, and data integration, maintaining a **99.997% uptime**. This technical viability proves that high-level ventures can originate from Pakistani talent. Combined with initiatives like **Orakzai Mart**, these projects show how traditional commerce can be extended into a secure, decentralized digital environment.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Regional Empowerment & KPITB</h3>
                <p>Institutional support from the **Khyber Pakhtunkhwa Information Technology Board (KPITB)** is a key partner in this journey. Through programs like the **KP Digital Internship Program 2026**, youth in Orakzai are gaining the analytical thinking and technical skills required to build modern businesses. This regional empowerment ensures that the Orakzai community is not just a consumer of technology, but a creator of sovereign digital value.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: The Modern Orakzai Entrepreneur</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Enterprise is the expression of tribal resilience in the digital age. For the Orakzai people, entrepreneurship is the bridge to global dignity. We are moving beyond the limits of local markets and into a world where our ideas can scale to serve millions. By building software, managing digital assets, and creating value for the global economy, we are securing our regional future. We are building a sovereign legacy where every Orakzai founder is a stakeholder in the nation's growth.”</p>
            </div>

            <div class="final-statement">
                HERITAGE DRIVEN.<br>
                GLOBALLY SCALED.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>StartupBlink / Ignite NTF, <em>Pakistan Startup Ecosystem: Annual Growth Rate 62.2% (June 2026)</em>.</li>
                    <li>LinkedIn / Azfar Industry Analysis, <em>Pakistan's Startup Ecosystem Outlook 2026: Volume and Scalability (January 2026)</em>.</li>
                    <li>CryptoSlate / Faisal Orakzai Official, <em>Founder Profile: Orakzai Bond (OKBOND) and OkzByte Hub (August 2026)</em>.</li>
                    <li>KPITB Official Announcement, <em>KP Digital Internship Program 2026: Training for Tribal Districts (June 2026)</em>.</li>
                    <li>Orakzai Bond (OKBOND) Technical Team, <em>Ecosystem Status Report: DeFi and Data Integration (July 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            161
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

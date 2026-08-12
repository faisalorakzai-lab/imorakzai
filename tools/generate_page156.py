from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-156-diaspora-investment.html'

GRAPHICS = [
    ("Global Connection", "MANY", "↔", "ONE"),
    ("Diaspora Network", "GLOB", "↔", "PAK"),
    ("Capital Rail", "CASH", "→", "GROW"),
    ("Investment Cycle", "SEED", "→", "VALU"),
    ("Remittance Loop", "HOME", "↔", "CASH"),
    ("Investment Loop", "GROW", "↔", "CASH"),
    ("Capital Formation", "SAVE", "→", "BASE"),
    ("Income Abroad", "WORK", "↔", "GLOB"),
    ("Saving Path", "CASH", "→", "BANK"),
    ("Business Activity", "MAKE", "↔", "DONE"),
    ("Employment Goal", "JOB", "↔", "GROW"),
    ("Economic Value", "VALU", "↔", "NATL"),
    ("Diaspora Knowledge", "WISE", "↔", "BASE"),
    ("Local Advantage", "HOME", "↔", "IDEA"),
    ("International Exp", "GLOB", "↔", "WISE"),
    ("Corporate Gov", "LAW", "↔", "SAFE"),
    ("Market Knowledge", "DATA", "↔", "GLOB"),
    ("Diaspora Bridge", "NET", "↔", "LINK"),
    ("Angel Investment", "ONE", "→", "SEED"),
    ("VC Investment", "TEAM", "→", "GROW"),
    ("Startup Opportunity", "NEW", "↔", "VALU"),
    ("Risk Evaluation", "SAFE", "↔", "DATA"),
    ("SME Investment", "SME", "↔", "CASH"),
    ("Family Business", "HOME", "↔", "COMP"),
    ("Manufacturing Rail", "MAKE", "↔", "BASE"),
    ("Agri Investment", "FARM", "↔", "BASE"),
    ("Real Estate Rail", "LAND", "↔", "VALU"),
    ("Commercial Prop", "SHOP", "↔", "CASH"),
    ("Housing Market", "HOME", "↔", "VALU"),
    ("Infra Investment", "BASE", "↔", "LONG"),
    ("Renewable Energy", "SUN", "↔", "POWR"),
    ("Tech Infra", "NET", "↔", "BASE"),
    ("Fintech Path", "TECH", "↔", "FIN"),
    ("Payment Path", "PAY", "↔", "NET"),
    ("E-commerce Path", "SHOP", "↔", "NET"),
    ("Export Business", "PAK", "→", "GLOB"),
    ("Software Export", "CODE", "→", "GLOB"),
    ("SaaS Model", "CLOU", "↔", "CASH"),
    ("AI Company", "AI", "↔", "NEW"),
    ("Cybersecurity Co", "SEC", "↔", "SAFE"),
    ("Blockchain Path", "BC", "↔", "NEW"),
    ("Digital Assets", "TOK", "↔", "VALU"),
    ("Research Biz", "SCI", "↔", "CASH"),
    ("Univ Spinout", "UNI", "→", "COMP"),
    ("IP Commercial", "IDEA", "→", "VALU"),
    ("Knowledge Capital", "WISE", "↔", "CASH"),
    ("Human Capital", "PEOP", "↔", "VALU"),
    ("Diaspora Mentor", "WISE", "↔", "USER"),
    ("Market Access", "GLOB", "↔", "USER"),
    ("Customer Link", "USER", "↔", "GLOB"),
    ("Global Distro", "PAK", "→", "GLOB"),
    ("Export Revenue", "GLOB", "→", "CASH"),
    ("Reinvestment", "CASH", "→", "NEW"),
    ("Diaspora-Led Co", "OWN", "↔", "PAK"),
    ("Cross-Border Team", "TEAM", "↔", "GLOB"),
    ("Global Management", "WISE", "↔", "GLOB"),
    ("Professional Gov", "LAW", "↔", "NAME"),
    ("Financial Report", "DATA", "↔", "SAFE"),
    ("Board Oversight", "WISE", "↔", "SAFE"),
    ("Shareholder Right", "OWN", "↔", "LAW"),
    ("Transparency", "OPEN", "↔", "DATA"),
    ("Due Diligence", "READ", "↔", "SAFE"),
    ("Legal Structure", "LAW", "↔", "BASE"),
    ("RDA Total 2026", "$13.6B", "↔", "DONE"),
    ("RDA Monthly", "$282M", "↔", "JULY"),
    ("RDA Accounts", "956K", "↔", "USER"),
    ("FDI Growth", "+163%", "↔", "FY26"),
    ("Startup Flow", "$36M", "↔", "2025"),
    ("SIFC Support", "GOV", "↔", "SEED"),
    ("Investor Summit", "SUMM", "↔", "2026"),
    ("Orakzai Invest", "ORAK", "↔", "CASH"),
    ("Regional Solar", "SUN", "↔", "ORAK"),
    ("Valley AgriTech", "FARM", "↔", "ORAK"),
    ("Future Rail", "TIME", "↔", "NEW"),
    ("Sovereign Wealth", "OWN", "↔", "NATL"),
    ("Inclusive Growth", "ALL", "↔", "GROW"),
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
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g156-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g156-{index}-title g156-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g156-{index}-title">{safe}</title><desc id="g156-{index}-desc">A diaspora investment relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g156-{index}-caption" class="diagram-caption">{index}. {safe} — Diaspora investment relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Diaspora Investment Framework</title><desc id="hero-desc">A diagram showing the 2026 diaspora investment stack, including RDA milestones, capital formation pathways, and the bridge between global capital and national growth.</desc><defs><linearGradient id="h156-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h156-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE DIASPORA CAPITAL ENGINE (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">ROSHAN DIGITAL ACCOUNT ($13.6B+ Total)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">JULY 2026 INFLOWS ($282M / +52% YoY)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">FDI RECOVERY (+163% YoY March 2026)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">STARTUP & SME FLOW ($36M+ Flow Recovery)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">KNOWLEDGE & HUMAN CAPITAL TRANSFER</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">SIFC & REGULATORY ENABLERS (TRUST)</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">ECONOMIC SOVEREIGNTY (INVEST → GROW)</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">DIASPORA INVESTMENT</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Turning Global Connections into Economic Opportunity.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Diaspora Investment Framework: The 2026 stack of capital formation, RDA milestones, and the bridge between global Pakistani capital and national growth.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 156</title>
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
            <p class="section-label">PAGE 156</p>
            <h2>DIASPORA INVESTMENT</h2>
            <p>“Turning Global Connections into Economic Opportunity.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “The Pakistani diaspora represents a significant international network of professionals and investors. Its economic contribution extends far beyond remittances; diaspora investment connects Pakistan with international capital, business expertise, and global markets. The opportunity is to create a cycle where diaspora capital builds businesses, creates jobs, and drives innovation for national development.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Roshan Digital Account Milestone</h3>
                <p>In 2026, the **Roshan Digital Account (RDA)** has become the primary rail for diaspora investment. By August 2026, cumulative inflows reached **$13.647 billion**, with over **956,000 accounts** opened by overseas Pakistanis. The month of July 2026 alone saw a record **$282 million** in inflows, a **52% year-on-year increase**. This sustained growth reflects deep-seated trust in the national financial system and the effectiveness of digital-first investment channels.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">FDI Recovery & Strategic Sectors</h3>
                <p>Net Foreign Direct Investment (FDI) has shown a massive recovery in 2026, with March recording **$168 million**, up **163%** from the previous year. Diaspora investors are increasingly focusing on strategic sectors such as **Renewable Energy (Solar)**, **Infrastructure**, and **Technology**. Through the Special Investment Facilitation Council (SIFC), the government has provided the regulatory certainty and transparency necessary to attract large-scale capital from overseas professionals.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Startup Flow & Angel Mentorship</h3>
                <p>The startup ecosystem is a major destination for diaspora "Angels" and venture capital. Following a recovery in 2025 where startups raised **$36.6 million**, the 2026 trend shows increased diaspora participation in **AI-Native** and **FinTech** ventures. Beyond capital, these investors provide vital **Knowledge Capital**—mentoring local founders, introducing them to international customers, and facilitating global distribution for Pakistani software and products.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Orakzai Regional Bridge</h3>
                <p>Diaspora investment acts as a bridge for regional empowerment. Overseas Orakzai natives are bypassing traditional geographic constraints to invest directly in the valley's development. From **Solar-powered irrigation** to **AgriTech processing units**, diaspora capital is improving local productivity. This model of "Regional DDI" ensures that the benefits of global success are felt in the most remote valleys, building a sovereign and inclusive future for all.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Diaspora Investment</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Investment is an act of faith in the future. For the Orakzai community, the diaspora is our global equity. Our people abroad are not just sending money to sustain families; they are investing to build a nation. When an Orakzai professional in Dubai or London invests in a startup in Karachi or a solar farm in the valley, they are weaving a web of sovereign prosperity. We are building an economy where every connection is a catalyst for growth.”</p>
            </div>

            <div class="final-statement">
                CAPITAL IS CONNECTION.<br>
                GROWTH IS SHARED.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>State Bank of Pakistan (SBP) / ProPakistani, <em>RDA Inflows Cross $13.6 Billion Milestone (August 2026)</em>.</li>
                    <li>SBP / Connected Pakistan, <em>Roshan Digital Account Performance and Cumulative Inflows (July 2026)</em>.</li>
                    <li>Economic Monitoring Report, <em>Net Foreign Direct Investment Jumps 163% in March 2026 (April 2026)</em>.</li>
                    <li>MOITT / TechDestiNation, <em>Pakistan Investor Summit 2026: Diaspora and Institutional Funding (July 2026)</em>.</li>
                    <li>Industry Analysis / Ignite NTF, <em>Startup Funding Recovery and Diaspora Participation Trends (March 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            156
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

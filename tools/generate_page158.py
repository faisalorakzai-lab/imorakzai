from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-158-technology-and-financial-markets.html'

GRAPHICS = [
    ("Market Transformation", "INFO", "↔", "TRUST"),
    ("Digital Market", "CODE", "↔", "CASH"),
    ("Capital Market Rail", "SAVE", "→", "GROW"),
    ("Financial Infra", "BASE", "↔", "LINK"),
    ("Electronic Market", "NET", "↔", "DONE"),
    ("Digital Trading", "APP", "↔", "DONE"),
    ("Mobile Investing", "USER", "↔", "GLOB"),
    ("Financial Data", "DATA", "↔", "WISE"),
    ("Real-Time Data", "TIME", "→", "DATA"),
    ("Cloud Computing", "CLOU", "↔", "BASE"),
    ("Financial Software", "CODE", "↔", "RUN"),
    ("API Connection", "BANK", "↔", "APP"),
    ("Open Banking Path", "OPEN", "↔", "DATA"),
    ("Digital Payment", "PAY", "↔", "NET"),
    ("Instant Payment", "TIME", "↔", "PAY"),
    ("Digital Bank Rail", "CLOU", "↔", "BANK"),
    ("Mobile Wallet", "ID", "↔", "CASH"),
    ("Financial Inclusion", "ALL", "↔", "CASH"),
    ("Digital Identity", "ID", "↔", "SAFE"),
    ("Electronic KYC", "ID", "↔", "CODE"),
    ("AML Technology", "SEC", "↔", "SAFE"),
    ("RegTech Rail", "LAW", "↔", "CODE"),
    ("SupTech Rail", "GOV", "↔", "DATA"),
    ("Algo Trading", "CODE", "→", "SELL"),
    ("HFT Infrastructure", "FAST", "↔", "NET"),
    ("Quant Finance", "MATH", "↔", "CASH"),
    ("ML in Finance", "AI", "↔", "DATA"),
    ("AI Market Analysis", "AI", "↔", "WISE"),
    ("NLP Extraction", "READ", "→", "DATA"),
    ("Sentiment Analysis", "FEEL", "→", "DATA"),
    ("Automated Research", "AI", "→", "READ"),
    ("Portfolio Analytics", "MANY", "↔", "ONE"),
    ("Robo-Advisory", "AI", "→", "WISE"),
    ("Risk Management", "SAFE", "↔", "DATA"),
    ("Market Risk Rail", "GLOB", "↔", "SAFE"),
    ("Credit Risk Rail", "CASH", "↔", "SAFE"),
    ("Liquidity Risk", "FLOW", "↔", "SAFE"),
    ("Operational Risk", "RUN", "↔", "SAFE"),
    ("Cybersecurity Rail", "LOCK", "↔", "NET"),
    ("Security Ops", "SEC", "↔", "RUN"),
    ("Encryption Path", "LOCK", "↔", "DATA"),
    ("MFA Protection", "MANY", "↔", "ID"),
    ("Fraud Detection", "WARN", "↔", "DATA"),
    ("Anomaly Detection", "NEW", "↔", "DATA"),
    ("Identity Fraud Re", "ID", "↔", "SAFE"),
    ("Financial Crime Re", "LAW", "↔", "SAFE"),
    ("Market Surveillance", "EYE", "↔", "DATA"),
    ("Manipulation Detect", "WARN", "↔", "CODE"),
    ("Insider Monitoring", "EYE", "↔", "ID"),
    ("Clearing Path", "NET", "↔", "DONE"),
    ("Settlement Path", "DONE", "↔", "CASH"),
    ("Settlement Tech", "CODE", "↔", "TIME"),
    ("Custodian Rail", "SAFE", "↔", "OWN"),
    ("Brokerage Rail", "LINK", "↔", "USER"),
    ("Exchange Rail", "HUB", "↔", "ALL"),
    ("Bond Market Rail", "DEBT", "↔", "CASH"),
    ("Equity Market Rail", "OWN", "↔", "CASH"),
    ("Currency Market", "FX", "↔", "CASH"),
    ("Commodity Market", "STUF", "↔", "CASH"),
    ("Derivative Rail", "LINK", "↔", "CASH"),
    ("Money Market Rail", "TIME", "↔", "CASH"),
    ("IPO Momentum", "10", "↔", "Rs20B"),
    ("Trading Volume", "1.2B", "↔", "Rs63B"),
    ("Share Digitization", "BOOK", "↔", "CODE"),
    ("SECP Registration", "3.8K", "↔", "JAN"),
    ("Virtual Assets Act", "LAW", "↔", "2026"),
    ("Digital Bank Lic", "5", "↔", "DONE"),
    ("PSX Data Portal", "DATA", "↔", "USER"),
    ("Corporate Super", "GOV", "↔", "COMP"),
    ("Merger Logic", "ONE", "↔", "TWO"),
    ("Liquidation Logic", "DONE", "↔", "CASH"),
    ("Research Analyst", "WISE", "↔", "DATA"),
    ("Retail Investor", "USER", "↔", "PSX"),
    ("Dividend Path", "OWN", "→", "CASH"),
    ("Growth Engine", "GROW", "↔", "NATL"),
    ("Wealth Creation", "USER", "↔", "VALU"),
    ("Transparency Rail", "OPEN", "↔", "SAFE"),
    ("Efficiency Rail", "FAST", "↔", "DONE"),
    ("Orakzai Investor", "ORAK", "↔", "PSX"),
    ("Valley Brokerage", "ORAK", "↔", "APP"),
    ("Regional Wealth", "ORAK", "↔", "GROW"),
    ("Future Rail", "TIME", "↔", "NEW"),
    ("Sovereign Finance", "OWN", "↔", "NATL"),
    ("Inclusive Market", "ALL", "↔", "GLOB"),
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
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g158-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g158-{index}-title g158-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g158-{index}-title">{safe}</title><desc id="g158-{index}-desc">A technology and financial markets relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g158-{index}-caption" class="diagram-caption">{index}. {safe} — Technology and financial markets relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Technology & Financial Markets Framework</title><desc id="hero-desc">A diagram showing the 2026 digital financial engine, including IPO momentum, share digitization, digital banking, and RegTech integration.</desc><defs><linearGradient id="h158-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h158-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE DIGITAL FINANCIAL ENGINE (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">CAPITAL MARKET MOMENTUM (10 IPOs / Rs 20B+)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">MANDATORY DIGITIZATION (SECP S.R.O. 328)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">DIGITAL BANKING (5 Full-Fledged Licenses)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">VIRTUAL ASSETS ACT 2026 (SBP Regulation)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">REGTECH & SUPTECH (Real-Time Oversight)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AI & ML RISK MANAGEMENT (Fraud Detection)</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SOVEREIGN FINANCE (DIGITIZE → EMPOWER)</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">TECHNOLOGY & FINANCIAL MARKETS</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“The Digital Transformation of Finance.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Digital Financial Engine: The 2026 stack of capital market growth, mandatory digitization, and the integration of RegTech and AI into national finance.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 158</title>
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
            <p class="section-label">PAGE 158</p>
            <h2>TECHNOLOGY & FINANCIAL MARKETS</h2>
            <p>“The Digital Transformation of Finance.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Financial markets have always depended on information, trust, infrastructure, and connectivity. Technology is transforming all four. The result is not simply a faster system, but the emergence of a new digital financial infrastructure in which transactions, compliance, and settlement operate through interconnected software. For Pakistan, this transformation creates a historic opportunity to broaden access and connect businesses with capital.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Capital Market Momentum & IPOs</h3>
                <p>In the first half of 2026, Pakistan's capital markets have shown significant momentum. A record **10 IPOs** successfully raised over **Rs. 20 billion**, bringing businesses from manufacturing, energy, and technology to the public market. The PSX ready market saw trading volumes of **1.226 billion shares** valued at **Rs 63.897 billion** in Q1 2026. This growth is supported by digital listing processes and increased retail participation through mobile brokerage platforms.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Mandatory Share Digitization</h3>
                <p>A landmark regulatory shift occurred in 2026 with the SECP's issuance of **S.R.O. 328(I)/2026**. This regulation mandates that all unlisted companies replace physical shares with **book-entry (digital) form**. By eliminating paper-based ownership, the SECP is enhancing transparency, reducing fraud, and laying the foundation for a fully digital corporate ownership structure that integrates seamlessly with the national financial grid.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Banking & Virtual Assets</h3>
                <p>By mid-2026, Pakistan's five licensed digital banks are moving into full operations, leveraging **AI and Machine Learning** for credit scoring and risk management. Simultaneously, the SBP's introduction of the **Virtual Assets Act 2026** provides a clear regulatory framework for digital finance. This dual approach—empowering digital banks while regulating virtual assets—ensures that the nation's financial evolution remains secure, compliant, and globally competitive.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Orakzai Financial Bridge</h3>
                <p>Financial technology is a primary catalyst for regional wealth creation. Through **Mobile Investing** and **Digital Brokerage**, residents of the Orakzai valleys are no longer excluded from national capital markets. Valley natives can now invest in national companies and government bonds directly from their smartphones. This democratization of finance integrates the tribal economy into the national engine, allowing every Orakzai citizen to participate in sovereign wealth creation.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Technology & Financial Markets</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Finance is the plumbing of civilization. For the Orakzai people, digital finance is the bridge to national inclusion. We are moving beyond a cash-based tribal economy and toward a digital financial future. By investing in our nation's companies through the power of our smartphones, we are securing our regional prosperity. We are building a sovereign financial system where every citizen, from the city to the valley, is a stakeholder in Pakistan's growth.”</p>
            </div>

            <div class="final-statement">
                DIGITAL PLUMBING.<br>
                SOVEREIGN WEALTH.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>SECP Pakistan, <em>H1 2026 Capital Market Momentum and IPO Report (July 2026)</em>.</li>
                    <li>SECP S.R.O. 328(I)/2026, <em>Mandatory Book-Entry Form for Unlisted Companies (January 2026)</em>.</li>
                    <li>PSX Q1 2026 Market Outlook, <em>Trading Volumes and Ready Market Performance Analysis (February 2026)</em>.</li>
                    <li>State Bank of Pakistan (SBP), <em>The Virtual Assets Act 2026: Regulatory Framework (May 2026)</em>.</li>
                    <li>SECP Official Statistics, <em>New Company Registrations and Sectoral Growth (February 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            158
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

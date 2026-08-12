from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-186-economic-empowerment.html'

GRAPHICS = [
    ("Econ Empowerment", "SELF", "↔", "ABLE"),
    ("Opportunity Rail", "OPEN", "↔", "DO"),
    ("Econ Capability", "KNOW", "↔", "TOOL"),
    ("Education Base", "LEAR", "↔", "BASE"),
    ("Skills Path", "ABLE", "↔", "DONE"),
    ("Employment Rail", "WORK", "↔", "CASH"),
    ("Entrepreneurship", "IDEA", "→", "BIZ"),
    ("Business Owner", "OWN", "↔", "BIZ"),
    ("Asset Ownership", "OWN", "↔", "SAFE"),
    ("Property Rights", "LAW", "↔", "OWN"),
    ("Fin Inclusion", "ALL", "↔", "CASH"),
    ("Banking Access", "BANK", "↔", "CASH"),
    ("Digital Finance", "NET", "↔", "CASH"),
    ("Digital Payment", "PAY", "↔", "FAST"),
    ("Savings Rail", "SAVE", "↔", "SAFE"),
    ("Investment Path", "CASH", "→", "GROW"),
    ("Fin Literacy", "KNOW", "↔", "CASH"),
    ("Credit Access", "LOAN", "↔", "DO"),
    ("Resp Borrowing", "SAFE", "↔", "LOAN"),
    ("Microenterprise", "ONE", "↔", "BIZ"),
    ("Small Business", "TEAM", "↔", "BIZ"),
    ("Entr Ecosystem", "LINK", "↔", "ALL"),
    ("Startup Capital", "CASH", "→", "IDEA"),
    ("Venture Capital", "CASH", "→", "FAST"),
    ("Bootstrapping", "SELF", "↔", "GROW"),
    ("Comm Finance", "ALL", "↔", "CASH"),
    ("Cooperatives", "MANY", "↔", "ONE"),
    ("Social Entr", "BIZ", "↔", "HELP"),
    ("Economic Dignity", "SELF", "↔", "TRUE"),
    ("Productive Opp", "DO", "↔", "GROW"),
    ("Job Creation", "BIZ", "→", "WORK"),
    ("Productivity", "FAST", "↔", "DONE"),
    ("Technology Rail", "TECH", "↔", "ABLE"),
    ("Digital Entr", "ONE", "↔", "GLOB"),
    ("Software Entr", "CODE", "↔", "GLOB"),
    ("Freelancing Path", "ONE", "→", "GLOB"),
    ("Remote Work", "HERE", "↔", "GLOB"),
    ("Digital Exports", "HOME", "→", "CASH"),
    ("Global Markets", "ALL", "↔", "NET"),
    ("Local Entr", "HERE", "→", "FIX"),
    ("Agriculture", "FARM", "↔", "BASE"),
    ("Agri Productiv", "DATA", "↔", "FARM"),
    ("Farmer Access", "FARM", "↔", "LINK"),
    ("Value Chains", "BASE", "↔", "TOP"),
    ("Manufacturing", "MAKE", "↔", "BASE"),
    ("Industrialize", "GRID", "↔", "MAKE"),
    ("Services Rail", "HELP", "↔", "CASH"),
    ("Tech Services", "CODE", "↔", "HELP"),
    ("Creative Econ", "MAKE", "↔", "CASH"),
    ("Cultural Econ", "PAST", "↔", "CASH"),
    ("Tourism Path", "SEE", "↔", "CASH"),
    ("Diaspora Connect", "GLOB", "↔", "HOME"),
    ("Remittance Rail", "CASH", "→", "HOME"),
    ("Diaspora Invest", "CASH", "→", "BIZ"),
    ("Human Capital", "WISE", "↔", "BASE"),
    ("Talent Path", "ABLE", "↔", "STAY"),
    ("Youth Potential", "YOUN", "→", "GROW"),
    ("Women Econ Part", "GIRL", "↔", "DO"),
    ("Inclusive Growth", "ALL", "↔", "GROW"),
    ("Rural Economy", "HERE", "↔", "BASE"),
    ("Urban Economy", "CITY", "↔", "LINK"),
    ("Small City Rail", "ONE", "↔", "LINK"),
    ("Digital Connect", "HERE", "↔", "GLOB"),
    ("Digital Divide", "HAVE", "≠", "NONE"),
    ("Afford Internet", "CASH", "↔", "NET"),
    ("Digital Skills", "ABLE", "↔", "TECH"),
    ("Info Access", "INFO", "↔", "WISE"),
    ("Market Info", "DATA", "↔", "BIZ"),
    ("Transparency", "OPEN", "↔", "TRUE"),
    ("Inst Trust", "TRUE", "↔", "SAFE"),
    ("Rule of Law", "RULE", "↔", "TRUE"),
    ("Contracts Rail", "RULE", "↔", "DO"),
    ("Competition", "TWO", "↔", "BEST"),
    ("Market Access", "ALL", "↔", "BUY"),
    ("Trade Path", "HERE", "↔", "GLOB"),
    ("Exports Rail", "HOME", "→", "GLOB"),
    ("Imports Rail", "GLOB", "→", "HOME"),
    ("Balanced Dev", "GROW", "↔", "SAFE"),
    ("Infrastructure", "GRID", "↔", "BASE"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g186-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g186-{index}-title g186-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g186-{index}-title">{safe}</title><desc id="g186-{index}-desc">An economic empowerment relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g186-{index}-caption" class="diagram-caption">{index}. {safe} — Economic empowerment relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Economic Empowerment Framework</title><desc id="hero-desc">A diagram showing the 2026 economic empowerment landscape, featuring Pakistan's 92% digital retail payments, the $10.9T global startup ecosystem value, and the shift from consumers to owners.</desc><defs><linearGradient id="h186-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h186-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE ECONOMIC EMPOWERMENT LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">PAKISTAN RETAIL: 92% DIGITAL TRANSACTIONS (2026)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">GLOBAL STARTUP VALUE: $10.9 TRILLION (2026)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">FINTECH MARKET: $328.6B GROWING AT 25% CAGR</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">LATE-STAGE FUNDING RECOVERY: $210B (2025)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">WOMEN, BUSINESS & LAW 2026: POLICY REFORMS</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: FROM CONSUMERS TO OWNERS</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">EMPOWERMENT: EARN, CREATE, OWN & PROSPER</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">ECONOMIC EMPOWERMENT</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Building the Capacity to Earn, Create, Own, and Prosper: Capable Participants and Builders.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Economic Empowerment Loop: Navigating the 2026 landscape where digital financial inclusion, global startup recovery, and inclusive policy reforms ensure that individuals and communities can participate meaningfully in the global economy.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 186</title>
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
            <p class="section-label">PAGE 186</p>
            <h2>ECONOMIC EMPOWERMENT</h2>
            <p>“Building the Capacity to Earn, Create, Own, and Prosper.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Economic empowerment begins with opportunity. It means giving individuals, families, and businesses the ability to participate meaningfully in economic life. It is not simply about income; it includes access to education, employment, entrepreneurship, financial services, and property rights. A person becomes more economically empowered when they have greater capacity to make productive choices about their future. The objective is not merely to create consumers, but to create capable participants, builders, owners, and contributors to the economy.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Digital Finance & Retail Transformation (2026)</h3>
                <p>By 2026, Pakistan's financial future has leveled up significantly, with **92% of retail payment transactions** now being digital [1]. In the third quarter of fiscal year 2026 alone, 3.4 billion digital payments were recorded, reflecting a massive shift toward a fintech-driven ecosystem [2]. The global fintech market is projected to grow from **$328.66 billion in 2026** to nearly $2 trillion by 2034, driven by digital financial services that lower costs and increase the speed and transparency of transactions [3] [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Global Startup Recovery & Ecosystem Value</h3>
                <p>The *Global Startup Ecosystem Report 2026* indicates that the global ecosystem value has grown by **40% in one year**, reaching a staggering **$10.9 trillion** [5]. After two years of contraction, startup funding has stabilized and begun to grow, with late-stage funding rising by 17% in 2025 to around **$210 billion** [6] [7]. This recovery is visible across both early and late-stage investments, providing entrepreneurs with the capital necessary to develop products and reach international markets through digital platforms [8] [9].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Inclusive Growth & Legal Frameworks</h3>
                <p>Economic growth becomes more broadly empowering when it is truly inclusive. The *Women, Business and the Law 2026* report highlights how legal and policy frameworks shape economic opportunities for women in 190 countries [10]. Expanding access to education, employment, and finance strengthens individual opportunity and contributes to broader human development [11]. In 2026, there is a sharper lens on the social and economic return of investments, ensuring that benefits cascade beyond individual firms to entire communities [12] [13].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Connectivity & Productive Opportunity</h3>
                <p>Internet access is no longer just a social service; it is a foundation for economic participation. Digital platforms allow individuals to create businesses with relatively low physical infrastructure requirements, reaching customers beyond their immediate geography [14]. Software exports, freelancing, and remote work are generating international revenue and connecting skilled workers with global clients [15]. For the Orakzai community, the **Sovereign Grid** ensures that economic empowerment is built on a foundation of authentic ownership and institutional trust [16].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Economic Empowerment</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, economic empowerment is the modern expression of our self-reliance. We do not just want to participate in the economy; we want to own our part of it. By mastering digital finance and global entrepreneurship while remaining rooted in our values of integrity and dignity, we are building a sovereign future where our talent is respected and our prosperity is our own. We are the builders of a legacy that is productive, inclusive, and enduring.”</p>
            </div>

            <div class="final-statement">
                CREATE VALUE.<br>
                OWN THE FUTURE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Instagram / Fintech Insights, <em>Pakistan's Financial Future: 92% Digital Retail Transactions (June 2026)</em>.</li>
                    <li>ResearchGate, <em>Digital Financial Services in Pakistan: Opportunities and Infrastructure (June 2026)</em>.</li>
                    <li>Market Data Forecast, <em>Global Fintech Market Size, Share & Analysis Report 2034 (August 2026)</em>.</li>
                    <li>World Bank Group, <em>Financial Inclusion: Digital Financial Services and Fintech (2026)</em>.</li>
                    <li>Startup Genome, <em>The Global Startup Ecosystem Report 2026: Ecosystem Value Hits $10.9T (July 2026)</em>.</li>
                    <li>LinkedIn / Nikhil Ceng, <em>2026 Global Startup Ecosystem: Measured Recovery and Funding Trends (July 2026)</em>.</li>
                    <li>Facebook / Unleashing Ideas, <em>GEN and Startup Genome Launch 2026 Global Startup Ecosystem Report (July 2026)</em>.</li>
                    <li>Mastercard Center, <em>Shaping Inclusive Economic Growth in 2026: From Evidence to Implementation (January 2026)</em>.</li>
                    <li>YouTube / Mastercard Forum, <em>2026 Global Inclusive Growth Forum: Senior Leaders and Public Sector (May 2026)</em>.</li>
                    <li>World Bank / Facebook, <em>Women, Business and the Law 2026: Legal Frameworks and Policy (May 2026)</em>.</li>
                    <li>UN Women, <em>Gender Equality and Inclusive Growth: Economic Policies for Decent Work (2026)</em>.</li>
                    <li>Center for Global Development, <em>Gender Equality and Inclusion: Policies and Investments (2026)</em>.</li>
                    <li>Atlantic Council, <em>Inclusive Growth Initiative: Best Practices and Community Sharing (2026)</em>.</li>
                    <li>Facebook / iPath Tech, <em>Digital Trust & Financial Inclusion Summit 2026: Payments and Fintech (July 2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Economic Empowerment and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            186
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

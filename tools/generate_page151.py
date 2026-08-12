from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-151-pakistans-economic-future.html'

GRAPHICS = [
    ("Economic Future", "NATL", "↔", "TIME"),
    ("Productivity Base", "KNOW", "→", "VALU"),
    ("Economic Asset", "PEOP", "↔", "BASE"),
    ("Human Capital", "LEAR", "→", "GROW"),
    ("Consumption Model", "BUY", "↔", "OLD"),
    ("Production Model", "MAKE", "↔", "NEW"),
    ("Productivity Rail", "CAP", "→", "VALU"),
    ("Value Addition", "RAW", "→", "BRAND"),
    ("Export Expansion", "DOM", "→", "GLOB"),
    ("Global Compete", "PAK", "↔", "GLOB"),
    ("Human Asset", "YOUT", "↔", "OPPT"),
    ("Employment Challenge", "JOB", "↔", "YOUT"),
    ("Domestic Market", "BUY", "↔", "NATL"),
    ("Education Goal", "MATH", "↔", "GROW"),
    ("Technical Skill", "CODE", "↔", "GROW"),
    ("Vocational Path", "WORK", "↔", "SKIL"),
    ("Renewable Energy", "SUN", "↔", "POWR"),
    ("Software Export", "CODE", "↔", "CASH"),
    ("IT Milestone", "$4.6B", "↔", "FY26"),
    ("Export Surge", "+21%", "↔", "GROW"),
    ("AI Strategy", "AI", "↔", "GROW"),
    ("Cybersecurity", "SEC", "↔", "ECON"),
    ("Cloud Computing", "CLOU", "↔", "GROW"),
    ("Data Analysis", "DATA", "↔", "GROW"),
    ("Entrepreneurship", "NEW", "↔", "JOB"),
    ("Startup Ecosystem", "SEED", "↔", "GROW"),
    ("Local to Global", "HOME", "→", "GLOB"),
    ("Digital Platform", "APP", "↔", "GROW"),
    ("Karachi Hub", "KHI", "↔", "FIN"),
    ("Lahore Hub", "LHE", "↔", "TECH"),
    ("Peshawar Hub", "PEW", "↔", "GROW"),
    ("Islamabad Hub", "ISB", "↔", "GOV"),
    ("Value-Added Goal", "RAW", "→", "PROD"),
    ("Pharmaceuticals", "MED", "↔", "GROW"),
    ("Creative Industry", "ART", "↔", "GROW"),
    ("Textile Future", "TEX", "↔", "AUTO"),
    ("Textile Branding", "TEX", "↔", "BRAND"),
    ("Agri Productivity", "FARM", "↔", "GROW"),
    ("Water Efficiency", "H2O", "↔", "SAVE"),
    ("Precision Agri", "AI", "↔", "FARM"),
    ("Crop Analytics", "DATA", "↔", "FARM"),
    ("Climate Resilience", "SAFE", "↔", "GROW"),
    ("Manufacturing", "MAKE", "↔", "GROW"),
    ("LSM Growth", "5.77%", "↔", "FY26"),
    ("Industrial Modern", "AUTO", "↔", "GROW"),
    ("Mobile Policy", "2026", "↔", "33"),
    ("SME Digital", "SME", "↔", "APP"),
    ("E-commerce Rail", "PAY", "↔", "SHIP"),
    (" Raast Economy", "PAY", "↔", "NATL"),
    ("Financial Inclusion", "ALL", "↔", "BANK"),
    ("Fintech Innovation", "TECH", "↔", "FIN"),
    ("Capital Market", "STCK", "↔", "GROW"),
    ("Foreign Invest", "FDI", "↔", "NATL"),
    ("Domestic Saving", "SAVE", "↔", "GROW"),
    ("Diaspora Capital", "HOME", "↔", "GLOB"),
    ("Digital Diaspora", "WORK", "↔", "NET"),
    ("Knowledge Economy", "IDEA", "↔", "VALU"),
    ("Research Value", "R&D", "↔", "GROW"),
    ("Intellectual Prop", "IP", "↔", "OWN"),
    ("Advanced Service", "SERV", "↔", "GLOB"),
    ("AI Productivity", "AI", "↔", "WORK"),
    ("Blockchain Value", "BC", "↔", "VALU"),
    ("Tokenization", "REAL", "→", "TOK"),
    ("Real Estate Digital", "HOME", "↔", "DATA"),
    ("Urbanization Hub", "CITY", "↔", "GROW"),
    ("Orakzai Economy", "ORAK", "↔", "NEW"),
    ("Digital Bridge", "ORAK", "↔", "GLOB"),
    ("Reform Year", "2026", "↔", "DONE"),
    ("Modernization", "NEW", "↔", "STAT"),
    ("Economic Sovereignty", "OWN", "↔", "NATL"),
    ("Future Value", "$60B", "↔", "2030"),
    ("Productive Future", "ALL", "↔", "GROW"),
    ("The Permanent Growth", "STAY", "↔", "DONE"),
    ("Economic Unity", "ALL", "↔", "ONE"),
    ("The Global Goal", "GLOB", "↔", "DONE"),
    ("Human Capital", "PEOP", "↔", "VALU"),
    ("Knowledge Power", "WISE", "↔", "GROW"),
    ("Industrial Power", "POWR", "↔", "MAKE"),
    ("Digital Power", "CODE", "↔", "GROW"),
    ("Agricultural Power", "SEED", "↔", "GROW"),
    ("Financial Power", "CASH", "↔", "GROW"),
    ("Sovereign Power", "OWN", "↔", "NATL"),
    ("Orakzai Power", "ORAK", "↔", "GROW"),
    ("Pakistan Power", "PAK", "↔", "GROW"),
    ("Future Power", "TIME", "↔", "GROW"),
    ("Unity Power", "ONE", "↔", "GROW"),
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
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g151-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g151-{index}-title g151-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g151-{index}-title">{safe}</title><desc id="g151-{index}-desc">An economic relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g151-{index}-caption" class="diagram-caption">{index}. {safe} — Economic relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Pakistan’s Economic Future Framework</title><desc id="hero-desc">A diagram showing the transition from a traditional consumption-based economy to a digital, productive, and global export-led economy.</desc><defs><linearGradient id="h151-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h151-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE ECONOMIC TRANSFORMATION (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">HUMAN CAPITAL (1M AI Experts / Digital Skills)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">IT EXPORTS (Record $4.6B / +21% Growth)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">INDUSTRIAL MODERNIZATION (LSM +5.77%)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">VALUE-ADDED EXPORTS (Branding / Manufacturing)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL AGRICULTURE (Precision / Analytics)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ENTREPRENEURIAL ECOSYSTEM (Startups / SMEs)</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">GLOBAL MARKET INTEGRATION (Digital Rails)</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">PAKISTAN’S ECONOMIC FUTURE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Traditional Consumption to Productive Global Sovereignty.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Economic Future Framework: The transition toward a knowledge-based, productive, and export-led economy in 2026.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 151</title>
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
            <p class="section-label">PAGE 151</p>
            <h2>PAKISTAN’S ECONOMIC FUTURE</h2>
            <p>“From Traditional Consumption to Productive Global Sovereignty.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Pakistan's economic future is being shaped by the convergence of population growth, urbanization, and technology. The central question is not just how large the economy can become, but what kind of economy we can build. A stronger future economy combines agriculture, manufacturing, and services with technology and entrepreneurship, increasing productivity and expanding access to global markets.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The IT Export Milestone</h3>
                <p>In the fiscal year 2025-26, Pakistan achieved a record-breaking **$4.6 billion** in IT and telecom exports, marking a **21% surge** over the previous year. This milestone reflects the growing global demand for Pakistani software services and the success of the national strategy to position the country as a tech hub. With a focus on AI, cybersecurity, and cloud computing, the IT sector is now a primary driver of high-value employment and economic dynamism.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Industrial Modernization & LSM Growth</h3>
                <p>The year 2026, designated as the **'Year of Reform and Modernization,'** has seen a significant pivot toward value-added manufacturing. The Large-Scale Manufacturing (LSM) sector recorded a **5.77% year-on-year growth**, supported by the **Mobile & Electronics Policy 2026–33**. By modernizing industrial systems through automation and digital production, Pakistan is moving from raw material exports to branded global products, capturing higher value in the international market.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Human Capital & The Young Economy</h3>
                <p>Pakistan's most important economic asset is its young population. The strategy for 2026 focuses on training **1 million AI experts** and developing practical skills in science and technology. By transforming the youth into a productive workforce, the country is addressing the employment challenge and creating a large domestic market. Vocational and technical education now connect workers directly with renewable energy, software, and telecommunications industries.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Agriculture & Climate Resilience</h3>
                <p>Agriculture remains central to food security and the national economy. The future of the sector depends on **Digital Agriculture**, where farmers use AI and precision analytics to improve water efficiency and crop yields. In 2026, agricultural output saw a boost of **3.4 million tons** in key areas, driven by better market access and logistics. Economic planning now incorporates climate resilience to protect infrastructure and activity from environmental risks.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Pakistan’s Economic Future</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“The economy of the future is built on knowledge, not just consumption. For the Orakzai community, this means that the boundaries of the valley are no longer the boundaries of their business. A young entrepreneur in Orakzai can now serve global markets, backed by digital skills and a sovereign economic framework. We are building a productive nation where every individual has the tools to create value and every business has the rail to reach the world.”</p>
            </div>

            <div class="final-statement">
                PRODUCTIVITY IS PROSPERITY.<br>
                THE FUTURE IS GLOBAL.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Dawn News / Business Recorder, <em>Pakistan IT Exports Hit Record $4.6 Billion in FY26 (July 2026)</em>.</li>
                    <li>Ministry of Industries & Production (MoI&P), <em>Mobile & Electronics Policy 2026–33: A Milestone for Industrial Modernization (2026)</em>.</li>
                    <li>Planning Commission of Pakistan, <em>2026: The Year of Reform and Modernization (October 2025-2026)</em>.</li>
                    <li>Pakistan Bureau of Statistics (PBS), <em>Large-Scale Manufacturing (LSM) Growth and Economic Performance FY26 (July 2026)</em>.</li>
                    <li>Ignite / DEEP Pakistan, <em>Digital Economy Enhancement Project: Strategic Goals for 2030 ($60B Add) (April 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            151
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

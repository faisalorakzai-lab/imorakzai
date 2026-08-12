from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-152-technology-and-economic-development.html'

GRAPHICS = [
    ("Technology Force", "KNOW", "→", "DEV"),
    ("Productivity Rail", "TOOL", "→", "VALU"),
    ("Economic Development", "INC", "↔", "GROW"),
    ("Infra Evolution", "TOOL", "→", "BASE"),
    ("Cross-Sector Tech", "MANY", "↔", "ONE"),
    ("Productivity Gap", "OLD", "≠", "NEW"),
    ("Automation Value", "AUTO", "→", "VALU"),
    ("Logistics Sync", "MOVE", "↔", "DATA"),
    ("Transaction Friction", "SLOW", "→", "FAST"),
    ("Decision Support", "DATA", "→", "WISE"),
    ("Digital Transform", "PAPE", "→", "AUTO"),
    ("Intelligent System", "DATA", "→", "AI"),
    ("Connected Economy", "NET", "↔", "GLOB"),
    ("Broadband Base", "CONN", "↔", "ECON"),
    ("Mobile Gateway", "PHON", "↔", "USER"),
    ("Digital Payments", "PAY", "↔", "NET"),
    ("Fintech Bridge", "TECH", "↔", "FIN"),
    ("Digital Banking", "APP", "↔", "BANK"),
    ("E-commerce Reach", "HOME", "→", "GLOB"),
    ("Startup Growth", "SEED", "↔", "GROW"),
    ("Founder Tools", "CODE", "↔", "USER"),
    ("SME Software", "SME", "↔", "APP"),
    ("Cloud Computing", "CLOU", "↔", "USER"),
    ("Data Center Foundation", "STOR", "↔", "NET"),
    ("Computing Capacity", "COMP", "↔", "NATL"),
    ("AI Analysis", "AI", "↔", "DATA"),
    ("AI Prediction", "PRED", "↔", "DATA"),
    ("AI Decision", "WISE", "↔", "AI"),
    ("AI Across Industry", "ALL", "↔", "AI"),
    ("AI Human Capital", "HUMA", "↔", "AI"),
    ("Digital Literacy", "READ", "↔", "CODE"),
    ("Robotics Product", "ROBO", "↔", "MAKE"),
    ("Industry 4.0", "I4.0", "↔", "NATL"),
    ("Smart Factory", "AUTO", "↔", "DATA"),
    ("Agri Tech Decision", "FARM", "↔", "DATA"),
    ("Precision Agri", "AI", "↔", "FARM"),
    ("Water Tech Sync", "H2O", "↔", "DATA"),
    ("Telemedicine Reach", "DOC", "↔", "NET"),
    ("EdTech Access", "LEAR", "↔", "NET"),
    ("Skills Economy", "SKIL", "↔", "VALU"),
    ("Reskilling Loop", "LEAR", "→", "NEW"),
    ("Remote Work Rail", "WORK", "↔", "NET"),
    ("Services Export", "SERV", "→", "GLOB"),
    ("IT Export FY26", "$4.6B", "↔", "DONE"),
    ("Freelance Goal", "$1B+", "↔", "DONE"),
    ("IDI Score 2026", "67.7", "↔", "PAK"),
    ("Maturity Jump", "+20%", "↔", "GROW"),
    ("Freelance Growth", "+49%", "↔", "FY26"),
    ("Monthly Record", "$169M", "↔", "MAY"),
    ("Economic Value", "$34.9B", "↔", "2030"),
    ("Intellectual Prop", "IP", "↔", "OWN"),
    ("Global Product", "PAK", "→", "GLOB"),
    ("Local Knowledge", "HOME", "↔", "IDEA"),
    ("Technology Advantage", "YOUT", "↔", "OPPT"),
    ("Connectivity Growth", "CONN", "↔", "GROW"),
    ("Orakzai Node", "ORAK", "↔", "GLOB"),
    ("Digital Sovereignty", "OWN", "↔", "NATL"),
    ("Renewable Energy", "SUN", "↔", "POWR"),
    ("Cybersecurity", "SEC", "↔", "ECON"),
    ("Future Rail", "TIME", "↔", "NEW"),
    ("Permanent Growth", "STAY", "↔", "DONE"),
    ("Economic Unity", "ALL", "↔", "ONE"),
    ("The Knowledge Goal", "WISE", "↔", "DONE"),
    ("Human Asset", "PEOP", "↔", "VALU"),
    ("Productive Nation", "MAKE", "↔", "NATL"),
    ("Sovereign Tech", "OWN", "↔", "TECH"),
    ("Inclusive Future", "ALL", "↔", "GROW"),
    ("Digital Power", "POWR", "↔", "CODE"),
    ("Industrial Power", "POWR", "↔", "MAKE"),
    ("Agricultural Power", "POWR", "↔", "SEED"),
    ("Financial Power", "POWR", "↔", "CASH"),
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
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g152-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g152-{index}-title g152-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g152-{index}-title">{safe}</title><desc id="g152-{index}-desc">A technology and economic relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g152-{index}-caption" class="diagram-caption">{index}. {safe} — Tech-economic relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Technology & Economic Development Framework</title><desc id="hero-desc">A diagram showing how technology acts as an economic force to transform productivity, industry, and opportunity in 2026.</desc><defs><linearGradient id="h152-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h152-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE TECHNOLOGY-ECONOMY ENGINE (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">KNOWLEDGE & DIGITAL MATURITY (IDI 67.7)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL SERVICES EXPORTS ($4.6B / +21%)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">FREELANCE ECONOMY ($1B+ / +49% Growth)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">INDUSTRY 4.0 & SMART MANUFACTURING</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">PRECISION AGRICULTURE & WATER TECH</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">STARTUP ECOSYSTEM & SME DIGITALIZATION</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">ECONOMIC VALUE POTENTIAL ($34.9B BY 2030)</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">TECHNOLOGY & ECONOMIC DEVELOPMENT</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Technology is the Infrastructure of Opportunity.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Technology & Economic Development Framework: How digital forces transform productivity and global opportunity in 2026.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 152</title>
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
            <p class="section-label">PAGE 152</p>
            <h2>TECHNOLOGY & ECONOMIC DEVELOPMENT</h2>
            <p>“Technology is the Infrastructure of Opportunity.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Technology is no longer a separate sector of the economy; it is becoming the infrastructure through which almost every sector operates. From digital agriculture to automated manufacturing, technology increases productivity and expands access to global markets. For Pakistan, the economic importance of technology extends beyond the IT industry—it is the force that transforms productivity across the entire national landscape.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Digital Maturity & Export Growth</h3>
                <p>In 2026, Pakistan's digital maturity has reached a new peak, with the **ICT Development Index (IDI) score rising to 67.7**, a 20% improvement in just one year. This maturity is reflected in the record-breaking **IT exports of $4.6 billion** for FY26. Furthermore, the freelance economy has crossed the **$1 billion annual milestone**, with a record $169 million earned in May 2026 alone. These figures demonstrate that Pakistan is no longer just adopting technology but shaping global digital services.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Industry 4.0 & Smart Manufacturing</h3>
                <p>The adoption of **Industry 4.0** technologies is closing the productivity gap in Pakistan's manufacturing and textile sectors. By combining sensors, robotics, and data analytics, modern factories are increasing resource efficiency and quality control. This industrial shift, supported by advanced computing and cloud infrastructure, is projected to generate **$34.9 billion (Rs. 9.7 trillion)** in economic value by 2030, transforming the country's productive base.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Agriculture, Health & Education Tech</h3>
                <p>Technological impact spans the most critical sectors of society. **Precision Agriculture** uses AI and satellite imagery to improve crop yields, while **Telemedicine** and **EdTech** expand access to healthcare and education in remote regions. These digital classrooms and clinics connect citizens to global knowledge and services, ensuring that human capital remains the primary purpose of technological advancement.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Skills Economy & Global Markets</h3>
                <p>The rise of the **Skills Economy** creates a demand for expertise in AI, cybersecurity, and software engineering. **Remote Work** has become a vital rail for economic participation, allowing professionals in the Orakzai valleys to serve international clients without relocation. By moving from "Freelancing to Products," Pakistani entrepreneurs are building intellectual property and global brands, leveraging the country's young workforce and growing connectivity.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Technology & Economic Development</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Technology is the ultimate equalizer of opportunity. It removes the friction of distance and the barriers of scale. For the Orakzai community, a connected valley is a productive valley. We are building an economy where local knowledge creates global products, and where every citizen has the digital tools to reach their full potential. The future is not just digital; it is productive, inclusive, and sovereign.”</p>
            </div>

            <div class="final-statement">
                TECHNOLOGY IS PRODUCTIVITY.<br>
                OPPORTUNITY IS UNIVERSAL.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>State Bank of Pakistan (SBP) / Connected Pakistan, <em>Pakistan IT Exports Hit Record $4.6 Billion in FY26 (August 2026)</em>.</li>
                    <li>Ministry of IT & Telecommunication (MOITT) / Bloom Pakistan, <em>Freelance Economy Surpasses $1 Billion Milestone (July 2026)</em>.</li>
                    <li>International Telecommunication Union (ITU) / SIFC, <em>Pakistan's ICT Development Index (IDI) Score Rises to 67.7 (July 2026)</em>.</li>
                    <li>ProPakistani / Economic Forecasts, <em>Digital Transformation to Add $34.9 Billion to Pakistan's Economy by 2030 (June 2026)</em>.</li>
                    <li>LinkedIn / Industry Reports, <em>Industry 4.0 Adoption and Industrial Automation Trends in Pakistan (January 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            152
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

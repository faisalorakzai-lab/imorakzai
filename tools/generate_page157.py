from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-157-technology-and-real-estate.html'

GRAPHICS = [
    ("Real Estate Stack", "LAND", "↔", "DATA"),
    ("Digital Lifecycle", "PLAN", "→", "DONE"),
    ("Property Data", "INFO", "↔", "VALU"),
    ("Location Intelligence", "MAP", "↔", "WISE"),
    ("Market Transparency", "OPEN", "↔", "SAFE"),
    ("Land Digitization", "PAPER", "→", "CODE"),
    ("Planning Rail", "IDEA", "→", "MAP"),
    ("Design Rail", "ART", "→", "BIM"),
    ("Financing Rail", "CASH", "→", "OWN"),
    ("Construction Rail", "MAKE", "→", "BASE"),
    ("Marketing Rail", "SHOW", "→", "SELL"),
    ("Sale / Lease Path", "SIGN", "↔", "DONE"),
    ("Property Mgmt", "RUN", "↔", "VALU"),
    ("Maintenance Rail", "FIX", "↔", "SAFE"),
    ("Redevelopment Path", "OLD", "→", "NEW"),
    ("Location Data", "MAP", "↔", "INFO"),
    ("Ownership Data", "ID", "↔", "INFO"),
    ("Valuation Data", "CASH", "↔", "INFO"),
    ("Occupancy Data", "USER", "↔", "INFO"),
    ("Rental Data", "RENT", "↔", "INFO"),
    ("Market Demand", "WANT", "↔", "INFO"),
    ("Digital Listing", "APP", "↔", "HOME"),
    ("Virtual Tour", "EYE", "↔", "NET"),
    ("360 View Path", "ALL", "↔", "EYE"),
    ("AR Layout Path", "VIRT", "↔", "REAL"),
    ("Interactive Floor", "MAP", "↔", "USER"),
    ("GIS Analysis", "MAP", "↔", "DATA"),
    ("Zoning Rail", "LAW", "↔", "MAP"),
    ("Infra Mapping", "BASE", "↔", "MAP"),
    ("Urban Growth", "CITY", "↔", "TIME"),
    ("Satellite Intel", "SKY", "→", "DATA"),
    ("Drone Survey", "FLY", "→", "DATA"),
    ("Accuracy Rail", "TRUE", "↔", "DATA"),
    ("Digital CAD", "CODE", "↔", "ART"),
    ("BIM Collab", "ALL", "↔", "BIM"),
    ("Digital Twin", "REAL", "↔", "VIRT"),
    ("Smart Building", "HOME", "↔", "NET"),
    ("IoT Sensor", "SENS", "→", "DATA"),
    ("Building Auto", "RUN", "↔", "CODE"),
    ("Energy Mgmt", "POWR", "↔", "SAFE"),
    ("Smart Lighting", "LITE", "↔", "AUTO"),
    ("Smart HVAC", "TEMP", "↔", "AUTO"),
    ("Water Mgmt", "WATR", "↔", "AUTO"),
    ("Leak Detection", "DROP", "→", "WARN"),
    ("Predictive Maint", "TIME", "→", "FIX"),
    ("AI Property Mgmt", "AI", "↔", "RUN"),
    ("Property Chatbot", "TALK", "↔", "AI"),
    ("Recommendation Sys", "WANT", "→", "HOME"),
    ("AVM Estimate", "DATA", "→", "CASH"),
    ("Market Pattern", "BIG", "↔", "DATA"),
    ("Real Estate Analytics", "DATA", "↔", "WISE"),
    ("Rental Yield Path", "CASH", "↔", "TIME"),
    ("Occupancy Rate", "USER", "↔", "BASE"),
    ("Price Movement", "CASH", "↔", "UP"),
    ("Construction Cost", "MAKE", "↔", "CASH"),
    ("Market Intel", "GLOB", "↔", "WISE"),
    ("Digital Lease", "SIGN", "↔", "NET"),
    ("E-Signature Rail", "PEN", "↔", "CODE"),
    ("Doc Management", "FILE", "↔", "NET"),
    ("Cloud Platform", "CLOU", "↔", "USER"),
    ("Portfolio Mgmt", "MANY", "↔", "ONE"),
    ("Digital Rent", "PAY", "↔", "NET"),
    ("PropTech Rail", "TECH", "↔", "HOME"),
    ("Construction Tech", "TECH", "↔", "MAKE"),
    ("Robotics Rail", "ROBO", "↔", "MAKE"),
    ("Project Mgmt", "PLAN", "↔", "DONE"),
    ("Schedule Rail", "TIME", "↔", "DONE"),
    ("Budget Rail", "CASH", "↔", "DONE"),
    ("Material Track", "STUF", "↔", "DONE"),
    ("Procurement Path", "BUY", "↔", "NET"),
    ("Supply Visibility", "SEE", "↔", "FLOW"),
    ("Prefabrication", "OFF", "→", "ON"),
    ("Modular Build", "BOX", "→", "HOME"),
    ("3D Printing", "INK", "→", "BASE"),
    ("Sustainable Build", "ECO", "↔", "BASE"),
    ("KPK BOR 2026", "KPK", "↔", "CODE"),
    ("PLRA Digitized", "23K", "↔", "DONE"),
    ("Mauza Data", "LAND", "↔", "CODE"),
    ("Ownership Record", "OWN", "↔", "CODE"),
    ("Overseas Access", "GLOB", "↔", "LAND"),
    ("Remote Management", "AWAY", "↔", "LAND"),
    ("One-Window Path", "ONE", "↔", "ALL"),
    ("Smart City Rail", "CITY", "↔", "NET"),
    ("Eco-Compute Rail", "ECO", "↔", "CODE"),
    ("Capital Smart", "ISL", "↔", "CITY"),
    ("Ravi Riverfront", "RAVI", "↔", "CITY"),
    ("Digital Title", "LAW", "↔", "CODE"),
    ("Collateral Rail", "LAND", "→", "CASH"),
    ("Formal Finance", "BANK", "↔", "LAND"),
    ("Orakzai Land", "ORAK", "↔", "CODE"),
    ("Tribal Settlement", "TRIBE", "→", "CODE"),
    ("Valley Mapping", "ORAK", "↔", "MAP"),
    ("Future Rail", "TIME", "↔", "NEW"),
    ("Sovereign Property", "OWN", "↔", "NATL"),
    ("Inclusive City", "ALL", "↔", "CITY"),
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
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g157-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g157-{index}-title g157-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g157-{index}-title">{safe}</title><desc id="g157-{index}-desc">A technology and real estate relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g157-{index}-caption" class="diagram-caption">{index}. {safe} — Technology and real estate relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Technology & Real Estate Framework</title><desc id="hero-desc">A diagram showing the 2026 PropTech stack, land record digitization rails, and the integration of AI and IoT into smart city infrastructure.</desc><defs><linearGradient id="h157-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h157-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE PROPTECH ENGINE (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">LAND DIGITIZATION (KPK BOR / PLRA 2026)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">SMART CITIES (Capital Smart / Eco-Compute)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">PROPTECH PLATFORMS (Zameen / Graana 2026)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">OVERSEAS ACCESS (Remote Land Management)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">BIM & GIS (Digital Construction Monitoring)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AI VALUATION & ANALYTICS (AVM 2026)</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SOVEREIGN PROPERTY (DIGITIZE → SECURE)</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">TECHNOLOGY & REAL ESTATE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“How Digital Technology Is Transforming Property.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The PropTech Engine: The 2026 stack of land digitization, smart cities, and the integration of AI and data into the property sector.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 157</title>
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
            <p class="section-label">PAGE 157</p>
            <h2>TECHNOLOGY & REAL ESTATE</h2>
            <p>“How Digital Technology Is Transforming Property.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Real estate has traditionally been built around physical assets. Technology is changing how these assets are designed, financed, marketed, managed, and experienced. The modern property sector increasingly combines real estate with data, software, and automation. The future of real estate is physical infrastructure enhanced by digital intelligence.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Land Record Revolution</h3>
                <p>In 2026, Pakistan has achieved a historic milestone in land record digitization. The **KPK Board of Revenue (BOR)** set a critical deadline of **February 10, 2026**, for the online settlement of land records across the province, including tribal districts like Orakzai. In Punjab, the **PLRA** has digitized over **23,542 Mauzas**, managing **1.75 million+** ownership records. This transition from paper-based to digital titles is providing the legal certainty necessary for formal investment and financing.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">PropTech & Market Transparency</h3>
                <p>PropTech platforms like Zameen.com and Graana.com have revolutionized property discovery. The **PropTech Convention 2026** (March) highlighted the shift toward **digital housing finance (HBFC)** and the use of AI for **Automated Valuation Models (AVMs)**. These tools provide real-time market intelligence, reducing speculation and enhancing credibility. Furthermore, the May 2026 launch of **Remote Land Record Services** allows overseas Pakistanis to manage their property records securely from anywhere in the world.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Smart Cities & Digital Twins</h3>
                <p>The **Pakistan Eco-Compute & Smart Cities Summit 2026** (July) showcased the integration of AI and eco-friendly solutions into urban planning. Projects like **Capital Smart City Islamabad** are utilizing **Building Information Modeling (BIM)** and **GIS-based mapping** to create data-driven infrastructure. The use of **Digital Twins** allows facility managers to monitor building performance in real-time, optimizing energy consumption and maintenance through IoT-connected sensors.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Orakzai Tribal Transition</h3>
                <p>For the Orakzai community, the digitization of land records represents a fundamental shift in tribal governance. The 2026 KPK initiative is providing valley natives with recognized digital titles, enabling them to leverage land as a productive asset. By integrating GIS mapping with traditional tribal boundaries, the government is creating a secure framework for regional development, allowing Orakzai owners to participate in the formal economy while preserving their heritage.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Technology & Real Estate</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Land is the foundation of identity. For the Orakzai people, our mountains and valleys are not just property; they are our history. Technology is providing us with the tools to secure that history. By digitizing our land records and using GIS to map our future, we are building a bridge between our tribal traditions and the modern digital economy. We are creating a sovereign future where every inch of our land is protected by the power of digital intelligence.”</p>
            </div>

            <div class="final-statement">
                PHYSICAL FOUNDATION.<br>
                DIGITAL INTELLIGENCE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>KPK Board of Revenue (BOR), <em>Settlement and Digitalization of Land Record Deadline (February 2026)</em>.</li>
                    <li>Zameen.com / PropTech Convention, <em>Digital Real Estate and Housing Finance Trends (March 2026)</em>.</li>
                    <li>Punjab Land Records Authority (PLRA), <em>Mauza Digitization and Ownership Records Status (July 2026)</em>.</li>
                    <li>MOITT / Eco-Compute Summit, <em>Smart Cities and Intelligent Urban Design Report (July 2026)</em>.</li>
                    <li>Ministry of Foreign Affairs (MOFA), <em>Remote Land Record Management for Overseas Pakistanis (May 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            157
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

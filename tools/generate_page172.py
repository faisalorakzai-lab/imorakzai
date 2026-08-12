from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-172-what-young-pakistanis-can-build.html'

GRAPHICS = [
    ("Youth Potential", "YOUN", "↔", "GROW"),
    ("Potential to Product", "IDEA", "→", "DONE"),
    ("Build Environment", "BASE", "↔", "ABLE"),
    ("Skill Foundation", "LEAR", "↔", "BASE"),
    ("Software Reach", "CODE", "→", "ALL"),
    ("SaaS Tools", "SUB", "↔", "GLOB"),
    ("Mobile Solutions", "APP", "↔", "USER"),
    ("AI Automation", "AI", "↔", "AUTO"),
    ("AI for Pakistan", "AI", "↔", "HOME"),
    ("Urdu Tech", "LANG", "↔", "NET"),
    ("Regional Lang", "TALK", "↔", "TECH"),
    ("EdTech Access", "LEAR", "↔", "NET"),
    ("AI Education", "AI", "→", "LEAR"),
    ("Digital Library", "BOOK", "↔", "SAVE"),
    ("Research Collab", "SCI", "↔", "LINK"),
    ("HealthTech Admin", "DOC", "↔", "DATA"),
    ("Digital Health", "DOC", "↔", "LINK"),
    ("AgriTech Data", "FARM", "↔", "DATA"),
    ("Climate Tech", "EARTH", "↔", "TECH"),
    ("Water Tech", "SAVE", "↔", "DROP"),
    ("Energy Innov", "SUN", "↔", "GRID"),
    ("Fintech Access", "CASH", "↔", "NET"),
    ("Digital Payment", "PAY", "↔", "FAST"),
    ("Financial Inclus", "ALL", "↔", "CASH"),
    ("Digital Bank", "BANK", "↔", "NET"),
    ("RegTech Flow", "LAW", "↔", "BIZ"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Digital Identity", "SELF", "↔", "NAME"),
    ("Blockchain Infra", "BC", "↔", "BASE"),
    ("Digital Assets", "OWN", "↔", "CODE"),
    ("Tokenization", "OWN", "↔", "NET"),
    ("PropTech Prop", "LAND", "↔", "DATA"),
    ("ConTech Build", "MAKE", "↔", "TECH"),
    ("Logistics Tech", "SHIP", "↔", "MAP"),
    ("E-commerce Net", "BUY", "↔", "SELL"),
    ("Cross-Border", "HOME", "→", "GLOB"),
    ("Digital Export", "CODE", "→", "CASH"),
    ("Creative Industry", "ART", "↔", "TECH"),
    ("Game Dev Path", "PLAY", "↔", "CODE"),
    ("Digital Media", "TALK", "↔", "ALL"),
    ("Digital Publish", "BOOK", "↔", "NET"),
    ("Cultural Tech", "PAST", "↔", "SAVE"),
    ("Digital Archive", "DATA", "↔", "SAVE"),
    ("Orakzai Heritage", "ORAK", "↔", "SAVE"),
    ("Cultural Ownership", "OWN", "↔", "ALL"),
    ("Tourism Tech", "MOVE", "↔", "GLOB"),
    ("Agri Marketplace", "FARM", "↔", "BUY"),
    ("Manufacturing Auto", "AUTO", "↔", "MAKE"),
    ("Robotics Fusion", "BOT", "↔", "PHYS"),
    ("Drone Support", "FLY", "↔", "DATA"),
    ("Advanced Mfg", "NEW", "↔", "MAKE"),
    ("Semiconductor Tal", "CHIP", "↔", "WISE"),
    ("Embedded Systems", "CODE", "↔", "PHYS"),
    ("IoT Connection", "LINK", "↔", "ALL"),
    ("Smart Infra", "CITY", "↔", "NET"),
    ("Digital Govt", "GOVT", "↔", "USER"),
    ("Civic Tech", "ALL", "↔", "GOVT"),
    ("Govt Data", "OPEN", "↔", "WISE"),
    ("Institution Build", "ALL", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g172-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g172-{index}-title g172-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g172-{index}-title">{safe}</title><desc id="g172-{index}-desc">A "What Young Pakistanis Can Build" relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g172-{index}-caption" class="diagram-caption">{index}. {safe} — "What Young Pakistanis Can Build" relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">What Young Pakistanis Can Build Framework</title><desc id="hero-desc">A diagram showing the diverse sectors young Pakistani builders can impact, from AI infrastructure and EdTech to smart manufacturing and sovereign institutions.</desc><defs><linearGradient id="h172-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h172-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE GENERATION OF BUILDERS LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AI INFRASTRUCTURE: $1B PAKISTAN COMMITMENT</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">EDTECH & HEALTH-TECH: 70% YOUTH GAI ENGAGEMENT</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">SMART MANUFACTURING & ROBOTICS (INDUSTRY 4.0)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">FINTECH & BLOCKCHAIN: SOVEREIGN DIGITAL ASSETS</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">AGRITECH & CLIMATE TECH: WATER & GRID MGMT</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI ECOSYSTEM: HUB, BOND, GRID & ARCHIVE</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">INSTITUTIONAL BUILDING: ALLOWING OTHERS TO BUILD</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">WHAT YOUNG PAKISTANIS CAN BUILD</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Potential to Products, Companies and Institutions.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Generation of Builders Loop: Navigating the 2026 landscape where young Pakistani innovators transform potential into global-scale products and sovereign institutions across diverse technology sectors.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 172</title>
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
            <p class="section-label">PAGE 172</p>
            <h2>WHAT YOUNG PAKISTANIS CAN BUILD</h2>
            <p>“From Potential to Products, Companies and Institutions.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Pakistan's young population represents one of the country's most important sources of future human capital. But potential by itself does not create development. Potential becomes meaningful when people have the education, infrastructure, capital, and freedom to turn ideas into useful products and services. Young Pakistanis can build much more than startups; they can build software, scientific research, financial infrastructure, AI systems, digital platforms, and global technology companies. They can also build institutions that allow other people to build. The question is: What can an entire generation build when knowledge, technology and opportunity become more accessible?”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The AI Revolution & Infrastructure (2026)</h3>
                <p>By 2026, Pakistan has committed **$1 billion** to its national AI ecosystem, aiming to modernize the digital economy through "AI Factories" and specialized academies [1]. This investment equips young builders with the resources to develop AI platforms designed around Pakistani languages, markets, and institutional needs. In urban centers, nearly **70% of youth** are already engaging with generative AI for health and educational purposes, reflecting a rapid adoption of advanced automation tools [2] [3].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Sector Innovation: EdTech, HealthTech & AgriTech</h3>
                <p>Young Pakistani innovators are rewriting the country's economic story across multiple sectors. EdTech platforms are expanding access to tutoring and assessments, while HealthTech initiatives explore remote consultation and medical logistics with a focus on privacy and safety [4] [5]. In AgriTech, satellite imagery and AI-powered crop monitoring are helping farmers optimize water management and disaster preparedness, ensuring that technology addresses Pakistan's most critical climate challenges [6] [7].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Smart Manufacturing & Industry 4.0</h3>
                <p>The future of Pakistani manufacturing is being shaped by **Industry 4.0** adoption. Young engineers are developing tools for industrial monitoring, quality control, and inventory management using robotics and advanced sensors [8]. While building a full semiconductor industry requires long-term strategy, Pakistani talent is already making its mark in Silicon Valley and global ecosystems through chip design, verification, and embedded systems research [9] [10].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Sovereign Institutions & Digital Heritage</h3>
                <p>Building something that lasts means creating institutions that allow others to build. Orakzai researchers are contributing to this legacy through responsible digital preservation of oral histories, manuscripts, and family records [11]. By combining fintech, blockchain, and digital identity systems, initiatives like **OKBOND** and the **Sovereign Grid** are exploring new approaches to digital ownership and infrastructure, securing a sovereign future for the community [12] [13].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: What Young Pakistanis Can Build</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai youth, building is a form of tribal resilience. We do not just build for the present; we build for the next generation. By mastering the tools of AI, robotics, and blockchain, we are turning our potential into a sovereign legacy of products, companies, and institutions. We are the architects of a future where Pakistani talent is respected worldwide and our heritage is the foundation of our global strength.”</p>
            </div>

            <div class="final-statement">
                BUILD IMPACT.<br>
                REDEFINE THE ECONOMY.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Instagram / Tech News, <em>Pakistan Commits $1 Billion to National AI Ecosystem by 2030 (2026)</em>.</li>
                    <li>PLOS Digital Health, <em>Use of Generative AI for Health Among Urban Youth in Pakistan (2026)</em>.</li>
                    <li>Shad Foundation, <em>How Pakistani Youth Can Thrive in 2026's Digital Economy (February 2026)</em>.</li>
                    <li>Pak Global Alumni, <em>Pakistan's Startup Surge: How Youth Innovation Is Redefining the Economy (2025)</em>.</li>
                    <li>UNESCO, <em>Empowering Pakistan's Educators for an AI-Driven Future (January 2026)</em>.</li>
                    <li>Instagram / Youth Innovation Challenge, <em>Brightest Startup Talent and Sector Impact (2026)</em>.</li>
                    <li>University of Faisalabad, <em>Innovative Pakistan 2026: Strengthening the Tech Ecosystem (June 2026)</em>.</li>
                    <li>JR Automation, <em>2026 Key Trends in Automation Shaping the Future of Manufacturing (March 2026)</em>.</li>
                    <li>LinkedIn / Industry Insights, <em>5 Trends Shaping the Future of Industrial Automation in Pakistan (February 2026)</em>.</li>
                    <li>Facebook / 9NewsHD, <em>Pakistanis Making Their Mark in Silicon Valley: June 2026 Report</em>.</li>
                    <li>TW Automation, <em>Robotics in 2026: Key Trends for Manufacturers (January 2026)</em>.</li>
                    <li>RSM US, <em>Top 2026 Manufacturing Trends: Smarter Products and AI (January 2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Institutional Building and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            172
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-113-pakistans-digital-economy.html'

GRAPHICS = [
    ("What is a Digital Economy?", "TECH", "ACTIVITY", "VALUE"),
    ("Digital Economy Structure", "INFRA", "PLATFORMS", "USERS"),
    ("Internet to Economy Path", "ACCESS", "USAGE", "VALUE"),
    ("Pakistan Transformation", "TELECOM", "MOBILE", "DIGITAL"),
    ("Connectivity as Infra", "FIBER", "4G", "DATA"),
    ("Digital Divide: Access", "CONNECTED", "↔", "GAP"),
    ("Digital Divide: Factors", "INCOME", "GEO", "SKILLS"),
    ("IT & ITeS Services", "SOFTWARE", "BPO", "CLOUD"),
    ("IT Exports Milestone", "$3.4B", "GROWTH", "FY26"),
    ("Export Share: Services", "46.1%", "IT SHARE", "FY26"),
    ("Why IT Exports Matter", "FOREX", "JOBS", "MARKETS"),
    ("Skills to Exports Flow", "SKILLS", "SERVICES", "FOREX"),
    ("Freelancing Ecosystem", "GLOBAL", "PLATFORM", "SKILLS"),
    ("Freelance Categories", "CODE", "DESIGN", "WRITE"),
    ("Freelancer Facilitation", "REG", "CENTERS", "GOVT"),
    ("e-Rozgaar Model", "SPACE", "SKILLS", "JOBS"),
    ("Startup Lifecycle", "IDEA", "TEAM", "SCALE"),
    ("Startup Ecosystem Nodes", "VC", "UNIV", "GOVT"),
    ("Pakistan Startup Fund", "CAPITAL", "SUPPORT", "SCALE"),
    ("E-commerce Pillars", "SHOP", "PAY", "SHIP"),
    ("Social Commerce Flow", "SOCIAL", "CHAT", "SALE"),
    ("Digital Payment Types", "WALLET", "QR", "RAAST"),
    ("Raast Payment Flow", "P2P", "P2M", "INSTANT"),
    ("Cashless Economy Risks", "FRAUD", "PRIVACY", "SEC"),
    ("Fintech Definition", "FINANCE", "+", "TECH"),
    ("Digital Banking Stack", "APP", "ID", "CORE"),
    ("E-commerce Logistics", "BUY", "SHIP", "DELIVER"),
    ("Small Business Tools", "WEB", "SOCIAL", "PAY"),
    ("Digital Agriculture", "MARKET", "DATA", "PAY"),
    ("Digital Health Flow", "DOC", "DATA", "PATIENT"),
    ("Digital Education Stack", "LMS", "SKILL", "CERT"),
    ("Digital Government", "ID", "PORTAL", "DATA"),
    ("Digital Public Infra", "ID", "PAY", "DATA"),
    ("Data Economy Cycle", "COLLECT", "STORE", "VALUE"),
    ("Data Governance", "PRIVACY", "SEC", "RULES"),
    ("AI Economy Potential", "AUTO", "AUG", "SKILLS"),
    ("AI Policy Framework", "GOV", "SKILLS", "RESEARCH"),
    ("AI and Employment", "JOBS", "CHANGE", "SKILLS"),
    ("Digital Skills Gap", "CODE", "AI", "DATA"),
    ("Youth Opportunity Path", "LEARN", "BUILD", "EARN"),
    ("Women's Participation", "ACCESS", "SKILLS", "OPP"),
    ("Remote Work Pathway", "HOME", "WEB", "GLOBAL"),
    ("Global Digital Position", "MARKET", "TALENT", "COST"),
    ("Diaspora Economy Bridge", "INVEST", "MENTOR", "LINK"),
    ("Orakzai Digital Path", "SKILL", "CONNECT", "MARKET"),
    ("Orakzai Entrepreneur", "LOCAL", "DIGITAL", "GLOBAL"),
    ("Digital Migration Flow", "VILLAGE", "CITY", "WEB"),
    ("Rural Digital Barriers", "POWER", "SIGNAL", "SKILLS"),
    ("Digital Culture Space", "PASHTO", "MEDIA", "ARTS"),
    ("Language Tech Economy", "TRANS", "OCR", "SPEECH"),
    ("Digital Trust Model", "SEC", "PRIV", "RELIABLE"),
    ("Cybersecurity Economy", "PROTECT", "TRUST", "VALUE"),
    ("Consumer Protection", "RIGHTS", "SAFETY", "TRUST"),
    ("Regulation Ecosystem", "PTA", "SBP", "SECP"),
    ("Digital Taxation", "POLICY", "ADMIN", "COMPLY"),
    ("Formalization Flow", "DIGITAL", "RECORD", "FORMAL"),
    ("Digital Employment", "DIRECT", "TRANS", "NEW"),
    ("Productivity Pathway", "TOOLS", "DATA", "GAIN"),
    ("Pakistan Future Vision", "IT", "AI", "EXPORT"),
    ("Success Measurement", "INCL", "PROD", "EXPORT"),
    ("Key Data: Exports", "$3.4B", "FY26", "SBP"),
    ("Key Data: Growth", "19.8%", "FY26", "SBP"),
    ("Key Data: Broadband", "147M", "2025", "PTA"),
    ("Key Data: Coverage", "91%", "2024", "PTA"),
    ("Research Gap: District", "LOCAL", "DATA", "NEED"),
    ("Oral History Digital", "VOICE", "MEMORY", "SAVE"),
    ("Skills to Opportunity", "LEARN", "CONNECT", "OPP"),
    ("Infrastructure Stack", "POWER", "FIBER", "CLOUD"),
    ("Connectivity to Exports", "INFRA", "SERVICES", "$"),
    ("Mobile Payment Flow", "WALLET", "RAAST", "PAY"),
    ("E-commerce Transaction", "ORDER", "PAY", "SHIP"),
    ("Startup Capital Flow", "ANGEL", "VC", "SCALE"),
    ("Cloud Economy Node", "STORAGE", "COMPUTE", "APP"),
    ("AI Value Chain", "DATA", "MODEL", "APP"),
    ("Digital Gov Service", "ID", "LOGIN", "APPLY"),
    ("Digital Skills Path", "BASIC", "ADV", "PRO"),
    ("Freelancer Remittance", "WORK", "BANK", "PKR"),
    ("Software Export Pipe", "CODE", "CLIENT", "EXPORT"),
    ("Cyber Trust Stack", "SECURE", "PRIV", "AUTH"),
    ("Digital Divide Concept", "IN", "↔", "OUT"),
    ("Rural-to-Global Path", "VILLAGE", "WEB", "WORLD"),
    ("Pashto Digital Market", "CONTENT", "USER", "VALUE"),
    ("Cultural Commerce Flow", "CRAFT", "WEB", "BUYER"),
    ("Data Privacy Flow", "CONSENT", "SEC", "USER"),
    ("Regulation Cycle", "RULES", "GROWTH", "TRUST"),
    ("Inclusive Success", "ALL", "ACCESS", "VALUE"),
    ("Digital Future Map", "NOW", "→", "2030"),
    ("Responsible Tech", "ETHICS", "INCL", "SAFE"),
    ("Orakzai Youth Path", "SCHOOL", "SKILL", "WORK"),
    ("Global Client Network", "US", "EU", "GULF"),
    ("Tech Transfer Flow", "UNIV", "LAB", "BIZ"),
    ("Digital Trust Bridge", "USER", "TRUST", "SERVICE"),
    ("Innovation Cycle", "IDEA", "BUILD", "GROW"),
    ("Sovereignty Model", "DATA", "INFRA", "SKILLS"),
    ("Future Tech Node", "AI", "EDGE", "QUANT"),
    ("Pakistan Export Hub", "KHI", "LHR", "ISB"),
    ("Remote Work Economy", "SKILLS", "TIME", "PAY"),
    ("Digital Economy Goal", "VALUE", "JOBS", "EXPORT"),
    ("Final Statement Logic", "PEOPLE", "CONNECT", "BUILD"),
    ("End of Page 113", "113", "DONE", "GIT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g113-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g113-{index}-title g113-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g113-{index}-title">{safe}</title><desc id="g113-{index}-desc">A digital economy relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g113-{index}-caption" class="diagram-caption">{index}. {safe} — economic concept.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Pakistan’s Digital Economy</title><desc id="hero-desc">A conceptual digital landscape of Pakistan showing connectivity, software exports, fintech, e-commerce, and global connections.</desc><defs><linearGradient id="h113-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h113-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(100, 100)" opacity=".6"><rect x="0" y="0" width="150" height="100" rx="8" fill="#153B2A" stroke="#2E8B57"/><text x="75" y="55" text-anchor="middle" fill="#F5F0E6" font-size="12">IT EXPORTS</text><text x="75" y="75" text-anchor="middle" fill="#B59654" font-size="10">$3.4 BILLION</text></g><g transform="translate(300, 150)" opacity=".7"><rect x="0" y="0" width="150" height="100" rx="8" fill="#3C3020" stroke="#B59654"/><text x="75" y="55" text-anchor="middle" fill="#F5F0E6" font-size="12">FINTECH</text><text x="75" y="75" text-anchor="middle" fill="#B59654" font-size="10">RAAST • WALLETS</text></g><g transform="translate(500, 200)" opacity=".6"><rect x="0" y="0" width="150" height="100" rx="8" fill="#202B35" stroke="#7894A8"/><text x="75" y="55" text-anchor="middle" fill="#F5F0E6" font-size="12">E-COMMERCE</text><text x="75" y="75" text-anchor="middle" fill="#B59654" font-size="10">GLOBAL MARKET</text></g><path d="M250 150 L 300 150 M 450 200 L 500 200" stroke="#B59654" stroke-width="2" stroke-dasharray="5 5"/><text x="380" y="50" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">PAKISTAN’S DIGITAL ECONOMY</text><text x="380" y="80" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="12" font-style="italic">“From connectivity to opportunity.”</text><g transform="translate(380, 380)" opacity=".8"><text x="0" y="0" text-anchor="middle" fill="#B59654" font-size="10">INFRASTRUCTURE • SKILLS • TRUST • INNOVATION</text></g></svg><figcaption id="hero-caption" class="diagram-caption">Pakistan’s Digital Economy: A multi-layered landscape of services, exports, and digital infrastructure.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 113</title>
    <link rel="stylesheet" href="../styles/main.css">
    <style>
        :root {{ --gold: #B59654; --green: #2E8B57; --blue: #7894A8; --cream: #F5F0E6; --muted: rgba(245,240,230,.72); }}
        body {{ background: #070807; color: var(--cream); font-family: Georgia, serif; line-height: 1.72; }}
        .content-page {{ max-width: 1100px; margin: 0 auto; padding: 40px 6vw; }}
        .page-header {{ text-align: center; border-bottom: 1px solid var(--gold); padding-bottom: 20px; margin-bottom: 40px; }}
        .page-header h2 {{ color: var(--gold); font-size: 2.2rem; letter-spacing: 0.1rem; }}
        .section-label {{ color: var(--gold); font-weight: 700; letter-spacing: 0.15rem; text-transform: uppercase; font-size: 0.85rem; margin-top: 40px; }}
        .hero-diagram {{ margin: 40px auto; }}
        .atlas-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 30px; }}
        .opening-text {{ font-size: 1.15rem; font-style: italic; border-left: 3px solid var(--gold); padding-left: 20px; margin: 40px 0; }}
        .prose-section {{ margin-bottom: 40px; }}
        .data-table {{ width: 100%; border-collapse: collapse; margin: 30px 0; font-size: 0.85rem; }}
        .data-table th, .data-table td {{ border: 1px solid rgba(181,150,84,0.3); padding: 12px; text-align: left; }}
        .data-table th {{ background: rgba(181,150,84,0.1); color: var(--gold); }}
        .reflection-box {{ border: 1px solid var(--gold); padding: 30px; margin: 50px 0; background: rgba(181,150,84,0.05); }}
        .final-statement {{ text-align: center; font-size: 1.8rem; font-weight: 700; color: var(--gold); margin: 60px 0; }}
        @media (max-width: 768px) {{ .atlas-grid {{ grid-template-columns: 1fr; }} }}
        svg {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="content-page">
        <header class="page-header">
            <p class="section-label">PAGE 113</p>
            <h2>PAKISTAN’S DIGITAL ECONOMY</h2>
            <p>“From connectivity to opportunity.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “An economy no longer exists only in factories, farms, shops and offices. It also exists in servers. In software. In digital payments. In online marketplaces. In remote work. In cloud platforms. In data. In the skills of people who can work for a customer thousands of kilometres away.<br><br>
                Pakistan entered this transformation gradually. The country's digital economy grew from telecommunications and internet access into software services, freelancing, e-commerce, fintech, startups and increasingly artificial intelligence. But digital opportunity is not distributed equally. A fast connection means little without a device. A talented freelancer needs skills, payments and access to global markets. A startup needs capital, customers and reliable infrastructure. A digital economy therefore depends on more than technology. It depends on people, institutions, infrastructure and trust.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">What is a Digital Economy?</h3>
                <p>A digital economy is economic activity enabled or transformed by digital technologies. It is not limited to the IT industry; instead, it encompasses how agriculture, banking, education, healthcare, and government become digitally enabled. In Pakistan, this transition is driven by connectivity, software services, and digital public infrastructure.</p>
                <p><strong>DIGITAL ECONOMY = INFRASTRUCTURE + SKILLS + TRUST + INNOVATION</strong></p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Key Economic Indicators (2025–2026)</h3>
                <table class="data-table">
                    <thead>
                        <tr><th>Indicator</th><th>Value</th><th>Period</th><th>Source</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>IT Services Exports</td><td>US$3.4 Billion</td><td>FY 2025-26</td><td>Economic Survey</td></tr>
                        <tr><td>IT Export Growth</td><td>19.8%</td><td>FY 2025-26</td><td>Economic Survey</td></tr>
                        <tr><td>Share of Services Exports</td><td>46.1%</td><td>FY 2025-26</td><td>Economic Survey</td></tr>
                        <tr><td>Broadband Subscribers</td><td>147.2 Million</td><td>March 2025</td><td>PTA</td></tr>
                        <tr><td>Broadband Penetration</td><td>59.8%</td><td>March 2025</td><td>PTA</td></tr>
                        <tr><td>Cellular Coverage</td><td>91%</td><td>Dec 2024</td><td>PTA</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">IT Services and Freelancing</h3>
                <p>Pakistan has emerged as a major global player in IT and IT-enabled services (ITeS). Software development, consultancy, and BPO services are significant drivers of foreign exchange. The freelance economy, supported by government initiatives like <strong>e-Rozgaar</strong>, allows individuals to sell their skills globally in fields like design, marketing, and AI services.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Fintech and Digital Payments</h3>
                <p>The State Bank of Pakistan’s <strong>Raast</strong> instant payment system and mobile wallets have transformed financial inclusion. By reducing transaction friction and enabling secure, instant transfers, fintech is providing the foundation for a cashless economy, though constraints in trust and digital literacy remain.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Pakistan’s Digital Economy</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Orakzai and the Digital Economy</h3>
                <p>For Orakzai communities, the digital economy offers pathways to global markets that geography alone cannot determine. Remote work and digital education enable youth to participate in national and international economic activity. However, rural barriers such as electricity reliability and network quality remain critical constraints that must be addressed for inclusive growth.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“An economy is ultimately about people. Technology may provide the tools, but people create the value. A mountain village can still produce a digital worker. A diaspora family can become a bridge to another market. The digital economy is not simply Pakistan becoming more technological; it is Pakistan learning how technology can expand what its people are able to build.”</p>
            </div>

            <div class="final-statement">
                THE DIGITAL ECONOMY IS NOT ABOUT MACHINES.<br>
                IT IS ABOUT WHAT PEOPLE CAN BUILD WHEN THEY ARE CONNECTED.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Ministry of Finance, <em>Pakistan Economic Survey 2025-26</em>.</li>
                    <li>Pakistan Telecommunication Authority (PTA), <em>Annual Report 2025</em>.</li>
                    <li>State Bank of Pakistan (SBP), <em>Payment Systems Review FY 2025-26</em>.</li>
                    <li>World Bank, <em>Pakistan Digital Economy Report 2024</em>.</li>
                    <li>Pakistan Software Export Board (PSEB), <em>IT Industry Milestones 2025</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            113
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

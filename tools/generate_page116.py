from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-116-local-to-global.html'

GRAPHICS = [
    ("Global Market Hero", "LOCAL", "NETWORK", "GLOBAL"),
    ("What is a Market?", "PEOPLE", "PRODUCT", "DEAL"),
    ("Local Market Pillars", "TRUST", "REPUTATION", "REPEAT"),
    ("Orakzai Markets", "AGRI", "TRADE", "LOCAL"),
    ("Village to District", "VILLAGE", "→", "DISTRICT"),
    ("District to City", "DISTRICT", "→", "CITY"),
    ("Diaspora Market", "HOMELAND", "+", "DIASPORA"),
    ("Local to Global Path", "LOCAL", "→", "WORLD"),
    ("Quality Before Scale", "QUALITY", "→", "CONSISTENCY"),
    ("Product Journey", "MAKE", "SHIP", "USER"),
    ("Logistics Chain", "ROAD", "PORT", "AIR"),
    ("Pakistan Single Window", "DIGITAL", "TRADE", "FAST"),
    ("Customs Boundaries", "LAW", "TAX", "BORDER"),
    ("E-commerce Bridge", "WEB", "PAY", "SHIP"),
    ("Digital Products", "CODE", "CLOUD", "USER"),
    ("IT Exports FY26", "$4.6B", "RECORD", "PSEB"),
    ("Freelancer to Company", "SKILL", "TEAM", "BIZ"),
    ("Global Value Chain", "PART", "VALUE", "WHOLE"),
    ("Export Diversification", "AGRI", "IT", "MFG"),
    ("Beyond Textiles", "VALUE", "TECH", "DESIGN"),
    ("Brand Pillars", "STORY", "QUALITY", "TRUST"),
    ("Orakzai Identity Brand", "ROOTS", "+", "STORY"),
    ("Cultural Products", "CRAFT", "HERITAGE", "MARKET"),
    ("Global Customer", "LANG", "CURR", "LAW"),
    ("Language Bridge", "PASHTO", "URDU", "ENG"),
    ("International Payments", "BANK", "GATEWAY", "SEC"),
    ("Foreign Exchange", "PKR", "↔", "USD"),
    ("Global Trust Stack", "ID", "REV", "SHIP"),
    ("Standards & Certs", "ISO", "SPS", "TBT"),
    ("Intellectual Property", "TM", "COPY", "PAT"),
    ("Global Competition", "LOCAL", "↔", "WORLD"),
    ("Price vs Quality", "COST", "VALUE", "WIN"),
    ("Role of Technology", "DATA", "WEB", "AI"),
    ("AI in Global BIZ", "TRANS", "RES", "AUTO"),
    ("Faisal Case Study", "TECH", "→", "GLOBAL"),
    ("Faisal Global Mindset", "ROOTS", "→", "BEYOND"),
    ("Diaspora Network", "LINK", "KNOW", "$"),
    ("Local Stories Global", "STORY", "+", "QUALITY"),
    ("Orakzai to Pakistan", "LOCAL", "→", "NATIONAL"),
    ("Pakistan to World", "MADE", "DESIGNED", "SERVED"),
    ("Export Entrepreneur", "CLIENT", "OUTSIDE", "PAK"),
    ("Global Market Entry", "RES", "TEST", "SCALE"),
    ("Market Research", "WHO", "WHAT", "HOW"),
    ("Pilot Before Scale", "TEST", "LEARN", "GROW"),
    ("Global Failure Risks", "LAW", "SHIP", "CULT"),
    ("Cost of Going Global", "REG", "MKT", "TECH"),
    ("Small BIZ Global", "NICHE", "SKILL", "WEB"),
    ("Orakzai Youth Global", "SKILL", "WEB", "OPP"),
    ("Globalization Impact", "WORK", "CULT", "ID"),
    ("Local Identity Global", "SAVE", "MEM", "TRADE"),
    ("Cultural Commodity", "MEAN", "≠", "$"),
    ("Community Development", "BIZ", "JOBS", "DEV"),
    ("Pakistan Export Future", "AI", "SaaS", "MFG"),
    ("Pakistan Needs Pillars", "POLICY", "INFRA", "SKILL"),
    ("Young Orakzai Build", "CODE", "AGRI", "TOUR"),
    ("Research Gap: Trade", "HIST", "DATA", "NEED"),
    ("Oral History: Trade", "ELDER", "NOW", "FUTURE"),
    ("Local Customer Node", "TRUST", "PROX", "KNOW"),
    ("Regional Customer Node", "TOWN", "LINK", "BUY"),
    ("National Customer Node", "CITY", "WEB", "REACH"),
    ("International Customer", "ZONE", "LAW", "NEED"),
    ("Global Customer Node", "ALL", "WEB", "WORLD"),
    ("Market Expansion Ladder", "1", "10", "1000"),
    ("Customer Acquisition", "FIND", "WIN", "KEEP"),
    ("Product Localization", "FIT", "USE", "CULT"),
    ("Language Localization", "TRANS", "ADAPT", "USE"),
    ("Digital Marketing Node", "AD", "SEO", "DATA"),
    ("International Branding", "LOGO", "STORY", "NAME"),
    ("Global Support Node", "HELP", "FAST", "TRUST"),
    ("Cross-border Payments", "SEND", "SEC", "GET"),
    ("International Shipping", "PACK", "SEND", "DEL"),
    ("Warehouse Node", "STORE", "INV", "SHIP"),
    ("Supply Chain Node", "RAW", "MAKE", "SELL"),
    ("Export Documentation", "FORM", "PSW", "FILE"),
    ("Trade Facilitation Node", "FAST", "EASY", "LAW"),
    ("Market Intelligence", "DATA", "RES", "PLAN"),
    ("Competitive Analysis", "US", "THEM", "GAP"),
    ("Product Quality Node", "TEST", "FIX", "GOOD"),
    ("Quality Control Node", "CHECK", "FIX", "PASS"),
    ("Customer Feedback Node", "ASK", "LIST", "FIX"),
    ("Scaling Logic", "CAP", "SYS", "GROW"),
    ("Business Systems Node", "PLAN", "DO", "CHECK"),
    ("International Team", "DIVERSE", "SKILL", "WORK"),
    ("Remote Work Node", "HOME", "WEB", "TEAM"),
    ("Global Talent Node", "SKILL", "HIRE", "WIN"),
    ("Diaspora Commerce Node", "NET", "TRADE", "LINK"),
    ("Cultural Enterprise Node", "CRAFT", "MEAN", "BIZ"),
    ("Heritage Economy Node", "PAST", "VALUE", "NOW"),
    ("Digital Heritage Node", "SAVE", "DATA", "SHARE"),
    ("Orakzai Tech Pathway", "LEARN", "BUILD", "GLOBAL"),
    ("Skill to Global Income", "SKILL", "WEB", "$"),
    ("Local Idea Global", "IDEA", "BUILD", "WORLD"),
    ("Pakistan Global Net", "ISB", "KHI", "LHR"),
    ("Global Entrepreneurship", "MIND", "DO", "WORLD"),
    ("Export Ecosystem Node", "GOVT", "BANK", "BIZ"),
    ("Market Risk Node", "CASH", "LAW", "CULT"),
    ("Global Opportunity Node", "OPEN", "NEW", "VALUE"),
    ("Evidence Matrix Logic", "DATA", "CONF", "SAVE"),
    ("Research Gap Analysis", "MISS", "NEED", "FIND"),
    ("Final Statement Logic", "LOCAL", "BUILD", "GLOBAL"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g116-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g116-{index}-title g116-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g116-{index}-title">{safe}</title><desc id="g116-{index}-desc">A market relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g116-{index}-caption" class="diagram-caption">{index}. {safe} — market concept.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">From Local Markets to Global Markets</title><desc id="hero-desc">A conceptual map showing the journey from an Orakzai mountain market through regional cities to a global digital network.</desc><defs><linearGradient id="h116-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h116-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(60, 250)" opacity=".8"><rect x="0" y="0" width="80" height="50" rx="4" fill="#3C3020" stroke="#B59654"/><text x="40" y="30" text-anchor="middle" fill="#F5F0E6" font-size="10">ORAKZAI</text></g><path d="M140 275 L 200 275" stroke="#B59654" stroke-width="2" stroke-dasharray="4 4"/><g transform="translate(200, 250)" opacity=".8"><rect x="0" y="0" width="80" height="50" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="40" y="30" text-anchor="middle" fill="#F5F0E6" font-size="10">PESHAWAR</text></g><path d="M280 275 L 340 275" stroke="#B59654" stroke-width="2" stroke-dasharray="4 4"/><g transform="translate(340, 250)" opacity=".9"><rect x="0" y="0" width="80" height="50" rx="4" fill="#202B35" stroke="#7894A8"/><text x="40" y="30" text-anchor="middle" fill="#F5F0E6" font-size="10">KARACHI</text></g><path d="M420 275 L 480 275" stroke="#B59654" stroke-width="2" stroke-dasharray="4 4"/><g transform="translate(480, 250)" opacity=".9"><rect x="0" y="0" width="80" height="50" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="40" y="30" text-anchor="middle" fill="#F5F0E6" font-size="10">DUBAI/LDN</text></g><path d="M560 275 L 620 275" stroke="#B59654" stroke-width="2" stroke-dasharray="4 4"/><g transform="translate(620, 250)"><circle cx="40" cy="25" r="30" fill="none" stroke="#B59654" stroke-width="2"/><text x="40" y="30" text-anchor="middle" fill="#F5F0E6" font-size="10">GLOBAL</text></g><text x="380" y="50" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">LOCAL TO GLOBAL MARKETS</text><text x="380" y="80" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="12" font-style="italic">“A local idea can travel farther than its birthplace.”</text><g transform="translate(380, 390)" opacity=".8"><text x="0" y="0" text-anchor="middle" fill="#B59654" font-size="10">QUALITY • TRUST • LOGISTICS • TECHNOLOGY • REPUTATION</text></g></svg><figcaption id="hero-caption" class="diagram-caption">From Local to Global: The strategic journey of products and ideas across physical and digital boundaries.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 116</title>
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
        .case-study-card {{ border: 1px solid var(--gold); padding: 30px; margin: 50px 0; background: rgba(181,150,84,0.05); }}
        .final-statement {{ text-align: center; font-size: 1.8rem; font-weight: 700; color: var(--gold); margin: 60px 0; }}
        @media (max-width: 768px) {{ .atlas-grid {{ grid-template-columns: 1fr; }} }}
        svg {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="content-page">
        <header class="page-header">
            <p class="section-label">PAGE 116</p>
            <h2>FROM LOCAL MARKETS TO GLOBAL MARKETS</h2>
            <p>“A local idea can travel farther than its birthplace.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “A market begins with a relationship. A shopkeeper knows the people who walk through the door. A farmer knows the buyers who come for the harvest. A craftsman knows the community that values the work. A small business may begin with ten customers. Then twenty. Then a hundred. Eventually, the question changes: Can this product travel beyond the place where it began? For some businesses, the answer is another town. For others, another province. For others, another country. And for a small number, a local idea becomes a global business. The journey from local markets to global markets is not simply a journey across geography. It is a journey of quality, trust, logistics, technology, finance, language, regulation and reputation.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Current Trade Context (2025–2026)</h3>
                <p>Pakistan's trade policy for 2025–2030 emphasizes an export-led growth strategy. The <strong>National Tariff Policy (2025–30)</strong> aims to improve competitiveness by rationalizing tariffs and reducing anti-export bias. Digital trade facilitation, led by the <strong>Pakistan Single Window (PSW)</strong>, is reducing fragmentation in trade processes, enabling SMEs to participate more effectively in global value chains.</p>
                <p>A major milestone was reached in FY 2025–26, with IT and IT-enabled services (ITeS) exports reaching a record <strong>US$4.6 billion</strong>, highlighting the growing role of digital exports in the national economy.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Diaspora as a Global Bridge</h3>
                <p>Diaspora communities are critical connectors in the journey from local to global. Beyond being customers, they serve as business partners, investors, and mentors. By bridging the gap between the homeland and international markets, diaspora networks facilitate knowledge transfer and capital flow, allowing local products and services to find resonance in diverse cultural and economic landscapes.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Building Beyond Borders</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur</strong></p>
                    <p>Faisal Orakzai illustrates one individual's pathway from local roots to global technology markets. His work, focused on computer science and digital systems, is oriented toward international audiences. By leveraging digital infrastructure, his projects (e.g., <strong>Orakzai Group</strong>, <strong>OkzByte Hub</strong>) show how a "Global Mindset"—combined with technical curiosity and cultural identity—can address problems that cross physical boundaries.</p>
                    <p><em>“This case study illustrates one individual's pathway... It is not evidence that all Orakzai entrepreneurs follow the same path.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: From Local to Global</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Orakzai Identity in a Global Economy</h3>
                <p>Participating in global markets does not require the loss of local identity. A person can carry their language, family history, and community relationships while building for the world. For Orakzai youth, the goal is not only to reach the global market but to build something from their own context that can travel—turning mountain-based memory into global-facing value.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Research Gap: What Still Needs to be Documented</h3>
                <ul>
                    <li>Historical Orakzai trade routes and merchant family records.</li>
                    <li>Specific outcomes of Orakzai-led businesses in the diaspora.</li>
                    <li>The role of traditional trading networks in modern cross-border commerce.</li>
                    <li>Data on women-led and youth-led businesses in remote district markets.</li>
                </ul>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“I grew up understanding that identity begins somewhere specific. For me, that place is Orakzai. But technology taught me that work does not have to remain limited by geography. A piece of software built in Pakistan can be used on another continent. Local markets remain the foundation—they teach us trust and responsibility—but the world can become a market. The challenge is to build with quality, consistency, and respect for other cultures, remembering where we came from without allowing it to determine where our ideas can go.”</p>
            </div>

            <div class="final-statement">
                THE WORLD CAN BECOME A MARKET.<br>
                BUT EVERY GLOBAL JOURNEY BEGINS SOMEWHERE LOCAL.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Ministry of Commerce, <em>National Tariff Policy 2025–30</em>.</li>
                    <li>Pakistan Single Window (PSW), <em>Trade Facilitation Updates 2026</em>.</li>
                    <li>PSEB / Ministry of IT, <em>IT & ITeS Export Performance FY 2025–26</em>.</li>
                    <li>Ministry of Commerce, <em>Second National E-Commerce Policy (Draft 2026)</em>.</li>
                    <li>State Bank of Pakistan (SBP), <em>Export Facilitation Directives 2026</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            116
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-115-entrepreneurship-pakistan.html'

GRAPHICS = [
    ("Entrepreneurship Hero", "IDEA", "VALUE", "GROWTH"),
    ("What is Entrepreneurship?", "PROBLEM", "→", "SOLUTION"),
    ("Entrepreneurship Types", "SME", "STARTUP", "FAMILY"),
    ("Small Business Economy", "SHOP", "CRAFT", "JOBS"),
    ("SME Definitions (SBP)", "MICRO", "SMALL", "MEDIUM"),
    ("Family Business Pillars", "TRUST", "CAPITAL", "LEGACY"),
    ("Family-to-Modern Path", "TRADITION", "+", "TECH"),
    ("Entrepreneurial Mindset", "LEARN", "DO", "ADAPT"),
    ("Idea vs Opportunity", "IDEA", "≠", "OPPORTUNITY"),
    ("Customer Feedback Loop", "LISTEN", "BUILD", "FIX"),
    ("Startup Culture", "SCALE", "RISK", "GROW"),
    ("Startup Ecosystem", "VC", "HUB", "UNIV"),
    ("National Incubation Centers", "MENTOR", "SPACE", "LINK"),
    ("Pakistan Startup Fund", "$50K", "→", "$1M"),
    ("Access to Capital Ladder", "OWN", "BANK", "VC"),
    ("SME Financing Limits", "30M", "400M", "2B"),
    ("Informal Entrepreneurship", "BARRIER", "↔", "ACCESS"),
    ("Women Entrepreneurs", "SKILL", "WEB", "OPP"),
    ("Youth Entrepreneurs", "TECH", "IDEA", "BIZ"),
    ("Faisal Orakzai Case Study", "TECH", "→", "FOUNDER"),
    ("Faisal: Builder Model", "BUILD", "TEST", "SCALE"),
    ("Orakzai Identity & BIZ", "IDENTITY", "+", "MARKET"),
    ("Entrepreneurship Outside Cities", "REMOTE", "LOCAL", "WEB"),
    ("Orakzai Entrepreneurship", "TRADE", "TRANS", "TECH"),
    ("Diaspora Entrepreneurship", "GLOBAL", "→", "LOCAL"),
    ("Digital Entrepreneurship", "LAPTOP", "WEB", "BIZ"),
    ("E-commerce Flow", "SHOP", "PAY", "SHIP"),
    ("Freelancing to BIZ", "SKILL", "TEAM", "AGENCY"),
    ("Technology Entrepreneurship", "AI", "CLOUD", "CODE"),
    ("Innovation Logic", "PROBLEM", "+", "NEW"),
    ("Export Entrepreneur", "LOCAL", "→", "GLOBAL"),
    ("Local Entrepreneur", "NEIGHBOR", "→", "VALUE"),
    ("Rural Entrepreneurship", "AGRI", "CRAFT", "WEB"),
    ("Cultural Enterprise", "HERITAGE", "→", "MARKET"),
    ("Tourism Entrepreneurship", "STAY", "TOUR", "FOOD"),
    ("The Role of Trust", "TRUST", "→", "SALE"),
    ("Digital Trust Stack", "SECURE", "PRIV", "AUTH"),
    ("Formalization Pathway", "REG", "BANK", "GROW"),
    ("Regulation Ecosystem", "SECP", "FBR", "SBP"),
    ("Taxation Context", "POLICY", "ADMIN", "PAY"),
    ("Failure & Learning", "FAIL", "LEARN", "ADAPT"),
    ("Self-Made Myth", "INDIV", "≠", "SUCCESS"),
    ("Ecosystem Network", "LINK", "SHARE", "GROW"),
    ("Entrepreneurship Education", "STUDY", "PRACTICE", "DO"),
    ("Mentorship Value", "GUIDE", "NET", "KNOW"),
    ("Youth Career Pathway", "LEARN", "BUILD", "SELL"),
    ("Women + Youth + Tech", "INCL", "SKILL", "OPP"),
    ("Future Growth Areas", "AI", "AGRI", "FIN"),
    ("Nation Building Logic", "BIZ", "JOBS", "TAX"),
    ("What Pakistan Needs", "POLICY", "CAPITAL", "INFRA"),
    ("What Young Orakzai Needs", "SIGNAL", "MENTOR", "SKILL"),
    ("Research Gap Map", "DATA", "MISSING", "NEED"),
    ("Oral History Questions", "PAST", "NOW", "FUTURE"),
    ("Idea Validation", "ASK", "TEST", "PROVE"),
    ("Customer Discovery", "WHO", "WHY", "HOW"),
    ("Product Development", "DESIGN", "CODE", "SHIP"),
    ("Business Model", "VALUE", "COST", "PRICE"),
    ("Revenue Model", "SELL", "EARN", "SAVE"),
    ("Cash Flow Management", "IN", "↔", "OUT"),
    ("Team Building", "HIRE", "TRUST", "LEAD"),
    ("Hiring Strategy", "SKILL", "CULTURE", "FIT"),
    ("Leadership Logic", "VISION", "TEAM", "DO"),
    ("Market Research", "SIZE", "COMP", "NEED"),
    ("Competition Analysis", "THEM", "US", "GAP"),
    ("Innovation Cycle", "NEW", "BETTER", "FAST"),
    ("Startup Lifecycle", "SEED", "GROW", "EXIT"),
    ("SME Lifecycle", "START", "RUN", "STAY"),
    ("Family BIZ Lifecycle", "GEN 1", "GEN 2", "GEN 3"),
    ("Digital Business Stack", "APP", "CLOUD", "DATA"),
    ("Global Market Node", "EXPORT", "TRUST", "VALUE"),
    ("Export Pathway", "READY", "LINK", "SHIP"),
    ("Investment Pathway", "PITCH", "DEAL", "GROW"),
    ("Bootstrapping", "SAVE", "SELL", "GROW"),
    ("Venture Capital Node", "FUND", "SCALE", "EQUITY"),
    ("Angel Investment Node", "SEED", "ADVICE", "NET"),
    ("Business Mentorship", "LISTEN", "LEARN", "DO"),
    ("Youth Innovation Node", "NEW", "SPEED", "VALUE"),
    ("Women-led Enterprise", "SKILL", "LEAD", "GROW"),
    ("Rural Enterprise Node", "LOCAL", "AGRI", "WEB"),
    ("Diaspora Network Node", "DIASPORA", "LINK", "INVEST"),
    ("Orakzai-to-Market", "VILLAGE", "→", "GLOBAL"),
    ("Technology-to-Business", "CODE", "→", "PRODUCT"),
    ("Skill-to-Income Flow", "SKILL", "WEB", "PAY"),
    ("Problem-to-Product", "NEED", "→", "BUILD"),
    ("Product-to-Market", "READY", "→", "SELL"),
    ("Business-to-Jobs", "GROW", "→", "HIRE"),
    ("Entrepreneur-to-Eco", "PART", "GIVE", "GET"),
    ("Evidence Matrix Logic", "TOPIC", "DATA", "CONF"),
    ("Research Gap Analysis", "NEED", "FIND", "SAVE"),
    ("Final Statement Logic", "IDEA", "VALUE", "BUILD"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g115-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g115-{index}-title g115-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g115-{index}-title">{safe}</title><desc id="g115-{index}-desc">An entrepreneurial relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g115-{index}-caption" class="diagram-caption">{index}. {safe} — entrepreneurial concept.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Entrepreneurship in Pakistan</title><desc id="hero-desc">A conceptual landscape of Pakistani entrepreneurship showing a person at a workspace surrounded by a shop, factory, agriculture, laptop, and global connections.</desc><defs><linearGradient id="h115-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h115-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 215)"><circle cx="0" cy="0" r="120" fill="none" stroke="#B59654" stroke-opacity=".15"/><path d="M-60 20 Q 0 -100 60 20" fill="none" stroke="#B59654" stroke-width="2.5"/><circle cx="0" cy="-40" r="30" fill="none" stroke="#B59654" stroke-width="2.5"/><text x="0" y="70" text-anchor="middle" fill="#F5F0E6" font-size="14" font-weight="bold">ENTREPRENEUR</text></g><g transform="translate(120, 100)" opacity=".7"><rect x="0" y="0" width="100" height="60" rx="6" fill="#153B2A" stroke="#2E8B57"/><text x="50" y="35" text-anchor="middle" fill="#F5F0E6" font-size="10">SMALL SHOP</text></g><g transform="translate(540, 100)" opacity=".7"><rect x="0" y="0" width="100" height="60" rx="6" fill="#3C3020" stroke="#B59654"/><text x="50" y="35" text-anchor="middle" fill="#F5F0E6" font-size="10">FACTORY</text></g><g transform="translate(120, 300)" opacity=".7"><rect x="0" y="0" width="100" height="60" rx="6" fill="#202B35" stroke="#7894A8"/><text x="50" y="35" text-anchor="middle" fill="#F5F0E6" font-size="10">STARTUP</text></g><g transform="translate(540, 300)" opacity=".7"><rect x="0" y="0" width="100" height="60" rx="6" fill="#153B2A" stroke="#2E8B57"/><text x="50" y="35" text-anchor="middle" fill="#F5F0E6" font-size="10">AGRICULTURE</text></g><text x="380" y="50" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">ENTREPRENEURSHIP IN PAKISTAN</text><text x="380" y="80" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="12" font-style="italic">“From ideas and livelihoods to companies and opportunity.”</text><g transform="translate(380, 390)" opacity=".8"><text x="0" y="0" text-anchor="middle" fill="#B59654" font-size="10">SMEs • STARTUPS • FAMILY BUSINESS • INNOVATION</text></g></svg><figcaption id="hero-caption" class="diagram-caption">Entrepreneurship in Pakistan: A diverse ecosystem of livelihoods, production, and technology-enabled growth.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 115</title>
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
        .case-study-card {{ border: 1px solid var(--gold); padding: 30px; margin: 50px 0; background: rgba(181,150,84,0.05); }}
        .final-statement {{ text-align: center; font-size: 1.8rem; font-weight: 700; color: var(--gold); margin: 60px 0; }}
        @media (max-width: 768px) {{ .atlas-grid {{ grid-template-columns: 1fr; }} }}
        svg {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="content-page">
        <header class="page-header">
            <p class="section-label">PAGE 115</p>
            <h2>ENTREPRENEURSHIP IN PAKISTAN</h2>
            <p>“From ideas and livelihoods to companies and opportunity.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Entrepreneurship begins with a simple question: Can something be done differently? Sometimes the answer becomes a small shop. Sometimes it becomes a family business. Sometimes it becomes a factory. Sometimes it becomes a software company. Sometimes it begins with a laptop, an internet connection and an idea. Pakistan's entrepreneurial story is therefore much larger than the startup world. It includes shopkeepers, farmers, manufacturers, traders, craftspeople, freelancers, exporters, technology founders and families who have built businesses across generations. The common thread is not size. It is the willingness to turn an idea, skill, resource or opportunity into something that creates value.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The SME Landscape (2025–2026)</h3>
                <p>According to the <strong>Pakistan Economic Survey 2025–26</strong>, Small and Medium Enterprises (SMEs) are a crucial force for job creation, industrial growth, and value addition. The State Bank of Pakistan (SBP) provides regulatory definitions to facilitate financing and support for these enterprises.</p>
                <table class="data-table">
                    <thead>
                        <tr><th>Category</th><th>Annual Sales Turnover</th><th>Source</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Micro Enterprise</td><td>Up to PKR 30 Million</td><td>SBP (July 16, 2026)</td></tr>
                        <tr><td>Small Enterprise</td><td>PKR 30 Million to 400 Million</td><td>SBP (July 16, 2026)</td></tr>
                        <tr><td>Medium Enterprise</td><td>PKR 400 Million to 2 Billion</td><td>SBP (July 16, 2026)</td></tr>
                        <tr><td>Startup (Regulatory)</td><td>Up to 5 Years Old</td><td>SBP (July 16, 2026)</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Startup Ecosystem</h3>
                <p>Pakistan's startup ecosystem has evolved through a network of incubators, accelerators, and venture capital. The <strong>Pakistan Startup Fund (PSF)</strong>, managed by Ignite, provides non-equity grants ranging from <strong>US$50,000 to US$1,000,000</strong> to catalyze private and foreign investment. These programs aim to build technical entrepreneurship while addressing the inherent risks of uncertainty and failure.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: From Technology to Entrepreneurship</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Pakistani Technology Entrepreneur</strong></p>
                    <p>Faisal Orakzai serves as one contemporary case study of the transition from technical expertise to entrepreneurship. His pathway—moving from computer science and software systems to founding the <strong>Orakzai Group</strong> and <strong>OkzByte Hub</strong>—illustrates the "Builder's Model." By leveraging blockchain and AI, his projects show how individual technical interests can become organizational entities that create digital products for a global market.</p>
                    <p><em>“An individual case study—not a representation of Pakistan's entrepreneurs or the Orakzai community as a whole.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate, ResearchGate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Entrepreneurship in Pakistan</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Orakzai Identity and Enterprise</h3>
                <p>Entrepreneurship offers a bridge between tribal identity and modern markets. For Orakzai youth, digital entrepreneurship and e-commerce allow participation in national and global economies without abandoning their roots. However, success in rural areas requires addressing critical gaps in connectivity, financial literacy, and mentorship—priorities that remain central to sustainable development.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Research Gap: What Still Needs to be Documented</h3>
                <ul>
                    <li>Oral histories of Orakzai traders and traditional trading networks.</li>
                    <li>The impact of migration on Orakzai family business structures.</li>
                    <li>District-level data on women's entrepreneurship and informal commerce.</li>
                    <li>Long-term outcomes of technology-enabled businesses in remote communities.</li>
                </ul>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“Entrepreneurship sits between an idea and reality. Building it requires learning, testing, and continuing when the first version does not work. My own journey grew from an interest in computer science and digital systems. A company is not only a name; the real question is whether it solves a problem and creates value. The most meaningful form of entrepreneurship is not simply building something large, but building something useful that creates opportunity for others.”</p>
            </div>

            <div class="final-statement">
                ENTREPRENEURSHIP BEGINS WITH AN IDEA.<br>
                IT BECOMES MEANINGFUL WHEN THAT IDEA CREATES VALUE FOR OTHERS.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Ministry of Finance, <em>Pakistan Economic Survey 2025–26</em>.</li>
                    <li>State Bank of Pakistan (SBP), <em>Updated Prudential Regulations for SME Financing</em>, July 16, 2026.</li>
                    <li>Ignite / Ministry of IT, <em>Pakistan Startup Fund (PSF) Guidelines</em>, 2026.</li>
                    <li>SMEDA, <em>Strategic Pillars for SME Development 2026</em>.</li>
                    <li>World Bank, <em>Pakistan Entrepreneurship Ecosystem Assessment 2024</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            115
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

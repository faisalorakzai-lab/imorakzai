from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-153-youth-and-entrepreneurship.html'

GRAPHICS = [
    ("Youth Opportunity", "YOUT", "↔", "ECON"),
    ("Demographic Goal", "PEOP", "→", "GROW"),
    ("Productive Builder", "USER", "↔", "NEW"),
    ("Youth Assets", "CREA", "↔", "BASE"),
    ("Population Rail", "YOUT", "→", "VALU"),
    ("Education Path", "LEAR", "→", "SKIL"),
    ("Skills Path", "SKIL", "→", "WORK"),
    ("Employment Goal", "JOB", "↔", "YOUT"),
    ("Productivity Goal", "VALU", "↔", "DONE"),
    ("Economic Growth", "GROW", "↔", "NATL"),
    ("Problem Solver", "PROB", "→", "SOLU"),
    ("Entrepreneur Path", "IDEA", "→", "COMP"),
    ("Platform Builder", "BASE", "→", "MANY"),
    ("Process Innovation", "OLD", "→", "NEW"),
    ("Startup Ecosystem", "SEED", "↔", "GROW"),
    ("Shopkeeper Tech", "SHOP", "↔", "APP"),
    ("Farmer Tech", "FARM", "↔", "APP"),
    ("Manufacturer Tech", "MAKE", "↔", "APP"),
    ("Exporter Tech", "GLOB", "↔", "APP"),
    ("Developer Tech", "CODE", "↔", "APP"),
    ("Digital Founder", "USER", "↔", "CODE"),
    ("Cloud Access", "CLOU", "↔", "USER"),
    ("Payment Access", "PAY", "↔", "USER"),
    ("Market Access", "GLOB", "↔", "USER"),
    ("Social Access", "SOCL", "↔", "USER"),
    ("Remote Talent", "WORK", "↔", "NET"),
    ("Global Customer", "GLOB", "↔", "USER"),
    ("First Business", "TRY", "↔", "LEAR"),
    ("Small Experiment", "TEST", "↔", "DONE"),
    ("Learning Value", "FAIL", "→", "WISE"),
    ("Customer Need", "WANT", "↔", "DATA"),
    ("Pricing Logic", "CASH", "↔", "VALU"),
    ("Operational Logic", "RUN", "↔", "SAFE"),
    ("Market Response", "DATA", "↔", "USER"),
    ("Starting Small", "SEED", "→", "TREE"),
    ("Bootstrap Loop", "REV", "→", "GROW"),
    ("Reinvestment", "CASH", "→", "NEW"),
    ("Problem-First", "PROB", "↔", "BASE"),
    ("Customer First", "USER", "↔", "BASE"),
    ("Solution First", "SOLU", "↔", "BASE"),
    ("Test & Feedback", "TRY", "↔", "DATA"),
    ("Product Fit", "WANT", "↔", "HAVE"),
    ("Idea vs Biz", "IDEA", "≠", "CASH"),
    ("Customer Evidence", "DATA", "↔", "PAY"),
    ("Scalable Model", "ONE", "→", "MANY"),
    ("Technology Lever", "CODE", "↔", "GROW"),
    ("Small Team Power", "TEAM", "↔", "GLOB"),
    ("Operating Cost", "LESS", "↔", "CODE"),
    ("Digital Gen", "BORN", "↔", "NET"),
    ("Smartphone Base", "PHON", "↔", "LIFE"),
    ("Social Media Base", "SOCL", "↔", "LIFE"),
    ("Digital Familiar", "USER", "↔", "APP"),
    ("Geographic Bridge", "HOME", "↔", "GLOB"),
    ("Software Export", "CODE", "↔", "CASH"),
    ("Consulting Rail", "WISE", "↔", "NET"),
    ("Online Store", "SHOP", "↔", "NET"),
    ("Digital Content", "ART", "↔", "NET"),
    ("Global Platform", "PAK", "↔", "GLOB"),
    ("Freelancing Entry", "WORK", "↔", "NET"),
    ("Freelancer Skills", "SKIL", "↔", "DONE"),
    ("Client Manage", "USER", "↔", "DATA"),
    ("Communication", "TALK", "↔", "DONE"),
    ("Intl Experience", "GLOB", "↔", "DONE"),
    ("Freelancer to Co", "ONE", "→", "TEAM"),
    ("Agency Path", "TEAM", "→", "COMP"),
    ("Product Path", "CODE", "→", "OWN"),
    ("Global Business", "PAK", "↔", "GLOB"),
    ("AI Opportunity", "AI", "↔", "NEW"),
    ("AI Automation", "AI", "↔", "DONE"),
    ("AI Analytics", "AI", "↔", "DATA"),
    ("AI Education", "AI", "↔", "LEAR"),
    ("AI Healthcare", "AI", "↔", "DOC"),
    ("AI Finance", "AI", "↔", "FIN"),
    ("AI Agriculture", "AI", "↔", "FARM"),
    ("Blockchain Opportunity", "BC", "↔", "NEW"),
    ("Digital Assets", "TOK", "↔", "VALU"),
    ("Tokenization", "REAL", "→", "TOK"),
    ("Dapp Economy", "APP", "↔", "NET"),
    ("Digital Ownership", "OWN", "↔", "NET"),
    ("Responsible Dev", "SAFE", "↔", "CODE"),
    ("Fintech Solution", "TECH", "↔", "FIN"),
    ("Payment Solution", "PAY", "↔", "DONE"),
    ("Savings Solution", "SAVE", "↔", "DONE"),
    ("Credit Solution", "LOAN", "↔", "DONE"),
    ("Insurance Solution", "SAFE", "↔", "DONE"),
    ("E-commerce Brand", "BRAND", "↔", "NET"),
    ("Creative Biz", "ART", "↔", "GROW"),
    ("Design Economy", "DESI", "↔", "VALU"),
    ("Social Enterprise", "GOOD", "↔", "CASH"),
    ("Agri Biz", "FARM", "↔", "GROW"),
    ("Manufacturing Biz", "MAKE", "↔", "GROW"),
    ("Export Biz", "GLOB", "↔", "DONE"),
    ("Global-First", "GLOB", "↔", "IDEA"),
    ("Pakistani Brand", "PAK", "↔", "BRAND"),
    ("Intellectual Prop", "IP", "↔", "OWN"),
    ("Patent Value", "IDEA", "↔", "LAW"),
    ("Trademark Value", "NAME", "↔", "LAW"),
    ("Proprietary Data", "DATA", "↔", "OWN"),
    ("Entrepreneur Ed", "LEAR", "↔", "NEW"),
    ("Problem Solving", "WISE", "↔", "DONE"),
    ("Financial Lit", "CASH", "↔", "DATA"),
    ("Market Research", "DATA", "↔", "IDEA"),
    ("Univ Support", "UNI", "↔", "SEED"),
    ("Incubator Rail", "UNI", "↔", "GROW"),
    ("Mentorship Rail", "WISE", "↔", "NEW"),
    ("Research Comm", "IDEA", "→", "CASH"),
    ("Prototype Path", "IDEA", "→", "MAKE"),
    ("Market Path", "MAKE", "→", "USER"),
    ("Technical Skills", "CODE", "↔", "BASE"),
    ("Business Skills", "SALE", "↔", "BASE"),
    ("Negotiation", "TALK", "↔", "DONE"),
    ("Strategy Logic", "PLAN", "↔", "DONE"),
    ("English Access", "ENG", "↔", "GLOB"),
    ("Digital Literacy", "READ", "↔", "CODE"),
    ("Capital Stages", "IDEA", "→", "CASH"),
    ("Seed Capital", "SEED", "↔", "GROW"),
    ("Venture Capital", "VC", "↔", "GROW"),
    ("Scale Logic", "ONE", "↔", "ALL"),
    ("Bootstrapping", "OWN", "↔", "GROW"),
    ("Youth Optimism", "76%", "↔", "PAK"),
    ("Population 2026", "259M", "↔", "PAK"),
    ("Youth Under 30", "64%", "↔", "PAK"),
    ("Ecosystem Growth", "62%", "↔", "FY26"),
    ("Startup All-Time", "4.9M", "↔", "DONE"),
    ("Global Ranking", "#67", "↔", "DONE"),
    ("Digital Hub", "800K", "↔", "USER"),
    ("National Council", "4TH", "↔", "DONE"),
    ("Orakzai Youth", "ORAK", "↔", "NEW"),
    ("Regional Hub", "ORAK", "↔", "DPI"),
    ("Inclusive Growth", "ALL", "↔", "GROW"),
    ("Future Rail", "TIME", "↔", "NEW"),
    ("The Permanent Record", "STAY", "↔", "DONE"),
    ("Youth Empowerment", "POWR", "↔", "YOUT"),
    ("The Global Goal", "GLOB", "↔", "DONE"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g153-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g153-{index}-title g153-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g153-{index}-title">{safe}</title><desc id="g153-{index}-desc">A youth and entrepreneurship relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g153-{index}-caption" class="diagram-caption">{index}. {safe} — Youth-entrepreneurship relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Youth & Entrepreneurship Framework</title><desc id="hero-desc">A diagram showing the integrated stack of youth empowerment and the entrepreneurial engine for Pakistan's 2026 economy.</desc><defs><linearGradient id="h153-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h153-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE YOUTH-ENTERPRISE ENGINE (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DEMOGRAPHIC ASSET (64% Under 30 / 259M)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL YOUTH HUB (800K+ Active Users)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">STARTUP ECOSYSTEM (4.9M Total / +62% Growth)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">FREELANCE ECONOMY ($1B+ FY26 Earnings)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">KNOWLEDGE PATHWAY (Skills → Global Market)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">PROBLEM-FIRST INNOVATION (Local Solutions)</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">OPTIMISM & RESILIENCE (76% Positive Outlook)</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">YOUTH & ENTREPRENEURSHIP</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Building the Future Through the Power of the Next Generation.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Youth & Entrepreneurship Framework: The integrated stack of demographic assets, digital hubs, and the entrepreneurial engine in 2026.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 153</title>
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
            <p class="section-label">PAGE 153</p>
            <h2>YOUTH & ENTREPRENEURSHIP</h2>
            <p>“Building the Future Through the Power of the Next Generation.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Pakistan's young population represents one of the country's most important economic opportunities. Youth alone does not create growth; the opportunity emerges when young people have access to education, skills, capital, and markets. Entrepreneurship is the pathway through which this potential becomes value. From local businesses to global platforms, the next generation is building the productive nation of the future.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Demographic Catalyst of 2026</h3>
                <p>In 2026, Pakistan's population has reached an estimated **259.3 million**, with over **64% under the age of 30**. This "Youth Bulge" provides a massive workforce of approximately **165 million young people**. Far from being a burden, this demographic is a primary source of national optimism; a 2026 UNFPA report found that **76% of young Pakistanis** remain optimistic about their future prospects, driven by the expanding opportunities in the digital economy and the democratization of entrepreneurship.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Startup Ecosystem Boom</h3>
                <p>Pakistan's startup ecosystem has entered a new phase of growth, recording a **62.2% growth rate** in the FY25-26 period. The country now counts an all-time high of **4.9 million startups**, including tech-enabled SMEs and high-growth ventures. Ranking **#67 globally** in the Startup Ecosystem Index, Pakistan is becoming a regional hub for innovation. Through the **Finance Bill 2026**, the government has introduced key reforms to support seed capital, venture debt, and research commercialization, turning discoveries into products.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Youth Hub & Institutional Support</h3>
                <p>The **Prime Minister's Digital Youth Hub (DYH)** serves as the central rail for youth empowerment, reaching over **800,000 active users** by June 2026. This platform, developed in partnership with international agencies, provides a centralized space for skills development, mentorship, and opportunity exploration. By connecting youth in remote areas like Orakzai to national platforms, the DYH bridges the geographic divide, ensuring that every young builder has the tools to succeed in the modern economy.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">From Freelancing to Global Products</h3>
                <p>The pathway to productivity for the digital generation often begins with **Freelancing**, which generated over **$1 billion** in FY26. However, the 2026 strategy focuses on moving from individual services to building **Agencies, Products, and Global Businesses**. By leveraging skills in AI, software engineering, and digital marketing, young entrepreneurs are creating Pakistani brands that compete on the global stage. This "Global-First" mindset allows founders to solve local problems while designing solutions for international markets.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Youth & Entrepreneurship</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“The youth are not just the leaders of tomorrow; they are the builders of today. For the Orakzai community, entrepreneurship means that the valley is no longer a place of limited options—it is a launchpad for global enterprise. A young founder in Orakzai can now access the same cloud infrastructure and global markets as a founder in London or San Francisco. We are building a nation where ideas have no boundaries and where every young person has the power to create a sovereign future.”</p>
            </div>

            <div class="final-statement">
                YOUTH IS POTENTIAL.<br>
                ENTERPRISE IS DESTINY.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Worldometers / UN Population Data, <em>Pakistan Population Projections and Demographic Profiles (August 2026)</em>.</li>
                    <li>Press Information Department (PID), <em>Prime Minister's Digital Youth Hub Reaches 800,000 Active Users (June 2026)</em>.</li>
                    <li>LinkedIn / Industry Analysis, <em>Pakistan's Startup Ecosystem Outlook 2026: 4.9 Million Startups and Growth Trends (Feb 2026)</em>.</li>
                    <li>UNFPA / ProPakistani, <em>Youth Sentiment Report 2026: 76% Optimism Index (2026)</em>.</li>
                    <li>StartupBlink / Global Index, <em>Pakistan's Global Startup Ranking and Ecosystem Performance FY25-26 (2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            153
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

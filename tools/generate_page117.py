from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-117-pakistani-startup-ecosystem.html'

GRAPHICS = [
    ("Startup Ecosystem Hero", "IDEA", "ECOSYSTEM", "GLOBAL"),
    ("What is a Startup?", "PROBLEM", "→", "SCALE"),
    ("What is an Ecosystem?", "PARTS", "+", "NETWORK"),
    ("Early Internet Era", "WEB", "MODEM", "BIZ"),
    ("Software Houses", "SERVICE", "→", "EXPERIENCE"),
    ("Mobile Internet", "PHONE", "APP", "USER"),
    ("Digital Payments", "CASH", "→", "DIGITAL"),
    ("Fintech Ecosystem", "PAY", "LEND", "SAVE"),
    ("E-commerce Startups", "STORE", "PAY", "SHIP"),
    ("Healthtech Wave", "DOCTOR", "WEB", "CARE"),
    ("Edtech Pathways", "LEARN", "SKILL", "FUTURE"),
    ("Agritech Innovation", "FARM", "DATA", "MARKET"),
    ("Logistics Startups", "ROAD", "WARE", "DEL"),
    ("SaaS Model", "CODE", "CLOUD", "$$$"),
    ("AI Startups", "DATA", "AI", "VALUE"),
    ("The Founder", "PROBLEM", "RISK", "DO"),
    ("The Team", "TECH", "BIZ", "OPS"),
    ("Universities", "TALENT", "RES", "START"),
    ("NIC Network", "IGNITE", "NIC", "GROW"),
    ("Accelerators", "FAST", "SCALE", "WIN"),
    ("Invest2Innovate", "DATA", "LINK", "GROW"),
    ("Venture Capital", "RISK", "$$$", "EQUITY"),
    ("Funding Stages", "SEED", "A", "GROWTH"),
    ("Angel Investors", "MENTOR", "$", "NETWORK"),
    ("VC Ecosystem", "LOCAL", "INTL", "DIAS"),
    ("Diaspora Investor", "LINK", "CAP", "KNOW"),
    ("Government Role", "POLICY", "INFRA", "$"),
    ("Pakistan Startup Fund", "GRANT", "IGNITE", "BIZ"),
    ("Regulation Logic", "LAW", "TAX", "TRUST"),
    ("SECP Digital", "REG", "WEB", "FAST"),
    ("SBP Fintech", "BANK", "PAY", "SAFE"),
    ("The Customer", "NEED", "BUY", "FIX"),
    ("Product-Market Fit", "PROB", "+", "SOL"),
    ("The Pivot", "TEST", "DATA", "CHANGE"),
    ("Startup Failure", "CASH", "TEAM", "MKT"),
    ("Funding Paradox", "$$$", "≠", "SUCCESS"),
    ("Burn Rate Logic", "CASH", "-", "EXP"),
    ("Revenue Models", "SUB", "FEE", "AD"),
    ("Global Markets", "PAK", "→", "WORLD"),
    ("Remote Entrepreneur", "HOME", "WEB", "TEAM"),
    ("Freelancer Role", "SKILL", "CLIENT", "KNOW"),
    ("Women Entrepreneurs", "WIN", "LOAN", "GROW"),
    ("Youth Potential", "SKILL", "WEB", "OPP"),
    ("Orakzai Startup Path", "ROOTS", "TECH", "BIZ"),
    ("Faisal Case Study", "TECH", "FOUND", "GLOBAL"),
    ("Faisal Path Logic", "ID", "CODE", "BIZ"),
    ("Idea-to-Company", "FIND", "TEST", "SCALE"),
    ("Ecosystem Map Node", "GOVT", "UNIV", "BIZ"),
    ("Pakistani Advantage", "YOUTH", "COST", "TALENT"),
    ("Structural Challenges", "MACRO", "LAW", "INFRA"),
    ("Brain Drain Logic", "OUT", "↕", "LINK"),
    ("Diaspora Knowledge", "NET", "KNOW", "PAK"),
    ("Startup Exits", "ACQ", "IPO", "SALE"),
    ("Ecosystem Maturity", "EXIT", "CAP", "TALENT"),
    ("Startup Culture", "PITCH", "MEET", "CODE"),
    ("Failure and Learning", "FAIL", "→", "LEARN"),
    ("Startup Ethics", "PRIV", "DATA", "FAIR"),
    ("AI Startup Wave", "GPT", "DATA", "SOL"),
    ("Future Sectors", "AI", "CLIM", "AGRI"),
    ("Orakzai Youth Node", "WEB", "SKILL", "PATH"),
    ("Future Ecosystem", "INTL", "NET", "GROW"),
    ("Founder Network", "LINK", "HELP", "DO"),
    ("Customer Feedback", "ASK", "LIST", "FIX"),
    ("Product Iteration", "BUILD", "TEST", "FIX"),
    ("Market Validation", "BUY", "YES", "GROW"),
    ("Startup Team Node", "HACK", "HIP", "HUS"),
    ("Technology Stack", "OS", "DB", "API"),
    ("Cloud Infra", "AWS", "AZ", "GC"),
    ("Developer Ecosystem", "GIT", "STACK", "DEV"),
    ("Open Source Logic", "FREE", "SHARE", "BUILD"),
    ("Digital Skills Node", "CODE", "DATA", "UX"),
    ("Global Talent Node", "HIRE", "WORK", "WIN"),
    ("Remote Teams Node", "ZONE", "WEB", "SYNC"),
    ("Startup Capital", "PRE", "SEED", "A"),
    ("Investor Network", "LP", "GP", "BIZ"),
    ("University Pipeline", "LAB", "IDE", "OUT"),
    ("Incubator Pipeline", "NIC", "TRAIN", "OUT"),
    ("Accelerator Pipeline", "SCALE", "FAST", "OUT"),
    ("Customer Acquisition", "AD", "SEO", "USER"),
    ("Startup Scaling", "CAP", "SYS", "GROW"),
    ("Startup Risk Node", "MKT", "TECH", "EXEC"),
    ("Startup Runway", "CASH", "/", "BURN"),
    ("Revenue Growth", "USER", "PAY", "GROW"),
    ("Global Customer Node", "US", "UK", "UAE"),
    ("Export Startup", "CODE", "→", "WORLD"),
    ("Pak Startup Global", "ISB", "→", "NYC"),
    ("Diaspora Startup Net", "UK", "US", "PAK"),
    ("Regional Entrepreneur", "PSH", "LHR", "KHI"),
    ("Rural Entrepreneur", "VILL", "WEB", "BIZ"),
    ("Women-led Innovate", "WIN", "TECH", "BIZ"),
    ("Startup Ethics Node", "USER", "SAFE", "DATA"),
    ("AI & Entrepreneur", "LLM", "APP", "USER"),
    ("Startup Ethics Logic", "DATA", "PRIV", "LAW"),
    ("Failure Recovery", "FAIL", "TRY", "WIN"),
    ("Ecosystem Loop", "GIVE", "GET", "GROW"),
    ("Startup Lifecycle", "BORN", "GROW", "EXIT"),
    ("Evidence Matrix Logic", "DATA", "CONF", "SAVE"),
    ("Research Gap Node", "MISS", "NEED", "FIND"),
    ("Oral History Node", "PAST", "NOW", "NEXT"),
    ("Final Statement Logic", "BIZ", "EXPER", "PAK"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g117-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g117-{index}-title g117-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g117-{index}-title">{safe}</title><desc id="g117-{index}-desc">A startup relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g117-{index}-caption" class="diagram-caption">{index}. {safe} — startup concept.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">The Pakistani Startup Ecosystem</title><desc id="hero-desc">A conceptual map showing a Pakistan silhouette constructed from connected nodes of founders, capital, technology, and institutions.</desc><defs><linearGradient id="h117-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h117-bg)" stroke="#B59654" stroke-opacity=".55"/><path d="M380 80 L300 200 L380 350 L460 200 Z" fill="none" stroke="#B59654" stroke-width="1" stroke-dasharray="4 4" opacity=".3"/><circle cx="380" cy="215" r="80" fill="none" stroke="#B59654" stroke-width="2" opacity=".6"/><g transform="translate(380, 215)"><circle cx="0" cy="0" r="10" fill="#B59654"/><text x="0" y="25" text-anchor="middle" fill="#F5F0E6" font-size="12" font-weight="bold">STARTUP</text></g><g transform="translate(380, 80)"><circle cx="0" cy="0" r="5" fill="#2E8B57"/><text x="0" y="-10" text-anchor="middle" fill="#B59654" font-size="10">GOVERNMENT</text></g><g transform="translate(300, 200)"><circle cx="0" cy="0" r="5" fill="#7894A8"/><text x="-15" y="0" text-anchor="end" fill="#B59654" font-size="10">UNIVERSITY</text></g><g transform="translate(460, 200)"><circle cx="0" cy="0" r="5" fill="#7894A8"/><text x="15" y="0" text-anchor="start" fill="#B59654" font-size="10">INVESTOR</text></g><g transform="translate(380, 350)"><circle cx="0" cy="0" r="5" fill="#2E8B57"/><text x="0" y="20" text-anchor="middle" fill="#B59654" font-size="10">GLOBAL MARKET</text></g><text x="380" y="50" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">PAKISTANI STARTUP ECOSYSTEM</text><text x="380" y="390" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="12" font-style="italic">“Where ideas meet people, capital, technology and opportunity.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Startup Ecosystem: A network of connections between founders, institutions, and markets.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 117</title>
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
            <p class="section-label">PAGE 117</p>
            <h2>THE PAKISTANI STARTUP ECOSYSTEM</h2>
            <p>“Where ideas meet people, capital, technology and opportunity.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “A startup usually begins with something very small. A problem. A conversation. A prototype. A founder asking a simple question: Can this be done differently? In Pakistan, thousands of young people have asked that question in different ways. Some built software. Some created online marketplaces. Some developed financial technology. Some worked on education, healthcare, logistics, agriculture or artificial intelligence. Many failed. Some survived. A smaller number grew into companies serving customers far beyond their original market. Together, these people and institutions form something larger than individual companies. They form an ecosystem. An ecosystem is not only startups. It includes founders, employees, customers, universities, investors, banks, regulators, incubators, accelerators, mentors, technology providers and communities. When these parts connect effectively, an idea can become a company. And a company can become an engine of innovation.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Ecosystem Landscape (2025–2026)</h3>
                <p>Pakistan's startup ecosystem witnessed a significant rebound in 2026. After a period of adjustment in 2025, where equity funding was approximately <strong>US$36.6 million</strong>, the first half of 2026 saw a surge to <strong>US$113 million</strong> across 9 disclosed rounds. This 371% increase highlights renewed investor confidence in Pakistani technology companies.</p>
                <p>The ecosystem is supported by institutional pillars such as <strong>Ignite</strong>, which manages the <strong>National Incubation Centers (NIC 2.0)</strong> and the <strong>Pakistan Startup Fund (PSF)</strong>. These programs provide the infrastructure, mentorship, and catalytic grants necessary for early-stage experimentation and growth.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: An Orakzai Founder in the Digital Economy</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur</strong></p>
                    <p>Faisal Orakzai serves as a case study of a young Pakistani technology entrepreneur working across software, digital infrastructure, and blockchain ventures. His path—from computer science to founding projects like <strong>Orakzai Group</strong> and <strong>OkzByte Hub</strong>—illustrates how individuals from less-connected regions can participate in the digital economy. By adopting a "Global Thinking" mindset, his work addresses problems beyond a single physical location.</p>
                    <p><em>“This case study is included to illustrate how an individual from an Orakzai background can participate in Pakistan's emerging digital entrepreneurial economy... It should not be interpreted as a statistical representation of Orakzai entrepreneurs.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: The Startup Ecosystem</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Structural Challenges & Future Wave</h3>
                <p>While the ecosystem is growing, it faces structural challenges including macroeconomic volatility, limited exit opportunities, and a "brain drain" of technical talent. However, a new wave of startups in <strong>AI</strong>, <strong>Fintech</strong>, and <strong>Agritech</strong> is emerging, leveraging cloud infrastructure and remote-first models to serve both domestic and international markets.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Research Gap: What Still Needs to be Documented</h3>
                <ul>
                    <li>Startup histories and data from tribal districts and remote regions.</li>
                    <li>Long-term success rates and impact of regional incubation programs.</li>
                    <li>Documentation of quiet failures and the learning they provided to the ecosystem.</li>
                    <li>Detailed records of diaspora-led knowledge transfer and investment.</li>
                </ul>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“A startup is behind every company is a person who decided to try. Coming from an Orakzai background, I see the ecosystem as a new pathway for people who were historically distant from technology. You don't need to leave your identity behind to participate in the digital economy. You can build from where you are, learn from the world, and create something that reaches thousands. But the ecosystem must also learn from failure. The real measure is whether talented people have a fair opportunity to experiment, build, learn, and try again.”</p>
            </div>

            <div class="final-statement">
                STARTUPS ARE NOT ONLY COMPANIES.<br>
                THEY ARE EXPERIMENTS IN WHAT A COUNTRY CAN BUILD.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Data Darbar / Invest2Innovate, <em>Pakistan Startup Ecosystem Review 2025 & H1 2026</em>.</li>
                    <li>Ignite (Ministry of IT), <em>NIC 2.0 & Pakistan Startup Fund (PSF) Status 2026</em>.</li>
                    <li>Tracxn Technologies, <em>Pakistan Startup Funding Trends (May 2026)</em>.</li>
                    <li>State Bank of Pakistan (SBP), <em>Digital Banking & Fintech Regulation 2026</em>.</li>
                    <li>PSEB, <em>IT & ITeS Export Milestones FY 2025–26</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            117
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

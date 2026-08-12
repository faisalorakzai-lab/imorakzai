from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-114-young-pakistan-technology.html'

GRAPHICS = [
    ("Young Pakistan Technology Hero", "YOUTH", "TECH", "BUILD"),
    ("Youth Population 2025", "252M", "TOTAL", "26.5% YOUTH"),
    ("Youth Advantage", "IDEAS", "SKILLS", "GROWTH"),
    ("Digital Generation", "SMARTPHONE", "SOCIAL", "WEB"),
    ("First Digital Lesson", "YOUTUBE", "COMMUNITY", "LEARN"),
    ("Consumer to Creator", "WATCH", "→", "BUILD"),
    ("Coding Pathway", "PYTHON", "JS", "GO"),
    ("Computer Science", "SYSTEMS", "DATA", "ALGO"),
    ("AI in Education", "TUTOR", "ASSIST", "LEARN"),
    ("AI as a Tool", "EXPERIMENT", "VERIFY", "BUILD"),
    ("Freelance Generation", "$856M", "FY26", "SBP"),
    ("Remote Work Path", "PAKISTAN", "↔", "GLOBAL"),
    ("Startup Culture", "IDEA", "VC", "SCALE"),
    ("Entrepreneurial Reality", "IDEA", "+", "EXECUTION"),
    ("Young Builders", "DEV", "FOUNDER", "DESIGN"),
    ("Faisal Orakzai Case Study", "ONE", "JOURNEY", "PROFILE"),
    ("Faisal: Computer Science", "SYSTEMS", "ARCH", "INFRA"),
    ("Faisal: Builder Pathway", "LEARN", "→", "FOUNDER"),
    ("Faisal: Orakzai Identity", "IDENTITY", "+", "TECH"),
    ("Orakzai to Global", "LOCAL", "↔", "GLOBAL"),
    ("Youth & Orakzai Opp", "SKILL", "WEB", "JOBS"),
    ("Mountains & Internet", "TERRAIN", "↔", "SIGNAL"),
    ("Digital Education", "ONLINE", "LIB", "SKILLS"),
    ("Laptop Access FY26", "72,000", "UNITS", "PES"),
    ("e-Rozgaar Target", "250", "CENTERS", "MOIT"),
    ("Digital Skills Path", "BASIC", "→", "EXPERT"),
    ("Youth and AI Opp", "LEARN", "CODE", "BIZ"),
    ("AI Risks for Youth", "FAKE", "BIAS", "OVER-RELY"),
    ("Social Media Balance", "CONNECT", "↔", "OVERLOAD"),
    ("Gaming Ecosystem", "DEV", "ESPORTS", "3D"),
    ("Content Creation", "VIDEO", "PODCAST", "BIZ"),
    ("Cybersecurity Basics", "PASS", "MFA", "PRIV"),
    ("Digital Payments", "WALLET", "RAAST", "BIZ"),
    ("Women in Technology", "ACCESS", "SKILLS", "OPP"),
    ("Youth Outside Cities", "REMOTE", "RURAL", "ACCESS"),
    ("The Next Generation", "2026", "→", "2040"),
    ("What Young Pakistan Needs", "EDU", "INFRA", "TRUST"),
    ("What Young Orakzai Needs", "SIGNAL", "SKILLS", "MENTOR"),
    ("Youth as Culture Builders", "SAVE", "PASHTO", "VOICE"),
    ("The Young Builder Logic", "FAIL", "IMPROVE", "BUILD"),
    ("Research Gap: Youth", "LOCAL", "DATA", "NEED"),
    ("Oral History Tech", "RECORD", "ARCHIVE", "SAVE"),
    ("Learning Pathway", "CURIOSITY", "STUDY", "SKILL"),
    ("Coding Career", "CODE", "WORK", "EARN"),
    ("AI Learning Flow", "ASK", "AI", "LEARN"),
    ("Freelancer Flow", "SKILL", "CLIENT", "$"),
    ("Startup Lifecycle", "IDEA", "TEAM", "GROW"),
    ("Global Client Network", "US/UK", "GULF", "PAK"),
    ("Digital Ed Flow", "STUDENT", "LMS", "CERT"),
    ("Device Access Path", "LAPTOP", "INTERNET", "WORK"),
    ("Connectivity Path", "TOWER", "MOBILE", "DATA"),
    ("Skill-to-Income", "SKILL", "WEB", "PAY"),
    ("Youth Entrepreneurship", "FOUND", "BUILD", "SCALE"),
    ("Technology Ecosystem", "UNIV", "BIZ", "GOVT"),
    ("Youth Innovation", "NEW", "FAST", "VALUE"),
    ("Digital Opportunity", "ACCESS", "SKILLS", "JOBS"),
    ("Digital Divide Map", "IN", "↔", "OUT"),
    ("Urban Youth Hub", "KHI", "LHR", "ISB"),
    ("Rural Youth Path", "VILLAGE", "WEB", "OPP"),
    ("Orakzai Youth Path", "SKILL", "CONNECT", "MARKET"),
    ("Diaspora Mentorship", "GLOBAL", "→", "LOCAL"),
    ("Pashto Tech Path", "SCRIPT", "AI", "WEB"),
    ("Cultural Preservation", "PASHTO", "VOICE", "DATA"),
    ("Digital Heritage Flow", "ITEM", "DATA", "ARCH"),
    ("Responsible AI Path", "ETHICS", "VERIFY", "USE"),
    ("Cyber Awareness", "SECURE", "PRIV", "SAFE"),
    ("Digital Identity", "ID", "NADRA", "BIZ"),
    ("Digital Payment Flow", "USER", "RAAST", "SHOP"),
    ("Remote Work Pathway", "HOME", "WEB", "WORLD"),
    ("Global Market Node", "EXPORT", "TALENT", "VALUE"),
    ("Future Workforce", "AI", "DATA", "CLOUD"),
    ("2030 Tech Node", "AGENT", "EDGE", "5G"),
    ("2040 Tech Node", "QUANT", "BIO", "SPACE"),
    ("AI Workforce Node", "MODEL", "TRAIN", "USE"),
    ("Software Workforce", "ARCH", "CODE", "TEST"),
    ("Creative Tech Node", "DESIGN", "UX", "3D"),
    ("Digital Biz Node", "MARKET", "PAY", "SHIP"),
    ("Tech Education Flow", "SCHOOL", "LAB", "BIZ"),
    ("Youth Innovation Eco", "HUB", "FUND", "TEAM"),
    ("Pakistan Tech Network", "URBAN", "RURAL", "LINK"),
    ("Orakzai Tech Bridge", "HOME", "WEB", "DIASPORA"),
    ("Mountain-to-Global", "VILLAGE", "→", "WORLD"),
    ("Tradition-to-Tech", "MEMORY", "+", "CODE"),
    ("Learning-to-Building", "STUDY", "→", "CREATE"),
    ("Curiosity-to-Creation", "ASK", "→", "MAKE"),
    ("Youth Responsibility", "LEARN", "BUILD", "SERVE"),
    ("Generation-to-Gen", "PAST", "NOW", "FUTURE"),
    ("Evidence Matrix", "TOPIC", "DATA", "CONF"),
    ("Research Gap Map", "MISSING", "NEED", "RESEARCH"),
    ("Final Statement Logic", "YOUTH", "BUILD", "FUTURE"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g114-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g114-{index}-title g114-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g114-{index}-title">{safe}</title><desc id="g114-{index}-desc">A technological relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g114-{index}-caption" class="diagram-caption">{index}. {safe} — youth technology concept.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Young Pakistan & Technology</title><desc id="hero-desc">A young Pakistani technology creator at a desk integrated with a digital network, cloud, AI nodes, and global connections.</desc><defs><linearGradient id="h114-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h114-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 250)"><circle cx="0" cy="0" r="100" fill="none" stroke="#B59654" stroke-opacity=".2"/><path d="M-40 0 Q 0 -60 40 0" fill="none" stroke="#B59654" stroke-width="2"/><circle cx="0" cy="-30" r="20" fill="none" stroke="#B59654" stroke-width="2"/><text x="0" y="60" text-anchor="middle" fill="#F5F0E6" font-size="12">YOUNG CREATOR</text></g><g transform="translate(100, 100)" opacity=".6"><rect x="0" y="0" width="60" height="40" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="30" y="25" text-anchor="middle" fill="#F5F0E6" font-size="8">CODE</text></g><g transform="translate(600, 100)" opacity=".6"><rect x="0" y="0" width="60" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="30" y="25" text-anchor="middle" fill="#F5F0E6" font-size="8">AI</text></g><g transform="translate(100, 300)" opacity=".6"><rect x="0" y="0" width="60" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="30" y="25" text-anchor="middle" fill="#F5F0E6" font-size="8">GLOBAL</text></g><text x="380" y="50" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">YOUNG PAKISTAN & TECHNOLOGY</text><text x="380" y="80" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="12" font-style="italic">“A generation learning to build beyond geography.”</text><g transform="translate(380, 380)" opacity=".8"><text x="0" y="0" text-anchor="middle" fill="#B59654" font-size="10">CURIOSITY • EDUCATION • SKILLS • ENTREPRENEURSHIP</text></g></svg><figcaption id="hero-caption" class="diagram-caption">Young Pakistan & Technology: A multi-dimensional journey from curiosity to global participation.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 114</title>
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
            <p class="section-label">PAGE 114</p>
            <h2>YOUNG PAKISTAN & TECHNOLOGY</h2>
            <p>“A generation learning to build beyond geography.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “A country's technological future is often discussed in terms of machines, networks and software. But behind every technology statistic is a person. A student opening a laptop for the first time. A young developer writing code late at night. A freelancer working for a client in another country. A founder building a product from a small room. A researcher experimenting with artificial intelligence. A young person discovering that geography does not have to define the limits of their ambition. Pakistan is a young country. Its digital future will therefore be shaped not only by infrastructure and policy, but by what its young people learn, create and build. The story is already beginning.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Pakistan's Young Population</h3>
                <p>According to the <strong>Pakistan Economic Survey 2025–26</strong>, Pakistan's population stands at 252.09 million. The youth cohort (ages 15–29) accounts for 26.56% of the population, while the working-age group (15–64) represents 56.9%. This demographic profile provides a significant potential advantage for technology adoption and innovation-led growth.</p>
                <table class="data-table">
                    <thead>
                        <tr><th>Category</th><th>Value</th><th>Source</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Total Population (2025)</td><td>252.09 Million</td><td>Economic Survey 2025–26</td></tr>
                        <tr><td>Youth Cohort (15–29)</td><td>26.56%</td><td>Economic Survey 2025–26</td></tr>
                        <tr><td>Working Age (15–64)</td><td>56.9%</td><td>Economic Survey 2025–26</td></tr>
                        <tr><td>Internet Usage</td><td>57%</td><td>PBS HIES 2024–25</td></tr>
                        <tr><td>Smartphone Ownership</td><td>50%</td><td>PBS HIES 2024–25</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Digital Generation</h3>
                <p>Young Pakistanis are increasingly defined by their relationship with digital tools. Beyond social media and gaming, technology has become a primary medium for education and employment. The transition from <strong>Consumer to Creator</strong> is evident in the rise of coding, digital design, and content creation, often learned through online communities and open-source platforms.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Freelance Economy</h3>
                <p>Pakistan has become a leading regional hub for tech freelancing. The 2025–26 Economic Survey reports tech freelancer exports of <strong>US$856.3 million</strong> during July–March FY2026, marking a 51% increase. This allows young professionals to access global markets without the need for immediate physical migration, though barriers in payments and internet reliability remain.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: One Young Pakistani Technology Journey</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Young Pakistani Technology Entrepreneur</strong></p>
                    <p>Faisal Orakzai is a contemporary example of a young Pakistani engaging with the global technology economy. His journey reflects a focus on computer science, software systems, blockchain infrastructure, and artificial intelligence. As the Founder & Chairman of the <strong>Orakzai Group</strong> and <strong>OkzByte Hub</strong>, his work illustrates how technical curiosity can evolve into entrepreneurship and digital product building.</p>
                    <p><em>“One individual's path can provide a window into a broader possibility.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate, ResearchGate (Verified 2026). This is an individual case study—not a representation of an entire generation or community.</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Young Pakistan & Technology</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Youth and Orakzai: Contemporary Opportunity</h3>
                <p>For young people from Orakzai, digital technology reduces the constraints of physical geography. Mountains and distance no longer have to limit access to knowledge. Connectivity enables participation in remote work, digital education, and cultural preservation—allowing the next generation to carry their tribal identity into the global digital future.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Research Gap: What Still Needs to be Documented</h3>
                <ul>
                    <li>District-level digital skills and youth employment data.</li>
                    <li>Orakzai-specific technology participation and entrepreneurship.</li>
                    <li>The role of young women in the rural digital economy.</li>
                    <li>AI adoption and impact at the school and household levels.</li>
                </ul>
            </section>

            <div class="reflection-box" style="border: 1px solid var(--gold); padding: 30px; margin: 50px 0; background: rgba(181,150,84,0.05);">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“I belong to a generation that did not grow up watching technology from a distance. We grew up inside it. Software became a language, and the world became closer than geography suggested. My own journey is only one story, but it is an example of what becomes possible when curiosity turns into building. The future does not require us to abandon where we came from; it asks us to decide what we will build from it.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF PAKISTAN WILL NOT ONLY BE CONSUMED BY ITS YOUTH.<br>
                IT WILL BE BUILT BY THEM.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Ministry of Finance, <em>Pakistan Economic Survey 2025–26</em>.</li>
                    <li>Pakistan Bureau of Statistics (PBS), <em>HIES 2024–25</em>.</li>
                    <li>State Bank of Pakistan (SBP), <em>ICT Export Remittances Report FY2026</em>.</li>
                    <li>Ministry of IT & Telecom, <em>National AI Policy Framework 2025</em>.</li>
                    <li>Crunchbase / LinkedIn, <em>Faisal Orakzai Professional Profile</em>, 2026.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            114
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

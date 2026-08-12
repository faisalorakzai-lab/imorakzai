from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-111-pakistans-technology-revolution.html'

GRAPHICS = [
    ("What is a technology revolution?", "TECHNOLOGY", "ADOPTION", "CHANGE"),
    ("Pakistan Technology Timeline", "1947", "→", "2026"),
    ("Early Telecommunications", "TELEGRAPH", "TELEPHONE", "PTCL"),
    ("Radio & Broadcasting", "RADIO", "PUBLIC", "INFO"),
    ("Early Computing", "MAINFRAME", "UNIV", "RESEARCH"),
    ("Universities & Computing", "ENGINEERING", "CS", "TALENT"),
    ("Software Industry", "SOFTWARE", "SERVICES", "PSEB"),
    ("Internet Arrival", "DIAL-UP", "ISPS", "BACKBONE"),
    ("Internet & Society", "CONNECT", "INFO", "ACCESS"),
    ("Mobile Revolution", "MOBILE", "GSM", "3G/4G"),
    ("Mobile Money", "WALLET", "FINTECH", "SBP"),
    ("Broadband Growth", "FIBER", "MOBILE", "PTA"),
    ("Digital Divide", "INCOME", "GEO", "GENDER"),
    ("Electricity Infrastructure", "POWER", "STABILITY", "TECH"),
    ("Software Exports", "$4.18B", "GROWTH", "SBP"),
    ("Freelancing", "GLOBAL", "SKILLS", "REMOTE"),
    ("Startup Culture", "NIC", "PLAN9", "VC"),
    ("Startup Correction", "GROWTH", "FAILURE", "SCALE"),
    ("Fintech Ecosystem", "BANKING", "DIGITAL", "SBP"),
    ("Raast Payment System", "INSTANT", "P2P", "MERCHANT"),
    ("E-commerce", "ONLINE", "LOGISTICS", "TRUST"),
    ("Cloud Computing", "STORAGE", "COMPUTE", "INFRA"),
    ("Data Centers", "POWER", "SECURITY", "CLOUD"),
    ("Cybersecurity", "IDENTITY", "DATA", "PROTECT"),
    ("Digital Government", "NADRA", "FBR", "PORTAL"),
    ("Education Technology", "LMS", "ONLINE", "LEARN"),
    ("Language Technology", "UNICODE", "URDU", "PASHTO"),
    ("AI in Pakistan", "RESEARCH", "ML", "NLP"),
    ("National AI Policy", "GOVERNANCE", "SKILLS", "GOVT"),
    ("AI and Jobs", "OPP", "RISK", "SKILLS"),
    ("AI and Pashto", "OCR", "TRANS", "SPEECH"),
    ("AI and Heritage", "ARCHIVE", "TRANS", "ASSIST"),
    ("Blockchain", "LEDGER", "RECORD", "TRUST"),
    ("Web3", "DECENTRAL", "OWNER", "TOKEN"),
    ("Technology Regulation", "PTA", "SBP", "SECP"),
    ("Data Protection", "CONSENT", "PRIVACY", "ETHICS"),
    ("Digital Assets", "ASSET", "REG", "MARKET"),
    ("Technology Cities", "KHI", "LHR", "ISB"),
    ("Karachi Tech", "FINANCE", "STARTUP", "HUB"),
    ("Lahore Tech", "SOFTWARE", "UNIV", "HUB"),
    ("Islamabad Tech", "GOVT", "RESEARCH", "HUB"),
    ("Peshawar Tech", "UNIV", "SKILLS", "HUB"),
    ("Tech Outside Cities", "REMOTE", "RURAL", "ACCESS"),
    ("Orakzai & Technology", "MOBILE", "EDUCATION", "REMOTE"),
    ("Orakzai Youth", "CODING", "FREE", "OPP"),
    ("Orakzai Education", "ONLINE", "LIBRARIES", "ACCESS"),
    ("Orakzai Diaspora", "NETWORK", "DIGITAL", "BRIDGE"),
    ("Digital Preservation", "PASHTO", "VOICE", "ARCHIVE"),
    ("Tradition & Technology", "CONTINUITY", "CHANGE", "TRUST"),
    ("Digital Economy", "SKILLS", "CAPITAL", "TRUST"),
    ("Skills Gap", "ENGINEERING", "AI", "NEED"),
    ("Research & Innovation", "UNIV", "FUNDING", "LINK"),
    ("Brain Drain", "LOSS", "↔", "DIASPORA"),
    ("Technology & Women", "ACCESS", "SKILLS", "OPP"),
    ("Accessibility", "ASSISTIVE", "INCLUSION", "W3C"),
    ("Technology & Climate", "ENERGY", "WASTE", "GREEN"),
    ("Digital Trust", "SECURITY", "PRIVACY", "RELIABILITY"),
    ("Digital Sovereignty", "DATA", "INFRA", "SKILLS"),
    ("Tech Opportunities", "SOFTWARE", "AI", "FINTECH"),
    ("Constraints", "POWER", "SKILLS", "REG"),
    ("Future Technologies", "ROBOTICS", "EDGE", "QUANTUM"),
    ("Next Generation", "LEARN", "BUILD", "SERVE"),
    ("National Development", "PROD", "GOV", "EXPORTS"),
    ("Responsible Innovation", "ETHICS", "INCLUSION", "TRUST"),
    ("Evidence Matrix", "ERA", "DEV", "SOURCE"),
    ("Research Gap", "HISTORY", "LOCAL", "NEED"),
    ("Oral History Tech", "VOICE", "RECORD", "SAVE"),
    ("Author Reflection", "BRIDGE", "KNOWLEDGE", "FUTURE"),
    ("Final Statement", "PEOPLE", "LEARN", "FUTURE"),
    ("Telecom-to-AI Bridge", "INFRA", "DATA", "AI"),
    ("Infrastructure Stack", "POWER", "FIBER", "CLOUD"),
    ("Connectivity Map", "URBAN", "RURAL", "NETWORK"),
    ("Mobile Adoption", "200M", "PTA", "ACCESS"),
    ("Broadband Network", "150M", "PTA", "DATA"),
    ("Digital Payment Flow", "USER", "RAAST", "MERCHANT"),
    ("Startup Ecosystem", "NIC", "VC", "SCALE"),
    ("Freelancer Network", "PAKISTAN", "GLOBAL", "REMIT"),
    ("Software Pipeline", "CODE", "EXPORT", "SBP"),
    ("Cloud Architecture", "AWS", "AZURE", "LOCAL"),
    ("Data Center Security", "POWER", "COOL", "SECURE"),
    ("AI Ecosystem", "UNIV", "STARTUP", "GOVT"),
    ("Language AI", "URDU", "PASHTO", "LLM"),
    ("Digital Gov Flow", "CITIZEN", "DATA", "SERVICE"),
    ("Digital Ed Flow", "STUDENT", "LMS", "SKILL"),
    ("Digital Commerce", "BUYER", "PAY", "DELIVER"),
    ("Cyber Trust Model", "SEC", "PRIV", "RELIABLE"),
    ("Digital Divide Map", "ACCESS", "↔", "GAP"),
    ("Rural Connectivity", "TOWER", "SIGNAL", "VILLAGE"),
    ("Urban Tech Hub", "OFFICE", "TALENT", "CAPITAL"),
    ("Diaspora Bridge", "UK/US", "GULF", "PAK"),
    ("Orakzai Pathway", "SKILL", "CONNECT", "GLOBAL"),
    ("Skills Pathway", "LEARN", "WORK", "EARN"),
    ("Research Pathway", "UNIV", "LAB", "INDUSTRY"),
    ("Policy Cycle", "PLAN", "REG", "IMPACT"),
    ("Innovation Cycle", "IDEA", "BUILD", "SCALE"),
    ("Sovereignty Model", "DATA", "SKILLS", "INFRA"),
    ("Future Tech Stack", "AGENT", "EDGE", "QUANTUM"),
    ("Technology Ethics", "FAIR", "SECURE", "OPEN"),
    ("Pakistan to Future", "NOW", "→", "2100"),
    ("Tech Evolution", "INFRA", "SERVICES", "AI"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g111-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g111-{index}-title g111-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g111-{index}-title">{safe}</title><desc id="g111-{index}-desc">A technological relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g111-{index}-caption" class="diagram-caption">{index}. {safe} — technological framework.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Pakistan’s Technology Revolution</title><desc id="hero-desc">A conceptual map of Pakistan integrated with a technological timeline from early infrastructure to modern AI and digital services.</desc><defs><linearGradient id="h111-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h111-bg)" stroke="#B59654" stroke-opacity=".55"/><path d="M250 350 L 300 200 L 350 100 L 450 150 L 500 300 Z" fill="none" stroke="#2E8B57" stroke-opacity=".3" stroke-width="2"/><g transform="translate(100, 320)" font-family="Arial,sans-serif" font-size="10" fill="#B59654"><text x="0" y="0">TELECOM</text><circle cx="60" cy="-5" r="3"/><line x1="60" y1="-5" x2="150" y2="-40" stroke="#B59654" stroke-opacity=".4"/></g><g transform="translate(200, 250)" font-family="Arial,sans-serif" font-size="10" fill="#B59654"><text x="0" y="0">INTERNET</text><circle cx="60" cy="-5" r="3"/><line x1="60" y1="-5" x2="250" y2="-50" stroke="#B59654" stroke-opacity=".4"/></g><g transform="translate(350, 150)" font-family="Arial,sans-serif" font-size="10" fill="#B59654"><text x="0" y="0">MOBILE</text><circle cx="60" cy="-5" r="3"/><line x1="60" y1="-5" x2="450" y2="-20" stroke="#B59654" stroke-opacity=".4"/></g><g transform="translate(550, 100)" font-family="Arial,sans-serif" font-size="10" fill="#B59654"><text x="0" y="0">AI & CLOUD</text><circle cx="70" cy="-5" r="3"/></g><text x="380" y="50" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">PAKISTAN’S TECHNOLOGY REVOLUTION</text><text x="380" y="80" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="12" font-style="italic">“From connectivity to computation.”</text><g transform="translate(380, 380)" opacity=".8"><text x="0" y="0" text-anchor="middle" fill="#B59654" font-size="10">INFRASTRUCTURE • EDUCATION • INNOVATION</text></g></svg><figcaption id="hero-caption" class="diagram-caption">Pakistan’s Technology Revolution: A story of infrastructure, institutions, and human potential.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 111</title>
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
            <p class="section-label">PAGE 111</p>
            <h2>PAKISTAN’S TECHNOLOGY REVOLUTION</h2>
            <p>“From connectivity to computation.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Pakistan’s technology story did not begin with smartphones. It began with infrastructure. Telephones. Radio. Broadcasting. Early computing. Telecommunications networks. Universities. Engineering institutions. Then came the internet. Then the mobile phone. Then broadband. Then digital payments, software companies, online commerce and startup culture. Each generation built on the infrastructure created by the previous one.<br><br>
                Today, Pakistan is entering another technological transition. Artificial intelligence is changing how software is built. Cloud computing is changing infrastructure. Digital payments are changing commerce. And millions of young people are entering an economy where technical skills can connect local communities to global markets. The transformation is unfinished. Its opportunities are large. Its constraints are real. Pakistan's technology revolution is therefore not simply a story about innovation. It is a story about infrastructure, education, institutions, entrepreneurship and the ability of a society to adapt.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">What is a Technology Revolution?</h3>
                <p>A technology revolution occurs when technologies become capable of changing production, communication, commerce, education, government, employment, and social life. In Pakistan, this has been driven by the adoption of digital infrastructure and the development of technical human capital. We distinguish between historical facts, statistical data, and emerging trends.</p>
                <p><strong>TECHNOLOGY → ADOPTION → INFRASTRUCTURE → SKILLS → CHANGE</strong></p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Technology Evidence Matrix</h3>
                <table class="data-table">
                    <thead>
                        <tr><th>Era / Sector</th><th>Approx. Period</th><th>Main Development</th><th>Source</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Telecom Infrastructure</td><td>1947–1990s</td><td>Telegraph, Fixed-line, PTCL</td><td>Historical Records</td></tr>
                        <tr><td>Internet Adoption</td><td>1990s–2010</td><td>Dial-up, Broadband launch</td><td>PTA / ISPs</td></tr>
                        <tr><td>Mobile Revolution</td><td>2014–Present</td><td>3G/4G, Smartphone growth</td><td>PTA</td></tr>
                        <tr><td>Digital Economy</td><td>2018–Present</td><td>Fintech, Raast, Startups</td><td>SBP / PSEB</td></tr>
                        <tr><td>Emerging Tech (AI)</td><td>2024–Future</td><td>National AI Policy</td><td>Govt Policy</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Key Statistics (2025–2026)</h3>
                <ul>
                    <li><strong>Telecom (PTA):</strong> Surpassed 200 million subscribers and 150 million broadband users (June 2025).</li>
                    <li><strong>IT Exports (SBP):</strong> ICT export remittances reached $4.18 billion (July 2025 – May 2026).</li>
                    <li><strong>Monthly Record:</strong> Monthly IT exports hit $386 million in October 2025.</li>
                    <li><strong>Data Usage:</strong> Total data usage reached 27,727 petabytes in 2025.</li>
                </ul>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Digital Economy and Fintech</h3>
                <p>The rise of fintech, driven by the State Bank of Pakistan's <strong>Raast</strong> instant payment system and mobile wallets like Easypaisa and JazzCash, has transformed financial inclusion. Digital payments are no longer limited to urban centers but are reaching rural communities, including those in Orakzai, enabling new forms of commerce and remote work.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Pakistan’s Technology Revolution</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Orakzai and Technology</h3>
                <p>Orakzai communities are increasingly connected to Pakistan's digital infrastructure through mobile broadband. For Orakzai youth, technology offers pathways to coding, freelancing, and global markets. However, the <strong>Digital Divide</strong> remains a reality, constrained by electricity stability and network coverage in mountainous terrain. Connectivity allows for the digital preservation of Orakzai culture, connecting the homeland to its global diaspora.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Research Gap: What Still Needs to be Documented</h3>
                <ul>
                    <li>Pakistan's early computing history and regional technology archives.</li>
                    <li>The role of women in the early software industry.</li>
                    <li>Pashto computing and local-language AI development.</li>
                    <li>Digital preservation of Orakzai's own technological transition.</li>
                </ul>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“Technology changes quietly at first. A new telephone line. A computer in a classroom. A modem connecting to the internet. A mobile phone in a village. Then, suddenly, it becomes part of everyday life. For Orakzai communities, the opportunity is not simply to consume technology, but to build with it and preserve culture through it. A revolution is complete when people gain the knowledge and opportunity to use it.”</p>
            </div>

            <div class="final-statement">
                PAKISTAN'S TECHNOLOGY REVOLUTION IS NOT ONLY ABOUT MACHINES.<br>
                IT IS ABOUT PEOPLE WHO LEARN TO BUILD THE FUTURE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Pakistan Telecommunication Authority (PTA), <em>Telecom Indicators 2025</em>.</li>
                    <li>State Bank of Pakistan (SBP), <em>ICT Export Remittances Report 2025-2026</em>.</li>
                    <li>Pakistan Software Export Board (PSEB), <em>Annual Report 2025</em>.</li>
                    <li>Ministry of IT & Telecom, <em>National AI Policy Draft 2025</em>.</li>
                    <li>World Bank, <em>Pakistan Digital Economy Report 2024</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            111
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

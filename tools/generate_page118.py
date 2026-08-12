from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-118-software-digital-infrastructure.html'

GRAPHICS = [
    ("Software & Infra Hero", "INFRA", "SYSTEMS", "APPS"),
    ("What is Software?", "HARD", "+", "SOFT"),
    ("Digital Infrastructure", "NET", "SRV", "DATA"),
    ("Digital Stack", "PHYS", "NET", "APP"),
    ("Physical Infra", "CABLE", "TOWER", "DC"),
    ("Fiber Optics", "DATA", "→", "LIGHT"),
    ("Submarine Cables", "SEA", "↔", "LAND"),
    ("Mobile Networks", "CELL", "CORE", "NET"),
    ("Internet Exchange", "LOCAL", "IXP", "NET"),
    ("Data Centres", "SRV", "COOL", "POW"),
    ("Cloud Computing", "SRV", "WEB", "USER"),
    ("IaaS Logic", "CPU", "RAM", "DISK"),
    ("PaaS Logic", "OS", "DB", "RUN"),
    ("SaaS Logic", "SOFT", "WEB", "$$$"),
    ("Edge Computing", "USER", "↔", "EDGE"),
    ("Server Logic", "REQ", "SRV", "RES"),
    ("Database Types", "SQL", "NoSQL", "GRAPH"),
    ("API Concept", "APP", "API", "SRV"),
    ("Software Architecture", "MONO", "↔", "MICRO"),
    ("Monolith Logic", "ONE", "BIG", "APP"),
    ("Microservices", "MANY", "SMALL", "SRV"),
    ("Event-driven", "EVT", "→", "ACT"),
    ("Serverless Logic", "CODE", "RUN", "OFF"),
    ("Open Source", "FREE", "CODE", "COMM"),
    ("Developer Ecosystem", "GIT", "STACK", "DEV"),
    ("Software Houses", "SRV", "CODE", "$$$"),
    ("Software Products", "BUILD", "SCALE", "USER"),
    ("SaaS Products", "SUB", "CLOUD", "USE"),
    ("Digital Public Infra", "ID", "PAY", "DATA"),
    ("Digital Identity", "NADRA", "ID", "VER"),
    ("Digital Payments", "BANK", "PAY", "SEC"),
    ("Raast Logic", "FAST", "PAY", "SBP"),
    ("Digital Government", "GOVT", "WEB", "CIT"),
    ("Data Foundational", "DATA", "→", "VAL"),
    ("Data Governance", "PRIV", "SEC", "LAW"),
    ("Cybersecurity", "CONF", "INT", "AVAIL"),
    ("CIA Security Model", "C", "I", "A"),
    ("Supply-chain Sec", "DEV", "DEP", "APP"),
    ("Software Updates", "TEST", "REL", "MON"),
    ("Reliability Logic", "UP", "RED", "FAIL"),
    ("Disaster Recovery", "FAIL", "→", "REST"),
    ("Power Infra", "ELEC", "UPS", "SRV"),
    ("Digital Climate", "WAT", "CO2", "POW"),
    ("Pak Software Exports", "$4.6B", "FY26", "PSEB"),
    ("Remote Work", "HOME", "WEB", "TEAM"),
    ("Digital Entrepreneur", "IDEA", "INFRA", "BIZ"),
    ("Orakzai Connectivity", "ROOTS", "NET", "GLOB"),
    ("Faisal Case Study", "TECH", "SRV", "INFRA"),
    ("Faisal Philosophy", "PROB", "SYS", "SOFT"),
    ("Software as Bridge", "VILL", "↔", "WORLD"),
    ("Digital Sovereignty", "CTRL", "DATA", "LAW"),
    ("Open Standards", "SYS", "STD", "SYS"),
    ("Interoperability", "A", "↔", "B"),
    ("Future Computing", "AI", "QUANT", "ROB"),
    ("AI Compute Logic", "DATA", "GPU", "MOD"),
    ("Quantum Computing", "QBIT", "PROB", "SOL"),
    ("Robotics Logic", "SEN", "SOFT", "ACT"),
    ("Infrastructure Gap", "URB", "≠", "REM"),
    ("Urban vs Remote", "CITY", "↔", "DIST"),
    ("Digital Inclusion", "ACC", "AFF", "SKIL"),
    ("Future Infra", "5G", "AI", "EDGE"),
    ("Network Topology", "NODE", "LINK", "NET"),
    ("Client-Server", "CLI", "↔", "SRV"),
    ("Request-Response", "GET", "→", "OK"),
    ("DNS Concept", "NAME", "→", "IP"),
    ("Web Hosting", "FILE", "SRV", "WEB"),
    ("Domain Names", ".COM", ".PK", ".ORG"),
    ("HTTPS Logic", "SEC", "SSL", "WEB"),
    ("Encryption Logic", "KEY", "LOCK", "DATA"),
    ("Authentication", "USER", "PASS", "OK"),
    ("Cloud Storage", "FILE", "CLOUD", "ANY"),
    ("Cloud Databases", "DATA", "SCAL", "SRV"),
    ("API Gateway", "REQ", "GATE", "SRV"),
    ("Load Balancing", "REQ", "BAL", "SRV"),
    ("Caching Logic", "REQ", "FAST", "MEM"),
    ("Content Delivery", "SRV", "EDGE", "USER"),
    ("Monitoring Logic", "SRV", "EYE", "DATA"),
    ("Logging Logic", "ACT", "→", "FILE"),
    ("Backup Logic", "DATA", "→", "SAVE"),
    ("DR Recovery", "BACK", "→", "LIVE"),
    ("Software Testing", "CODE", "TRY", "OK"),
    ("Continuous Integ", "CODE", "MERG", "TEST"),
    ("Continuous Depl", "TEST", "PUSH", "LIVE"),
    ("Version Control", "V1", "V2", "GIT"),
    ("Git Workflow", "BRAN", "MERG", "MAIN"),
    ("Containerization", "APP", "BOX", "ANY"),
    ("Virtual Machines", "SOFT", "ON", "HARD"),
    ("Kubernetes Logic", "BOX", "ORCH", "SRV"),
    ("DB Replication", "DB", "→", "DB"),
    ("High Availability", "SRV", "+", "SRV"),
    ("Developer Skills", "CODE", "PROB", "DO"),
    ("Digital Talent", "BRAIN", "CODE", "WIN"),
    ("Global Soft Work", "PAK", "→", "GLOB"),
    ("Infra Economics", "$$$", "CAP", "OPS"),
    ("Digital Ecosystem", "PARTS", "NET", "WHO"),
    ("Infra Resilience", "STRON", "FAST", "SAFE"),
    ("Evidence Matrix", "DATA", "CONF", "SAVE"),
    ("Research Gap Node", "MISS", "NEED", "FIND"),
    ("Oral History Node", "PAST", "NOW", "NEXT"),
    ("Final Statement", "INFRA", "SOFT", "LIFE"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g118-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g118-{index}-title g118-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g118-{index}-title">{safe}</title><desc id="g118-{index}-desc">An infrastructure relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g118-{index}-caption" class="diagram-caption">{index}. {safe} — infrastructure concept.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Software & Digital Infrastructure</title><desc id="hero-desc">A layered diagram showing physical infrastructure at the bottom, servers and cloud in the middle, and applications at the top.</desc><defs><linearGradient id="h118-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h118-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(60, 320)" opacity=".8"><rect x="0" y="0" width="640" height="60" rx="4" fill="#3C3020" stroke="#B59654"/><text x="320" y="35" text-anchor="middle" fill="#F5F0E6" font-size="12">PHYSICAL: FIBER • SUBSEA CABLES • POWER • DATA CENTRES</text></g><path d="M380 320 L 380 260" stroke="#B59654" stroke-width="2" stroke-dasharray="4 4"/><g transform="translate(60, 200)" opacity=".9"><rect x="0" y="0" width="640" height="60" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="320" y="35" text-anchor="middle" fill="#F5F0E6" font-size="12">SYSTEMS: SERVERS • CLOUD • DATABASES • APIs • SECURITY</text></g><path d="M380 200 L 380 140" stroke="#B59654" stroke-width="2" stroke-dasharray="4 4"/><g transform="translate(60, 80)"><rect x="0" y="0" width="640" height="60" rx="4" fill="#202B35" stroke="#7894A8"/><text x="320" y="35" text-anchor="middle" fill="#F5F0E6" font-size="12">APPLICATIONS: FINTECH • E-COMMERCE • AI • GOVT SERVICES</text></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="22" font-weight="bold" letter-spacing="3">SOFTWARE & DIGITAL INFRASTRUCTURE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“The invisible systems behind the digital world.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Digital Stack: Vertical integration from physical hardware to visible applications.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 118</title>
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
            <p class="section-label">PAGE 118</p>
            <h2>SOFTWARE & DIGITAL INFRASTRUCTURE</h2>
            <p>“The invisible systems behind the digital world.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Most people experience technology through a screen. They open an application. Send a message. Transfer money. Watch a video. Buy something online. Or open a website. But beneath every one of these actions is another world. Networks carry the data. Servers process requests. Databases store information. Software turns instructions into services. Cloud platforms provide computing capacity. Data centres keep machines running. Cables connect cities and countries. Security systems protect the information moving through them. This hidden layer is digital infrastructure. And modern society increasingly depends on it. Pakistan's digital economy is therefore not built only by visible apps and startups. It is also built by the infrastructure underneath them.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Foundation: Physical & Network Layers</h3>
                <p>Pakistan's connection to the global internet is anchored by a network of international submarine cable systems, including <strong>AAE-1</strong>, <strong>PEACE</strong>, <strong>IMEWE</strong>, <strong>SMW-4</strong>, and <strong>SMW-5</strong>. The launch of <strong>SMW-6</strong> in 2025–26 marks a significant boost in bandwidth capacity. Internally, a growing fiber-optic backbone and mobile networks (led by Jazz, Zong, and PTCL) provide the connectivity that reaches users from urban centers to remote districts.</p>
                <p>Digital Public Infrastructure (DPI) provides the shared systems necessary for broad service delivery. This includes <strong>NADRA's</strong> identity layer and the State Bank of Pakistan's <strong>Raast</strong> instant payment system, which reduces friction for both public and private transactions.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Building with Software from an Orakzai Perspective</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur</strong></p>
                    <p>Faisal Orakzai serves as a personal case study within Pakistan's software and digital economy. His work involves moving between software development, digital platforms, and emerging infrastructure. Projects such as <strong>OkzByte Hub</strong>, <strong>Orakzai Group</strong>, and <strong>Orakzai Bond</strong> illustrate a "Systems Philosophy"—viewing software not just as code, but as part of a larger infrastructure that connects people across geographic distances. His approach highlights how individual founders can leverage blockchain and cloud systems to build digital products for a global audience.</p>
                    <p><em>“This case study illustrates one individual's pathway... It should not be interpreted as a statistical representation of Orakzai entrepreneurs.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Software & Infrastructure</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Future Computing & The Infrastructure Gap</h3>
                <p>The future of computing in Pakistan is being shaped by <strong>AI infrastructure</strong>, <strong>Edge computing</strong>, and the potential of <strong>Quantum systems</strong>. However, structural gaps remain, particularly the urban-remote divide in connectivity and the need for energy-resilient data centers. Addressing these gaps is essential for achieving true digital inclusion and a resilient digital economy.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Research Gap: What Still Needs to be Documented</h3>
                <ul>
                    <li>Regional data-centre capacity and local cloud infrastructure investment.</li>
                    <li>Detailed connectivity data for tribal districts and remote mountainous regions.</li>
                    <li>The role of women in software engineering and local open-source contributions.</li>
                    <li>Historical records of Pakistan's early digital networks and BBS systems.</li>
                </ul>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“When I look at software, I see systems. A piece of software can begin as a small experiment, but a serious service requires networks, servers, and security. Technology can reduce distance—a person far from a major center can still build a company that reaches the world. But infrastructure must not become invisible. We should understand who controls it and who is excluded. If Pakistan wants a stronger digital economy, it must build both: the software people see, and the infrastructure that allows it to exist.”</p>
            </div>

            <div class="final-statement">
                EVERY DIGITAL EXPERIENCE HAS AN INFRASTRUCTURE BEHIND IT.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Submarine Cable Map, <em>Pakistan Connectivity Status 2026</em>.</li>
                    <li>PTA, <em>Telecom Market Share & Broadband Growth Reports 2026</em>.</li>
                    <li>DPI Map, <em>Digital Public Infrastructure: Pakistan 2026</em>.</li>
                    <li>Mordor Intelligence, <em>Pakistan Data Center Market Forecast 2030</em>.</li>
                    <li>PSEB, <em>IT & Software Export Statistics FY 2025–26</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            118
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

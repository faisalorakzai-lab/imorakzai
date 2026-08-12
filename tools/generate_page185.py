from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-185-technology-as-the-future.html'

GRAPHICS = [
    ("Tech Future", "PAST", "↔", "NEXT"),
    ("Human Tool", "SELF", "↔", "ABLE"),
    ("System Path", "ONE", "→", "MANY"),
    ("Tech Accel", "FAST", "↔", "GROW"),
    ("Computing Rail", "DATA", "↔", "BASE"),
    ("Digital Infra", "GRID", "↔", "ALL"),
    ("Cloud Computing", "NET", "↔", "SAVE"),
    ("Edge Computing", "HERE", "↔", "FAST"),
    ("Distributed Comp", "MANY", "↔", "ONE"),
    ("HPC Rail", "FAST", "↔", "SCI"),
    ("Semiconductors", "BASE", "↔", "TECH"),
    ("Chip Economy", "CASH", "↔", "TECH"),
    ("Comp Arch", "PLAN", "↔", "DO"),
    ("AI Capability", "AI", "↔", "ALL"),
    ("Machine Learn", "DATA", "→", "KNOW"),
    ("Generative AI", "MAKE", "↔", "AI"),
    ("AI Infra", "BASE", "↔", "AI"),
    ("Human + AI", "WISE", "↔", "FAST"),
    ("AI Limitation", "AI", "≠", "TRUE"),
    ("AI Safety Rail", "SAFE", "↔", "AI"),
    ("AI Governance", "RULE", "↔", "AI"),
    ("Robotics Path", "BOT", "↔", "PHYS"),
    ("Industrial Bot", "MAKE", "↔", "BOT"),
    ("Service Robot", "HELP", "↔", "BOT"),
    ("Autonomous Sys", "SELF", "↔", "DO"),
    ("Human Oversight", "USER", "↔", "BOT"),
    ("Drones Rail", "FLY", "↔", "EYE"),
    ("Smart Machines", "EYE", "↔", "DO"),
    ("IoT Network", "LINK", "↔", "ALL"),
    ("Smart Cities", "CITY", "↔", "LINK"),
    ("Smart Infra", "GRID", "↔", "EYE"),
    ("Digital Twin", "PHYS", "↔", "DIGI"),
    ("Urban Tech", "CITY", "↔", "TECH"),
    ("Future Transp", "MOVE", "↔", "NEXT"),
    ("Electric Mobil", "GRID", "↔", "MOVE"),
    ("Energy Tech", "POWER", "↔", "BASE"),
    ("Renewable Ener", "SUN", "↔", "POWER"),
    ("Energy Storage", "SAVE", "↔", "POWER"),
    ("Nuclear Energy", "ATOM", "↔", "POWER"),
    ("Grid Tech Rail", "GRID", "↔", "LINK"),
    ("Water Tech", "SAFE", "↔", "TRUE"),
    ("Agri Tech Rail", "FARM", "↔", "TECH"),
    ("Precision Agri", "DATA", "↔", "FARM"),
    ("Food Systems", "COOK", "↔", "SAFE"),
    ("Biotechnology", "LIFE", "↔", "TECH"),
    ("Genomics Path", "GENE", "↔", "KNOW"),
    ("Comp Biology", "CODE", "↔", "LIFE"),
    ("Digital Health", "DOC", "↔", "NET"),
    ("Telemedicine", "HERE", "↔", "THERE"),
    ("Medical AI", "AI", "↔", "DOC"),
    ("Personalized Med", "ONE", "↔", "DOC"),
    ("Tech & Edu", "LEAR", "↔", "TECH"),
    ("Digital Class", "NET", "↔", "LEAR"),
    ("AI Education", "AI", "↔", "LEAR"),
    ("Tech & Finance", "CASH", "↔", "TECH"),
    ("Digital Payment", "PAY", "↔", "SAFE"),
    ("Fintech Path", "CASH", "↔", "TECH"),
    ("Blockchain Rail", "GRID", "↔", "TRUE"),
    ("Digital Assets", "OWN", "↔", "NET"),
    ("Tokenization", "PHYS", "→", "DIGI"),
    ("Decentralized", "MANY", "↔", "RULE"),
    ("Digital Identity", "SELF", "↔", "TRUE"),
    ("Privacy Rail", "SAFE", "↔", "DATA"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Zero-Trust Rail", "NONE", "↔", "SAFE"),
    ("Cryptography", "SEC", "↔", "TRUE"),
    ("Post-Quantum", "ATOM", "↔", "SEC"),
    ("Quantum Comp", "ATOM", "↔", "CODE"),
    ("Quantum Limit", "ATOM", "≠", "ALL"),
    ("Future Comput", "MANY", "↔", "ONE"),
    ("Software Rail", "CODE", "↔", "BASE"),
    ("Open Source", "OPEN", "↔", "ALL"),
    ("Software Eco", "LINK", "↔", "LINK"),
    ("Developer Econ", "MAKE", "↔", "CASH"),
    ("Programming", "IDEA", "→", "CODE"),
    ("Cyber-Physical", "CODE", "↔", "PHYS"),
    ("Automation Rail", "AUTO", "↔", "DONE"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g185-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g185-{index}-title g185-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g185-{index}-title">{safe}</title><desc id="g185-{index}-desc">A technology relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g185-{index}-caption" class="diagram-caption">{index}. {safe} — Technology relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Technology as the Future Framework</title><desc id="hero-desc">A diagram showing the 2026 technology landscape, featuring the $975B semiconductor market, the $39.75B digital twin market, and the convergence of AI and robotics.</desc><defs><linearGradient id="h185-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h185-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE TECHNOLOGICAL SYSTEMS LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SEMICONDUCTOR PEAK: $975B ANNUAL SALES</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL TWIN MARKET: $39.75B (2026)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AI GOES PHYSICAL: AI + ROBOTICS CONVERGENCE</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AGENTIC AI: PRODUCTION-READY INFRASTRUCTURE</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">NUCLEAR ENERGY RESURGENCE FOR DATA CENTERS</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: CYBER-PHYSICAL FUTURE</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SYSTEMS: INTERCONNECTED, SECURE & RESPONSIBLE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">TECHNOLOGY AS THE FUTURE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Building the Systems That Will Shape the Next Century: Interconnected and Sovereign.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Technological Systems Loop: Navigating the 2026 landscape where the convergence of AI, robotics, semiconductors, and digital twins forms the foundational infrastructure of a responsible and sovereign digital civilization.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 185</title>
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
            <p class="section-label">PAGE 185</p>
            <h2>TECHNOLOGY AS THE FUTURE</h2>
            <p>“Building the Systems That Will Shape the Next Century.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Technology has never been only about machines. At its deepest level, technology is humanity's ability to transform knowledge into tools, systems, and capabilities. Each technological transition changes not only what people can do, but also how societies organize themselves. The future will emerge from the interaction of computing, AI, robotics, biotechnology, and human institutions. The central challenge will not simply be building more powerful technology; it will be learning how to use technological power responsibly.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Semiconductor Peak & Chip Economy (2026)</h3>
                <p>By 2026, the global semiconductor industry has reached a historic peak, with annual sales expected to hit **$975 billion** [1] [2]. This growth is fueled by an intensifying AI landscape, where AI workloads account for a substantial share of new data center investment [3]. Future technological competitiveness depends on access to advanced semiconductor design, as the "chip economy" becomes the foundation for all modern computing and electronics [4] [5].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI Goes Physical: Robotics & Autonomy</h3>
                <p>A major trend in 2026 is **"AI Goes Physical"**—the convergence of AI and robotics [6]. Robots that use artificial intelligence to work independently are becoming common in industrial, service, and emergency response environments [7]. **Agentic AI** is moving from pilot projects to production infrastructure, allowing autonomous systems to make decisions within defined operating environments while maintaining appropriate human oversight [8] [9].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Twins & Smart Infrastructure</h3>
                <p>The global digital twin market has increased to **$39.75 billion in 2026**, projected to reach $122 billion by 2035 [10] [11]. Digital twins create computational representations of physical systems—from factories to entire cities—for real-time analysis and simulation [12]. Smart infrastructure, powered by IoT sensors and edge computing, is helping cities manage increasingly complex transportation, utility, and public service systems [13] [14].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Energy, Security & Sovereign Systems</h3>
                <p>Future computing requires reliable and efficient energy, leading to a **resurgence of nuclear energy** to power massive data centers [15]. Cybersecurity has become part of national security, with a focus on **Zero-Trust** architectures and post-quantum cryptography research [16] [17]. For the Orakzai community, the **Sovereign Grid** represents a cyber-physical future where technology is used responsibly to protect digital identity, data, and community values [18].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Technology as the Future</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, technology is the tool of our resilience. We do not just build machines; we build the systems that protect our sovereignty. By mastering semiconductors, AI, and digital twins while remaining rooted in our responsibility to lead, we are ensuring that the next century is shaped by our values. We are the architects of a digital civilization that is powerful, secure, and authentic.”</p>
            </div>

            <div class="final-statement">
                SYSTEMS OF POWER.<br>
                ROOTED IN RESPONSIBILITY.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Deloitte Insights, <em>2026 Global Semiconductor Industry Outlook: Historic Peak (February 2026)</em>.</li>
                    <li>BNP Paribas CIB, <em>Semiconductor Market 2026: Reaching nearly USD 917 Billion (March 2026)</em>.</li>
                    <li>Component Sense, <em>Semiconductor Industry Trends Report 2026: AI Workloads and Data Centers (2026)</em>.</li>
                    <li>Precedence Research, <em>AI in Semiconductor Market Size and Projections 2035 (2026)</em>.</li>
                    <li>LinkedIn / Industry Insights, <em>2026 Global Semiconductor Market: Structural Prosperity (February 2026)</em>.</li>
                    <li>Deloitte Insights, <em>Tech Trends 2026: AI Goes Physical and Robotics Convergence (December 2025)</em>.</li>
                    <li>International Federation of Robotics, <em>Top 5 Global Robotics Trends 2026: AI and Autonomy (2026)</em>.</li>
                    <li>Capgemini, <em>Insights on Top Tech Trends 2026: Agentic AI and Autonomous Robotics (2026)</em>.</li>
                    <li>Basis, <em>2026 Digital Advertising Trends: Agentic AI as Production Infrastructure (2026)</em>.</li>
                    <li>The Business Research Company, <em>Digital Twin Global Market Report 2026: Forecast to 2035 (2026)</em>.</li>
                    <li>MarketsandMarkets, <em>Digital Twin Market Size, Share & Trends: 2025-2030 Projections (2026)</em>.</li>
                    <li>Hexagon, <em>Where are Digital Twins Making an Impact? Statistics 2026 (2026)</em>.</li>
                    <li>Market.us, <em>Digital Twin Market Size and Share: CAGR of 38.2% (2026)</em>.</li>
                    <li>Stanford University, <em>2026 Emerging Technology Review: Innovations in AI, Robotics, and Biotech (January 2026)</em>.</li>
                    <li>Globant Reports, <em>Tech Trends 2026: 5 Forces Shaping the Future (2026)</em>.</li>
                    <li>YouTube / Tech Breakthroughs, <em>2026 Will Be Ruled by These 20 New Tech Trends (December 2025)</em>.</li>
                    <li>Orakzai Group Archives, <em>Technology as the Future and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            185
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

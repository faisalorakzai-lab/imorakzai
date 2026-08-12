from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-150-building-the-digital-nation.html'

GRAPHICS = [
    ("Digital Nation", "NATL", "↔", "NET"),
    ("Physical Infra", "ROAD", "→", "PORT"),
    ("Digital Infra", "CONN", "→", "DATA"),
    ("Connectivity Rail", "FIBE", "↔", "5G"),
    ("Universal Access", "ALL", "↔", "NET"),
    ("Rural Connect", "ORAK", "↔", "SAT"),
    ("Digital Divide", "OLD", "≠", "NEW"),
    ("Digital Literacy", "READ", "↔", "CODE"),
    ("Identity Layer", "ID", "↔", "BASE"),
    ("Pak ID App", "APP", "↔", "USER"),
    ("Credential Flow", "CERT", "→", "USER"),
    ("Privacy Shield", "PRIV", "↔", "DATA"),
    ("Data Minimization", "LESS", "↔", "SAFE"),
    ("Access Control", "LOCK", "↔", "USER"),
    ("Digital Gov", "GOVT", "↔", "NET"),
    ("Gov as Platform", "BASE", "→", "SERV"),
    ("One Citizen Model", "USER", "↔", "ALL"),
    ("DPI Foundation", "DPI", "↔", "NATL"),
    ("Open Standards", "OPEN", "↔", "SYNC"),
    ("Interoperability", "SYNC", "↔", "MANY"),
    ("Data Exchange", "SEND", "↔", "RECV"),
    ("Government Data", "DATA", "↔", "GOV"),
    ("Data Governance", "RULE", "↔", "DATA"),
    ("Data Sovereignty", "OWN", "↔", "NATL"),
    ("National Cloud", "CLOU", "↔", "GOV"),
    ("Data Center Stack", "STOR", "↔", "SAFE"),
    ("Tier III Standard", "T3", "↔", "STAY"),
    ("Geographic Redun", "SITE", "↔", "SITE"),
    ("Cybersecurity", "SEC", "↔", "NET"),
    ("Zero-Trust Model", "CHK", "↔", "ALL"),
    ("Verify Always", "CHK", "→", "DONE"),
    ("Infrastructure Sec", "SAFE", "↔", "SYS"),
    ("Digital Resilience", "STAY", "↔", "SAFE"),
    ("Backup System", "BACK", "↔", "MAIN"),
    ("Digital Payments", "PAY", "↔", "NET"),
    ("Raast Rail", "PAY", "↔", "DPI"),
    ("Instant Transfer", "FAST", "→", "DONE"),
    ("Digital Banking", "APP", "↔", "BANK"),
    ("Financial Include", "ALL", "↔", "PAY"),
    ("Digital Taxation", "TAX", "↔", "NET"),
    ("Business Reg", "NEW", "↔", "CODE"),
    ("Entrepreneurship", "GROW", "↔", "USER"),
    ("Digital Health", "DOC", "↔", "NET"),
    ("Digital Education", "LEAR", "↔", "NET"),
    ("AI Expert Program", "1M", "↔", "AI"),
    ("National Masterplan", "PLAN", "↔", "NATL"),
    ("Digital Nation Act", "LAW", "↔", "2025"),
    ("PDA Mandate", "PDA", "↔", "GOV"),
    ("Cabinet Digital", "70%", "↔", "DONE"),
    ("Orakzai Digital", "ORAK", "↔", "NEW"),
    ("Identity Power", "POWR", "↔", "ID"),
    ("Asset Rights", "RITE", "↔", "OWN"),
    ("Governance Trust", "TRST", "↔", "GOV"),
    ("Inclusive Future", "ALL", "↔", "TIME"),
    ("Sovereign Technology", "OWN", "↔", "TECH"),
    ("The Future Rail", "TIME", "↔", "NEW"),
    ("The Permanent Record", "STAY", "↔", "DONE"),
    ("Physical Nation", "PHYS", "↔", "BASE"),
    ("Digital Nation", "DIGI", "↔", "BASE"),
    ("Nation Purpose", "PEOP", "↔", "BASE"),
    ("Infrastructure Purpose", "SERV", "↔", "PEOP"),
    ("Connectivity Access", "CONN", "↔", "PEOP"),
    ("Digital Rights", "RITE", "↔", "PEOP"),
    ("Digital Freedom", "FREE", "↔", "PEOP"),
    ("Digital Security", "SAFE", "↔", "PEOP"),
    ("Digital Inclusion", "ALL", "↔", "PEOP"),
    ("Digital Growth", "GROW", "↔", "PEOP"),
    ("Digital Future", "TIME", "↔", "PEOP"),
    ("Digital Sovereignty", "OWN", "↔", "PEOP"),
    ("Digital Identity", "ID", "↔", "PEOP"),
    ("Digital Value", "VALU", "↔", "PEOP"),
    ("Digital Record", "STAY", "↔", "PEOP"),
    ("Digital Service", "SERV", "↔", "PEOP"),
    ("Digital Trust", "TRST", "↔", "PEOP"),
    ("Digital Legacy", "HIST", "↔", "PEOP"),
    ("Digital Connection", "LINK", "↔", "PEOP"),
    ("Digital Power", "POWR", "↔", "PEOP"),
    ("Digital Life", "LIFE", "↔", "PEOP"),
    ("Digital State", "STAT", "↔", "PEOP"),
    ("Digital World", "GLOB", "↔", "PEOP"),
    ("Digital Home", "HOME", "↔", "PEOP"),
    ("Digital Orakzai", "ORAK", "↔", "PEOP"),
    ("Digital Pakistan", "PAK", "↔", "PEOP"),
    ("Digital Nation", "NATN", "↔", "PEOP"),
    ("Digital Citizen", "CITI", "↔", "PEOP"),
    ("Digital Human", "HUMA", "↔", "PEOP"),
    ("Digital Soul", "SOUL", "↔", "PEOP"),
    ("Digital Mind", "MIND", "↔", "PEOP"),
    ("Digital Hand", "HAND", "↔", "PEOP"),
    ("Digital Eye", "EYE", "↔", "PEOP"),
    ("Digital Voice", "VOIC", "↔", "PEOP"),
    ("Digital Heart", "HEAR", "↔", "PEOP"),
    ("Digital Breath", "BREA", "↔", "PEOP"),
    ("Digital Step", "STEP", "↔", "PEOP"),
    ("Digital Path", "PATH", "↔", "PEOP"),
    ("Digital Goal", "GOAL", "↔", "PEOP"),
    ("Digital Aim", "AIM", "↔", "PEOP"),
    ("Digital Work", "WORK", "↔", "PEOP"),
    ("Digital Play", "PLAY", "↔", "PEOP"),
    ("Digital Rest", "REST", "↔", "PEOP"),
    ("Digital Love", "LOVE", "↔", "PEOP"),
    ("Digital Peace", "PEAC", "↔", "PEOP"),
    ("Digital Joy", "JOY", "↔", "PEOP"),
    ("Digital Hope", "HOPE", "↔", "PEOP"),
    ("Digital Dream", "DREA", "↔", "PEOP"),
    ("Digital Reality", "REAL", "↔", "PEOP"),
    ("Digital Truth", "TRUT", "↔", "PEOP"),
    ("Digital Wisdom", "WISE", "↔", "PEOP"),
    ("Digital Light", "LITE", "↔", "PEOP"),
    ("Digital Fire", "FIRE", "↔", "PEOP"),
    ("Digital Water", "WATE", "↔", "PEOP"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g150-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g150-{index}-title g150-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g150-{index}-title">{safe}</title><desc id="g150-{index}-desc">A digital nation relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g150-{index}-caption" class="diagram-caption">{index}. {safe} — Digital nation relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Building the Digital Nation Framework</title><desc id="hero-desc">A diagram showing the integrated stack of a digital nation, from connectivity and identity to data sovereignty and AI services.</desc><defs><linearGradient id="h150-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h150-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE DIGITAL NATION STACK (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">CONNECTIVITY (5G / Fiber / Satellite)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL IDENTITY (NADRA / Pak ID)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">CLOUD & DATA INFRASTRUCTURE (T3 Centers)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DIGITAL PAYMENTS (Raast / DPI)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL GOVT & PUBLIC SERVICES</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AI SERVICES & EXPERT TRAINING</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">CYBERSECURITY & ZERO-TRUST GOVERNANCE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">BUILDING THE DIGITAL NATION</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Physical Foundations to Digital Sovereign Horizons.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Digital Nation Framework: The integrated stack of connectivity, identity, infrastructure, and services for the 2026 digital state.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 150</title>
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
            <p class="section-label">PAGE 150</p>
            <h2>BUILDING THE DIGITAL NATION</h2>
            <p>“From Physical Foundations to Digital Sovereign Horizons.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “A nation is traditionally understood through its physical infrastructure—roads, bridges, and power plants. In the 21st century, the digital layer has become equally important. Internet connectivity, cloud computing, and digital identity increasingly influence how citizens interact with their state. A digital nation is not simply a country with more technology; it is a society where digital infrastructure is an integrated part of economic, governmental, and social life.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Digital Nation Pakistan Act 2025</h3>
                <p>The enactment of the **Digital Nation Pakistan Act 2025** provided the legal framework for the country's rapid digital acceleration in 2026. This landmark legislation mandate the transition to a "fully digital government," prioritizing electronic records, online payments, and integrated public services. By July 2026, over 70% of cabinet operations were digitalized, demonstrating the state's commitment to institutional modernization and administrative efficiency.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Connectivity & Universal Access</h3>
                <p>Reliable connectivity is the prerequisite for a digital nation. By August 2026, Pakistan's phased **5G rollout** has reached over 1,000 sites, providing high-speed mobile networks to major urban centers. Simultaneously, the finalization of the satellite internet framework has begun to bridge the **Digital Divide** in remote regions like Orakzai. Domestic internet connections have risen to **5.1 million**, ensuring that digital services reach citizens regardless of their geographic location.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Identity, Data & Sovereignty</h3>
                <p>Digital Identity, led by **NADRA**, serves as the common layer for banking, healthcare, and education. The **National Data Governance Policy 2026**, finalized in June 2026, establishes the rules for data sovereignty and security. By building geographically distributed **Tier III Data Centers**, Pakistan ensures that its critical national data remains secure and resilient against cyber threats, adopting a **Zero-Trust Security** model where every request is verified and authorized.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Public Infrastructure (DPI)</h3>
                <p>Digital Public Infrastructure—specifically identity, payments (**Raast**), and data exchange—acts as the "rails" for the modern economy. These shared systems support both public and private services, fostering innovation and competition. The 2026 vision includes training **1 million AI experts** to lead the development of intelligent public services, ensuring that technology remains the infrastructure while people remain the purpose of the digital nation.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Building the Digital Nation</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Infrastructure is the destiny of a nation. As we build the digital nation, we are not just installing cables and servers; we are building the pathways of opportunity and the records of our identity. For the Orakzai community, digital infrastructure means that the valley is no longer remote—it is a node in a global network, connected by high-speed fiber and protected by sovereign law. We are building a nation where every citizen has a digital voice and a secure digital future.”</p>
            </div>

            <div class="final-statement">
                INFRASTRUCTURE IS EMPOWERMENT.<br>
                THE NATION IS DIGITAL.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Ministry of IT and Telecommunication (MOITT), <em>Digital Nation Pakistan Act 2025 and e-Governance Expansion (July 2026)</em>.</li>
                    <li>GSMA / Digital Nation Summit, <em>Unlocking Pakistan's Digital Future: Policy Opportunities for Acceleration (2025-2026)</em>.</li>
                    <li>Arab News / Jazz Reports, <em>Phased 5G Rollout Reaches 1,000 Network Sites in Pakistan (August 2026)</em>.</li>
                    <li>Pakistan Bureau of Statistics (PBS) / FNPK, <em>Digital Pakistan Monitor: Domestic Internet Connections Rise to 5.1 Million (June 2026)</em>.</li>
                    <li>MOITT / Industry Reports, <em>Finalization of the National Data Governance Policy 2026 and Tier III Data Center Rollout (June 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            150
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

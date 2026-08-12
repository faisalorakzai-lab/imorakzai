from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-146-digital-governance.html'

GRAPHICS = [
    ("Digital Governance", "GOVT", "↔", "NET"),
    ("Digital State Model", "INST", "→", "DATA"),
    ("Public Service Flow", "USER", "↔", "GOV"),
    ("DPI Foundation", "BASE", "→", "SERV"),
    ("Digital Identity Rail", "ID", "↔", "BASE"),
    ("Payment Rail", "PAY", "↔", "BASE"),
    ("Data Exchange Rail", "SYNC", "↔", "BASE"),
    ("Registry Layer", "LIST", "↔", "BASE"),
    ("Authentication Rail", "AUTH", "↔", "BASE"),
    ("Platform Layer", "PLAT", "↔", "BASE"),
    ("E-Gov vs D-Gov", "EGOV", "≠", "DGOV"),
    ("Gov Transformation", "OLD", "→", "NEW"),
    ("Institutional Cap", "CAP", "↔", "TECH"),
    ("Public Trust Model", "TRST", "↔", "GOV"),
    ("DPI Identity Link", "ID", "→", "DPI"),
    ("DPI Payment Link", "PAY", "→", "DPI"),
    ("DPI Data Link", "DATA", "→", "DPI"),
    ("Ministry Sync", "MIN1", "↔", "MIN2"),
    ("Cross-Dept Flow", "DEPT", "↔", "DEPT"),
    ("Interoperability", "SYNC", "↔", "MANY"),
    ("Unified Portal", "ONE", "→", "ALL"),
    ("Service API", "API", "↔", "BACK"),
    ("Back-end System", "DB", "↔", "API"),
    ("Mobile Government", "MOB", "↔", "GOV"),
    ("Omnichannel Access", "MANY", "↔", "USER"),
    ("Citizen-Centered", "USER", "↔", "CORE"),
    ("Life-Event Model", "LIFE", "→", "SERV"),
    ("Birth Registration", "BABY", "→", "ID"),
    ("Business Formation", "CORP", "→", "REG"),
    ("Digital Taxation", "TAX", "↔", "PAY"),
    ("Tax Compliance", "RULE", "↔", "TAX"),
    ("Digital Customs", "TRAD", "↔", "GOV"),
    ("Digital Procurement", "BUY", "↔", "GOV"),
    ("Open Contracting", "OPEN", "↔", "BUY"),
    ("Digital Budgeting", "CASH", "↔", "PLAN"),
    ("Budget Transparency", "OPEN", "↔", "CASH"),
    ("Digital Welfare", "HELP", "↔", "USER"),
    ("Welfare Targeting", "DATA", "→", "HELP"),
    ("Health Governance", "MED", "↔", "GOV"),
    ("Education Gov", "GRAD", "↔", "GOV"),
    ("Agri Governance", "FARM", "↔", "GOV"),
    ("Land Governance", "LAND", "↔", "GOV"),
    ("Digital Justice", "LAW", "↔", "GOV"),
    ("Case Management", "CASE", "↔", "SYS"),
    ("Digital Policing", "SAFE", "↔", "GOV"),
    ("Cybersecurity Gov", "SEC", "↔", "RULE"),
    ("Zero Trust Gov", "ZERO", "↔", "SAFE"),
    ("Cloud Government", "CLOU", "↔", "GOV"),
    ("Data Sovereignty", "OWN", "↔", "DATA"),
    ("Gov Data Center", "STOR", "↔", "GOV"),
    ("Hybrid Cloud Gov", "HYB", "↔", "GOV"),
    ("PDA Leadership", "PDA", "→", "PLAN"),
    ("Digital Nation Act", "LAW", "↔", "2025"),
    ("Cabinet Digital", "CAB", "↔", "NET"),
    ("70% Digital Milestone", "70%", "↔", "DONE"),
    ("National Masterplan", "PLAN", "↔", "NATL"),
    ("Sectoral Framework", "SECT", "↔", "PLAN"),
    ("DPI Scalability", "GROW", "↔", "DPI"),
    ("Governance Metrics", "MEAS", "↔", "GOV"),
    ("Accountability", "CHK", "↔", "GOV"),
    ("Privacy Safeguard", "PRIV", "↔", "GOV"),
    ("Inclusion Strategy", "ALL", "↔", "GOV"),
    ("Orakzai Inclusion", "ORAK", "↔", "GOV"),
    ("Remote Access", "DIST", "↔", "GOV"),
    ("Mobile-First Gov", "MOB", "↔", "CORE"),
    ("Legacy Migration", "OLD", "→", "NEW"),
    ("System Resilience", "STAY", "↔", "SAFE"),
    ("Policy Driven Gov", "RULE", "→", "GOV"),
    ("Data Driven Gov", "DATA", "→", "GOV"),
    ("Algorithmic Gov", "AI", "→", "GOV"),
    ("Smart City Gov", "CITY", "↔", "GOV"),
    ("Village Digital", "VILL", "↔", "GOV"),
    ("Regional Autonomy", "REGN", "↔", "GOV"),
    ("Federal Alignment", "FED", "↔", "REGN"),
    ("Standardized API", "STD", "↔", "API"),
    ("Secure Gateway", "GATE", "↔", "SAFE"),
    ("Citizen Feedback", "TALK", "↔", "GOV"),
    ("Public Audit Flow", "AUDT", "↔", "GOV"),
    ("Digital Archiving", "ARCH", "↔", "GOV"),
    ("Knowledge Mgmt", "KNOW", "↔", "GOV"),
    ("HR Governance", "HR", "↔", "GOV"),
    ("Resource Alloc", "RES", "↔", "GOV"),
    ("Crisis Management", "HELP", "↔", "FAST"),
    ("Disaster Gov", "SAFE", "↔", "FAST"),
    ("Environmental Gov", "ECO", "↔", "GOV"),
    ("Energy Governance", "POWR", "↔", "GOV"),
    ("Transport Gov", "MOVE", "↔", "GOV"),
    ("Telecom Gov", "NET", "↔", "GOV"),
    ("Postal Digital", "MAIL", "↔", "GOV"),
    ("Statistics Gov", "STAT", "↔", "GOV"),
    ("Census Digital", "CENS", "↔", "GOV"),
    ("Electoral Gov", "VOTE", "↔", "GOV"),
    ("Legislative Gov", "LAW", "↔", "GOV"),
    ("Executive Gov", "EXEC", "↔", "GOV"),
    ("Judicial Gov", "JUDI", "↔", "GOV"),
    ("Local Gov Digital", "LOCL", "↔", "GOV"),
    ("Provincial Gov", "PROV", "↔", "GOV"),
    ("Federal Gov", "FED", "↔", "GOV"),
    ("Global Governance", "GLOB", "↔", "GOV"),
    ("Future Gov Model", "TIME", "↔", "NEXT"),
    ("Identity Wallet", "WAL", "↔", "GOV"),
    ("Credential Verify", "CHK", "↔", "CERT"),
    ("License Portal", "LIC", "↔", "GOV"),
    ("Permit Workflow", "DO", "↔", "GOV"),
    ("Grant Management", "GIVE", "↔", "GOV"),
    ("Subsidy Flow", "SUB", "↔", "USER"),
    ("Pension Digital", "OLD", "↔", "PAY"),
    ("Emergency Alert", "WARN", "↔", "ALL"),
    ("Public Safety Net", "SAFE", "↔", "NET"),
    ("Digital Sovereignty", "OWN", "↔", "NATL"),
    ("Sovereign Compute", "COMP", "↔", "NATL"),
    ("Sovereign Data", "DATA", "↔", "NATL"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g146-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g146-{index}-title g146-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g146-{index}-title">{safe}</title><desc id="g146-{index}-desc">A digital governance relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g146-{index}-caption" class="diagram-caption">{index}. {safe} — Digital governance relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Digital Governance Framework</title><desc id="hero-desc">A diagram showing the integrated stack of digital governance, from citizens to public institutions.</desc><defs><linearGradient id="h146-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h146-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">DIGITAL GOVERNANCE STACK</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">CITIZENS & USERS</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL SERVICES (Omnichannel)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">GOVERNMENT PLATFORMS (Portals/APIs)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DPI RAILS (ID / Pay / Data)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DATA & CLOUD INFRASTRUCTURE</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">PUBLIC INSTITUTIONS (PDA / Ministries)</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">LEGAL & REGULATORY FRAMEWORK</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">DIGITAL GOVERNANCE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Governing the Digital State for the Common Good.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Digital Governance Framework: The integrated stack of citizens, services, platforms, infrastructure, and institutions.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 146</title>
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
            <p class="section-label">PAGE 146</p>
            <h2>DIGITAL GOVERNANCE</h2>
            <p>“Governing the Digital State.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Digital technology has changed how governments operate, how public services are delivered, and how citizens interact with institutions. Digital governance is broader than simply putting government forms online; it concerns how institutions use technology to deliver services, manage information, make decisions, establish accountability, and interact with citizens. A mature digital-government system should therefore combine technology with law, institutional capacity, transparency, privacy, security, and public trust.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Digital Nation Act & The PDA</h3>
                <p>As of 2026, Pakistan's digital transformation is guided by the **Digital Nation Pakistan Act 2025**, enacted in January 2025. This landmark legislation established the **Pakistan Digital Authority (PDA)** as the single body with the legal power to lead, plan, and govern the country's digital journey. The PDA's mandate is to enable an inclusive digital society, a vibrant digital economy, and a modern digital governance framework. By June 2026, over 70% of cabinet operations were digitalized, demonstrating a clear commitment to institutional modernization.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Public Infrastructure (DPI)</h3>
                <p>Digital Public Infrastructure (DPI) refers to foundational digital systems—specifically **Digital Identity (NADRA)**, **Payment Infrastructure (Raast)**, and **Data Exchange**—that enable people and organizations to participate in digital services. Pakistan has built a layered stack of DPI solutions, drawing inspiration from global best practices. This stack acts as the "rails" for modern governance, allowing ministries to synchronize data while maintaining appropriate legal and privacy controls. The objective is a seamless, citizen-centered experience across all public services.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Citizen-Centered & Life-Event Services</h3>
                <p>Modern digital governance shifts from department-centered silos to **Citizen-Centered services**. Instead of navigating five different departments to register a business, citizens use a unified portal designed around their needs. The **Life-Event approach** organizes services around major events such as birth, education, employment, and retirement. For the Orakzai community, this means that even in remote valleys, a citizen can register a birth or apply for a license through a mobile device, bridging the geographic gap with the digital state.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Security, Sovereignty & The Future</h3>
                <p>As the state becomes digital, **Cybersecurity Governance** becomes a national priority. Critical systems like identity and payments are protected by zero-trust principles and secure government data centers. The **National Digital Masterplan**, launched in mid-2026, guides the transition from legacy systems to a sovereign, resilient, and inclusive digital future. Digital governance is not just about efficiency; it is about building a state that is accountable, transparent, and responsive to the needs of every citizen.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Digital Governance</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Governance is a trust. In the digital age, that trust is mediated by technology. The objective of digital governance is to create a state that is as dynamic as the people it serves. From the unified portals of Islamabad to the digital registries of Orakzai, we are designing a foundation where the state is not a distant institution, but a responsive partner in the citizen's journey.”</p>
            </div>

            <div class="final-statement">
                GOVERNANCE IS DIGITAL.<br>
                TRUST IS SOVEREIGN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Pakistan Digital Authority (PDA), <em>The Digital Nation Pakistan Act 2025: Legal Framework for Transformation (2026)</em>.</li>
                    <li>Business Recorder, <em>Reshaping Pakistan's Digital Governance: 70% of Cabinet Operations Digitalized (June 2026)</em>.</li>
                    <li>World Bank, <em>Digital Public Infrastructure (DPI) and the Transformation of Public Services (May 2026)</em>.</li>
                    <li>Pakistan Digital Authority (PDA), <em>National Digital Masterplan & Sectoral Frameworks (August 2026)</em>.</li>
                    <li>GlobalDev Blog, <em>Digital Public Infrastructure and Taxes: Pakistan's High-Stakes Experiment (2025)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            146
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

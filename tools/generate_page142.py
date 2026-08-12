from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-142-sovereign-technology.html'

GRAPHICS = [
    ("Sovereign Tech", "CTRL", "↔", "SOV"),
    ("Digital vs Sovereign", "DATA", "→", "TECH"),
    ("Strategic Resilience", "FAIL", "→", "ABLE"),
    ("Open but Capable", "OPEN", "↔", "ABLE"),
    ("The Tech Stack", "BASE", "→", "APPL"),
    ("Energy Layer", "POWR", "↔", "BASE"),
    ("Semiconductor Layer", "CHIP", "↔", "BASE"),
    ("Hardware Layer", "HARD", "↔", "BASE"),
    ("Network Layer", "NETW", "↔", "BASE"),
    ("AI Computing Layer", "AI", "↔", "BASE"),
    ("Software Layer", "CODE", "↔", "BASE"),
    ("Application Layer", "APP", "↔", "BASE"),
    ("Software Sov", "CODE", "↔", "SOV"),
    ("OS Sovereignty", "OS", "↔", "CTRL"),
    ("Enterprise Sov", "ENTR", "↔", "CTRL"),
    ("Cloud Platform Sov", "CLD", "↔", "CTRL"),
    ("Cybersecurity Sov", "SAFE", "↔", "CTRL"),
    ("AI Application Sov", "AI", "↔", "CTRL"),
    ("Developer Tool Sov", "TOOL", "↔", "CTRL"),
    ("Open Source Infra", "OPEN", "↔", "STRT"),
    ("Cloud Tech Sov", "CLD", "↔", "SOV"),
    ("Local Data Center", "LOCL", "↔", "DATA"),
    ("Virtualization Sov", "VIRT", "↔", "CTRL"),
    ("Storage Sov", "STOR", "↔", "CTRL"),
    ("Disaster Recovery", "BACK", "→", "UP"),
    ("Data Center Cap", "DC", "↔", "SOV"),
    ("Reliable Power", "POWR", "↔", "DC"),
    ("DC Cooling", "COOL", "↔", "DC"),
    ("DC Security", "SAFE", "↔", "DC"),
    ("DC Connectivity", "NET", "↔", "DC"),
    ("Computing Power", "CPU", "↔", "STRT"),
    ("AI Compute", "GPU", "↔", "AI"),
    ("Scientific Compute", "SCI", "↔", "HPC"),
    ("Financial Compute", "FIN", "↔", "HPC"),
    ("Weather Compute", "WTHR", "↔", "HPC"),
    ("Engineering Compute", "ENG", "↔", "HPC"),
    ("Cybersecurity Comp", "SAFE", "↔", "HPC"),
    ("AI Sovereignty", "AI", "↔", "SOV"),
    ("AI Data Loop", "DATA", "→", "MODL"),
    ("AI Research", "FIND", "↔", "KNOW"),
    ("AI Engineering", "ENG", "→", "SYS"),
    ("AI Governance", "RULE", "↔", "AI"),
    ("Local AI App", "LOCL", "↔", "AI"),
    ("Education AI", "EDU", "↔", "AI"),
    ("Healthcare AI", "HLTH", "↔", "AI"),
    ("Agriculture AI", "AGRI", "↔", "AI"),
    ("Finance AI", "FIN", "↔", "AI"),
    ("Public Admin AI", "GOVT", "↔", "AI"),
    ("Language Tech AI", "LANG", "↔", "AI"),
    ("Urdu AI", "URDU", "↔", "AI"),
    ("Pashto AI", "PSHT", "↔", "AI"),
    ("Punjabi AI", "PUNJ", "↔", "AI"),
    ("Sindhi AI", "SIND", "↔", "AI"),
    ("Balochi AI", "BALO", "↔", "AI"),
    ("AI GPU Strategy", "GPU", "↔", "PLAN"),
    ("AI Energy Strategy", "POWR", "↔", "PLAN"),
    ("AI Talent Stack", "HUMN", "→", "AI"),
    ("ML Engineer", "CODE", "↔", "AI"),
    ("Data Scientist", "DATA", "↔", "AI"),
    ("AI Researcher", "FIND", "↔", "AI"),
    ("AI Mathematician", "MATH", "↔", "AI"),
    ("Semiconductor Sov", "CHIP", "↔", "SOV"),
    ("Chip Design Sov", "IDEA", "→", "CHIP"),
    ("Chip Verification", "CHK", "↔", "CHIP"),
    ("Embedded Processor", "EMBD", "↔", "CHIP"),
    ("Chip Accelerator", "ACCL", "↔", "CHIP"),
    ("Advanced Mfg", "MFG", "↔", "SOV"),
    ("Electronics Assy", "ASSY", "↔", "MFG"),
    ("Precision Eng", "PREC", "↔", "MFG"),
    ("Industrial Auto", "AUTO", "↔", "MFG"),
    ("Advanced Materials", "MATR", "↔", "MFG"),
    ("Robotics Stack", "AI", "MECH", "SYS"),
    ("Robotics Mfg", "MFG", "↔", "ROB"),
    ("Robotics Agri", "AGRI", "↔", "ROB"),
    ("Robotics Logistics", "LOGI", "↔", "ROB"),
    ("Robotics Health", "HLTH", "↔", "ROB"),
    ("Robotics Disaster", "SOS", "↔", "ROB"),
    ("Telecom Resilience", "NET", "↔", "SOV"),
    ("Fiber Optic Sov", "FIBR", "↔", "SOV"),
    ("Mobile Network Sov", "MOB", "↔", "SOV"),
    ("Satellite Network", "SAT", "↔", "SOV"),
    ("Network Equip Sov", "HARD", "↔", "SOV"),
    ("5G Future Net", "5G", "↔", "FAST"),
    ("Autonomous Net", "AUTO", "↔", "NET"),
    ("Industrial IoT", "IOT", "↔", "NET"),
    ("Smart Infra Net", "SMART", "↔", "NET"),
    ("Remote Health Net", "HLTH", "↔", "NET"),
    ("Intelligent Trans", "TRAN", "↔", "NET"),
    ("Cybersecurity Sov", "SAFE", "↔", "SOV"),
    ("Malware Protection", "VIRU", "≠", "SAFE"),
    ("Ransomware Prot", "LOCK", "≠", "SAFE"),
    ("Supply Chain Prot", "SUPP", "↔", "SAFE"),
    ("Infrastructure Prot", "CRIT", "↔", "SAFE"),
    ("Security Process", "PREV", "DET", "RESP"),
    ("Cryptography Sov", "MATH", "↔", "SOV"),
    ("Encryption Sov", "HIDE", "↔", "SOV"),
    ("Digital Signature", "SIGN", "↔", "SOV"),
    ("Key Management", "KEYS", "↔", "SOV"),
    ("Post-Quantum Crypt", "PQ", "↔", "SAFE"),
    ("Quantum Computing", "QUAN", "↔", "SOV"),
    ("Quantum Research", "FIND", "↔", "QUAN"),
    ("Quantum Algorithm", "ALGO", "↔", "QUAN"),
    ("Quantum Crypt Plan", "PLAN", "↔", "QUAN"),
    ("Blockchain Sov", "BC", "↔", "SOV"),
    ("Consensus System", "AGRE", "↔", "BC"),
    ("Smart Contract Sov", "CODE", "↔", "BC"),
    ("Digital Asset Sov", "ASST", "↔", "BC"),
    ("Decentralized ID", "ID", "↔", "BC"),
    ("Sovereign BC Infra", "GOVT", "↔", "BC"),
    ("OSG Concept", "OSG", "↔", "PLAN"),
    ("OSG User Loop", "USER", "→", "OSG"),
    ("OSG Wallet Loop", "WAL", "→", "OSG"),
    ("OSG RPC Loop", "API", "→", "OSG"),
    ("OSG Node Loop", "NODE", "→", "OSG"),
    ("OSG Validator Loop", "VAL", "→", "OSG"),
    ("OSG Consensus Loop", "AGRE", "→", "OSG"),
    ("Faisal Orakzai profile", "SYS", "↔", "SOV"),
    ("Sovereign-by-Design", "PLAN", "→", "SOV"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g142-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g142-{index}-title g142-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g142-{index}-title">{safe}</title><desc id="g142-{index}-desc">A sovereign technology relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g142-{index}-caption" class="diagram-caption">{index}. {safe} — Sovereign technology relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Sovereign Technology Stack</title><desc id="hero-desc">A diagram showing the layered architecture of sovereign technology, from energy and semiconductors to AI and applications.</desc><defs><linearGradient id="h142-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h142-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">SOVEREIGN TECHNOLOGY STACK</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">APPLICATIONS</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">SOFTWARE</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AI / COMPUTING</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">NETWORKS</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">HARDWARE</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">SEMICONDUCTORS</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">ENERGY</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">SOVEREIGN TECHNOLOGY</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Building the Technologies That Define the Future.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Sovereign Technology: The integrated framework for developing, operating, and governing critical technologies according to strategic priorities.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 142</title>
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
        .case-study-card {{ border: 1px solid var(--gold); padding: 30px; margin: 50px 0; background: rgba(181,150,84,0.05); }}
        .final-statement {{ text-align: center; font-size: 1.8rem; font-weight: 700; color: var(--gold); margin: 60px 0; }}
        @media (max-width: 768px) {{ .atlas-grid {{ grid-template-columns: 1fr; }} }}
        svg {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="content-page">
        <header class="page-header">
            <p class="section-label">PAGE 142</p>
            <h2>SOVEREIGN TECHNOLOGY</h2>
            <p>“Building the Technologies That Define the Future.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Sovereign technology is the capability of a country, institution, or community to develop, operate, and govern critical technologies according to its own strategic priorities. It extends beyond digital sovereignty to the technologies themselves—AI, semiconductors, robotics, and advanced software. For Pakistan, sovereign technology is about developing enough knowledge, talent, and infrastructure to make strategic technological choices independently, ensuring resilience in a complex global ecosystem.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Sovereign Technology Stack</h3>
                <p>Sovereign capability is a layered system. Weakness at any critical layer—from <strong>Energy</strong> and <strong>Semiconductors</strong> to <strong>Hardware</strong> and <strong>Networks</strong>—creates dependencies elsewhere. As of 2026, Pakistan is addressing these layers through initiatives like the <strong>National Semiconductor Plan</strong>, a Rs 4.5 billion program focusing on chip design clusters. The objective is strategic resilience: maintaining domestic expertise and infrastructure while collaborating within the global technology market.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI Sovereignty & Computing Capacity</h3>
                <p>Artificial Intelligence is a strategic frontier. Sovereign AI capability involves more than models; it requires integrated <strong>Data</strong>, <strong>Computing</strong>, and <strong>Research</strong>. In March 2026, Pakistan launched its first <strong>Sovereign AI Cloud</strong> infrastructure, supported by a $1 billion national investment. This initiative aims to develop AI applications tailored to local needs—including language technologies for Urdu and Pashto—ensuring that the development of AI remains aligned with national interests and cultural values.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Connectivity & Cybersecurity</h3>
                <p>Modern sovereignty requires resilient <strong>Telecommunications</strong> and <strong>Cybersecurity</strong>. Fiber optics, mobile networks, and satellite connectivity provide the physical foundation for the digital economy. Technology sovereignty without cybersecurity is incomplete; critical systems must be protected through a continuous process of prevention, detection, and response. By fostering domestic <strong>Robotics</strong> and advanced manufacturing, nations can build resilient ecosystems that support agriculture, healthcare, and disaster response.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists advocating for "Sovereign-by-Design." His work explores building end-to-end technology stacks that reduce external dependencies and prioritize domestic capability. He serves as one example of the "Young Pakistani Builder" who bridges the gap between global standards and local requirements. His vision includes the <strong>Orakzai Sovereign Grid (OSG)</strong>—a proposed regional blockchain infrastructure concept—illustrating how decentralized technologies can empower local communities and ensure that their digital future remains secure and sovereign.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Sovereign Technology</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Future is Open & Capable</h3>
                <p>Sovereign technology does not require technological isolation. The strongest model is generally <strong>Open but Capable</strong>—participating in international trade and research while maintaining strategic independence. By developing <strong>Quantum Readiness</strong> and post-quantum cryptographic transition plans, nations can prepare for longer-term technological frontiers. From the urban design centers of Pakistan to the valleys of Orakzai, we are building the technologies that will define our future, ensuring that the machine-readable world remains a human-centered one.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Technology is the language of the future. To be sovereign, we must not only speak this language but contribute to its grammar. The objective of sovereign technology is to ensure that our tools reflect our values and our strategic priorities. From the national semiconductor labs of Pakistan to the proposed sovereign grids of Orakzai, we are designing a future where technology is a partner in our progress, and the capability remains ours.”</p>
            </div>

            <div class="final-statement">
                THE STACK IS GLOBAL.<br>
                THE CAPABILITY IS SOVEREIGN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Ministry of IT & Telecom (MoITT), <em>Launch of Pakistan's First Sovereign AI Cloud Infrastructure (2026)</em>.</li>
                    <li>Government of Pakistan, <em>National Semiconductor Plan & Chip Design Cluster Initiatives (2026)</em>.</li>
                    <li>TechPolicy.Press, <em>The High Stakes of Pakistan's Push for AI Sovereignty ($1B Investment)</em>.</li>
                    <li>ResearchGate, <em>Latest Trends in Chip Technology in Pakistan: Emerging Opportunities and National Priorities (2026)</em>.</li>
                    <li>Ignite National Technology Fund, <em>NAIIH Sovereign AI Consultation Framework (2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            142
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

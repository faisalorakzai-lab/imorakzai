from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-141-digital-sovereignty.html'

GRAPHICS = [
    ("Digital Sovereignty", "CTRL", "↔", "SOV"),
    ("Sovereignty vs Isolation", "SOV", "≠", "ISOL"),
    ("Traditional vs Digital", "LAND", "→", "DATA"),
    ("New Dimensions", "AI", "↔", "FIN"),
    ("Strategic Resilience", "FAIL", "→", "RECV"),
    ("Data Sovereignty", "DATA", "↔", "LAW"),
    ("Data as Resource", "DATA", "→", "VALU"),
    ("Cloud Sovereignty", "CLD", "↔", "CTRL"),
    ("Sovereign Cloud", "LOCL", "↔", "DATA"),
    ("Computing Capacity", "CPU", "↔", "SOV"),
    ("AI Sovereignty", "AI", "↔", "CTRL"),
    ("National AI Stack", "DATA", "→", "APP"),
    ("Semiconductor Sov", "CHIP", "↔", "SOV"),
    ("Hardware Capability", "HARD", "↔", "SOV"),
    ("Telecommunications", "NET", "↔", "PHYS"),
    ("IXP Resilience", "IXP", "↔", "LOCL"),
    ("Undersea Cables", "SEA", "→", "NET"),
    ("Satellite Link", "SAT", "↔", "REMT"),
    ("Digital Identity", "ID", "↔", "SOV"),
    ("DPI Framework", "ID", "PAY", "DATA"),
    ("Cybersecurity Sov", "SAFE", "↔", "SOV"),
    ("Security Talent", "TALN", "↔", "SAFE"),
    ("Open Source Sov", "OPEN", "↔", "FREE"),
    ("Software Sovereignty", "CODE", "↔", "CTRL"),
    ("Blockchain Sov", "BC", "↔", "DECN"),
    ("National BC Infra", "GOVT", "↔", "BC"),
    ("Financial Sovereignty", "FIN", "↔", "CTRL"),
    ("Digital Currency", "CASH", "↔", "DIGI"),
    ("Remittance Infra", "REMT", "↔", "FAST"),
    ("E-Commerce Sov", "BUY", "↔", "LOCL"),
    ("Digital Entreprene", "BLD", "→", "SOV"),
    ("Faisal Orakzai profile", "SYS", "↔", "SOV"),
    ("Sovereignty-by-Design", "PLAN", "→", "SOV"),
    ("Local Data Control", "LOCL", "↔", "DATA"),
    ("Jurisdiction Loop", "LAW", "↔", "DATA"),
    ("Cross-Border Data", "OUT", "↔", "IN"),
    ("Sensitive Data", "PRIV", "↔", "SAFE"),
    ("Responsible Collect", "GET", "↔", "RULE"),
    ("Alternative Cloud", "ALT", "↔", "MAIN"),
    ("Contingency Plan", "FAIL", "→", "ALT"),
    ("GPU Acceleration", "GPU", "↔", "AI"),
    ("Edge Computing", "EDGE", "↔", "SOV"),
    ("High Performance", "HPC", "↔", "SCI"),
    ("Strategic Independence", "FREE", "↔", "SOV"),
    ("AI Dataset Loop", "DATA", "→", "MODL"),
    ("Model Training", "TRAI", "→", "AI"),
    ("AI Evaluation", "TEST", "↔", "SAFE"),
    ("AI Governance", "RULE", "↔", "AI"),
    ("Chip Design Stack", "IDEA", "→", "CHIP"),
    ("Packaging/Testing", "PKG", "↔", "TEST"),
    ("Strategic Hardware", "HARD", "↔", "SEC"),
    ("Fiber-Optic Net", "FIBR", "↔", "FAST"),
    ("Mobile Networks", "MOB", "↔", "ALL"),
    ("Satellite Backup", "SAT", "→", "EMRG"),
    ("Emergency Comm", "SOS", "↔", "NET"),
    ("Identity Support", "ID", "→", "BANK"),
    ("Government DPI", "GOVT", "↔", "DPI"),
    ("Payment DPI", "PAY", "↔", "DPI"),
    ("Data Exchange DPI", "EXCH", "↔", "DPI"),
    ("Credential DPI", "CERT", "↔", "DPI"),
    ("Public Service DPI", "SERV", "↔", "DPI"),
    ("Attack Detection", "DET", "↔", "HACK"),
    ("Incident Invest", "CHK", "↔", "EVNT"),
    ("Breach Response", "ACT", "↔", "SAFE"),
    ("System Recovery", "BACK", "→", "UP"),
    ("Security Research", "FIND", "↔", "SAFE"),
    ("Cryptographer", "MATH", "↔", "SEC"),
    ("Software Audit", "CODE", "↔", "CHK"),
    ("Vendor Lock-In", "LOCK", "≠", "SOV"),
    ("Critical Systems", "CRIT", "↔", "SAFE"),
    ("Banking Sov", "BANK", "↔", "SOV"),
    ("Healthcare Sov", "HLTH", "↔", "SOV"),
    ("National ID Stack", "ID", "↔", "PAK"),
    ("Sovereign Grid Arch", "SOV", "↔", "GRID"),
    ("Orakzai Heritage", "PAST", "→", "DIGI"),
    ("Local Jurisdiction", "LOCL", "↔", "LAW"),
    ("Strategic Resource", "DATA", "↔", "VALU"),
    ("Inclusive Market", "ALL", "↔", "VALU"),
    ("Diaspora Capital", "ABRD", "→", "HOME"),
    ("Verifiable Rights", "TRUE", "↔", "RGHT"),
    ("Ownership-by-Design", "OWN", "↔", "PLAN"),
    ("Resilient Systems", "SAFE", "↔", "TIME"),
    ("Distributed State", "MANY", "↔", "ONE"),
    ("Jurisdiction Gap", "LAW", "≠", "DATA"),
    ("Digital Border", "BORD", "↔", "DIGI"),
    ("Strategic Capability", "ABLE", "↔", "SOV"),
    ("National Interest", "PAK", "↔", "SAFE"),
    ("Policy Framework", "PLAN", "→", "RULE"),
    ("Institutional Cap", "INST", "↔", "SOV"),
    ("Strategic Resource", "DATA", "↔", "VALU"),
    ("Economic Security", "ECON", "↔", "SEC"),
    ("National Defense", "DEF", "↔", "SOV"),
    ("Public Admin", "GOVT", "↔", "DATA"),
    ("Research Loop", "FIND", "→", "KNOW"),
    ("Engineering Stack", "ENG", "→", "SYS"),
    ("Application Layer", "APP", "↔", "USER"),
    ("Governance Loop", "RULE", "↔", "ALL"),
    ("Semiconductor Plan", "CHIP", "↔", "PAK"),
    ("Chip Talent", "TALN", "↔", "CHIP"),
    ("Design Partnership", "COOP", "↔", "CHIP"),
    ("Physical Foundation", "PHYS", "↔", "NET"),
    ("Peering Resilience", "PEER", "↔", "NET"),
    ("Latency Loop", "REQ", "↔", "RES"),
    ("Local Traffic", "LOCL", "↔", "NET"),
    ("Submarine Cables", "SEA", "↔", "GLOB"),
    ("Terrestrial Net", "LAND", "↔", "NET"),
    ("Emergency Link", "SOS", "↔", "SAT"),
    ("Remote Access", "REMT", "↔", "NET"),
    ("Authentication", "USER", "↔", "ID"),
    ("Taxation Support", "TAX", "↔", "ID"),
    ("Shared Foundation", "BASE", "↔", "ALL"),
    ("Incident Response", "ACT", "↔", "SAFE"),
    ("Software Mod", "CODE", "↔", "EDIT"),
    ("Expertise Loop", "LEAR", "→", "ABLE"),
    ("Digital Future", "IDEA", "↔", "REAL"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g141-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g141-{index}-title g141-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g141-{index}-title">{safe}</title><desc id="g141-{index}-desc">A digital sovereignty relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g141-{index}-caption" class="diagram-caption">{index}. {safe} — Digital sovereignty relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Digital Sovereignty Framework</title><desc id="hero-desc">A diagram showing the multi-dimensional framework for national digital sovereignty, from data and computing to AI and cybersecurity.</desc><defs><linearGradient id="h141-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h141-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">DIGITAL SOVEREIGNTY STACK</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">DATA</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="65" font-size="12">NETWORKS</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">COMPUTING</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">SOFTWARE</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AI</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="65" font-size="12">CYBERSECURITY</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">DIGITAL</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">SERVICES</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">DIGITAL SOVEREIGNTY</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Controlling the Digital Foundations of the Modern State.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Digital Sovereignty: The integrated framework for maintaining control over infrastructure, data, technology, and strategic capabilities in a digital world.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 141</title>
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
            <p class="section-label">PAGE 141</p>
            <h2>DIGITAL SOVEREIGNTY</h2>
            <p>“Controlling the Digital Foundations of the Modern State.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Digital sovereignty is the ability of a country, institution, or community to maintain meaningful control over its digital infrastructure, data, and strategic capabilities. In the modern world, sovereignty is no longer limited to territory and physical resources; it increasingly includes data, networks, computing, and artificial intelligence. For countries like Pakistan, digital sovereignty is becoming a cornerstone of long-term economic and national security.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The New Dimensions of Sovereignty</h3>
                <p>Modern economies depend on digital foundations. Digital sovereignty adds layers of <strong>Data</strong>, <strong>Networks</strong>, <strong>Computing</strong>, and <strong>AI</strong> to traditional concepts of territory and borders. As of 2026, Pakistan has launched the <strong>National Data Governance Policy</strong> to establish a framework for managing government data. The objective is strategic capability—ensuring that critical digital systems are resilient and independent while remaining connected to global technology markets and open-source communities.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Data, Cloud & Computing Capacity</h3>
                <p>Data sovereignty concerns the control and legal jurisdiction surrounding data. Countries are transitioning from foreign cloud reliance to domestic <strong>Tier-III Data Centers</strong> to safeguard sensitive information. Access to computing capacity, including <strong>GPUs</strong> for AI training, is a critical requirement for AI sovereignty. The <strong>National AI Policy 2025</strong> emphasizes building local datasets and models, ensuring that the development and deployment of AI systems remain aligned with national interests and cultural values.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Hardware & Connectivity</h3>
                <p>Digital sovereignty is anchored in the physical foundation of <strong>Telecommunications</strong>. Fiber-optic networks, internet exchange points (IXPs), and undersea cables connect nations to the global web. Resilience in these systems is strategically vital. Pakistan's <strong>National Semiconductor Plan</strong> focuses on developing talent in chip design, recognizing that software sovereignty has limitations without hardware capability. Satellite connectivity complements terrestrial networks, providing vital links for remote regions like Orakzai.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists advocating for "Sovereignty-by-Design." His work explores building systems that prioritize local control over data, infrastructure, and strategic capabilities. He serves as one example of the "Young Pakistani Builder" who leverages technologies like blockchain and decentralized identity to empower local communities. His vision ensures that Orakzai's digital heritage and economic participation remain secure and sovereign, providing a model for how regional communities can participate in the global digital economy without losing their autonomy.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Digital Sovereignty</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Public Infrastructure (DPI)</h3>
                <p>A sovereign digital ecosystem is built on <strong>Digital Public Infrastructure (DPI)</strong>—the integration of identity, payments, and data exchange. <strong>Cybersecurity Sovereignty</strong> is perhaps the most critical dimension, requiring the capability to detect and respond to incidents independently. By fostering domestic <strong>Digital Entrepreneurship</strong> and cybersecurity talent, nations can build resilient systems that empower individual, institutional, and national sovereignty in a machine-readable economy.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Sovereignty in the digital age is not about isolation; it is about capability. To build a secure digital world, we must bridge the gap between global connectivity and local control. The objective of digital sovereignty is to ensure that our digital future remains in our own hands. From the national data centers of Pakistan to the valleys of Orakzai, we are designing the foundations of a modern state where technology serves the people, and the data remains ours.”</p>
            </div>

            <div class="final-statement">
                THE FOUNDATION IS DIGITAL.<br>
                THE SOVEREIGNTY IS HUMAN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Pakistan Digital Authority (PDA), <em>National Data Governance Policy 2026</em>.</li>
                    <li>Ignite National Technology Fund, <em>National Artificial Intelligence (AI) Policy 2025</em>.</li>
                    <li>Chambers & Partners, <em>Data Protection & Privacy 2026 — Pakistan Practice Guide</em>.</li>
                    <li>Government of Pakistan (MoITT), <em>National Semiconductor Plan & Chip Design Initiatives (2026)</em>.</li>
                    <li>Quantum Global Data Centre (QGDC), <em>Domestic Tier-III Infrastructure Development ($230M Project)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            141
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

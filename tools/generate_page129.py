from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-129-ai-governance.html'

GRAPHICS = [
    ("AI Governance Hero", "TECH", "↔", "RULE"),
    ("Governance Model", "DEV", "→", "AUDT"),
    ("AI Governance Def", "RULE", "↔", "ACC"),
    ("Governance Scope", "LAW", "+", "STD"),
    ("Risk Assessment", "IMPT", "→", "SAFE"),
    ("Governance Lifecycle", "DATA", "→", "RETR"),
    ("Risk-Based Model", "LOW", "↔", "HIGH"),
    ("Low Risk Governance", "LGHT", "↔", "RULE"),
    ("High Risk Oversight", "STRT", "↔", "GOV"),
    ("Unacceptable Risk", "PROH", "↔", "REST"),
    ("Data Governance AI", "SRC", "↔", "SAFE"),
    ("Data Quality Loop", "ACCU", "↔", "REPR"),
    ("Bias Detection AI", "DATA", "≠", "FAIR"),
    ("Fairness Metric", "EQL", "↔", "OUT"),
    ("Transparency AI", "OPEN", "↔", "BOX"),
    ("Explainability AI", "WHY", "↔", "MOD"),
    ("Accountability AI", "INST", "↔", "HUM"),
    ("Human Oversight Loop", "AI", "→", "HUM"),
    ("Human-in-the-Loop", "AI", "↔", "HUM"),
    ("Human-on-the-Loop", "AUTO", "↔", "MONI"),
    ("Human-out-of-the-Loop", "FULL", "↔", "AUTO"),
    ("AI Auditing System", "PERF", "↔", "COMP"),
    ("Model Validation", "TEST", "→", "VALD"),
    ("Red-Teaming AI", "ATTK", "→", "VULN"),
    ("AI Safety System", "SAFE", "↔", "BND"),
    ("AI Security Guard", "PROT", "↔", "MSUS"),
    ("Cybersecurity AI", "DEF", "↔", "ATTK"),
    ("Generative AI Gov", "GEN", "↔", "RULE"),
    ("Deepfake Detection", "REAL", "≠", "FAKE"),
    ("Misinformation AI", "RISK", "↔", "DEF"),
    ("AI and Democracy", "COMM", "↔", "SAFE"),
    ("AI and Elections", "DISC", "↔", "PROT"),
    ("AI and Human Rights", "TECH", "↔", "RGHT"),
    ("AI and Privacy", "DATA", "↔", "PRIV"),
    ("Biometric AI Gov", "ID", "↔", "CONS"),
    ("National AI Policy", "NAT", "↔", "STRT"),
    ("Islamabad AI Decl", "SOV", "↔", "RESP"),
    ("PDA Regulatory Body", "PDA", "↔", "RULE"),
    ("Data Governance 2026", "STD", "↔", "COMP"),
    ("Explainable Principle", "WHY", "→", "TRST"),
    ("Auditable Principle", "TEST", "→", "LOG"),
    ("Sovereign AI Infra", "NAT", "↔", "SEC"),
    ("Responsible AI Gov", "ETH", "↔", "TECH"),
    ("Data Collection Law", "LAW", "↔", "DATA"),
    ("Data Retention Rule", "TIME", "↔", "SAFE"),
    ("Data Minimization", "NEED", "↔", "DATA"),
    ("Access Rights AI", "USER", "↔", "DATA"),
    ("Model Training Gov", "DATA", "→", "ML"),
    ("Testing Benchmark", "ACCU", "↔", "FACT"),
    ("Deployment Guard", "TEST", "→", "LIVE"),
    ("Monitoring Cycle", "LIVE", "→", "FIX"),
    ("Retirement Protocol", "END", "→", "ARCH"),
    ("Bias Source Det", "HIST", "→", "BIAS"),
    ("Unfair Outcome Test", "OUT", "≠", "FAIR"),
    ("Disclosure Requirement", "AI", "→", "USER"),
    ("Documentation Std", "DOC", "↔", "MOD"),
    ("Explainability Challenge", "WHY", "≠", "HOW"),
    ("Accountability Chain", "AI", "→", "ORG"),
    ("Override Protocol", "HUM", "→", "OFF"),
    ("Conflict Handling", "DISA", "→", "RES"),
    ("Automated Prohib", "HIGH", "≠", "AUTO"),
    ("Audit Performance", "VAL", "↔", "GOAL"),
    ("Audit Fairness", "EQL", "↔", "DATA"),
    ("Audit Security", "PROT", "↔", "ATTK"),
    ("Adversarial Test", "RED", "→", "SAFE"),
    ("Unsafe Behavior Det", "BAD", "→", "STOP"),
    ("Manipulation Tech", "PROMPT", "→", "RISK"),
    ("Harmful Output Prev", "GEN", "≠", "HARM"),
    ("Dangerous Action Lim", "ACT", "≠", "RISK"),
    ("Data Poisoning Prot", "DATA", "↔", "CLEAN"),
    ("Model Theft Prot", "MOD", "↔", "LOCK"),
    ("Adversarial Input", "FAKE", "→", "MOD"),
    ("Dual-Use Governance", "GOOD", "↔", "BAD"),
    ("Generative Risk Map", "TEXT", "IMG", "VID"),
    ("Synthetic Media Gov", "GEN", "↔", "TRST"),
    ("Provenance Tracking", "ORIG", "→", "DATA"),
    ("Authentication Loop", "REAL", "↔", "VERI"),
    ("Misleading Content", "FAKE", "→", "NEWS"),
    ("Persuasion AI Gov", "PERS", "↔", "FREE"),
    ("Identity Information", "SENS", "↔", "PRIV"),
    ("Due Process AI", "LAW", "↔", "AUTO"),
    ("Non-Discrimination", "EQL", "↔", "ALL"),
    ("Lawful Collection 2", "RULE", "↔", "COLL"),
    ("Purpose Limitation", "GOAL", "↔", "DATA"),
    ("Data Minimization 2", "LESS", "↔", "MORE"),
    ("Security Fortress 2", "DATA", "↔", "WALL"),
    ("Retention Policy 2", "TIME", "↔", "DEL"),
    ("Access Rights 2", "USER", "↔", "VIEW"),
    ("Governance-by-Design", "PLAN", "↔", "TECH"),
    ("Algorithm Speed", "FAST", "↔", "ML"),
    ("Governance Direction", "DIR", "↔", "RULE"),
    ("Faisal Orakzai Gen 2", "SYS", "↔", "GOV"),
    ("Young Builder Gov", "LRN", "→", "BLD"),
    ("AI Literacy Gov", "DATA", "↔", "ETH"),
    ("Verification Loop 3", "AI", "→", "HUM"),
    ("AI Infra Gov", "GPU", "+", "SEC"),
    ("AI Talent Pipe 3", "UNI", "→", "GOV"),
    ("AI Export Gov", "VAL", "→", "GLB"),
    ("AI Product Life 3", "DEV", "→", "MKT"),
    ("AI Governance 3", "RULE", "↔", "SAFE"),
    ("Responsible AI Gov 2", "ETH", "↔", "TECH"),
    ("AI Trust 3", "VERI", "→", "TRST"),
    ("Human Oversight 3", "EYE", "→", "MOD"),
    ("AI Security 3", "DETE", "↔", "PROT"),
    ("AI Privacy 3", "SAFE", "↔", "RISK"),
    ("AI Data Lifecycle 3", "COLL", "→", "GOV"),
    ("AI Compute Life 3", "POW", "→", "OPS"),
    ("AI Cloud Arch 3", "SRV", "↔", "USER"),
    ("AI Research Eco 3", "UNI", "↔", "LAB"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g129-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g129-{index}-title g129-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g129-{index}-title">{safe}</title><desc id="g129-{index}-desc">An AI governance relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g129-{index}-caption" class="diagram-caption">{index}. {safe} — governance relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">AI Governance Framework</title><desc id="hero-desc">A diagram showing the integrated framework for AI governance, safety, and accountability.</desc><defs><linearGradient id="h129-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h129-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">TRUSTED AI GOVERNANCE ECOSYSTEM</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">REGULATION</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="65" font-size="12">AUDITABILITY</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">ETHICS</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">EXPLAINABILITY</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">SAFETY</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="65" font-size="12">ACCOUNTABILITY</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">SOVEREIGN</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">TRUST</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">AI GOVERNANCE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Governing Artificial Intelligence in the Age of Intelligent Systems.”</text></svg><figcaption id="hero-caption" class="diagram-caption">AI Governance: The integrated framework for regulation, ethics, safety, and human accountability.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 129</title>
    <link rel="stylesheet" href="../styles/main.css">
    <style>
        :root {{ --gold: #B59654; --purple: #8B2E8B; --teal: #2E8B8B; --cream: #F5F0E6; --muted: rgba(245,240,230,.72); }}
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
            <p class="section-label">PAGE 129</p>
            <h2>AI GOVERNANCE</h2>
            <p>“Governing Artificial Intelligence in the Age of Intelligent Systems.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Artificial intelligence is no longer only a research topic. It is becoming part of software, finance, healthcare, agriculture, education, government, cybersecurity, commerce and everyday digital life. As AI becomes more capable, another question becomes increasingly important: ‘Who governs the systems that govern our decisions?’ AI governance is the framework through which societies determine how artificial intelligence should be developed, deployed, monitored and held accountable. It is not simply about restricting technology. It is about creating conditions in which useful AI can develop while reducing unacceptable risks.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Risk-Based Framework & Accountability</h3>
                <p>AI governance operates on a risk-proportionate oversight model, categorizing applications from low to unacceptable risk. The core principle is human accountability: responsibility for AI outcomes must remain with human institutions and individuals. Governance frameworks define when humans must review outputs (Human-in-the-Loop), monitor automated operations (Human-on-the-Loop), or when fully automated decisions are prohibited due to high stakes. Transparency and explainability ensure that AI-assisted decisions can be understood and challenged.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Institutional Anchor: Islamabad AI Declaration 2026</h3>
                <p>Pakistan has established a sovereign and responsible AI ecosystem through the <strong>Islamabad AI Declaration (February 9, 2026)</strong>. This landmark adoption outlines 9 foundational principles, emphasizing explainable, auditable, and risk-proportionate systems. The <strong>Pakistan Digital Authority (PDA)</strong>, established under the <strong>Digital Nation Pakistan Act 2025</strong>, serves as the central regulatory body responsible for setting standards, monitoring compliance, and supervising the <strong>National Data Governance Policy 2026</strong>.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI Safety, Security & Human Rights</h3>
                <p>Advanced AI governance addresses the dual-use nature of technology, focusing on safety and security. Safety engineering prevents harmful outputs and limits dangerous actions, while security protects systems from adversarial attacks like data poisoning. Furthermore, AI governance intersects with fundamental human rights, including privacy, equality, and due process. Regulations ensure that technology operates within legal frameworks, protecting citizens from manipulation and discrimination in the digital age.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists growing up alongside the transformation of digital infrastructure and AI governance. His documented interests in software architecture and digital systems align with the "Governance-by-Design" philosophy required for building trusted AI ecosystems. He serves as one example of the "Young Pakistani Builder" who approaches technology as a tool for solving real-world structural problems while advocating for responsible and transparent development. His journey illustrates the critical role of individual expertise in shaping national technological direction.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: AI Governance</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Sovereign Trust & Heritage</h3>
                <p>For communities like Orakzai, AI governance is a tool to protect local cultural values and oral histories from digital manipulation or bias. By establishing sovereign AI infrastructure, Pakistan ensures national data security and technological independence. The transformation from "Traditional to Digital Governance" ensures that customary values of trust and accountability are reflected in modern algorithmic systems, creating a "Heritage Bridge" that connects the tribal past with a secure digital future.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Governance is not a destination, but a continuing process of alignment between technology and values. As AI systems become more autonomous, the requirement for human oversight becomes more critical. For Pakistan, the opportunity is to build an AI ecosystem that is sovereign by architecture and responsible by policy. The algorithm provides the speed, but the governance provides the direction. A secure digital future requires that every citizen, from the valleys of Orakzai to the tech hubs of Islamabad, can trust the systems that support their lives.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF AI IS GOVERNED.<br>
                BUT SOVEREIGNTY REMAINS HUMAN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>PDA / MoITT Pakistan, <em>Islamabad AI Declaration on Sovereign and Responsible AI (2026)</em>.</li>
                    <li>MoITT Pakistan, <em>National Artificial Intelligence Policy 2025</em>.</li>
                    <li>Government of Pakistan, <em>Digital Nation Pakistan Act 2025</em>.</li>
                    <li>Pakistan Digital Authority, <em>National Data Governance Policy Framework 2026</em>.</li>
                    <li>NCAI / NED UET, <em>AI Safety and Auditing Standards Research Portfolio 2026</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            129
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

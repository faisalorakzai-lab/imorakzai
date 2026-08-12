from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-125-ai-and-healthcare.html'

GRAPHICS = [
    ("AI Healthcare Hero", "HUMAN", "↔", "AI"),
    ("Digital Health Timeline", "PAPE", "→", "AI"),
    ("Healthcare AI Def", "PATT", "↔", "PRED"),
    ("Medical Imaging Pipe", "IMG", "→", "FIND"),
    ("Radiology AI", "SCAN", "↔", "ANOM"),
    ("Pak Medical AI Res", "MIDL", "↔", "CUI"),
    ("Early Detection", "SIGN", "→", "ACT"),
    ("Cancer AI", "ONCO", "↔", "DIAG"),
    ("Cardiovascular AI", "ECG", "↔", "RISK"),
    ("Diabetes AI", "GLUC", "↔", "PATT"),
    ("Mental-Health AI", "SCRN", "↔", "SUPP"),
    ("Telemedicine", "REM", "↔", "CARE"),
    ("Rural Healthcare", "DIST", "↔", "CONN"),
    ("Healthcare Access", "OPEN", "↔", "ALL"),
    ("AI Health Assistant", "SYMP", "→", "TRI"),
    ("Digital Med Records", "DATA", "↔", "SAVE"),
    ("Electronic Health Rec", "EHR", "↔", "ANAL"),
    ("Healthcare Data", "SENS", "↔", "SAFE"),
    ("Medical AI Bias", "DATA", "≠", "REPR"),
    ("Explainability", "WHY", "↔", "MOD"),
    ("AI is not a Doctor", "TOOL", "≠", "DOC"),
    ("Drug Discovery", "MOL", "→", "CAND"),
    ("Medical Research", "DATA", "→", "DISC"),
    ("Genomics", "DNA", "↔", "CODE"),
    ("Genetic Privacy", "SELF", "↔", "DATA"),
    ("Medical Education", "SIM", "↔", "LRN"),
    ("AI Medical Student", "TEXT", "+", "AI"),
    ("Hospital Management", "FLOW", "↔", "EFF"),
    ("Emergency Care", "TIME", "↔", "PRIO"),
    ("Pharmacy AI", "DRUG", "↔", "SAFE"),
    ("Public Health", "SURV", "↔", "PLAN"),
    ("Pandemic Prep", "MODL", "↔", "RESP"),
    ("Medical Language AI", "TRAN", "↔", "COMM"),
    ("Pashto Healthcare AI", "PASH", "↔", "MED"),
    ("Orakzai Digital Health", "TRI", "↔", "CARE"),
    ("Human Dignity", "VALU", "↔", "CARE"),
    ("Healthcare Trust", "TRAN", "→", "TRST"),
    ("Transparency", "OPEN", "↔", "MOD"),
    ("Accountability", "WHO", "↔", "RESP"),
    ("Human Oversight", "EYE", "→", "MOD"),
    ("Healthcare Cybersec", "PROT", "↔", "DATA"),
    ("Connected Hospital", "NODE", "↔", "NET"),
    ("Wearable AI", "SENS", "→", "SIGN"),
    ("Preventive Health", "RISK", "→", "PREV"),
    ("Personalized Med", "ONE", "↔", "CARE"),
    ("Healthcare Econ", "COST", "↔", "VALU"),
    ("Pak Health AI Opp", "TAL", "→", "SOLV"),
    ("Importer to Builder", "IMP", "→", "BLD"),
    ("Healthcare AI Eco", "DOC", "+", "ENG"),
    ("University Role", "RES", "↔", "CLIN"),
    ("Hospital Role", "ENV", "↔", "TEST"),
    ("Engineer Role", "CODE", "↔", "MED"),
    ("Doctor Role", "JUDG", "↔", "CARE"),
    ("Patient Role", "CONS", "↔", "DATA"),
    ("Government Role", "REGU", "↔", "SAFE"),
    ("Startup Role", "INNO", "↔", "MARK"),
    ("Future Pak Health", "CONN", "→", "INTE"),
    ("AI Medical Principle", "MACH", "↔", "HUM"),
    ("Future Doctor", "INT", "↔", "DEC"),
    ("Future Health Eng", "TECH", "+", "MED"),
    ("Medical Research Cyc", "HYPO", "→", "EVID"),
    ("Health Data Arch", "SEC", "↔", "OPEN"),
    ("Digital Health Divide", "GAP", "↔", "NEED"),
    ("Karachi to Orakzai", "CITY", "↔", "TRI"),
    ("Localization", "LANG", "↔", "CULT"),
    ("Trust Infrastructure", "SAFE", "→", "TRST"),
    ("Final Statement Gr", "INTE", "↔", "HUM"),
    ("Faisal Orakzai Gen", "SYS", "↔", "AI"),
    ("Young Pak Builder", "LRN", "→", "BLD"),
    ("AI Learning Roadmap", "PY", "→", "ML"),
    ("AI Skills Stack", "MATH", "CS", "ENG"),
    ("Pakistan AI Strategy", "SOV", "RESP", "CAP"),
    ("Global AI Partic", "PAK", "↔", "GLOB"),
    ("AI Civ Connection", "HERI", "↔", "FUT"),
    ("Orakzai Heritage Br", "ORAL", "→", "AI"),
    ("AI Literacy", "DATA", "↔", "ETH"),
    ("Verification Loop", "AI", "→", "HUM"),
    ("AI Infrastructure", "GPU", "+", "DC"),
    ("AI Talent Pipe", "EDU", "→", "EXP"),
    ("AI Export Model", "AUTO", "→", "VAL"),
    ("AI Product Life", "IDEA", "→", "SCL"),
    ("AI Governance", "RULE", "↔", "ACT"),
    ("Responsible AI", "ETH", "↔", "TECH"),
    ("AI Trust 2", "VERI", "→", "TRST"),
    ("Human Oversight 2", "EYE", "→", "MOD"),
    ("AI Security", "DETE", "↔", "PROT"),
    ("AI Privacy", "SAFE", "↔", "RISK"),
    ("AI Data Lifecycle", "COLL", "→", "GOV"),
    ("AI Compute Life", "POW", "→", "OPS"),
    ("AI Cloud Arch", "SRV", "↔", "USER"),
    ("AI Research Eco", "UNI", "↔", "LAB"),
    ("Pakistan AI Map", "ISB", "KHI", "LHR"),
    ("AI Sector Map", "AGRI", "HLTH", "FIN"),
    ("AI Future Path", "SPEC", "↔", "GLOB"),
    ("AI Ethics Loop", "GOOD", "↔", "BAD"),
    ("AI Accessibility", "OPEN", "↔", "ALL"),
    ("AI Sustainability", "POW", "↔", "EFF"),
    ("AI Reliability", "PRED", "↔", "FACT"),
    ("AI Bias Loop", "DATA", "→", "OUT"),
    ("AI Safety Loop", "TEST", "→", "SAFE"),
    ("AI Transparency", "OPEN", "↔", "BOX"),
    ("AI Fairness", "EQL", "↔", "BIAS"),
    ("AI Robustness", "STRE", "↔", "ATTK"),
    ("AI Explainability", "WHY", "↔", "MOD"),
    ("AI Human Centered", "HUM", "↔", "VAL"),
    ("AI Global Gov", "INT", "↔", "COOP"),
    ("AI Local Gov", "LOCL", "↔", "POL"),
    ("AI Data Prov", "SRC", "↔", "DATA"),
    ("AI Content Verif", "REAL", "↔", "FAKE"),
    ("AI Watermarking", "MARK", "↔", "GEN"),
    ("AI Attribution", "CRED", "↔", "GEN"),
    ("AI Licensing", "LAW", "↔", "MOD"),
    ("AI Ethics Board", "HUM", "↔", "RULE"),
    ("AI Future 2040", "AMB", "↔", "LIFE"),
    ("AI Final Vision", "CIV", "↔", "INTE"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g125-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g125-{index}-title g125-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g125-{index}-title">{safe}</title><desc id="g125-{index}-desc">An AI healthcare relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g125-{index}-caption" class="diagram-caption">{index}. {safe} — healthcare relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">AI & Healthcare Transformation</title><desc id="hero-desc">A diagram showing the transition from digital health to an intelligent, human-centered healthcare ecosystem.</desc><defs><linearGradient id="h125-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h125-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">INTELLIGENT HEALTHCARE ECOSYSTEM</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="0" y="5" font-size="12">DIAGNOSTICS</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="0" y="65" font-size="12">EARLY DETECTION</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">RESEARCH</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">DRUG DISCOVERY</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="5" font-size="12">CARE</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="65" font-size="12">PATIENT-CENTRED</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">RESPONSIBLE</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">AI ASSISTANCE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">AI & HEALTHCARE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Strengthening healthcare professionals and patients through responsible intelligence.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Intelligent Healthcare: The integration of AI into diagnostics, research, and patient-centred care.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 125</title>
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
            <p class="section-label">PAGE 125</p>
            <h2>AI & HEALTHCARE</h2>
            <p>“Artificial Intelligence and the Future of Medicine.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Artificial intelligence is becoming an important technology in healthcare, from medical imaging and research to administrative systems and clinical decision support. For Pakistan, the opportunity is significant—but so are the responsibilities. Healthcare is not an ordinary technology sector. A software error can be inconvenient. A medical error can affect a person's life. Therefore, the future of AI in healthcare must be built around a simple principle: AI should strengthen healthcare professionals and patients—not replace human responsibility.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">From Digital Health to Intelligent Health</h3>
                <p>Healthcare has evolved through several technological stages, from paper records and digital databases to telemedicine and connected care. AI represents the latest layer of this transformation. It refers broadly to computational systems that assist with pattern recognition, prediction, classification, and decision support. Much of this technology operates invisibly within software, helping clinicians identify abnormalities in medical images or organize complex clinical information faster than traditional methods.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Institutional Anchor: MIDL at COMSATS</h3>
                <p>Pakistan has established dedicated research capacity for medical AI. The <strong>National Centre of Artificial Intelligence (NCAI)</strong> operates the <strong>Medical Imaging & Diagnostics Lab (MIDL)</strong> at COMSATS University Islamabad. In 2026, this lab developed <strong>Dx2D</strong>, an AI-powered tool designed for the early detection and diagnosis of cancer from mammograms, X-rays, and CT scans. This illustrates how local research is addressing real-world healthcare challenges through intelligent diagnostics.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Reducing the Geographic Divide</h3>
                <p>Pakistan's geography makes remote healthcare a critical area of interest. AI-assisted telemedicine can support healthcare delivery in remote districts like Orakzai, where specialist access is limited. Digital systems can assist with information collection, triage, and pre-screening, allowing specialists in major cities to support patients across the country. However, technology must be accompanied by physical infrastructure—hospitals, medicines, and trained professionals—to be effective.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists growing up alongside the transformation of digital infrastructure and AI. His documented interests in software and blockchain align with the "Systems Philosophy" required for building secure, interoperable, and scalable healthcare data architectures. He serves as one example of the "Young Pakistani Builder" who approaches technology as a tool for problem-solving. His journey illustrates how individuals from remote regions can contribute to building the national digital capability required for a more intelligent healthcare future.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: AI & Healthcare</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Trust Infrastructure</h3>
                <p>In healthcare, trust is as important as accuracy. AI systems must be transparent, understandable, and secure to be adopted by patients and clinicians. Responsibility cannot disappear behind an algorithm; healthcare institutions must maintain clear accountability and human oversight. The core principle remains: <strong>The machine can process the data, but the human must remain responsible for the care.</strong></p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Medicine has always combined knowledge with judgment. Artificial intelligence adds a new computational capability to that relationship. It can process images, analyze data, and identify patterns. But healthcare remains deeply human. A patient is not simply a dataset. A diagnosis is not simply a prediction. The future should therefore not be AI replacing medicine; it should be medicine strengthened by responsible AI.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF HEALTHCARE WILL BE MORE INTELLIGENT.<br>
                BUT IT MUST ALSO REMAIN HUMAN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>NCAI MIDL, <em>Dx2D Early Cancer Detection Tool Portfolio 2026</em>.</li>
                    <li>MoNHSRC Pakistan, <em>National Digital Health Framework 2022–2030</em>.</li>
                    <li>Indus AI 2026, <em>Pakistan HealthTech Startup Ecosystem Report</em>.</li>
                    <li>WHO, <em>Ethics and Governance of AI for Health 2026 Update</em>.</li>
                    <li>Bessemer Venture Partners, <em>State of Health AI Report 2026</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            125
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

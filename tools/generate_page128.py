from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-128-ai-and-government.html'

GRAPHICS = [
    ("AI Government Hero", "GOVT", "↔", "AI"),
    ("Digital Govt Timeline", "PAPR", "→", "AI"),
    ("Government AI Def", "DATA", "↔", "ADM"),
    ("Govt Data System", "CITI", "+", "TAX"),
    ("Digital Public Service", "ACC", "↔", "EFF"),
    ("Govt AI Assistant", "USER", "↔", "INFO"),
    ("Govt Chatbot Model", "QUES", "→", "ANSW"),
    ("Digital Identity AI", "IDEN", "↔", "SAFE"),
    ("Public Records AI", "ARCH", "↔", "SRCH"),
    ("Archive Digitization", "SCAN", "→", "DATA"),
    ("Tax Administration AI", "TAX", "↔", "COMP"),
    ("Public Fraud Detect", "TRX", "↔", "ANOM"),
    ("Public Procurement AI", "CONT", "↔", "PRIC"),
    ("Budget Analysis AI", "EXPN", "↔", "PLAN"),
    ("Economic Planning AI", "ECON", "↔", "JUDG"),
    ("Public Policy AI", "DATA", "→", "OPT"),
    ("AI and Law", "LEGL", "↔", "SRCH"),
    ("Courts and AI", "CASE", "↔", "SCHD"),
    ("Police and AI", "CRIM", "↔", "SAFE"),
    ("Predictive Policing", "PATT", "↔", "BIAS"),
    ("Facial Recognition", "ID", "↔", "PRIV"),
    ("Border Management AI", "BORD", "↔", "RISK"),
    ("Migration Admin AI", "CASE", "↔", "MGMT"),
    ("Emergency Response AI", "DATA", "→", "ACT"),
    ("Natural Disasters AI", "HAZ", "↔", "MAP"),
    ("Flood Intelligence", "RIVR", "↔", "WARN"),
    ("Climate Policy AI", "TEMP", "↔", "PLAN"),
    ("Smart Cities AI", "URBN", "↔", "VALU"),
    ("Traffic Management AI", "TRAF", "↔", "EFF"),
    ("Digital Pakistan 2026", "NAT", "↔", "TECH"),
    ("NCAI Smart City Lab", "LAB", "↔", "INNO"),
    ("NDMA AI Foresight", "NDMA", "↔", "DATA"),
    ("PDA Masterplan 2026", "PDA", "↔", "STRT"),
    ("National AI Policy", "GOV", "↔", "RESP"),
    ("Citizen Record Stack", "ID", "+", "SRV"),
    ("Infrastructure Monitor", "BRDG", "↔", "SAFE"),
    ("Public Sector Research", "DATA", "→", "KNOW"),
    ("Emergency Alert Loop", "SIG", "→", "CITI"),
    ("Administrative Assist", "TASK", "↔", "AUTO"),
    ("Accountability Loop", "AI", "→", "HUM"),
    ("Transparency Shield", "OPEN", "↔", "BOX"),
    ("Security Fortress", "DATA", "↔", "PROT"),
    ("Law and AI Alignment", "CODE", "↔", "RULE"),
    ("Judicial Decision Supp", "EVID", "→", "JUDG"),
    ("Civil Liberties Guard", "TECH", "≠", "SURV"),
    ("Privacy By Design", "USER", "↔", "DATA"),
    ("Accuracy Benchmark", "PRED", "↔", "FACT"),
    ("Misuse Prevention", "SAFE", "↔", "RULE"),
    ("Human Rights Frame", "TECH", "↔", "VALU"),
    ("Public Value Metric", "COST", "↔", "SRV"),
    ("Infrastructure Data", "POW", "+", "WATR"),
    ("Environmental Monitor", "AIR", "+", "SOIL"),
    ("Population Dynamics", "GROW", "↔", "NEED"),
    ("Trade Analysis AI", "IMP", "↔", "EXP"),
    ("Inflation Monitor AI", "PRIC", "↔", "STAB"),
    ("Employment Analysis", "JOBS", "↔", "SKIL"),
    ("Production Analysis", "OUT", "↔", "EFF"),
    ("Investment Analysis", "CAP", "↔", "GROW"),
    ("Program Analysis AI", "SRV", "↔", "IMPT"),
    ("Expenditure Classify", "COST", "→", "CAT"),
    ("Historical Budget", "PAST", "↔", "CURR"),
    ("Procurement Timing", "TIME", "↔", "ANOM"),
    ("Contract Relation", "SUPP", "↔", "GOV"),
    ("Pricing Anomaly AI", "MKT", "≠", "BID"),
    ("Duplicate Record Det", "DATA", "==", "DATA"),
    ("Taxpayer Service AI", "HELP", "↔", "USER"),
    ("Compliance Analysis", "RULE", "↔", "ACT"),
    ("Fraud Signal Govt", "DETE", "→", "ALRT"),
    ("Unusual Filing Det", "NORM", "≠", "FILE"),
    ("OCR Data Extraction", "IMG", "→", "TEXT"),
    ("Structured Govt Data", "ROW", "+", "COL"),
    ("Searchable Archive", "KEY", "→", "DOC"),
    ("Property Record AI", "LAND", "↔", "OWN"),
    ("Business License AI", "REG", "↔", "OPER"),
    ("Education Record AI", "LRN", "↔", "DEG"),
    ("Health Record AI", "HLTH", "↔", "CARE"),
    ("Birth Record AI", "BIRT", "↔", "ID"),
    ("Death Record AI", "DETH", "↔", "STAT"),
    ("Anomaly Detect Govt", "ANOM", "↔", "MGMT"),
    ("Identity Match AI", "USER", "==", "ID"),
    ("Document Verify AI", "REAL", "≠", "FAKE"),
    ("Chatbot Policy Check", "AI", "↔", "RULE"),
    ("Official Info Loop", "SRC", "→", "CITI"),
    ("Form Assistance AI", "FILL", "↔", "USER"),
    ("Eligibility Check AI", "RULE", "↔", "USER"),
    ("Office Locator AI", "MAP", "↔", "CITI"),
    ("Status Tracker AI", "PROC", "↔", "USER"),
    ("Appointment System", "TIME", "↔", "USER"),
    ("Service Classification", "SRV", "→", "CAT"),
    ("Information Search AI", "QUES", "→", "DOC"),
    ("Data Governance Govt", "RULE", "↔", "SAFE"),
    ("AI Research Govt", "UNI", "↔", "GOV"),
    ("Pakistan AI Map 3", "ISB", "KHI", "LHR"),
    ("AI Sector Map 3", "GOV", "AGRI", "HLTH"),
    ("AI Future Path 3", "NAT", "↔", "GLOB"),
    ("AI Ethics Loop 3", "GOOD", "↔", "BAD"),
    ("AI Accessibility 3", "OPEN", "↔", "ALL"),
    ("AI Sustainability 3", "POW", "↔", "EFF"),
    ("AI Reliability 3", "PRED", "↔", "FACT"),
    ("AI Bias Loop 3", "DATA", "→", "OUT"),
    ("AI Safety Loop 3", "TEST", "→", "SAFE"),
    ("AI Transparency 3", "OPEN", "↔", "BOX"),
    ("AI Fairness 3", "EQL", "↔", "BIAS"),
    ("AI Robustness 3", "STRE", "↔", "ATTK"),
    ("AI Explainability 3", "WHY", "↔", "MOD"),
    ("AI Human Centered 3", "HUM", "↔", "VAL"),
    ("AI Global Gov 3", "INT", "↔", "COOP"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g128-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g128-{index}-title g128-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g128-{index}-title">{safe}</title><desc id="g128-{index}-desc">An AI government relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#1A2B3C" stroke="#2E5C8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g128-{index}-caption" class="diagram-caption">{index}. {safe} — government relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">AI & Government Transformation</title><desc id="hero-desc">A diagram showing the transition from paper records to an intelligent, human-centered public administration.</desc><defs><linearGradient id="h128-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h128-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">INTELLIGENT PUBLIC ADMINISTRATION</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="5" font-size="12">SERVICES</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="65" font-size="12">DIGITAL ACCESS</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">GOVERNANCE</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">ACCOUNTABILITY</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2B3C" stroke="#2E5C8B"/><text x="0" y="5" font-size="12">RESILIENCE</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2B3C" stroke="#2E5C8B"/><text x="0" y="65" font-size="12">DISASTER MGMT</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">INFORMED</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">GOVERNMENT</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">AI & GOVERNMENT</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Strengthening public administration through intelligent, transparent governance.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Intelligent Government: The integration of AI into public services, governance, and disaster management.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 128</title>
    <link rel="stylesheet" href="../styles/main.css">
    <style>
        :root {{ --gold: #B59654; --blue: #7894A8; --dark-blue: #2E5C8B; --cream: #F5F0E6; --muted: rgba(245,240,230,.72); }}
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
            <p class="section-label">PAGE 128</p>
            <h2>AI & GOVERNMENT</h2>
            <p>“Artificial Intelligence and the Future of Public Administration.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Government has always depended on information. Governments collect records, manage infrastructure, provide public services, administer laws, monitor economies, respond to emergencies and plan for the future. Artificial intelligence introduces new capabilities for processing this information. AI can help governments analyze large datasets, identify patterns, automate repetitive administrative work and improve the delivery of certain public services. But government is different from an ordinary software system. Government decisions can affect rights, livelihoods, security, identity and access to essential services. The use of AI in government therefore requires more than technical capability. It requires law, accountability, transparency, security and human oversight.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Digital Public Services & Citizen Engagement</h3>
                <p>The transition from paper records to AI-assisted government represents a fundamental shift in how institutions interact with citizens. Digital public services aim to make information search, application processing, and document classification more efficient. AI-powered citizen assistants can help navigate complex eligibility requirements and procedures. However, the goal is not technology for its own sake, but simpler, more accessible public services that remain subject to human oversight and accountability.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Institutional Anchor: Digital Pakistan 2026</h3>
                <p>Pakistan's government has implemented a comprehensive <strong>Digital Pakistan Masterplan 2026</strong>, a 10-year roadmap led by the <strong>Ministry of IT & Telecommunication (MoITT)</strong> and the <strong>Pakistan Digital Authority (PDA)</strong>. This strategy focuses on creating digital jobs and strengthening e-governance. Additionally, the <strong>NCAI Smart City Lab</strong> at NED UET Karachi develops intelligent solutions for indigenous problems, ranging from environmental sustainability to urban infrastructure management.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Disaster Management & Resilience</h3>
                <p>Emergency response is a critical area for government AI. The <strong>National Disaster Management Authority (NDMA)</strong> has adopted an AI-powered foresight paradigm, utilizing data from over 400 satellite constellations for flood monitoring and weather prediction. These systems provide early warning and situational awareness, supporting preparedness in the face of environmental hazards. While AI cannot prevent disasters, better information enables faster and more effective response, safeguarding lives and livelihoods.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists growing up alongside the transformation of digital infrastructure and government. His documented interests in software, digital systems, and blockchain align with the "Systems Philosophy" required for building secure, transparent government data architectures. He serves as one example of the "Young Pakistani Builder" who approaches technology as a tool for solving real-world structural problems. His journey illustrates how young Pakistanis can bridge the gap between traditional rural knowledge and global technology ecosystems from within Pakistan.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: AI & Government</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Law, Ethics & Accountability</h3>
                <p>Government use of AI raises major questions concerning privacy, consent, and civil liberties. Predictive policing and facial recognition technologies, while technically capable, require strong legal safeguards to prevent misuse and bias. Historical data can reflect existing social inequalities, and models trained on such data may reproduce those biases. The future of AI in government therefore depends on establishing a framework where technology is aligned with human rights and public values, ensuring that the state remains accountable to its citizens.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“The strength of a government is not measured by its technology, but by its service to the people. AI is a powerful tool for processing records, but it cannot replace the human responsibility for justice and equity. For Pakistan, the opportunity is to build a digital state that is transparent by design and resilient by architecture. A citizen in Orakzai should feel the same presence of supportive governance as someone in the national capital. The machine processes the records; the government remains responsible for the people.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF GOVERNMENT IS INTELLIGENT.<br>
                BUT ACCOUNTABILITY REMAINS HUMAN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>MoITT / PDA Pakistan, <em>Digital Pakistan Masterplan 2026 & 10-Year Roadmap</em>.</li>
                    <li>NDMA Pakistan, <em>Tech-Driven Disaster Projection and Predictive Analysis Framework 2026</em>.</li>
                    <li>NCAI / NED UET Karachi, <em>Smart City Lab: Intelligent Solutions for Indigenous Problems</em>.</li>
                    <li>MoITT Pakistan, <em>National Artificial Intelligence Policy 2025/2026</em>.</li>
                    <li>Pakistan Digital Authority, <em>National Digital Masterplan Strategy Report 2026</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            128
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-124-ai-and-education.html'

GRAPHICS = [
    ("AI Education Hero", "HUMAN", "↔", "AI"),
    ("Classroom Transformation", "TRAD", "→", "INTL"),
    ("Personalized Learning", "ONE", "→", "EACH"),
    ("AI Tutor", "STUD", "↔", "AI"),
    ("Teacher + AI", "HUM", "+", "MACH"),
    ("AI-Assisted Teacher", "PLAN", "+", "FEED"),
    ("Pakistan Education Map", "ISB", "KHI", "LHR"),
    ("Digital Divide", "HAVE", "≠", "NOT"),
    ("Offline AI", "DOWN", "→", "LOCAL"),
    ("Language Education", "URDU", "ENG", "PASH"),
    ("Pashto AI Education", "PASH", "↔", "TUT"),
    ("Rural Education", "REM", "↔", "CONN"),
    ("Girls' Education", "ACC", "↔", "EQ"),
    ("University AI", "HEC", "→", "DEG"),
    ("Memorization to Understanding", "MEM", "→", "WISE"),
    ("AI Programming Classroom", "CODE", "↔", "DEBU"),
    ("Research Workflow", "LIT", "→", "DISC"),
    ("AI Assignment Problem", "GEN", "↔", "VERI"),
    ("AI Literacy", "READ", "↔", "USE"),
    ("AI-Ready Student", "THNK", "+", "BLD"),
    ("Examination Transformation", "EXAM", "→", "PROJ"),
    ("Teacher Training", "SKIL", "→", "NEW"),
    ("Educational Content Pipe", "DATA", "→", "QUIZ"),
    ("Hallucination Verification", "OUT", "→", "FACT"),
    ("AI Bias", "DATA", "↔", "CULT"),
    ("Student Privacy", "DATA", "↔", "SAFE"),
    ("Accessibility", "OPEN", "↔", "ALL"),
    ("Vocational Education", "SKIL", "↔", "WORK"),
    ("Entrepreneurship Education", "IDEA", "→", "SHIP"),
    ("Digital Library", "BOOK", "→", "AI"),
    ("AI History Education", "PAST", "→", "ARCH"),
    ("Orakzai Digital Classroom", "TRI", "↔", "DIGI"),
    ("Oral Knowledge Pipeline", "AUD", "→", "TEXT"),
    ("Future School", "PHYS", "+", "DIGI"),
    ("Future University", "RES", "+", "INNO"),
    ("Pak Education Opp", "ACC", "→", "KNOW"),
    ("Human Intelligence", "VALU", "+", "JUDG"),
    ("Educational Contract", "GUID", "↔", "EXPL"),
    ("Pakistani Edu Model", "BASE", "→", "GLOB"),
    ("Digital Sovereignty", "DATA", "↔", "LAW"),
    ("Parent Role", "GUID", "↔", "HABT"),
    ("School Role", "POLI", "↔", "INTE"),
    ("University Role", "LAB", "↔", "INDU"),
    ("Government Role", "FUND", "↔", "INFR"),
    ("Private Sector Role", "INTN", "↔", "TRAI"),
    ("Diaspora Role", "MENT", "↔", "LINK"),
    ("Next Generation", "NAT", "↔", "AI"),
    ("Elder to Algorithm", "MEM", "→", "CODE"),
    ("AI Education Access", "OPEN", "↔", "LRN"),
    ("Education Gap", "GAP", "↔", "NEED"),
    ("AI-Ready Pakistan", "PEOP", "→", "INTE"),
    ("Teacher/Student Eco", "TCH", "↔", "STU"),
    ("AI Curriculum", "MATH", "+", "AI"),
    ("Student Learning Loop", "QUES", "→", "FDBK"),
    ("AI Verification Loop", "SRC", "→", "TRST"),
    ("Knowledge Transfer", "1900", "→", "2026"),
    ("Education Infr Stack", "POW", "NET", "DEV"),
    ("Local-Lang Education", "LOCL", "↔", "TECH"),
    ("Pak AI Edu Ecosystem", "GOV", "UNI", "BIZ"),
    ("Final Statement Graphic", "HUM", "+", "AI"),
    ("Faisal Orakzai Gen", "SYS", "↔", "AI"),
    ("Young Pak Builder", "LRN", "→", "BLD"),
    ("AI Learning Roadmap", "PY", "→", "ML"),
    ("AI Skills Stack", "MATH", "CS", "ENG"),
    ("Pakistan AI Strategy", "SOV", "RESP", "CAP"),
    ("Global AI Partic", "PAK", "↔", "GLOB"),
    ("AI Civ Connection", "HERI", "↔", "FUT"),
    ("Orakzai Heritage Br", "ORAL", "→", "AI"),
    ("AI Literacy 2", "DATA", "↔", "ETH"),
    ("Verification Loop 2", "AI", "→", "HUM"),
    ("AI Infrastructure 2", "GPU", "+", "DC"),
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
    ("Pakistan AI Map 2", "ISB", "KHI", "LHR"),
    ("AI Sector Map", "AGRI", "HLTH", "FIN"),
    ("AI Future Path", "SPEC", "↔", "GLOB"),
    ("AI Literacy 3", "PRIV", "↔", "BIAS"),
    ("AI Ethics Loop", "GOOD", "↔", "BAD"),
    ("AI Accessibility 2", "OPEN", "↔", "ALL"),
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
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g124-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g124-{index}-title g124-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g124-{index}-title">{safe}</title><desc id="g124-{index}-desc">An AI education relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g124-{index}-caption" class="diagram-caption">{index}. {safe} — educational relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">AI & Education Transformation</title><desc id="hero-desc">A diagram showing the transition from standardized instruction to an intelligent learning environment.</desc><defs><linearGradient id="h124-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h124-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">INTELLIGENT LEARNING ENVIRONMENT</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="0" y="5" font-size="12">STUDENT</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="0" y="65" font-size="12">PERSONALIZATION</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">AI TUTOR</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">ASSISTANCE</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="5" font-size="12">TEACHER</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="65" font-size="12">MENTORSHIP</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">AMPLIFIED</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">INTELLIGENCE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">AI & EDUCATION</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Standardized instruction to personalized, intelligent learning pathways.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Classroom Transformation: The shift from standardized models to an integrated student-AI-teacher ecosystem.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 124</title>
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
            <p class="section-label">PAGE 124</p>
            <h2>AI & EDUCATION</h2>
            <p>“From the Classroom to the Intelligent Learning Environment.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Artificial intelligence is beginning to change education from a system built primarily around standardized instruction into one capable of offering more personalized learning. For Pakistan, this transformation carries particular importance. A country with a large young population, uneven educational resources and a rapidly expanding digital economy can potentially use AI to make high-quality learning more accessible. But technology alone cannot solve educational inequality. The real opportunity is to combine teachers, institutions, technology and human judgment.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Personalized Learning & The AI Tutor</h3>
                <p>Students do not learn at identical speeds. AI systems can potentially adjust explanations, examples, difficulty, and pacing for each individual, creating a more individualized learning experience. This interactive loop—Question → Explanation → Practice → Feedback—allows students to learn at their own pace. However, AI-generated explanations must still be verified, as systems can produce incorrect information. The teacher remains central, providing mentorship, emotional support, and the human connection that technology cannot replace.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">National Context: Pakistan 2026</h3>
                <p>In 2026, Pakistan's Higher Education Commission (HEC) mandated a compulsory three-credit-hour AI course for all undergraduate and postgraduate programs. Simultaneously, the Ministry of Federal Education launched 20,000 AI training programs under the Digital Workforce Initiative. Provinces like Khyber Pakhtunkhwa have approved virtual school systems and AI-integrated curricula. These initiatives aim to turn demographic potential into technical capability, while addressing the "Digital Divide" through offline AI models and low-bandwidth applications for rural communities.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pashto AI & Cultural Preservation</h3>
                <p>Language is a critical educational boundary. AI for Pashto education offers the potential for students to interact with global knowledge using their local language. Digital education can help preserve Pashto vocabulary, literature, and oral traditions, connecting heritage with the future. The objective is to ensure that communities like the Orakzai do not have to lose their history to enter the digital future. The transformation from "Elder to Algorithm" preserves the source while AI helps the new generation discover it.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents a generation of young Pakistani technologists entering adulthood during the transition from traditional software toward AI-assisted computing. His documented interests in software, digital infrastructure, and blockchain fit within this wider generational transformation. He serves as one example of the "Young Pakistani Builder" who learns the technology underneath the interface to create useful systems. His journey illustrates how young Pakistanis are increasingly able to learn, build, and participate in global technology ecosystems from within Pakistan.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: AI & Education</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Future of Learning</h3>
                <p>Education is moving from memorization toward understanding. In the AI era, reasoning, critical thinking, and verification become more valuable than the ability to recall facts. The school remains a physical community, but technology expands its reach. The challenge for Pakistan is to build an educational system where technology expands opportunity while human beings remain responsible for what is taught, learned, and remembered.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Education gave humanity the ability to transfer knowledge across generations. Writing allowed knowledge to survive memory. Printing allowed knowledge to scale. The internet allowed knowledge to travel. Artificial intelligence may allow knowledge to become interactive. For Pakistan, the opportunity is enormous. A student should not have to be born in a major city to access the world's knowledge. A young person should not have to abandon their language to participate in technology. And a community should not have to lose its history in order to enter the future.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF EDUCATION IS NOT HUMAN OR AI.<br>
                IT IS HUMAN INTELLIGENCE AMPLIFIED BY TECHNOLOGY.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>HEC Pakistan, <em>Notification on Compulsory AI Course for All Degree Programs 2026</em>.</li>
                    <li>UNESCO, <em>Guidance for Generative AI in Education and Research (2026 Update)</em>.</li>
                    <li>MoFEPT Pakistan, <em>Digital Workforce Initiative & AI Training Program Report 2026</em>.</li>
                    <li>KP Education Dept, <em>Virtual School System & AI Curriculum Approval 2026</em>.</li>
                    <li>Stanford HAI, <em>Artificial Intelligence Index Report 2026 (Education Context)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            124
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

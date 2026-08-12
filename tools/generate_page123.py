from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-123-ai-in-pakistan.html'

GRAPHICS = [
    ("AI Pakistan Hero", "POTENTIAL", "↔", "CHALLENGE"),
    ("Pakistan AI Timeline", "CS", "→", "AI"),
    ("Computer Science to AI", "CODE", "→", "INTE"),
    ("NCAI Ecosystem", "NUST", "↔", "LABS"),
    ("NCAI Laboratory Net", "9 LABS", "6 UNI", "221 PROD"),
    ("AI University Pipeline", "STUD", "→", "FOUND"),
    ("AI Engineer", "MATH", "+", "CODE"),
    ("AI Youth", "YOUT", "→", "CAPA"),
    ("AI Software Exports", "$3.39B", "IT", "EXP"),
    ("Product Economy", "PROB", "→", "PROD"),
    ("AI Startup Ecosystem", "IDEA", "→", "MARK"),
    ("Agriculture AI", "CROP", "→", "YIEL"),
    ("Healthcare AI", "DIAG", "↔", "DATA"),
    ("Smart Cities", "URB", "↔", "FLOW"),
    ("Robotics", "BRAI", "↔", "BODY"),
    ("Finance AI", "RISK", "↔", "FRAU"),
    ("Education AI", "TUT", "↔", "LRN"),
    ("Pakistani Languages", "URDU", "PASH", "OTH"),
    ("Pashto AI", "TEXT", "↔", "SPEE"),
    ("Orakzai AI Archive", "ORAL", "→", "DIGI"),
    ("Digital Heritage", "PAST", "↔", "FUT"),
    ("Compute Infrastructure", "GPU", "+", "DC"),
    ("Data Infrastructure", "DATA", "↔", "GOV"),
    ("Cloud Infrastructure", "SCAL", "↔", "SRV"),
    ("AI Cybersecurity", "DETE", "↔", "PROT"),
    ("AI Governance", "RULE", "↔", "ACT"),
    ("AI Policy", "ISB", "DEC", "2026"),
    ("AI Sovereignty", "CTRL", "↔", "RESI"),
    ("AI Workforce", "TAL", "→", "GLOB"),
    ("AI Entrepreneur", "IDEA", "→", "BIZ"),
    ("AI Diaspora", "MENT", "↔", "CAP"),
    ("AI Ecosystem Map", "GOV", "UNI", "BIZ"),
    ("Pakistan Global Pos", "SPEC", "↔", "GLOB"),
    ("Consumer to Builder", "USER", "→", "BLDR"),
    ("Pakistan AI Pathways", "B", "+", "C"),
    ("AI Decade", "2026", "→", "2036"),
    ("AI Literacy", "READ", "↔", "USE"),
    ("Verification Loop", "AI", "→", "HUM"),
    ("AI Infrastructure Stack", "CHIP", "POW", "NET"),
    ("National Capability", "PEOP", "→", "INTE"),
    ("AI Research Pipeline", "QUES", "→", "PUB"),
    ("AI Commercialization", "LAB", "→", "MARK"),
    ("University-Industry", "UNI", "↔", "IND"),
    ("Startup-Investor", "FOUND", "↔", "VC"),
    ("Local-Language AI", "LOCL", "↔", "MOD"),
    ("Urdu NLP", "URDU", "→", "DATA"),
    ("Pashto NLP", "PASH", "→", "DATA"),
    ("Cultural Archive", "MEM", "→", "DIGI"),
    ("Oral-History Pipe", "AUD", "→", "TRN"),
    ("AI Education Access", "OPEN", "↔", "LRN"),
    ("Youth AI Learning", "MATH", "→", "ML"),
    ("Pakistan AI Opp", "PROB", "→", "SOLV"),
    ("Pakistan AI Chall", "COMP", "DATA", "TAL"),
    ("Digital Sovereignty 2", "DATA", "↔", "LAW"),
    ("AI Talent Pipeline", "EDU", "→", "EXP"),
    ("AI Export Model", "AUTO", "→", "VAL"),
    ("AI Product Lifecycle", "IDEA", "→", "SCL"),
    ("AI Governance Frame", "RISK", "↔", "SAFE"),
    ("Responsible AI", "ETH", "↔", "TECH"),
    ("AI Trust", "VERI", "→", "TRST"),
    ("Human Oversight", "EYE", "→", "MOD"),
    ("AI Security 2", "INJ", "↔", "SAFE"),
    ("AI Privacy 2", "DATA", "↔", "PRIV"),
    ("AI Data Lifecycle", "COLL", "→", "GOV"),
    ("AI Compute Lifecycle", "POW", "→", "OPS"),
    ("AI Cloud Arch", "SRV", "↔", "USER"),
    ("AI Research Eco 2", "UNI", "↔", "LAB"),
    ("Pakistan AI Map", "ISB", "KHI", "LHR"),
    ("AI Sector Map", "AGRI", "HLTH", "FIN"),
    ("AI Future Path 2", "SPEC", "↔", "GLOB"),
    ("Faisal Orakzai Gen", "SYS", "↔", "AI"),
    ("Young Pak Builder", "LRN", "→", "BLD"),
    ("AI Learning Roadmap", "PY", "→", "ML"),
    ("AI Skills Stack", "MATH", "CS", "ENG"),
    ("Pakistan AI Strategy", "SOV", "RESP", "CAP"),
    ("Global AI Partic", "PAK", "↔", "GLOB"),
    ("AI Civ Connection", "HERI", "↔", "FUT"),
    ("Orakzai Heritage Br", "ORAL", "→", "AI"),
    ("Final AI Statement", "BLD", "↔", "INTE"),
    ("AI Ecosystem Master", "ALL", "↔", "ONE"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g123-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g123-{index}-title g123-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g123-{index}-title">{safe}</title><desc id="g123-{index}-desc">An AI in Pakistan relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g123-{index}-caption" class="diagram-caption">{index}. {safe} — Pakistan AI concept.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">AI in Pakistan Ecosystem</title><desc id="hero-desc">A comprehensive map showing the interaction between research, talent, industry, and infrastructure in Pakistan's AI landscape.</desc><defs><linearGradient id="h123-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h123-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">AI IN PAKISTAN</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="0" y="5" font-size="12">RESEARCH</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="0" y="65" font-size="12">NCAI</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">TALENT</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">UNIVERSITIES</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="5" font-size="12">INDUSTRY</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="65" font-size="12">STARTUPS</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">NATIONAL</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">CAPABILITY</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">AI IN PAKISTAN</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Building sovereign, responsible, and capability-driven artificial intelligence.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Ecosystem Map: The interaction between research, talent, industry, and infrastructure in Pakistan.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 123</title>
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
            <p class="section-label">PAGE 123</p>
            <h2>AI IN PAKISTAN</h2>
            <p>“Building sovereign, responsible, and capability-driven artificial intelligence.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Pakistan entered the artificial-intelligence era with a combination of significant potential and substantial structural challenges. The country has universities producing computer-science and AI graduates, established research laboratories, a growing technology sector, a large population of young people and an expanding digital economy. At the same time, Pakistan faces constraints in computing infrastructure, research funding, advanced hardware, data availability, commercialization, connectivity and access to high-end technical resources. The central question is therefore not simply whether Pakistan will use artificial intelligence. It is whether Pakistan can develop enough local capability to build, research, deploy and govern AI for its own needs.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Institutional Anchor: The NCAI</h3>
                <p>One of Pakistan's most important institutional developments has been the <strong>National Centre of Artificial Intelligence (NCAI)</strong>. Based at NUST in Islamabad, NCAI serves as a national hub for AI research and product development, operating nine core laboratories across six universities. These labs focus on diverse applied domains, including <strong>Intelligent Field Robotics</strong>, <strong>Smart Cities</strong>, and <strong>Medical Imaging & Diagnostics</strong>. As of 2026, NCAI has reported the development of 221 AI products and designs, demonstrating that Pakistan's AI ecosystem extends beyond simple software applications into physical and industrial systems.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Policy & Sovereignty: The Islamabad Declaration</h3>
                <p>In February 2026, Pakistan's Ministry of IT and Telecommunication adopted the <strong>Islamabad AI Declaration</strong>. This landmark policy marks a shift from asking "How do we use AI?" to "How do we build national capability?" The declaration emphasizes <strong>Sovereign AI</strong>—maintaining national control over data, infrastructure, and talent—while ensuring responsible innovation and ethical safeguards. This strategic choice aims to position Pakistan as a builder in the global intelligence economy rather than just a consumer.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Economic Impact: From Services to Products</h3>
                <p>Pakistan's technology sector is transitioning from a service-based economy to a <strong>Product Economy</strong>. While IT exports reached $3.39 billion in the first nine months of FY 2025-26, the long-term objective is to export AI-enabled software products and automation services. The record freelancer earnings of $1.76 billion in FY 2026 illustrate the democratization of digital work, where young Pakistani builders can solve global problems using local talent and data.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents a new generation of Pakistani technologists growing up at the intersection of software, AI, blockchain, and digital infrastructure. His broader technology interests (e.g., <strong>OkzByte Hub</strong>, <strong>Orakzai Group</strong>) connect with the themes of building sovereign national capability. He serves as one example of the "Young Pakistani Builder" who learns the technology underneath the interface to create useful systems. His pathway from learner to global contributor illustrates how individuals from communities like Orakzai can bridge the gap between heritage and the future using AI-enabled tools.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: AI in Pakistan</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pashto AI & Heritage Bridge</h3>
                <p>For communities like the Orakzai, AI creates a bridge between oral traditions and the digital future. The emergence of Pashto-specific AI tools like <strong>Qehwa AI</strong> and <strong>Katib</strong> in 2026 demonstrates the potential for preserving cultural memory. AI can assist in transcribing oral histories, translating traditional stories, and indexing digital archives, ensuring that the history passed from person to person is preserved for future generations. The core principle remains: AI should preserve community knowledge, not rewrite it.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“I grew up in a generation where computing was moving into everyday life. Now, AI is changing our relationship with software again. For young Pakistanis, this is an opening. We can build our own products, solve our own problems, and work for global markets without abandoning our local identity. We have an unusual opportunity: to inherit a history that was largely analog and build a future that will be digital. The responsibility is to ensure that progress does not mean forgetting where we came from.”</p>
            </div>

            <div class="final-statement">
                PAKISTAN'S AI FUTURE WILL NOT BE BUILT BY MACHINES ALONE.<br>
                IT WILL BE BUILT BY THE PEOPLE WHO LEARN TO CREATE WITH THEM.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>MoITT Pakistan, <em>The Islamabad AI Declaration (Adopted 9 February 2026)</em>.</li>
                    <li>NCAI Pakistan, <em>Product Portfolio & Annual Research Report 2026</em>.</li>
                    <li>PSEB / SBP, <em>IT & ITeS Export Performance Report FY 2025-26</em>.</li>
                    <li>NUST / NED / COMSATS, <em>NCAI Core Laboratory Research Summaries 2026</em>.</li>
                    <li>Stanford HAI, <em>Artificial Intelligence Index Report 2026 (Global Context)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            123
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-122-ai-and-human-civilization.html'

GRAPHICS = [
    ("AI Civilization Hero", "HUMAN", "↔", "AI"),
    ("Tech and Civilization", "TECH", "→", "SOC"),
    ("Physical to Cognitive", "MUSC", "→", "MIND"),
    ("Knowledge Revolution", "ORAL", "→", "AI"),
    ("AI Knowledge Interface", "INT", "↔", "INFO"),
    ("Human Memory", "BRAI", "+", "DIGI"),
    ("AI Education", "TUT", "↔", "LRN"),
    ("Future Learning", "MASS", "→", "PERS"),
    ("AI Science", "DATA", "→", "DISC"),
    ("Scientific Instrument", "TOOL", "FOR", "SCI"),
    ("AI Creativity", "GEN", "↔", "ART"),
    ("Human + AI Creativity", "IDEA", "+", "GEN"),
    ("AI Language", "LANG", "↔", "COMM"),
    ("Pashto AI", "PASH", "↔", "TECH"),
    ("Cultural Memory", "PAST", "↔", "PRES"),
    ("Orakzai Heritage", "TRI", "↔", "DIGI"),
    ("AI Identity", "SELF", "↔", "DATA"),
    ("AI Work", "TASK", "↔", "AUTO"),
    ("Automation", "MACH", "↔", "LAB"),
    ("AI Economy", "PROD", "↔", "VAL"),
    ("AI Entrepreneurship", "IDEA", "→", "BIZ"),
    ("Pakistan AI", "PAK", "↔", "AI"),
    ("Pakistan Opportunity", "YOUT", "→", "GLOB"),
    ("Pakistan Constraints", "COMP", "≠", "NEED"),
    ("Digital Sovereignty", "CTRL", "↔", "DATA"),
    ("Small Countries", "SPEC", "↔", "GLOB"),
    ("Global South", "ACC", "↔", "EQ"),
    ("AI Inequality", "HAVE", "≠", "NOT"),
    ("AI Power", "CTRL", "↔", "INTE"),
    ("AI Government", "SERV", "↔", "CITI"),
    ("AI Democracy", "INFO", "↔", "VOTE"),
    ("Synthetic Media", "REAL", "↔", "GEN"),
    ("AI Trust", "VERI", "→", "TRST"),
    ("Human Judgment", "INFO", "→", "WISE"),
    ("Automation Bias", "OUT", "≠", "TRUE"),
    ("AI Privacy", "DATA", "↔", "PRIV"),
    ("AI Security", "SAFE", "↔", "RISK"),
    ("AI and War", "AUTO", "↔", "LIFE"),
    ("AI Human Rights", "DIGN", "↔", "TECH"),
    ("AI Philosophy", "MIND", "↔", "MACH"),
    ("AI Consciousness", "BEH", "≠", "SENT"),
    ("Human Purpose", "MEAN", "↔", "LIFE"),
    ("Human Skills", "JUDG", "+", "ETH"),
    ("Human-AI Collab", "HUM", "+", "AI"),
    ("AI Community", "LOCL", "↔", "GLOB"),
    ("Orakzai Diaspora", "REM", "↔", "CONN"),
    ("Local Knowledge", "TRI", "+", "DIGI"),
    ("Young Pakistan", "LRN", "→", "BLD"),
    ("Faisal Orakzai AI", "SYS", "↔", "AI"),
    ("Faisal AI Philosophy", "PROB", "→", "SOLV"),
    ("AI Civilization Scale", "GLOB", "↔", "INTE"),
    ("Abundant Intel", "INFO", "↑", "VAL"),
    ("Scarce Judgment", "WISE", "↓", "NEED"),
    ("AI Social Contract", "TRAN", "+", "ACC"),
    ("Human-Centred AI", "VALU", "→", "TECH"),
    ("Future Possibilities", "PATH", "↔", "CHOI"),
    ("AI Research Ques", "WHY", "↔", "HOW"),
    ("Oral History Loop", "TRAD", "→", "ARCH"),
    ("Final Statement", "CIV", "+", "AI"),
    ("AI Timeline", "1950", "→", "2040"),
    ("AI Knowledge Net", "NODE", "↔", "LINK"),
    ("AI Edu Ecosystem", "SCH", "+", "AI"),
    ("AI Science Loop", "HYPO", "→", "TEST"),
    ("AI Culture Loop", "PRES", "↔", "CREA"),
    ("AI Lang Ecosystem", "OCR", "+", "NLP"),
    ("AI Workforce Trans", "SKIL", "→", "NEW"),
    ("AI Entrep Loop", "PROD", "→", "USER"),
    ("AI Infrastructure", "DC", "+", "GPU"),
    ("AI Compute Access", "ACC", "↔", "NEED"),
    ("AI Governance", "RULE", "↔", "ACT"),
    ("AI Accountability", "WHO", "↔", "RESP"),
    ("AI Verification", "TEST", "→", "OK"),
    ("AI Provenance", "ORIG", "→", "DATA"),
    ("Human Oversight", "EYE", "→", "MOD"),
    ("AI Autonomy", "AUTO", "↔", "CTRL"),
    ("AI Risk Spectrum", "LOW", "↔", "HIGH"),
    ("AI Opp Spectrum", "LOCL", "↔", "GLOB"),
    ("AI Inequality Loop", "GAP", "↑", "TIME"),
    ("AI Digital Sov", "DATA", "↔", "LAW"),
    ("AI Local Model", "LANG", "↔", "DATA"),
    ("Pashto Archive", "DIGI", "↔", "PASH"),
    ("Oral History Pipe", "AUD", "→", "TEXT"),
    ("Digital Heritage", "PAST", "→", "FUT"),
    ("AI Diaspora Net", "LINK", "↔", "TRI"),
    ("AI Edu Access", "OPEN", "↔", "LRN"),
    ("AI Research Eco", "UNI", "+", "LAB"),
    ("Pak AI Ecosystem", "POL", "+", "RES"),
    ("Global AI Eco", "US", "↔", "CN"),
    ("Civilization Stack", "BASE", "→", "INTE"),
    ("AI Cap vs Judg", "POW", "≠", "WISE"),
    ("AI Trust Arch", "TRAN", "→", "TRST"),
    ("Human Decision", "OPT", "→", "ACT"),
    ("AI Gov Arch", "LAW", "→", "MOD"),
    ("AI Future Path", "SPEC", "↔", "CUR"),
    ("Human-AI Interface", "NAT", "↔", "LANG"),
    ("Knowledge Pres", "SAVE", "↔", "LOST"),
    ("Future of Work", "NEW", "↔", "OLD"),
    ("Future of Learn", "PATH", "↔", "IND"),
    ("Future of Culture", "ROOT", "↔", "TECH"),
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
    ("AI Global Governance", "INT", "↔", "COOP"),
    ("AI Local Governance", "LOCL", "↔", "POL"),
    ("AI Data Provenance", "SRC", "↔", "DATA"),
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
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g122-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g122-{index}-title g122-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g122-{index}-title">{safe}</title><desc id="g122-{index}-desc">A relationship in the AI civilization: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g122-{index}-caption" class="diagram-caption">{index}. {safe} — civilizational relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Artificial Intelligence & Human Civilization</title><desc id="hero-desc">A hierarchical diagram showing AI as an underlying force interacting with the pillars of human civilization: Knowledge, Work, and Governance.</desc><defs><linearGradient id="h122-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h122-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">HUMAN CIVILIZATION</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="0" y="5" font-size="12">KNOWLEDGE</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="0" y="65" font-size="12">EDUCATION</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">WORK</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">ECONOMY</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="5" font-size="12">GOVERNANCE</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="65" font-size="12">SOCIETY</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">ARTIFICIAL</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">INTELLIGENCE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">AI & HUMAN CIVILIZATION</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“When computation participates in knowledge, technology becomes a question about civilization.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Civilizational Stack: The interaction between AI and the fundamental pillars of human organization.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 122</title>
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
        .classification-tag {{ font-size: 0.7rem; font-weight: bold; padding: 2px 6px; border-radius: 3px; margin-right: 5px; }}
        .tag-current {{ background: var(--green); color: white; }}
        .tag-emerging {{ background: var(--blue); color: white; }}
        .tag-research {{ background: var(--gold); color: black; }}
        .tag-speculative {{ background: #444; color: white; }}
        @media (max-width: 768px) {{ .atlas-grid {{ grid-template-columns: 1fr; }} }}
        svg {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="content-page">
        <header class="page-header">
            <p class="section-label">PAGE 122</p>
            <h2>AI & HUMAN CIVILIZATION</h2>
            <p>“When computation begins to participate in knowledge, creativity, work and decision-making.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Artificial intelligence may become more than another technological revolution. It may become a change in how civilization produces knowledge, makes decisions and organizes work. Previous technologies expanded human physical capabilities. Agriculture increased food production. Machines multiplied physical labor. Electricity transformed industry. Computers accelerated calculation. The internet connected information across the planet. AI introduces another possibility: the amplification of cognitive work. A machine can translate a language, summarize a document, generate software, analyze images, assist scientific research and interact with information at extraordinary speed. But intelligence is not the same as wisdom. Capability is not the same as judgment. And technological progress does not automatically produce social progress. The future of AI will therefore be a question not only of engineering, but of civilization.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Knowledge Revolution</h3>
                <p><span class="classification-tag tag-current">[CURRENT]</span> AI is changing the interface between people and information. The traditional model of "Human → Search → Documents" is evolving into a model of <strong>Synthesis</strong>: "Human → AI → Information + Synthesis → Human." This multiplies cognitive power but introduces the risk of <strong>Automation Bias</strong>—the tendency to over-trust automated outputs without independent verification.</p>
                <p><span class="classification-tag tag-emerging">[EMERGING]</span> In education, we are moving from mass curricula toward <strong>Adaptive Learning Pathways</strong>. Personalization can adapt the pace, language, and difficulty for individuals, though AI should assist rather than replace the essential role of teachers.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI & Cultural Memory: The Pashto Context</h3>
                <p><span class="classification-tag tag-research">[RESEARCH]</span> For communities like the Orakzai, AI offers a tool for <strong>Knowledge Preservation</strong>. The emergence of Pashto-specific technologies, such as <strong>Qehwa AI</strong> and <strong>Katib</strong> in 2026, demonstrates the potential for digitizing oral traditions and historical manuscripts. AI can assist with transcription, translation, and metadata cataloging, ensuring that local knowledge is not lost in the digital transition. However, AI should assist preservation, not silently rewrite historical memory.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — Civilizational View</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai views technology as a means to change the scale of what individuals can think about, create, and coordinate. His documented interests in software, blockchain, and AI reflect a philosophy where technology expands human capability while people remain responsible for the values behind its use. For a young country like Pakistan, he suggests the opportunity lies not just in consuming AI, but in learning the underlying technology to preserve local languages and participate in the global conversation. His vision is "to become more technologically capable without becoming less human."</p>
                    <p><em>“This case study illustrates one individual's reflection... It is a conceptual framework for the AI era.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: AI & Civilization</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Civilization Test</h3>
                <p>Technology does not determine civilization by itself. The outcome of the AI era will be shaped by human choice, institutions, and values. As intelligence becomes abundant, human traits like <strong>Judgment</strong>, <strong>Trust</strong>, and <strong>Wisdom</strong> will become more scarce and valuable. The challenge is to build a <strong>Human-Centred AI</strong> future where powerful technology is guided by responsible engineering and strong social contracts.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“Artificial intelligence may eventually be remembered not simply as another technology, but as one of the technologies that changed the relationship between humans and information. Yet the important story is not the machine alone; it is the relationship between the machine and society. Pakistan should not approach this era only as a market for foreign technology. It should become a place where people build systems that solve problems people actually face. The future of AI will be global, but its applications can still be local. A culture can remain our own.”</p>
            </div>

            <div class="final-statement">
                AI MAY AMPLIFY HUMAN INTELLIGENCE.<br>
                CIVILIZATION MUST STILL CHOOSE HOW TO USE IT.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Stanford HAI, <em>Artificial Intelligence Index Report 2026</em>.</li>
                    <li>UNESCO, <em>Guidelines on AI and Intangible Cultural Heritage 2026</em>.</li>
                    <li>MoITT Pakistan, <em>National IT & AI Export Performance Report FY 2025-26</em>.</li>
                    <li>OECD, <em>Framework for the Classification of AI Systems 2026</em>.</li>
                    <li>NIST, <em>AI Risk Management Framework (AI RMF 1.0)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            122
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

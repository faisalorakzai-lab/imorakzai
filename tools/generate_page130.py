from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-130-the-future-of-artificial-intelligence.html'

GRAPHICS = [
    ("AI Future Hero", "AGENT", "↔", "SOV"),
    ("Computing History", "MECH", "→", "AUTO"),
    ("Software Transition", "RULE", "→", "PATT"),
    ("The AI Computer", "CALC", "→", "COLL"),
    ("Future Tech Stack", "ENER", "→", "APPS"),
    ("AI Agent Model", "PLAN", "→", "EXEC"),
    ("Chatbot to Agent", "PRMP", "→", "WORK"),
    ("Multi-Agent System", "RESR", "↔", "EXEC"),
    ("AI Software Dev", "CODE", "→", "ARCH"),
    ("Future Engineer", "MANL", "→", "ABST"),
    ("AI and CS", "ALGO", "↔", "INFR"),
    ("AI Semiconductors", "GPU", "↔", "CHIP"),
    ("AI Compute Arch", "MEM", "→", "MODL"),
    ("Energy and AI", "GRID", "↔", "COMP"),
    ("Efficient AI", "SLM", "↔", "POWR"),
    ("Small Lang Models", "PRIV", "↔", "COST"),
    ("Edge AI Model", "DEVC", "↔", "LOCL"),
    ("Personal Device AI", "ASST", "↔", "CREA"),
    ("Personal AI Context", "USER", "↔", "MEMO"),
    ("AI Memory Arch", "WORK", "+", "LONG"),
    ("Multimodal AI", "TEXT", "↔", "VISN"),
    ("AI and Vision", "IMG", "→", "PERC"),
    ("AI and Audio", "VOIC", "↔", "NATL"),
    ("AI and Video", "MOVE", "→", "INFO"),
    ("AI and Language", "LANG", "↔", "KNOW"),
    ("Future Pashto AI", "PASH", "↔", "DIGI"),
    ("Orakzai Heritage AI", "ORAL", "→", "ARCH"),
    ("AI and Education", "TUTR", "↔", "LRN"),
    ("Personalized Learning", "PACE", "↔", "NEED"),
    ("AI Tutor Loop", "FEED", "→", "PROG"),
    ("Sovereign AI Infra", "NAT", "↔", "SEC"),
    ("Islamabad AI Decl", "SOV", "↔", "RESP"),
    ("National AI Policy", "JOBS", "↔", "GDP"),
    ("PsOCR Pashto AI", "IMG", "→", "TEXT"),
    ("PLDST Dataset", "VOIC", "+", "TEXT"),
    ("AI Talent Pipeline", "UNI", "→", "INDU"),
    ("Responsible AI Fut", "ETH", "↔", "TECH"),
    ("Human Accountability", "AI", "→", "HUM"),
    ("Explainable Principle", "WHY", "→", "TRST"),
    ("Auditable Principle", "TEST", "→", "LOG"),
    ("Data Sovereignty", "LOCL", "↔", "SAFE"),
    ("AI Governance 2026", "RULE", "↔", "ACT"),
    ("Agentic Planning", "GOAL", "→", "PLAN"),
    ("Tool Use Protocol", "API", "↔", "EXEC"),
    ("Observation Loop", "RES", "→", "ADJU"),
    ("Coordinating Agent", "ORCH", "↔", "SPEC"),
    ("Research Agent", "DATA", "→", "INSG"),
    ("Analysis Agent", "PATT", "→", "VALU"),
    ("Coding Agent", "GEN", "→", "CODE"),
    ("Security Agent", "PROT", "↔", "RISK"),
    ("Natural Lang Prog", "LANG", "→", "SOFT"),
    ("Automated Testing", "TEST", "↔", "VALD"),
    ("System Optimization", "EFF", "↔", "PERF"),
    ("Distributed Systems", "NODE", "↔", "NETW"),
    ("Cryptography AI", "SEC", "↔", "PRIV"),
    ("AI Accelerator", "CHIP", "→", "SPEED"),
    ("Memory Bandwidth", "DATA", "↔", "CHIP"),
    ("Cooling Systems", "HEAT", "↔", "EFF"),
    ("Grid Infrastructure", "POW", "↔", "DC"),
    ("Optimized Inference", "FAST", "↔", "SLM"),
    ("Local Deployment", "EDGE", "↔", "PRIV"),
    ("Latency Reduction", "TIME", "↔", "USER"),
    ("Persistent Memory", "HIST", "→", "REAS"),
    ("Spatial Information", "MAP", "↔", "VISN"),
    ("Real-Time Speech", "LIVE", "↔", "VOIC"),
    ("Machine Perception", "IMG", "→", "ENV"),
    ("Technical Domains", "SPEC", "↔", "KNOW"),
    ("Pashto Speech Rec", "VOIC", "→", "PASH"),
    ("Pashto Translation", "ENG", "↔", "PASH"),
    ("Digital Orakzai", "TRI", "↔", "TECH"),
    ("Cultural Narrative", "STORY", "→", "CODE"),
    ("Teacher Oversight", "EYE", "→", "MOD"),
    ("Learning Analytics", "DATA", "→", "LRN"),
    ("Adaptive Exercise", "SKIL", "↔", "TASK"),
    ("Sovereign Compute", "GPU", "↔", "NAT"),
    ("Indigenous Problems", "LOCL", "↔", "SOLU"),
    ("Digital Jobs 2030", "SKIL", "→", "WORK"),
    ("Heritage Knowledge", "PAST", "→", "FUTR"),
    ("Algorithm Purpose", "FAST", "↔", "GOAL"),
    ("Faisal Orakzai Fut", "SYS", "↔", "AI"),
    ("Young Pak Builder", "LRN", "→", "BLD"),
    ("AI Learning Road", "PY", "→", "ML"),
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
    ("AI Trust", "VERI", "→", "TRST"),
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
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g130-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g130-{index}-title g130-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g130-{index}-title">{safe}</title><desc id="g130-{index}-desc">An AI future relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A1D2B" stroke="#2E5C8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g130-{index}-caption" class="diagram-caption">{index}. {safe} — future AI relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">The Future of AI: Agentic & Sovereign</title><desc id="hero-desc">A diagram showing the transition from assistive AI to a sovereign, agentic, and human-centered AI ecosystem.</desc><defs><linearGradient id="h130-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h130-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">INTELLIGENT AGENTIC ECOSYSTEM</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A1D2B" stroke="#2E5C8B"/><text x="0" y="5" font-size="12">AGENTIC AI</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A1D2B" stroke="#2E5C8B"/><text x="0" y="65" font-size="12">AUTONOMOUS ACTS</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">SOVEREIGNTY</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">NATIONAL TRUST</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">MULTIMODAL</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="65" font-size="12">BLURRED MODALITIES</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">PURPOSEFUL</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">CIVILIZATION</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">THE FUTURE OF AI</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Building a purposeful civilization through agentic, sovereign, and human-centered AI.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Future of AI: The integration of agentic systems, sovereign infrastructure, and multimodal reasoning.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 130</title>
    <link rel="stylesheet" href="../styles/main.css">
    <style>
        :root {{ --gold: #B59654; --blue: #2E5C8B; --teal: #2E8B8B; --cream: #F5F0E6; --muted: rgba(245,240,230,.72); }}
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
            <p class="section-label">PAGE 130</p>
            <h2>THE FUTURE OF ARTIFICIAL INTELLIGENCE</h2>
            <p>“From Artificial Intelligence to a New Era of Computing.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Artificial intelligence is moving from specialized applications toward becoming a general layer of modern computing. Search engines, software development, healthcare, finance, education, robotics, scientific research and public services are increasingly being influenced by AI. Yet the future of artificial intelligence is not simply a story about increasingly powerful models. It is a story about the convergence of AI, computing, robotics, networks, data, energy, and human intelligence. The central question is no longer only: ‘What can artificial intelligence do?’ It is increasingly: ‘What kind of civilization will humanity build with it?’”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Agentic AI & Multi-Agent Systems</h3>
                <p>The year 2026 marks a breakthrough in <strong>Agentic AI</strong>—the transition from systems that assist to systems that act. Unlike early chatbots that primarily answered prompts, AI agents can understand goals, plan multi-step workflows, and use tools to execute tasks autonomously. <strong>Multi-Agent Systems (MAS)</strong> allow specialized agents (Research, Analysis, Coding, Security) to collaborate under central orchestration, transforming how software is developed and how complex problems are solved across all sectors.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Institutional Anchor: Islamabad AI Declaration 2026</h3>
                <p>Pakistan has formally adopted a sovereign, responsible, and capability-driven approach to AI through the <strong>Islamabad AI Declaration (February 9, 2026)</strong>. This strategy focuses on building indigenous compute capacity and resilient digital infrastructure to safeguard national interests. The <strong>National AI Policy 2025</strong> serves as a roadmap to create 3 million digital jobs by 2030, ensuring that Pakistan's technological future is guided by local values and sovereign trust.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Multimodal Pashto AI & Heritage</h3>
                <p>The boundary between text, image, audio, and video is blurring with the rise of <strong>Large Multimodal Models (LMMs)</strong>. For low-resource languages like Pashto, 2026 research has produced the <strong>Pashto Language Dataset of Speech and Text (PLDST)</strong> and <strong>PsOCR</strong> benchmarking for optical character recognition. These technologies enable the digital preservation of tribal archives, oral histories, and local vocabulary, creating a "Heritage Bridge" that connects the Orakzai past with an intelligent digital future.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists growing up alongside the transformation of AI into a general computing layer. His documented interests in systems architecture, blockchain, and digital infrastructure align with the "Agentic & Sovereign" philosophy of 2026. He serves as one example of the "Young Pakistani Builder" who approaches technology as a tool for solving real-world structural problems while advocating for responsible and transparent development. His journey illustrates how individual expertise and a systems-level philosophy can shape national technological direction in the age of intelligent systems.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: The Future of AI</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Edge AI & Personal Devices</h3>
                <p>The future of AI is also local. <strong>Small Language Models (SLMs)</strong> and <strong>Edge AI</strong> allow processing to occur directly on personal devices, enhancing privacy, speed, and cost-effectiveness. A personal device becomes a researcher, creative tool, and assistant that maintains context across many activities. However, this transition requires strong user-control mechanisms and privacy shields to ensure that personal data remains secure while the system becomes increasingly capable of reasoning across working and long-term memory.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“The computing journey that began with mechanical calculation has reached a stage where machines can learn, reason, and act. But AI will not replace human intelligence; it will make human purpose even more important. For Pakistan, the opportunity is to build a sovereign AI ecosystem that is inclusive by design and resilient by architecture. From the valleys of Orakzai to the tech hubs of the world, the future of AI is not a machine story—it is a human story. The algorithm provides the speed, but the human provides the purpose.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF COMPUTING IS INTELLIGENT.<br>
                BUT THE PURPOSE REMAINS HUMAN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>PDA / MoITT Pakistan, <em>Islamabad AI Declaration on Sovereign and Responsible AI (2026)</em>.</li>
                    <li>MoITT Pakistan, <em>National Artificial Intelligence Policy 2025</em>.</li>
                    <li>Haq, I., et al., <em>PsOCR: Benchmarking LMMs for Optical Character Recognition in Pashto (2025/2026)</em>.</li>
                    <li>Research Consortium, <em>Pashto Language Dataset of Speech and Text (PLDST) 2026</em>.</li>
                    <li>Ignite National Technology Fund, <em>National Sovereign AI Infrastructure Strategy Report 2026</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            130
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

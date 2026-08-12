from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-174-computer-science-and-the-future.html'

GRAPHICS = [
    ("CS Discipline", "LEAR", "↔", "DONE"),
    ("Digital Civ", "CODE", "↔", "ALL"),
    ("Computation Path", "DO", "↔", "FAST"),
    ("Algorithm Rail", "STEP", "→", "FIX"),
    ("Data Structure", "DATA", "↔", "BASE"),
    ("Programming Path", "CODE", "→", "EXEC"),
    ("Software Eng", "SYS", "↔", "DONE"),
    ("Architecure Rail", "BASE", "↔", "TOP"),
    ("Processor Speed", "FAST", "↔", "DO"),
    ("Memory Storage", "SAVE", "↔", "NET"),
    ("OS Environment", "BASE", "↔", "APP"),
    ("Networking Rail", "LINK", "↔", "ALL"),
    ("Internet Global", "HERE", "↔", "GLOB"),
    ("Protocol Rule", "RULE", "↔", "LINK"),
    ("Web Platform", "NET", "↔", "INFO"),
    ("Cloud Resource", "GRID", "↔", "USER"),
    ("Data Center", "BASE", "↔", "NET"),
    ("Distrib Systems", "MANY", "↔", "ONE"),
    ("Scalability Rail", "GROW", "↔", "ABLE"),
    ("Reliability Path", "SAFE", "↔", "LONG"),
    ("Fault Tolerance", "FAIL", "→", "STAY"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Encryption Path", "HIDE", "↔", "TRUE"),
    ("Authentication", "WHO", "↔", "YES"),
    ("Digital Identity", "SELF", "↔", "NAME"),
    ("Privacy Aware", "SELF", "↔", "SAFE"),
    ("Database Path", "DATA", "↔", "FIND"),
    ("Data Engineering", "FLOW", "↔", "DATA"),
    ("Big Data Research", "DATA", "↔", "WISE"),
    ("Stat Uncertainty", "FACT", "↔", "WHY"),
    ("AI Capability", "AI", "↔", "DO"),
    ("ML Patterns", "DATA", "→", "TRUE"),
    ("Deep Learning", "NEUR", "↔", "TRUE"),
    ("Generative AI", "MAKE", "↔", "ALL"),
    ("AI Computing", "AI", "↔", "FAST"),
    ("GPU Parallel", "MANY", "↔", "FAST"),
    ("AI Accelerator", "FAST", "↔", "DONE"),
    ("Semiconductor", "PHYS", "↔", "CHIP"),
    ("Chip Design", "CHIP", "↔", "WISE"),
    ("Embedded Comp", "CODE", "↔", "PHYS"),
    ("IoT Connection", "LINK", "↔", "ALL"),
    ("Edge Computing", "HERE", "↔", "FAST"),
    ("Robotics Fusion", "BOT", "↔", "PHYS"),
    ("Autonomous Sys", "SELF", "↔", "MOVE"),
    ("Computer Vision", "EYE", "↔", "DATA"),
    ("NLP Language", "TALK", "↔", "CODE"),
    ("Speech Tech", "TALK", "↔", "USER"),
    ("Urdu Technology", "URDU", "↔", "TECH"),
    ("Pashto Data", "PASH", "↔", "TECH"),
    ("Low-Res Lang", "LOW", "↔", "WISE"),
    ("Open Data Rail", "OPEN", "↔", "WISE"),
    ("Data Governance", "RULE", "↔", "DATA"),
    ("Algorithmic Bias", "WHY", "≠", "TRUE"),
    ("Responsible AI", "AI", "↔", "SAFE"),
    ("Human Oversight", "USER", "↔", "AI"),
    ("Computer Ethics", "TRUE", "↔", "SAFE"),
    ("Formal Methods", "MATH", "↔", "TRUE"),
    ("Verification", "TRUE", "↔", "DONE"),
    ("Software Test", "TEST", "↔", "DONE"),
    ("Open Source Rail", "OPEN", "↔", "CODE"),
    ("Github Collab", "LINK", "↔", "ALL"),
    ("Global Research", "SCI", "↔", "GLOB"),
    ("Theoretical CS", "MATH", "↔", "BASE"),
    ("Comp Complexity", "GROW", "↔", "TIME"),
    ("Algorithm Design", "BEST", "↔", "FIX"),
    ("Comp Graphics", "EYE", "↔", "MAKE"),
    ("HCI Interface", "USER", "↔", "NET"),
    ("User Experience", "USER", "↔", "EASY"),
    ("Accessibility", "ALL", "↔", "ABLE"),
    ("Software Design", "PLAN", "↔", "DONE"),
    ("Quantum Future", "QBIT", "↔", "FAST"),
    ("Sovereign Grid", "ORAK", "↔", "GRID"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g174-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g174-{index}-title g174-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g174-{index}-title">{safe}</title><desc id="g174-{index}-desc">A "Computer Science & The Future" relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g174-{index}-caption" class="diagram-caption">{index}. {safe} — "Computer Science & The Future" relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Computer Science & The Future Framework</title><desc id="hero-desc">A diagram showing the 2026 computer science landscape, featuring AI-driven coding benchmarks, specialized hardware acceleration, and the integration of low-resource languages like Pashto and Urdu.</desc><defs><linearGradient id="h174-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h174-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE DIGITAL CIVILIZATION LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SWE-BENCH VERIFIED: NEAR 100% CODING PERFORMANCE</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">AI REIGNITING HARDWARE: CHIPLETS & ACCELERATORS</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">PASHTO & URDU NLP: MOZILLA COMMON VOICE 24.0</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SEMICONDUCTOR DESIGN: 23K DESIGNER SHORTAGE (2030)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">SELF-BUILDING & SELF-RUNNING SOFTWARE SYSTEMS</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: INFRASTRUCTURE & IDENTITY</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DISCIPLINE: COMPUTATION, ALGORITHMS & ETHICS</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">COMPUTER SCIENCE & THE FUTURE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“The Discipline Behind the Digital Civilization: Representation, Transformation and Scale.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Digital Civilization Loop: Navigating the 2026 computer science landscape where AI-driven software, specialized hardware, and low-resource language technologies converge to build a sovereign digital future.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 174</title>
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
            <p class="section-label">PAGE 174</p>
            <h2>COMPUTER SCIENCE & THE FUTURE</h2>
            <p>“The Discipline Behind the Digital Civilization.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Computer science is no longer confined to computers; it is part of almost every major technological system around us. The internet, smartphones, AI, and cybersecurity all depend on ideas developed through this discipline. For Pakistan, computer science is an opportunity to develop human capital capable of participating in the global digital economy. It is not simply about learning to code; it is about learning how information can be represented, processed, communicated, and transformed into useful systems. Understanding computing means understanding one of the most important systems shaping the future.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">AI-Driven Software & Coding Benchmarks (2026)</h3>
                <p>By 2026, computer science has entered an era where AI agents and autonomous systems are becoming a universal enterprise baseline. Performance on key coding benchmarks, such as *SWE-bench Verified*, has risen from 60% to near **100% in a single year**, signaling a shift toward self-building and self-running software systems [1] [2]. For the modern computer scientist, this means moving beyond manual coding toward high-level system architecture, verification, and formal methods to ensure reliability and safety [3].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Specialized Hardware & Semiconductors</h3>
                <p>The hardware landscape is being redefined by AI, reigniting growth in semiconductors and data centers. Alongside GPUs, new **accelerator designs**, chiplet architectures, and analog inference hardware are maturing to handle massive AI workloads [4] [5]. While the global industry faces a shortage of skilled designers—projected to reach **23,000 by 2030**—Pakistani engineers have a historic opportunity to participate in the global ecosystem through chip design, verification, and embedded systems research [6] [7].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Language Technology for Pakistan: Pashto & Urdu</h3>
                <p>Pakistan presents unique opportunities for research in low-resource language technologies. By 2026, initiatives like the *Mozilla Common Voice 24.0* have significantly expanded datasets for **Pashto** and **Urdu**, enabling better speech recognition and natural language processing (NLP) applications [8] [9]. Creating high-quality, responsible datasets for regional languages like Punjabi, Sindhi, and Balochi is essential for bridging the digital divide and ensuring that technology serves all communities [10] [11].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Ethics, Governance & Sovereign Infrastructure</h3>
                <p>As dependence on computing grows, computer scientists must consider the social consequences of their systems, including algorithmic bias, privacy, and accountability [12]. The integration of formal methods and software testing is critical for protecting digital identity and infrastructure. For the Orakzai community, building a **Sovereign Grid** means combining these technical disciplines with a commitment to data governance and ethical innovation, securing a future where technology respects cultural identity [13] [14].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Computer Science & The Future</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai computer scientist, code is the modern language of our resilience. We do not just study computation; we build the systems that protect our dignity and expand our reach. By mastering the hardware and software of 2026 while documenting our own languages and heritage, we are ensuring that our digital civilization remains sovereign and authentic. We are the architects of the logic that shapes tomorrow.”</p>
            </div>

            <div class="final-statement">
                CODE THE FUTURE.<br>
                BUILD TO ENDURE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Stanford HAI, <em>The 2026 AI Index Report: SWE-bench Verified and Organizational Adoption (2026)</em>.</li>
                    <li>HCL Software, <em>Tech Trends 2026: AI Agents and Self-Running Systems (2026)</em>.</li>
                    <li>IBM Think, <em>The Trends That Will Shape AI and Tech in 2026 (January 2026)</em>.</li>
                    <li>Deloitte Insights, <em>2026 Global Hardware and Consumer Tech Industry Outlook (February 2026)</em>.</li>
                    <li>Talent500, <em>AI and Tech in 2026: Specialized Hardware and Accelerators (February 2026)</em>.</li>
                    <li>Deloitte, <em>2026 Global Semiconductor Industry Outlook: Integrated Systems and Risk Mitigation (February 2026)</em>.</li>
                    <li>Semiconductor Industry Association, <em>The Growing Challenge of Semiconductor Design Leadership (2026)</em>.</li>
                    <li>arXiv, <em>A Release-Level Analysis of the Pashto Common Voice Corpus v24.0 (February 2026)</em>.</li>
                    <li>ResearchGate, <em>Natural Language Processing for Pashto: Challenges and Opportunities (February 2026)</em>.</li>
                    <li>Mendeley Data, <em>Bilingual Pashto Speech and Text Dataset (BPSTD) for Low-Resource Research (2026)</em>.</li>
                    <li>Linguist List, <em>LaTeLL 2026: Language Technologies for Low-resource Communities (November 2025)</em>.</li>
                    <li>Jama Software, <em>2026 Semiconductor Predictions: AI Chiplets and Sustainable Innovation (January 2026)</em>.</li>
                    <li>LinkedIn / yieldwerx, <em>Top 15 Semiconductor Industry Trends for 2026: Workload-specific NPUs (December 2025)</em>.</li>
                    <li>Orakzai Group Archives, <em>Sovereign Grid and Formal Verification Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            174
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

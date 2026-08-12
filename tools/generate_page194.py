from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-194-im-a-technologist-the-meaning-of-innovation.html'

GRAPHICS = [
    ("Technologist", "SELF", "↔", "TECH"),
    ("Tech as Tool", "TECH", "↔", "FIX"),
    ("Innovation Meaning", "NEW", "↔", "TRUE"),
    ("Invent vs Innov", "NEW", "≠", "DO"),
    ("Execution Rail", "IDEA", "→", "DONE"),
    ("Problem First", "WHY", "↔", "FIX"),
    ("Human-Centered", "SAFE", "↔", "LIFE"),
    ("Accessibility", "ALL", "↔", "SAFE"),
    ("Simplicity Rail", "SAFE", "↔", "DO"),
    ("Design & Eng", "SOUL", "↔", "GRID"),
    ("Computer Science", "CODE", "↔", "BASE"),
    ("Software Path", "CODE", "→", "DO"),
    ("Hardware Base", "PHYS", "↔", "BASE"),
    ("Network Rail", "LINK", "↔", "ALL"),
    ("Cloud Infra", "NET", "↔", "SAVE"),
    ("Data Importance", "DATA", "↔", "WISE"),
    ("Data Quality", "TRUE", "↔", "SAFE"),
    ("Algorithm Path", "RULE", "↔", "FIX"),
    ("AI Capability", "AI", "↔", "NEXT"),
    ("Machine Learn", "DATA", "→", "RULE"),
    ("Generative AI", "AI", "→", "NEW"),
    ("AI Limitations", "AI", "≠", "ALL"),
    ("Human Oversight", "WISE", "↔", "DO"),
    ("AI Literacy", "KNOW", "↔", "ABLE"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Security Design", "SEC", "↔", "DO"),
    ("Privacy Rail", "SAFE", "↔", "DATA"),
    ("Trust Base", "TRUE", "↔", "SAFE"),
    ("Reliability", "TRUE", "↔", "DO"),
    ("Resilience Rail", "FIX", "↔", "LONG"),
    ("Redundancy", "MANY", "↔", "SAFE"),
    ("Scalability", "ONE", "→", "ALL"),
    ("Performance", "FAST", "↔", "SAFE"),
    ("Efficiency Rail", "LESS", "→", "MORE"),
    ("Cost Sustainability", "CASH", "↔", "LONG"),
    ("Open Source", "OPEN", "↔", "ALL"),
    ("Collaboration", "MANY", "↔", "ONE"),
    ("Team Innovation", "ALL", "↔", "LINK"),
    ("Communication", "TALK", "↔", "TRUE"),
    ("Documentation", "TRUE", "↔", "LONG"),
    ("Testing Path", "TEST", "→", "SAFE"),
    ("Iteration Rail", "TRY", "→", "BEST"),
    ("Prototype Path", "TEST", "↔", "IDEA"),
    ("Experimentation", "WHY", "→", "FACT"),
    ("Failure Info", "FAIL", "→", "KNOW"),
    ("Scientific Think", "WHY", "↔", "FACT"),
    ("Evidence Base", "FACT", "↔", "TRUE"),
    ("Benchmark Rail", "TRUE", "↔", "FAST"),
    ("Metrics Path", "TRUE", "↔", "DO"),
    ("Society Change", "TECH", "↔", "ALL"),
    ("Edu Innovation", "LEAR", "↔", "TECH"),
    ("Health Innovation", "LIFE", "↔", "TECH"),
    ("Agri Innovation", "GROW", "↔", "TECH"),
    ("Fin Innovation", "CASH", "↔", "TECH"),
    ("Manu Innovation", "MAKE", "↔", "TECH"),
    ("Trans Innovation", "MOVE", "↔", "TECH"),
    ("Energy Innov", "POWER", "↔", "TECH"),
    ("Water Innov", "LIFE", "↔", "TECH"),
    ("Climate Innov", "SAFE", "↔", "TECH"),
    ("Gov Innovation", "RULE", "↔", "TECH"),
    ("Digital Identity", "SELF", "↔", "NET"),
    ("Blockchain Rail", "GRID", "↔", "TRUE"),
    ("Decentralization", "ALL", "↔", "FREE"),
    ("RRI Principles", "TRUE", "↔", "SAFE"),
    ("Change Fitness", "ABLE", "↔", "NEW"),
    ("Quantum Comm", "FAST", "↔", "SAFE"),
    ("Neurotech Rail", "MIND", "↔", "TECH"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g194-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g194-{index}-title g194-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g194-{index}-title">{safe}</title><desc id="g194-{index}-desc">An innovation relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g194-{index}-caption" class="diagram-caption">{index}. {safe} — Innovation relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">I’M A TECHNOLOGIST — The Meaning of Innovation Framework</title><desc id="hero-desc">A diagram showing the 2026 technology and innovation landscape, featuring Responsible Research and Innovation (RRI), AI Literacy, Change Fitness, and Quantum Communication.</desc><defs><linearGradient id="h194-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h194-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE INNOVATION IMPACT LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">RRI: RESPONSIBLE RESEARCH & INNOVATION (2026)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">AI LITERACY: BEYOND FLUENCY TO ETHICAL OVERSIGHT</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">CHANGE FITNESS: ADAPTING TO GEOPOLITICAL SHIFTS</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">QUANTUM COMMUNICATION & NEUROTECHNOLOGY</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">HUMAN-CENTRIC AI: FROM EXPERIMENT TO IMPACT</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: INNOVATION AS SERVICE</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">INNOVATION: CURIOSITY, ENGINEERING & RESPONSIBILITY</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">I’M A TECHNOLOGIST — THE MEANING OF INNOVATION</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Innovation as Curiosity, Engineering, Responsibility, and Progress: Built for Human Needs.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Innovation Impact Loop: Navigating the 2026 landscape where Responsible Research and Innovation (RRI), AI Literacy, and Change Fitness ensure that technological advances serve human needs and build a resilient digital civilization.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 194</title>
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
            <p class="section-label">PAGE 194</p>
            <h2>I’M A TECHNOLOGIST — THE MEANING OF INNOVATION</h2>
            <p>“Innovation as Curiosity, Engineering, Responsibility, and Progress.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “I’m a technologist. That does not simply mean that I use technology. It means that I choose to understand how technology works, what problems it can solve, where it can fail, and how it can affect people. Technology is not innovation by itself. Innovation begins with a problem, a question, or an opportunity to improve something. It requires curiosity, experimentation, engineering, persistence, and responsibility. To be a technologist is to become a builder, a learner, and a problem-solver.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Responsible Research & Innovation (RRI) (2026)</h3>
                <p>By 2026, the integration of **Responsible Research and Innovation (RRI)** principles has become standard in engineering and living labs [1]. RRI emphasizes that technological advances, from neurotechnology to AI, must serve human needs and undergo ethical oversight [2] [3]. Reclaiming RRI as a perspective commentary, experts highlight the importance of human-centered design in times of transformation, ensuring that disruptive technologies do not leave human beings behind [4] [5].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI Literacy & Ethical Engineering</h3>
                <p>AI literacy in 2026 extends beyond technical fluency; it refers to understanding how AI behaves in real workplace contexts and the critical ethics of source verification [6] [7]. For technologists, this means moving from copilots to **"vibe coding"** and elevating IT's role in organizational DNA [8]. Engineering leaders are adopting frameworks that balance trade-offs between speed, cost, and reliability, ensuring that AI is a true partner in research and infrastructure efficiency [9] [10].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Tech Trends 2026: From Experiment to Impact</h3>
                <p>Major reports from Deloitte, Globant, and Info-Tech reveal that successful organizations are moving from experimentation to **impact** in 2026 [11]. Top trends include **Quantum Communication**, Robotics, and the adoption of human-centric AI [12] [13]. Emerging technologies are being evaluated not just by their novelty, but by the problems they solve in sectors like healthcare, energy, and climate monitoring [14]. **"Change Fitness"** has become the key metric for adapting to geopolitical shifts and technological volatility [15].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Sovereignty & Sovereign Infrastructure</h3>
                <p>Technologists are increasingly focused on **digital sovereignty**—the technical capacity to understand and manage critical infrastructure [16]. For the Orakzai community, the **Sovereign Grid** represents innovation as a service, providing the physical and digital foundation for economic development [17]. By mastering computer science, cybersecurity, and data governance, we are ensuring that technology solves meaningful problems and builds a resilient digital civilization for the century that follows [18].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: I’m a Technologist — The Meaning of Innovation</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, technology is our tool, and innovation is our responsibility. We do not just consume systems; we build them. By mastering AI literacy and RRI principles while remaining rooted in our values of curiosity and persistence, we are ensuring that the Orakzai name is synonymous with progress and human-centered design. We are the architects of an innovation that is sovereign, ethical, and eternal. Our engineering is our service, and our curiosity is our strength.”</p>
            </div>

            <div class="final-statement">
                ENGINEER MEANING.<br>
                INNOVATE RESPONSIBLY.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>ScienceDirect, <em>Responsible Research and Innovation-Labs: Integration in Engineering (2026)</em>.</li>
                    <li>OECD, <em>Responsible Innovation in Neurotechnology: Serving Human Needs (2026)</em>.</li>
                    <li>Berlin Science Week, <em>Responsible Innovation in Times of Transformation: Rethinking Digital Care (2026)</em>.</li>
                    <li>Taylor & Francis Online, <em>Reclaiming 'Responsible Research and Innovation' as a Perspective (2026)</em>.</li>
                    <li>ScienceBusiness, <em>Harnessing Human-Centric Research and Innovation: Where AI Leaves Humans (2025-2026)</em>.</li>
                    <li>AI Literacy Day, <em>5 AI Literacy Trends Shaping Education and the Workforce in 2026 (March 2026)</em>.</li>
                    <li>LinkedIn / StrongYesMedia, <em>From AI Literacy to Ethics: The Skills Shaping Work in 2026 (December 2025)</em>.</li>
                    <li>Info-Tech Research Group, <em>AI Trends 2026: From Copilots to Vibe Coding (2026)</em>.</li>
                    <li>Waydev, <em>2026 Tech Trends: A Guide for Engineering Leaders and AI Governance (December 2025)</em>.</li>
                    <li>AI Literacy Institute, <em>AI Literacy Review: National Policy Framework for AI (April 2026)</em>.</li>
                    <li>Deloitte Insights, <em>Tech Trends 2026: Moving from Experimentation to Impact (December 2025)</em>.</li>
                    <li>Globant Reports, <em>Tech Trends 2026: 5 Forces Shaping the Future - Robotics and Quantum (2026)</em>.</li>
                    <li>Capgemini, <em>Top Tech Trends 2026: AI, Cloud, and Innovation Insights (2026)</em>.</li>
                    <li>World Economic Forum, <em>Top 10 Emerging Technologies 2026: 14th Annual Report (June 2026)</em>.</li>
                    <li>UNCTAD, <em>Technology and Innovation Report: Biennial Publication for Sustainability (2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>I’m a Technologist and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            194
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

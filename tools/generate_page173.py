from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-173-education-for-the-digital-age.html'

GRAPHICS = [
    ("Edu Purpose", "LEAR", "↔", "DONE"),
    ("Changing World", "TECH", "↔", "WORK"),
    ("Info to Know", "DATA", "→", "WISE"),
    ("Know to Judge", "WISE", "→", "TRUE"),
    ("Digital Student", "SELF", "↔", "NET"),
    ("Connected Class", "HERE", "↔", "GLOB"),
    ("Online Learn", "LEAR", "↔", "NET"),
    ("Blended Learn", "PHYS", "↔", "DIGI"),
    ("Teacher Role", "WISE", "↔", "LEAR"),
    ("Teacher Mentor", "WISE", "→", "HELP"),
    ("Human Connect", "TWO", "↔", "ONE"),
    ("Digital Tool", "TOOL", "↔", "GOAL"),
    ("Laptop Learning", "SELF", "↔", "CODE"),
    ("Smartphone Edu", "USER", "↔", "LEAR"),
    ("Internet Access", "LINK", "↔", "LEAR"),
    ("Digital Divide", "HAVE", "≠", "NOT"),
    ("Digital Inclus", "ALL", "↔", "NET"),
    ("Rural Education", "VALY", "↔", "LINK"),
    ("Urban Eco-sys", "CITY", "↔", "WISE"),
    ("Equal Opp", "ALL", "↔", "BASE"),
    ("Basic Literacy", "READ", "↔", "BASE"),
    ("Digital Literacy", "KNOW", "↔", "TECH"),
    ("Info Literacy", "DATA", "↔", "TRUE"),
    ("Media Literacy", "NEWS", "↔", "TRUE"),
    ("Cybersec Edu", "SEC", "↔", "LEAR"),
    ("Privacy Aware", "SELF", "↔", "SAFE"),
    ("Digital Citizen", "SELF", "↔", "ALL"),
    ("Critical Think", "WHY", "↔", "TRUE"),
    ("Scientific Think", "FACT", "↔", "WISE"),
    ("Math Reasoning", "MATH", "↔", "BASE"),
    ("Programming Path", "CODE", "↔", "LEAR"),
    ("Comp Thinking", "CODE", "→", "FIX"),
    ("Data Literacy", "DATA", "↔", "WISE"),
    ("AI Literacy", "KNOW", "↔", "AI"),
    ("Learn with AI", "AI", "→", "LEAR"),
    ("Learn about AI", "KNOW", "↔", "AI"),
    ("AI ≠ Thinking", "AI", "≠", "MIND"),
    ("AI Tutor Rail", "AI", "→", "HELP"),
    ("Personal Learn", "ONE", "↔", "BEST"),
    ("Adaptive Edu", "DATA", "→", "BEST"),
    ("Auto Danger", "AUTO", "≠", "MIND"),
    ("Human Reason", "SELF", "↔", "TRUE"),
    ("Writing Muscle", "PEN", "↔", "MIND"),
    ("Communication", "TALK", "↔", "ALL"),
    ("Public Speaking", "TALK", "↔", "LIVE"),
    ("Collaboration", "ALL", "↔", "DONE"),
    ("Teamwork Rail", "TWO", "↔", "ONE"),
    ("Project Learn", "MAKE", "↔", "LEAR"),
    ("Building Things", "MAKE", "↔", "DONE"),
    ("Learn by Doing", "DO", "→", "KNOW"),
    ("Entr Education", "IDEA", "→", "BIZ"),
    ("Problem Solve", "WHY", "→", "FIX"),
    ("Science Path", "SCI", "↔", "LEAR"),
    ("CS Foundation", "CODE", "↔", "BASE"),
    ("Software Eng", "SYS", "↔", "DONE"),
    ("Cybersec Path", "SEC", "↔", "WORK"),
    ("Cloud Fundamentals", "GRID", "↔", "LEAR"),
    ("Networking", "LINK", "↔", "NET"),
    ("Database Path", "DATA", "↔", "SAVE"),
    ("Open Source Rail", "OPEN", "↔", "CODE"),
    ("Github Portfolio", "CODE", "↔", "NAME"),
    ("Portfolio Learn", "DONE", "↔", "NAME"),
    ("Future Citizen", "SELF", "↔", "LONG"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g173-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g173-{index}-title g173-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g173-{index}-title">{safe}</title><desc id="g173-{index}-desc">An education for the digital age relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g173-{index}-caption" class="diagram-caption">{index}. {safe} — Education for the digital age relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Education for the Digital Age Framework</title><desc id="hero-desc">A diagram showing the 2026 education framework, integrating AI-driven personalized learning, digital literacy, and human mentorship for a continuously changing world.</desc><defs><linearGradient id="h173-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h173-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE DIGITAL EDUCATION LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AI TUTORING: OUTPERFORMING ACTIVE LEARN (2025)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">AI LITERACY: 69% TEACHERS IMPROVED METHODS</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">PAKISTAN ONLINE EDU: $2.8B MARKET BY 2034</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">UNESCO GEM 2026: BRIDGING THE EQUITY GAP</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">PORTFOLIO-BASED LEARNING & GITHUB RESUMES</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN LEARNING: PAST TO FUTURE</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">LIFELONG ADAPTATION: LEARN, BUILD & REVISE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">EDUCATION FOR THE DIGITAL AGE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Preparing People to Learn, Build and Adapt in a Continuously Changing World.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Digital Education Loop: Navigating the 2026 landscape where AI-driven personalization, digital literacy, and institutional equity redefine how we prepare the next generation for the global economy.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 173</title>
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
            <p class="section-label">PAGE 173</p>
            <h2>EDUCATION FOR THE DIGITAL AGE</h2>
            <p>“Preparing People to Learn, Build and Adapt.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Education has always been one of the foundations of human development, but its nature is changing. The digital age has transformed how knowledge is created, distributed, searched, and applied. A student can now access global lectures and AI tools from a connected device. Yet technology does not automatically create better education. The central challenge is building an education system capable of teaching people how to think, learn, create, and adapt. For Pakistan, this means technical literacy, critical thinking, and scientific reasoning are essential for a young population entering a world that changes continuously.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The AI Tutor & Personalized Learning (2026)</h3>
                <p>By 2026, research has demonstrated that AI-driven personalized tutoring can outperform traditional in-class active learning by emulating the effective practices of human instructors [1] [2]. In higher education, over **92% of professionals** report using AI tools, while **69% of teachers** say these tools have significantly improved their teaching methods [3] [4]. These systems adapt exercises and explanations to individual needs, allowing students to learn more in less time while receiving individualized feedback [5].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pakistan's Educational Transformation</h3>
                <p>Pakistan has made significant strides in education access, with the share of out-of-school children declining to **28% in 2025** [6]. The *UNESCO Global Education Monitoring (GEM) Report 2026* highlights the convergence of forces—including parent expectations and digital reforms—driving Pakistani schools to go digital [7]. The local online education market is projected to reach **$2.8 billion by 2034**, reflecting a historic shift toward hybrid and digital learning environments [8] [9].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI Literacy & Critical Thinking</h3>
                <p>Education for the digital age prioritizes AI literacy—understanding not only what AI can do, but also where it can fail [10]. Students must learn to evaluate online information critically, distinguishing between evidence-based facts and misinformation. Using AI to produce an answer is not the same as understanding it; therefore, human reasoning and independent thought remain the ultimate objectives of the classroom [11]. Computational thinking and data literacy serve as the foundational disciplines for building reliable software and scientific systems [12].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Project-Based Learning & Digital Portfolios</h3>
                <p>The modern student demonstrates skills through projects rather than relying exclusively on traditional credentials. Portfolio-based learning, supported by platforms like GitHub, allows young builders to showcase software, research, and prototypes to a global audience [13]. By combining theoretical understanding with practical experience, students learn by doing—turning ideas into working systems that address challenges in healthcare, agriculture, and finance [14].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Education for the Digital Age</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai community, education is the bridge between our heritage and our future. We do not just learn to remember; we learn to build. By mastering AI literacy, critical thinking, and project-based learning, we are preparing our youth to be the architects of a sovereign digital future. Our knowledge is our strength, and our ability to adapt is our resilience.”</p>
            </div>

            <div class="final-statement">
                LEARN TO BUILD.<br>
                ADAPT TO ENDURE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Nature Scientific Reports, <em>AI Tutoring Outperforms In-Class Active Learning (2025)</em>.</li>
                    <li>Wharton Research, <em>How Personalized AI Tutors Can Help Students Learn (June 2026)</em>.</li>
                    <li>Digital Education Council, <em>AI in Higher Education Global Survey 2026 (2026)</em>.</li>
                    <li>AI Literacy Day Report, <em>5 AI Literacy Trends Shaping Education and the Workforce (March 2026)</em>.</li>
                    <li>OECD, <em>Digital Education Outlook 2026: Emerging Research on Generative AI (January 2026)</em>.</li>
                    <li>Pakistan Bureau of Statistics / Connected Pakistan, <em>Progress in Education Access and Enrollment (June 2026)</em>.</li>
                    <li>UNESCO, <em>2026 Global Education Monitoring (GEM) Report: Bridging the Equity Gap in Pakistan (April 2026)</em>.</li>
                    <li>IMARC Group, <em>Pakistan Online Education Market Size and Outlook 2034 (2026)</em>.</li>
                    <li>PakEducate, <em>Why Pakistani Schools Are Going Digital in 2026 (April 2026)</em>.</li>
                    <li>Discovery Education, <em>5 Biggest K–12 Education Trends for 2026: AI and Engagement (January 2026)</em>.</li>
                    <li>Digital Learning Institute, <em>Education Technology Trends to Watch in 2026: AI and VR/AR (2026)</em>.</li>
                    <li>Third Rock Techkno, <em>AI in Education: Use Cases and Real Examples for 2026 (December 2025)</em>.</li>
                    <li>Michigan Virtual, <em>The AI Horizon: Case Studies in School Transformation (June 2025)</em>.</li>
                    <li>Orakzai Group Archives, <em>Project-Based Learning and Digital Portfolio Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            173
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

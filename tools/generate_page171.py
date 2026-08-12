from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-171-my-generation.html'

GRAPHICS = [
    ("Born Into Change", "BORN", "↔", "TIME"),
    ("Digital Gen", "SELF", "↔", "NET"),
    ("Connected World", "HERE", "↔", "GLOB"),
    ("Consumer Creator", "BUY", "→", "MAKE"),
    ("Smartphone Power", "SELF", "↔", "TOOL"),
    ("Internet Classroom", "LEAR", "↔", "NET"),
    ("Self-Education", "SELF", "→", "KNOW"),
    ("Global Learning", "LEAR", "↔", "GLOB"),
    ("Open Knowledge", "OPEN", "↔", "WISE"),
    ("Info Evaluation", "DATA", "→", "TRUE"),
    ("Critical Thinking", "WHY", "↔", "FACT"),
    ("Misinformation", "FALSE", "≠", "TRUE"),
    ("Digital Resp", "SELF", "↔", "TRUE"),
    ("Social Media", "TALK", "↔", "ALL"),
    ("Attention Econ", "EYE", "↔", "CASH"),
    ("Digital Well-being", "SELF", "↔", "TIME"),
    ("Online Identity", "SELF", "↔", "NAME"),
    ("Digital Rep", "NAME", "↔", "LONG"),
    ("Prof Identity", "SELF", "↔", "WORK"),
    ("Global Network", "LINK", "↔", "ALL"),
    ("Global Job Mkt", "WORK", "↔", "GLOB"),
    ("Remote Work", "HERE", "↔", "TEAM"),
    ("Freelancing Path", "ONE", "→", "CASH"),
    ("Digital Exports", "CODE", "→", "GLOB"),
    ("Pakistani Youth", "HOME", "↔", "YOUN"),
    ("Future Capacity", "LEAR", "→", "GROW"),
    ("Digital Divide", "HAVE", "≠", "NOT"),
    ("Rural Inclusion", "VALY", "↔", "NET"),
    ("Broad Partic", "ALL", "↔", "DONE"),
    ("Education First", "LEAR", "↔", "BASE"),
    ("Future Classroom", "LEAR", "↔", "TECH"),
    ("AI Learning Tool", "AI", "→", "LEAR"),
    ("AI Literacy", "KNOW", "↔", "AI"),
    ("Question AI", "WHY", "↔", "AI"),
    ("AI and Work", "AI", "↔", "WORK"),
    ("Reskilling Path", "LEAR", "→", "WORK"),
    ("Lifelong Learn", "TIME", "↔", "LEAR"),
    ("Low-Cost Startup", "LOW", "↔", "START"),
    ("Laptop Workshop", "SELF", "↔", "DONE"),
    ("Build Pakistan", "HOME", "↔", "MAKE"),
    ("Global Ambition", "IDEA", "↔", "GLOB"),
    ("Local Problem", "HERE", "→", "FIX"),
    ("Build for World", "HERE", "→", "GLOB"),
    ("Software Power", "CODE", "↔", "MANY"),
    ("AI Capability", "AI", "↔", "SELF"),
    ("Blockchain Framework", "BC", "↔", "OWN"),
    ("Digital Finance", "CASH", "↔", "NET"),
    ("Digital Commerce", "BUY", "↔", "SELL"),
    ("Creator Economy", "MAKE", "↔", "MANY"),
    ("Knowledge Creator", "WISE", "↔", "ALL"),
    ("Open Source", "OPEN", "↔", "CODE"),
    ("Global Collab", "ALL", "↔", "LINK"),
    ("Science Access", "SCI", "↔", "NET"),
    ("Young Researcher", "SELF", "↔", "SCI"),
    ("Foundational CS", "CODE", "↔", "BASE"),
    ("Data Centrality", "DATA", "↔", "ALL"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Digital Privacy", "SELF", "↔", "SAFE"),
    ("Digital Identity", "SELF", "↔", "NAME"),
    ("Digital Rights", "OWN", "↔", "DATA"),
    ("AI Governance", "RULE", "↔", "AI"),
    ("Orakzai Future", "ORAK", "↔", "TIME"),
    ("Future Builder", "SELF", "↔", "INNO"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g171-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g171-{index}-title g171-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g171-{index}-title">{safe}</title><desc id="g171-{index}-desc">A "My Generation" relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g171-{index}-caption" class="diagram-caption">{index}. {safe} — "My Generation" relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">My Generation Framework</title><desc id="hero-desc">A diagram showing the 2026 digital generation's pathway from being consumers to creators, navigating AI, global connectivity, and lifelong learning.</desc><defs><linearGradient id="h171-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h171-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE DIGITAL GENERATION LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">CONSUMER → CREATOR: $33T POTENTIAL (2030)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">GEN ALPHA RISE: OLDEST TURN 16 IN 2026</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AI RESHAPING 55% OF JOBS (2026-2028)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">PAKISTAN YOUTH: 800K+ ON DIGITAL HUB</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">LIFELONG LEARNING & AI LITERACY (JFF 2026)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN FUTURE: BORN INTO CHANGE</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">BUILDING THE FUTURE: OPPORTUNITY & RESP</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">MY GENERATION</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“A Generation Growing Up Between Two Worlds, Inheriting and Building.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Digital Generation Loop: Navigating the 2026 digital era where Gen Z and Gen Alpha transition from consumers to creators, leveraging AI and global networks while maintaining digital responsibility.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 171</title>
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
            <p class="section-label">PAGE 171</p>
            <h2>MY GENERATION</h2>
            <p>“A Generation Growing Up Between Two Worlds.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Every generation inherits a different world. My generation has grown up during a period in which smartphones, social media, cloud computing, artificial intelligence, digital finance and global connectivity have become part of everyday life. We are among the first generations to experience a world where a person can learn from a university thousands of kilometres away, collaborate with people on another continent, build software from a laptop and launch a digital product to a global audience. But this generation also inherits difficult challenges: economic uncertainty, misinformation, and rapidly changing employment. My generation is not only inheriting the future. We are beginning to build it.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Digital Generation (2026)</h3>
                <p>By 2026, the oldest members of Gen Alpha have turned 16, already steering spending decisions and making their presence felt across screens and society [1]. Gen Z's global earning potential is estimated to reach **$33 trillion by 2030**, reflecting a historic shift from being mere consumers to powerful creators [2]. In Pakistan, the *Digital Youth Hub* has surpassed **800,000 registered users**, connecting a massive young population with opportunities in jobs, education, and entrepreneurship [3] [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI, Work & Lifelong Learning</h3>
                <p>Artificial Intelligence is reshaped more jobs than it replaces, with **55% of jobs** in major economies expected to be transformed by 2028 [5]. Entry-level workers are moving into complex tasks earlier, requiring a focus on AI literacy and critical thinking from the earliest stages of their careers [6]. By 2026, education has transitioned into a continuous process of reskilling and lifelong learning, where AI serves as a personalized learning tool rather than a replacement for independent thought [7] [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Responsibility & Trust</h3>
                <p>Living in the "Attention Economy" requires a new set of digital muscles. My generation must navigate misinformation, privacy concerns, and the challenges of online identity [9]. Verification and digital well-being have become essential skills as digital platforms compete for human attention. Understanding data rights and AI governance is critical for ensuring that technology supports human needs rather than treating people merely as data points [10] [11].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Building from Pakistan to the World</h3>
                <p>A laptop has become a development environment, design studio, and business office, allowing young Orakzai founders to serve global customers without leaving their homes [12]. By contributing to open-source software and participating in global professional networks, Pakistani youth are generating international revenue through digital exports [13]. Ambition no longer requires cultural disappearance; instead, it allows for a sovereign future where local background coexists with global technological ambition [14].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: My Generation</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai youth, being born into change is our greatest advantage. We do not fear the digital future; we are its architects. By combining our heritage with AI literacy and global connectivity, we are building a sovereign legacy that is authentic and innovative. We are the generation that turns uncertainty into opportunity and responsibility into progress.”</p>
            </div>

            <div class="final-statement">
                BORN INTO CHANGE.<br>
                BUILDING THE FUTURE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>LinkedIn / MBA Group, <em>The Rise of Gen Alpha in 2026: Oldest Turn 16 (February 2026)</em>.</li>
                    <li>Mastercard News, <em>How Gen Z and Gen Alpha are Building Today's Culture: $33T Potential (February 2026)</em>.</li>
                    <li>Prime Minister's Youth Programme, <em>Digital Youth Hub Milestones and IT Training Collaboration (July 2026)</em>.</li>
                    <li>Pakistan PID, <em>Youth Enterprise Financing and Digital Hub Milestone (May 2026)</em>.</li>
                    <li>BCG Publications, <em>AI Will Reshape More Jobs Than It Replaces: 2026-2028 Projections (April 2026)</em>.</li>
                    <li>World Economic Forum, <em>Artificial Intelligence and the Future of Entry-Level Work (2026)</em>.</li>
                    <li>JFF Survey, <em>AI for Workers and Learners 2026: Real Work Ahead (2026)</em>.</li>
                    <li>Educause Research, <em>The Impact of AI on Work in Higher Education (January 2026)</em>.</li>
                    <li>The Social Juice, <em>Gen-Z Stats and Diverging Trends in 2026 (January 2026)</em>.</li>
                    <li>House of Communication, <em>Next Gen Signals: Five Trends Reshaping Gen Z and Alpha (April 2026)</em>.</li>
                    <li>GWI Blog, <em>7 Gen Alpha Characteristics to Know for 2026 (2026)</em>.</li>
                    <li>EMARKETER, <em>FAQ on Gen Alpha: Reaching the Digital Gaming Generation in 2026 (February 2026)</em>.</li>
                    <li>LinkedIn / Asma Mohsin, <em>Pakistan Youth Development Index 2026: Skills for the Future (February 2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Youth Entrepreneurship and Global Digital Ambition (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            171
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

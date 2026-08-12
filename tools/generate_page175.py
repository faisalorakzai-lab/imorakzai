from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-175-ai-native-generations.html'

GRAPHICS = [
    ("AI-Native Gen", "BORN", "↔", "AI"),
    ("Intelligent Soft", "APP", "↔", "WISE"),
    ("Generational Shift", "PAST", "→", "NEW"),
    ("AI Infrastructure", "GRID", "↔", "ALL"),
    ("Embedded AI", "SOFT", "↔", "AI"),
    ("AI Search Rail", "FIND", "↔", "AI"),
    ("AI Productivity", "WORK", "↔", "AI"),
    ("AI Finance Rail", "CASH", "↔", "AI"),
    ("AI Health Rail", "DOC", "↔", "AI"),
    ("AI Commerce", "BUY", "↔", "AI"),
    ("AI Comm Rail", "TALK", "↔", "AI"),
    ("Digital Env", "SELF", "↔", "NET"),
    ("AI Not Magic", "MATH", "↔", "CODE"),
    ("AI Dependency", "DATA", "↔", "GRID"),
    ("AI Literacy", "KNOW", "↔", "AI"),
    ("Prompt Skill", "TALK", "→", "AI"),
    ("Verification Rail", "CHECK", "↔", "TRUE"),
    ("Critical Thinking", "WHY", "↔", "FACT"),
    ("Human Judgment", "SELF", "↔", "WISE"),
    ("AI Education", "LEAR", "↔", "AI"),
    ("AI Tutor Path", "AI", "→", "HELP"),
    ("Personalized Learn", "ONE", "↔", "BEST"),
    ("Educational Access", "ALL", "↔", "WISE"),
    ("Digital Divide", "HAVE", "≠", "NOT"),
    ("AI Access Pak", "HOME", "↔", "AI"),
    ("Pak Youth Potential", "YOUN", "↔", "GROW"),
    ("Local Language AI", "LANG", "↔", "AI"),
    ("Urdu AI Support", "URDU", "↔", "AI"),
    ("Regional Lang AI", "TALK", "↔", "AI"),
    ("Cultural Context", "HOME", "↔", "WISE"),
    ("Local Data Rail", "HERE", "↔", "DATA"),
    ("Data Resp", "SAFE", "↔", "DATA"),
    ("Privacy Consent", "SELF", "↔", "YES"),
    ("AI Creativity", "MAKE", "↔", "AI"),
    ("AI Collaborator", "TWO", "↔", "ONE"),
    ("Writing with AI", "PEN", "↔", "AI"),
    ("Design with AI", "ART", "↔", "AI"),
    ("Music Audio AI", "SONG", "↔", "AI"),
    ("Video Gen AI", "FILM", "↔", "AI"),
    ("Creator Economy", "MAKE", "↔", "ALL"),
    ("Quality Value", "BEST", "↔", "CASH"),
    ("AI Originality", "SELF", "≠", "AUTO"),
    ("AI Programming", "CODE", "↔", "AI"),
    ("Explain Code", "WHY", "↔", "CODE"),
    ("Identify Errors", "FIX", "↔", "CODE"),
    ("System Builder", "PLAN", "↔", "DONE"),
    ("AI Assisted Dev", "TEAM", "↔", "AI"),
    ("AI Agents", "AUTO", "↔", "GOAL"),
    ("Agent Reliability", "TRUE", "↔", "AUTO"),
    ("Human Oversight", "USER", "↔", "AI"),
    ("AI Entr", "IDEA", "↔", "AI"),
    ("One-Person Biz", "ONE", "↔", "ALL"),
    ("AI Prototyping", "FAST", "↔", "MAKE"),
    ("Market Research", "FIND", "↔", "DATA"),
    ("Business Auto", "AUTO", "↔", "BIZ"),
    ("AI-Native Co", "AI", "↔", "BASE"),
    ("Founder Skills", "WISE", "↔", "ALL"),
    ("Pak AI Founders", "HOME", "→", "GLOB"),
    ("Global Digital", "HERE", "→", "GLOB"),
    ("Local Problem", "HERE", "→", "FIX"),
    ("Agri AI Path", "FARM", "↔", "AI"),
    ("Health Image AI", "EYE", "↔", "DOC"),
    ("Fin Fraud AI", "SEC", "↔", "CASH"),
    ("Gov Admin AI", "RULE", "↔", "AI"),
    ("Legal Research AI", "LAW", "↔", "AI"),
    ("Sci Discovery AI", "SCI", "↔", "AI"),
    ("Eng Simulation", "MAKE", "↔", "AI"),
    ("Robotics AI", "BOT", "↔", "AI"),
    ("Autonomous Sys", "SELF", "↔", "MOVE"),
    ("Physical AI", "PHYS", "↔", "AI"),
    ("Edge AI Rail", "HERE", "↔", "AI"),
    ("Cloud Compute", "GRID", "↔", "AI"),
    ("GPU Parallel", "MANY", "↔", "FAST"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g175-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g175-{index}-title g175-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g175-{index}-title">{safe}</title><desc id="g175-{index}-desc">An AI-native generation relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g175-{index}-caption" class="diagram-caption">{index}. {safe} — AI-native generation relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">AI-Native Generations Framework</title><desc id="hero-desc">A diagram showing the 2026 AI-native landscape, featuring Gen Alpha's co-pilot culture, the shift to one-person startups, and the integration of AI agents into global digital civilization.</desc><defs><linearGradient id="h175-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h175-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE AI-NATIVE GENERATION LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">GEN ALPHA: FIRST AI-NATIVE CO-PILOT CULTURE</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">POPULATION ADOPTION: 53% REACHED BY 2026</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ONE-PERSON STARTUPS: AI AGENTS REPLACING TEAMS</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AGENTIC WORKFLOWS: 40% OF APPS EMBEDDED BY 2026</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">URDU & PASHTO AI: LOCAL CONTEXT & SOVEREIGN DATA</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: AI INFRA & IDENTITY</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">LITERACY TO CAPABILITY: RESPONSIBLE CREATION</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">AI-NATIVE GENERATIONS</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Growing Up in the Age of Artificial Intelligence: From Consumption to Creation.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The AI-Native Generation Loop: Navigating the 2026 landscape where Gen Alpha and Gen Z transition from AI users to AI architects, leveraging agentic workflows and local-language models to build a sovereign digital future.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 175</title>
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
            <p class="section-label">PAGE 175</p>
            <h2>AI-NATIVE GENERATIONS</h2>
            <p>“Growing Up in the Age of Artificial Intelligence.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Every generation grows up surrounded by technologies that previous generations experienced as new. For today's young people, artificial intelligence is becoming part of the environment in which they learn, communicate, create and work. An AI-native generation is not simply a generation that uses AI; it is a generation that grows up expecting intelligent software to exist. For young Pakistanis, this transformation could influence every aspect of life. The central challenge is to move from AI consumption to AI literacy, from AI literacy to AI capability, and from capability to responsible creation.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Gen Alpha: The First AI-Native Generation (2026)</h3>
                <p>By 2026, **Generation Alpha** has emerged as the first truly AI-native generation, using AI chatbots as "co-pilots for life choices" [1]. Generative AI adoption reached **53% of the population** within just three years—a pace faster than the personal computer or the internet [2]. For these young people, AI isn't cutting-edge; it's commonplace, embedded in everything from search engines and productivity software to healthcare and finance [3]. Nearly half of Gen Alpha students already use AI for information gathering and schoolwork, redefining their academic performance and creativity [4] [5].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI Agents & The One-Person Startup</h3>
                <p>The year 2026 marks the rise of **Agentic Workflows**, with 40% of enterprise applications featuring embedded AI agents capable of working for hours without interruption [6] [7]. This shift is transforming the economy, making "one-person companies" increasingly viable as AI agents replace traditional teams in areas like market research, customer service, and business automation [8] [9]. For the young Orakzai entrepreneur, AI reduces the cost of experimentation and prototyping, allowing small teams to build global-scale products from a local foundation [10].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI Literacy & Local Language Resources</h3>
                <p>Realizing the AI opportunity in Pakistan requires more than just access; it requires AI literacy—understanding what these systems can do and where they can fail [11]. Improving datasets for **Urdu, Pashto, Punjabi**, and other regional languages is essential for creating AI that understands local cultural contexts [12]. By 2026, AI literacy frameworks are being integrated into education to help students move from prompting to verification and critical thinking, ensuring that human judgment remains the final authority in a world of automated content [13] [14].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Physical AI & The Future of Discovery</h3>
                <p>The next phase of AI connects software intelligence with the physical world through robotics, autonomous systems, and **Edge AI** [15]. In fields like agriculture, Image analysis and disease detection are optimizing resource use, while in science, AI helps researchers identify patterns in massive datasets to accelerate discovery [16]. For the AI-native generation, these tools are not a replacement for scientific reasoning or engineering skills, but a powerful collaborator for building a sovereign and innovative future [17].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: AI-Native Generations</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai youth, being AI-native is a new dimension of our tribal resilience. We do not just inherit the tools of the digital age; we master the logic behind them. By building AI that speaks our languages and respects our values, we are ensuring that our digital future remains sovereign. We are not just users of AI; we are its architects, turning intelligence into impact for our community and the world.”</p>
            </div>

            <div class="final-statement">
                LITERACY TO IMPACT.<br>
                BUILDING SOVEREIGN AI.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Mastercard News, <em>Gen Z and Gen Alpha Shift from Scrolling to Shaping Culture: AI Co-pilots (February 2026)</em>.</li>
                    <li>Stanford HAI, <em>The 2026 AI Index Report: Population Adoption and Benchmarks (2026)</em>.</li>
                    <li>Attest Research, <em>US Gen Alpha Report: AI as Commonplace and Embedded (2026)</em>.</li>
                    <li>Taylor & Francis Online, <em>Bridging Gen Alpha's Digital Habits with AI in Education (2026)</em>.</li>
                    <li>Greenbook Insights, <em>Gen Alpha vs Gen Z: Two Generations, Two Consumer Playbooks (October 2025)</em>.</li>
                    <li>PwC, <em>2026 AI Business Predictions: Agentic Workflows and Responsible Innovation (2026)</em>.</li>
                    <li>MindStudio Blog, <em>The Future of AI Agents: Trends and Interruption-Free Operations (January 2026)</em>.</li>
                    <li>Taskade Blog, <em>One-Person Company Software: AI Agents Replacing Teams (March 2026)</em>.</li>
                    <li>BCG Capabilities, <em>AI Agents: What They Are and Their Business Impact (2026)</em>.</li>
                    <li>MJV Innovation, <em>The Gen Alpha-Gen Z Continuity: Youth Strategy in 2026 (June 2026)</em>.</li>
                    <li>Digital Education Council, <em>AI in Higher Education Global Survey 2026 (2026)</em>.</li>
                    <li>ScienceDirect, <em>Enhancing AI Literacy for Educators: Frameworks and Outcomes (2026)</em>.</li>
                    <li>AI Literacy Institute, <em>AI Literacy Review: 40 Frameworks and Expert Interviews (May 2026)</em>.</li>
                    <li>California Dept of Education, <em>AI Literacy: Knowledge, Skills, and Attitudes for the Future (2026)</em>.</li>
                    <li>Deloitte Insights, <em>2026 Global Hardware and Consumer Tech Industry Outlook: AI Reigniting Growth (February 2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>AI-Native Generation and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                    <li>Growing Up in the Digital Age Summit, <em>Collaborating to Protect and Empower AI-Native Youth (2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            175
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

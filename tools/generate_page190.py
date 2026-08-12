from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-190-a-message-to-the-next-generation.html'

GRAPHICS = [
    ("Next Gen Message", "PAST", "↔", "NEXT"),
    ("Learn Path", "LEAR", "→", "WISE"),
    ("Build Rail", "MAKE", "↔", "DO"),
    ("Preserve Base", "SAVE", "↔", "LONG"),
    ("Serve Path", "HELP", "↔", "TRUE"),
    ("Imagine Rail", "MIND", "↔", "NEW"),
    ("Inherit World", "PAST", "→", "NOW"),
    ("Inherit Opp", "OPEN", "↔", "NEXT"),
    ("Inherit Prob", "FIX", "↔", "NEXT"),
    ("Unfinished Work", "DO", "↔", "NEXT"),
    ("Uncertainty Rail", "WHY", "↔", "NEW"),
    ("Build Better", "OLD", "→", "BEST"),
    ("Not Zero Base", "BASE", "↔", "GROW"),
    ("Study Knowledge", "LEAR", "↔", "WISE"),
    ("Question All", "WHY", "↔", "TRUE"),
    ("Lifelong Learn", "TIME", "↔", "LEAR"),
    ("Learn How Think", "RULE", "↔", "FIX"),
    ("Analyze Evidence", "FACT", "↔", "TRUE"),
    ("Verify Info", "TRUE", "↔", "SAFE"),
    ("Read Widely", "BOOK", "↔", "ALL"),
    ("Understand Hist", "PAST", "↔", "WISE"),
    ("Learn Mistakes", "FAIL", "→", "WISE"),
    ("Respect Know", "TRUE", "↔", "BASE"),
    ("Consumer to Bld", "BUY", "→", "MAKE"),
    ("Start Small", "ONE", "→", "MANY"),
    ("Experiment Rail", "TEST", "→", "LEAR"),
    ("Accept Failure", "FAIL", "→", "WISE"),
    ("Develop Skills", "ABLE", "↔", "DONE"),
    ("CS Foundation", "CODE", "↔", "BASE"),
    ("Prog Logic", "RULE", "↔", "FIX"),
    ("AI Partnership", "AI", "↔", "HELP"),
    ("AI Limits Rail", "AI", "≠", "ALL"),
    ("Resp Tech Use", "TRUE", "↔", "SAFE"),
    ("Tech as Tool", "TECH", "↔", "FIX"),
    ("Build Respons", "IDEA", "↔", "SAFE"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Privacy Path", "SAFE", "↔", "DATA"),
    ("Digital Resp", "YES", "↔", "SAFE"),
    ("Human Judgment", "WISE", "↔", "DO"),
    ("Own Thinking", "SELF", "↔", "TRUE"),
    ("Build Purpose", "WHY", "↔", "HELP"),
    ("Entrepreneurship", "IDEA", "→", "BIZ"),
    ("Calculated Risk", "SAFE", "↔", "DO"),
    ("Build Trust", "TRUE", "↔", "SAFE"),
    ("Keep Your Word", "YES", "↔", "TRUE"),
    ("No Status Chase", "NAME", "≠", "LONG"),
    ("Create Opp", "OPEN", "↔", "ALL"),
    ("Teach Others", "WISE", "→", "LEAR"),
    ("Mentorship Rail", "WISE", "→", "YOUN"),
    ("Build Networks", "ALL", "↔", "LINK"),
    ("Find Good People", "SELF", "↔", "LINK"),
    ("Collaborate Path", "MANY", "↔", "ONE"),
    ("Respect Diff", "MANY", "↔", "TRUE"),
    ("Build Bridges", "HERE", "↔", "GLOB"),
    ("Think Globally", "ALL", "↔", "NET"),
    ("Stay Connected", "GLOB", "↔", "HOME"),
    ("Remember Roots", "PAST", "↔", "SELF"),
    ("Not Museum Cult", "PAST", "→", "NEW"),
    ("Preserve Matter", "SAVE", "↔", "TRUE"),
    ("Question Change", "WHY", "↔", "NEW"),
    ("Balance Rail", "SAVE", "↔", "GROW"),
    ("Pashto Legacy", "PASH", "↔", "LONG"),
    ("Listen Elders", "WISE", "→", "LEAR"),
    ("Oral Hist Path", "TALK", "→", "SAVE"),
    ("Respect Generation", "OLD", "↔", "YOUN"),
    ("Bridge Gen", "PAST", "↔", "NEXT"),
    ("Change Fitness", "ABLE", "↔", "NEW"),
    ("Youth Progress", "YOUN", "→", "GROW"),
    ("AI Co-Pilot", "AI", "↔", "DO"),
    ("Culture Shapers", "YOUN", "→", "NEW"),
    ("Digital Ubuntu", "ALL", "↔", "LINK"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g190-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g190-{index}-title g190-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g190-{index}-title">{safe}</title><desc id="g190-{index}-desc">A message relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g190-{index}-caption" class="diagram-caption">{index}. {safe} — Next generation relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">A Message to the Next Generation Framework</title><desc id="hero-desc">A diagram showing the 2026 youth leadership and empowerment landscape, featuring the UNESCO 2026 Youth Report, the $98.7B leadership development market, and the "Human-Centered Leadership" model.</desc><defs><linearGradient id="h190-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h190-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE NEXT GENERATION LEADERSHIP LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">UNESCO 2026 YOUTH REPORT: LEAD WITH YOUTH</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">LEADERSHIP MARKET: $98.7B IN 2026 (10% CAGR)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">UN YOUTH2030: MEANINGFUL YOUTH PARTICIPATION</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">HUMAN-CENTERED LEADERSHIP: AI AS A PARTNER</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CHANGE FITNESS: BALANCING TRADE-OFFS (HBS 2026)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: KNOWLEDGE & CHARACTER</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">MISSION: LEARN, BUILD, PRESERVE, SERVE, IMAGINE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">A MESSAGE TO THE NEXT GENERATION</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Learn. Build. Preserve. Serve. Imagine. Your responsibility is to build something better.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Next Generation Leadership Loop: Navigating the 2026 landscape where youth-led dissemination, human-centered leadership, and "change fitness" ensure that the generation inheriting the world is prepared to lead with wisdom and purpose.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 190</title>
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
            <p class="section-label">PAGE 190</p>
            <h2>A MESSAGE TO THE NEXT GENERATION</h2>
            <p>“Learn. Build. Preserve. Serve. Imagine.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “To the generation that comes next: You will inherit a world you did not create. You will inherit its opportunities and its problems. Your responsibility is not to reproduce the past exactly; your responsibility is to understand it, learn from it, and build something better. Do not be afraid of uncertainty. Every generation faces a future that previous generations could not completely predict. Learn. Build. Preserve. Serve. Imagine.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Lead with Youth & Meaningful Participation (2026)</h3>
                <p>By 2026, global institutions are prioritizing youth-led dissemination and participation. The **UNESCO 2026 Youth Report** aims to empower young people in national policy-making and leadership [1]. Similarly, the **UN Youth2030 Progress Report 2026** takes stock of how the UN system is advancing meaningful youth leadership across the globe [2]. The leadership development market has grown to **$98.7 billion in 2026**, reflecting a shift toward human-centered leadership that treats AI as a partner [3] [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Human-Centered Leadership & Change Fitness</h3>
                <p>Leadership in 2026 is no longer about authority alone; it is about **"Change Fitness"**—the ability to balance trade-offs and navigate uncertainty in the AI era [5]. Human-centered leadership, supported by AI-powered coaching and development, is becoming the new standard [6]. The *2026 AI Index Report* highlights that AI is boosting teamwork, research momentum, and infrastructure efficiency, making it a true partner for the next generation of builders [7] [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">From Scrolling to Shaping Culture</h3>
                <p>Gen Z and Gen Alpha are shifting from mere consumers to culture shapers. Mastercard’s 2026 study reveals how youth culture is being redefined by **AI co-pilots**, the creator economy, and micro-communities [9]. These digital-native generations are using AI to learn, research, create, and experiment, while maintaining their own judgment [10]. They are not starting from zero; they are building upon the foundational AI principles that have rewritten organizational DNA [11] [12].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Intergenerational Wisdom & Sovereign Legacy</h3>
                <p>AI technology adoption is significantly enhancing **intergenerational knowledge transfer**, allowing older employees and elders to transmit their wisdom to younger generations more effectively [13]. For the Orakzai community, the **Sovereign Grid** serves as the anchor for this transfer, preserving Pashto language, historical records, and family memories [14]. By bridging experience and innovation, we are ensuring that the Orakzai name thrives for the century that follows [15].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: A Message to the Next Generation</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, the next generation is our greatest investment. We do not just leave you a world; we leave you a mission. By mastering AI literacy and digital sovereignty while remaining rooted in your character and roots, you are ensuring that the Orakzai legacy is one of continuous improvement and service. Build with purpose, ask the hard questions, and never forget where you came from. You are the architects of a future that is sovereign, wise, and better.”</p>
            </div>

            <div class="final-statement">
                BUILD BETTER.<br>
                LEAD WITH PURPOSE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>UNESCO, <em>2026 Youth Report: Lead with Youth and Empower Student Participation (2026)</em>.</li>
                    <li>UN Youth Affairs, <em>Youth2030 Progress Report 2026: Meaningful Youth Leadership (2026)</em>.</li>
                    <li>Future Market Insights, <em>Leadership Development Program Market Size and Growth 2026 (February 2026)</em>.</li>
                    <li>DDI Blog, <em>Leadership Trends 2026: AI, Uncertainty, and Human Expectations (November 2025)</em>.</li>
                    <li>Harvard Business School, <em>AI Trends for 2026: Building 'Change Fitness' and Balancing Trade-Offs (December 2025)</em>.</li>
                    <li>LinkedIn / Leadership Insights, <em>2026 Trends in Leadership Development: Human-Centered AI (August 2025)</em>.</li>
                    <li>Stanford HAI, <em>The 2026 AI Index Report: Value to Consumers and Tripling Utility (2026)</em>.</li>
                    <li>Microsoft Source, <em>What's Next in AI: 7 Trends to Watch in 2026 (December 2025)</em>.</li>
                    <li>Mastercard, <em>Gen Z and Gen Alpha: Shifting from Scrolling to Shaping Culture in 2026 (February 2026)</em>.</li>
                    <li>PwC, <em>2026 Gen Alpha Survey Report: Kids, Household Spending, and AI (March 2026)</em>.</li>
                    <li>Info-Tech Research Group, <em>AI Trends 2026: Rewriting Organizational DNA (2026)</em>.</li>
                    <li>UN DESA, <em>World Population Highlights 2026: Youth Population Trends (March 2026)</em>.</li>
                    <li>PMC / NCBI, <em>AI Technology Adoption and Intergenerational Knowledge Transfer (November 2025)</em>.</li>
                    <li>House of Communication, <em>Next Gen Signals: Five Trends Reshaping Gen Z and Gen Alpha in 2026 (April 2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>A Message to the Next Generation and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            190
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

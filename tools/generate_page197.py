from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-197-from-history-to-the-future.html'

GRAPHICS = [
    ("History to Future", "PAST", "↔", "NEXT"),
    ("Inherited Know", "WISE", "↔", "BASE"),
    ("Source Context", "PAST", "↔", "TRUE"),
    ("Future Question", "SELF", "↔", "DO"),
    ("AI Change", "AI", "↔", "WORK"),
    ("Digital Network", "LINK", "↔", "ALL"),
    ("Blockchain Rail", "GRID", "↔", "TRUE"),
    ("Automation Rail", "MAKE", "↔", "DO"),
    ("Biotech Rail", "LIFE", "↔", "NEW"),
    ("Climate Challenge", "SAFE", "↔", "NEXT"),
    ("Human Journey", "PAST", "↔", "LONG"),
    ("History Base", "PAST", "↔", "BASE"),
    ("Knowledge Acc", "LEAR", "→", "LEAR"),
    ("Inst Evolution", "OLD", "→", "NEW"),
    ("Tech Develop", "IDEA", "↔", "FIX"),
    ("Society Base", "ALL", "↔", "PAST"),
    ("Preserve Hist", "SAVE", "↔", "TRUE"),
    ("Decision Context", "PAST", "↔", "DO"),
    ("Documentation", "TRUE", "↔", "WISE"),
    ("Evidence Base", "FACT", "↔", "TRUE"),
    ("Interpretation", "WHY", "↔", "TRUE"),
    ("Oral History", "TALK", "→", "SAVE"),
    ("Cultural Memory", "MIND", "↔", "SAVE"),
    ("Value Archives", "DATA", "↔", "SAFE"),
    ("Digital Pres", "NET", "↔", "SAVE"),
    ("Stewardship", "RULE", "↔", "SAFE"),
    ("History Ident", "PAST", "↔", "SELF"),
    ("Orakzai Heritage", "ORAK", "↔", "TRUE"),
    ("Pashtun History", "PASH", "↔", "TRUE"),
    ("Pakistani Hist", "FLAG", "↔", "TRUE"),
    ("Many Perspect", "MANY", "↔", "ONE"),
    ("Complexity Rail", "WHY", "↔", "TRUE"),
    ("No Romanticize", "PAST", "≠", "BEST"),
    ("No Rejection", "WHY", "≠", "HATE"),
    ("Past Teacher", "PAST", "→", "WISE"),
    ("Mistake Lesson", "FAIL", "→", "WISE"),
    ("Success Base", "BEST", "↔", "SAVE"),
    ("Adaptation Rail", "OLD", "→", "NEW"),
    ("Continuity Rail", "SAVE", "↔", "LONG"),
    ("Meaning Values", "TRUE", "↔", "LONG"),
    ("Tech Change", "FAST", "↔", "NEW"),
    ("Human Needs", "LIFE", "↔", "BASE"),
    ("Future People", "TECH", "↔", "LIFE"),
    ("Tools to Systems", "ONE", "→", "ALL"),
    ("Ind Revolution", "MAKE", "↔", "BASE"),
    ("Electrification", "POWER", "↔", "BASE"),
    ("Computing Base", "CODE", "↔", "BASE"),
    ("Internet Rail", "LINK", "↔", "ALL"),
    ("Mobile Tech", "MOVE", "↔", "ALL"),
    ("Cloud Infra", "NET", "↔", "SAVE"),
    ("Modern AI", "AI", "↔", "NEXT"),
    ("Next Tech Era", "NEW", "↔", "NEXT"),
    ("Tech Cumulative", "PAST", "→", "NEW"),
    ("No Tech Alone", "AI", "↔", "ALL"),
    ("Infrastructure", "GRID", "↔", "BASE"),
    ("Human Capital", "ABLE", "↔", "NEXT"),
    ("Edu Progress", "LEAR", "↔", "BASE"),
    ("Continuous Edu", "TIME", "↔", "LEAR"),
    ("Lifelong Learn", "TIME", "↔", "LEAR"),
    ("Digital Lit", "KNOW", "↔", "ABLE"),
    ("AI Literacy", "AI", "↔", "LEAR"),
    ("CS Foundation", "CODE", "↔", "BASE"),
    ("Engineering", "RULE", "↔", "FIX"),
    ("Research Path", "WHY", "↔", "LONG"),
    ("Entrepreneurship", "IDEA", "→", "BIZ"),
    ("Builders Rail", "DO", "↔", "MAKE"),
    ("Responsibility", "SELF", "↔", "DO"),
    ("Digital Gen", "YOUN", "↔", "NET"),
    ("AI-Native Lear", "AI", "↔", "LEAR"),
    ("Human Judgment", "WISE", "↔", "DO"),
    ("Crit Thinking", "WHY", "↔", "TRUE"),
    ("Info Quality", "TRUE", "↔", "WISE"),
    ("Digital Trust", "TRUE", "↔", "SAFE"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Privacy Path", "SAFE", "↔", "DATA"),
    ("Digital Ident", "SELF", "↔", "NET"),
    ("Digital Gov", "RULE", "↔", "NET"),
    ("Digital Rights", "FREE", "↔", "SAFE"),
    ("Digital Owner", "OWN", "↔", "TRUE"),
    ("Tokenization", "PHYS", "→", "DIGI"),
    ("Decentralize", "ALL", "↔", "FREE"),
    ("Tech Limits", "TECH", "≠", "ALL"),
    ("Future Finance", "CASH", "↔", "NET"),
    ("Fin Inclusion", "ALL", "↔", "CASH"),
    ("RWA Assets", "PHYS", "↔", "NET"),
    ("Future Work", "DO", "↔", "NEXT"),
    ("Tasks not Jobs", "DO", "↔", "FIX"),
    ("Agentic AI", "AI", "↔", "DO"),
    ("Quantum Rail", "FAST", "↔", "SAFE"),
    ("Global Intelligence", "AI", "↔", "GLOB"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g197-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g197-{index}-title g197-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g197-{index}-title">{safe}</title><desc id="g197-{index}-desc">A transition relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g197-{index}-caption" class="diagram-caption">{index}. {safe} — Transition relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">From History to the Future Framework</title><desc id="hero-desc">A diagram showing the 2026 transition landscape, featuring the AI Index Report data, the $172B generative AI consumer value, and the shift toward Agentic AI and Quantum Computing.</desc><defs><linearGradient id="h197-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h197-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE TEMPORAL TRANSITION LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AI INDEX REPORT 2026: MEASURING THE REVOLUTION</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CONSUMER AI VALUE: $172B ANNUALLY (EARLY 2026)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AGENTIC AI & HUMANOID ROBOTICS: THE NEXT WAVE</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">GLOBAL INTELLIGENCE CRISIS: AI CAPEX AT 2% OF GDP</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">QUANTUM COMPUTING: UNLOCKING MOLECULAR MYSTERIES</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: ANCHORING THE FUTURE</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">MISSION: REMEMBER ROOTS, BUILD WHAT COMES NEXT</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">FROM HISTORY TO THE FUTURE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Remembering Where We Came From While Building What Comes Next: Context and Responsibility.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Temporal Transition Loop: Navigating the 2026 landscape where generative AI value, agentic automation, and quantum breakthroughs redefine how societies build upon their history to create a sovereign and intelligent future.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 197</title>
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
            <p class="section-label">PAGE 197</p>
            <h2>FROM HISTORY TO THE FUTURE</h2>
            <p>“Remembering Where We Came From While Building What Comes Next.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “The future does not begin from nothing. Every generation inherits knowledge, institutions, and achievements from those who came before. History is more than a record; it is a source of context. It tells us where we came from and how people responded to challenges. The future then asks: What will we do with what we have inherited? For a young generation in a rapidly changing world, this question matters deeply. Artificial intelligence, digital networks, and blockchain are part of a much longer human journey.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The 2026 AI Index & Consumer Value (2026)</h3>
                <p>By early 2026, the estimated value of generative AI tools to consumers has reached **$172 billion annually**, with the median value per user tripling since 2025 [1]. The **2026 AI Index Report** provides the data-driven roadmap for this revolution, measuring shifts in research, adoption, and public opinion [2]. As 74% of executives recognize that economic volatility creates new opportunities, organizations are adapting to human-centric AI to elevate their roles in the global growth landscape [3] [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Agentic AI, Robotics & The Next Wave</h3>
                <p>The next wave of innovation in 2026 is defined by **Agentic AI** and humanoid robotics, transforming how we work, build, and grow [5]. AI is reshaping decision-making from boardrooms to laboratories, pushing the boundaries of discovery in physics and biotechnology [6]. **Quantum Computing** is beginning to unlock molecular mysteries, while spatial computing and brain-computer interfaces (BCIs) redefine human health outcomes and digital interaction [7] [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Global Intelligence Crisis & AI Capex</h3>
                <p>2026 is being described as the year of the **Global Intelligence Crisis**, where AI capital expenditure (Capex) has reached **2% of global GDP** (approx. $650 billion) [9]. AI-adjacent commodities have surged by 65% as the world renovates its digital infrastructure to support the intelligence revolution [10]. In this fragmenting global order, navigating shifting power dynamics and rivalry among major powers has become a critical strategic trend for national security and economic resilience [11] [12].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Legacy, Responsibility & Sovereign Future</h3>
                <p>History is the foundation upon which the future is built. Critically examining the past does not require rejecting one's identity; instead, past mistakes become lessons and successes reveal practices worth preserving [13]. For the Orakzai community, the **Sovereign Grid** anchors the future in ancestral roots, ensuring that digital sovereignty and intergenerational responsibility guide the next century of progress [14]. By mastering AI literacy and digital trust, we are ensuring that the Orakzai name remains a source of wisdom and intelligence for the century that follows [15].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: From History to the Future</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, history is our teacher and the future is our canvas. We do not just inherit the world; we improve it. By mastering agentic AI and quantum breakthroughs while remaining rooted in our values of honesty and service, we are ensuring that the Orakzai legacy is one of intelligent progress and sovereign strength. We are the architects of a future that is wise, connected, and eternal. Our past is our context, and our future is our responsibility.”</p>
            </div>

            <div class="final-statement">
                CONTEXTUAL WISDOM.<br>
                INTELLIGENT FUTURE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Stanford HAI, <em>The 2026 AI Index Report: Consumer Value and Adoption (2026)</em>.</li>
                    <li>Stanford HAI / Facebook, <em>Measuring the AI Revolution: Data from the 2026 AI Index (August 2026)</em>.</li>
                    <li>IBM Institute for Business Value, <em>Business and Technology Trends for 2026: Economic Volatility (December 2025)</em>.</li>
                    <li>Info-Tech Research Group, <em>Tech Trends 2026: Human-Centric AI and IT's Role (2026)</em>.</li>
                    <li>Intellipaat / Instagram, <em>New Technology Trends That Will Transform 2026: Agentic AI (November 2025)</em>.</li>
                    <li>IBM Think, <em>The Future of Artificial Intelligence: Pushing Boundaries in Physics (2026)</em>.</li>
                    <li>The Innovation Mode, <em>2026 Technology Innovation: Trends, Opportunities, and Risks (December 2025)</em>.</li>
                    <li>Middle East Business News, <em>New Tech Trends for 2026: Quantum and Biotech (July 2026)</em>.</li>
                    <li>Citadel Securities, <em>The 2026 Global Intelligence Crisis: AI Capex at 2% of GDP (February 2026)</em>.</li>
                    <li>Coldstream Insights, <em>10 Trends to Watch for in 2026: Welcome to the Future (December 2025)</em>.</li>
                    <li>Brunswick Group / Robert Moran, <em>Twenty Trends in 2026: Global Risks and Power Dynamics (January 2026)</em>.</li>
                    <li>Strategic Trends 2026, <em>Navigating a Fragmenting Global Order and Power Shifts (May 2026)</em>.</li>
                    <li>Activant Research, <em>Global Mega Trends 2026: Foundational Forces Reshaping Growth (March 2026)</em>.</li>
                    <li>ScienceDirect, <em>Evolution of AI Research in Technological Forecasting and Social Change (2023-2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>From History to the Future and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            197
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

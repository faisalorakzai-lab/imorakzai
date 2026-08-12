from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-199-final-reflection-im-orakzai.html'

GRAPHICS = [
    ("Final Reflection", "PAST", "↔", "NEXT"),
    ("Who Am I?", "SELF", "↔", "ALL"),
    ("Identity Layers", "HOME", "↔", "GLOB"),
    ("Inherited Ident", "PAST", "→", "SELF"),
    ("Lived Identity", "DO", "↔", "SELF"),
    ("Heritage Context", "PAST", "↔", "TRUE"),
    ("Memory Link", "PAST", "↔", "NEXT"),
    ("Family History", "HOME", "↔", "TRUE"),
    ("Stories Path", "TALK", "→", "SAVE"),
    ("Language Rail", "TALK", "↔", "TRUE"),
    ("Tradition Rail", "SAVE", "↔", "LONG"),
    ("Living Culture", "PAST", "→", "NEW"),
    ("Preserve Path", "SAVE", "↔", "TRUE"),
    ("Critical Memory", "WHY", "↔", "TRUE"),
    ("Evidence Base", "FACT", "↔", "TRUE"),
    ("Respect Rail", "TRUE", "↔", "SAFE"),
    ("Diversity Path", "MANY", "↔", "ONE"),
    ("No Single Story", "ONE", "≠", "ALL"),
    ("Many Journeys", "HERE", "↔", "GLOB"),
    ("Diaspora Link", "HOME", "↔", "GLOB"),
    ("Connection Rail", "LINK", "↔", "ALL"),
    ("Digital Comm", "ALL", "↔", "NET"),
    ("Preserve Online", "NET", "↔", "SAVE"),
    ("Resp Doc", "TRUE", "↔", "SAFE"),
    ("Future Edu", "LEAR", "↔", "NEXT"),
    ("Learning Base", "LEAR", "↔", "LIFE"),
    ("Knowledge Path", "KNOW", "↔", "ABLE"),
    ("Crit Thinking", "WHY", "↔", "TRUE"),
    ("Science Path", "WHY", "↔", "FACT"),
    ("CS Foundation", "CODE", "↔", "BASE"),
    ("Technology Rail", "TECH", "↔", "DO"),
    ("Responsibility", "SELF", "↔", "DO"),
    ("Digital Gen", "YOUN", "↔", "NET"),
    ("AI Impact", "AI", "↔", "ALL"),
    ("Human Judgment", "WISE", "↔", "DO"),
    ("Digital Lit", "KNOW", "↔", "ABLE"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Privacy Rail", "SAFE", "↔", "DATA"),
    ("Digital Ident", "SELF", "↔", "NET"),
    ("The Builder", "DO", "↔", "MAKE"),
    ("The Engineer", "RULE", "↔", "FIX"),
    ("The Programmer", "CODE", "↔", "DO"),
    ("The Researcher", "WHY", "↔", "LONG"),
    ("The Entrepreneur", "IDEA", "→", "BIZ"),
    ("The Educator", "WISE", "→", "LEAR"),
    ("Comm Builder", "LINK", "↔", "TRUE"),
    ("Success Meaning", "TRUE", "↔", "ALL"),
    ("Service Path", "SELF", "→", "ALL"),
    ("Character Base", "TRUE", "↔", "BASE"),
    ("Integrity Rail", "TRUE", "↔", "SAFE"),
    ("Honesty Path", "TRUE", "↔", "SAFE"),
    ("Humility Rail", "KNOW", "≠", "ALL"),
    ("Curiosity Path", "WHY", "↔", "LONG"),
    ("Courage Rail", "NEW", "↔", "SAFE"),
    ("Patience Rail", "TIME", "↔", "LONG"),
    ("Resilience Path", "FAIL", "→", "WISE"),
    ("Adaptation Rail", "OLD", "→", "NEW"),
    ("Orakzai/Pak", "HOME", "↔", "FLAG"),
    ("Local Belong", "HERE", "↔", "SELF"),
    ("National Belong", "FLAG", "↔", "SELF"),
    ("Global Part", "GLOB", "↔", "SELF"),
    ("Human Base", "LIFE", "↔", "BASE"),
    ("No Exclusion", "ALL", "↔", "TRUE"),
    ("Respect Others", "SELF", "↔", "ALL"),
    ("Global/Roots", "GLOB", "↔", "HOME"),
    ("Mtns/Networks", "LAND", "↔", "NET"),
    ("Geography Base", "LAND", "↔", "BASE"),
    ("Tech Geography", "TECH", "↔", "LAND"),
    ("Connectivity", "NET", "↔", "ALL"),
    ("Opportunity", "OPEN", "↔", "ALL"),
    ("Realism Path", "TRUE", "↔", "FACT"),
    ("Education First", "LEAR", "↔", "BASE"),
    ("Future Tradition", "PAST", "↔", "NEW"),
    ("Life-Centered", "LIFE", "↔", "ALL"),
    ("Digital Wallet", "OWN", "↔", "NET"),
    ("AI Agents", "AI", "↔", "DO"),
    ("Human Capital", "ABLE", "↔", "NEXT"),
    ("Intergen Transfer", "WISE", "→", "NEXT"),
    ("Responsible Tech", "TRUE", "↔", "SAFE"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g199-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g199-{index}-title g199-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g199-{index}-title">{safe}</title><desc id="g199-{index}-desc">A reflection relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g199-{index}-caption" class="diagram-caption">{index}. {safe} — Reflection relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">FINAL REFLECTION — I’M ORAKZAI Framework</title><desc id="hero-desc">A diagram showing the 2026 reflection landscape, featuring future tradition, digital identity assurance, intergenerational knowledge transfer, and life-centered design.</desc><defs><linearGradient id="h199-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h199-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE FINAL IDENTITY LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">FUTURE TRADITION: REDEFINING CULTURE & HERITAGE</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL IDENTITY: CONTINUOUS ASSURANCE & WALLETS</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">INTERGENERATIONAL KNOWLEDGE TRANSFER STRATEGY</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">LIFE-CENTERED DESIGN: BEYOND HUMAN TO ECOSYSTEM</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">RESPONSIBLE TECH: ALIGNING FUTURE WITH PUBLIC INTEREST</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: IDENTITY AS INFRASTRUCTURE</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">I’M ORAKZAI: IDENTITY, MEMORY, RESPONSIBILITY & FUTURE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">FINAL REFLECTION — I’M ORAKZAI</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Identity, Memory, Responsibility and the Future: A Sovereign Journey.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Final Identity Loop: Navigating the 2026 landscape where future tradition, continuous identity assurance, and intergenerational knowledge transfer ensure that Orakzai identity remains the foundation for a sovereign, intelligent, and human-centered future.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 199</title>
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
            <p class="section-label">PAGE 199</p>
            <h2>FINAL REFLECTION — I’M ORAKZAI</h2>
            <p>“Identity, Memory, Responsibility and the Future.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “At the end of a long journey, the simplest question is: Who am I? The answer is a name, a family, a language, a place, a history, and a set of values. But identity is rarely only one thing. For an Orakzai person, saying ‘I’m Orakzai’ is a statement of connection to a heritage longer than any individual life. Identity is not a limitation; it is the foundation from which we enter the wider world. We are connected to an identity that existed before us and will continue after us—inherited, lived, and sovereign.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Future Tradition & Cultural Evolution (2026)</h3>
                <p>By 2026, **"Future Tradition"** has emerged as a key trend redefining how people connect with culture and heritage [1]. This concept suggests that no living culture remains completely unchanged; instead, tradition evolves as people respond to new circumstances [2]. Digital transformation provide unique capabilities to create more livable, inclusive, and people-centered societies, where pride in one's heritage coexists with global participation [3] [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Identity & Continuous Assurance</h3>
                <p>Digital identity in 2026 has shifted toward **continuous assurance**, as digital wallets scale and AI agents require sophisticated authentication [5]. The *Digital 2026 Global Overview Report* highlights milestones in digital participation, where understanding technology has become part of modern citizenship [6]. In this landscape, identity verification is defined by trust and security, ensuring that personal information is treated with care in a world of proliferating deepfakes [7] [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Intergenerational Knowledge Transfer & Legacy</h3>
                <p>Strategic frameworks for **intergenerational knowledge transfer** have become essential for family firms and communities to retain wisdom across generations [9]. By facilitating skills transfer, organizations avoid disruptions to productivity and preserve cultural memory [10]. This intergenerational dialogue ensures that young people learn about their heritage while gaining the skills required for an AI-driven world, where character and integrity determine how capability is used [11] [12].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Responsible Tech & Life-Centered Design</h3>
                <p>The **Responsible Tech** movement is aligning the future of technology with the public interest, moving from human-centered to **life-centered design** that considers the entire ecosystem [13] [14]. As AI systems like those documented in the *2026 AI Index Report* influence education, work, and research, the need for human judgment and critical thinking remains paramount [15]. For the Orakzai community, the **Sovereign Grid** anchors this responsibility in a foundation of dignity, service, and local technical capability [16].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Final Reflection — I’M ORAKZAI</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, identity is our anchor and our wings. We are Orakzai, Pakistani, and global citizens all at once. By mastering future tradition and intergenerational wisdom while remaining rooted in our values of integrity and curiosity, we are ensuring that the Orakzai name represents a journey from mountains to networks that is sovereign and eternal. We are the builders, the engineers, the researchers, and the educators of a future where identity is our strength and responsibility is our legacy.”</p>
            </div>

            <div class="final-statement">
                SOVEREIGN IDENTITY.<br>
                ETERNAL JOURNEY.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Human8, <em>Future Tradition: A Key 2026 Trend Shaping the Evolution of Culture (March 2026)</em>.</li>
                    <li>We Are Social, <em>Digital 2026 Global Overview Report: Milestones and Insights (October 2025)</em>.</li>
                    <li>ITU, <em>Digital Transformation Trends: Livable, Inclusive, and People-Centered Cities (2026)</em>.</li>
                    <li>ScienceDirect, <em>From Human-Centred to Life-Centred Design: Considering the Ecosystem (2022-2026)</em>.</li>
                    <li>Daon, <em>5 Digital Identity Predictions for 2026: Continuous Assurance and Wallets (December 2025)</em>.</li>
                    <li>Regula / YouTube, <em>12 Trends Reshaping Identity Verification in 2026: Trust and Security (2026)</em>.</li>
                    <li>Deloitte Insights, <em>2026 Global Human Capital Trends: Speed, Adaptability, and Choice (March 2026)</em>.</li>
                    <li>All Tech Is Human, <em>Responsible Tech Summit: Centering Humanity in Our Tech Future (November 2025)</em>.</li>
                    <li>Emerald / VJIKMS, <em>Exploring Intergenerational Knowledge Transfer in Family Businesses (November 2025)</em>.</li>
                    <li>LinkedIn / Wainwright, <em>Unlocking Potential Through Intergenerational Skills Transfer (2025-2026)</em>.</li>
                    <li>AMA, <em>Effective Knowledge Transfer Across Generations: captures and Transfer (2026)</em>.</li>
                    <li>Academia.edu, <em>Intergenerational Knowledge Transfer Strategy Framework for Family Firms (2026)</em>.</li>
                    <li>ACM / GenAI, <em>Responsible Use of AI Personas in Human-Centered Design Workshop (April 2026)</em>.</li>
                    <li>Disher Blog, <em>Human-Centered Design and the Trends Reshaping Product Development (June 2026)</em>.</li>
                    <li>Stanford HAI, <em>The 2026 AI Index Report: trajectory and Human-Centered AI (2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Final Reflection: I’M ORAKZAI and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            199
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

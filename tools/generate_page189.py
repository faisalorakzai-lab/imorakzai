from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-189-what-we-leave-behind.html'

GRAPHICS = [
    ("Generation Legacy", "PAST", "↔", "NEXT"),
    ("Inherited History", "PAST", "→", "NOW"),
    ("Inherited Culture", "HOME", "↔", "NEXT"),
    ("Inherited Know", "WISE", "↔", "BASE"),
    ("Inherited Inst", "GRID", "↔", "LONG"),
    ("Unfinished Work", "DO", "↔", "NEXT"),
    ("Legacy Question", "SELF", "↔", "TRUE"),
    ("Fame vs Legacy", "FAST", "≠", "LONG"),
    ("Memory Base", "MIND", "↔", "SAVE"),
    ("Documentation", "TRUE", "↔", "WISE"),
    ("Book Continuity", "BOOK", "↔", "LONG"),
    ("Digital Archive", "DATA", "↔", "SAFE"),
    ("Oral History", "TALK", "→", "SAVE"),
    ("Family Stories", "HOME", "↔", "WISE"),
    ("Comm History", "ALL", "↔", "DATA"),
    ("Photo Record", "EYE", "↔", "SAVE"),
    ("Audio/Video Rec", "MOVE", "↔", "SAVE"),
    ("Language Path", "TALK", "↔", "TRUE"),
    ("Pashto Continuity", "PASH", "↔", "TIME"),
    ("Cult Knowledge", "ALL", "↔", "WISE"),
    ("Edu Inheritance", "LEAR", "↔", "BASE"),
    ("Teacher Impact", "WISE", "→", "NEXT"),
    ("Mentor Path", "WISE", "→", "ABLE"),
    ("Parent Values", "HOME", "→", "NEXT"),
    ("Elder Wisdom", "PAST", "↔", "LONG"),
    ("Youth Creation", "YOUN", "→", "NEW"),
    ("Next Gen Opp", "FREE", "↔", "DO"),
    ("Build for Others", "SELF", "→", "ALL"),
    ("Public Inst", "ALL", "↔", "LONG"),
    ("Comm Inst", "ALL", "↔", "LINK"),
    ("School Legacy", "LEAR", "↔", "LONG"),
    ("Library Base", "BOOK", "↔", "NEXT"),
    ("Archive Safety", "DATA", "↔", "SAFE"),
    ("Uni Capacity", "LEAR", "↔", "TOP"),
    ("Research Path", "WHY", "↔", "LONG"),
    ("Science Base", "FACT", "↔", "ALL"),
    ("Tech Tool", "TECH", "↔", "FIX"),
    ("Software Rail", "CODE", "↔", "LONG"),
    ("Open Source", "OPEN", "↔", "ALL"),
    ("Digital Infra", "GRID", "↔", "BASE"),
    ("Cultural Infra", "SAVE", "↔", "TRUE"),
    ("Economic Infra", "CASH", "↔", "GROW"),
    ("Human Capital", "ABLE", "↔", "NEXT"),
    ("Know Compounding", "LEAR", "→", "LEAR"),
    ("Trust Compounding", "TRUE", "→", "TRUE"),
    ("Inst Durability", "ONE", "≠", "ALL"),
    ("Succession Path", "OLD", "→", "NEW"),
    ("Doc Know Base", "DATA", "↔", "SAFE"),
    ("Stewardship", "RULE", "↔", "SAFE"),
    ("Service Legacy", "HELP", "↔", "TRUE"),
    ("Comm Service", "ALL", "↔", "GROW"),
    ("Philanthropy", "CASH", "→", "LONG"),
    ("Edu Support", "LEAR", "↔", "NEXT"),
    ("Scholarship Path", "CASH", "→", "LEAR"),
    ("Mentor Mult", "ONE", "→", "MANY"),
    ("Entr Legacy", "BIZ", "↔", "LONG"),
    ("Resp Business", "TRUE", "↔", "SAFE"),
    ("Employment Base", "WORK", "↔", "BASE"),
    ("Innovation Rail", "NEW", "↔", "NEXT"),
    ("Tech for Dev", "TECH", "↔", "LIFE"),
    ("AI Inheritance", "AI", "↔", "NEXT"),
    ("Digital Memory", "DATA", "↔", "TIME"),
    ("Digital Pres", "SAVE", "↔", "DATA"),
    ("Data Loss Risk", "DATA", "≠", "LONG"),
    ("Standards Path", "OPEN", "↔", "SAFE"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Authenticity", "TRUE", "↔", "SAFE"),
    ("Fact vs Memory", "FACT", "↔", "MIND"),
    ("Ambient Memory", "AI", "↔", "MIND"),
    ("Living Legacy", "CASH", "↔", "NEXT"),
    ("Curation Crisis", "DATA", "≠", "SAVE"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g189-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g189-{index}-title g189-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g189-{index}-title">{safe}</title><desc id="g189-{index}-desc">A legacy relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g189-{index}-caption" class="diagram-caption">{index}. {safe} — Legacy relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">What We Leave Behind Framework</title><desc id="hero-desc">A diagram showing the 2026 legacy landscape, featuring ambient AI memory, the $62.6B digital legacy market, the $124T wealth transfer, and the digital curation crisis.</desc><defs><linearGradient id="h189-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h189-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE LIVING LEGACY LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AMBIENT AI MEMORY: PERSISTENT LONG-TERM MEMORY</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL LEGACY MARKET: $62.6B BY 2035</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">HISTORIC WEALTH TRANSFER: $124 TRILLION (2026)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DIGITAL CURATION CRISIS: NAVIGATING PERMANENCE</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">AI IN DIGITAL PRESERVATION: CATALOGING & ACCESS</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: INSTITUTIONAL MEMORY</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">LEGACY: USEFULNESS, STEWARDSHIP & CONTINUITY</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">WHAT WE LEAVE BEHIND</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Legacy, Memory, Knowledge, and the Responsibility of a Generation: Building for Tomorrow.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Living Legacy Loop: Navigating the 2026 landscape where ambient AI memory, the massive global wealth transfer, and the digital curation crisis redefine how generations inherit knowledge and build lasting institutions.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 189</title>
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
            <p class="section-label">PAGE 189</p>
            <h2>WHAT WE LEAVE BEHIND</h2>
            <p>“Legacy, Memory, Knowledge, and the Responsibility of a Generation.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Every generation inherits something—language, history, knowledge, and traditions created by those who came before. It also inherits unfinished work. The future is built from what previous generations leave behind. Legacy is often misunderstood as fame, but lasting legacy is about creating something useful enough that others can continue building upon it. The most important things we leave behind may not carry our names; they exist in the lives we helped, the knowledge we preserved, and the institutions we strengthened.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Ambient AI Memory & Institutional Knowledge (2026)</h3>
                <p>2026 is being recognized as the year of **Ambient AI Memory**, where persistent, long-term memory has become a core breakthrough in AI systems [1] [2]. This technology is revolutionizing institutional memory, allowing organizations to maintain context across millions of data points and ensuring that critical knowledge does not disappear when individuals leave [3] [4]. AI agent memory trends are shaping intelligent systems that rank, forget, and preserve information with unprecedented efficiency [5] [6].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Digital Legacy Market & Wealth Transfer</h3>
                <p>The global digital legacy market is projected to hit **$62.60 billion by 2035**, reflecting a growing societal focus on preserving digital assets and personal memory [7] [8]. As a historic **$124-trillion wealth transfer** begins, the *2026 Living Legacy Report* reveals how individuals and firms are using estate guidance to drive measurable intergenerational impact [9] [10]. This transfer includes not just financial capital, but the digital and intellectual assets that define a generation's contribution [11].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Navigating the Digital Curation Crisis</h3>
                <p>Researchers at ASU and other institutions are helping chart a path through the **"digital curation crisis,"** emphasizing that technology alone does not guarantee permanence [12]. Digital archives require deliberate maintenance, migration, and security to protect historical memory from obsolescence [13]. The *Digital Preservation Summit 2026* highlights the need for frameworks that secure cultural heritage through language processing and storytelling, ensuring that memory remains living and authentic [14] [15].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Stewardship, Service & Sovereign Legacy</h3>
                <p>The strongest legacy comes from serving others rather than seeking recognition. Leadership is increasingly understood as **stewardship**—a responsibility to protect and improve inherited institutions [16]. For the Orakzai community, the **Sovereign Grid** provides the digital infrastructure to preserve oral histories, Pashto literature, and family traditions [17]. By building schools, libraries, and businesses that outlast individuals, we are ensuring that the Orakzai legacy remains a foundation for the century that follows [18].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: What We Leave Behind</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, our legacy is the bridge we build for our children. We do not just inherit the past; we steward the future. By mastering ambient AI memory and digital preservation while remaining rooted in our values of service and integrity, we are ensuring that the Orakzai name remains synonymous with usefulness and strength. We leave behind not just our names, but the capacity for our people to prosper for generations to come.”</p>
            </div>

            <div class="final-statement">
                ARCHIVE MEANING.<br>
                BUILD FOR ETERNITY.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>LinkedIn / AI Insights, <em>2026: The Year of Ambient AI Memory and Long-Term Context (January 2026)</em>.</li>
                    <li>Stanford HAI, <em>The 2026 AI Index Report: Performance and Organizational Adoption (2026)</em>.</li>
                    <li>arXiv, <em>Revolutionizing Long-Term Memory in AI: New Horizons for ASI (2026)</em>.</li>
                    <li>Mem0.ai, <em>State of AI Agent Memory 2026: Progress Benchmark Report (July 2026)</em>.</li>
                    <li>IBM Think, <em>Tech Trends 2026: Memory, Security, and Quantum Breakthroughs (January 2026)</em>.</li>
                    <li>Reddit / AI Memory, <em>What AI Memory Systems Look Like in 2026: Google Research (March 2026)</em>.</li>
                    <li>Precedence Research, <em>Digital Legacy Market Size to Hit $62.60 Billion by 2035 (2026)</em>.</li>
                    <li>Zion Market Research, <em>Global Digital Legacy Market Value and Forecast 2034 (2026)</em>.</li>
                    <li>Wealth.com, <em>The 2026 Living Legacy Report: Historic Wealth Transfer (2026)</em>.</li>
                    <li>Smartheritance, <em>Digital Legacy Planning: Steps, Checklist, and Tools 2026 (June 2026)</em>.</li>
                    <li>Trust and Will, <em>2025 Estate Planning Report: Digital Legacy Trends (2025-2026)</em>.</li>
                    <li>ASU News, <em>Researchers Chart a Path Through the Digital Curation Crisis (June 2026)</em>.</li>
                    <li>Ithaka S+R, <em>The Effectiveness and Durability of Digital Preservation Systems (2026)</em>.</li>
                    <li>Henry Stewart Conferences, <em>Digital Preservation Summit 2026: Securing Cultural Heritage (2026)</em>.</li>
                    <li>IFLA, <em>Artificial Intelligence and the Future of Digital Preservation (2026)</em>.</li>
                    <li>HKSMP / WSR, <em>The Psychology of Digital Legacy: Conceptual Transformation (2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>What We Leave Behind and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            189
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

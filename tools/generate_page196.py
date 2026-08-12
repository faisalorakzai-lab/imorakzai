from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-196-from-mountains-to-technology.html'

GRAPHICS = [
    ("Mountain Journey", "PAST", "↔", "NEXT"),
    ("Digital Frontier", "NET", "↔", "NEW"),
    ("Ancestral Land", "HERE", "↔", "PAST"),
    ("Environment Rail", "LAND", "↔", "SELF"),
    ("Ancient Base", "OLD", "↔", "LONG"),
    ("Changing Tech", "FAST", "↔", "NEW"),
    ("Geography Base", "LAND", "↔", "BASE"),
    ("Digital Network", "LINK", "↔", "ALL"),
    ("Resilience Path", "FIX", "↔", "LONG"),
    ("Adaptation Rail", "OLD", "→", "NEW"),
    ("Resourceful", "ONE", "↔", "MAKE"),
    ("Mountain Mind", "MIND", "↔", "FIX"),
    ("Distance Rail", "HERE", "≠", "GLOB"),
    ("Digital Bridge", "LINK", "↔", "ALL"),
    ("Access Know", "LEAR", "↔", "NET"),
    ("Remote Learn", "HERE", "↔", "GLOB"),
    ("Remote Work", "HERE", "↔", "GLOB"),
    ("Global Market", "ALL", "↔", "NET"),
    ("Local Roots", "HOME", "↔", "SELF"),
    ("Identity Path", "SELF", "↔", "TRUE"),
    ("Digital Heritage", "SAVE", "↔", "DATA"),
    ("Language Mech", "TALK", "↔", "TRUE"),
    ("Oral History", "TALK", "→", "SAVE"),
    ("Cultural Memory", "MIND", "↔", "SAVE"),
    ("Orakzai Story", "ORAK", "↔", "TRUE"),
    ("Beyond Geog", "LAND", "≠", "ALL"),
    ("Digital Diaspora", "GLOB", "↔", "HOME"),
    ("Comm Network", "ALL", "↔", "LINK"),
    ("Global Orakzai", "ALL", "↔", "LINK"),
    ("Preserve Hist", "SAVE", "↔", "LONG"),
    ("Archive Rail", "DATA", "↔", "SAFE"),
    ("Authenticity", "TRUE", "↔", "SAFE"),
    ("Fact-Checking", "FACT", "↔", "TRUE"),
    ("Resp Story", "TRUE", "↔", "SAFE"),
    ("Documentation", "TRUE", "↔", "LONG"),
    ("Two Worlds", "PAST", "↔", "NEXT"),
    ("Heritage Modern", "OLD", "↔", "NEW"),
    ("Learn Past", "PAST", "→", "WISE"),
    ("Build Future", "DO", "↔", "NEXT"),
    ("Memory to Data", "MIND", "→", "DATA"),
    ("Stories to Rec", "TALK", "→", "SAVE"),
    ("Distance Connect", "HERE", "↔", "ALL"),
    ("Local to Global", "ONE", "→", "GLOB"),
    ("Consumer to Ctr", "BUY", "→", "MAKE"),
    ("The Builder", "SELF", "↔", "MAKE"),
    ("Digital Skills", "ABLE", "↔", "DONE"),
    ("CS Foundation", "CODE", "↔", "BASE"),
    ("Engineering", "RULE", "↔", "FIX"),
    ("Entrepreneurship", "IDEA", "→", "BIZ"),
    ("Research Path", "WHY", "↔", "LONG"),
    ("Innovation Rail", "NEW", "↔", "NEXT"),
    ("Tech Leverage", "ONE", "→", "MANY"),
    ("Software Path", "CODE", "→", "GLOB"),
    ("Cloud Infra", "NET", "↔", "SAVE"),
    ("Digital Plat", "ALL", "↔", "LINK"),
    ("E-Commerce Rail", "BUY", "↔", "NET"),
    ("Digital Payment", "PAY", "↔", "SAFE"),
    ("Fintech Path", "CASH", "↔", "TECH"),
    ("Digital Assets", "OWN", "↔", "NET"),
    ("Blockchain Rail", "GRID", "↔", "TRUE"),
    ("Smart Contract", "CODE", "↔", "SAFE"),
    ("Decentralize", "ALL", "↔", "FREE"),
    ("Digital Owner", "OWN", "↔", "TRUE"),
    ("Resp Tech Use", "TRUE", "↔", "SAFE"),
    ("Digital Divide", "HAVE", "≠", "NONE"),
    ("Connectivity Gap", "NET", "≠", "ALL"),
    ("Device Access", "TECH", "↔", "ALL"),
    ("Digital Literacy", "KNOW", "↔", "ABLE"),
    ("Affordability", "CASH", "↔", "NET"),
    ("Infrastructure", "GRID", "↔", "BASE"),
    ("Electricity Base", "POWER", "↔", "BASE"),
    ("Telecom Rail", "LINK", "↔", "ALL"),
    ("Data Centers", "DATA", "↔", "PHYS"),
    ("Undersea Cable", "LINK", "↔", "GLOB"),
    ("Satellite Conn", "SKY", "↔", "HERE"),
    ("Edge Computing", "HERE", "↔", "FAST"),
    ("Mountain Infra", "LAND", "↔", "GRID"),
    ("Eng Challenges", "FIX", "↔", "LAND"),
    ("Tech/Geography", "TECH", "↔", "LAND"),
    ("Physical Base", "PHYS", "↔", "BASE"),
    ("Tech & Infra", "CODE", "↔", "GRID"),
    ("Local Tech Cap", "HERE", "↔", "ABLE"),
    ("Sovereignty", "SELF", "↔", "TECH"),
    ("Space-Based DC", "SKY", "↔", "DATA"),
    ("AI Co-Creation", "AI", "↔", "ALL"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g196-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g196-{index}-title g196-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g196-{index}-title">{safe}</title><desc id="g196-{index}-desc">A journey relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g196-{index}-caption" class="diagram-caption">{index}. {safe} — Journey relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">From Mountains to Technology Framework</title><desc id="hero-desc">A diagram showing the 2026 digital frontier landscape, featuring edge computing for remote regions, space-based data centers, AI for cultural heritage, and digital diaspora engagement.</desc><defs><linearGradient id="h196-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h196-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE DIGITAL FRONTIER LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">EDGE COMPUTING: $28.5B MARKET IN 2026</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">SPACE-BASED DATA CENTERS: SATELLITE OPERATIONS</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AI CULTURAL SAFEGUARDING: INCLUSIVE INDIGENOUS AI</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DIGITAL DIASPORA: ACTIVE HOMELAND MOBILIZATION</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">COMMUNITY AI CO-CREATION: PARTICIPATORY DESIGN</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: INFRASTRUCTURE AS IDENTITY</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">FUTURE: ANCESTRAL ROOTS & DIGITAL SOVEREIGNTY</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">FROM MOUNTAINS TO TECHNOLOGY</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“A Journey from Ancestral Landscapes to the Digital Frontier: Sovereign and Connected.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Digital Frontier Loop: Navigating the 2026 landscape where edge computing, space-based data centers, and AI-driven cultural safeguarding ensure that remote mountain communities remain sovereign, connected, and culturally authentic.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 196</title>
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
            <p class="section-label">PAGE 196</p>
            <h2>FROM MOUNTAINS TO TECHNOLOGY</h2>
            <p>“A Journey from Ancestral Landscapes to the Digital Frontier.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Mountains and technology may appear to belong to different worlds—one ancient and physical, the other constantly changing and digital. Yet both teach the same lesson: the environment shapes the people who learn to navigate it. For Orakzai communities, the mountains demanded resilience and resourcefulness. Technology creates another kind of landscape, with networks instead of valleys and algorithms instead of pathways. The people who navigate this new frontier will help shape the future.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Edge Computing & Remote Infrastructure (2026)</h3>
                <p>By 2026, the global edge computing market is projected to reach **$28.5 billion**, providing localized compute nodes that reduce latency for remote regions [1] [2]. This architecture allows mountain communities to grow incrementally by adding compute power closer to users, bypassing the limitations of traditional terrestrial infrastructure [3]. Furthermore, **space-based data centers** are revolutionizing satellite operations, meeting the surging demand from AI and machine learning in areas where terrestrial cables are difficult to deploy [4] [5].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI & Cultural Safeguarding for Indigenous Heritage</h3>
                <p>Artificial Intelligence is emerging as a powerful tool for **cultural heritage protection**, particularly for endangered languages and oral histories [6]. UNESCO reports emphasize the need for AI to be inclusive and respectful of Indigenous peoples' rights, ensuring that technology amplifies wisdom rather than replacing it [7]. By 2026, communities are starting to **co-create with AI**, using machine learning to document intangible heritage and foster understanding across geographic boundaries [8] [9].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Digital Diaspora & Homeland Engagement</h3>
                <p>Digital transformation has enabled diaspora actors to engage more actively in their homelands, shaping global public opinion and navigating conflicts [10]. **Digital diasporas** are using technological tools to design new ways of thinking and doing, facilitating communication, collaboration, and knowledge sharing across borders [11] [12]. These networks connect Orakzai people across cities and countries, ensuring that identity remains strong despite physical migration [13].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Sovereignty & Local Technical Capability</h3>
                <p>The digital future requires investment in both software and physical infrastructure, including reliable power, telecom, and undersea cables [14]. Communities benefit most when they develop **local technical capability**, reducing dependence on external providers [15]. For the Orakzai community, the **Sovereign Grid** represents the physical foundation of identity, where technical capability and digital sovereignty ensure that the ancestral spirit thrives in the digital age [16].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: From Mountains to Technology</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, the journey from the mountains to technology is a path of continuity. We do not leave our roots behind; we carry them into the digital frontier. By mastering edge computing and AI-driven preservation while remaining rooted in our values of resilience and resourcefulness, we are ensuring that the Orakzai name remains a source of strength in both the physical and digital worlds. We are the builders of a civilization that is sovereign, connected, and eternal. Our mountains are our foundation, and technology is our bridge.”</p>
            </div>

            <div class="final-statement">
                ANCESTRAL STRENGTH.<br>
                DIGITAL FRONTIER.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>TechTarget, <em>10 Edge Computing Trends to Watch in 2026 and Beyond (January 2026)</em>.</li>
                    <li>FloLive, <em>Edge Computing in 2026: Use Cases, Technology, and Edge AI (December 2025)</em>.</li>
                    <li>S&P Global, <em>2026 Trends in Data Center Services & Infrastructure: AI Race (2026)</em>.</li>
                    <li>Aerospace Corp / Facebook, <em>Space-based Data Centers Revolutionizing Satellite Operations (June 2026)</em>.</li>
                    <li>TierPoint, <em>Digital Infrastructure Trends to Watch in 2026: AI-Ready Centers (March 2026)</em>.</li>
                    <li>Calvium, <em>Using AI to Preserve Cultural Heritage: Safeguarding Legacies (January 2026)</em>.</li>
                    <li>UNESCO, <em>Exploring the Impact of AI on Intangible Cultural Heritage (2026)</em>.</li>
                    <li>ScienceDirect, <em>New AI Challenges for Cultural Heritage Protection: ML Review (2025-2026)</em>.</li>
                    <li>Medium / Andrew E. Coulson, <em>Five Emerging Trends in Community Engagement for 2026: AI Co-Creation (2026)</em>.</li>
                    <li>New Lines Institute, <em>How Social Media Has Transformed Diaspora Mobilization (September 2025)</em>.</li>
                    <li>iDiaspora, <em>Digital Diaspora: Technological Tools for Engagement and Innovation (2022-2026)</em>.</li>
                    <li>IOM, <em>Global Diaspora Summit: Digital Innovation and New Ways of Doing (2026)</em>.</li>
                    <li>Culture Unbound, <em>Digital Cultural Heritage of Minorities and Indigenous Peoples (2026)</em>.</li>
                    <li>TerraWatch Space, <em>Edge Computing for Earth Observation: 2026 Edition (February 2026)</em>.</li>
                    <li>LinkedIn / Antonio Guterres, <em>How AI Can Help Preserve Indigenous Knowledge and Culture (August 2025)</em>.</li>
                    <li>Orakzai Group Archives, <em>From Mountains to Technology and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            196
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

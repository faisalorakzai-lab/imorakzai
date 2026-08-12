from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-180-never-forget-where-you-came-from.html'

GRAPHICS = [
    ("Identity Path", "PAST", "↔", "NEXT"),
    ("Journey Start", "HOME", "→", "GLOB"),
    ("Memory Link", "THEN", "↔", "NOW"),
    ("Roots Rail", "BASE", "↔", "STAY"),
    ("Continuity Path", "OLD", "→", "NEW"),
    ("Origins Rail", "BORN", "↔", "SELF"),
    ("Family Value", "HOME", "↔", "WISE"),
    ("Comm Social", "ALL", "↔", "LINK"),
    ("Place Perspective", "HERE", "↔", "EYE"),
    ("Culture Frame", "TRUE", "↔", "WISE"),
    ("Language Memory", "TALK", "↔", "TIME"),
    ("History Understand", "PAST", "↔", "NOW"),
    ("Heritage Connect", "PAST", "↔", "ALL"),
    ("Roots Stability", "BASE", "↔", "ABLE"),
    ("Identity Evolve", "SELF", "↔", "TIME"),
    ("Adaptation Rail", "LEAR", "↔", "TIME"),
    ("Modernization", "NEW", "≠", "LOSS"),
    ("Global Connect", "HERE", "↔", "GLOB"),
    ("Global Citizen", "SELF", "↔", "ALL"),
    ("Local Roots", "BASE", "↔", "GLOB"),
    ("Global Vision", "GLOB", "↔", "EYE"),
    ("Migration Link", "HERE", "↔", "THERE"),
    ("Diaspora Connect", "GLOB", "↔", "HOME"),
    ("Digital Bridge", "LINK", "↔", "HOME"),
    ("Digital Memory", "DATA", "↔", "SAVE"),
    ("Preserve Story", "TALK", "↔", "SAVE"),
    ("Oral History", "TALK", "→", "SAVE"),
    ("Intergen Know", "WISE", "→", "LEAR"),
    ("Elder Wisdom", "WISE", "↔", "LONG"),
    ("Youth Express", "YOUN", "↔", "MAKE"),
    ("Tech Bridge", "LINK", "↔", "ALL"),
    ("Digital Archive", "DATA", "↔", "SAVE"),
    ("Preserve Context", "TRUE", "↔", "SAVE"),
    ("Comm Steward", "ALL", "↔", "OWN"),
    ("Respect Rail", "SELF", "↔", "THEY"),
    ("Humility Path", "SELF", "↔", "WISE"),
    ("Gratitude Path", "SELF", "↔", "HELP"),
    ("Family Sacrifice", "GIVE", "→", "ABLE"),
    ("Mentor Influence", "WISE", "→", "DO"),
    ("Friend Resilience", "TWO", "↔", "STAY"),
    ("Comm Support", "ALL", "→", "ONE"),
    ("Begin Perspective", "BORN", "↔", "EYE"),
    ("Success Meaning", "DONE", "↔", "WISE"),
    ("Ambition Purpose", "WANT", "↔", "WHY"),
    ("Purpose Value", "WHY", "↔", "TRUE"),
    ("Values Rail", "TRUE", "↔", "TIME"),
    ("Character Path", "SELF", "↔", "DO"),
    ("Integrity Rail", "TRUE", "↔", "STAY"),
    ("Responsibility", "ABLE", "→", "MUST"),
    ("Success Resp", "DONE", "→", "MUST"),
    ("Remember People", "DONE", "↔", "NAME"),
    ("Acknowledgment", "NAME", "↔", "TRUE"),
    ("Lead Gratitude", "LEAD", "↔", "HELP"),
    ("Entr Humility", "BIZ", "↔", "WISE"),
    ("Failure Lesson", "FAIL", "→", "WISE"),
    ("Resilience Path", "FAIL", "→", "STAY"),
    ("First Idea", "IDEA", "→", "TEST"),
    ("First Product", "MAKE", "↔", "LEAR"),
    ("First Customer", "BUY", "↔", "WISE"),
    ("First Team", "TEAM", "↔", "BASE"),
    ("First Mistake", "FAIL", "→", "FIX"),
    ("First Break", "DONE", "↔", "TIME"),
    ("Growth Change", "GROW", "↔", "SYS"),
    ("Scale Principle", "GROW", "↔", "BASE"),
    ("Tech Reach", "SELF", "↔", "GLOB"),
    ("Digital Entr", "ONE", "↔", "GLOB"),
    ("Global Access", "ALL", "↔", "NET"),
    ("Local Advantage", "HERE", "↔", "WISE"),
    ("Local Problem", "HERE", "→", "FIX"),
    ("Pak Potential", "HOME", "↔", "GROW"),
    ("Pakistani Youth", "YOUN", "→", "GLOB"),
    ("Local Entr", "HERE", "→", "BIZ"),
    ("Build from Home", "HOME", "→", "GLOB"),
    ("Digital Access", "ALL", "↔", "TOOL"),
    ("Education Path", "LEAR", "↔", "GLOB"),
    ("Self-Education", "SELF", "→", "KNOW"),
    ("CS Foundations", "CODE", "↔", "BASE"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g180-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g180-{index}-title g180-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g180-{index}-title">{safe}</title><desc id="g180-{index}-desc">A "Never Forget Where You Came From" relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g180-{index}-caption" class="diagram-caption">{index}. {safe} — Identity and memory relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Never Forget Where You Came From Framework</title><desc id="hero-desc">A diagram showing the 2026 framework for maintaining cultural continuity, featuring the "Local Roots + Global Vision" model, AI-driven family discovery, and the digital legacy market.</desc><defs><linearGradient id="h180-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h180-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE CULTURAL CONTINUITY LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">LOCAL ROOTS + GLOBAL VISION (2026)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">AI-DRIVEN FAMILY DISCOVERY: intuitve & FAST</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">DIGITAL LEGACY MARKET: $15B+ (2025-2035)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">REVERSE MENTORING: DIGITAL KNOWLEDGE UPWARD</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">GLOBAL CITIZENSHIP & SOCIAL JUSTICE BALANCE</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN MEMORY: PAST TO FUTURE</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">IDENTITY: UNDERSTANDING ORIGINS, BUILDING FUTURE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">NEVER FORGET WHERE YOU CAME FROM</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Identity, Memory, and the Journey Forward: Local Roots + Global Vision.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Cultural Continuity Loop: Navigating the 2026 landscape where AI-driven family discovery, digital legacy markets, and intergenerational knowledge transfer ensure that global progress remains rooted in local identity and values.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 180</title>
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
            <p class="section-label">PAGE 180</p>
            <h2>NEVER FORGET WHERE YOU CAME FROM</h2>
            <p>“Identity, Memory, and the Journey Forward.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Progress can take people far from where they began. Education, technology, and entrepreneurship open new worlds, changing circumstances and expectations. But movement forward does not require forgetting the place, people, and values that shaped the journey. Never forget where you came from. This is not an argument against change; it is an argument for continuity. A person can become global without becoming disconnected from their roots. The future is built by people who understand where they have come from and where they want to go.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">AI-Driven Family Discovery & Digital Legacy (2026)</h3>
                <p>By 2026, the world has entered a "family history era," where emerging technologies are providing unprecedented access to genealogical records [1]. The *FamilySearch Global Tech Forum 2026* unveiled powerful new AI-driven tools that make family discovery faster and more intuitive, moving beyond "dusty photo albums" to interactive digital trees [2] [3]. The global digital legacy market is projected to reach **$62.60 billion by 2035**, reflecting a massive shift toward securing collective memory for future generations [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Intergenerational Knowledge & Reverse Mentoring</h3>
                <p>Digital technology is redefining how knowledge moves between generations. Research highlights a unique mechanism of "upward" knowledge transfer, where youth act as catalysts for parental social mobility by sharing digital skills [5]. At the same time, effective mentoring programs are essential for capturing the historical wisdom of elders that is difficult to recover once lost [6] [7]. Technology acts as a bridge, connecting families separated by distance and ensuring that cultural foundations remain living and evolving [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Global Citizenship & Local Identity</h3>
                <p>The relationship for the modern builder can be expressed as: **local roots + global vision** [9]. Global citizenship education is being strategically employed to create social balance, allowing individuals to embrace their responsibility to act for the benefit of all societies while remaining connected to their local community [10] [11]. The *World Citizenship Report 2026* emphasizes that global choices are increasingly driven by safety, quality of life, and economic opportunity, yet authentic identity remains the anchor for meaningful impact [12].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Character, Values & Sovereign Memory</h3>
                <p>Individual success rarely exists in isolation; it depends on the sacrifices of parents, teachers, and mentors [13]. Success should not erase the experiences that made the journey meaningful. Values provide continuity through periods of rapid change, and integrity means maintaining principles even under pressure [14]. For the Orakzai community, **Sovereign Memory** is about understanding origins to build a future where local knowledge and global ambition coexist, ensuring that our dignity and strength endure [15].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Never Forget Where You Came From</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, our origins are our strength. We do not fear the global digital economy; we enter it with the resilience of our ancestors. By mastering the tools of AI and digital archives while honoring our family sacrifices, we are building a sovereign legacy that is globally respected and locally rooted. We remember where we came from, so we can build a future that is truly ours.”</p>
            </div>

            <div class="final-statement">
                ROOTED IN VALUES.<br>
                BUILDING THE FUTURE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>FamilySearch UK, <em>What to Expect in 2026: Emerging Tech and Genealogical Access (March 2026)</em>.</li>
                    <li>YouTube / FamilySearch, <em>Global Tech Forum 2026: AI Updates for Family Discovery (April 2026)</em>.</li>
                    <li>MyHeritage, <em>2026 is in its Family History Era: Learning Your Story (March 2026)</em>.</li>
                    <li>Precedence Research, <em>Digital Legacy Market Size and Projections 2035 (2026)</em>.</li>
                    <li>ResearchGate, <em>Intergenerational Knowledge Transfer: Youth as Catalysts for Social Mobility (May 2026)</em>.</li>
                    <li>AMA, <em>Effective Knowledge Transfer: Capturing Wisdom Across Generations (2026)</em>.</li>
                    <li>Vorecol Blog, <em>Best Practices for Mentoring and Intergenerational Transfer (August 2024)</em>.</li>
                    <li>Hilton Trends Report, <em>2026 Trends: Families Redefining Stays and Togetherness (October 2025)</em>.</li>
                    <li>Academia.edu, <em>Intergenerational Knowledge Transfer Framework for Family Firms (2026)</em>.</li>
                    <li>Taylor & Francis, <em>Global Citizenship Education as a Strategy for Social Balance (2025)</em>.</li>
                    <li>United Nations, <em>Academic Impact: Promoting Global Citizenship for Sustainable Development (2026)</em>.</li>
                    <li>CS Global Partners, <em>World Citizenship Report 2026: Safety, Quality and Identity (2026)</em>.</li>
                    <li>ResearchGate, <em>Global Citizenship Education for Meaningful Social Impact (August 2025)</em>.</li>
                    <li>NEDCC, <em>The Relevance of Preservation in a Digital World: Context and History (2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Sovereign Memory and Cultural Continuity Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            180
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

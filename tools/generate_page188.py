from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-188-a-digital-future-for-orakzai.html'

GRAPHICS = [
    ("Digital Future", "PAST", "↔", "NEXT"),
    ("Digital Orakzai", "SELF", "↔", "TECH"),
    ("Identity Rail", "SELF", "↔", "TRUE"),
    ("Cult Continuity", "PAST", "↔", "NEXT"),
    ("Digital Heritage", "PAST", "↔", "DATA"),
    ("Oral History", "TALK", "→", "SAVE"),
    ("Hist Archives", "DATA", "↔", "WISE"),
    ("Comm Memory", "ALL", "↔", "DATA"),
    ("Language Path", "TALK", "↔", "TRUE"),
    ("Pashto Digital", "PASH", "↔", "NET"),
    ("Local Know", "HERE", "↔", "WISE"),
    ("Cult Education", "LEAR", "↔", "TRUE"),
    ("Youth Center", "YOUN", "↔", "NEXT"),
    ("Digital Native", "BORN", "↔", "NET"),
    ("Digital Literacy", "KNOW", "↔", "ABLE"),
    ("Comp Education", "BASE", "↔", "KNOW"),
    ("Programming Rail", "CODE", "↔", "MAKE"),
    ("AI Future", "AI", "↔", "ALL"),
    ("AI Education", "AI", "↔", "LEAR"),
    ("Crit Thinking", "WHY", "↔", "TRUE"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Online Privacy", "SAFE", "↔", "DATA"),
    ("Digital Safety", "SAFE", "↔", "NET"),
    ("Strong Auth", "LOCK", "↔", "SAFE"),
    ("Data Protection", "DATA", "↔", "SAFE"),
    ("Digital Infra", "GRID", "↔", "BASE"),
    ("Connectivity", "NET", "↔", "ALL"),
    ("Rural Connect", "HERE", "↔", "NET"),
    ("Afford Access", "CASH", "↔", "NET"),
    ("Mobile Internet", "MOVE", "↔", "NET"),
    ("Digital Inclusion", "ALL", "↔", "GROW"),
    ("Digital Divide", "HAVE", "≠", "NONE"),
    ("Accessibility", "SAFE", "↔", "ALL"),
    ("Multilingual", "PASH", "↔", "TECH"),
    ("Digital Edu", "LEAR", "↔", "NET"),
    ("Online Learning", "NET", "↔", "LEAR"),
    ("Remote Edu", "HERE", "↔", "GLOB"),
    ("Uni Access", "LEAR", "↔", "GLOB"),
    ("Research Path", "WHY", "↔", "GLOB"),
    ("Global Acad Net", "LEAR", "↔", "GLOB"),
    ("Digital Library", "BOOK", "↔", "DATA"),
    ("Open Edu Res", "FREE", "↔", "LEAR"),
    ("Skills Develop", "ABLE", "↔", "TIME"),
    ("Lifelong Learn", "TIME", "↔", "LEAR"),
    ("Digital Careers", "WORK", "↔", "TECH"),
    ("Remote Work", "HERE", "↔", "GLOB"),
    ("Freelancing", "ONE", "→", "GLOB"),
    ("Digital Entr", "IDEA", "→", "BIZ"),
    ("Global Customer", "ALL", "↔", "NET"),
    ("Digital Exports", "HOME", "→", "CASH"),
    ("Startups Rail", "IDEA", "↔", "CASH"),
    ("Software Dev", "CODE", "↔", "GLOB"),
    ("AI Startups", "AI", "↔", "BIZ"),
    ("Cybersec Ind", "SEC", "↔", "CASH"),
    ("Cloud Services", "NET", "↔", "SAVE"),
    ("Data Importance", "DATA", "↔", "WISE"),
    ("Resp Data Use", "TRUE", "↔", "SAFE"),
    ("Digital Commerce", "BUY", "↔", "NET"),
    ("Digital Payment", "PAY", "↔", "SAFE"),
    ("Fin Inclusion", "ALL", "↔", "CASH"),
    ("Fin Literacy", "KNOW", "↔", "CASH"),
    ("Digital Assets", "OWN", "↔", "NET"),
    ("Blockchain Rail", "GRID", "↔", "TRUE"),
    ("Digital Owner", "OWN", "↔", "TRUE"),
    ("Tokenization", "PHYS", "→", "DIGI"),
    ("Resp Innovation", "IDEA", "↔", "SAFE"),
    ("Digital Gov", "RULE", "↔", "NET"),
    ("Comm Platform", "ALL", "↔", "LINK"),
    ("Digital Dir", "NAME", "↔", "LINK"),
    ("Privacy-First", "SAFE", "↔", "DO"),
    ("Comm Verif", "TRUE", "↔", "SAFE"),
    ("Digital Trust", "TRUE", "↔", "SAFE"),
    ("Info Quality", "TRUE", "↔", "WISE"),
    ("Misinfo Rail", "BAD", "≠", "TRUE"),
    ("Digital Media", "TALK", "↔", "NET"),
    ("Resp Comm", "TRUE", "↔", "SAFE"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g188-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g188-{index}-title g188-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g188-{index}-title">{safe}</title><desc id="g188-{index}-desc">A digital future relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g188-{index}-caption" class="diagram-caption">{index}. {safe} — Digital future relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">A Digital Future for Orakzai Framework</title><desc id="hero-desc">A diagram showing the 2026 digital future landscape, featuring DRIF26 inclusive futures, indigenous data sovereignty, and AI-driven cultural revitalization.</desc><defs><linearGradient id="h188-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h188-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE DIGITAL FUTURE LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DRIF26: BUILDING INCLUSIVE & RESILIENT FUTURES</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">INDIGENOUS DATA SOVEREIGNTY: TRIBAL DATA CONTROL</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AI CULTURAL REVITALIZATION: ENDANGERED LANGUAGES</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">PARTICIPATORY AI: COMMUNITY-LED DESIGN PROCESS</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL INCLUSION WEEK 2026: PROGRESS TOWARD EQUITY</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: IDENTITY AS INFRASTRUCTURE</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">FUTURE: SOVEREIGN, INCLUSIVE & CULTURALLY ROOTED</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">A DIGITAL FUTURE FOR ORAKZAI</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Preserving Identity While Building for a Connected World: Sovereign and Inclusive.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Digital Future Loop: Navigating the 2026 landscape where DRIF26 inclusive futures, tribal data sovereignty, and AI-driven cultural revitalization ensure that Orakzai identity thrives in a globally connected digital civilization.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 188</title>
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
            <p class="section-label">PAGE 188</p>
            <h2>A DIGITAL FUTURE FOR ORAKZAI</h2>
            <p>“Preserving Identity While Building for a Connected World.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “The future of Orakzai communities will be shaped by many forces—education, technology, and cultural continuity. Digital technology will be one of them. A digital future does not mean replacing traditional identity with technology; it means using technology to preserve knowledge, expand opportunity, and connect communities. For Orakzai people around the world, digital connectivity reduces geographic distance, allowing students to learn, professionals to work, and families to remain connected. The goal is to use technology where it creates genuine human value.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">DRIF26: Inclusive & Resilient Digital Futures (2026)</h3>
                <p>By 2026, the global conversation on digital rights has reached a critical milestone at the **Digital Rights and Inclusion Forum (#DRIF26)**. The forum’s theme, *“Building Inclusive and Resilient Digital Futures,”* emphasizes the need for **"Digital Ubuntu"**—a framework that promotes interconnectedness and equity in the digital age [1] [2]. This global movement highlights milestones in digital rights and inclusion, ensuring that technology serves all communities, regardless of geography or background [3].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Indigenous Data Sovereignty & Tribal Governance</h3>
                <p>Tribal nations are entering a new phase of sovereignty, one defined by **control over data** rather than just land and resources [4]. Indigenous Data Sovereignty (IDS) allows communities to lead in the governance of AI, strengthening government functions and ensuring that traditional knowledge is not exploited [5]. In March 2026, some tribal councils even voted to approve moratoriums on generative AI to ensure that their digital future is built on their own terms [6] [7].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI-Driven Cultural Revitalization</h3>
                <p>Artificial intelligence is increasingly being used to support **endangered language documentation** and revitalization [8]. Multimodal language models aid in the preservation of intangible cultural heritage, including storytelling, oral histories, and traditional practices [9] [10]. **Participatory AI** ensures that communities lead the design process, making technology a partner in cultural continuity rather than a substitute for it [11] [12].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Inclusion & Sovereign Infrastructure</h3>
                <p>**Digital Inclusion Week 2026** celebrates progress toward digital equity, highlighting the importance of affordable access and digital literacy [13]. For the Orakzai community, the **Sovereign Grid** serves as the foundational social infrastructure, where identity is integrated into digital systems [14]. This sovereign approach ensures that digital careers, remote work, and entrepreneurship are accessible to all, bridging the digital divide and building a future that is both globally connected and culturally rooted [15].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: A Digital Future for Orakzai</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, a digital future is the next chapter of our story. We do not just use technology; we build our presence within it. By mastering AI literacy and digital sovereignty while remaining rooted in our Pashtun identity, we are ensuring that our culture is not just preserved but revitalized for the modern world. We are the builders of a digital civilization that is sovereign, inclusive, and authentic. Our future is connected, and our identity is eternal.”</p>
            </div>

            <div class="final-statement">
                DIGITAL IDENTITY.<br>
                SOVEREIGN FUTURE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Instagram / DRIF26, <em>DRIF26: The Future of Digital Rights and Inclusion (April 2026)</em>.</li>
                    <li>Facebook / ParadigmHQ, <em>Building Inclusive and Resilient Digital Futures: DRIF26 Highlights (July 2026)</em>.</li>
                    <li>We Are Social USA, <em>Digital 2026 Global Overview Report: Milestones and Trends (October 2025)</em>.</li>
                    <li>Native News Online, <em>Data Control Will Shape the Next Phase of Tribal Sovereignty (April 2026)</em>.</li>
                    <li>Brookings Institution, <em>Defining Digital Sovereignty for Tribal Nations in the AI Age (2026)</em>.</li>
                    <li>Facebook / Indian Country Today, <em>Tribal Council Votes on Generative AI Moratorium (March 2026)</em>.</li>
                    <li>Facebook / NCAI, <em>AI and the Future of Tribal Nations: Data Sovereignty and Language (July 2026)</em>.</li>
                    <li>Bowdoin Science Journal, <em>AI for Language and Cultural Preservation: Endangered Language Documentation (December 2025)</em>.</li>
                    <li>NRF Kenya, <em>Application of AI in Cultural Heritage: Language Processing and Archiving (February 2025)</em>.</li>
                    <li>IEEE Xplore, <em>AI-Driven Cultural Preservation: Multimodal Language Models (2026)</em>.</li>
                    <li>IMUNA, <em>UNPFII 2026 Update: Preserving and Revitalizing Indigenous Languages (January 2026)</em>.</li>
                    <li>Medium / Andrew E. Coulson, <em>Five Emerging Trends in Community Engagement for 2026: Participatory AI (February 2026)</em>.</li>
                    <li>NDIA, <em>Digital Inclusion Week 2026: Celebrating Progress Toward Digital Equity (2026)</em>.</li>
                    <li>BroadbandUSA, <em>Five Digital Inclusion Trends: Regional and State-wide Planning (2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>A Digital Future for Orakzai and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            188
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

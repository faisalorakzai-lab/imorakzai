from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-181-the-future-of-orakzai.html'

GRAPHICS = [
    ("Orakzai Future", "PAST", "↔", "NEXT"),
    ("People Resource", "SELF", "↔", "ALL"),
    ("Next Gen Path", "YOUN", "→", "NEXT"),
    ("Education Base", "LEAR", "↔", "BASE"),
    ("Digital Edu Rail", "LEAR", "↔", "NET"),
    ("CS Foundation", "CODE", "↔", "BASE"),
    ("AI Opportunity", "AI", "↔", "GROW"),
    ("Software Path", "CODE", "↔", "GLOB"),
    ("Digital Infra", "GRID", "↔", "ALL"),
    ("Internet Access", "LINK", "↔", "ALL"),
    ("Digital Inclus", "ALL", "↔", "LINK"),
    ("Connectivity", "HERE", "↔", "GLOB"),
    ("Remote Work", "ONE", "↔", "GLOB"),
    ("Global Opp", "HERE", "→", "GLOB"),
    ("Global Orakzai", "ORAK", "↔", "GLOB"),
    ("Diaspora Path", "GLOB", "↔", "HOME"),
    ("Knowledge Trans", "WISE", "→", "LEAR"),
    ("Mentorship Rail", "WISE", "↔", "YOUN"),
    ("Entrepreneurship", "IDEA", "→", "BIZ"),
    ("Local Entr", "HERE", "→", "FIX"),
    ("Global Entr", "HOME", "→", "GLOB"),
    ("Small Biz Rail", "ONE", "↔", "BIZ"),
    ("Digital Commerce", "BUY", "↔", "SELL"),
    ("Cultural Product", "TRUE", "↔", "GLOB"),
    ("Creative Econ", "MAKE", "↔", "CASH"),
    ("Cultural Entr", "PAST", "↔", "NEW"),
    ("Agri Technology", "FARM", "↔", "TECH"),
    ("AI Agriculture", "AI", "↔", "FARM"),
    ("Health Tech", "DOC", "↔", "TECH"),
    ("Edu Technology", "LEAR", "↔", "TECH"),
    ("Fintech Path", "CASH", "↔", "TECH"),
    ("Digital Payment", "PAY", "↔", "SAFE"),
    ("Fin Literacy", "KNOW", "↔", "CASH"),
    ("Blockchain Rail", "GRID", "↔", "TRUE"),
    ("Digital Assets", "OWN", "↔", "NET"),
    ("Responsible Tech", "TRUE", "↔", "SAFE"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Digital Literacy", "KNOW", "↔", "TECH"),
    ("Data Protection", "DATA", "↔", "SAFE"),
    ("Digital Identity", "SELF", "↔", "TRUE"),
    ("Tech & Trust", "LINK", "↔", "TRUE"),
    ("Institutions", "ALL", "↔", "LONG"),
    ("Comm Institution", "ALL", "↔", "HELP"),
    ("Edu Institution", "LEAR", "↔", "ALL"),
    ("Scholarship Rail", "CASH", "→", "LEAR"),
    ("Skills Develop", "ABLE", "↔", "TIME"),
    ("Vocational Edu", "WORK", "↔", "LEAR"),
    ("Entr Education", "BIZ", "↔", "LEAR"),
    ("Research Path", "WHY", "↔", "TRUE"),
    ("Local Research", "HERE", "↔", "KNOW"),
    ("Cultural Res", "PAST", "↔", "TRUE"),
    ("Orakzai History", "PAST", "↔", "SAVE"),
    ("Digital Heritage", "PAST", "↔", "DATA"),
    ("Oral History", "TALK", "→", "SAVE"),
    ("Comm Consent", "YES", "↔", "SAVE"),
    ("Language Path", "TALK", "↔", "TRUE"),
    ("Digital Lang", "TALK", "↔", "NET"),
    ("Lang Preserve", "TALK", "↔", "SAVE"),
    ("Cultural Evol", "PAST", "↔", "NEXT"),
    ("Modern Identity", "PAST", "↔", "NOW"),
    ("Multi Identity", "MANY", "↔", "ONE"),
    ("Identity & Inno", "TRUE", "↔", "NEW"),
    ("Global Connect", "HERE", "↔", "GLOB"),
    ("Comm Networks", "ALL", "↔", "LINK"),
    ("Diaspora Net", "GLOB", "↔", "HOME"),
    ("Investment Path", "CASH", "→", "HOME"),
    ("Digital Sovereignty", "OWN", "↔", "RULE"),
    ("Tribal Governance", "ALL", "↔", "RULE"),
    ("Self-Determined", "SELF", "↔", "NEXT"),
    ("Meaningful Conn", "LINK", "↔", "WISE"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g181-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g181-{index}-title g181-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g181-{index}-title">{safe}</title><desc id="g181-{index}-desc">A future of Orakzai relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g181-{index}-caption" class="diagram-caption">{index}. {safe} — Future of Orakzai relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">The Future of Orakzai Framework</title><desc id="hero-desc">A diagram showing the 2026 framework for the Orakzai future, featuring digital sovereignty, meaningful connectivity, and the integration of tribal governance with AI-age infrastructure.</desc><defs><linearGradient id="h181-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h181-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE ORAKZAI FUTURE LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DIGITAL SOVEREIGNTY: TRIBAL AI GOVERNANCE</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">PAKISTAN DIGITAL INCLUSION: 8% GENDER GAP (2025)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">MEANINGFUL CONNECTIVITY & INDIGENOUS EMPOWERMENT</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DIASPORA KNOWLEDGE TRANSFER & INVESTMENT</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">SUSTAINABLE COMMUNITY DEVELOPMENT MODELS</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: CONTINUITY VIA ADAPTATION</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">FUTURE: SELF-DETERMINED, AUTHENTIC & GLOBAL</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">THE FUTURE OF ORAKZAI</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Heritage, Opportunity, Technology, and the Next Generation: Continuity through Adaptation.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Orakzai Future Loop: Navigating the 2026 landscape where digital sovereignty, meaningful connectivity, and sustainable community development ensure that tribal heritage thrives in a global digital economy.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 181</title>
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
            <p class="section-label">PAGE 181</p>
            <h2>THE FUTURE OF ORAKZAI</h2>
            <p>“Heritage, Opportunity, Technology, and the Next Generation.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “The future of any community is ultimately shaped by its people. Technology can create new opportunities, and education can expand possibilities, but technology alone does not determine the future. People do. The future of Orakzai will depend on how future generations preserve meaningful parts of their heritage while participating in the modern economy. The goal is not to preserve the past unchanged, but to achieve continuity through adaptation. Orakzai communities can carry historical memory into a future shaped by education, technology, and global connectivity.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Digital Sovereignty & Tribal Governance (2026)</h3>
                <p>By 2026, tribal nations are increasingly defining **digital sovereignty** in the AI age. Communities are leading in the governance of AI to strengthen their sovereignty and revitalize indigenous languages [1]. Exercising governance over data and AI tools allows Orakzai communities to harness technology for self-determined futures, ensuring that digital development respects tribal values and government functions [2] [3]. Meaningful connectivity and digital inclusion are the foundations of this empowered future [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pakistan's Digital Inclusion & Rural Empowerment</h3>
                <p>Pakistan has achieved significant milestones in digital inclusion, with the mobile internet gender gap narrowing to a historic low of **8% in 2025** [5]. Female internet usage surged to **45%**, reflecting a broader shift toward digital empowerment [6]. In rural areas, AI and digital literacy are being used to empower communities through e-commerce and community-centered connectivity frameworks [7]. These developments ensure that technological progress benefits not just urban centers, but all Orakzai people [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Education, AI & The Next Generation</h3>
                <p>The next generation will inherit both the opportunities and challenges of the digital age. Education in computer science, AI, and software development provides young people with the skills to participate in emerging fields like healthcare, agriculture, and finance [9]. AI-driven personalization in education is helping students who have limited access to specialized instruction [10]. Mentorship and knowledge transfer from experienced professionals and the diaspora are shortening learning curves for young Orakzai builders [11].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Economic Resilience & Global Connectivity</h3>
                <p>Orakzai's economic future will depend on a mix of local and global entrepreneurship. Digital technology allows businesses to serve international customers from Pakistan, while e-commerce connects local cultural products with wider markets [12]. Sustainable community development models integrate environmental, economic, and social factors to create a holistic strategy for progress [13] [14]. Diaspora networks contribute knowledge, investment, and professional connections, ensuring that the Global Orakzai community remains a powerful force for development [15].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: The Future of Orakzai</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, the future is the legacy we build today. We do not abandon our roots to reach the world; we use our roots to anchor our global ambition. By mastering digital sovereignty and meaningful connectivity while honoring our heritage, we are building a sovereign future that is authentic, inclusive, and enduring. We are the architects of a tomorrow where our people, our technology, and our values thrive together.”</p>
            </div>

            <div class="final-statement">
                SOVEREIGN FUTURE.<br>
                ROOTED EXCELLENCE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Brookings Institution, <em>Defining Digital Sovereignty for Tribal Nations in the AI Age (2026)</em>.</li>
                    <li>Internet Society, <em>Advancing a Connected Future for Indigenous Communities (August 2026)</em>.</li>
                    <li>NCAI / Facebook, <em>Tribal Nations Exercising Governance Over AI and Language Revitalization (July 2026)</em>.</li>
                    <li>Indian Country Today, <em>Artificial Intelligence Shaping the Future of Tribal Nations (November 2025)</em>.</li>
                    <li>MoITT / Facebook, <em>Pakistan's Mobile Internet Gender Gap Narrows to 8% (July 2026)</em>.</li>
                    <li>Instagram / ProPakistani, <em>Pakistan Milestone in Digital Inclusion: Mobile Gender Gap Surge (July 2026)</em>.</li>
                    <li>Hassan et al. / JOBS, <em>Empowering Rural Communities in Pakistan through AI and Digital Literacy (2026)</em>.</li>
                    <li>Universal Service Fund Pakistan, <em>Community-Centered Connectivity (CCC) Framework for Women (July 2026)</em>.</li>
                    <li>Wipfli Insights, <em>Tribal 2026 Trends: Gains in Digital and Automation (December 2025)</em>.</li>
                    <li>Michelson 20MM, <em>Digital Equity in Tribal Communities: Knowledge and Tools (2026)</em>.</li>
                    <li>One Community Global, <em>Sustainable Community Models: Strategies for Success (2026)</em>.</li>
                    <li>ResearchGate, <em>Sustainable Community Development Framework for Environmental Citizenship (2026)</em>.</li>
                    <li>US EPA, <em>Tools and Resources for Sustainable Communities: Best Practices (January 2026)</em>.</li>
                    <li>Sage Knowledge, <em>Sustainable Community Development: Holistic Strategy (2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Future of Orakzai and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            181
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

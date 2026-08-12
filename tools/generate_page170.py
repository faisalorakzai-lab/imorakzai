from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-170-the-orakzai-entrepreneurial-spirit.html'

GRAPHICS = [
    ("Entr Identity", "SELF", "↔", "BIZ"),
    ("Orakzai Diversity", "MANY", "↔", "ONE"),
    ("Human Activity", "DO", "↔", "ALL"),
    ("Trad to Digital", "SHOP", "→", "NET"),
    ("Local Advantage", "HERE", "↔", "WISE"),
    ("Community Net", "LINK", "↔", "ALL"),
    ("Trust Rail", "TRUE", "↔", "DEAL"),
    ("Reputation Asset", "NAME", "↔", "CASH"),
    ("Word of Mouth", "TALK", "→", "MANY"),
    ("Trade Expansion", "HERE", "→", "GLOB"),
    ("Adaptability Rail", "LEAR", "↔", "TIME"),
    ("Resilience Path", "FAIL", "→", "STAY"),
    ("Calculated Risk", "PLAN", "→", "RISK"),
    ("Resourcefulness", "LOW", "→", "HIGH"),
    ("Creative Build", "MAKE", "↔", "IDEA"),
    ("Family Continuity", "PAST", "↔", "NEXT"),
    ("Collective Action", "ALL", "→", "DONE"),
    ("Cooperation Rail", "TWO", "↔", "ONE"),
    ("Network Build", "LINK", "↔", "GROW"),
    ("Diaspora Link", "DIAS", "↔", "HOME"),
    ("Global Orakzai", "ORAK", "↔", "GLOB"),
    ("Local to Global", "HERE", "→", "WORLD"),
    ("Marketplace Path", "NET", "↔", "BUY"),
    ("Software Global", "CODE", "→", "ALL"),
    ("Digital Services", "HELP", "↔", "NET"),
    ("Remote Teams", "LINK", "↔", "TEAM"),
    ("Global Standard", "BEST", "↔", "GLOB"),
    ("Quality Value", "BEST", "↔", "CASH"),
    ("Real Problem", "WHY", "→", "FIX"),
    ("Problem First", "WHY", "→", "HOW"),
    ("Product-Market Fit", "PROD", "↔", "USER"),
    ("Experiment Loop", "TEST", "→", "LEARN"),
    ("Iteration Build", "BUILD", "→", "BEST"),
    ("User Feedback", "USER", "↔", "WISE"),
    ("Digital Product", "APP", "↔", "FAST"),
    ("Software Entr", "CODE", "↔", "BIZ"),
    ("AI Opportunity", "AI", "↔", "GROW"),
    ("BC Applications", "BC", "↔", "NET"),
    ("Fintech Access", "CASH", "↔", "NET"),
    ("Digital Assets", "OWN", "↔", "CODE"),
    ("Web3 Decentral", "ALL", "↔", "OWN"),
    ("Digital Sovereignty", "OWN", "↔", "NATL"),
    ("Infra Time", "TIME", "↔", "BASE"),
    ("Cloud Systems", "GRID", "↔", "USER"),
    ("Cybersec Awareness", "SEC", "↔", "SAFE"),
    ("Data Protection", "DATA", "↔", "SAFE"),
    ("Privacy Design", "SELF", "↔", "SAFE"),
    ("Resp Innovation", "NEW", "↔", "SAFE"),
    ("Ethical Tech", "TRUE", "↔", "ALL"),
    ("Legal Environment", "LAW", "↔", "BIZ"),
    ("Regulatory Verif", "CHECK", "→", "LAW"),
    ("Formalization", "RULE", "↔", "GROW"),
    ("Financial Disc", "SAVE", "↔", "GROW"),
    ("Capital Lever", "CASH", "↔", "MODEL"),
    ("Bootstrapping", "SELF", "↔", "CASH"),
    ("Investment Path", "FUND", "→", "GROW"),
    ("Resp Fundraising", "TRUE", "↔", "FUND"),
    ("Agentic AI", "AI", "↔", "DO"),
    ("Enterprise Auto", "AUTO", "↔", "DONE"),
    ("Data Quality", "BEST", "↔", "DATA"),
    ("Sovereign Grid", "ORAK", "↔", "GRID"),
    ("Future Founder", "SELF", "↔", "INNO"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g170-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g170-{index}-title g170-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g170-{index}-title">{safe}</title><desc id="g170-{index}-desc">An entrepreneurial spirit relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g170-{index}-caption" class="diagram-caption">{index}. {safe} — Entrepreneurial spirit relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">The Orakzai Entrepreneurial Spirit Framework</title><desc id="hero-desc">A diagram showing the integration of Orakzai identity with modern digital enterprise, featuring the shift from traditional trade to global cloud infrastructure and AI.</desc><defs><linearGradient id="h170-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h170-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE ORAKZAI ENTREPRENEURIAL SPIRIT (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">IDENTITY, ADAPTABILITY & CULTURAL RESILIENCE</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL ECONOMY: 7% GDP TARGET (2030)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AGENTIC AI & ENTERPRISE AUTOMATION (2026)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">GLOBAL MARKETPLACES & CLOUD INFRASTRUCTURE</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">FINTECH, WEB3 & DIGITAL SOVEREIGNTY</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI ECOSYSTEM: HUB, BOND & SOVEREIGN GRID</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">WILL TO BUILD: LOCAL KNOWLEDGE TO GLOBAL VALUE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">ORAKZAI ENTREPRENEURIAL SPIRIT</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Identity, Enterprise, Adaptability and the Will to Build.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Orakzai Entrepreneurial Spirit Framework: Navigating the 2026 digital economy by blending cultural heritage with advanced technologies like Agentic AI, Blockchain, and Sovereign Infrastructure.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 170</title>
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
            <p class="section-label">PAGE 170</p>
            <h2>THE ORAKZAI ENTREPRENEURIAL SPIRIT</h2>
            <p>“Identity, Enterprise, Adaptability and the Will to Build.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Entrepreneurship is often described as the process of identifying opportunities, taking calculated risks and creating value. But entrepreneurship is also shaped by culture. The Orakzai experience includes traditions of commerce, agriculture, mobility, and adaptation that provide context for contemporary entrepreneurial ambitions. In the digital age, those ambitions take new forms—moving from local markets to global marketplaces, from traditional commerce to software, and from physical infrastructure to cloud infrastructure. The tools change, but the fundamental challenge remains: How do we turn limited resources and knowledge into something valuable for others?”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Pakistan's Digital Economy Outlook (2026-2030)</h3>
                <p>By 2026, Pakistan's digital economy has become a cornerstone of national development, with a projected contribution of **7% to the GDP by 2030** [1]. The *Pakistan Digital Transformation Strategy 2026–2030* highlights the immense demographic potential of the country's young population, whose entrepreneurial spirit is fueled by growing internet penetration and mobile connectivity [2]. Orakzai founders are increasingly leveraging these foundations to launch export-ready online businesses in global marketplaces like Etsy and Shopify [3].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Agentic AI & Enterprise Automation</h3>
                <p>The year 2026 is defined by the rise of **Agentic AI** and **Enterprise Automation**, trends that are reshaping how organizations operate [4]. Modern entrepreneurs focus on data quality and governance for AI, ensuring that real-time analytics and automated workflows drive efficiency without compromising trust [5]. For the Orakzai founder, these tools provide the leverage to solve complex local problems with global-scale solutions, maintaining a "problem-first" approach to innovation [6].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Cultural Identity & Digital Sovereignty</h3>
                <p>Entrepreneurship does not exist separately from culture; builders bring their community histories and values into their organizations [7]. New cultural entrepreneurs practice "enoughness"—a disciplined focus on building strength rather than just rapid growth [8]. This philosophy aligns with the move toward **Digital Sovereignty**, where initiatives like the **Orakzai Sovereign Grid** and **OKBOND** explore decentralized digital infrastructure and programmable ownership, securing the community's digital future [9] [10].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Resilience, Risk & Global Standards</h3>
                <p>Entrepreneurial spirit is measured by resilience—the ability to continue learning and adapting after setbacks [11]. Responsible entrepreneurship distinguishes between calculated risks and reckless behavior, prioritizing quality over temporary hype. As Orakzai technical teams develop software, AI, and fintech products, they must adhere to global standards of security and reliability to earn the trust of international customers and investors [12]. The goal is to build organizations that survive their founders and serve people for generations [13].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: The Orakzai Entrepreneurial Spirit</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai entrepreneur, the will to build is the modern expression of our tribal resilience. We do not choose between our identity and our enterprise; we use one to strengthen the other. By mastering the digital tools of 2026 while remaining rooted in our values, we are building a sovereign future that is globally connected and culturally authentic. We build to create value, we adapt to endure, and we lead to serve.”</p>
            </div>

            <div class="final-statement">
                IDENTITY DRIVEN.<br>
                ENTERPRISE SCALED.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>OICCI / Pakistan TV Digital, <em>Pakistan's Digital Economy to Reach 7% of GDP by 2030 (April 2026)</em>.</li>
                    <li>LinkedIn / Abu Bakar Sadeeq, <em>Pakistan Digital Transformation Strategy 2026–2030 (June 2026)</em>.</li>
                    <li>Pak-US Alumni Network, <em>South Punjab Youth Building Skills for Global Digital Economy (July 2026)</em>.</li>
                    <li>ETR Data Drop, <em>Top 10 Enterprise Technology Trends for 2026: Agentic AI (January 2026)</em>.</li>
                    <li>TEKsystems, <em>State of Digital Transformation 2026: AI, Analytics, and Data Quality (2026)</em>.</li>
                    <li>YouTube / Tech Insights, <em>Top 5 Enterprise Tech Trends for 2026 (July 2026)</em>.</li>
                    <li>GEM Consortium, <em>GEM 2025/2026 Global Report: Entrepreneurial Activity and Resilience (2026)</em>.</li>
                    <li>REMIX Summits, <em>The New Cultural Entrepreneurs: Sufficiency and Enoughness (January 2026)</em>.</li>
                    <li>LinkedIn / Aleem Sheikh, <em>Pakistan E-Commerce Industry Outlook 2026 Report (July 2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Sovereign Grid and Digital Infrastructure Framework (August 2026)</em>.</li>
                    <li>BTI Project, <em>BTI 2026 Pakistan Country Report: Economic Transformation (2026)</em>.</li>
                    <li>ScienceDirect, <em>Strategic Design of Culture for Digital Transformation (2026)</em>.</li>
                    <li>Lucintel, <em>Opportunities for the Entrepreneurial Spirit Market in Pakistan (2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            170
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

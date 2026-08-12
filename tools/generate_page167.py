from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-167-young-founders-and-global-ambition.html'

GRAPHICS = [
    ("New Gen Founders", "YOUN", "↔", "TECH"),
    ("Age vs Model", "AGE", "≠", "BIZ"),
    ("Experience Build", "LEAR", "→", "DONE"),
    ("Curiosity Path", "WHY", "↔", "NEW"),
    ("Learning Speed", "TIME", "→", "KNOW"),
    ("Build vs Permission", "MAKE", "→", "TEST"),
    ("Small Start", "ONE", "→", "MANY"),
    ("Validation Loop", "TEST", "↔", "TRUE"),
    ("Customer First", "USER", "↔", "HELP"),
    ("Product-Market Fit", "PROD", "↔", "USER"),
    ("Tech Leverage", "TECH", "↔", "MANY"),
    ("Software Scale", "CODE", "→", "ALL"),
    ("Cloud Scale", "GRID", "↔", "GROW"),
    ("AI Dev Tool", "AI", "→", "CODE"),
    ("AI-Native Co", "AI", "↔", "BASE"),
    ("BC Entr", "BC", "↔", "IDEA"),
    ("Digital Assets", "OWN", "↔", "CODE"),
    ("Fintech Opp", "CASH", "↔", "NET"),
    ("E-commerce Reach", "BUY", "↔", "GLOB"),
    ("Global-First", "GLOB", "↔", "IDEA"),
    ("Local to Global", "HERE", "→", "GLOB"),
    ("Global Customer", "USER", "↔", "GLOB"),
    ("International Std", "BEST", "↔", "GLOB"),
    ("Brand Trust", "NAME", "↔", "TRUE"),
    ("Digital Presence", "NET", "↔", "NAME"),
    ("Reputation Path", "TRUE", "→", "TRUST"),
    ("Evidence vs Hype", "FACT", "≠", "TALK"),
    ("Public Building", "SHOW", "↔", "ALL"),
    ("Open Source", "OPEN", "↔", "CODE"),
    ("Global Community", "LINK", "↔", "ALL"),
    ("Remote Entr", "HERE", "↔", "GLOB"),
    ("Global Teams", "ALL", "↔", "TEAM"),
    ("Pakistan Talent", "HOME", "↔", "BEST"),
    ("Diaspora Bridge", "DIAS", "↔", "HOME"),
    ("Know Transfer", "WISE", "↔", "LINK"),
    ("Capital Scale", "CASH", "→", "BIG"),
    ("Bootstrapping", "SELF", "↔", "CASH"),
    ("Investment Path", "FUND", "→", "GROW"),
    ("Due Diligence", "CHECK", "→", "DEAL"),
    ("Financial Disc", "SAVE", "↔", "GROW"),
    ("Revenue Evidence", "CASH", "↔", "TRUE"),
    ("Unit Economics", "COST", "↔", "GAIN"),
    ("Scalability", "ONE", "↔", "MANY"),
    ("Team Attraction", "BEST", "→", "TEAM"),
    ("Company Culture", "TEAM", "↔", "WISE"),
    ("Leadership Resp", "SELF", "↔", "ALL"),
    ("Delegation Path", "SELF", "→", "TEAM"),
    ("System Build", "SYS", "↔", "DONE"),
    ("Institutional Goal", "ALL", "↔", "LONG"),
    ("Failure Info", "FAIL", "→", "DATA"),
    ("Learning Failure", "FAIL", "→", "WISE"),
    ("Resilience Path", "TIME", "↔", "TRUE"),
    ("Risk Uncertainty", "RISK", "↔", "TIME"),
    ("Calculated Risk", "PLAN", "→", "RISK"),
    ("Resp Ambition", "GROW", "↔", "SAFE"),
    ("Ethics Consideration", "TRUE", "↔", "ALL"),
    ("Responsible AI", "AI", "↔", "SAFE"),
    ("Cybersecurity First", "SEC", "↔", "BASE"),
    ("Data Protection", "DATA", "↔", "SAFE"),
    ("Legal Operation", "LAW", "↔", "BIZ"),
    ("Global Compliance", "GLOB", "↔", "LAW"),
    ("Governance Goal", "ALL", "↔", "RULE"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g167-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g167-{index}-title g167-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g167-{index}-title">{safe}</title><desc id="g167-{index}-desc">A young founder and global ambition relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g167-{index}-caption" class="diagram-caption">{index}. {safe} — Young founder and global ambition relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Young Founders & Global Ambition Framework</title><desc id="hero-desc">A diagram showing the pathway for a new generation of founders to build AI-native, global-first companies using technology as leverage while maintaining resilience and discipline.</desc><defs><linearGradient id="h167-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h167-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE FOUNDER-SCALE PATHWAY (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AI-NATIVE FOUNDATIONS ($15B GLOBAL VC 2025)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">VALIDATION: ONE PROBLEM → ONE PRODUCT</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">PAKISTAN STARTUP ECOSYSTEM ($74M+ FUNDING)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">GLOBAL-FIRST AMBITION & INTERNATIONAL STDS</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">RESILIENCE, DISCIPLINE & ETHICAL GOVERNANCE</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">DIASPORA BRIDGES & KNOWLEDGE TRANSFER</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN VENTURE: BEYOND BORDERS</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">YOUNG FOUNDERS & GLOBAL AMBITION</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“A Generation Building Beyond Borders with Resilience and Leverage.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Founder-Scale Pathway: Navigating the 2026 digital economy through AI-native design, rapid validation, and global-first execution for a new generation of Orakzai founders.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 167</title>
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
            <p class="section-label">PAGE 167</p>
            <h2>YOUNG FOUNDERS & GLOBAL AMBITION</h2>
            <p>“A Generation Building Beyond Borders.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Entrepreneurship has always involved ambition, but the digital economy has changed what young founders can attempt. A founder no longer needs a large factory or a major physical office; a laptop, an internet connection, technical skills and a clear understanding of a problem can be enough to begin. This does not make entrepreneurship easy—building a company still requires discipline, capital, talent, and resilience. The difference is that technology has expanded the potential reach of a small team. For young founders in Pakistan, this creates an important opportunity: they can build locally while thinking globally.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The AI-Native Generation (2026)</h3>
                <p>By 2026, a new wave of "AI-native" startups has emerged, designed around artificial intelligence from their earliest stages. Global funding for AI-native companies increased by **17%** in 2025, reaching **$15 billion** even as broader tech investment recalibrated [1]. These founders use AI not just as a feature, but as a core development tool for coding, research, and customer support, allowing small teams to achieve unprecedented leverage and scale [2] [3].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pakistan's Emerging Ecosystem</h3>
                <p>Pakistan's startup ecosystem entered a new phase of growth in 2026, with local startups securing over **$74 million** in funding [4]. The *Pakistan Startup Fund* and an increase in equity deals reflect a growing confidence in the country's young technology workforce. Founders are increasingly moving beyond freelancing to build product-centric ventures in fintech, e-commerce, and blockchain, using Pakistan as a base for global expansion [5] [6].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Validation, Leverage & Global Standards</h3>
                <p>Modern entrepreneurship prioritizes "building before permission" through rapid prototyping and validation. By focusing on one problem, one product, and one customer, founders can achieve product-market fit before committing significant resources. However, global ambition requires global standards; international customers expect quality, security, and responsive communication. Branding and digital presence serve to communicate trust, but they cannot replace the foundational requirement of product excellence [7] [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Resilience, Ethics & Governance</h3>
                <p>Building a long-term institution requires more than just technical skill; it requires leadership, delegation, and financial discipline. As startups scale, founders must implement systems for engineering, compliance, and operations. Furthermore, responsible ambition demands attention to ethics, including privacy, cybersecurity, and AI accuracy. For the Orakzai founder, resilience is the ability to treat failure as information and continue adapting under the uncertainty of the global marketplace [9] [10].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Young Founders & Global Ambition</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the new generation of Orakzai founders, ambition is the engine and technology is the lever. We do not build for the local market alone; we build for the world. By maintaining our cultural identity while mastering international standards of governance and execution, we are securing a sovereign future. We are the generation that builds beyond borders.”</p>
            </div>

            <div class="final-statement">
                BUILD BEYOND.<br>
                THINK GLOBAL.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Startup Genome, <em>The Global Startup Ecosystem Report 2026: AI-Native Funding Trends (2026)</em>.</li>
                    <li>Founder Institute, <em>The AI-Native Founder's Guide: Building in 2026 (July 2026)</em>.</li>
                    <li>Fortune Business Insights, <em>Global Artificial Intelligence Market Projections 2026-2034 (2026)</em>.</li>
                    <li>LinkedIn / Azfar, <em>Pakistan Startup Ecosystem Outlook 2026: Funding and Governance (2026)</em>.</li>
                    <li>Pakistan Startup Fund, <em>Annual Report on Local Tech Investment and Growth (2026)</em>.</li>
                    <li>Y Combinator, <em>Requests for Startups 2026: Rebuilding the Real World with AI (2026)</em>.</li>
                    <li>Harvard Business School, <em>AI-Native Firms: Performance and Posting Trends (2026)</em>.</li>
                    <li>AWS Startups, <em>Engines of Growth: AI-Native Startups and Modern Infrastructure (June 2026)</em>.</li>
                    <li>Forbes, <em>2026 AI 50 List: Spotlight on Promising AI Businesses (August 2026)</em>.</li>
                    <li>Vention Teams, <em>State of AI 2026: Market Size, Investment, and Industry Data (September 2025)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            167
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

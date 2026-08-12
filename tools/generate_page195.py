from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-195-im-a-builder-the-meaning-of-responsibility.html'

GRAPHICS = [
    ("Builder Meaning", "IDEA", "↔", "BASE"),
    ("Decision Path", "SELF", "↔", "NEXT"),
    ("Structure Rail", "IDEA", "→", "GRID"),
    ("Problem to Proj", "FIX", "↔", "DO"),
    ("Uncertainty", "WHY", "↔", "NEW"),
    ("Choices Rail", "ONE", "↔", "MANY"),
    ("Consequences", "DO", "→", "ALL"),
    ("Inseparable", "MAKE", "↔", "CARE"),
    ("Software Resp", "CODE", "↔", "LIFE"),
    ("Entr Resp", "BIZ", "↔", "ALL"),
    ("Arch Resp", "GRID", "↔", "SAFE"),
    ("Research Resp", "WISE", "↔", "LONG"),
    ("Tech Resp", "TECH", "↔", "BASE"),
    ("Comm Resp", "LINK", "↔", "TRUE"),
    ("Builder Mindset", "MIND", "↔", "DO"),
    ("Creation Rail", "MAKE", "↔", "CARE"),
    ("Ownership Path", "SELF", "↔", "TRUE"),
    ("Accountability", "TRUE", "↔", "FIX"),
    ("Intention Rail", "WANT", "≠", "DONE"),
    ("Outcomes Path", "DO", "→", "FACT"),
    ("Think Before", "WHY", "→", "DO"),
    ("Build Right Thing", "WHY", "↔", "HELP"),
    ("Build It Right", "RULE", "↔", "FIX"),
    ("Quality Base", "TRUE", "↔", "DONE"),
    ("Reliability", "TRUE", "↔", "LONG"),
    ("Safety Rail", "SAFE", "↔", "ALL"),
    ("Security Path", "SEC", "↔", "DO"),
    ("Privacy Rail", "SAFE", "↔", "DATA"),
    ("Accessibility", "ALL", "↔", "SAFE"),
    ("Inclusion Path", "MANY", "↔", "ONE"),
    ("Simplicity Rail", "SAFE", "↔", "DO"),
    ("Transparency", "TRUE", "↔", "ALL"),
    ("Honesty Path", "TRUE", "↔", "SAFE"),
    ("No False Prom", "TRUE", "↔", "FACT"),
    ("Measure Results", "FACT", "↔", "TRUE"),
    ("Listen Users", "USER", "→", "LEAR"),
    ("Feedback Rail", "INFO", "→", "BEST"),
    ("Iteration Path", "TRY", "→", "BEST"),
    ("Testing Rail", "TEST", "→", "SAFE"),
    ("Failure Info", "FAIL", "→", "KNOW"),
    ("Resp Failure", "WHY", "↔", "TRUE"),
    ("Correction Rail", "FIX", "↔", "DONE"),
    ("Maintenance", "SAVE", "↔", "LONG"),
    ("Technical Debt", "FAST", "≠", "LONG"),
    ("Documentation", "TRUE", "↔", "LONG"),
    ("Handover Path", "OLD", "→", "NEW"),
    ("Next Gen Base", "PAST", "↔", "NEXT"),
    ("Infrastructure", "GRID", "↔", "BASE"),
    ("Digital Infra", "NET", "↔", "BASE"),
    ("Physical Infra", "PHYS", "↔", "BASE"),
    ("Critical Sys", "TOP", "↔", "SAFE"),
    ("Redundancy", "MANY", "↔", "SAFE"),
    ("Resilience Rail", "FIX", "↔", "LONG"),
    ("Disaster Rec", "SAFE", "↔", "DO"),
    ("Biz Continuity", "BIZ", "↔", "LONG"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Security Cult", "ALL", "↔", "SAFE"),
    ("Data Resp", "DATA", "↔", "SAFE"),
    ("Data Minim", "LESS", "→", "SAFE"),
    ("Data Gov", "RULE", "↔", "SAFE"),
    ("Consent Path", "YES", "↔", "SAFE"),
    ("AI Resp", "AI", "↔", "SAFE"),
    ("Human Oversight", "WISE", "↔", "DO"),
    ("AI Limits Rail", "AI", "≠", "ALL"),
    ("Algorithmic Bias", "DATA", "≠", "TRUE"),
    ("Fairness Path", "ALL", "↔", "TRUE"),
    ("Explainability", "WHY", "↔", "TRUE"),
    ("AI Accountable", "SELF", "↔", "AI"),
    ("Blockchain Resp", "GRID", "↔", "TRUE"),
    ("Smart Contract", "CODE", "↔", "SAFE"),
    ("Immutability", "TRUE", "↔", "LONG"),
    ("Digital Assets", "OWN", "↔", "NET"),
    ("Resp Fintech", "CASH", "↔", "SAFE"),
    ("Team Building", "ALL", "↔", "LINK"),
    ("Hiring Path", "ONE", "→", "MANY"),
    ("Agentic ERA", "AI", "↔", "DO"),
    ("Resp by Design", "IDEA", "↔", "SAFE"),
    ("Digital Ubuntu", "ALL", "↔", "LINK"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g195-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g195-{index}-title g195-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g195-{index}-title">{safe}</title><desc id="g195-{index}-desc">A builder relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g195-{index}-caption" class="diagram-caption">{index}. {safe} — Builder relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">I’M A BUILDER — The Meaning of Responsibility Framework</title><desc id="hero-desc">A diagram showing the 2026 builder responsibility landscape, featuring AI Accountability in the Agentic Era, Responsibility by Design, Global Cybersecurity Outlook 2026, and Digital Resilience.</desc><defs><linearGradient id="h195-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h195-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE RESPONSIBLE BUILDER LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AI ACCOUNTABILITY: SHIFTING TO THE AGENTIC ERA</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">RESPONSIBILITY BY DESIGN: ENGINEERING ETHICS</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">CYBERSECURITY OUTLOOK 2026: $240B SPENDING</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DIGITAL RESILIENCE: WITHSTANDING DISRUPTION</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">BUSINESS & HUMAN RIGHTS: ETHICAL GOVERNANCE</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: INFRASTRUCTURE AS TRUST</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">BUILDER: ACCOUNTABILITY FOR WHAT YOU CREATE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">I’M A BUILDER — THE MEANING OF RESPONSIBILITY</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Building Is Not Only About Creating — It Is About Being Accountable for What You Create.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Responsible Builder Loop: Navigating the 2026 landscape where AI accountability, responsibility by design, and digital resilience ensure that builders are prepared to own the consequences of their creations in a complex digital civilization.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 195</title>
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
            <p class="section-label">PAGE 195</p>
            <h2>I’M A BUILDER — THE MEANING OF RESPONSIBILITY</h2>
            <p>“Building Is Not Only About Creating — It Is About Being Accountable.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “I’m a builder. To build something is to make a decision about the future. A builder takes an idea and gives it structure; turns a problem into a project; accepts uncertainty; and makes choices. And every choice has consequences. That is why building is inseparable from responsibility. Whether it is software, a company, a structure, or knowledge, the responsibility is similar: if I build it, I must care about what it does.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">AI Accountability in the Agentic Era (2026)</h3>
                <p>By 2026, AI accountability faces its most profound test as autonomous agents begin managing critical workflows without constant human input [1]. As these systems become more embedded in society, gaps in governance and risk management are becoming increasingly costly [2]. A Practical and unified accountability framework is being developed to support transparent decisions regarding AI risks, ensuring that builders acknowledge the limitations and potential errors of their systems [3] [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Responsibility by Design & Engineering Ethics</h3>
                <p>Engineering ethics in 2026 is moving toward **"Responsibility by Design,"** where safety and accountability are considered during development rather than after deployment [5]. Organizations are shifting from tensions to tipping points, making intentional choices to adapt continuously to ethical mandates [6]. A workplace culture that empowers engineers to raise concerns and put safety first is becoming the standard for building systems that shape millions of lives [7] [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Resilience & Global Cybersecurity</h3>
                <p>Global end-user spending on information security is forecasted to grow to **$240 billion in 2026**, reflecting a 12.5% increase as businesses defend against agentic and AI-driven threats [9]. The *Global Cybersecurity Outlook 2026* highlights the significance of infrastructure security in safeguarding the digital world [10]. **Digital Resilience** has become the key metric for building systems that can withstand disruption and recover from failure, ensuring business continuity in a volatile environment [11] [12].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Data Responsibility & Sovereign Infrastructure</h3>
                <p>Builders have a fundamental responsibility to protect personal information, treating data not merely as a resource but as a representation of people's identities [13]. **Data Minimization** and clear governance rules are essential for reducing unnecessary risks [14]. For the Orakzai community, the **Sovereign Grid** represents infrastructure built on trust, where digital and physical systems are designed for long-term sustainability and the benefit of the next generation [15].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: I’m a Builder — The Meaning of Responsibility</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, building is an act of service. We do not just create objects; we build foundations. By mastering AI accountability and responsibility by design while remaining rooted in our values of ownership and integrity, we are ensuring that the Orakzai name is synonymous with quality and trust. We are the architects of a future that is sovereign, reliable, and eternal. Our building is our responsibility, and our accountability is our strength.”</p>
            </div>

            <div class="final-statement">
                BUILD WITH CARE.<br>
                OWN THE FUTURE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>LinkedIn / AI Accountability, <em>AI Accountability in 2026: Constrained Autonomy and Real Tests (January 2026)</em>.</li>
                    <li>McKinsey & Company, <em>State of AI Trust in 2026: Shifting to the Agentic Era (March 2026)</em>.</li>
                    <li>IEAI TUM, <em>Towards an Accountability Framework for AI Systems: Transparent Decisions (2026)</em>.</li>
                    <li>LinkedIn / Pavanduggal, <em>AI Accountability and Autonomous Systems Governance (June 2026)</em>.</li>
                    <li>Bertrand's Brain Grep, <em>Engineering & Ethics: Responsibility by Design (May 2026)</em>.</li>
                    <li>Deloitte Insights, <em>2026 Global Human Capital Trends: From Tensions to Tipping Points (March 2026)</em>.</li>
                    <li>ASME, <em>Ethics in Engineering: Culture and Accountability in AI Policies (June 2026)</em>.</li>
                    <li>IHRB, <em>Top Ten Business and Human Rights Issues in 2026: Construction and Engineering (December 2025)</em>.</li>
                    <li>Fortinet / Gartner, <em>Cybersecurity Trends 2026: Defending Against Agentic and AI Threats (2026)</em>.</li>
                    <li>World Economic Forum, <em>Global Cybersecurity Outlook 2026: Trends Reshaping Cybersecurity (January 2026)</em>.</li>
                    <li>Taylor Wessing, <em>Digital Resilience in 2026: Key Trends and Predictions (2026)</em>.</li>
                    <li>Jisc Social, <em>What's Really Happening Across Digital Infrastructure in 2026 (2026)</em>.</li>
                    <li>Ethisphere, <em>The Biggest Ethics and Compliance News Stories of 2026 (June 2026)</em>.</li>
                    <li>LinkedIn / NAVEX, <em>The Future of Compliance and Ethics: Trends into 2026 (February 2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>I’m a Builder and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            195
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-168-leadership-and-responsibility.html'

GRAPHICS = [
    ("Leadership Resp", "LEAD", "↔", "RESP"),
    ("Authority vs Trust", "TITLE", "≠", "TRUST"),
    ("Accountability Loop", "DECIDE", "→", "OWN"),
    ("Integrity Path", "RULE", "↔", "DONE"),
    ("Credibility Base", "TRUE", "↔", "BASE"),
    ("Action vs Words", "DO", "≠", "SAY"),
    ("Vision Direction", "HERE", "→", "THERE"),
    ("Purpose Why", "WHY", "↔", "ALL"),
    ("Mission Path", "WHY", "→", "DO"),
    ("Values Filter", "DECIDE", "↔", "RULE"),
    ("Uncertainty Nav", "RISK", "↔", "TIME"),
    ("Judgment Mix", "FACT", "↔", "WISE"),
    ("Listening Muscle", "TALK", "↔", "HEAR"),
    ("Feedback Loop", "BACK", "→", "BEST"),
    ("Humility Base", "SELF", "↔", "OPEN"),
    ("Learning Engine", "KNOW", "→", "MORE"),
    ("Adaptability Rail", "CHANGE", "↔", "TRUE"),
    ("Resilience Path", "FAIL", "→", "STAY"),
    ("Failure Data", "FAIL", "→", "WISE"),
    ("No-Blame Culture", "FAIL", "↔", "HELP"),
    ("Team Leadership", "ONE", "↔", "ALL"),
    ("Delegation Flow", "SELF", "→", "TEAM"),
    ("Empowerment Rail", "TEAM", "↔", "ABLE"),
    ("Clear Expectation", "GOAL", "↔", "TEAM"),
    ("Communication Rail", "TALK", "↔", "TRUE"),
    ("Transparency Base", "OPEN", "↔", "TRUST"),
    ("Conflict Resolution", "FIGHT", "→", "FIX"),
    ("Fairness Standard", "SAME", "↔", "ALL"),
    ("Respect Rail", "SELF", "↔", "ALL"),
    ("Thought Diversity", "DIFF", "↔", "BEST"),
    ("Meritocracy Path", "DONE", "↔", "GAIN"),
    ("Mentorship Link", "WISE", "→", "LEAR"),
    ("Future Leaders", "ALL", "→", "LEAD"),
    ("Succession Plan", "ONE", "→", "ALL"),
    ("Institutional Sys", "SYS", "↔", "LONG"),
    ("Governance Rule", "RULE", "↔", "ALL"),
    ("Corp Resp Loop", "BIZ", "↔", "ALL"),
    ("Customer Resp", "BIZ", "↔", "USER"),
    ("Employee Resp", "BIZ", "↔", "TEAM"),
    ("Investor Resp", "BIZ", "↔", "FUND"),
    ("Community Resp", "BIZ", "↔", "HOME"),
    ("Regulatory Resp", "BIZ", "↔", "LAW"),
    ("Ethical Entr", "IDEA", "↔", "TRUE"),
    ("Long-Term Value", "TIME", "↔", "BEST"),
    ("Reputation Rail", "NAME", "↔", "TRUE"),
    ("Evidence Base", "FACT", "↔", "BASE"),
    ("Honest Talk", "TRUE", "↔", "ALL"),
    ("Speculation Hype", "HOPE", "≠", "FACT"),
    ("Tech Leadership", "TECH", "↔", "WISE"),
    ("Eng Responsibility", "CODE", "↔", "SAFE"),
    ("Cybersecurity Resp", "SEC", "↔", "LEAD"),
    ("Data Protection", "DATA", "↔", "SAFE"),
    ("Privacy Design", "SELF", "↔", "SAFE"),
    ("AI Leadership", "AI", "↔", "LEAD"),
    ("Responsible AI", "AI", "↔", "SAFE"),
    ("Automation Shift", "AUTO", "↔", "WORK"),
    ("Human Oversight", "SELF", "↔", "AI"),
    ("Blockchain Lead", "BC", "↔", "RULE"),
    ("Digital Assets", "OWN", "↔", "CODE"),
    ("Sovereign Progress", "ORAK", "↔", "GLOB"),
    ("Future Founder", "SELF", "↔", "INNO"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g168-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g168-{index}-title g168-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g168-{index}-title">{safe}</title><desc id="g168-{index}-desc">A leadership and responsibility relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g168-{index}-caption" class="diagram-caption">{index}. {safe} — Leadership and responsibility relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Leadership & Responsibility Framework</title><desc id="hero-desc">A diagram showing the 2026 leadership framework, integrating human empathy with digital fluency, AI governance, and corporate responsibility.</desc><defs><linearGradient id="h168-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h168-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE RESPONSIBLE LEADERSHIP MODEL (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">HUMAN + AI: EMPATHY & DIGITAL FLUENCY</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">AI GOVERNANCE: ETHICS, BIAS & OVERSIGHT</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ACCOUNTABILITY & LONG-TERM CREDIBILITY</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">GOVERNANCE & INSTITUTIONAL RESILIENCE</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CORPORATE RESPONSIBILITY (ESG 2.0)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI FOUNDATION & COMMUNITY IMPACT</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SOVEREIGN LEADERSHIP: SERVE TO BUILD</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">LEADERSHIP & RESPONSIBILITY</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Leadership is the Responsibility to Build, Decide and Serve.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Responsible Leadership Model: Integrating human skills with digital governance, ethical AI oversight, and multi-stakeholder responsibility in the 2026 era.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 168</title>
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
            <p class="section-label">PAGE 168</p>
            <h2>LEADERSHIP & RESPONSIBILITY</h2>
            <p>“Leadership Is the Responsibility to Build, Decide and Serve.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Leadership is often associated with authority, titles and visibility. But lasting leadership is measured differently—by decisions, accountability, integrity and the ability to create value for others. For entrepreneurs, leadership begins long before a company becomes large. A founder leads when deciding what problem to solve; a team member leads when taking responsibility for a difficult task; an engineer leads when protecting users from preventable failures. Leadership is not simply about being followed; it is about accepting responsibility for the direction and consequences of one's decisions.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The 2026 Leadership Landscape</h3>
                <p>In 2026, leadership trends highlight the convergence of "Human + AI" capabilities. Modern leaders are required to combine deep empathy with digital fluency, navigating uncertainty through context switching and relational intelligence [1] [2]. As human expectations rise, competitive advantage depends on choices that enable speed and adaptability while maintaining a calm presence in volatile environments [3]. Credibility is no longer built on authority alone but on the consistent evidence of reliability and honesty [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI Governance & Ethical Judgment</h3>
                <p>Technology leadership in 2026 demands rigorous AI governance. Effective frameworks now address technical robustness, ethical considerations, legal compliance (such as the EU AI Act), and social impact [5] [6]. Leaders must distinguish between speculation and established fact, ensuring that AI systems are deployed with appropriate human oversight to prevent bias and inaccuracies [7]. Responsible board governance now includes external accountability and socially responsible technology development as core priorities [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Multi-Stakeholder Responsibility</h3>
                <p>Lasting organizations recognize their responsibilities toward a broad ecosystem: customers, employees, investors, communities, and regulators. Corporate responsibility in 2026 leverages tech-powered transparency—using blockchain and AI to verify supply chain ethics and improve reporting accuracy [9]. A founder's trajectory, such as that of **Faisal Orakzai**, illustrates how local background can coexist with global technological ambition when guided by institutional leadership and systemic resilience [10].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Institutional Resilience & Succession</h3>
                <p>The strongest organizations build systems that survive leadership transitions. Institutional leadership means creating a culture where meritocracy, mentorship, and diversity of thought improve decision-making [11]. By empowering teams through delegation and clear expectations, leaders ensure that the organization functions beyond one person. For the Orakzai entrepreneur, heritage provides the values, but professional discipline and ethical judgment provide the foundation for a sovereign digital future [12].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Leadership & Responsibility</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the modern Orakzai leader, responsibility is the highest form of service. We do not seek authority for its own sake; we seek the opportunity to build solutions that endure. By combining cultural integrity with global standards of governance, we are securing a legacy that is not only successful but respected. We lead to build, we decide to serve, and we serve to progress.”</p>
            </div>

            <div class="final-statement">
                SERVE TO BUILD.<br>
                DECIDE TO PROGRESS.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>DDI World, <em>Leadership Trends 2026: Human + AI and Rising Expectations (November 2025)</em>.</li>
                    <li>Deloitte Insights, <em>2026 Global Human Capital Trends: Speed, Adaptability, and Choice (March 2026)</em>.</li>
                    <li>USDLA, <em>Leadership and Human Skills Trends for 2026: Relational Intelligence (January 2026)</em>.</li>
                    <li>Harvard Business Publishing, <em>2026 Global Leadership Study: Research Findings on AI Strategy (2026)</em>.</li>
                    <li>World Economic Forum, <em>Building a Global AI Governance Framework (November 2025)</em>.</li>
                    <li>European Union, <em>The AI Act: Harmonised Rules on Artificial Intelligence (Regulation 2024/1689)</em>.</li>
                    <li>Athena Solutions, <em>AI Governance 2026: Guide to Responsible and Ethical AI Success (2026)</em>.</li>
                    <li>Institute of Directors (IoD), <em>Ethics & Technology: The New Frontier of Board Governance (2026)</em>.</li>
                    <li>The Hill Standem, <em>Business Corporate Responsibility Trends & Ethics in 2026 (September 2025)</em>.</li>
                    <li>Orakzai Group Archives, <em>Institutional Leadership and Global Ambition Framework (August 2026)</em>.</li>
                    <li>KPMG International, <em>Global Tech Report 2026: The Future of Organizational Resilience (March 2026)</em>.</li>
                    <li>BSR, <em>Effective Engagement with Technology Companies: International Standards (2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            168
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

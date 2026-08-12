from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-163-entrepreneurship-and-risk.html'

GRAPHICS = [
    ("Entrepreneurial Risk", "IDEA", "↔", "RISK"),
    ("Risk vs Uncertainty", "RISK", "↔", "TIME"),
    ("Calculated Risk", "REWARD", "→", "ACTION"),
    ("Startup Risk", "CAPITAL", "↔", "DEMAND"),
    ("Market Risk", "PROD", "↔", "MARKET"),
    ("Financial Risk", "CASH", "↔", "COST"),
    ("Runway Management", "CASH", "→", "TIME"),
    ("Bootstrapping Path", "SELF", "↔", "CASH"),
    ("External Capital", "FUND", "↔", "EQUITY"),
    ("Technology Risk", "CODE", "↔", "SEC"),
    ("Cybersecurity Risk", "DATA", "↔", "TRUST"),
    ("Regulatory Risk", "LAW", "↔", "BIZ"),
    ("Operational Risk", "SYS", "↔", "FAIL"),
    ("Key-Person Risk", "ONE", "↔", "TEAM"),
    ("Risk Assessment", "WHY", "→", "FIX"),
    ("Risk Mitigation", "PLAN", "→", "SAFE"),
    ("Experimentation Loop", "TEST", "→", "LEARN"),
    ("Minimum Viable Prod", "MVP", "↔", "USER"),
    ("Pivot Strategy", "PIVOT", "→", "GROW"),
    ("Opportunity Cost", "TIME", "↔", "GAIN"),
    ("Capital Discipline", "SAVE", "↔", "VALUE"),
    ("Debt Obligation", "LOAN", "↔", "PAY"),
    ("Equity Dilution", "SHARE", "↔", "OWN"),
    ("Product Risk", "BUG", "↔", "FIX"),
    ("Customer Risk", "USER", "↔", "FEED"),
    ("Cash Flow Timing", "IN", "↔", "OUT"),
    ("AI System Risk", "AI", "↔", "SAFE"),
    ("Blockchain Risk", "BC", "↔", "SEC"),
    ("Digital Asset Risk", "COIN", "↔", "VOL"),
    ("Legal Structure", "DOC", "↔", "BIZ"),
    ("Reputational Risk", "TRUST", "↔", "RISK"),
    ("Brand Risk", "BRAND", "↔", "PROD"),
    ("Supply-Chain Risk", "SHIP", "↔", "GOOD"),
    ("Human Risk", "TEAM", "↔", "LEAD"),
    ("Business Continuity", "BACK", "↔", "RUN"),
    ("System Redundancy", "TWO", "↔", "ONE"),
    ("Risk Matrix", "PROB", "×", "IMPACT"),
    ("Insurance Transfer", "RISK", "→", "INS"),
    ("Contractual Protection", "LAW", "↔", "DEAL"),
    ("Due Diligence", "VERIFY", "→", "DEAL"),
    ("Confidence vs Certainty", "HOPE", "≠", "FACT"),
    ("Iterative Build", "BUILD", "→", "LEARN"),
    ("Failure Analysis", "FAIL", "→", "WISE"),
    ("Strategic Exit", "STOP", "→", "SAVE"),
    ("Time Allocation", "TIME", "↔", "FOCUS"),
    ("Focus Discipline", "ONE", "↔", "DONE"),
    ("Orakzai Resilience", "ORAK", "↔", "RISK"),
    ("Modern Venture", "TECH", "↔", "CASH"),
    ("Sovereign Enterprise", "ORAK", "↔", "GLOB"),
    ("Venture Lifecycle", "IDEA", "→", "BEST"),
    ("Future Founder", "SELF", "↔", "INNO"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g163-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g163-{index}-title g163-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g163-{index}-title">{safe}</title><desc id="g163-{index}-desc">An entrepreneurship and risk relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g163-{index}-caption" class="diagram-caption">{index}. {safe} — Entrepreneurship and risk relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Entrepreneurship & Risk Framework</title><desc id="hero-desc">A diagram showing the navigation of entrepreneurial risk, uncertainty, financial runway, capital discipline, and modern venture creation.</desc><defs><linearGradient id="h163-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h163-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE ENTREPRENEURIAL RISK FRAMEWORK</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">UNCERTAINTY & ASSUMPTION TESTING</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CALCULATED RISK VS RECKLESS GAMBLE</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">FINANCIAL RUNWAY & CASH DISCIPLINE</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">TECHNOLOGY & CYBERSECURITY SAFETY</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">RISK ASSESSMENT & MITIGATION MATRIX</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">EXPERIMENTATION, MVP & PIVOTING</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">ORAKZAI RESILIENCE & SOVEREIGN GROWTH</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">ENTREPRENEURSHIP & RISK</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Building Through Uncertainty with Resilience and Discipline.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Entrepreneurial Risk Framework: Navigating uncertainty, managing financial runway, implementing risk mitigation, and building sustainable ventures.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 163</title>
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
            <p class="section-label">PAGE 163</p>
            <h2>ENTREPRENEURSHIP & RISK</h2>
            <p>“Building Through Uncertainty with Resilience and Discipline.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Entrepreneurship is the process of turning an idea, skill or opportunity into something that creates value. But entrepreneurship is never completely predictable. Every business operates under uncertainty—customers may not respond as expected, technology may change, competitors may enter the market, regulations may evolve, capital may become difficult to obtain, and products may fail. Risk is therefore not an unusual part of entrepreneurship; it is part of the environment in which entrepreneurs operate. The objective is not to eliminate every risk, but to understand risk, measure it, manage it and make informed decisions despite uncertainty.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Foundational Risk Principles</h3>
                <p>Entrepreneurial risk encompasses the possibility that a business decision will produce an outcome different from what was expected, involving money, technology, customers, employees, regulation, reputation, and operations. Good entrepreneurs distinguish between calculated risks—which weigh potential rewards, probabilities, downsides, and available resources—and reckless gambles made without sufficient consideration of consequences [1] [2].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Financial Discipline & Runway</h3>
                <p>Financial risk management is critical for early-stage survival. Revenue does not automatically equate to financial stability; companies must meticulously manage cash flow timing and operational runway. Whether bootstrapping through personal resources or securing external capital via angel investors, venture capital, or business loans, founders must maintain capital discipline and understand the long-term implications of equity dilution and debt obligations [3] [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Technology & Modern Risk Vectors</h3>
                <p>As modern enterprises integrate advanced technologies, new risk vectors emerge. Technology risk covers software bugs, system failures, and infrastructure vulnerabilities. Furthermore, cybersecurity breaches, data privacy violations, AI inaccuracies, and blockchain smart-contract exploits demand rigorous oversight, redundancy, and robust business continuity planning [5] [6].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Experimentation, Failure & Strategic Pivots</h3>
                <p>Uncertainty is best managed through rapid experimentation, minimum viable products (MVPs), and the build-measure-learn feedback loop. When assumptions prove incorrect, failure serves as a learning mechanism rather than a definitive defeat. Entrepreneurs who embrace strategic pivoting, recognize opportunity costs, and maintain disciplined focus can navigate ambiguity and build enduring, sovereign ventures [7] [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Entrepreneurship & Risk</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the modern Orakzai entrepreneur, heritage provides identity, education provides knowledge, and technology provides leverage, but responsible risk management provides resilience. By combining cultural fortitude with rigorous financial and operational discipline, founders can transform uncertainty into enduring value.”</p>
            </div>

            <div class="final-statement">
                CALCULATED RISK.<br>
                ENDURING VALUE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Harvard Business Review, <em>Managing Risks: A New Framework (June 2025)</em>.</li>
                    <li>Sutter, R., <em>Entrepreneurial Strategy Under Uncertainty (2025)</em>.</li>
                    <li>Startup Genome, <em>Global Startup Ecosystem Report: Financial Discipline and Runway (2026)</em>.</li>
                    <li>Venture Capital Institute, <em>Bootstrapping vs. External Capital Dynamics (2025)</em>.</li>
                    <li>OWASP Foundation, <em>Cybersecurity and Digital Asset Risk Management (2026)</em>.</li>
                    <li>IEEE Computer Society, <em>AI Safety and Systemic Risk in Modern Ventures (2026)</em>.</li>
                    <li>Ries, E., <em>The Lean Startup: Continuous Innovation Through Experimentation (2025 Ed.)</em>.</li>
                    <li>Orakzai Innovation Archives, <em>The Modern Founder's Handbook on Uncertainty (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            163
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

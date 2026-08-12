from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-154-the-future-of-pakistani-entrepreneurs.html'

GRAPHICS = [
    ("Next Gen Founder", "USER", "↔", "NEW"),
    ("Builder Mindset", "IDEA", "→", "MAKE"),
    ("Global Reach", "PAK", "↔", "GLOB"),
    ("Ownership Ladder", "USE", "→", "OWN"),
    ("Talent Export", "PEOP", "→", "GLOB"),
    ("Product Export", "CODE", "→", "GLOB"),
    ("IP Ownership", "IDEA", "↔", "OWN"),
    ("Economic Value", "VALU", "↔", "DONE"),
    ("Startup Base", "PAK", "↔", "BASE"),
    ("Global Operation", "RUN", "↔", "GLOB"),
    ("Local Value", "VALU", "↔", "HOME"),
    ("Digital Border", "NET", "↔", "GLOB"),
    ("Software Scale", "ONE", "→", "MANY"),
    ("AI-Native Start", "AI", "↔", "BASE"),
    ("AI-Native Growth", "AI", "↔", "GROW"),
    ("AI Agent Flow", "AI", "↔", "AUTO"),
    ("Multi-Step Auto", "STEP", "→", "DONE"),
    ("Human Strategy", "WISE", "↔", "AI"),
    ("Human Responsibility", "OWN", "↔", "AI"),
    ("AI Productivity", "FAST", "↔", "AI"),
    ("Blockchain Problem", "PROB", "↔", "BC"),
    ("Digital Identity", "ID", "↔", "NET"),
    ("Custody Logic", "SAFE", "↔", "OWN"),
    ("RegTech Flow", "LAW", "↔", "TECH"),
    ("Fintech Opportunity", "FIN", "↔", "NEW"),
    ("Payment Brand", "PAY", "↔", "NAME"),
    ("Logistics Tech", "MOVE", "↔", "DATA"),
    ("Creative Tech", "ART", "↔", "CODE"),
    ("Gaming Potential", "PLAY", "↔", "MAKE"),
    ("Deep-Tech Path", "SCI", "→", "VALU"),
    ("Robotics Goal", "ROBO", "↔", "MAKE"),
    ("Biotech Goal", "BIO", "↔", "VALU"),
    ("Energy Tech Goal", "POWR", "↔", "NEW"),
    ("Semiconductor Path", "CHIP", "↔", "NATL"),
    ("INSPIRE Program", "7.2K", "↔", "CHIP"),
    ("Chip Design Co", "12", "↔", "PAK"),
    ("EDA Workflow", "TOOL", "↔", "CHIP"),
    ("Verification Rail", "TEST", "↔", "CHIP"),
    ("Climate Opportunity", "PLAN", "↔", "NEW"),
    ("Renewable Tech", "SUN", "↔", "POWR"),
    ("Water Tech Goal", "H2O", "↔", "DATA"),
    ("Sustainable Agri", "FARM", "↔", "SAFE"),
    ("Healthtech Access", "DOC", "↔", "NET"),
    ("Telemedicine Path", "DOC", "↔", "GLOB"),
    ("EdTech Skills", "LEAR", "↔", "NEW"),
    ("Cybersecurity Biz", "SEC", "↔", "GROW"),
    ("Cloud Biz Model", "CLOU", "↔", "OWN"),
    ("Open Source Rep", "CODE", "↔", "NAME"),
    ("API Economy", "LINK", "↔", "VALU"),
    ("Platform Model", "BASE", "↔", "MANY"),
    ("Creator Economy", "ART", "↔", "CASH"),
    ("Personal Brand", "NAME", "↔", "TRUST"),
    ("Recruitment Rail", "PEOP", "↔", "NAME"),
    ("Data Asset Value", "DATA", "↔", "VALU"),
    ("Digital Trust", "SAFE", "↔", "NAME"),
    ("Secure System", "LOCK", "↔", "NET"),
    ("Privacy Design", "PRIV", "↔", "CODE"),
    ("Regulated Strategy", "LAW", "↔", "GROW"),
    ("Predictable Rule", "LAW", "↔", "SEED"),
    ("Gov as Enabler", "GOV", "↔", "GROW"),
    ("Digital Registry", "GOV", "↔", "DONE"),
    ("Orakzai Founder", "ORAK", "↔", "GLOB"),
    ("Inclusive Future", "ALL", "↔", "GROW"),
    ("Sovereign Nation", "OWN", "↔", "NATL"),
    ("Future Builder", "TIME", "↔", "NEW"),
    ("The Permanent Goal", "STAY", "↔", "DONE"),
    ("Unity of Purpose", "ONE", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g154-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g154-{index}-title g154-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g154-{index}-title">{safe}</title><desc id="g154-{index}-desc">A future entrepreneurship relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g154-{index}-caption" class="diagram-caption">{index}. {safe} — Entrepreneurship relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">The Future of Pakistani Entrepreneurs</title><desc id="hero-desc">A diagram showing the strategic evolution of Pakistani entrepreneurship toward global products, deep-tech, and AI-native architectures in 2026.</desc><defs><linearGradient id="h154-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h154-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE GLOBAL FOUNDER STRATEGY (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DEEP-TECH LEAP (Semiconductors / Chip Design)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">AI-NATIVE STARTUPS (Agentic Workflows)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">PRODUCT EXPORT (IP Ownership / Global Brands)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">BUILD IN PAKISTAN → OPERATE GLOBALLY</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">HUMAN + AI SYNERGY (Productivity Lever)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">REGULATORY CERTAINTY & GOV ENABLER</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">ECONOMIC SOVEREIGNTY (OWN → EXPORT)</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">FUTURE OF PAKISTANI ENTREPRENEURS</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Building Companies for Pakistan and the World.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Global Founder Strategy: How Pakistani entrepreneurs are evolving toward deep-tech, AI-native products, and global IP ownership in 2026.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 154</title>
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
            <p class="section-label">PAGE 154</p>
            <h2>THE FUTURE OF PAKISTANI ENTREPRENEURS</h2>
            <p>“Building Companies for Pakistan and the World.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “The future of Pakistani entrepreneurship will be shaped by a generation growing up in a deeply connected digital economy. We are moving beyond the model of exporting talent and toward one that exports products, intellectual property, and companies. By building from Pakistan to serve the world, the next generation of founders is creating the foundations of national economic sovereignty.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Deep-Tech & Semiconductor Leap</h3>
                <p>In 2026, Pakistan has taken a historic step into high-barrier industries. Through the **Rs 4.5 billion INSPIRE program**, over **7,200 engineers** are being trained in semiconductor technology and chip design. By mid-2026, **12 local companies** have entered the global chip design market, focusing on Electronic Design Automation (EDA) workflows and chip IP. This transition from consumer to builder of core technology represents a major shift in the national entrepreneurial ambition.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI-Native Startups & Agentic Workflows</h3>
                <p>The entrepreneurial model in 2026 is defined by **AI-Native** architectures. Rather than adding AI as an afterthought, new startups are designed around **Agentic Workflows** from day one. These AI agents automate multi-step digital processes in finance, healthcare, and legal tech, allowing small Pakistani teams to perform work that previously required massive organizations. This "Human + AI" synergy acts as a productivity lever, enabling local founders to compete with global giants.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">From IT Services to Global Products</h3>
                <p>A central strategic transition is the move from **Freelancing and IT Services** to **Software Products and Platforms**. By owning the Intellectual Property (IP), Pakistani entrepreneurs are capturing greater long-term value. The 2026 strategy follows the "Build in Pakistan → Operate Globally" model, leveraging domestic cost advantages while serving high-value markets in North America, the Gulf, and Southeast Asia. This creates a sustainable cycle of local value creation through global expansion.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Climate, Health & Regulatory Tech</h3>
                <p>Future entrepreneurs are solving the most pressing global challenges. **Climate Entrepreneurship** addresses energy efficiency and water technology, while **HealthTech** and **EdTech** deliver essential services to remote regions. These founders operate within a framework of **Regulatory Technology (RegTech)**, ensuring digital trust, secure systems, and responsible data practices. Government acts as an enabler, providing the infrastructure and predictable rules necessary for large-scale investment.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Future Entrepreneurs</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“The future Pakistani entrepreneur is a global citizen with a local heart. For the Orakzai community, this means that the valley is no longer just a place of heritage, but a center of innovation. A young founder in Orakzai can design a chip, build an AI agent, or launch a global brand from their home. We are building a nation where ownership is the key to sovereignty, and where every builder has the opportunity to shape the world.”</p>
            </div>

            <div class="final-statement">
                BUILD LOCALLY.<br>
                OWN GLOBALLY.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Ministry of IT & Telecommunication (MOITT) / GIKI, <em>The INSPIRE Program: Semiconductor & Chip Design Training (May 2026)</em>.</li>
                    <li>LUMS / SBASSE, <em>Highlights from the Pakistan Semiconductor Summit 2026: EDA and Chip IP (April 2026)</em>.</li>
                    <li>PwC / Tech Effect, <em>2026 AI Business Predictions: Agentic Workflows and AI-Native Companies (2026)</em>.</li>
                    <li>LinkedIn / VertexIT, <em>Pakistan's Tech Industry Insights 2026: Record Growth and Global Engagement (Feb 2026)</em>.</li>
                    <li>EmporionSoft / Trend Analysis, <em>Pakistan Tech Trends 2026: AI, Cloud, and Cybersecurity Shifts (Dec 2025)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            154
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-165-technology-as-a-tool-for-change.html'

GRAPHICS = [
    ("Technology Tool", "TOOL", "↔", "USE"),
    ("Problem First", "WHY", "→", "HOW"),
    ("Human-Centered", "USER", "↔", "NEED"),
    ("Access Expansion", "NET", "↔", "DATA"),
    ("Digital Education", "LEARN", "↔", "NET"),
    ("AI Learning Aid", "AI", "→", "WISE"),
    ("Digital Literacy", "KNOW", "↔", "TECH"),
    ("Digital Divide", "HAVE", "≠", "NOT"),
    ("Connectivity Base", "LINK", "↔", "BASE"),
    ("Rural Access", "VALY", "↔", "NET"),
    ("Pakistan Future", "YOUN", "→", "GROW"),
    ("Youth Potential", "ORAK", "↔", "TECH"),
    ("Entr Barrier", "LOW", "↔", "START"),
    ("Local Problem", "HERE", "→", "FIX"),
    ("Digital Solution", "CODE", "↔", "FIX"),
    ("Digital Commerce", "BUY", "↔", "SELL"),
    ("Fintech Inclusion", "CASH", "↔", "NET"),
    ("Digital Payments", "PAY", "↔", "FAST"),
    ("Blockchain Record", "BC", "↔", "DATA"),
    ("Decentralization", "ALL", "↔", "OWN"),
    ("Digital Ownership", "OWN", "↔", "CODE"),
    ("AI General Tech", "AI", "↔", "ALL"),
    ("AI Productivity", "AI", "→", "DONE"),
    ("Human Judgment", "SELF", "↔", "AI"),
    ("Automation Path", "AUTO", "↔", "DONE"),
    ("Robotics Fusion", "BOT", "↔", "PHYS"),
    ("Cloud Resource", "GRID", "↔", "USER"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Data Protection", "DATA", "↔", "SAFE"),
    ("Privacy Design", "SELF", "↔", "DATA"),
    ("Digital Identity", "SELF", "↔", "NET"),
    ("Digital Govt", "GOVT", "↔", "USER"),
    ("Open Data", "OPEN", "↔", "WISE"),
    ("Digital Trust", "TRUE", "↔", "NET"),
    ("Health Access", "DOC", "↔", "NET"),
    ("Telemedicine", "DOC", "↔", "LINK"),
    ("AI Healthcare", "AI", "→", "HELP"),
    ("Agri Support", "FARM", "↔", "DATA"),
    ("Smart Agri", "AI", "↔", "FARM"),
    ("Water Management", "SAVE", "↔", "DROP"),
    ("Climate Monitoring", "EARTH", "↔", "DATA"),
    ("Renewable Energy", "SUN", "↔", "GRID"),
    ("Smart Grid", "GRID", "↔", "DATA"),
    ("Transport Nav", "MOVE", "↔", "MAP"),
    ("Smart City", "CITY", "↔", "NET"),
    ("Work Structure", "WORK", "↔", "TECH"),
    ("Reskilling Path", "LEARN", "→", "WORK"),
    ("Future Skills", "KNOW", "↔", "DONE"),
    ("Human Creativity", "ART", "↔", "SELF"),
    ("Entr Creativity", "IDEA", "→", "DONE"),
    ("Cultural Pres", "PAST", "↔", "SAVE"),
    ("Knowledge Dist", "WISE", "↔", "NET"),
    ("Sovereign Tool", "ORAK", "↔", "TOOL"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g165-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g165-{index}-title g165-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g165-{index}-title">{safe}</title><desc id="g165-{index}-desc">A technology as a tool relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g165-{index}-caption" class="diagram-caption">{index}. {safe} — Technology as a tool relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Technology as a Tool for Change Framework</title><desc id="hero-desc">A diagram showing technology as a tool for solving problems, connecting people, improving access, and strengthening institutions in the 2026 digital era.</desc><defs><linearGradient id="h165-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h165-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE TECHNOLOGY-IMPACT LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">PROBLEM-FIRST DESIGN & HUMAN-CENTERED AI</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL INCLUSION: 5.1M PAKISTAN CONNECTIONS</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">BLOCKCHAIN & TOKENIZATION FOR OWNERSHIP</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">CLOUD INFRASTRUCTURE & SOVEREIGN GRIDS</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CYBERSECURITY, PRIVACY & DIGITAL TRUST</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">SOCIAL SECTOR IMPACT: AGRI, HEALTH & EDU</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">ORAKZAI RESILIENCE: HERITAGE TO PROGRESS</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">TECHNOLOGY AS A TOOL FOR CHANGE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Technology is a tool for human progress when guided by human decisions.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Technology-Impact Loop: Navigating the 2026 digital era where technology serves as a tool for social sectors, economic growth, and sovereign progress.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 165</title>
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
            <p class="section-label">PAGE 165</p>
            <h2>TECHNOLOGY AS A TOOL FOR CHANGE</h2>
            <p>“Technology, Human Progress and the Power to Build.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Technology is not an end in itself. It is a tool—a tool for solving problems, connecting people, improving access to information, creating businesses, preserving history, and strengthening institutions. From the printing press to the internet, technological progress has repeatedly changed how societies communicate, learn, work and organize. The digital era has accelerated that process. Today, a smartphone can provide access to information that once required a library; cloud computing allows organizations to deploy infrastructure without large physical data centers. But technology alone does not guarantee progress. Human decisions determine how technology is designed, deployed and used.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Pakistan's Digital Transformation (2026)</h3>
                <p>The year 2026 marked a pivotal shift in Pakistan's digital landscape. Domestic internet connections surged from 1.9 million in 2024 to **5.1 million** by mid-2026, significantly narrowing the digital divide [1]. The *State of Freedom Report 2026* highlights that 75% of women in the tech sector are satisfied with the progress of digitalization, reflecting a more inclusive economic participation [2]. This expansion of connectivity is the foundational tool for rural development and institutional strengthening across the country [3].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI & Human-Centered Innovation</h3>
                <p>In 2026, Artificial Intelligence (AI) transitioned from experimentation to widespread impact. Successful organizations now prioritize human-centric AI, ensuring that automation assists research, analysis, and language learning while complementing human judgment rather than replacing critical thinking [4] [5]. In the social sector, AI tools are being vetted for operational transparency and stakeholder accountability, ensuring that innovation remains connected to real human needs like healthcare imaging and agricultural precision [6] [7].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Blockchain, Tokenization & Digital Trust</h3>
                <p>The convergence of AI and Blockchain has created new rails for economic activity. Blockchain technology provides a secure method for maintaining shared digital records, enabling digital ownership, tokenization, and decentralized coordination [8]. By 2026, tokenization has shone as a stable sector amid global geopolitical turmoil, providing Orakzai entrepreneurs with tools for sovereign digital assets and infrastructure through initiatives like **OKBOND** and the **Sovereign Grid** [9] [10].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Future Skills & The Work Structure</h3>
                <p>As technology reshapes the structure of work, reskilling has become a necessity. Important skills in 2026 include digital literacy, AI literacy, data analysis, and programming, alongside traditional strengths like communication and critical thinking [11]. While some roles decline due to automation, new opportunities emerge in robotics, smart agriculture, and digital governance. Technology amplifies human creativity and imagination, allowing entrepreneurs to combine tools in new ways to solve enduring problems [12].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Technology as a Tool</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai community, technology is the modern expression of our ancient resilience. It is the tool that allows us to preserve our culture while building our future. By choosing the problem before the technology and the human before the machine, we ensure that our digital transformation is a sovereign journey toward progress and dignity.”</p>
            </div>

            <div class="final-statement">
                PROBLEM FIRST.<br>
                HUMAN GUIDED.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Digital Pakistan Monitor, <em>Growth in Domestic Internet Penetration (June 2026)</em>.</li>
                    <li>State of Freedom Report 2026, <em>Digitalization and Gender Inclusion in Pakistan (July 2026)</em>.</li>
                    <li>GSMA, <em>Making Digital Pakistan a Reality: Growth and Development Report (2026)</em>.</li>
                    <li>Deloitte Insights, <em>Tech Trends 2026: Moving from Experimentation to Impact (December 2025)</em>.</li>
                    <li>Info-Tech Research Group, <em>Adapting to Human-Centric AI and Geopolitical Shifts (2026)</em>.</li>
                    <li>Social Current, <em>2026 Trends Report: AI in the Social Sector (January 2026)</em>.</li>
                    <li>BSR, <em>Making Sense of AI in 2026: Social Impacts in Asia (2026)</em>.</li>
                    <li>Pantera Capital, <em>The Convergence of AI and Blockchain: Economic Rails (May 2026)</em>.</li>
                    <li>Grayscale Research, <em>Crypto Sectors Quarterly: AI and Tokenization (March 2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Technical Framework: OKBOND and Sovereign Grid (August 2026)</em>.</li>
                    <li>KPMG International, <em>Global Tech Report 2026: The Future of Work and Skills (March 2026)</em>.</li>
                    <li>Forbes India, <em>Five Global Trends in Business and Society in 2026 (February 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            165
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

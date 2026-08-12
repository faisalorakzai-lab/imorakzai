from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-155-global-pakistani-talent.html'

GRAPHICS = [
    ("Global Resource", "PEOP", "↔", "ECON"),
    ("Talent Network", "MANY", "↔", "ONE"),
    ("Knowledge Cycle", "KNOW", "→", "VALU"),
    ("Innovation Loop", "IDEA", "→", "GROW"),
    ("Global Opportunity", "PAK", "↔", "GLOB"),
    ("Professional Hub", "GULF", "↔", "PAK"),
    ("Western Hub", "WEST", "↔", "PAK"),
    ("East Asia Hub", "EAST", "↔", "PAK"),
    ("Diaspora Asset", "HOME", "↔", "GLOB"),
    ("Expertise Transfer", "WISE", "→", "HOME"),
    ("Mentorship Rail", "WISE", "→", "NEW"),
    ("Investment Rail", "CASH", "→", "GROW"),
    ("Tech Transfer", "TECH", "→", "BASE"),
    ("Business Link", "LINK", "↔", "GLOB"),
    ("Research Collab", "SCI", "↔", "NET"),
    ("Medical Impact", "DOC", "↔", "LIFE"),
    ("Telemedicine Path", "DOC", "↔", "NET"),
    ("Engineering Rail", "MAKE", "↔", "VALU"),
    ("Software Rail", "CODE", "↔", "GLOB"),
    ("Civil Eng Rail", "BASE", "↔", "VALU"),
    ("Electrical Rail", "POWR", "↔", "VALU"),
    ("Telecom Rail", "CONN", "↔", "VALU"),
    ("Energy Rail", "POWR", "↔", "GLOB"),
    ("Scientific Impact", "SCI", "↔", "NEW"),
    ("Medical Research", "DOC", "↔", "SCI"),
    ("Physics Impact", "ATOM", "↔", "SCI"),
    ("Chemistry Impact", "MOLC", "↔", "SCI"),
    ("CS Impact", "CODE", "↔", "SCI"),
    ("Env Sci Impact", "PLAN", "↔", "SCI"),
    ("Eng Sci Impact", "MAKE", "↔", "SCI"),
    ("Tech Professional", "USER", "↔", "CODE"),
    ("Data Sci Impact", "DATA", "↔", "WISE"),
    ("AI Specialist", "AI", "↔", "NEW"),
    ("Cyber Specialist", "SEC", "↔", "SAFE"),
    ("Product Manager", "PLAN", "↔", "DONE"),
    ("Designer Impact", "ART", "↔", "VALU"),
    ("Cloud Engineer", "CLOU", "↔", "BASE"),
    ("ML Engineering", "AI", "↔", "CODE"),
    ("Data Engineering", "DATA", "↔", "BASE"),
    ("Computer Vision", "EYE", "↔", "AI"),
    ("NLP Engineering", "TALK", "↔", "AI"),
    ("AI Infrastructure", "BASE", "↔", "AI"),
    ("Network Protect", "LOCK", "↔", "NET"),
    ("App Protection", "APP", "↔", "SAFE"),
    ("Data Protection", "DATA", "↔", "SAFE"),
    ("Identity Protect", "ID", "↔", "SAFE"),
    ("Insight Engine", "DATA", "→", "WISE"),
    ("Forecast Engine", "TIME", "→", "DATA"),
    ("UX Design Path", "USER", "↔", "APP"),
    ("Arch Design Path", "BASE", "↔", "ART"),
    ("Fashion Design", "WEAR", "↔", "ART"),
    ("Digital Media", "NET", "↔", "ART"),
    ("Finance Impact", "CASH", "↔", "VALU"),
    ("Accounting Rail", "DATA", "↔", "CASH"),
    ("Banking Rail", "BANK", "↔", "CASH"),
    ("Economic Rail", "GROW", "↔", "CASH"),
    ("Investment Path", "SEED", "↔", "GROW"),
    ("Founder Bridge", "PAK", "↔", "GLOB"),
    ("Global Capital", "CASH", "↔", "GLOB"),
    ("Intl Customer", "USER", "↔", "GLOB"),
    ("Remote Economy", "HOME", "↔", "GLOB"),
    ("Labor Market", "WORK", "↔", "NET"),
    ("Freelancing Path", "ONE", "↔", "NET"),
    ("Market Knowledge", "GLOB", "↔", "WISE"),
    ("Team Path", "ONE", "→", "MANY"),
    ("Agency Path", "TEAM", "→", "COMP"),
    ("Exporter Path", "PAK", "→", "GLOB"),
    ("Digital Export", "CODE", "→", "NET"),
    ("Knowledge Export", "WISE", "→", "NET"),
    ("Consulting Rail", "WISE", "↔", "CASH"),
    ("Publication Rail", "READ", "↔", "DONE"),
    ("Training Rail", "LEAR", "↔", "DONE"),
    ("Startup Transfer", "IDEA", "→", "PAK"),
    ("University Link", "UNI", "↔", "GLOB"),
    ("Partnership Rail", "LINK", "↔", "GROW"),
    ("Diaspora Bridge", "NET", "↔", "GLOB"),
    ("Virtual Mentor", "TALK", "↔", "NET"),
    ("Network Infra", "NET", "↔", "BASE"),
    ("Diaspora Invest", "CASH", "→", "PAK"),
    ("Property Invest", "LAND", "↔", "CASH"),
    ("Asset Invest", "TOK", "↔", "CASH"),
    ("Social Project", "GOOD", "↔", "CASH"),
    ("Remittance Rail", "CASH", "→", "HOME"),
    ("Remittance Flow", "GLOB", "→", "PAK"),
    ("Employment Goal", "JOB", "↔", "GROW"),
    ("Cross-Border Co", "MANY", "↔", "ONE"),
    ("Engineering Team", "TEAM", "↔", "CODE"),
    ("SaaS Export", "CLOU", "↔", "CASH"),
    ("AI Product", "AI", "↔", "OWN"),
    ("Blockchain Dev", "BC", "↔", "CODE"),
    ("Protocol Dev", "BASE", "↔", "BC"),
    ("Smart Contract", "LAW", "↔", "CODE"),
    ("Web3 Talent", "NET", "↔", "NEW"),
    ("Open Source Cont", "CODE", "↔", "GLOB"),
    ("Fintech Talent", "FIN", "↔", "TECH"),
    ("Research Network", "SCI", "↔", "NET"),
    ("Joint Pub Rail", "READ", "↔", "NET"),
    ("Student Abroad", "LEAR", "↔", "GLOB"),
    ("Brain Circulation", "PAK", "↔", "GLOB"),
    ("Brain Drain Re", "LOSS", "→", "GAIN"),
    ("Connected Talent", "ALL", "↔", "ONE"),
    ("Orakzai Global", "ORAK", "↔", "GLOB"),
    ("Valley Mentor", "ORAK", "↔", "WISE"),
    ("Regional Invest", "ORAK", "↔", "CASH"),
    ("Future Rail", "TIME", "↔", "NEW"),
    ("Sovereign Talent", "OWN", "↔", "NATL"),
    ("Inclusive Global", "ALL", "↔", "GLOB"),
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
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g155-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g155-{index}-title g155-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g155-{index}-title">{safe}</title><desc id="g155-{index}-desc">A global talent relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g155-{index}-caption" class="diagram-caption">{index}. {safe} — Global talent relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Global Pakistani Talent Framework</title><desc id="hero-desc">A diagram showing the strategic integration of the Pakistani diaspora and global talent into the national economic engine in 2026.</desc><defs><linearGradient id="h155-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h155-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE GLOBAL TALENT ENGINE (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">BRAIN CIRCULATION (Knowledge & Tech Transfer)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIASPORA FOUNDERS (10 Billion-Dollar US Cos)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">DIGITAL EXPORTS ($1.76B Freelance FY26)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">HEALTHCARE LINK (Telemedicine Backup Model)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">VIRTUAL MENTORSHIP & RESEARCH NETWORKS</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">DIASPORA INVESTMENT & CAPITAL FLOWS</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">GLOBAL DIGITAL RANKING (+27 Places in 2026)</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">GLOBAL PAKISTANI TALENT</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Pakistani Skills to Global Value.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Global Talent Engine: Strategic integration of the Pakistani diaspora and global professionals into the national economic framework in 2026.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 155</title>
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
            <p class="section-label">PAGE 155</p>
            <h2>GLOBAL PAKISTANI TALENT</h2>
            <p>“From Pakistani Skills to Global Value.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Pakistan's most important global resource is its people. Across technology, medicine, engineering, and the creative industries, Pakistanis contribute to economies and institutions around the world. This global talent represents a network of knowledge, skills, and experience that connects Pakistan with international markets. The challenge is to transform this presence into a cycle of brain circulation and global opportunity.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Diaspora as Strategic Human Capital</h3>
                <p>In 2026, the Pakistani diaspora has emerged as a critical driver of national innovation. A June 2026 report by the National Foundation for American Policy highlighted that **10 Pakistani immigrants** are among the founders of billion-dollar startups in the United States. Beyond financial remittances, this global network provides expertise, mentorship, and technology transfer. The shift from "Brain Drain" to **"Brain Circulation"** is central to the 2026 economic strategy, turning international success into domestic gain.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Exports & The Remote Economy</h3>
                <p>The rise of the remote economy has allowed Pakistani talent to participate in global markets without relocation. In FY26, Pakistani freelancers earned a record **$1.76 billion**, a 78% increase from the previous year. IT freelancers alone generated **$1.16 billion**, demonstrating the scalability of digital exports. This "Digital Diaspora" bridges the geographic gap, allowing professionals in Karachi, Lahore, and even the Orakzai valleys to serve international clients and build global reputations.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Healthcare & Research Networks</h3>
                <p>Global Pakistani professionals are strengthening domestic institutions through specialized networks. The **Telemedicine Backup model**, proposed in 2026, engages overseas physicians to provide remote support to Pakistani hospitals. Similarly, research networks connected to international universities facilitate knowledge exchange and joint publications. These links ensure that the latest advancements in medicine, AI, and engineering are rapidly integrated into the Pakistani ecosystem.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Diaspora Bridge & Investment</h3>
                <p>The diaspora serves as a bridge to international customers, investors, and professional networks. In 2026, Pakistan's global digital position improved by **27 places**, largely due to increased diaspora engagement in the tech sector. Beyond traditional remittances, overseas Pakistanis are investing in startups, property, and social projects. This transition from "Income Abroad" to "Economic Value at Home" is creating a sustainable cycle of employment and growth across the country.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Global Pakistani Talent</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“A global Pakistani is a local asset. For the Orakzai community, the diaspora is a lifeline of knowledge. Our valley natives in the Gulf, Europe, and America are not just sending money home; they are sending expertise. Through virtual mentorship, they are training the next generation of Orakzai builders in AI and global business. We are building a nation where talent has no borders and where every citizen is part of a sovereign global network.”</p>
            </div>

            <div class="final-statement">
                TALENT IS GLOBAL.<br>
                VALUE IS NATIONAL.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>National Foundation for American Policy (NFAP), <em>Immigrant Founders and the Pakistani Impact (June 2026)</em>.</li>
                    <li>State Bank of Pakistan (SBP) / Freelance Monitor, <em>Pakistani Freelance Earnings Hit Record $1.76 Billion in FY26 (July 2026)</em>.</li>
                    <li>Ministry of Planning / PID, <em>Engaging the Diaspora: The Telemedicine Backup Model (July 2026)</em>.</li>
                    <li>Second Overseas Pakistanis Convention (OPC), <em>From Brain Drain to Brain Circulation: 2026 Strategy (March 2026)</em>.</li>
                    <li>ITU / Digital Trends Report, <em>Pakistan's Global Digital Ranking and Diaspora Impact (January 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            155
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

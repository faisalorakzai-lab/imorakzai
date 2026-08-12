from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-193-the-meaning-of-nation.html'

GRAPHICS = [
    ("Nation Meaning", "ALL", "↔", "NEXT"),
    ("I'm Pakistani", "SELF", "↔", "FLAG"),
    ("Citizenship Rail", "SELF", "↔", "RULE"),
    ("Nation Community", "ALL", "↔", "LINK"),
    ("Belonging Path", "SELF", "↔", "ALL"),
    ("Responsibility", "SELF", "↔", "DO"),
    ("Nation Dimens", "ALL", "↔", "TRUE"),
    ("Pakistan History", "PAST", "↔", "NOW"),
    ("Hist Understanding", "WHY", "↔", "TRUE"),
    ("Citizenship Rights", "SELF", "↔", "FREE"),
    ("National Ident", "SELF", "↔", "ALL"),
    ("Multilayered Id", "MANY", "↔", "ONE"),
    ("Identity Balance", "HERE", "↔", "ALL"),
    ("Diversity Rail", "MANY", "↔", "ONE"),
    ("Languages Path", "TALK", "↔", "TRUE"),
    ("Urdu Rail", "PASH", "↔", "TRUE"),
    ("English Rail", "GLOB", "↔", "TRUE"),
    ("Regional Lang", "HERE", "↔", "TRUE"),
    ("Lang Preserve", "SAVE", "↔", "LONG"),
    ("Cultural Divers", "MANY", "↔", "TRUE"),
    ("Provinces Rail", "HERE", "↔", "ALL"),
    ("City Identity", "CITY", "↔", "SELF"),
    ("Rural Pakistan", "HERE", "↔", "BASE"),
    ("Urbanization", "CITY", "↔", "GROW"),
    ("Internal Migr", "HERE", "↔", "THERE"),
    ("Diaspora Path", "HOME", "↔", "GLOB"),
    ("Diaspora Contrib", "GLOB", "→", "HOME"),
    ("National Memory", "MIND", "↔", "SAVE"),
    ("Historical Hon", "TRUE", "↔", "WISE"),
    ("Learn from Hist", "FAIL", "→", "WISE"),
    ("National Pride", "SELF", "↔", "FLAG"),
    ("Patriotism Path", "HELP", "↔", "TRUE"),
    ("Criticism Rail", "WHY", "↔", "FIX"),
    ("Civic Respons", "DO", "↔", "ALL"),
    ("Respect Law", "RULE", "↔", "SAFE"),
    ("Respect Rights", "ALL", "↔", "TRUE"),
    ("Public Respons", "ALL", "↔", "SAFE"),
    ("Taxation Rail", "CASH", "→", "GRID"),
    ("Voting Path", "YES", "↔", "DO"),
    ("Civic Partic", "ALL", "↔", "DO"),
    ("Democratic Cult", "MANY", "↔", "TRUE"),
    ("Political Diff", "MANY", "↔", "ONE"),
    ("Respect Disagree", "MANY", "↔", "SAFE"),
    ("Institutions", "GRID", "↔", "LONG"),
    ("Rule of Law", "RULE", "↔", "SAFE"),
    ("Indep Inst", "FREE", "↔", "SAFE"),
    ("Public Trust", "TRUE", "↔", "SAFE"),
    ("Edu Foundation", "LEAR", "↔", "BASE"),
    ("Universal Access", "ALL", "↔", "LEAR"),
    ("Higher Edu", "TOP", "↔", "LEAR"),
    ("Technical Edu", "ABLE", "↔", "WORK"),
    ("Digital Edu", "NET", "↔", "LEAR"),
    ("CS Foundation", "CODE", "↔", "BASE"),
    ("AI Opportunity", "AI", "↔", "NEXT"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Digital Infra", "GRID", "↔", "BASE"),
    ("Digital Sovereignty", "SELF", "↔", "TECH"),
    ("Tech as Tool", "TECH", "↔", "FIX"),
    ("Innovation Rail", "NEW", "↔", "NEXT"),
    ("Entrepreneurship", "IDEA", "→", "BIZ"),
    ("Young Founders", "YOUN", "→", "NEW"),
    ("Small Business", "ONE", "↔", "MANY"),
    ("Global Companies", "HOME", "→", "GLOB"),
    ("Digital Exports", "HOME", "→", "CASH"),
    ("Freelancing Rail", "ONE", "→", "GLOB"),
    ("Remote Work", "HERE", "↔", "GLOB"),
    ("Skills Compete", "ABLE", "↔", "GLOB"),
    ("Research Base", "WHY", "↔", "LONG"),
    ("Science Base", "FACT", "↔", "ALL"),
    ("Uni Engines", "LEAR", "↔", "BIZ"),
    ("Industry Rail", "MAKE", "↔", "BASE"),
    ("Agriculture", "GROW", "↔", "BASE"),
    ("Water Security", "LIFE", "↔", "SAFE"),
    ("Energy Base", "POWER", "↔", "BASE"),
    ("Infra Base", "GRID", "↔", "BASE"),
    ("Karachi Hub", "CITY", "↔", "BIZ"),
    ("Ports Path", "SHIP", "↔", "GLOB"),
    ("Trade Path", "BUY", "↔", "GLOB"),
    ("Exports Rail", "HOME", "→", "GLOB"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g193-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g193-{index}-title g193-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g193-{index}-title">{safe}</title><desc id="g193-{index}-desc">A nation relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g193-{index}-caption" class="diagram-caption">{index}. {safe} — Nation relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">I’M PAKISTANI — The Meaning of Nation Framework</title><desc id="hero-desc">A diagram showing the 2026 Pakistan national development landscape, featuring record IT exports of $4.6B, the 64% youth population, and the digital economy's growth to 7% of GDP.</desc><defs><linearGradient id="h193-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h193-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE NATIONAL DEVELOPMENT LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">IT EXPORTS RECORD: $4.60 BILLION IN FY 2025-26</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">YOUTH POPULATION: 64% UNDER 30 (140M+ CITIZENS)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">DIGITAL ECONOMY: PROJECTED 7% OF GDP BY 2030</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">FREELANCE EXPORTS: $1B+ ANNUALLY (2026)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DCO TRENDS 2026: 9.5% GLOBAL DIGITAL GROWTH</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: NATIONAL INTEGRATION</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">NATION: CITIZENSHIP, RESPONSIBILITY & SHARED FUTURE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">I’M PAKISTANI — THE MEANING OF NATION</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Nation as Citizenship, Responsibility, Diversity, and Shared Future: Lived and Inherited.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The National Development Loop: Navigating the 2026 landscape where record IT exports, a massive youth population, and a surging digital economy ensure that Pakistan's national identity remains resilient, diverse, and globally connected.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 193</title>
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
            <p class="section-label">PAGE 193</p>
            <h2>I’M PAKISTANI — THE MEANING OF NATION</h2>
            <p>“Nation as Citizenship, Responsibility, Diversity, and Shared Future.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “I’m Pakistani. For many, those words describe more than a nationality; they represent citizenship, family, and a connection to a country whose people come from many regions, languages, and cultural traditions. But being Pakistani does not mean every Pakistani has the same experience. Pakistan is diverse, its people living in cities, villages, mountains, and plains. Yet they share a national framework—a community of citizens connected through institutions, laws, history, and a common future. To say ‘I’m Pakistani’ is both a statement of belonging and a statement of responsibility.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">IT Exports Record & Digital Economy Surge (2026)</h3>
                <p>In fiscal year 2025-26, Pakistan’s information technology (IT) exports reached a historic record of **$4.60 billion**, reflecting the sector's robust growth and global competitiveness [1]. Individual freelancers now generate a quarter of these exports, on track to cross **$1 billion annually** [2]. Pakistan’s digital landscape is witnessing rapid growth, with internet connections surging to **5.10 million** in 2026 [3]. The digital economy is projected to reach **7% of GDP by 2030**, driven by strengthening cybersecurity and digital transformation [4] [5].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Youth Population & National Advancement</h3>
                <p>Pakistan enters 2026 with a massive youth population—**64% of its citizens are under 30**, representing over 140 million young people who will determine the country's future [6]. With a total population crossing **252 million**, over 56.9% are of working age, offering a significant demographic dividend if harnessed for jobs and productivity [7] [8]. National programs are increasingly focused on empowering these young founders through entrepreneurship, digital literacy, and technical education [9] [10].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Diversity, Federalism & Civic Responsibility</h3>
                <p>Pakistan’s diversity is one of its defining social characteristics, with distinct regional histories in Punjab, Sindh, Khyber Pakhtunkhwa, and Balochistan [11]. A strong national identity does not require abandoning regional languages like Punjabi, Pashto, or Balochi; instead, Urdu serves as the national bridge [12]. Responsible citizenship includes informed participation in democratic processes, respect for the rule of law, and collective responsibility for public infrastructure [13]. Stabilizing institutions and ensuring independent accountability remain key targets for 2026 [14].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Global Connectivity & Sovereign Infrastructure</h3>
                <p>The Pakistani diaspora, millions of whom live abroad, connects the country to global markets through investment, professional networks, and cultural exchange [15]. Digital sovereignty—the technical capacity to manage critical infrastructure—is becoming essential for national progress [16]. For the Orakzai community, the **Sovereign Grid** ensures that local identity is integrated into the national framework, allowing Pakistani professionals to participate in global digital exports while remaining rooted in their heritage [17].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: I’m Pakistani — The Meaning of Nation</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the people of Pakistan, our nation is the shared mission of our lives. We do not just inhabit a territory; we build a civilization. By mastering IT exports and digital sovereignty while remaining rooted in our diversity and civic responsibility, we are ensuring that the Pakistani name remains a source of resilience and progress for the next century. We are the architects of a nation that is sovereign, diverse, and eternal. Our unity is our strength, and our future is our responsibility.”</p>
            </div>

            <div class="final-statement">
                DIVERSE UNITY.<br>
                SOVEREIGN PROGRESS.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>The Express Tribune, <em>IT Exports Hit Record $4.6 Billion in FY 2025-26 (July 2026)</em>.</li>
                    <li>PakJournals / PTT, <em>Freelancing Built Pakistan's IT Exports: Reaching $1 Billion (July 2026)</em>.</li>
                    <li>Instagram / Digital Pakistan, <em>Pakistan's Internet Connections Surge to 5.1 Million in 2026 (April 2026)</em>.</li>
                    <li>Digital Cooperation Organization (DCO), <em>Digital Economy Trends 2026 Report: 9.5% Global Growth (December 2025)</em>.</li>
                    <li>ResearchGate, <em>Effect of Digital Economy on the Economic Development of Pakistan (June 2026)</em>.</li>
                    <li>Business Recorder, <em>Pakistan Needs to Convert Youth Numbers into Economic Growth (January 2026)</em>.</li>
                    <li>Instagram / Tabadlab, <em>Pakistan's Population Crosses 252 Million: Youth Trends (2026)</em>.</li>
                    <li>World Bank Group, <em>Digital and AI Report: Jobs, Productivity, and Inclusive Growth (2026)</em>.</li>
                    <li>LinkedIn / MOITT, <em>Pakistan ICT Exports Reach Record High in FY 2025-26 (June 2026)</em>.</li>
                    <li>Medium / Khan Abdul Qadeer, <em>The Future of Pakistan's Freelance Economy: Export Growth (July 2026)</em>.</li>
                    <li>GSM Intelligence, <em>Pakistan: Progressing Towards a Fully Fledged Digital Economy (2020-2026)</em>.</li>
                    <li>OECD, <em>Digital Transformation 2026: Efficiency, Inclusion, and Innovation (2026)</em>.</li>
                    <li>UNESCO Institute for Statistics (UIS), <em>Culture 2026 Data Release: Preserving Global Heritage (2026)</em>.</li>
                    <li>BTI Project, <em>BTI 2026 Pakistan Country Report: Social and Political Trends (2026)</em>.</li>
                    <li>Global Diaspora Summit, <em>Insights and Practices for National Connection (2026)</em>.</li>
                    <li>Payoneer, <em>Pakistan IT Exports: What's Driving the Surge in 2026 (April 2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>The Meaning of Nation and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            193
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

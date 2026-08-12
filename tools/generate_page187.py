from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-187-global-orakzai-network.html'

GRAPHICS = [
    ("Global Network", "HERE", "↔", "GLOB"),
    ("Shared Identity", "SELF", "↔", "ALL"),
    ("Community Link", "ONE", "↔", "MANY"),
    ("Global Connect", "CITY", "↔", "CONT"),
    ("Diaspora Path", "GLOB", "↔", "HOME"),
    ("Local Essential", "HERE", "↔", "WISE"),
    ("Digital Connect", "NET", "↔", "TALK"),
    ("Comm Network", "SELF", "↔", "LINK"),
    ("Know Exchange", "WISE", "↔", "LEAR"),
    ("Mentorship Rail", "WISE", "↔", "YOUN"),
    ("Student Net", "LEAR", "↔", "LINK"),
    ("Professional Net", "WORK", "↔", "LINK"),
    ("Entrepreneur Net", "BIZ", "↔", "LINK"),
    ("Research Net", "WHY", "↔", "LINK"),
    ("Tech Network", "CODE", "↔", "LINK"),
    ("Edu Opportunity", "LEAR", "↔", "OPEN"),
    ("Scholarship Info", "CASH", "↔", "LEAR"),
    ("Career Develop", "WORK", "↔", "GROW"),
    ("Internship Path", "LEAR", "→", "WORK"),
    ("Skills Develop", "ABLE", "↔", "TIME"),
    ("Digital Literacy", "KNOW", "↔", "TECH"),
    ("Startup Collab", "IDEA", "↔", "BIZ"),
    ("Global Markets", "ALL", "↔", "NET"),
    ("Diaspora Invest", "CASH", "→", "HOME"),
    ("Remittance Rail", "CASH", "→", "HOME"),
    ("Know Transfer", "WISE", "→", "LEAR"),
    ("Tech Transfer", "CODE", "→", "BASE"),
    ("Global Talent", "ABLE", "↔", "GLOB"),
    ("Professional Dir", "NAME", "↔", "WORK"),
    ("Privacy Rail", "SELF", "↔", "SAFE"),
    ("Data Protection", "DATA", "↔", "SAFE"),
    ("Digital Security", "SEC", "↔", "SAFE"),
    ("Verified Info", "TRUE", "↔", "FACT"),
    ("Misinformation", "BAD", "≠", "TRUE"),
    ("Trust Asset", "TRUE", "↔", "SAFE"),
    ("Transparency", "OPEN", "↔", "TRUE"),
    ("Accountability", "DO", "↔", "RULE"),
    ("Voluntary Path", "FREE", "↔", "DO"),
    ("Diversity Rail", "MANY", "↔", "ONE"),
    ("Different Prof", "ALL", "↔", "WORK"),
    ("Different Gen", "PAST", "↔", "NEXT"),
    ("Intergen Know", "WISE", "→", "LEAR"),
    ("Youth Partic", "YOUN", "↔", "DO"),
    ("Women Partic", "GIRL", "↔", "DO"),
    ("Student Partic", "LEAR", "↔", "DO"),
    ("Elder Knowledge", "WISE", "↔", "LONG"),
    ("Cultural Pres", "PAST", "↔", "SAVE"),
    ("Orakzai History", "PAST", "↔", "DATA"),
    ("Oral History", "TALK", "→", "SAVE"),
    ("Family History", "HOME", "↔", "SAVE"),
    ("Archive Rail", "DATA", "↔", "SAFE"),
    ("Cultural Doc", "TRUE", "↔", "SAVE"),
    ("Language Path", "TALK", "↔", "TRUE"),
    ("Pashto Rail", "PASH", "↔", "TRUE"),
    ("Local Dialect", "HERE", "↔", "PASH"),
    ("Storytelling", "TALK", "↔", "LIFE"),
    ("Poetry Rail", "ART", "↔", "LONG"),
    ("Music Path", "SONG", "↔", "SAVE"),
    ("Photography", "EYE", "↔", "SAVE"),
    ("Digital Heritage", "PAST", "↔", "NET"),
    ("Resp Archiving", "YES", "↔", "SAFE"),
    ("Edu Channel", "LEAR", "↔", "LINK"),
    ("Online Learning", "NET", "↔", "LEAR"),
    ("Uni Connection", "LEAR", "↔", "GLOB"),
    ("Research Collab", "WHY", "↔", "GLOB"),
    ("Tech Education", "CODE", "↔", "LEAR"),
    ("Entr Education", "BIZ", "↔", "LEAR"),
    ("Fin Literacy", "KNOW", "↔", "CASH"),
    ("Career Guidance", "WISE", "→", "WORK"),
    ("Global Exp", "GLOB", "↔", "WISE"),
    ("Local Knowledge", "HERE", "↔", "WISE"),
    ("Comm Problems", "HERE", "→", "FIX"),
    ("Local Inno", "HERE", "→", "BIZ"),
    ("Data Sovereignty", "OWN", "↔", "RULE"),
    ("Digital Diaspora", "GLOB", "↔", "HOME"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g187-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g187-{index}-title g187-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g187-{index}-title">{safe}</title><desc id="g187-{index}-desc">A global network relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g187-{index}-caption" class="diagram-caption">{index}. {safe} — Global network relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Global Orakzai Network Framework</title><desc id="hero-desc">A diagram showing the 2026 global community network landscape, featuring digital diaspora mobilization, indigenous data sovereignty, and the $10.9T global startup ecosystem connection.</desc><defs><linearGradient id="h187-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h187-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE GLOBAL COMMUNITY LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DIGITAL DIASPORA: ACTIVE MOBILIZATION (2026)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">INDIGENOUS DATA SOVEREIGNTY: BLOCKCHAIN-ENABLED</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">GLOBAL STARTUP VALUE: $10.9T ECOSYSTEM LINK</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">TRIBAL INTERNET NETWORKS: BRIDGING THE DIVIDE</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">AI-DRIVEN KNOWLEDGE TRANSFER & MENTORSHIP</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: AUTHENTIC CONNECTION</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">NETWORK: DECENTRALIZED, TRUSTED & SOVEREIGN</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">GLOBAL ORAKZAI NETWORK</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Connecting Communities, Knowledge, and Identity Across Borders: Trusted and Sovereign.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Global Community Loop: Navigating the 2026 landscape where digital diaspora mobilization, indigenous data sovereignty, and AI-driven knowledge transfer ensure that tribal identity thrives in a globally connected digital civilization.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 187</title>
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
            <p class="section-label">PAGE 187</p>
            <h2>GLOBAL ORAKZAI NETWORK</h2>
            <p>“Connecting Communities, Knowledge, Opportunity, and Identity Across Borders.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “A community does not end where its physical borders end. In an increasingly connected world, people can maintain relationships across cities, countries, and continents while participating in shared cultural, professional, and economic networks. For Orakzai people living in different parts of Pakistan and abroad, modern communications create new possibilities for connection. A Global Orakzai Network is a connected community of Orakzai people linking individuals, families, professionals, and students through shared identity and constructive cooperation. Its purpose is to create connection, exchange knowledge, and preserve cultural heritage for the people connected to it.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Digital Diasporas & Active Mobilization (2026)</h3>
                <p>By 2026, digital transformation has fundamentally reshaped how diaspora communities engage with their homelands. Social media and internet platforms have enabled **"Digital Diasporas"** to mobilize more actively, shaping global public opinion and navigating homeland challenges with unprecedented speed [1]. Transnational communities are now using digital innovation to design new ways of thinking and doing, moving beyond simple communication toward active participation in homeland development [2] [3].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Indigenous Data Sovereignty & Blockchain</h3>
                <p>A critical trend in 2026 is the rise of **Indigenous Data Sovereignty (IDS)**. As digital tools become more decentralized, communities are actively working to digitize, preserve, and share traditional knowledge on their own terms [4]. The development of **blockchain-based platforms** is enabling communities to operationalize IDS, ensuring that sensitive cultural information and community assets are managed securely and proactively [5]. This approach protects tribal governance and strengthens government functions in the AI age [6].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Tribal Internet Networks & Digital Equity</h3>
                <p>Meaningful connectivity is the foundation of any global network. The *2026 Tribal Internet Networks Census* highlights a significant growth in community-owned networks, bridging the digital divide for underserved populations [7]. These networks provide the infrastructure for **Advancing a Connected Future**, where indigenous communities worldwide can access critical resources, culturally adapted education, and international markets without permanently relocating [8] [9].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI-Driven Knowledge Transfer & Mentorship</h3>
                <p>While AI is transforming diaspora engagement by providing real-time guidance and personalized learning, **human mentorship** remains the essential link for transferring practical wisdom [10] [11]. Professional and student networks are utilizing AI to circulate information about scholarships and career pathways, while diaspora investment connects local businesses with international capital and expertise [12]. For the Orakzai community, the **Sovereign Grid** ensures that this global network remains decentralized, trusted, and authentic [13].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Global Orakzai Network</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, our network is the digital expression of our tribal strength. We do not just live in different places; we build together across borders. By mastering digital sovereignty and AI-driven knowledge transfer while remaining rooted in our shared identity, we are ensuring that the Global Orakzai Network is a source of opportunity and dignity for every member. We are the architects of a sovereign community that is globally connected and locally rooted.”</p>
            </div>

            <div class="final-statement">
                CONNECTED IDENTITY.<br>
                SOVEREIGN COOPERATION.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>New Lines Institute, <em>Digital Diasporas: How Social Media and the Internet Transform Mobilization (September 2025)</em>.</li>
                    <li>IOM (International Organization for Migration), <em>Diaspora Engagement: Empowered Individuals and Safe Mobility (2026)</em>.</li>
                    <li>iDiaspora, <em>Digital Diaspora: Technological Tools for Engagement and Innovation (2026)</em>.</li>
                    <li>IWGIA, <em>The Indigenous World 2026: Indigenous Data Sovereignty and Decentralized Tools (April 2026)</em>.</li>
                    <li>PubMed / PMC, <em>Development of a Blockchain-Based Platform to Enable Indigenous Data Sovereignty (2026)</em>.</li>
                    <li>Brookings Institution, <em>Defining Digital Sovereignty for Tribal Nations in the AI Age (2026)</em>.</li>
                    <li>Community Networks / ILSR, <em>2026 Census of Tribal Internet Networks: Bridging the Divide (June 2026)</em>.</li>
                    <li>Internet Society, <em>Advancing a Connected Future for Indigenous Communities (August 2026)</em>.</li>
                    <li>African Diaspora Network, <em>African Diaspora Investment Symposium 2026 (ADIS26): Investment Trends (2026)</em>.</li>
                    <li>LinkedIn / AI Insights, <em>AI and the Future of Knowledge Transfer: Upskilling the Next Workforce (2026)</em>.</li>
                    <li>Diaspora for Development, <em>AI Meets Diaspora: How Technology is Transforming Engagement (June 2025)</em>.</li>
                    <li>Digital Education Council, <em>AI in Higher Education Global Survey 2026: Understanding and Transformation (2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Global Orakzai Network and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                    <li>Indiaspora, <em>India and its Diaspora: Partners in Progress Report (April 2026)</em>.</li>
                    <li>IMF eLibrary, <em>Unlocking the Potential: AI in Sub-Saharan Africa and Emerging Markets (July 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            187
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

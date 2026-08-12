from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-191-the-meaning-of-identity.html'

GRAPHICS = [
    ("Identity Meaning", "SELF", "↔", "ALL"),
    ("Heritage Link", "PAST", "↔", "NEXT"),
    ("I'm Orakzai", "SELF", "↔", "NAME"),
    ("Belonging Rail", "ONE", "↔", "MANY"),
    ("Personal Ident", "SELF", "↔", "LIFE"),
    ("Multilayered Id", "MANY", "↔", "ONE"),
    ("Family First", "HOME", "↔", "BASE"),
    ("Ancestry Path", "PAST", "↔", "TRUE"),
    ("Memory Base", "MIND", "↔", "SAVE"),
    ("Oral History", "TALK", "→", "SAVE"),
    ("Stories Path", "TALK", "↔", "WISE"),
    ("Language Mech", "TALK", "↔", "TRUE"),
    ("Pashto Rail", "PASH", "↔", "TRUE"),
    ("Living Culture", "PAST", "→", "NEW"),
    ("Tradition Rail", "OLD", "↔", "NEXT"),
    ("Change Path", "OLD", "→", "NEW"),
    ("Modern Identity", "PAST", "↔", "NOW"),
    ("Ident & Tech", "SELF", "↔", "TECH"),
    ("Digital Identity", "NET", "↔", "SELF"),
    ("Digital Memory", "DATA", "↔", "TIME"),
    ("Resp Preserve", "TRUE", "↔", "SAFE"),
    ("Photo Record", "EYE", "↔", "SAVE"),
    ("Audio/Video Rec", "MOVE", "↔", "SAVE"),
    ("Documentation", "TRUE", "↔", "WISE"),
    ("Archive Rail", "DATA", "↔", "SAFE"),
    ("Comm Archive", "ALL", "↔", "DATA"),
    ("Digital Archive", "NET", "↔", "DATA"),
    ("Authenticity", "TRUE", "↔", "SAFE"),
    ("Hist Evidence", "FACT", "↔", "TRUE"),
    ("Memory vs Hist", "MIND", "↔", "FACT"),
    ("Respect Diff", "MANY", "↔", "TRUE"),
    ("Orakzai Divers", "MANY", "↔", "ONE"),
    ("Local vs Diasp", "HERE", "↔", "GLOB"),
    ("Generational", "OLD", "↔", "YOUN"),
    ("Youth Identity", "YOUN", "↔", "NEXT"),
    ("Women Identity", "GIRL", "↔", "TRUE"),
    ("Prof Identity", "WORK", "↔", "SELF"),
    ("Edu Expansion", "LEAR", "↔", "SELF"),
    ("Science Rail", "WHY", "↔", "TRUE"),
    ("Tech Bridge", "TECH", "↔", "BASE"),
    ("Entr Path", "BIZ", "↔", "SELF"),
    ("Global Partic", "SELF", "↔", "GLOB"),
    ("Global Citizen", "SELF", "↔", "ALL"),
    ("Pakistani Id", "SELF", "↔", "FLAG"),
    ("Pashtun Identity", "SELF", "↔", "PASH"),
    ("No Stereotype", "ONE", "≠", "ALL"),
    ("Character Base", "DO", "↔", "TRUE"),
    ("Responsibility", "SELF", "↔", "DO"),
    ("Ident Choice", "SELF", "↔", "FREE"),
    ("Ident/Exclusion", "SELF", "≠", "HATE"),
    ("Respect Others", "SELF", "↔", "ALL"),
    ("Dignity Base", "ALL", "↔", "TRUE"),
    ("Comm Relations", "ALL", "↔", "LINK"),
    ("Solidarity Path", "MANY", "↔", "ONE"),
    ("Service Rail", "HELP", "↔", "TRUE"),
    ("Edu Service", "LEAR", "↔", "HELP"),
    ("Know Service", "WISE", "↔", "ALL"),
    ("Entr Service", "BIZ", "↔", "HELP"),
    ("Tech Service", "TECH", "↔", "FIX"),
    ("Preserve Service", "SAVE", "↔", "NEXT"),
    ("Ident & Memory", "SELF", "↔", "SAVE"),
    ("Doc Memory", "TRUE", "↔", "LONG"),
    ("Family Archive", "HOME", "↔", "DATA"),
    ("Verify Records", "FACT", "↔", "SAFE"),
    ("Digital Twin", "PHYS", "↔", "DIGI"),
    ("Virtual World", "NET", "↔", "SELF"),
    ("AI Genealogy", "AI", "↔", "PAST"),
    ("Global Belong", "GLOB", "↔", "SELF"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g191-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g191-{index}-title g191-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g191-{index}-title">{safe}</title><desc id="g191-{index}-desc">An identity relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g191-{index}-caption" class="diagram-caption">{index}. {safe} — Identity relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">The Meaning of Identity Framework</title><desc id="hero-desc">A diagram showing the 2026 identity landscape, featuring AI-driven genealogy, digital cultural heritage preservation, and the intersection of global citizenship and local belonging.</desc><defs><linearGradient id="h191-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h191-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE IDENTITY TRANSFORMATION LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AI GENEALOGY: REVOLUTIONIZING FAMILY RESEARCH</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL TWINS: PRESERVING CULTURAL IDENTITY</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AC/E DIGITAL CULTURE: NAVIGATING VOLATILITY</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">GLOBAL CITIZENSHIP EDUCATION: INFORMED & ENGAGED</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CULTURAL IDENTITY AT THE CROSSROADS OF VIRTUAL WORLDS</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: AUTHENTIC BELONGING</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">IDENTITY: HERITAGE, MEMORY, RESPONSIBILITY & CHOICE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">I’M ORAKZAI — THE MEANING OF IDENTITY</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Identity as Heritage, Memory, Responsibility, and Choice: Lived and Inherited.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Identity Transformation Loop: Navigating the 2026 landscape where AI-driven genealogy, digital twin preservation, and global citizenship education ensure that Orakzai identity remains authentic, multilayered, and resilient.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 191</title>
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
            <p class="section-label">PAGE 191</p>
            <h2>I’M ORAKZAI — THE MEANING OF IDENTITY</h2>
            <p>“Identity as Heritage, Memory, Responsibility, and Choice.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “I’m Orakzai. Three words can carry a lifetime of meaning. They can connect a person to family, history, language, and community. But identity is never only a label. It is a relationship with the past and a responsibility toward the future. To say ‘I’m Orakzai’ can mean remembering where your family came from, knowing the stories of those who came before you, and choosing what kind of person you want to become. Identity is inherited, but identity is also lived.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">AI-Powered Genealogy & Family History (2026)</h3>
                <p>By 2026, artificial intelligence is revolutionizing how individuals research their family history and ancestry. AI can now transcribe record images—including those that are handwritten—making it easier for researchers to search and read historical documents [1]. AI assistants are being used to process and analyze thousands of documents in seconds, a task that previously would have taken humans years to complete [2]. This "AI Genealogy" makes family research faster, more thorough, and surprisingly intuitive [3] [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Cultural Heritage & Virtual Identity</h3>
                <p>The *AC/E Digital Culture Annual Report 2026* highlights the challenge of navigating cultural preservation in a volatile digital world [5]. Digital twins are emerging as a powerful tool for safeguarding cultural heritage, especially in the wake of conflicts or natural disasters [6]. These virtual representations showcase the potential for preserving cultural identity while also raising critical privacy and ethical concerns [7]. Digitization and virtual access are now fundamental to cultural heritage research, driving new acts of communication between generations [8] [9].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Global Citizenship in a Digital Age</h3>
                <p>In 2026, global citizenship education is being redefined for the digital era. UNESCO guidelines help teachers understand the critical role that digital citizenship plays in promoting a more informed and engaged society [10]. Linking digital literacy with global citizenship is essential to equip learners with the critical, ethical, and participatory skills needed for the 21st century [11]. The future of belonging in education explores how institutions can foster inclusion and identity alongside human progress [12] [13].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Identity, Responsibility & Sovereign Legacy</h3>
                <p>Strong cultural identity does not require exclusion or hostility; it is built on respect for others and individual dignity. Heritage provides belonging, but **responsibility** determines what a person does with that inheritance [14]. For the Orakzai community, the **Sovereign Grid** ensures that identity is documented responsibly and authentically, distinguishing personal memory from independently verified historical evidence [15]. By mastering digital identity and global participation, we are ensuring that the Orakzai name remains a source of pride and service for generations to come [16].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: The Meaning of Identity</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, our identity is the foundation of our character. We do not just carry a name; we carry a legacy. By mastering AI-driven genealogy and digital preservation while remaining rooted in our Pashtun values of dignity and service, we are ensuring that ‘I’m Orakzai’ remains a meaningful statement for the next century. We are the architects of an identity that is sovereign, multilayered, and eternal. Our past is our strength, and our future is our choice.”</p>
            </div>

            <div class="final-statement">
                INHERITED STRENGTH.<br>
                LIVED RESPONSIBILITY.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>FamilySearch Blog, <em>AI Developments in Genealogy and How They Impact You (February 2026)</em>.</li>
                    <li>JewishGen / Facebook, <em>The State of AI in Historical Document Analysis (August 2026)</em>.</li>
                    <li>YouTube / Family History AI, <em>2026: The Year AI Takes Over Genealogy Research (January 2026)</em>.</li>
                    <li>RootsTech / FamilySearch, <em>AI-Powered Family History Research: Faster and Intuitive (2026)</em>.</li>
                    <li>Accion Cultural Española, <em>AC/E Digital Culture Annual Report 2026: Navigating Volatility (2026)</em>.</li>
                    <li>UNESCO, <em>Protecting and Preserving Cultural Diversity in the Digital Era (2023-2026)</em>.</li>
                    <li>IFLA News, <em>Predicting the Future: Digital Twins and Cultural Heritage (November 2024)</em>.</li>
                    <li>MDPI / Sustainability, <em>The Evolution of Digital Cultural Heritage Research (2024-2026)</em>.</li>
                    <li>ScienceDirect, <em>Artificial Intelligence Adoption in the Cultural Heritage Sector (2026)</em>.</li>
                    <li>UNESCO, <em>Global Citizenship Education in a Digital Age: Teacher Guidelines (June 2026)</em>.</li>
                    <li>IAI (Istituto Affari Internazionali), <em>How to Build Digital Citizenship in the 21st Century (February 2026)</em>.</li>
                    <li>IGI Global, <em>The Future of Global Citizenship and Belonging in Education (2026)</em>.</li>
                    <li>Science Publishing Group, <em>Cultural Identity at the Crossroads of Virtual Worlds (June 2026)</em>.</li>
                    <li>European Heritage Hub, <em>Digital Cultural Heritage: Imagination, Innovation and Opportunity (2026)</em>.</li>
                    <li>Maastricht University, <em>Global Citizenship Education in the Digital Age: A Complex Set of Concepts (January 2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>The Meaning of Identity and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            191
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-192-the-meaning-of-heritage.html'

GRAPHICS = [
    ("Heritage Meaning", "PAST", "↔", "NEXT"),
    ("I'm Pashtun", "SELF", "↔", "NAME"),
    ("Heritage Base", "MIND", "↔", "SAVE"),
    ("Not Static Rail", "OLD", "→", "NEW"),
    ("Pashtun Heritage", "ALL", "↔", "TRUE"),
    ("Society Divers", "MANY", "↔", "ONE"),
    ("Many Homes", "HERE", "↔", "GLOB"),
    ("Borders Rail", "LINE", "≠", "LIFE"),
    ("Diaspora Path", "HOME", "→", "GLOB"),
    ("Local & Global", "SELF", "↔", "ALL"),
    ("Language Mech", "TALK", "↔", "TRUE"),
    ("Pashto Rail", "PASH", "↔", "TRUE"),
    ("Lang & Memory", "TALK", "↔", "MIND"),
    ("Teach Lang", "WISE", "→", "YOUN"),
    ("Writing Base", "BOOK", "↔", "LONG"),
    ("Poetry Path", "SOUL", "↔", "TRUE"),
    ("Oral Tradition", "TALK", "→", "SAVE"),
    ("Oral Hist Rec", "MOVE", "↔", "SAVE"),
    ("Evidence/Memory", "FACT", "↔", "MIND"),
    ("History Base", "PAST", "↔", "WISE"),
    ("Study History", "WHY", "↔", "TRUE"),
    ("No Romanticize", "PAST", "≠", "BEST"),
    ("Difficult Parts", "TRUE", "↔", "SAFE"),
    ("Hist Honesty", "TRUE", "↔", "WISE"),
    ("Family History", "HOME", "↔", "PAST"),
    ("Names Path", "NAME", "↔", "SAVE"),
    ("Places Rail", "HERE", "↔", "MIND"),
    ("Photo Record", "EYE", "↔", "SAVE"),
    ("Letter Record", "PEN", "↔", "SAVE"),
    ("Family Archive", "HOME", "↔", "DATA"),
    ("Digital Archive", "NET", "↔", "DATA"),
    ("Privacy Rail", "SAFE", "↔", "DO"),
    ("Consent Path", "YES", "↔", "SAFE"),
    ("Comm Archive", "ALL", "↔", "DATA"),
    ("Access Rail", "WHO", "↔", "SAFE"),
    ("Authenticity", "TRUE", "↔", "SAFE"),
    ("Cultural Know", "ALL", "↔", "WISE"),
    ("Food Memory", "EAT", "↔", "HOME"),
    ("Clothing Rail", "WEAR", "↔", "TRUE"),
    ("Music Path", "SONG", "↔", "SOUL"),
    ("Poetry/Song", "SONG", "↔", "LONG"),
    ("Architecture", "BASE", "↔", "LONG"),
    ("Hospitality", "GIVE", "↔", "TRUE"),
    ("Comm Relations", "ALL", "↔", "LINK"),
    ("Family Network", "HOME", "↔", "LINK"),
    ("Generations", "OLD", "↔", "YOUN"),
    ("Elder Wisdom", "WISE", "→", "LEAR"),
    ("Youth Interp", "YOUN", "→", "NEW"),
    ("Women Heritage", "GIRL", "↔", "TRUE"),
    ("Men Experience", "BOY", "↔", "TRUE"),
    ("Gen Experience", "OLD", "↔", "YOUN"),
    ("Urban Identity", "CITY", "↔", "SELF"),
    ("Diaspora Ident", "GLOB", "↔", "SELF"),
    ("Multiple Ident", "MANY", "↔", "ONE"),
    ("No Exclusion", "SELF", "≠", "HATE"),
    ("Respect Other", "SELF", "↔", "ALL"),
    ("Humanity Base", "ALL", "↔", "TRUE"),
    ("Ident/Dignity", "SELF", "↔", "TRUE"),
    ("No Stereotype", "ONE", "≠", "ALL"),
    ("Modern Pashtun", "SELF", "↔", "NOW"),
    ("Edu Strength", "LEAR", "↔", "SAVE"),
    ("Science Rail", "WHY", "↔", "TRUE"),
    ("Tech Bridge", "TECH", "↔", "BASE"),
    ("Digital Pashtun", "NET", "↔", "PASH"),
    ("Lang Preserve", "PASH", "↔", "SAVE"),
    ("AI & Pashto", "AI", "↔", "PASH"),
    ("Responsible AI", "TRUE", "↔", "SAFE"),
    ("Digitization", "PHYS", "→", "DIGI"),
    ("Metadata Rail", "DATA", "↔", "SAFE"),
    ("Long-Term Pres", "SAVE", "↔", "LONG"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Qehwa AI", "AI", "↔", "PASH"),
    ("Katib Tool", "TALK", "→", "TEXT"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g192-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g192-{index}-title g192-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g192-{index}-title">{safe}</title><desc id="g192-{index}-desc">A heritage relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g192-{index}-caption" class="diagram-caption">{index}. {safe} — Heritage relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">I’M PASHTUN — The Meaning of Heritage Framework</title><desc id="hero-desc">A diagram showing the 2026 Pashtun heritage landscape, featuring Qehwa AI, the recovery of 513 smuggled artefacts, and the UNESCO Culture 2026 Data Release.</desc><defs><linearGradient id="h192-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h192-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE HERITAGE PRESERVATION LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">QEHWA AI & KATIB: PASHTO AI BREAKTHROUGHS (2026)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">HERITAGE RECOVERY: 513 ARTEFACTS RETURNED TO PAKISTAN</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">UNESCO CULTURE 2026: TRACKING GLOBAL HERITAGE TARGETS</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">BPSTD: BILINGUAL PASHTO SPEECH & TEXT DATASET (2026)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">ISAC: CULTURAL HERITAGE PRESERVATION IN AFGHANISTAN</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: CULTURAL CONTINUITY</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">HERITAGE: MEMORY, LANGUAGE, COMMUNITY & CONTINUITY</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">I’M PASHTUN — THE MEANING OF HERITAGE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Heritage as Memory, Language, Community, and Continuity: Inherited and Interpreted.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Heritage Preservation Loop: Navigating the 2026 landscape where Pashto AI breakthroughs, the recovery of smuggled artefacts, and UNESCO global tracking ensure that Pashtun heritage remains living, resilient, and authentic.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 192</title>
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
            <p class="section-label">PAGE 192</p>
            <h2>I’M PASHTUN — THE MEANING OF HERITAGE</h2>
            <p>“Heritage as Memory, Language, Community, and Continuity.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “I’m Pashtun. For many, these words express a connection to a broad cultural and historical heritage that extends across generations and borders. But heritage is more than ancestry; it lives in language, family stories, poetry, hospitality, and relationships. It evolves as every generation encounters a changing world. To say ‘I’m Pashtun’ is not to claim a single experience—our communities are diverse, living in different countries and cities. Heritage is inherited, but it is also interpreted, practiced, and passed forward.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Pashto AI Era & Major Breakthroughs (2026)</h3>
                <p>2026 marks the entry of the Pashto language into the AI era with significant breakthroughs. Two young innovators in Peshawar have developed **Qehwa AI** and **Katib**, powerful tools that generate Pashto responses and convert speech into text [1]. Furthermore, the **Bilingual Pashto Speech and Text Dataset (BPSTD)** has been released to facilitate research in voice processing and speech recognition for the 60M+ speakers of this low-resource language [2] [3]. These developments ensure that Pashto literature and oral traditions are preserved in the digital civilization [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Heritage Recovery & Global Preservation Targets</h3>
                <p>Pakistan’s rich cultural heritage received a major boost in July 2026 with the recovery of **513 archaeological artefacts** illegally smuggled to the United States [5]. Globally, the **UNESCO Culture 2026 Data Release** provides new indicators to track progress toward target 11.4, focusing on the preservation of global heritage [6]. In Afghanistan, major projects led by ISAC continue to safeguard ancient cultures despite political challenges, emphasizing the importance of historical honesty and authenticity [7] [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Diversity, Diaspora & Digital Preservation</h3>
                <p>Pashtun communities comprise **15.4% of Pakistan’s population** (approx. 38.8 million) and form a significant global diaspora [9]. The *Global Diaspora Summit Report* captures insights into how these communities negotiate between ancestral heritage and global society [10]. Digital platforms now help preserve poetry, music, and family archives, though they require long-term maintenance and cybersecurity [11]. The challenge remains to bridge generations, allowing experience and innovation to work together in a changing world [12].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Sovereignty, Dignity & The Future of Heritage</h3>
                <p>Understanding heritage requires a mature perspective that includes both achievements and difficult chapters. Cultural pride does not require exaggeration, and identity should not be reduced to stereotypes [13]. For the Orakzai community, the **Sovereign Grid** serves as a bridge between heritage and the modern world, ensuring that language, stories, and social practices are carried forward with dignity [14]. By mastering technology as a tool for preservation, we are ensuring that Pashtun identity remains authentic and resilient [15].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: I’m Pashtun — The Meaning of Heritage</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Pashtun people, our heritage is the soul of our identity. We do not just inherit the past; we practice it in the present. By mastering Pashto AI and digital preservation while remaining rooted in our values of hospitality and dignity, we are ensuring that our culture is not just a memory but a living force. We are the builders of a heritage that is sovereign, diverse, and eternal. Our language is our legacy, and our continuity is our strength.”</p>
            </div>

            <div class="final-statement">
                LIVING HERITAGE.<br>
                ENDURING IDENTITY.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Nukta Pakistan / Facebook, <em>Artificial Intelligence in Pashto: Qehwa AI and Katib Breakthroughs (April 2026)</em>.</li>
                    <li>Mendeley Data, <em>BPSTD: A Bilingual Pashto Speech and Text Dataset for Low-Resource Research (March 2026)</em>.</li>
                    <li>Facebook / Pashto Tech Group, <em>Pashto Language Enters the AI Era: Innovators Ahmad and Uzair (April 2026)</em>.</li>
                    <li>IEEE Xplore, <em>Development of Isolated Words Corpus for Pashto Automatic Speech Recognition (2026)</em>.</li>
                    <li>Instagram / Pakistan Heritage, <em>Recovery of 513 Smuggled Artefacts from the United States (July 2026)</em>.</li>
                    <li>UNESCO Institute for Statistics (UIS), <em>Culture 2026 Data Release: Tracking Global Heritage Targets (2026)</em>.</li>
                    <li>Institute for the Study of Ancient Cultures (ISAC), <em>Preservation of Cultural Heritage in Afghanistan (2026)</em>.</li>
                    <li>ICCROM, <em>Leveraging Cultural Heritage: Research and Field Experience (2026)</em>.</li>
                    <li>World Factbook / Wikipedia, <em>Pashtun Population and Diaspora Statistics (2024-2026)</em>.</li>
                    <li>iDiaspora, <em>Global Diaspora Summit Report: Insights and Practices (2026)</em>.</li>
                    <li>MDPI / Sustainability, <em>Conservation Challenges and Digital Heritage Trends in Pakistan (2021-2026)</em>.</li>
                    <li>ASEAN Socio-Cultural Community, <em>Trend Report: Digital Trends for Culture and Heritage (2026)</em>.</li>
                    <li>Sage Journals, <em>Afghanistan’s Digital Diaspora: Conflicted Constructions of Identity (2026)</em>.</li>
                    <li>BTI Project, <em>BTI 2026 Afghanistan Country Report: Social and Political Trends (2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>The Meaning of Heritage and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            192
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

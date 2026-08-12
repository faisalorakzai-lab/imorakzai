from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-183-preserving-identity-for-100-years.html'

GRAPHICS = [
    ("Century Memory", "PAST", "↔", "2126"),
    ("Living Identity", "LIVE", "↔", "TIME"),
    ("Preserve Path", "SAVE", "↔", "NEXT"),
    ("Evolution Rail", "PAST", "↔", "NEW"),
    ("Memory Base", "PAST", "↔", "WISE"),
    ("Family Memory", "HOME", "↔", "SAVE"),
    ("Oral History", "TALK", "→", "SAVE"),
    ("Record Voice", "HEAR", "↔", "SAVE"),
    ("Record Story", "TALK", "↔", "WISE"),
    ("Family Archive", "HOME", "↔", "DATA"),
    ("Digital Archive", "DATA", "↔", "SAFE"),
    ("Digital Chall", "DATA", "≠", "LONG"),
    ("Format Obsol", "OLD", "→", "NONE"),
    ("Digital Pres", "SAVE", "↔", "TIME"),
    ("Backup Rail", "ONE", "↔", "MANY"),
    ("Metadata Path", "INFO", "↔", "DATA"),
    ("Redundancy Rail", "MANY", "↔", "SAFE"),
    ("3-2-1 Principle", "3CPY", "↔", "SAFE"),
    ("Offline Archive", "PHYS", "↔", "SAFE"),
    ("Cloud Storage", "NET", "↔", "SAVE"),
    ("Open Formats", "OPEN", "↔", "LONG"),
    ("Documentation", "TRUE", "↔", "WISE"),
    ("Context Rail", "HERE", "↔", "TRUE"),
    ("Photo Evidence", "EYE", "↔", "TRUE"),
    ("Family Photos", "HOME", "↔", "NAME"),
    ("Video Archive", "MOVE", "↔", "SAVE"),
    ("Audio Archive", "HEAR", "↔", "SAVE"),
    ("Manuscript Rail", "BOOK", "↔", "SAVE"),
    ("Digitization", "PHYS", "→", "DIGI"),
    ("Authenticity", "TRUE", "↔", "SAFE"),
    ("Provenance Path", "WHO", "↔", "TRUE"),
    ("Hist Accuracy", "FACT", "↔", "TRUE"),
    ("Memory vs Hist", "SELF", "↔", "FACT"),
    ("Comm Narrative", "ALL", "↔", "WISE"),
    ("Multi Perspect", "MANY", "↔", "ONE"),
    ("Cultural Bal", "ALL", "↔", "TRUE"),
    ("Language Rail", "TALK", "↔", "TRUE"),
    ("Pashto Continuity", "PASH", "↔", "TIME"),
    ("Digital Presence", "PASH", "↔", "NET"),
    ("Digital Keyboard", "TYPE", "↔", "NET"),
    ("Digital Publish", "BOOK", "↔", "NET"),
    ("Lang Corpora", "DATA", "↔", "PASH"),
    ("Machine Trans", "AI", "↔", "PASH"),
    ("AI & Language", "AI", "↔", "TALK"),
    ("Cultural Know", "ALL", "↔", "WISE"),
    ("Music Archive", "SONG", "↔", "SAVE"),
    ("Poetry Rail", "ART", "↔", "LONG"),
    ("Storytelling", "TALK", "↔", "LIFE"),
    ("Food Culture", "COOK", "↔", "SAVE"),
    ("Crafts Path", "MAKE", "↔", "SAVE"),
    ("Architecture", "BASE", "↔", "SAVE"),
    ("Clothing Rail", "WEAR", "↔", "SAVE"),
    ("Ceremonies", "ALL", "↔", "SAVE"),
    ("Family Trad", "HOME", "↔", "SAVE"),
    ("Comm Tradition", "ALL", "↔", "SAVE"),
    ("Religious Life", "TRUE", "↔", "SAVE"),
    ("Cultural Change", "OLD", "→", "NEW"),
    ("Right to Change", "SELF", "↔", "FREE"),
    ("Young People", "YOUN", "↔", "NEXT"),
    ("Youth Archivist", "YOUN", "→", "SAVE"),
    ("Digital Story", "TALK", "↔", "NET"),
    ("Social Media", "FAST", "≠", "SAVE"),
    ("Personal Web", "SELF", "↔", "NET"),
    ("Digital Library", "BOOK", "↔", "DATA"),
    ("Comm Database", "ALL", "↔", "DATA"),
    ("Family Tree", "PAST", "↔", "LINK"),
    ("Gen Caution", "TRUE", "↔", "SAFE"),
    ("100-Year Archive", "LONG", "↔", "SAFE"),
    ("AI Assistant", "AI", "↔", "HELP"),
    ("Heritage 4.0", "DIGI", "↔", "NEXT"),
    ("Digital Twin", "PHYS", "↔", "DIGI"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g183-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g183-{index}-title g183-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g183-{index}-title">{safe}</title><desc id="g183-{index}-desc">A 100-year identity preservation relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g183-{index}-caption" class="diagram-caption">{index}. {safe} — Identity preservation relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Preserving Identity for 100 Years Framework</title><desc id="hero-desc">A diagram showing the 2026 framework for century-long preservation, featuring the 100-Year Archive, AI-driven genealogy, Heritage 4.0, and the 3-2-1 digital preservation principle.</desc><defs><linearGradient id="h183-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h183-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE 100-YEAR PRESERVATION LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">100-YEAR ARCHIVE: GLENN HEINLE (2026)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">AI GENEALOGY: 95% ACCURACY IN TRANSCRIPTION</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">HERITAGE 4.0: 3D IMAGING & DIGITAL TWINS</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">3-2-1 PRINCIPLE: REDUNDANCY & LONG-TERM BACKUP</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL LEGACY MARKET: $15.1B (2025) → $62.6B (2035)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: PRESERVING FOR 2126</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">IDENTITY: CONTINUITY THROUGH AUTHENTIC ADAPTATION</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">PRESERVING IDENTITY FOR 100 YEARS</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“A Century of Memory, Culture, Knowledge, and Continuity: Preserving for 2126.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The 100-Year Preservation Loop: Navigating the 2026 landscape where AI-driven genealogy, Heritage 4.0, and the "100-Year Archive" framework ensure that cultural identity remains living and accessible for the next century.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 183</title>
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
            <p class="section-label">PAGE 183</p>
            <h2>PRESERVING IDENTITY FOR 100 YEARS</h2>
            <p>“A Century of Memory, Culture, Knowledge, and Continuity.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Preserving identity for the next hundred years is not simply about protecting old photographs or recording family names. It is about preserving memory, language, knowledge, and values while allowing future generations the freedom to evolve. A culture survives not because it never changes, but because people continue to find meaning in it. The next century will bring technologies that are difficult to predict today. Future generations may live far from their ancestral communities, yet one question will remain: Will they still know where they came from? Preserving identity for 100 years means making sure the answer can remain yes.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The 100-Year Archive & Digital Strategy (2026)</h3>
                <p>By 2026, the concept of the **"100-Year Archive"** has become a central focus for digital strategy and long-term preservation architecture [1]. Experts at the *Digital Preservation Summit 2026* are moving beyond basic file storage to comprehensive strategies that address the risk of digital obsolescence [2] [3]. AI is playing an increasing role in digital preservation, improving governance, compliance, and the security of sovereign data [4] [5]. The global digital legacy market is estimated to hit **$62.60 billion by 2035**, reflecting the growing importance of century-long memory [6].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI-Driven Genealogy & Family History</h3>
                <p>2026 is being hailed as the year AI takes over genealogy research, with every researcher now utilizing **AI assistants** to publish family stories and grow their family trees [7] [8]. AI-assisted transcription of old records has improved accuracy rates by up to **95%**, even for poor handwriting or damaged documents [9]. Guidelines for the responsible use of AI in genealogy are ensuring that these tools uphold genealogical standards while making family discovery faster and more intuitive than ever before [10] [11].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Heritage 4.0: Digital Twins & 3D Technologies</h3>
                <p>**Heritage 4.0** represents a new paradigm where 3D imaging, additive manufacturing, and digital twins contribute to interactive and immersive cultural preservation [12]. The digital twin heritage preservation market is projected to reach **$7.2 billion by 2034**, growing at a CAGR of 16.7% [13]. These "Heritage Digital Twins" bring together data, models, sensors, and AI to ensure that architecture, crafts, and sacred knowledge are preserved in high-fidelity for the next century [14] [15].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The 3-2-1 Principle & Long-Term Redundancy</h3>
                <p>Long-term preservation requires deliberate strategies for backup, metadata, and file migration. The **3-2-1 Principle**—maintaining three copies of data on two different media types with one copy off-site—remains the gold standard for important digital archives [16]. Open formats and structured metadata ensure that photographs, videos, and oral histories retain their historical value for researchers in **2126** [17]. For the Orakzai community, this sovereign approach to archiving ensures that identity remains living and authentic for the next hundred years [18].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Preserving Identity for 100 Years</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, our identity is the bridge between our ancestors and our descendants. We do not just store files; we document meaning. By mastering the 100-Year Archive and AI-driven genealogy while remaining rooted in our values, we are ensuring that the Orakzai name thrives for the next century. We build for 2126, so that our children’s children will know their strength and their story. Our legacy is sovereign, authentic, and eternal.”</p>
            </div>

            <div class="final-statement">
                ARCHIVING MEANING.<br>
                BUILDING FOR 2126.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>DigitalPreservation.gov, <em>100-Year Archive Update: Long-Term Preservation Architecture (2026)</em>.</li>
                    <li>DPC Online, <em>Digital Preservation for an Uncertain Future: Speakers and Trends (2026)</em>.</li>
                    <li>Henry Stewart Conferences, <em>Digital Preservation Summit 2026: Securing Cultural Heritage (2026)</em>.</li>
                    <li>Preservica, <em>The Impact of AI on Digital Preservation and Archiving in 2026 (January 2026)</em>.</li>
                    <li>Google Groups / Digital Curation, <em>Digital Preservation Summit 2026: Moving Beyond Basic Storage (2026)</em>.</li>
                    <li>Precedence Research, <em>Digital Legacy Market Size and Projections 2035 (2026)</em>.</li>
                    <li>YouTube / Family History AI, <em>2026: The Year AI Takes Over Genealogy Research (January 2026)</em>.</li>
                    <li>Apple Podcasts, <em>EP39: 2026 Predictions for Family History AI Platforms (December 2025)</em>.</li>
                    <li>JewishGen / Facebook, <em>How AI Will Change Genealogy in 2026: 95% Transcription Accuracy (January 2026)</em>.</li>
                    <li>Chronicle Makers / Substack, <em>How AI Will Change Genealogy 2026: Published Stories Explode (January 2026)</em>.</li>
                    <li>RootsTech / FamilySearch, <em>Guidelines for the Responsible Use of AI in Genealogy in 2026 (2026)</em>.</li>
                    <li>MDPI, <em>Heritage 4.0: How Applied 3D Technologies and Digital Twins Contribute to Preservation (2026)</em>.</li>
                    <li>DataIntelo, <em>Digital Twin Heritage Preservation Market Size and Projections 2034 (2026)</em>.</li>
                    <li>SciForum, <em>The Next Generation of Heritage Digital Twins: Models, Sensors, and AI (July 2026)</em>.</li>
                    <li>European Commission, <em>AI for 3D Digital Twins in Cultural Heritage: Event Highlights (March 2026)</em>.</li>
                    <li>CCAHA / Facebook, <em>Tips for Identifying and Selecting Digital Content to Preserve (April 2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>100-Year Identity Preservation and Sovereign Archive Framework (August 2026)</em>.</li>
                    <li>NEDCC, <em>The Relevance of Preservation in a Digital World: Reformatting and Archives (2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            183
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

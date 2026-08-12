from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-105-digital-preservation-of-history.html'

GRAPHICS = [
    ("What is digital preservation?", "MANAGED PROCESS", "LONG-TERM ACCESS", "AUTHENTICITY"),
    ("Why preserve history?", "FAMILY MEMORY", "TRIBAL IDENTITY", "FUTURE EVIDENCE"),
    ("Historical sources", "PRIMARY EVIDENCE", "SECONDARY ANALYSIS", "CULTURAL CONTEXT"),
    ("Primary vs secondary", "DIRECT WITNESS", "LATER INTERPRETATION", "EVIDENTIARY VALUE"),
    ("Digitization vs preservation", "DIGITAL CAPTURE", "LONG-TERM STEWARDSHIP", "SUSTAINABILITY"),
    ("Photographs", "PEOPLE + PLACES", "CLOTHING + EVENTS", "VISUAL MEMORY"),
    ("Photograph workflow", "ORIGINAL → SCAN", "METADATA → BACKUP", "ARCHIVE"),
    ("Photo metadata", "WHO + WHAT", "WHEN + WHERE", "SOURCE + RIGHTS"),
    ("Family photographs", "LIVED EXPERIENCE", "ORAL CONTEXT", "GENEALOGICAL DATA"),
    ("Oral history", "SPOKEN MEMORY", "PERSONAL NARRATIVE", "CULTURAL RECORD"),
    ("Consent", "INFORMED", "VOLUNTARY", "DOCUMENTED PERMISSION"),
    ("Recording oral histories", "AUDIO + VIDEO", "TRANSCRIPTION", "PRESERVATION"),
    ("Pashto oral history", "ORIGINAL VOICE", "DIALECT VARIATION", "VOCABULARY"),
    ("Translation", "ORIGINAL TEXT", "INTERPRETIVE TEXT", "CROSS-CULTURAL ACCESS"),
    ("Manuscripts", "HANDWRITTEN", "RELIGIOUS / LITERARY", "PRIMARY SOURCE"),
    ("Document digitization", "CAPTURE → OCR", "REVIEW → METADATA", "ARCHIVE"),
    ("OCR", "IMAGE → TEXT", "HUMAN REVIEW", "SEARCHABLE DATA"),
    ("Manuscript preservation", "PAGE ORDER", "MARGINAL NOTES", "PHYSICAL CONTEXT"),
    ("Maps", "HISTORICAL GEOGRAPHY", "VILLAGE NAMES", "SPATIAL MEMORY"),
    ("Place names", "LOCAL NAME", "VARIANT", "SOURCE + DATE"),
    ("Genealogies", "FAMILY TREE", "PROVENANCE", "IDENTITY RECORD"),
    ("Colonial records", "ADMINISTRATIVE DATA", "CRITICAL READING", "HISTORICAL BIAS"),
    ("Multiple sources", "TRIANGULATION", "CROSS-VERIFICATION", "STRONGER HISTORY"),
    ("Newspapers", "PUBLIC EVENTS", "COMMUNITY DEBATE", "HISTORICAL RECORD"),
    ("Audio archives", "VOICE + MUSIC", "PRONUNCIATION", "LIVING SOUND"),
    ("Video archives", "FESTIVALS + RITUALS", "VISUAL PERFORMANCE", "DYNAMIC RECORD"),
    ("File formats", "TIFF / WAV / PDF/A", "JPEG / MP3 / PDF", "SUSTAINABILITY"),
    ("Master files", "PRESERVATION MASTER", "CASUAL EDIT PROTECT", "HIGH QUALITY"),
    ("Metadata", "DATA ABOUT DATA", "CONTEXT + MEANING", "DISCOVERABILITY"),
    ("Metadata categories", "DESCRIPTIVE / TECH", "RIGHTS / PRESERV", "STRUCTURAL / ADMIN"),
    ("File naming", "YYYYMMDD_LOC", "SUBJECT_SEQ", "CONSISTENCY"),
    ("Folder structure", "LOGICAL HIERARCHY", "ORGANIZATION", "DISCOVERABILITY"),
    ("Backup", "3 COPIES", "2 MEDIA TYPES", "1 OFFSITE"),
    ("Cloud storage", "REMOTE ACCESS", "REDUNDANCY", "VENDOR RISK"),
    ("Offline archives", "LOCAL COPY", "OFFSITE COPY", "OFFLINE SAFETY"),
    ("Checksums", "FILE HASH", "INTEGRITY CHECK", "DATA SAFETY"),
    ("Version control", "ORIGINAL", "EDITED VERSIONS", "PUBLISHED COPY"),
    ("Authenticity", "PROVENANCE", "CONTEXT + INTEGRITY", "DOCUMENTATION"),
    ("Provenance", "CREATOR → OWNER", "CHAIN OF CUSTODY", "VERIFIED SOURCE"),
    ("AI and history", "NLP ASSISTANCE", "OCR / TRANSCRIPT", "NOT AUTHORITY"),
    ("AI image restoration", "ORIGINAL PRESERVE", "DOCUMENTED EDIT", "VERSION HISTORY"),
    ("Deepfakes", "SYNTHETIC MEDIA", "FABRICATION RISK", "VERIFICATION NEED"),
    ("Digital humanities", "HISTORY + CS", "VISUALIZATION", "DATA ANALYSIS"),
    ("GIS", "MAP + DATE", "SOURCE + STORY", "HISTORICAL GIS"),
    ("3D heritage", "3D SCANNING", "VIRTUAL EXHIBIT", "FUTURE TECH"),
    ("Digital museums", "ONLINE EXHIBITION", "ACCESS + EDUCATION", "CONCEPTUAL"),
    ("Community archives", "FAMILY + VILLAGE", "PARTICIPATION", "SHARED CONTROL"),
    ("Family digital archive", "GATHER → DIGITIZE", "METADATA → BACKUP", "SHARE SELECTIVE"),
    ("Oral-history kit", "RECORDER + CONSENT", "QUESTIONS + METADATA", "TRANSCRIPT"),
    ("What to record", "STORIES + PHOTOS", "VOCAB + CRAFTS", "VILLAGE HISTORY"),
    ("Privacy", "PERSONAL DATA", "FAMILY DISPUTES", "ETHICAL CHOICE"),
    ("Children", "HEIGHTENED CARE", "CONSENT-BASED", "PRIVACY PROTECT"),
    ("Intellectual property", "COPYRIGHT", "OWNERSHIP", "LICENSING"),
    ("Access levels", "OPEN / LIMITED", "RESTRICTED / PRIVATE", "DECISION DATA"),
    ("Community control", "SENSITIVE DATA", "DESCRIPTION CHOICE", "DIGNITY"),
    ("Description bias", "COLONIAL TERMS", "CONTEXTUAL EXPLAIN", "NEUTRALITY NEED"),
    ("Proposed archive", "CONCEPTUAL FRAME", "12 CATEGORIES", "FUTURE VISION"),
    ("Searchable history", "INDEXED DATA", "DISCOVERABILITY", "EVALUATION NEED"),
    ("Education", "STUDENT ACCESS", "RESEARCH SUPPORT", "TEACHING TOOL"),
    ("Pashto preservation", "TEXT + VOICE", "DIALECT + TRANS", "LINGUISTIC LEGACY"),
    ("Future generations", "PAST EVIDENCE", "DIGITAL BRIDGE", "UNDERSTANDING"),
    ("What preservation cannot do", "NOT RECOVER ALL", "NOT PROVE ALL", "NOT REMOVE BIAS"),
    ("Memory vs proof", "REMEMBERED STORY", "VERIFIED EVIDENCE", "RESEARCH HISTORY"),
    ("Future archive", "AI INDEXING", "3D + GIS", "LINKED DATA"),
    ("Orakzai digital history", "FRAGMENT CONNECT", "HOME + ARCHIVE", "SHARED MEMORY"),
    ("Research gap", "DIALECTS + VILLAGE", "WOMEN / CHILDREN", "DOCUMENTATION"),
    ("Oral-history questions", "FAMILY PHOTOS", "ELDER STORIES", "FUTURE VISION"),
    ("Author reflection", "EVIDENCE + CONTEXT", "BRIDGE GENERATIONS", "UNDERSTANDING"),
    ("Final statement", "SOURCE + STORY", "CONTEXT", "DISCOVERY"),
    ("Family photograph", "IMAGE", "MEMORY", "RECORD"),
    ("Manuscript", "TEXT", "HISTORY", "PRIMARY"),
    ("Audio recording", "VOICE", "LANGUAGE", "SOUND"),
    ("Historical map", "PLACE", "BOUNDARY", "SPATIAL"),
    ("Archive box", "STORAGE", "PROTECTION", "COLLECTION"),
    ("Digital repository", "SERVER", "ACCESS", "SECURITY"),
    ("Preservation master", "HIGH QUALITY", "UNCOMPRESSED", "PERMANENT"),
    ("Access copy", "COMPRESSED", "USABLE", "DISTRIBUTION"),
    ("Metadata", "TITLE", "DATE", "CREATOR"),
    ("Provenance chain", "ORIGIN", "CUSTODY", "ARCHIVE"),
    ("Historical timeline", "EVENT", "DATE", "SEQUENCE"),
    ("Digital integrity", "FILE", "CHECKSUM", "VERIFIED"),
    ("Community archive", "LOCAL", "OWNERSHIP", "PARTICIPATION"),
    ("Future researcher", "SEARCH", "DISCOVER", "ANALYZE"),
    ("Intergenerational memory", "ELDER", "DIGITAL", "YOUTH"),
    ("Pashto archive", "LANGUAGE", "SCRIPT", "VOICE"),
    ("Documentary heritage", "RECORD", "MEMORY", "WORLD"),
    ("Digital exhibition", "VIRTUAL", "DISPLAY", "EDUCATION"),
    ("Responsible AI", "ASSIST", "REVIEW", "ETHICS"),
    ("Evidence chain", "SOURCE", "CONTEXT", "TRUTH"),
    ("Digital bridge", "PAST", "TECHNOLOGY", "FUTURE"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g105-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g105-{index}-title g105-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g105-{index}-title">{safe}</title><desc id="g105-{index}-desc">A three-stage conceptual relationship: {left}, {center}, and {right}. This is a preservation framework.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g105-{index}-caption" class="diagram-caption">{index}. {safe} — preservation framework.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Digital Preservation of History</title><desc id="hero-desc">An old family photograph transforming into a digital archive. Left: mountains, old photo, manuscript, elder. Center: scanner, metadata tags. Right: digital archive, cloud storage, young researcher, future generation.</desc><defs><linearGradient id="h105-bg" x1="0" x2="1"><stop stop-color="#123B2A"/><stop offset=".5" stop-color="#1B1B18"/><stop offset="1" stop-color="#202B35"/></linearGradient><linearGradient id="h105-path" x1="0" x2="1"><stop stop-color="#2E8B57"/><stop offset="1" stop-color="#B59654"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h105-bg)" stroke="#B59654" stroke-opacity=".55"/><path d="M24 286 L104 150 L152 210 L222 110 L320 286Z" fill="#0B241A" stroke="#2E8B57" stroke-opacity=".55"/><path d="M440 286 V226 H472 V286 H490 V180 H526 V286 H544 V142 H585 V286 H606 V198 H642 V286 H660 V160 H736 V386 H440Z" fill="#111B24" stroke="#7894A8" stroke-opacity=".62"/><path d="M176 330 C245 290 286 332 336 286 C382 244 428 262 485 294 C548 329 610 288 710 314" fill="none" stroke="url(#h105-path)" stroke-width="9" stroke-linecap="round"/><g transform="translate(100, 200)" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="12">MEMORY</text></g><g transform="translate(350, 150)" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="12">PRESERVATION</text></g><g transform="translate(600, 100)" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="12">FUTURE ACCESS</text></g><g font-family="Arial,sans-serif" text-anchor="middle"><text x="380" y="380" fill="#B59654" font-size="10" letter-spacing="1.3">MEMORY → DOCUMENT → DIGITIZE → DESCRIBE → PRESERVE → VERIFY → ACCESS → FUTURE</text></g></svg><figcaption id="hero-caption" class="diagram-caption">Digital Preservation: Connecting ancestral memory to future generations through evidence and context.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 105</title>
    <link rel="stylesheet" href="../styles/main.css">
    <style>
        :root {{ --gold: #B59654; --green: #2E8B57; --blue: #7894A8; --cream: #F5F0E6; --muted: rgba(245,240,230,.72); }}
        body {{ background: #070807; color: var(--cream); font-family: Georgia, serif; line-height: 1.72; }}
        .content-page {{ max-width: 1100px; margin: 0 auto; padding: 40px 6vw; }}
        .page-header {{ text-align: center; border-bottom: 1px solid var(--gold); padding-bottom: 20px; margin-bottom: 40px; }}
        .page-header h2 {{ color: var(--gold); font-size: 2.2rem; letter-spacing: 0.1rem; }}
        .section-label {{ color: var(--gold); font-weight: 700; letter-spacing: 0.15rem; text-transform: uppercase; font-size: 0.85rem; margin-top: 40px; }}
        .hero-diagram {{ margin: 40px auto; }}
        .atlas-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 30px; }}
        .opening-text {{ font-size: 1.15rem; font-style: italic; border-left: 3px solid var(--gold); padding-left: 20px; margin: 40px 0; }}
        .prose-section {{ margin-bottom: 40px; }}
        .data-table {{ width: 100%; border-collapse: collapse; margin: 30px 0; font-size: 0.85rem; }}
        .data-table th, .data-table td {{ border: 1px solid rgba(181,150,84,0.3); padding: 12px; text-align: left; }}
        .data-table th {{ background: rgba(181,150,84,0.1); color: var(--gold); }}
        .reflection-box {{ border: 1px solid var(--gold); padding: 30px; margin: 50px 0; background: rgba(181,150,84,0.05); }}
        .final-statement {{ text-align: center; font-size: 1.8rem; font-weight: 700; color: var(--gold); margin: 60px 0; }}
        @media (max-width: 768px) {{ .atlas-grid {{ grid-template-columns: 1fr; }} }}
        svg {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="content-page">
        <header class="page-header">
            <p class="section-label">PAGE 105</p>
            <h2>DIGITAL PRESERVATION OF HISTORY</h2>
            <p>“Preserve the evidence. Preserve the context. Preserve the memory.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “History can disappear without anyone deciding to destroy it. A photograph fades. A notebook is lost. A recording becomes unreadable. A family story dies with the person who remembered it. A document remains in a box until nobody knows what it contains. And sometimes an entire generation remembers an event differently because the original evidence was never preserved.<br><br>
                Digital technology offers a powerful opportunity. A photograph can be scanned. A voice can be recorded. A manuscript can be photographed. A map can be digitized. An oral history can be indexed. A family archive can be copied across generations.<br><br>
                But pressing ‘scan’ is not the same as preserving history. Preservation requires context, provenance, metadata, redundancy, care and responsible access. For Orakzai history, digital preservation can become a bridge between memory and future generations.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">What is Digital Preservation?</h3>
                <p>Digital preservation is the managed process of maintaining digital objects and their meaning over time so they remain accessible, authentic and usable. It is critical to distinguish between <strong>digitization</strong> (the act of creating a digital copy) and <strong>digital preservation</strong> (the long-term stewardship of that copy). A digital file without metadata, backups, and a plan for format migration is at high risk of being lost.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Historical Sources: Primary vs Secondary</h3>
                <p>Orakzai history exists across multiple formats, including family memory, oral histories, photographs, letters, land records, genealogies, manuscripts, and colonial documents. Digitization does not change a source's original status: a scanned colonial document remains a <strong>primary source</strong> from its period, while a modern article describing it is a <strong>secondary source</strong>. Sources have different evidentiary values and must be read critically.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digitization vs Preservation</h3>
                <table class="data-table">
                    <thead>
                        <tr><th>Feature</th><th>Digitization</th><th>Digital Preservation</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Goal</td><td>Create a digital representation</td><td>Maintain access and meaning over time</td></tr>
                        <tr><td>Process</td><td>Scanning / Recording</td><td>Active management / Redundancy</td></tr>
                        <tr><td>Metadata</td><td>Minimal or none</td><td>Comprehensive context and technical data</td></tr>
                        <tr><td>Sustainability</td><td>Short-term access</td><td>Long-term stewardship</td></tr>
                        <tr><td>Risk</td><td>High (Obsolescence / Loss)</td><td>Managed and mitigated</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Photograph Preservation Workflow</h3>
                <p>Family photographs are valuable visual memories. Preserving them requires careful handling of the original, high-quality capture (e.g., TIFF format for masters), comprehensive metadata (who, what, when, where), and a robust backup strategy. We do not automatically assume an unidentified person is a tribal leader without evidence; metadata should clearly state "unknown" when information is missing.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Oral History and Ethics</h3>
                <p>Oral history records lived experience and spoken memory. Digital preservation involves recording original voices, transcribing them, and potentially translating them for broader access. <strong>Informed consent</strong> is the ethical foundation: participants must understand the purpose, storage, and future use of their recordings. Privacy must be respected, especially regarding sensitive family data or children's records.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI and Cultural Authenticity</h3>
                <p>AI tools can assist in OCR, transcription, and image restoration, but they are not historical authorities. AI can hallucinate or misidentify people. A digitally restored image should always preserve the original file, and any generative changes must be clearly labeled. We do not present AI-generated reconstructions as original historical evidence. AI-generated text is not evidence of historical truth. We do not automatically assume AI output is correct. We do not claim that technology can independently preserve culture; evidence is limited regarding AI's ability to capture deep cultural context.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Preservation Claim Matrix</h3>
                <table class="data-table">
                    <thead>
                        <tr><th>Claim</th><th>Source Type</th><th>Evidence</th><th>Source</th><th>Confidence</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Digitization ≠ Preservation</td><td>International Standard</td><td>UNESCO/PERSIST Guidelines</td><td>UNESCO (2021)</td><td>High</td></tr>
                        <tr><td>3-2-1 Backup Rule</td><td>Technical Standard</td><td>Industry best practice</td><td>DPC (2025)</td><td>High</td></tr>
                        <tr><td>Oral History as Evidence</td><td>Methodology</td><td>CAP Project data</td><td>CAP (2023)</td><td>High</td></tr>
                        <tr><td>Metadata Necessity</td><td>Archival Standard</td><td>Dublin Core Initiative</td><td>IFLA (2021)</td><td>High</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Proposed Orakzai Digital Archive — Concept</h3>
                <p>While no formal "Orakzai Digital Archive" currently exists, a proposed conceptual framework would include categories for History, Photographs, Oral Histories, Documents, Maps, Pashto, Music, Poetry, Family Archives, Migration, Community Records, and Research Sources. This community-led archive would prioritize provenance, context, and responsible access levels (Open, Limited, Restricted, Private).</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Digital Preservation</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Research Gap: What Still Needs to be Documented</h3>
                <ul style="columns: 2;">
                    <li>Family photograph collections</li>
                    <li>Village histories</li>
                    <li>Oral histories (Elders)</li>
                    <li>Pashto dialect recordings</li>
                    <li>Historical maps</li>
                    <li>Manuscripts</li>
                    <li>Land records (where accessible)</li>
                    <li>Migration records</li>
                    <li>Community newspapers</li>
                    <li>Sports and festival records</li>
                    <li>Music and poetry recordings</li>
                    <li>Women's oral histories</li>
                    <li>Children's memories</li>
                    <li>Diaspora archives</li>
                    <li>Colonial and post-1947 records</li>
                    <li>Historical buildings</li>
                    <li>Traditional crafts</li>
                    <li>Agricultural knowledge</li>
                    <li>Place-name histories</li>
                    <li>Community preservation standards</li>
                </ul>
                <p style="margin-top: 20px;">“An archive becomes meaningful when evidence survives with enough context for another generation to understand what it is, where it came from, and why it matters.”</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Oral History Questions</h3>
                <ol style="columns: 2;">
                    <li>What is the oldest photograph in your family?</li>
                    <li>Who is in it? When and where was it taken?</li>
                    <li>What story does your family associate with it?</li>
                    <li>Which family documents should be preserved?</li>
                    <li>Which stories did your grandparents tell?</li>
                    <li>Which village places have changed?</li>
                    <li>Which Pashto words are disappearing?</li>
                    <li>Which historical objects does your family still have?</li>
                    <li>Which memories should be recorded privately?</li>
                    <li>What should children know about their family history?</li>
                    <li>Which records were lost through migration or conflict?</li>
                    <li>What historical material exists outside formal archives?</li>
                    <li>What should an Orakzai digital archive contain?</li>
                    <li>Who should control access to sensitive records?</li>
                    <li>What should future generations be able to find?</li>
                </ol>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“Every generation inherits more than stories. It inherits photographs, names, documents, voices, places, objects, and memories. Some survive by accident; others disappear quietly. I believe technology gives us an opportunity to be more deliberate. We can record the voice of an elder before it is lost. We can preserve a photograph before it fades. We can digitize a document before its pages become unreadable. We can connect a family memory with a historical source.<br><br>
                But preservation also requires humility. Not everything we remember is automatically proven. Not every photograph tells us everything we think it does. Not every digital reconstruction is history. The responsibility is therefore not simply to save more files. It is to save evidence with context. If we preserve the original, document its source, protect its integrity and explain what we know and what we do not know, then digital technology can become more than a storage system. It can become a bridge between generations. A bridge from memory to evidence. And from evidence to understanding.”</p>
            </div>

            <div class="final-statement">
                PRESERVE THE SOURCE. PRESERVE THE STORY. PRESERVE THE CONTEXT.<br>
                SO THE NEXT GENERATION CAN DISCOVER THE HISTORY FOR ITSELF.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>UNESCO, <em>UNESCO/PERSIST Guidelines for the Selection of Digital Heritage for Long-Term Preservation</em>, 2021.</li>
                    <li>Citizens Archive of Pakistan, "Preserving History: The Citizens Archive of Pakistan," <em>Oral History Society</em>, 2023.</li>
                    <li>Digital Preservation Coalition, <em>Digital Preservation Handbook</em>, 2025.</li>
                    <li>IFLA, <em>Dublin Core Metadata Initiative Standards</em>, 2021.</li>
                    <li>Boyd, D., "Oral History in the Digital Age," <em>OHDA</em>, 2012.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            105
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

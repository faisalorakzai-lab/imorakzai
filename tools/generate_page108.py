from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-108-building-a-digital-orakzai-archive.html'

GRAPHICS = [
    ("What is a digital archive?", "ORGANIZED SYSTEM", "PRESERVATION", "ACCESS"),
    ("Website vs archive", "ACCESS LAYER", "≠", "PRESERVATION LAYER"),
    ("Proposed Orakzai archive", "18 CATEGORIES", "CENTRAL SYSTEM", "PROPOSED"),
    ("Collection types", "GRID OF 15", "PHOTOS / DOCS", "ARCHIVE TYPES"),
    ("Photograph archive", "FAMILY / HISTORIC", "METADATA", "VISUAL RECORD"),
    ("Document archive", "LETTERS / LAND", "PROVENANCE", "TEXTUAL RECORD"),
    ("Map archive", "VILLAGE / MIGR", "HISTORICAL SCALE", "SPATIAL RECORD"),
    ("Pashto manuscript", "ORIGINAL SCRIPT", "TRANSCRIPT", "LITERARY RECORD"),
    ("Audio archive", "VOICE / MUSIC", "METADATA", "SONIC RECORD"),
    ("Video archive", "GESTURE / ENV", "CULTURAL PERF", "MOVING RECORD"),
    ("Newspaper archive", "CONTEMP EVIDENCE", "HEADLINE / DATE", "SERIAL RECORD"),
    ("Family archive", "VOLUNTARY", "DONATE / KEEP", "PRIVATE MEMORY"),
    ("Community archive", "LOCAL CONTROL", "ADVISORY BOARD", "PARTICIPATION"),
    ("Governance", "WHO OWNS?", "WHO ACCESSES?", "DECISION POWER"),
    ("Provenance", "SOURCE → CUSTODY", "DIGITIZE → ARCH", "ORIGIN TRACK"),
    ("Chain of custody", "SAMPLE WORKFLOW", "TRANSFER LOG", "INTEGRITY"),
    ("Authenticity", "ORIGINAL", "PROVENANCE", "CONFIDENCE"),
    ("Digital integrity", "FILE CHECK", "FIXITY", "NO CHANGE"),
    ("Checksums", "HASH ALGORITHM", "DETECT CHANGE", "FILE HEALTH"),
    ("File naming", "UNIQUE ID", "STABLE / MACHINE", "ORA_PHOTO_001"),
    ("Folder structure", "MASTERS / ACCESS", "METADATA", "STRUCTURE"),
    ("Master vs access", "PRESERVATION", "↓", "WEB DELIVERY"),
    ("Metadata", "DATA ABOUT DATA", "DISCOVERY", "MANAGEMENT"),
    ("Metadata minimum", "SCHEMA OF 16", "IDENTIFIER / TITLE", "PROPOSED"),
    ("Controlled vocabulary", "CONSISTENT TERM", "SEARCHABLE", "TAXONOMY"),
    ("Place names", "ORIGINAL / ALT", "HISTORIC / MOD", "TOPONYMY"),
    ("Person names", "SPELLING / REL", "SOURCE / CONF", "ONOMASITCS"),
    ("Dates", "EXACT / APPROX", "RANGE / UNKNOWN", "TEMPORAL"),
    ("Geographic data", "COORDINATES", "PRIVACY RISK", "SPATIAL DATA"),
    ("Rights", "COPYRIGHT / PRIV", "OWNERSHIP ≠ ACC", "STAKEHOLDERS"),
    ("Access levels", "OPEN / LIMITED", "RESTRICTED", "5 LEVELS"),
    ("Takedown/correction", "REPORT → REVIEW", "DECISION", "ACCOUNTABLE"),
    ("Community review", "ARCHIVE ↔ COMM", "IDENTIFY / CONT", "PARTNERSHIP"),
    ("Crowdsourcing", "USER-SUBMITTED", "REVIEW NEEDED", "CONTRIBUTION"),
    ("Evidence levels", "LEVEL A → E", "PRIMARY → UNVER", "CLASSIFICATION"),
    ("Fact vs memory", "DOCUMENTED FACT", "ORAL TESTIMONY", "DISTINCTION"),
    ("Search", "KEYWORD / PLACE", "DATE / TOPIC", "DISCOVERY"),
    ("Proposed search", "INTERFACE MOCK", "FILTERS", "DISCOVERY TOOL"),
    ("Map archive", "MAP → PLACE", "DOCS / PHOTOS", "SPATIAL LINK"),
    ("Timeline", "COLONIAL → MOD", "MERGER", "CHRONOLOGY"),
    ("Collections vs subjects", "PROVENANCE", "↔", "TOPIC SEARCH"),
    ("Digital preservation", "FIXITY / MONITOR", "MIGRATION", "CONTINUITY"),
    ("Format obsolescence", "RISK MONITOR", "MIGRATE", "FUTURE ACCESS"),
    ("Backup", "3 COPIES", "2 MEDIA TYPES", "1 OFFSITE"),
    ("Cloud storage", "PROVIDER RISK", "RESILIENCE", "SUPPLEMENTAL"),
    ("Open-source tools", "SUSTAINABILITY", "METADATA", "IMPLEMENTATION"),
    ("Security", "AUTH / ENCRYPT", "LOGGING", "PROTECTION"),
    ("Cybersecurity", "RANSOMWARE", "RESILIENCE", "MONITORING"),
    ("Personal data", "PRIVACY REVIEW", "RESTRICTION", "DIGNITY"),
    ("Children's records", "SAFEGUARDING", "CONSENT", "PROTECTION"),
    ("Religious material", "CONTEXT / RESP", "SENSITIVITY", "HANDLING"),
    ("Genealogy", "SOURCE / DATE", "PROVENANCE", "NOT FACT ALONE"),
    ("Music archive", "PERFORMER / GEN", "RIGHTS", "SONIC HERITAGE"),
    ("Food archive", "RECIPE / PHOTO", "SCOPE", "CULINARY MEM"),
    ("Clothing archive", "GARMENT / STORY", "NOT UNIVERSAL", "TEXTILE MEM"),
    ("Hospitality archive", "HUJRA / CUSTOM", "SCOPE", "SOCIAL MEM"),
    ("Festival archive", "POSTER / PHOTO", "TRADITION", "EVENT MEM"),
    ("Migration archive", "DOCS / LETTERS", "DIASPORA", "JOURNEY MEM"),
    ("Urban archive", "CITY LIFE", "NETWORKS", "URBAN MEM"),
    ("Diaspora archive", "GULF / UK / US", "GLOBAL SCOPE", "TRANSNATIONAL"),
    ("Language archive", "AUDIO / TEXT", "DICT / PROV", "LINGUISTIC"),
    ("AI archive", "ASSISTANT", "OCR / TRANS", "NOT AUTHORITY"),
    ("AI OCR", "PERSO-ARABIC", "HANDWRITING", "LIMITATIONS"),
    ("AI image description", "SUGGESTION", "MISIDENTIFY", "REVIEW NEED"),
    ("AI search", "SEMANTIC", "SOURCE LINK", "DISCOVERY"),
    ("AI fabrication", "NO FAKE RECORDS", "NO FAKE GEN", "WARNING"),
    ("Digital reconstruction", "LABELED INTERP", "NOT EVIDENCE", "VISUALIZATION"),
    ("Transparency", "SOURCE / RIGHTS", "CONFIDENCE", "ACCOUNTABILITY"),
    ("Archival citation", "PROPOSED FORMAT", "ID / TITLE", "REFERENCE"),
    ("Persistent ID", "ARK / DOI / HAN", "STABLE", "IDENTIFIER"),
    ("Interoperability", "STANDARD", "↔", "IMPLEMENTATION"),
    ("IIIF", "IMAGE VIEW", "ZOOM / COMP", "INTEROP"),
    ("Dublin Core", "15 ELEMENTS", "DISCOVERY", "SCHEMA"),
    ("OAI-PMH", "HARVESTING", "METADATA", "REPOSITORY"),
    ("Archive website", "NAVIGATION MOCK", "COLLECTIONS", "INTERFACE"),
    ("Item page", "METADATA FIELDS", "RELATED ITEMS", "GRANULAR"),
    ("Collection page", "SCOPE / PROV", "ITEM COUNT", "CONTEXTUAL"),
    ("Researcher workspace", "SAVED SEARCH", "ANNOTATION", "PROPOSED"),
    ("Public education", "SCHOOL / UNIV", "JOURNALIST", "OUTREACH"),
    ("Archive and schools", "LOCAL HISTORY", "ID PROJECT", "LEARNING"),
    ("Archive and universities", "ETHNOGRAPHY", "DH RESEARCH", "SCHOLARSHIP"),
    ("Archive and journalists", "VERIFICATION", "TIMELINE", "CITATION"),
    ("Archive and families", "GENEALOGY", "MIGRATION", "PRIVATE MEM"),
    ("Future generations", "2026 → 2100", "BRIDGE", "LEGACY"),
    ("Funding", "GRANTS / PHIL", "COMMUNITY", "SUSTAINABILITY"),
    ("Institutional partners", "LIB / UNIV / MUS", "PARTNERSHIP", "CUSTODY"),
    ("Volunteers", "SCAN / TRANS", "TRAINING", "QC NEEDED"),
    ("Archivists", "APPRAISAL", "PRESERVATION", "SKILLS"),
    ("Historians", "CONTEXT", "CORROBORATION", "INTERPRETATION"),
    ("Linguists", "PASHTO TRANS", "DIALECT", "PRESERVATION"),
    ("Technologists", "STORAGE / SEC", "APIS", "INFRASTRUCTURE"),
    ("Multidisciplinary", "HIST / LANG / TECH", "ARCHIVE", "COLLABORATION"),
    ("Community governance", "STEWARDSHIP", "REPRESENTATION", "PROPOSED"),
    ("Ethical principles", "TRUTH / CONSENT", "PRIVACY", "ACCOUNTABLE"),
    ("Restricted material", "PRIVATE / SENS", "CHILDREN", "PROTECTION"),
    ("Open material", "PUBLIC DOMAIN", "LICENSED", "ACCESS"),
    ("Quality scorecard", "8 DIMENSIONS", "AUTHENTICITY", "EVALUATION"),
    ("Archive maturity", "LEVEL 1 → 6", "FILE → GOVERN", "PROPOSED"),
    ("Building roadmap", "PHASE 1 → 8", "DISCO → SUSTAIN", "PROPOSED"),
    ("Discovery", "IDENTIFY COLL", "PARTNERS", "PHASE 1"),
    ("Pilot", "ILLUSTRATIVE", "100 PHOTOS", "PHASE 2"),
    ("Description", "METADATA", "PROVENANCE", "PHASE 3"),
    ("Preservation phase", "MASTERS", "BACKUPS", "PHASE 4"),
    ("Search phase", "KEYWORD", "FILTERS", "PHASE 5"),
    ("Public access", "LAUNCH", "RIGHTS CHECK", "PHASE 6"),
    ("Governance phase", "REVIEW", "CORRECTION", "PHASE 7"),
    ("Sustainability", "FUNDING", "SUCCESSION", "PHASE 8"),
    ("Research gap", "WHAT STILL NEEDED", "PASHTO TOOLS", "FUTURE"),
    ("Archive questions", "FAMILY / COMM", "GOVERNANCE", "INQUIRY"),
    ("Author reflection", "BRIDGE", "HUMILITY", "UNDERSTANDING"),
    ("Final statement", "BRIDGE TO FUTURE", "NOT WAREHOUSE", "LEGACY"),
    ("Digital vault", "SECURITY", "ENCRYPT", "STORAGE"),
    ("Archive network", "FAMILY", "COMMUNITY", "INSTITUTION"),
    ("Metadata graph", "ENTITY", "RELATION", "LINKED DATA"),
    ("Evidence graph", "CLAIM", "SOURCE", "CONFIDENCE"),
    ("Family-to-archive", "DONATE", "DIGITIZE", "PRESERVE"),
    ("Voice-to-archive", "VOICE", "RECORD", "PRESERVE"),
    ("Photo-to-archive", "PHOTO", "ID", "PRESERVE"),
    ("Future archive bridge", "PAST", "PRESENT", "FUTURE"),
    ("Evidence chain", "SOURCE", "CONTEXT", "UNDERSTANDING"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g108-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g108-{index}-title g108-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g108-{index}-title">{safe}</title><desc id="g108-{index}-desc">A three-stage conceptual relationship: {left}, {center}, and {right}. This is an archival framework.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g108-{index}-caption" class="diagram-caption">{index}. {safe} — archival framework.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Building a Digital Orakzai Archive</title><desc id="hero-desc">A central digital archive vault surrounded by icons representing photographs, documents, Pashto manuscripts, audio, video, maps, and metadata tags against a subtle Orakzai mountain backdrop.</desc><defs><linearGradient id="h108-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient><linearGradient id="h108-vault" x1="0" x2="1"><stop stop-color="#B59654"/><stop offset="1" stop-color="#8A6D3B"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h108-bg)" stroke="#B59654" stroke-opacity=".55"/><path d="M20 380 L120 280 L220 340 L350 220 L480 380Z" fill="#0B241A" fill-opacity=".3" stroke="#2E8B57" stroke-opacity=".4"/><g transform="translate(380, 215)"><rect x="-60" y="-80" width="120" height="160" rx="10" fill="url(#h108-vault)" stroke="#F5F0E6" stroke-width="2"/><circle cx="0" cy="0" r="25" fill="none" stroke="#0E1110" stroke-width="3"/><line x1="0" y1="-25" x2="0" y2="25" stroke="#0E1110" stroke-width="2"/><line x1="-25" y1="0" x2="25" y2="0" stroke="#0E1110" stroke-width="2"/><text x="0" y="55" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#0E1110">ARCHIVE</text></g><g font-family="Arial,sans-serif" font-size="10" fill="#B59654" stroke="none"><text x="180" y="100">PHOTOGRAPHS</text><text x="580" y="100">DOCUMENTS</text><text x="120" y="200">PASHTO MS</text><text x="640" y="200">AUDIO</text><text x="180" y="320">VIDEO</text><text x="580" y="320">MAPS</text><text x="380" y="80" text-anchor="middle">METADATA</text></g><path d="M250 100 Q 300 150 330 180" fill="none" stroke="#B59654" stroke-opacity=".4" stroke-dasharray="4 2"/><path d="M520 100 Q 460 150 430 180" fill="none" stroke="#B59654" stroke-opacity=".4" stroke-dasharray="4 2"/><path x="380" y="100" d="M380 100 V 135" stroke="#B59654" stroke-opacity=".4" stroke-dasharray="4 2"/><g font-family="Arial,sans-serif" text-anchor="middle"><text x="380" y="400" fill="#B59654" font-size="11" letter-spacing="1.5">DISCOVER → COLLECT → DOCUMENT → PRESERVE → GOVERN → SHARE</text></g></svg><figcaption id="hero-caption" class="diagram-caption">Building a Digital Orakzai Archive: Preserving memory requires structure, context and trust.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 108</title>
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
            <p class="section-label">PAGE 108</p>
            <h2>BUILDING A DIGITAL ORAKZAI ARCHIVE</h2>
            <p>“Preserving memory requires more than storage. It requires structure, context and trust.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “An archive begins with a simple decision: Do not let the record disappear. A photograph without a name can become anonymous. A document without context can become difficult to understand. A recording without metadata can become almost impossible to search. A family story without preservation may disappear with the person who remembered it.<br><br>
                Digitization creates an opportunity. It allows fragile photographs, documents, recordings, maps and memories to be copied, described, preserved and connected. But a digital archive is more than a folder full of files. It needs structure. It needs metadata. It needs preservation. It needs verification. It needs access rules. It needs people who care for it. And most importantly, it needs trust.<br><br>
                For Orakzai history, the goal should not simply be to collect as much material as possible. The goal should be to build a record that future generations can understand, question, research and continue.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">What is a Digital Archive?</h3>
                <p>A digital archive is an organized system for preserving, describing, managing and providing appropriate access to digital or digitized records. It is distinct from a digital library, database, or social media page because it requires a long-term preservation strategy, comprehensive metadata, and strict governance. We follow the <strong>3-2-1 Backup Strategy</strong> (3 copies, 2 media types, 1 offsite) to ensure digital resilience.</p>
                <p><strong>Digital Archive Components:</strong> FILES + METADATA + PRESERVATION + GOVERNANCE + ACCESS</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Proposed Orakzai Digital Archive — Architecture</h3>
                <p>The following categories represent a proposed structure for a comprehensive Orakzai archive. <strong>PROPOSED ARCHITECTURE — NOT A CLAIM THAT ALL CATEGORIES CURRENTLY EXIST IN A SINGLE ORAKZAI ARCHIVE.</strong></p>
                <ul style="columns: 2;">
                    <li>HISTORY</li>
                    <li>ORAL HISTORY</li>
                    <li>PHOTOGRAPHS</li>
                    <li>DOCUMENTS</li>
                    <li>MAPS</li>
                    <li>LANGUAGE</li>
                    <li>MUSIC</li>
                    <li>POETRY</li>
                    <li>PROVERBS</li>
                    <li>FOOD</li>
                    <li>CLOTHING</li>
                    <li>HOSPITALITY</li>
                    <li>FAMILY RECORDS</li>
                    <li>GENEALOGIES</li>
                    <li>MIGRATION</li>
                    <li>DIASPORA</li>
                    <li>EDUCATION</li>
                    <li>RELIGIOUS LIFE</li>
                    <li>MARKETS</li>
                    <li>AGRICULTURE</li>
                </ul>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Archival Recommendation Matrix</h3>
                <table class="data-table">
                    <thead>
                        <tr><th>Recommendation</th><th>Classification</th><th>Standard / Best Practice</th><th>Source</th><th>Confidence</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>3-2-1 Backup Strategy</td><td>Preservation</td><td>Best Practice</td><td>DPC (2025)</td><td>High</td></tr>
                        <tr><td>Dublin Core Metadata</td><td>Description</td><td>Archival Standard</td><td>OAI-PMH Guidelines</td><td>High</td></tr>
                        <tr><td>Community Governance</td><td>Governance</td><td>Proposed Model</td><td>Mukurtu / CLOCKSS</td><td>High</td></tr>
                        <tr><td>IIIF Interoperability</td><td>Access</td><td>Archival Standard</td><td>IIIF Consortium</td><td>High</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Provenance and Authenticity</h3>
                <p>Provenance means documenting where material came from and its relationship to its creator, owner or previous custodian. A useful archive documents the <strong>Chain of Custody</strong> (Source → Custody → Digitization → Archive). We do not claim provenance is complete when records are uncertain. Digital integrity is maintained through <strong>Checksums</strong> and fixity checks, though these do not prove historical authenticity by themselves.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI and Archival Management</h3>
                <p>AI may assist with OCR, speech-to-text, and metadata suggestions, but it should never manufacture missing archive records. AI-generated metadata must be labelled as machine-generated until reviewed. We do not automatically assume AI output is correct. AI-generated text is not evidence of historical truth. Human review is the final authority to ensure authenticity and prevent the fabrication of history. We do not claim that technology can independently preserve culture; evidence is limited regarding AI's ability to capture deep cultural context.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Building a Digital Archive</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Archive Maturity Model</h3>
                <p><strong>PROPOSED MATURITY MODEL:</strong></p>
                <ul>
                    <li>LEVEL 1 — FILE COLLECTION</li>
                    <li>LEVEL 2 — ORGANIZED COLLECTION</li>
                    <li>LEVEL 3 — METADATA ARCHIVE</li>
                    <li>LEVEL 4 — PRESERVED REPOSITORY</li>
                    <li>LEVEL 5 — INTEROPERABLE DIGITAL ARCHIVE</li>
                    <li>LEVEL 6 — COMMUNITY-GOVERNED ARCHIVE</li>
                </ul>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Building Roadmap</h3>
                <ol>
                    <li>PHASE 1 — DISCOVERY: Identify existing collections and partners.</li>
                    <li>PHASE 2 — PILOT: Manage a small illustrative project-scoping example (e.g., 100 photos).</li>
                    <li>PHASE 3 — DESCRIPTION: Create metadata and document provenance.</li>
                    <li>PHASE 4 — PRESERVATION: Create masters, access copies, and backups.</li>
                    <li>PHASE 5 — SEARCH: Add keyword, place, and date indexing.</li>
                    <li>PHASE 6 — PUBLIC ACCESS: Launch material with clear rights status.</li>
                    <li>PHASE 7 — COMMUNITY GOVERNANCE: Create review and correction mechanisms.</li>
                    <li>PHASE 8 — SUSTAINABILITY: Plan long-term funding and succession.</li>
                </ol>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Archive Questions</h3>
                <ol style="columns: 2;">
                    <li>What historical materials already exist in your family?</li>
                    <li>Who owns them?</li>
                    <li>Where are they stored?</li>
                    <li>Are old photographs identified?</li>
                    <li>Are old recordings still playable?</li>
                    <li>Which documents require preservation?</li>
                    <li>Which family stories remain undocumented?</li>
                    <li>Which village histories need recording?</li>
                    <li>Which Pashto materials need digitization?</li>
                    <li>Which materials should remain private?</li>
                </ol>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“I have come to understand that preservation is not simply about saving the past. It is about creating a bridge between generations. A photograph may show a face, but an archive can help identify the person. A document may record a decision, but metadata can explain where it came from. A recording may preserve a voice, but a transcript can make that voice searchable. A map may show a place, but connected oral histories can reveal what that place meant to the people who lived there.<br><br>
                That is why I believe an Orakzai digital archive should be built with both technology and humility. Technology can store enormous amounts of information. It cannot decide what a memory means. It cannot determine whether a story is true simply because it is repeated. It cannot replace the people whose lives created the record.<br><br>
                The archive of the future should therefore be more than a database. It should be a carefully governed memory system — one that preserves evidence, respects people, records uncertainty and gives future generations the tools to ask better questions. If we build it responsibly, the archive will not merely preserve where we came from. It will help future generations understand who we became.”</p>
            </div>

            <div class="final-statement">
                AN ARCHIVE IS NOT A WAREHOUSE FOR THE PAST.<br>
                IT IS A BRIDGE TO THE FUTURE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Digital Preservation Coalition (DPC), <em>Digital Preservation Handbook</em>, 2025.</li>
                    <li>UNESCO, <em>Guidelines for the Selection of Digital Heritage for Long-Term Preservation</em>, 2024.</li>
                    <li>UI Libraries / Mukurtu, <em>The Ethics of Open Access Digital Archives</em>, 2018.</li>
                    <li>Library of Congress, <em>Sustainability of Digital Formats</em>, 2024.</li>
                    <li>National Archives (NARA), <em>Technical Guidelines for Digitizing Archival Materials</em>, 2023.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            108
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

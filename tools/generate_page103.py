from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-103-preserving-culture-digital-world.html'

GRAPHICS = [
    ("What is cultural preservation?", "LANGUAGE + MEMORY", "STORIES + PRACTICE", "TRANSMITTED IDENTITY"),
    ("Intangible cultural heritage", "ORAL TRADITIONS", "SOCIAL PRACTICES", "CRAFT KNOWLEDGE"),
    ("What should be documented?", "VOICE + TEXT", "IMAGE + VIDEO", "PLACE + MEMORY"),
    ("Oral history", "VOICE", "EXPERIENCE", "DOCUMENTED MEMORY"),
    ("Oral-history workflow", "CONSENT → RECORD", "IDENTIFY → TRANSCRIBE", "STORE → PRESERVE"),
    ("Consent", "INFORMED", "VOLUNTARY", "DOCUMENTED PERMISSION"),
    ("Family archive", "PHOTOS + LETTERS", "DOCUMENTS", "FAMILY MEMORY"),
    ("Photograph metadata", "NAME + DATE", "PLACE + EVENT", "HISTORICAL RECORD"),
    ("Photo preservation", "MASTER FILE", "ACCESS COPY", "METADATA + BACKUP"),
    ("Audio preservation", "VOICE + SONG", "PRONUNCIATION", "PRISTINE RECORD"),
    ("Video preservation", "DANCE + CRAFT", "FESTIVAL", "VISUAL CONTEXT"),
    ("Pashto preservation", "SPEAK → RECORD", "TRANSCRIBE → TEACH", "LIVING LANGUAGE"),
    ("Local vocabulary", "WORD + MEANING", "PRONUNCIATION", "LOCAL CONTEXT"),
    ("Proverbs", "PASHTO TEXT", "MEANING + CONTEXT", "CULTURAL WISDOM"),
    ("Music", "RECORDING", "PERFORMER + INSTRUMENT", "TRADITIONAL SOUND"),
    ("Attan", "MOVEMENT", "MUSIC + RHYTHM", "REGIONAL VARIATION"),
    ("Food knowledge", "RECIPE + METHOD", "INGREDIENTS", "FAMILY TRADITION"),
    ("Crafts", "OBJECT + MAKER", "METHOD + MATERIALS", "MATERIAL CULTURE"),
    ("Places", "VILLAGE + VALLEY", "HISTORIC SITES", "LANDSCAPE MEMORY"),
    ("Digital maps", "PLACE-NAMES", "HISTORICAL LAYERS", "SPATIAL HERITAGE"),
    ("Genealogy", "FAMILY TREE", "ORAL HISTORY", "IDENTITY RECORD"),
    ("Documents", "SCAN → METADATA", "CATALOGUE", "SEARCHABLE ARCHIVE"),
    ("OCR", "DOCUMENT → SCAN", "OCR → REVIEW", "SEARCHABLE TEXT"),
    ("Translation", "ORIGINAL TEXT", "TRANSLATION", "CROSS-CULTURAL ACCESS"),
    ("Metadata", "TITLE + CREATOR", "DATE + LOCATION", "CONTEXT FOR MEMORY"),
    ("Archive record", "TITLE + TYPE", "SOURCE + RIGHTS", "IDENTIFIER"),
    ("File organization", "NAMING CONVENTION", "FOLDER STRUCTURE", "DISCOVERABILITY"),
    ("Backups", "LOCAL COPY", "OFFSITE COPY", "INTEGRITY CHECK"),
    ("Checksums", "FILE HASH", "VERIFICATION", "DATA INTEGRITY"),
    ("Cloud storage", "ACCESS", "STORAGE", "NOT PRESERVATION"),
    ("Social media", "VISIBILITY", "DISTRIBUTION", "NOT AN ARCHIVE"),
    ("Digital death", "ACCOUNT LOST", "PASSWORD LOST", "CONTENT GONE"),
    ("Website preservation", "DOMAIN + SOURCE", "DATABASE + MEDIA", "LONG-TERM ACCESS"),
    ("Open/restricted access", "OPEN / LIMITED", "RESTRICTED / PRIVATE", "CONTROLLED ACCESS"),
    ("Copyright", "OWNERSHIP", "RIGHTS STATUS", "LEGAL CLARITY"),
    ("Community ownership", "COMMUNITY", "DOCUMENTS", "COMMUNITY CONTROL"),
    ("Stakeholders", "FAMILIES + ELDERS", "RESEARCHERS", "FUTURE GENERATIONS"),
    ("Ethical archiving", "CONSENT + CONTEXT", "PRIVACY + ACCURACY", "ACCOUNTABILITY"),
    ("Sensitive knowledge", "PRIVATE HISTORY", "SACRED PRACTICE", "RESTRICTED ACCESS"),
    ("Children", "NAME + FACE", "PRIVACY PROTECTION", "CONSENT-BASED"),
    ("Women's histories", "VOICE + EXPERIENCE", "RESPECT + PRIVACY", "DIVERSE STORIES"),
    ("Elders", "VOICE → RECORD", "TRANSCRIPT", "NEXT GENERATION"),
    ("Youth", "TECHNOLOGY", "RECORDING + SCANNING", "DIGITAL STEWARDS"),
    ("Schools", "LOCAL PROJECTS", "PASHTO LANGUAGE", "FAMILY HISTORY"),
    ("Universities", "DIGITAL HUMANITIES", "RESEARCH ARCHIVES", "SCHOLARLY ACCESS"),
    ("Museums", "CONSERVATION", "EXHIBITIONS", "PUBLIC EDUCATION"),
    ("Orakzai Digital Archive", "PROPOSED FRAMEWORK", "COMMUNITY-CENTERED", "FUTURE VISION"),
    ("Archive architecture", "COLLECT → DESCRIBE", "VERIFY → STORE", "SHARE RESPONSIBLY"),
    ("Digital storytelling", "PODCAST + VIDEO", "PHOTO ESSAY", "CONTEXTUAL NARRATIVE"),
    ("Social media risks", "MISINFORMATION", "DECONTEXTUALIZATION", "DISAPPEARANCE"),
    ("AI preservation", "OCR + TRANSLATION", "TRANSCRIPTION", "ARCHIVE ASSISTANCE"),
    ("AI restoration", "IMAGE ENHANCEMENT", "AUDIO CLEANUP", "EVIDENCE CAUTION"),
    ("Deepfakes", "FABRICATED VOICE", "FAKE PHOTO", "SYNTHETIC HISTORY"),
    ("Authenticity", "WHO + WHEN", "WHERE + SOURCE", "VERIFIED RECORD"),
    ("Fact checking", "MEMORY + DOCUMENT", "ACADEMIC SOURCE", "CROSS-CHECKED"),
    ("Misinformation", "UNSOURCED CLAIMS", "MISLABELLED PHOTOS", "FABRICATED HISTORY"),
    ("Searchability", "METADATA", "DISCOVERY", "BETTER RESEARCH"),
    ("Language preservation", "RECORDED SPEECH", "DICTIONARIES", "SEARCHABLE CORPORA"),
    ("Diaspora", "HOMELAND", "OVERSEAS", "DIGITAL CONNECTION"),
    ("Future generations", "TODAY → DOCUMENT", "2036 → 2076", "LONG-TERM LEGACY"),
    ("What should not be digitized?", "PRIVATE FAMILY", "RESTRICTED SACRED", "COMMUNITY CHOICE"),
    ("Preservation priority", "URGENCY", "SENSITIVITY", "PRIORITY ASSESSMENT"),
    ("Workflow", "IDENTIFY → CONSENT", "DIGITIZE → VERIFY", "PRESERVE → SHARE"),
    ("Five rules", "PRESERVE ORIGINAL", "RECORD CONTEXT", "GET CONSENT"),
    ("Research gap", "ORAL HISTORIES", "VILLAGE ARCHIVES", "PASHTO RECORDINGS"),
    ("Oral-history questions", "FAMILY PHOTOS?", "ELDER STORIES?", "PASHTO WORDS?"),
    ("Author reflection", "SAVING MEANING", "SAVING VOICES", "SAVING FUTURE"),
    ("Final statement", "PRESERVE RECORD", "PROTECT CONTEXT", "PASS MEMORY"),
    ("Memory", "LIVED EXPERIENCE", "INDIVIDUAL STORY", "CULTURAL MEMORY"),
    ("Documentation", "FACT + CONTEXT", "SOURCE + DATE", "VERIFIED RECORD"),
    ("Digitization", "SCAN + RECORD", "FILE + FORMAT", "DIGITAL ACCESS"),
    ("Context", "WHO + WHY", "WHERE + WHEN", "MEANINGFUL RECORD"),
    ("Community consent", "PERMISSION", "ETHICAL CHOICE", "COMMUNITY DIGNITY"),
    ("Digital archive", "SECURE STORAGE", "METADATA", "LONG-TERM STEWARDSHIP"),
    ("Cultural transmission", "ELDER TO YOUTH", "STORY TO RECORD", "PAST TO FUTURE"),
    ("Original vs restored", "MASTER FILE", "CLEANED COPY", "EVIDENCE INTEGRITY"),
    ("Human review", "AI ASSISTANCE", "HUMAN VERIFICATION", "ACCURATE ARCHIVE"),
    ("Digital continuity", "FORMAT MIGRATION", "BACKUP", "PERMANENT ACCESS"),
    ("Future archive", "MEMORY", "TECHNOLOGY", "RESPONSIBILITY"),
    ("Digital legacy", "DOCUMENT", "PRESERVE", "PASS FORWARD"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g103-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g103-{index}-title g103-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g103-{index}-title">{safe}</title><desc id="g103-{index}-desc">A three-stage conceptual relationship: {left}, {center}, and {right}. This is a preservation framework.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g103-{index}-caption" class="diagram-caption">{index}. {safe} — preservation framework.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Preserving Culture in a Digital World</title><desc id="hero-desc">An Orakzai mountain landscape connected to a digital archive. Left: mountains, village, elder, family, old photograph, handwritten document. Center: scanner, microphone, camera, archive box. Right: cloud archive, digital library, smartphone, laptop, future generation.</desc><defs><linearGradient id="h103-bg" x1="0" x2="1"><stop stop-color="#123B2A"/><stop offset=".5" stop-color="#1B1B18"/><stop offset="1" stop-color="#202B35"/></linearGradient><linearGradient id="h103-path" x1="0" x2="1"><stop stop-color="#2E8B57"/><stop offset="1" stop-color="#B59654"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h103-bg)" stroke="#B59654" stroke-opacity=".55"/><path d="M24 286 L104 150 L152 210 L222 110 L320 286Z" fill="#0B241A" stroke="#2E8B57" stroke-opacity=".55"/><path d="M24 286 H320 V386 H24Z" fill="#0A1B15"/><path d="M440 286 V226 H472 V286 H490 V180 H526 V286 H544 V142 H585 V286 H606 V198 H642 V286 H660 V160 H736 V386 H440Z" fill="#111B24" stroke="#7894A8" stroke-opacity=".62"/><path d="M176 330 C245 290 286 332 336 286 C382 244 428 262 485 294 C548 329 610 288 710 314" fill="none" stroke="url(#h103-path)" stroke-width="9" stroke-linecap="round"/><g transform="translate(320, 200)"><rect x="0" y="0" width="120" height="80" rx="5" fill="#3C3020" stroke="#B59654"/><circle cx="30" cy="40" r="10" fill="#B59654"/><path d="M60 40 H100" stroke="#B59654" stroke-width="2"/><text x="60" y="70" fill="#F5F0E6" font-size="8">DOCUMENTATION</text></g><g transform="translate(480, 50)"><path d="M0 40 Q20 0 40 40 Q60 0 80 40 Q100 0 120 40 V60 H0 Z" fill="#202B35" stroke="#7894A8"/><text x="60" y="55" text-anchor="middle" fill="#F5F0E6" font-size="10">CLOUD ARCHIVE</text></g><g font-family="Arial,sans-serif" text-anchor="middle"><text x="158" y="344" fill="#2E8B57" font-size="13" font-weight="700">MEMORY / ROOTS</text><text x="600" y="344" fill="#7894A8" font-size="13" font-weight="700">FUTURE / ACCESS</text><text x="380" y="380" fill="#B59654" font-size="10" letter-spacing="1.3">MEMORY → RECORD → ARCHIVE → VERIFY → SHARE → PRESERVE</text></g></svg><figcaption id="hero-caption" class="diagram-caption">Memory becomes stronger when it is documented with care. The digital world connects ancestral roots to future access.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 103</title>
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
        .final-statement {{ text-align: center; font-size: 2rem; font-weight: 700; color: var(--gold); margin: 60px 0; }}
        @media (max-width: 768px) {{ .atlas-grid {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <div class="content-page">
        <header class="page-header">
            <p class="section-label">PAGE 103</p>
            <h2>PRESERVING CULTURE IN A DIGITAL WORLD</h2>
            <p>“Memory becomes stronger when it is documented with care.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “A culture can disappear without a single person deciding to erase it.<br><br>
                A story may simply stop being told. A word may no longer be taught. A photograph may lose the name of the people in it. A song may survive only in the memory of one person. A family recording may remain on a phone until the phone is lost. An old document may exist in a home but never be catalogued.<br><br>
                Digital technology changes this possibility. For the first time, families and communities can record voices, photographs, documents, stories, music and memories at a scale that earlier generations could not easily achieve.<br><br>
                But technology alone cannot preserve culture. Preservation requires people who know what a record means, where it came from, who created it, and why it matters.<br><br>
                The goal is not simply to put Orakzai culture online. The goal is to make cultural memory discoverable, understandable, authentic, secure and available to future generations.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">What does cultural preservation mean?</h3>
                <p>Cultural preservation includes language, oral history, family photographs, letters, documents, genealogies, poetry, music, food knowledge, craft knowledge, stories, proverbs, festivals, religious history, architecture, landscape knowledge, traditional ecological knowledge, and community memories. However, not every item should be publicly published. We do not claim that every cultural practice is suitable for open access. Some knowledge may be private, sacred, family-specific, sensitive, restricted, or context-dependent.</p>
                <div class="logic-diagram mini-diagram" style="max-width: 400px; margin: 20px auto;">
                    <svg viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg">
                        <rect width="400" height="100" rx="10" fill="#0E1110" stroke="#B59654"/>
                        <text x="200" y="40" text-anchor="middle" fill="#B59654" font-size="16" font-weight="700">PRESERVE ≠ PUBLISH EVERYTHING</text>
                        <text x="200" y="70" text-anchor="middle" fill="#F5F0E6" font-size="12">Respect Privacy, Consent, and Sacredness</text>
                    </svg>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Intangible Cultural Heritage</h3>
                <p>Intangible cultural heritage (ICH) includes oral traditions, performing arts, social practices, rituals, festive events, knowledge concerning nature, and traditional craftsmanship. Connecting to Pages 59–70, it is vital to distinguish between documented culture and formally recognized UNESCO heritage. We do not automatically classify every Orakzai practice as UNESCO-recognized. Evidence is limited for many regional practices, but all are worth documenting.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Oral History: The Method of Memory</h3>
                <p>Oral history records lived experience, language, personal memories, and community changes. As seen in Pages 64–66, it is a major method for capturing Orakzai history. However, oral history is evidence of memory, not automatically proof of fact. The strongest history comes from memory corroborated by other sources.</p>
                <div class="logic-diagram mini-diagram" style="max-width: 400px; margin: 20px auto;">
                    <svg viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg">
                        <rect width="400" height="100" rx="10" fill="#0E1110" stroke="#B59654"/>
                        <text x="200" y="40" text-anchor="middle" fill="#B59654" font-size="16" font-weight="700">MEMORY + CORROBORATION</text>
                        <text x="200" y="70" text-anchor="middle" fill="#F5F0E6" font-size="14">= STRONGER HISTORY</text>
                    </svg>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Preservation Workflow</h3>
                <p>Preservation is a process, not a single act. It begins with consent and ends with long-term stewardship. A responsible workflow ensures that records remain authentic and accessible.</p>
                <div class="logic-diagram" style="margin: 20px 0;">
                    <svg viewBox="0 0 760 120" xmlns="http://www.w3.org/2000/svg">
                        <rect width="760" height="120" rx="10" fill="#0E1110" stroke="#B59654"/>
                        <g font-size="10" fill="#F5F0E6" text-anchor="middle">
                            <text x="50" y="60">CONSENT</text><path d="M80 60 H110" stroke="#B59654"/>
                            <text x="140" y="60">RECORD</text><path d="M170 60 H200" stroke="#B59654"/>
                            <text x="230" y="60">IDENTIFY</text><path d="M260 60 H290" stroke="#B59654"/>
                            <text x="320" y="60">TRANSCRIBE</text><path d="M350 60 H380" stroke="#B59654"/>
                            <text x="410" y="60">CONTEXT</text><path d="M440 60 H470" stroke="#B59654"/>
                            <text x="500" y="60">STORE</text><path d="M530 60 H560" stroke="#B59654"/>
                            <text x="590" y="60">BACKUP</text><path d="M620 60 H650" stroke="#B59654"/>
                            <text x="680" y="60">PRESERVE</text>
                        </g>
                    </svg>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Ethical Core: Consent</h3>
                <p>Consent is the foundation of ethical archiving. Before publishing, narrators must know who is collecting, why, and where it will appear. Recording does not grant an automatic right to publish.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Metadata: Context for Memory</h3>
                <p>A photograph or recording without metadata loses its historical value. Metadata provides the who, when, where, and why. It is the information that makes a digital file a historical record.</p>
                <div class="logic-diagram mini-diagram" style="max-width: 400px; margin: 20px auto;">
                    <svg viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg">
                        <rect width="400" height="100" rx="10" fill="#0E1110" stroke="#B59654"/>
                        <text x="200" y="40" text-anchor="middle" fill="#B59654" font-size="16" font-weight="700">PHOTO + METADATA</text>
                        <text x="200" y="70" text-anchor="middle" fill="#F5F0E6" font-size="14">= HISTORICAL RECORD</text>
                    </svg>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI and the Future of Heritage</h3>
                <p>AI offers tools for transcription, translation, and discovery. However, it must never be used to manufacture history. AI-generated reconstructions are not evidence. We do not claim that AI can replace human memory. Human review remains essential.</p>
                <div class="logic-diagram mini-diagram" style="max-width: 400px; margin: 20px auto;">
                    <svg viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg">
                        <rect width="400" height="100" rx="10" fill="#0E1110" stroke="#B59654"/>
                        <text x="200" y="40" text-anchor="middle" fill="#B59654" font-size="16" font-weight="700">SOURCE → AI → HUMAN REVIEW</text>
                        <text x="200" y="70" text-anchor="middle" fill="#F5F0E6" font-size="14">= RESPONSIBLE ARCHIVE</text>
                    </svg>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Preservation Priority Matrix</h3>
                <table class="data-table">
                    <thead>
                        <tr><th>Material</th><th>Urgency</th><th>Sensitivity</th><th>Priority</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Oral histories (Elders)</td><td>HIGH</td><td>ASSESS INDIVIDUALLY</td><td>HIGH</td></tr>
                        <tr><td>Old photographs</td><td>HIGH</td><td>MEDIUM</td><td>HIGH</td></tr>
                        <tr><td>Manuscripts</td><td>HIGH</td><td>HIGH</td><td>HIGH</td></tr>
                        <tr><td>Family documents</td><td>MEDIUM</td><td>HIGH</td><td>MEDIUM</td></tr>
                        <tr><td>Music recordings</td><td>MEDIUM</td><td>MEDIUM</td><td>MEDIUM</td></tr>
                        <tr><td>Pashto vocabulary</td><td>HIGH</td><td>LOW</td><td>HIGH</td></tr>
                        <tr><td>Proverbs</td><td>MEDIUM</td><td>LOW</td><td>MEDIUM</td></tr>
                        <tr><td>Recipes</td><td>LOW</td><td>LOW</td><td>LOW</td></tr>
                        <tr><td>Migration stories</td><td>MEDIUM</td><td>MEDIUM</td><td>MEDIUM</td></tr>
                        <tr><td>Women's histories</td><td>HIGH</td><td>HIGH</td><td>HIGH</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Digital Preservation</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">What still needs to be documented</h3>
                <ul style="columns: 2;">
                    <li>Orakzai oral histories</li>
                    <li>Village-level archives</li>
                    <li>Family photographs</li>
                    <li>Pashto recordings</li>
                    <li>Local vocabulary</li>
                    <li>Proverbs and poetry</li>
                    <li>Music and Attan</li>
                    <li>Food and crafts</li>
                    <li>Festivals and Hujras</li>
                    <li>Women's oral histories</li>
                    <li>Migration stories</li>
                    <li>Historical manuscripts</li>
                </ul>
                <p style="margin-top: 20px;">“The largest archive may not be a building. It may be the memories stored in homes, phones, family boxes and human voices. The challenge is to preserve them before they become difficult to recover.”</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Oral History Questions</h3>
                <ol style="columns: 2;">
                    <li>What family photographs should future generations see?</li>
                    <li>Who can identify the people in them?</li>
                    <li>What stories did your grandparents tell?</li>
                    <li>Which stories are no longer being told?</li>
                    <li>Which Pashto words are disappearing?</li>
                    <li>Which proverbs did elders use?</li>
                    <li>Which songs should be documented?</li>
                    <li>Which foods should be recorded?</li>
                    <li>Which crafts should be documented?</li>
                    <li>Which places carry important memories?</li>
                    <li>Which festivals should be documented?</li>
                    <li>What did the hujra mean to your generation?</li>
                    <li>What do elders remember that documents do not?</li>
                    <li>What experiences should remain private?</li>
                    <li>What should be shared publicly?</li>
                    <li>Who should control family archives?</li>
                    <li>How has migration changed cultural memory?</li>
                    <li>How has technology changed storytelling?</li>
                    <li>What should young people preserve?</li>
                    <li>What should future generations know about Orakzai life today?</li>
                </ol>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“I have come to believe that preservation is not simply about saving old things. It is about saving meaning. A photograph matters because someone remembers the people in it. A recording matters because a voice carries more than words. A Pashto proverb matters because its meaning can travel across generations. A family story matters because it connects people who may never meet.<br><br>
                Technology gives us extraordinary tools. But the tools are not the memory. People are. The elder who remembers. The parent who keeps the photograph. The young person who scans the document. The researcher who checks the source. The community that decides what should remain private. And the next generation that chooses to listen.<br><br>
                If we use technology responsibly, the digital world does not have to replace cultural memory. It can become one of the places where that memory survives.”</p>
            </div>

            <div class="final-statement">
                PRESERVE THE RECORD.<br>
                PROTECT THE CONTEXT.<br>
                PASS THE MEMORY FORWARD.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>UNESCO, <em>Guidelines for the Preservation of Digital Heritage</em>, 2003.</li>
                    <li>UNESCO/PERSIST, <em>Guidelines for the Selection of Digital Heritage for Long-Term Preservation</em>, 2nd Ed, 2021.</li>
                    <li>Mehmood, N., et al., "Integrating Digital Tools for the Documentation and Revitalization of Minority Languages in Pakistan," <em>JELLE</em>, 2025.</li>
                    <li>Boyd, D., "Search, Explore, Connect: Disseminating Oral History in the Digital Age," <em>OHDA</em>, 2012.</li>
                    <li>Manan, S. A., et al., "Ecological planning towards language revitalization: The Torwali minority language in Pakistan," <em>IJAL</em>, 2021.</li>
                    <li>Rahman, T., "The role of digital archives in preserving Pashto," <em>KJLR</em>, 2020.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            103
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

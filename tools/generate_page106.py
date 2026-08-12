from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-106-digitizing-tribal-archives.html'

GRAPHICS = [
    ("What is a tribal archive?", "FAMILY + COMMUNITY", "DIVERSE RECORD", "NOT STANDARDIZED"),
    ("Archive types", "FAMILY / RELIGIOUS", "GOVT / COLONIAL", "DIASPORA / MEDIA"),
    ("Orakzai landscape", "SCATTERED SOURCES", "DISTRIBUTED DATA", "CROSS-INSTITUTION"),
    ("Why digitize?", "FRAGILE ORIGIN", "PRESERVE + DISCOVER", "RESEARCH ACCESS"),
    ("What to digitize?", "PHOTOS + DOCUMENTS", "MAPS + AUDIO", "GENEALOGIES"),
    ("Sensitive materials", "PRIVATE DATA", "CULTURAL ETHICS", "RESTRICTED ACCESS"),
    ("Archive triage", "URGENT / IMPORTANT", "ROUTINE / DUP", "PRIORITY SCALE"),
    ("Collection survey", "INVENTORY", "CONDITION CHECK", "RIGHTS REVIEW"),
    ("Unique identifiers", "STABLE ID", "TRACKING", "PROPOSED SYSTEM"),
    ("Provenance", "CREATOR → OWNER", "CHAIN OF CUSTODY", "VERIFIED SOURCE"),
    ("Chain of custody", "TRANSFERS", "DOCUMENTATION", "RESEARCH TRUST"),
    ("Digitization workflow", "SURVEY → CAPTURE", "METADATA → BACKUP", "ACCESS"),
    ("Original material", "SAFE HANDLING", "STABLE ENV", "NO ALTERATION"),
    ("Photograph digitization", "FLAT / ALBUM", "NEGATIVE / SLIDE", "TECH VARIES"),
    ("Document digitization", "LETTERS / DEEDS", "MASTER → ACCESS", "METADATA"),
    ("Manuscripts", "FRAGILE BINDING", "INK / MARGINALIA", "PHYSICAL CONTEXT"),
    ("Pashto/Perso-Arabic", "ORTHOGRAPHY", "HANDWRITING", "SCRIPT CHALLENGE"),
    ("OCR", "IMAGE → TEXT", "HUMAN REVIEW", "ERROR DETECTION"),
    ("Audio archives", "MAGNETIC MEDIA", "DETERIORATION", "VOICE PRESERVE"),
    ("Video archives", "VHS / DIGITAL", "MASTER / ACCESS", "COMMUNITY EVENT"),
    ("Maps", "HISTORICAL DATE", "SOURCE CONTEXT", "NO SILENT CHANGE"),
    ("Genealogies", "FAMILY TREE", "PROVENANCE", "PRIVACY REVIEW"),
    ("Religious records", "MANUSCRIPTS", "COMMUNITY ACCESS", "SACRED CONTEXT"),
    ("Colonial archives", "ADMIN DATA", "CRITICAL READING", "BIAS AWARENESS"),
    ("Post-1947 records", "GOVT / MEDIA", "DEVELOPMENT", "MIGRATION"),
    ("Migration archives", "PASSPORTS / LETTERS", "SENSITIVE DATA", "REDACTION NEED"),
    ("Diaspora archives", "GEOG DISPERSED", "DIGITAL CONNECT", "FAMILY RECORD"),
    ("Metadata", "DATA ABOUT DATA", "CONTEXT + MEANING", "DISCOVERABILITY"),
    ("Metadata example", "KNOWN / UNKNOWN", "IDENTIFIER", "CONFIDENCE LEVEL"),
    ("Digital files", "MASTER / ACCESS", "THUMBNAIL", "NO OVERWRITE"),
    ("File formats", "TIFF / WAV / PDF/A", "PNG / MP3 / TXT", "SUSTAINABILITY"),
    ("Filename convention", "CONSISTENCY", "IDENTIFIER", "PRACTICAL EX"),
    ("Folder structure", "HIERARCHY", "ORGANIZATION", "DISCOVERABILITY"),
    ("Backup", "3 COPIES", "2 MEDIA TYPES", "1 OFFSITE"),
    ("Checksums", "FILE HASH", "INTEGRITY", "NOT AUTHENTICITY"),
    ("Access levels", "OPEN / LIMITED", "RESTRICTED / PRIV", "DECISION DATA"),
    ("Copyright", "PHYSICAL OWN", "COPYRIGHT OWN", "LEGAL DISTINCT"),
    ("Privacy", "PERSONAL DATA", "REVIEW NEED", "RESPONSIBLE"),
    ("Cultural sensitivity", "COMMUNITY RULE", "SACRED DATA", "RESPECT"),
    ("Community consent", "DISCUSSION", "VOLUNTARY", "ACCESS POLICY"),
    ("Archive control", "FAMILY / COMM", "INSTITUTIONAL", "GOVERNANCE"),
    ("Governance", "OWNERSHIP / ACCESS", "PRESERVATION", "DISPUTE RESOLVE"),
    ("Digitization ethics", "NO INVENTION", "NO ALTERATION", "CONTEXT PRESERVE"),
    ("AI archive assistance", "OCR / TRANSCRIPT", "METADATA TAG", "ASSISTANT ONLY"),
    ("AI restoration", "DIGITAL CLEANUP", "NO FABRICATION", "LABEL CHANGES"),
    ("Deepfakes", "SYNTHETIC MEDIA", "VERIFY PROV", "COMPARE SOURCES"),
    ("Searchable history", "INDEXED DATA", "DISCOVERABILITY", "SOURCE CRITIC"),
    ("Digital humanities", "MAPS + TIMELINES", "VISUALIZATION", "DATA ANALYSIS"),
    ("Historical GIS", "PLACE + DATE", "SOURCE + STORY", "NO INVENTION"),
    ("3D archiving", "3D SCANNING", "VIRTUAL EXHIBIT", "FUTURE TECH"),
    ("Digital exhibition", "STORY + SOURCE", "CONTEXT", "INTERPRETATION"),
    ("Proposed archive", "CONCEPTUAL MODEL", "12 CATEGORIES", "FUTURE VISION"),
    ("Contribution workflow", "DONOR → SURVEY", "RIGHTS → ARCHIVE", "DECISION"),
    ("Family donation", "DONATE / LEND", "DIGITAL COPY", "OWNERSHIP RETAIN"),
    ("Oral history contribution", "INTERVIEW → CONSENT", "TRANSCRIPT", "ACCESS LEVEL"),
    ("Researcher responsibility", "CITE SOURCES", "RESPECT LIMITS", "PROVENANCE"),
    ("Archivist responsibility", "PRESERVE + DESC", "PROTECT + DOC", "INTEGRITY"),
    ("Community responsibility", "IDENTIFY PEOPLE", "CORRECT NAMES", "CONTEXT"),
    ("Future generations", "FRAGILE → PRESERVE", "RESEARCHER", "EVIDENCE"),
    ("Limitations", "NOT RECOVER ALL", "NOT PROVE ALL", "NOT REMOVE BIAS"),
    ("Research gap", "DIALECTS + VILLAGE", "WOMEN / CHILDREN", "DOCUMENTATION"),
    ("Oral-history questions", "FAMILY PHOTOS", "ELDER STORIES", "FUTURE VISION"),
    ("Author reflection", "EVIDENCE + CONTEXT", "BRIDGE GENERATIONS", "UNDERSTANDING"),
    ("Final statement", "SOURCE + STORY", "CONTEXT", "DISCOVERY"),
    ("Photograph archive", "VISUAL", "MEMORY", "ARCHIVE"),
    ("Document archive", "TEXT", "HISTORY", "ARCHIVE"),
    ("Manuscript archive", "HANDWRITTEN", "SACRED", "ARCHIVE"),
    ("Map archive", "SPATIAL", "BOUNDARY", "ARCHIVE"),
    ("Audio archive", "VOICE", "SOUND", "ARCHIVE"),
    ("Video archive", "VISUAL", "PERFORMANCE", "ARCHIVE"),
    ("Genealogy archive", "FAMILY", "IDENTITY", "ARCHIVE"),
    ("Diaspora archive", "GLOBAL", "CONNECT", "ARCHIVE"),
    ("Colonial source analysis", "ADMIN", "BIAS", "CRITICAL"),
    ("Source comparison", "CROSS-REF", "VERIFY", "TRIANGULATE"),
    ("Evidence chain", "SOURCE", "CONTEXT", "TRUTH"),
    ("Metadata chain", "DATA", "CONTEXT", "MEANING"),
    ("Preservation master", "HIGH QUAL", "UNCOMPRESSED", "PERMANENT"),
    ("Access copy", "COMPRESSED", "USABLE", "DISTRIBUTE"),
    ("Archive box", "STORAGE", "PROTECT", "COLLECT"),
    ("Digital repository", "SERVER", "SECURE", "ACCESS"),
    ("Search index", "DISCOVER", "QUERY", "FIND"),
    ("Provenance chain", "ORIGIN", "CUSTODY", "TRUST"),
    ("Rights management", "LEGAL", "ETHICAL", "CONTROL"),
    ("Privacy review", "SENSITIVE", "PROTECT", "DIGNITY"),
    ("Community review", "PARTICIPATE", "REVIEW", "SOVEREIGN"),
    ("AI verification", "TOOL", "ASSIST", "REVIEW"),
    ("Human review", "AUTHORITY", "FINAL", "TRUTH"),
    ("Historical timeline", "EVENT", "DATE", "SEQUENCE"),
    ("Place-name archive", "GEOG", "LOCAL", "HISTORY"),
    ("Family memory", "ELDER", "STORY", "RECORD"),
    ("Village memory", "COMMUNITY", "HISTORY", "PLACE"),
    ("Future researcher", "SEARCH", "ANALYZE", "LEARN"),
    ("Digital exhibition", "VIRTUAL", "DISPLAY", "TEACH"),
    ("Documentary heritage", "RECORD", "MEMORY", "WORLD"),
    ("Preservation planning", "PLAN", "MONITOR", "SUSTAIN"),
    ("Archive risk", "LOSS", "OBSOLETE", "PROTECT"),
    ("Digital continuity", "ACCESS", "TIME", "FUTURE"),
    ("Intergenerational memory", "PAST", "PRESENT", "FUTURE"),
    ("Evidence preserved", "SOURCE", "STORY", "SAVED"),
    ("Digital archive", "DATA", "MEMORY", "SYSTEM"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g106-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g106-{index}-title g106-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g106-{index}-title">{safe}</title><desc id="g106-{index}-desc">A three-stage conceptual relationship: {left}, {center}, and {right}. This is an archival framework.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g106-{index}-caption" class="diagram-caption">{index}. {safe} — archival framework.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Digitizing Tribal Archives</title><desc id="hero-desc">An archival table with old photos, manuscripts, maps, and tapes being digitized into a structured digital archive against a subtle mountain landscape.</desc><defs><linearGradient id="h106-bg" x1="0" x2="1"><stop stop-color="#1A1A18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1A1A18"/></linearGradient><linearGradient id="h106-glow" x1="0" x2="1"><stop stop-color="#B59654" stop-opacity=".1"/><stop offset=".5" stop-color="#B59654" stop-opacity=".3"/><stop offset="1" stop-color="#B59654" stop-opacity=".1"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h106-bg)" stroke="#B59654" stroke-opacity=".55"/><path d="M20 320 L120 200 L200 280 L320 150 L450 320Z" fill="#0B241A" fill-opacity=".3" stroke="#2E8B57" stroke-opacity=".4"/><rect x="60" y="150" width="280" height="220" rx="8" fill="#1B1B18" stroke="#B59654" stroke-opacity=".4"/><text x="200" y="180" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#B59654">ARCHIVAL SOURCE</text><rect x="80" y="200" width="100" height="70" rx="4" fill="#2A2A25" stroke="#B59654" stroke-opacity=".3"/><text x="130" y="240" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">PHOTO</text><rect x="200" y="200" width="120" height="70" rx="4" fill="#2A2A25" stroke="#B59654" stroke-opacity=".3"/><text x="260" y="240" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">MANUSCRIPT</text><rect x="80" y="290" width="240" height="60" rx="4" fill="#2A2A25" stroke="#B59654" stroke-opacity=".3"/><text x="200" y="325" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">MAP / LETTER / TAPE</text><path d="M340 260 H420" stroke="#B59654" stroke-width="3" stroke-dasharray="8 4"/><path d="M420 260 l-10 -6 v12 z" fill="#B59654"/><rect x="440" y="150" width="260" height="220" rx="8" fill="#111B24" stroke="#7894A8" stroke-opacity=".4"/><text x="570" y="180" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#7894A8">DIGITAL ARCHIVE</text><g transform="translate(460, 200)" fill="#7894A8" fill-opacity=".2"><rect x="0" y="0" width="220" height="30" rx="3"/><rect x="0" y="40" width="220" height="30" rx="3"/><rect x="0" y="80" width="220" height="30" rx="3"/><rect x="0" y="120" width="220" height="30" rx="3"/></g><text x="570" y="220" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#F5F0E6">METADATA / INDEX</text><text x="570" y="260" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#F5F0E6">PRESERVATION MASTER</text><text x="570" y="300" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#F5F0E6">ACCESS COPY</text><text x="570" y="340" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#F5F0E6">PROVENANCE CHAIN</text><g font-family="Arial,sans-serif" text-anchor="middle"><text x="380" y="405" fill="#B59654" font-size="11" letter-spacing="1.5">FIND → IDENTIFY → DOCUMENT → DIGITIZE → DESCRIBE → PRESERVE → SHARE</text></g></svg><figcaption id="hero-caption" class="diagram-caption">Digitizing Tribal Archives: Transforming vulnerable historical records into structured, preserved resources for future generations.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 106</title>
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
            <p class="section-label">PAGE 106</p>
            <h2>DIGITIZING TRIBAL ARCHIVES</h2>
            <p>“From fragile records to carefully preserved memory.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “An archive does not always begin in an archive building. Sometimes it begins in a wooden box. A photograph kept inside a family cupboard. A handwritten genealogy. An old letter. A land document. A school certificate. A religious manuscript. A cassette recording. A newspaper clipping. A map folded for decades. Or the memory of an elder who knows where an important document was once kept.<br><br>
                For communities whose histories have often been recorded by outsiders, preserving locally held records can add another dimension to the historical record. But digitization must be approached carefully. The first responsibility is not to publish. It is to understand what the record is, who owns it, where it came from, what it contains, and who should be allowed to access it. Only then can technology help transform vulnerable records into preserved historical resources.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">What is a Tribal Archive?</h3>
                <p>There is no single universal definition of a "tribal archive." In the context of Orakzai history, the term describes a diverse range of historically significant records held by families, community institutions, religious bodies, and government archives. These records are not standardized and require specific cultural and ethical considerations during digitization.</p>
                <p><strong>Diverse Archival Record:</strong> FAMILY + COMMUNITY + RELIGIOUS + LOCAL + INSTITUTIONAL + GOVERNMENT + DIASPORA</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Orakzai Archival Landscape</h3>
                <p>Historical evidence relating to Orakzai communities is distributed across various institutions rather than a single central repository. Official state records, colonial documents, and academic research coexist with private family collections and oral histories. Digitization connects these fragments without requiring the physical transfer of originals. We distinguish between <strong>Primary vs Secondary</strong> sources to assess historical reliability.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Archival Ethics and Sensitivity</h3>
                <p>Digitization does not automatically make a record public or authentic. It does not transfer ownership or erase cultural sensitivity. Ethical archiving requires informed consent, especially for private correspondence, religious material, or records involving living individuals. Access levels (Open, Limited, Restricted, Private) must be determined based on privacy, copyright, and community sovereignty.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Archival Claim Matrix</h3>
                <table class="data-table">
                    <thead>
                        <tr><th>Claim</th><th>Archive/Material</th><th>Evidence</th><th>Source</th><th>Confidence</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Diverse Holdings</td><td>Family/Community</td><td>UCLA MEAP records</td><td>UCLA (2024)</td><td>High</td></tr>
                        <tr><td>Community Sovereignty</td><td>Metadata Practices</td><td>"Metadata as Radical Care"</td><td>ResearchGate (2024)</td><td>High</td></tr>
                        <tr><td>Safeguarding Principles</td><td>Documentary Heritage</td><td>UNESCO General Guidelines</td><td>UNESCO (2002)</td><td>High</td></tr>
                        <tr><td>Provenance Chain</td><td>Digital Preservation</td><td>ICA/DPC Standards</td><td>DPC (2025)</td><td>High</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digitization Workflow</h3>
                <p>A responsible workflow involves: 1. Survey, 2. Identify, 3. Consent, 4. Prepare, 5. Capture, 6. Quality Control, 7. Metadata, 8. Preservation Master, 9. Backup, and 10. Access. We follow the <strong>3-2-1 Backup Rule</strong> (3 copies, 2 media types, 1 offsite) for digital resilience. Documenting the <strong>Provenance</strong> (Creator → Owner → Custodian → Digitizer) and the <strong>Chain of Custody</strong> is essential for assessing a record's historical value.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI and Archive Assistance</h3>
                <p>AI tools can assist in OCR for Perso-Arabic scripts, transcription, and metadata tagging. However, AI is an assistant, not an authority. We do not automatically assume AI output is correct. AI-generated text is not evidence of historical truth. Human review is the final authority to ensure authenticity and prevent the fabrication of history. We do not claim that technology can independently preserve culture; evidence is limited regarding AI's ability to capture deep cultural context.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Digitizing Archives</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Research Gap: What Still Needs to be Documented</h3>
                <ul style="columns: 2;">
                    <li>Privately held Orakzai photographs</li>
                    <li>Family document collections</li>
                    <li>Village histories (unwritten)</li>
                    <li>Historical maps (local/colonial)</li>
                    <li>Manuscripts (religious/literary)</li>
                    <li>Pashto recordings (dialects)</li>
                    <li>Oral histories (elders/women)</li>
                    <li>Migration and diaspora records</li>
                    <li>Community and sports publications</li>
                    <li>Traditional music and poetry</li>
                    <li>Educational and school records</li>
                    <li>Local place-name histories</li>
                    <li>Colonial and post-1947 archives</li>
                    <li>Digital preservation standards</li>
                </ul>
                <p style="margin-top: 20px;">“Before an archive can be digitized, someone must first discover that it exists.”</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Oral History Questions</h3>
                <ol style="columns: 2;">
                    <li>What old documents does your family still have?</li>
                    <li>Who keeps them and where did they come from?</li>
                    <li>What stories are attached to family photographs?</li>
                    <li>Which recordings exist on old media (cassettes)?</li>
                    <li>Which documents relate to migration or land?</li>
                    <li>Which village histories are unwritten?</li>
                    <li>Which Pashto words appear in old records?</li>
                    <li>Who should control access to family records?</li>
                    <li>What material has already been lost?</li>
                    <li>What should future generations be able to search?</li>
                </ol>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“An archive can begin with one photograph. One document. One voice. One family deciding that something should not be forgotten. For communities whose histories are scattered across homes, institutions and generations, digitization can bring fragments together without requiring every original to leave the hands of the people who preserve it.<br><br>
                But technology should serve memory, not replace it. A scanner cannot explain a photograph. A database cannot know why a story matters. An algorithm cannot decide whether a private document should be public. Those decisions require people. They require context. They require consent. And they require respect for uncertainty.<br><br>
                If we digitize carefully, preserve the original, record provenance, protect privacy and allow communities to participate in the process, then scattered records can become a stronger historical resource. The goal is not to create a perfect archive. The goal is to make sure that evidence that can still be saved is not silently lost.”</p>
            </div>

            <div class="final-statement">
                DIGITIZE THE RECORD. PRESERVE ITS PROVENANCE. RESPECT ITS PEOPLE.<br>
                LET THE FUTURE READ THE EVIDENCE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>UNESCO, <em>Memory of the World: General Guidelines to Safeguard Documentary Heritage</em>, 2002.</li>
                    <li>ResearchGate, "Metadata as Radical Care: How Community-Led Archives Reimagine Descriptive Practices," 2024.</li>
                    <li>UCLA MEAP, <em>Endangered Archives from Sufi Shrines of the Afghan-Pakistan Frontier</em>, 2024.</li>
                    <li>Digital Preservation Coalition, <em>Digital Preservation Handbook</em>, 2025.</li>
                    <li>Boyd, D., "Oral History in the Digital Age," <em>OHDA</em>, 2012.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            106
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

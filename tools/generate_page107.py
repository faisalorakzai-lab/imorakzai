from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-107-oral-history-technology.html'

GRAPHICS = [
    ("What is oral history?", "RECORDED MEMORY", "PERSONAL EXPERIENCE", "PRIMARY SOURCE"),
    ("Memory vs evidence", "REMEMBERED STORY", "CORROBORATION", "VERIFIED RECORD"),
    ("Why oral history matters", "UNWRITTEN DATA", "LOCAL PERSPECTIVE", "CULTURAL CONTEXT"),
    ("Whose voice?", "DIVERSE CIRCLE", "INCLUSIVE RECORD", "REPRESENTATION"),
    ("Elders", "LONG-TERM MEMORY", "FAMILY STORIES", "TRADITION PASS"),
    ("Women", "HOUSEHOLD HISTORY", "SOCIAL NETWORKS", "HIDDEN VOICES"),
    ("Youth", "NEW EXPERIENCES", "TECH ADAPTATION", "FUTURE ARCHIVE"),
    ("Interviewer", "QUESTIONER", "LISTENER", "CONTEXT CREATOR"),
    ("Language", "MEANING + TONE", "METAPHOR + IDIOM", "CULTURAL NUANCE"),
    ("Pashto archive", "ORIGINAL VOICE", "DIALECT VARIATION", "VOCABULARY"),
    ("Transcription", "AUDIO → TEXT", "VERBATIM / EDITED", "SEARCHABLE"),
    ("Timestamps", "LOCATE THEME", "CHRONOLOGY", "REFERENCE TOOL"),
    ("Translation", "PASHTO → ENGLISH", "INTERPRETATION", "ACCESSIBILITY"),
    ("Untranslatable concepts", "KINSHIP / LAND", "HOSPITALITY", "CONTEXT NEED"),
    ("Oral history and place", "VOICE + MAP", "VILLAGE MEMORY", "SPATIAL CONTEXT"),
    ("Oral history and time", "EXACT / APPROX", "RELATIVE EVENT", "GENERATION"),
    ("Oral genealogy", "TESTIMONY", "LINEAGE MEMORY", "NOT FACT ALONE"),
    ("Recording technology", "RECORDER / PHONE", "MICROPHONE", "STABILITY"),
    ("Audio quality", "CLEAR SPEECH", "LOW NOISE", "PRESERVATION"),
    ("Audio vs video", "VOICE FOCUS", "VISUAL CONTEXT", "PURPOSE FIT"),
    ("Consent", "INFORMED", "VOLUNTARY", "DOCUMENTED"),
    ("Consent levels", "RECORD / TRANS", "PUBLISH / ONLINE", "REUSE PERMIT"),
    ("Sensitive stories", "TRAUMA / DISPUTE", "PRIVACY NEED", "RESTRICTION"),
    ("Privacy", "PERSONAL DATA", "PROTECTION", "RESPONSIBLE"),
    ("Rights", "SPEAKER / INTERV", "ARCHIVE / FAMILY", "STAKEHOLDERS"),
    ("Community ownership", "SHARED CONTROL", "SOVEREIGNTY", "PARTICIPATION"),
    ("Metadata", "DATA ABOUT DATA", "DISCOVERABILITY", "MANAGEMENT"),
    ("Sample metadata", "INTERVIEW ID", "DATE / TOPIC", "CONSENT STATUS"),
    ("Digital preservation", "MASTER / BACKUP", "ACCESS COPY", "CONTINUITY"),
    ("Backup", "3 COPIES", "2 MEDIA TYPES", "1 OFFSITE"),
    ("Audio formats", "WAV / FLAC", "MP3 / AAC", "SUSTAINABILITY"),
    ("Transcript formats", "TXT / DOCX", "XML / TEI", "RESEARCH FIT"),
    ("Searchable history", "INDEXED VOICE", "THEME FINDING", "ACCESS"),
    ("Keyword indexing", "PERSON / PLACE", "EVENT / TOPIC", "NAVIGATION"),
    ("AI transcription", "SPEECH-TO-TEXT", "HUMAN REVIEW", "ASSISTANCE"),
    ("AI translation", "MACHINE OUTPUT", "CULTURAL LOSS", "REVIEW NEED"),
    ("AI speaker ID", "SEGMENTATION", "BIOMETRIC RISK", "SAFEGUARD"),
    ("AI summarization", "NAVIGATE LONG", "NOT SOURCE", "RESEARCH TOOL"),
    ("AI historical memory", "ORGANIZE / SEARCH", "NO INVENTION", "ASSISTANT"),
    ("Synthetic voices", "AI RECREATION", "ETHICAL RISK", "LABEL CLEAR"),
    ("Digital restoration", "NOISE REDUCTION", "INTEGRITY", "ORIGINAL KEEP"),
    ("Deepfakes", "FABRICATION", "VERIFY PROV", "COMPARE SOURCE"),
    ("Social media", "WHATSAPP / YT", "PODCAST", "PERMISSION NEED"),
    ("Digital diaspora", "GLOBAL MEMORY", "CONNECT HOME", "REMOTE RECORD"),
    ("Remote interviews", "VIDEO CALL", "PHONE RECORD", "TECH LIMITS"),
    ("Children", "SAFEGUARDING", "PARTICIPATION", "PRIVACY"),
    ("Elders and tech", "ACCESSIBILITY", "DESIGN FOR ALL", "INCLUSION"),
    ("Accessibility", "CAPTIONS / TEXT", "AUDIO CONTROL", "EQUAL ACCESS"),
    ("Oral-history exhibit", "VOICE + PHOTO", "STORY + MAP", "PUBLIC LEARN"),
    ("Education", "STUDENT STUDY", "LANGUAGE LEARN", "PRIMARY SOURCE"),
    ("Research", "MULTI-SOURCE", "TRIANGULATION", "EVALUATION"),
    ("Corroboration", "CLAIM + SOURCE", "VERIFICATION", "CONFIDENCE"),
    ("Contradictions", "AGREE / DIFFER", "UNCERTAINTY", "EXPLANATION"),
    ("Trauma-sensitive", "EMOTIONAL CARE", "NO PRESSURE", "ETHICS"),
    ("Migration memory", "WHY / WHERE", "ADAPTATION", "IDENTITY"),
    ("Urban memory", "CITY LIFE", "NETWORKS", "SOCIAL CHANGE"),
    ("Family archive", "VOICE + PHOTO", "DOCUMENT + MAP", "CONTEXT"),
    ("Music", "SONG / POETRY", "PERFORMANCE", "PERMISSION"),
    ("Proverbs", "ORAL WISDOM", "WORDING KEEP", "WORD PRESERVE"),
    ("Food", "RECIPE / TERM", "FESTIVAL", "NOT UNIVERSAL"),
    ("Religion", "PERSONAL FAITH", "COMMUNITY LIFE", "TESTIMONY"),
    ("Politics", "OPINION / EVENT", "INSTITUTION", "CRITICAL READ"),
    ("Colonial history", "LOCAL VIEW", "COLONIAL DATA", "COMPARISON"),
    ("Post-1947 history", "ADMIN CHANGE", "DEVELOPMENT", "FATA MEMORY"),
    ("Archive access", "OPEN / LIMITED", "RESTRICTED", "TIME CHANGE"),
    ("Researcher access", "APPLICATION", "PERMISSION", "CITATION"),
    ("Family access", "PRIVATE RULE", "INHERITANCE", "CONTROL"),
    ("Community access", "RESPECT", "INTERPRETATION", "SOVEREIGNTY"),
    ("Proposed archive", "CONCEPTUAL", "18 CATEGORIES", "FUTURE VISION"),
    ("Interview workflow", "RESEARCH → CONSENT", "RECORD → PRESERVE", "PIPELINE"),
    ("Pre-interview", "PURPOSE / TOPIC", "LANGUAGE / TIME", "PREPARATION"),
    ("Interview questions", "OPEN ENDED", "NO ASSUMPTION", "MEMORY FLOW"),
    ("Avoid leading", "OPEN VS CLOSED", "NARRATOR LEAD", "RICHER DATA"),
    ("Field notes", "CONTEXT / ENV", "PARTICIPANTS", "OBSERVATION"),
    ("Research gap", "DIALECTS / WOMEN", "VILLAGE HISTORY", "DOCUMENTATION"),
    ("Archive questions", "ELDER STORIES", "MIGRATION", "FUTURE FIND"),
    ("Author reflection", "VOICE FRAGILE", "TECH BRIDGE", "UNDERSTANDING"),
    ("Final statement", "PRESERVE VOICE", "PROTECT MEMORY", "FUTURE LISTEN"),
    ("Voice waveform", "SOUND", "DATA", "WAVE"),
    ("Speaker profile", "NARRATOR", "ROLE", "IDENTITY"),
    ("Interview timeline", "START", "THEMES", "END"),
    ("Consent record", "SIGNED", "DATED", "SPECIFIC"),
    ("Transcript alignment", "TEXT", "TIME", "AUDIO"),
    ("Translation alignment", "SOURCE", "TARGET", "REVIEW"),
    ("Source comparison", "ORAL", "WRITTEN", "VISUAL"),
    ("Evidence confidence", "HIGH", "MEDIUM", "LOW"),
    ("Oral-memory map", "STORY", "PLACE", "PATH"),
    ("Migration story", "ORIGIN", "PATH", "DESTINATION"),
    ("Family memory tree", "ELDER", "PARENT", "YOUTH"),
    ("Digital archive", "SERVER", "STORAGE", "ACCESS"),
    ("Audio preservation", "WAV", "METADATA", "BACKUP"),
    ("Future researcher", "SEARCH", "ANALYZE", "DISCOVER"),
    ("Intergenerational", "PAST", "PRESENT", "FUTURE"),
    ("Pashto preservation", "SCRIPT", "SOUND", "LEGACY"),
    ("Human + AI workflow", "MACHINE", "HUMAN", "VERIFIED"),
    ("Source verification", "CROSS-REF", "PROVENANCE", "TRUTH"),
    ("Archive integrity", "CHECKSUM", "MONITOR", "SAFE"),
    ("Responsible access", "PRIVACY", "ETHICS", "DIGNITY"),
    ("Voice-to-archive", "VOICE", "RECORD", "PRESERVE"),
    ("Evidence chain", "SOURCE", "CONTEXT", "UNDERSTANDING"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g107-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g107-{index}-title g107-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g107-{index}-title">{safe}</title><desc id="g107-{index}-desc">A three-stage conceptual relationship: {left}, {center}, and {right}. This is an oral history framework.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g107-{index}-caption" class="diagram-caption">{index}. {safe} — oral history framework.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Oral History & Technology</title><desc id="hero-desc">An elder speaking into a microphone with a younger interviewer. Digital waveform lines move toward transcript, Pashto script, translation, and archive icons against an Orakzai mountain backdrop.</desc><defs><linearGradient id="h107-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient><linearGradient id="h107-wave" x1="0" x2="1"><stop stop-color="#2E8B57"/><stop offset="1" stop-color="#B59654"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h107-bg)" stroke="#B59654" stroke-opacity=".55"/><path d="M20 350 L120 220 L200 300 L320 180 L450 350Z" fill="#0B241A" fill-opacity=".3" stroke="#2E8B57" stroke-opacity=".4"/><g transform="translate(100, 200)"><circle cx="0" cy="0" r="40" fill="#2A2A25" stroke="#B59654" stroke-opacity=".6"/><text x="0" y="5" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">ELDER</text></g><g transform="translate(220, 250)"><circle cx="0" cy="0" r="30" fill="#2A2A25" stroke="#B59654" stroke-opacity=".6"/><text x="0" y="5" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#F5F0E6">YOUTH</text></g><path d="M140 200 Q 180 180 220 220" fill="none" stroke="#B59654" stroke-width="2" stroke-dasharray="4 2"/><path d="M250 250 H350" stroke="url(#h107-wave)" stroke-width="3" stroke-linecap="round"/><path d="M350 250 C400 250 420 200 450 200 H550" fill="none" stroke="url(#h107-wave)" stroke-width="2" stroke-dasharray="6 3"/><g transform="translate(580, 150)" fill="#111B24" stroke="#7894A8" stroke-opacity=".6"><rect x="0" y="0" width="120" height="150" rx="6"/><text x="60" y="30" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#7894A8" stroke="none">ARCHIVE</text><line x1="20" y1="50" x2="100" y2="50" stroke-width="1"/><line x1="20" y1="70" x2="100" y2="70" stroke-width="1"/><line x1="20" y1="90" x2="100" y2="90" stroke-width="1"/><line x1="20" y1="110" x2="100" y2="110" stroke-width="1"/></g><g font-family="Arial,sans-serif" text-anchor="middle"><text x="380" y="400" fill="#B59654" font-size="11" letter-spacing="1.5">VOICE → RECORD → CONTEXT → TRANSCRIBE → TRANSLATE → PRESERVE → ACCESS</text></g></svg><figcaption id="hero-caption" class="diagram-caption">Oral History & Technology: When memory becomes a record, technology helps the next generation listen.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 107</title>
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
            <p class="section-label">PAGE 107</p>
            <h2>ORAL HISTORY & TECHNOLOGY</h2>
            <p>“When memory becomes a record, technology can help the next generation listen.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Before history becomes a document, it is often a voice. An elder describing a village. A parent remembering migration. A grandmother recalling a family custom. A farmer describing a landscape. A poet reciting lines remembered from another generation. A child asking questions that an older generation may be hearing for the last time.<br><br>
                Oral history captures these voices. Technology gives us new ways to preserve them. A recording can travel across generations. A transcript can make a conversation searchable. A translation can introduce a story to a wider audience. A digital archive can keep a voice available long after the original recording has become fragile.<br><br>
                But technology must remain a servant of memory. It should preserve the voice without erasing its uncertainty. It should increase access without destroying privacy. And it should help future generations listen without pretending that every memory is an unquestionable fact.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">What is Oral History?</h3>
                <p>Oral history is a method of documenting people's memories, experiences and interpretations through recorded interviews. It is distinct from folklore or casual conversation because it involves a deliberate methodological approach, documentation, and informed consent. A person's memory may preserve details unavailable elsewhere, but it must be corroborated with other sources as it is evidence of experience rather than automatically verified fact.</p>
                <p><strong>Oral History Source:</strong> PERSON + MEMORY + INTERVIEW + RECORDING</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Why Oral History Matters for Orakzai</h3>
                <p>For Orakzai communities, oral history can preserve information that may not exist in formal written archives, such as village life, Hujra traditions, traditional sports, and women's household experiences. We do not claim that undocumented traditions exist merely because they could be recorded; rather, we provide the framework for their responsible documentation.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Language and Transcription</h3>
                <p>Pashto is a vital archival language. Preserving original Pashto recordings alongside transcripts and translations is essential for maintaining cultural nuance, metaphors, and dialect variation. We distinguish between <strong>verbatim</strong> and <strong>edited</strong> transcripts and emphasize that machine translation is an assistant, not a final authority.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Oral History Claim Matrix</h3>
                <table class="data-table">
                    <thead>
                        <tr><th>Claim</th><th>Subject</th><th>Evidence</th><th>Source</th><th>Confidence</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Voice as Primary Source</td><td>Methodology</td><td>OHA Manual</td><td>OHA (2024)</td><td>High</td></tr>
                        <tr><td>Pashto Oral Vitality</td><td>Culture</td><td>CAP Documentation</td><td>CAP (2023)</td><td>High</td></tr>
                        <tr><td>Digital Resilience (3-2-1)</td><td>Technology</td><td>DPC/OHA Guidelines</td><td>OHA (2024)</td><td>High</td></tr>
                        <tr><td>AI Transcription Risk</td><td>Technology</td><td>Archival Ethics Research</td><td>Lucidea (2025)</td><td>High</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Ethics and Consent</h3>
                <p>Consent is not a single sentence; it involves multiple decisions about recording, transcribing, publishing, and sharing. Informed consent is the ethical foundation of oral history. Privacy must be respected, especially for sensitive stories involving trauma, conflict, or living individuals. We distinguish between <strong>Ethical Best Practice</strong> and legal requirements.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI and Historical Memory</h3>
                <p>AI can assist with speech-to-text, translation, and summarization, but it should never manufacture missing evidence. We do not automatically assume AI output is correct. AI-generated text is not evidence of historical truth. Human review is the final authority to ensure authenticity and prevent the fabrication of history. We do not claim that technology can independently preserve culture; evidence is limited regarding AI's ability to capture deep cultural context.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Oral History & Technology</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Proposed Orakzai Oral History Archive — Concept</h3>
                <ul style="columns: 2;">
                    <li>ELDERS</li>
                    <li>WOMEN</li>
                    <li>YOUTH</li>
                    <li>FAMILY STORIES</li>
                    <li>VILLAGE MEMORY</li>
                    <li>MIGRATION</li>
                    <li>DIASPORA</li>
                    <li>LANGUAGE</li>
                    <li>MUSIC</li>
                    <li>POETRY</li>
                    <li>PROVERBS</li>
                    <li>EDUCATION</li>
                    <li>AGRICULTURE</li>
                    <li>MARKETS</li>
                    <li>RELIGIOUS LIFE</li>
                    <li>URBAN MEMORY</li>
                    <li>HISTORICAL TESTIMONY</li>
                </ul>
                <p style="margin-top: 20px;"><strong>PROPOSED CONCEPT — NOT A CLAIM THAT THIS ARCHIVE CURRENTLY EXISTS.</strong></p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Interview Questions</h3>
                <ol style="columns: 2;">
                    <li>Where did you grow up?</li>
                    <li>What do you remember about your village?</li>
                    <li>What did your family teach you?</li>
                    <li>What was school like?</li>
                    <li>How did people travel?</li>
                    <li>What did the market look like?</li>
                    <li>What role did the Hujra play?</li>
                    <li>What celebrations do you remember?</li>
                    <li>What songs or proverbs do you remember?</li>
                    <li>What changed during your lifetime?</li>
                    <li>Why did people migrate?</li>
                    <li>What do you remember about cities?</li>
                    <li>What traditions have changed?</li>
                    <li>What traditions have disappeared?</li>
                    <li>What should young people remember?</li>
                </ol>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“A voice is fragile. It exists in a moment. Then the conversation ends. The person who remembered it grows older. The language changes. The place changes. And eventually, the voice may disappear. Technology gives us an opportunity to slow that disappearance. A recording can preserve the sound of an elder's voice. A transcript can preserve the words. A translation can open the story to another audience. An archive can preserve the context.<br><br>
                But none of these should replace the person behind the memory. For me, the purpose of oral history is not to turn every memory into a fact. It is to give memory a responsible place in the historical record. The future should be able to hear what earlier generations remembered, while also understanding what remains uncertain. If we listen carefully today, tomorrow's generation will inherit more than photographs and documents. They will inherit voices.”</p>
            </div>

            <div class="final-statement">
                PRESERVE THE VOICE. PROTECT THE MEMORY. VERIFY THE RECORD.<br>
                LET FUTURE GENERATIONS LISTEN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Oral History Association (OHA), <em>Archiving Oral History: Manual of Best Practices</em>, 2024.</li>
                    <li>Citizens Archive of Pakistan (CAP), "Pashto Folk Stories and Oral Tradition," 2023.</li>
                    <li>Lucidea / NCSU, <em>The Ethical Use of Born-Digital Materials in Archives</em>, 2025.</li>
                    <li>Digital Preservation Coalition (DPC), <em>Digital Preservation Handbook</em>, 2025.</li>
                    <li>Smithsonian Institution Archives, "How to Do Oral History," 2024.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            107
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

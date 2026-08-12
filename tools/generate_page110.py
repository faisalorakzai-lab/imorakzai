from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-110-digital-heritage.html'

GRAPHICS = [
    ("What is digital heritage?", "HERITAGE", "DIGITAL", "PRESERVATION"),
    ("Physical to Digital", "PHYSICAL", "→", "DIGITAL COPY"),
    ("Born-Digital Heritage", "CREATED", "→", "DIGITAL RECORD"),
    ("Digitization ≠ Preservation", "SCAN", "≠", "LONG-TERM ACCESS"),
    ("Preservation Pillars", "METADATA", "STORAGE", "MIGRATION"),
    ("Heritage Types: Grid", "PHOTOS", "DOCS", "MAPS"),
    ("Audio Preservation", "WAVEFORM", "METADATA", "SONIC MEMORY"),
    ("Video Preservation", "FRAME", "FORMAT", "VISUAL MEMORY"),
    ("Pashto Language", "SCRIPT", "DIGITIZE", "LINGUISTIC"),
    ("Poetry Archive", "VERSE", "RECORD", "LITERARY"),
    ("Music Heritage", "TUNE", "PRESERVE", "CULTURAL"),
    ("Genealogy Archive", "LINEAGE", "DATA", "IDENTITY"),
    ("Family Archive", "PRIVATE", "→", "PROTECTED"),
    ("Community Archive", "COLLECTIVE", "→", "GOVERNED"),
    ("Object Digitization", "3D SCAN", "IMAGE", "ARTIFACT"),
    ("Place Digitization", "GPS", "PHOTO", "GEOGRAPHY"),
    ("Architectural Record", "PLAN", "PHOTO", "BUILT"),
    ("Newspaper Archive", "SERIAL", "OCR", "HISTORY"),
    ("Book Digitization", "PAGE", "TEXT", "LITERATURE"),
    ("Manuscript Preservation", "SCRIPT", "HI-RES", "TEXTUAL"),
    ("Art Heritage", "VISUAL", "DIGITIZE", "EXPRESSION"),
    ("Craft Knowledge", "PROCESS", "VIDEO", "TRADITION"),
    ("Community Memory", "STORY", "RECORD", "IDENTITY"),
    ("Digital Risks", "OBSOLESCENCE", "LOSS", "FAILURE"),
    ("Obsolete Format", "OLD FILE", "↔", "NO ACCESS"),
    ("Hardware Failure", "DISK", "CRASH", "LOSS"),
    ("Lost Account", "PLATFORM", "SHUT", "LOSS"),
    ("Broken Link", "URL", "404", "LOSS"),
    ("Metadata Loss", "DATA", "STRIP", "ANONYMOUS"),
    ("Fixity Check", "HASH", "VERIFY", "INTEGRITY"),
    ("3-2-1 Strategy", "3 COPIES", "2 MEDIA", "1 OFFSITE"),
    ("Cloud Preservation", "STORAGE", "SYNC", "RESILIENCE"),
    ("Offline Archive", "COLD", "SAFE", "SECURITY"),
    ("Format Migration", "OLD", "→", "NEW"),
    ("Emulation", "OLD OS", "RUN", "ACCESS"),
    ("Authenticity", "ORIGINAL", "↔", "VERIFIED"),
    ("Provenance", "SOURCE", "TRACK", "INTEGRITY"),
    ("Metadata: Descriptive", "TITLE", "DATE", "CREATOR"),
    ("Metadata: Preservation", "FIXITY", "EVENT", "RIGHTS"),
    ("Metadata: Technical", "FORMAT", "SIZE", "BITRATE"),
    ("IIIF Framework", "IMAGE", "ZOOM", "INTEROP"),
    ("Dublin Core", "15 ELEMENTS", "SCHEMA", "DISCOVERY"),
    ("PREMIS Standard", "PRESERVATION", "METADATA", "STANDARD"),
    ("OAIS Reference Model", "INGEST", "ARCHIVE", "ACCESS"),
    ("Trustworthy Repository", "ISO 16363", "CERT", "TRUST"),
    ("Orakzai Photo Heritage", "FAMILY", "LANDSCAPE", "HISTORY"),
    ("Photo + Context", "IMAGE", "STORY", "ARCHIVE"),
    ("Photo Metadata Card", "FIELDS", "VALUES", "RECORD"),
    ("Approximate Date", "c. 1950", "ESTIMATE", "LABEL"),
    ("Unverified Info", "CLAIM", "LABEL", "RESEARCH"),
    ("Photo Authenticity", "SOURCE", "VERIFY", "TRUST"),
    ("Restoration vs Manipulation", "CLEAN", "↔", "CHANGE"),
    ("AI Reconstruction", "AI", "VISUAL", "LABEL"),
    ("AI Warning Label", "NOT ORIGINAL", "LABEL", "ETHICS"),
    ("Document Heritage", "LETTER", "LAND", "RECORD"),
    ("Sensitive Document", "PRIVATE", "REDACT", "PROTECT"),
    ("Manuscript Imaging", "HI-RES", "LIGHT", "CAPTURE"),
    ("Transcription Flow", "IMAGE", "TEXT", "SEARCH"),
    ("OCR: Pashto", "SCRIPT", "AI", "TEXT"),
    ("Oral History Recording", "MIC", "VOICE", "DATA"),
    ("Interview Consent", "INFORMED", "SIGN", "ETHICS"),
    ("Consent Levels", "OPEN", "COMMUNITY", "PRIVATE"),
    ("Anonymization", "REDACT", "PROTECT", "ETHICS"),
    ("Takedown Policy", "REPORT", "REVIEW", "REMOVE"),
    ("Right to be Forgotten", "INDIVIDUAL", "REQUEST", "RIGHT"),
    ("Indigenous Sovereignty", "COMMUNITY", "CONTROL", "DATA"),
    ("Cultural Protocol", "TRADITION", "GUIDE", "ACCESS"),
    ("Digital Repatriation", "ARCHIVE", "→", "COMMUNITY"),
    ("Open Access Heritage", "PUBLIC", "SHARE", "LEARN"),
    ("Restricted Access", "SENSITIVE", "LIMIT", "PROTECT"),
    ("Fair Use / Fair Dealing", "RESEARCH", "EDUCATION", "RIGHTS"),
    ("Creative Commons", "LICENSE", "SHARE", "RULES"),
    ("Public Domain", "EXPIRED", "FREE", "ACCESS"),
    ("Copyright Verification", "CHECK", "DATE", "RIGHTS"),
    ("Privacy Review", "SCREEN", "PROTECT", "ETHICS"),
    ("Children's Privacy", "SAFEGUARD", "HIDE", "ETHICS"),
    ("Religious Sensitivity", "RESPECT", "CONTEXT", "HANDLE"),
    ("Genealogy Ethics", "SOURCE", "PRIVACY", "ACCURACY"),
    ("AI as Assistant", "OCR", "TRANS", "HELPER"),
    ("AI Hallucination", "FAKE", "ERROR", "WARNING"),
    ("Synthetic Evidence", "NO", "NEVER", "ETHICS"),
    ("Transparency", "SOURCE", "PROCESS", "TRUST"),
    ("Digital Humanities", "TECH", "HUMANITIES", "FIELD"),
    ("DH Research Flow", "DATA", "ANALYSIS", "INSIGHT"),
    ("Community Education", "LEARN", "PRESERVE", "SHARE"),
    ("School & Heritage", "STUDENT", "PROJECT", "IDENTITY"),
    ("University Partnership", "RESEARCH", "SUPPORT", "ARCHIVE"),
    ("Journalism & Archive", "VERIFY", "CONTEXT", "STORY"),
    ("Future Generations", "2026", "→", "2100"),
    ("Digital Bridge", "PAST", "PRESENT", "FUTURE"),
    ("Memory System", "INPUT", "PROCESS", "OUTPUT"),
    ("Archive Sustainability", "FUNDING", "TECH", "PEOPLE"),
    ("Succession Planning", "WHO?", "HOW?", "CONTINUITY"),
    ("Digital Vault", "SECURE", "ENCRYPT", "PRESERVE"),
    ("Metadata Graph", "ITEM", "LINK", "CONTEXT"),
    ("Evidence Graph", "CLAIM", "SOURCE", "VERIFY"),
    ("Proposed Archive", "ORAKZAI", "DIGITAL", "HERITAGE"),
    ("Archive Roadmap", "PHASE 1", "→", "PHASE 8"),
    ("Discovery Phase", "FIND", "PARTNER", "PHASE 1"),
    ("Pilot Project", "TEST", "LEARN", "PHASE 2"),
    ("Description Phase", "METADATA", "PROV", "PHASE 3"),
    ("Preservation Phase", "MASTERS", "BACKUP", "PHASE 4"),
    ("Search Interface", "DISCOVER", "FILTER", "PHASE 5"),
    ("Public Launch", "SHARE", "RIGHTS", "PHASE 6"),
    ("Governance Model", "REVIEW", "BOARD", "PHASE 7"),
    ("Sustainability Plan", "FUND", "MAINTAIN", "PHASE 8"),
    ("Research Gap", "MISSING", "NEED", "FUTURE"),
    ("Archive Questions", "WHAT?", "WHO?", "WHERE?"),
    ("Author's Reflection", "RESPONSIBILITY", "BRIDGE", "TRUST"),
    ("Final Statement", "PRESERVE", "MEMORY", "FUTURE"),
    ("Digital Integrity", "FIXITY", "NO CHANGE", "TRUST"),
    ("Bit Rot", "DECAY", "DETECT", "REPAIR"),
    ("Media Refresh", "OLD DISK", "→", "NEW DISK"),
    ("Checksum Verification", "HASH", "MATCH", "OK"),
    ("Archive Ingest", "SUBMIT", "CHECK", "STORE"),
    ("Archive Access", "REQUEST", "VERIFY", "DELIVER"),
    ("Metadata Harvesting", "OAI-PMH", "COLLECT", "SHARE"),
    ("Linked Open Data", "URI", "LINK", "WEB"),
    ("IIIF Manifest", "IMAGE", "DATA", "VIEW"),
    ("Future Heritage", "BORN-DIGITAL", "PRESERVE", "LEGACY"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g110-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g110-{index}-title g110-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g110-{index}-title">{safe}</title><desc id="g110-{index}-desc">A digital heritage relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g110-{index}-caption" class="diagram-caption">{index}. {safe} — heritage concept.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Digital Heritage</title><desc id="hero-desc">A visualization of traditional heritage items like photographs and manuscripts transforming into digital archive elements.</desc><defs><linearGradient id="h110-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h110-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(100, 100)" opacity=".6"><rect x="0" y="0" width="120" height="150" fill="#2A2A25" stroke="#B59654"/><text x="60" y="80" text-anchor="middle" fill="#B59654" font-size="10">PHOTO</text></g><g transform="translate(150, 150)" opacity=".7"><rect x="0" y="0" width="120" height="150" fill="#2A2A25" stroke="#B59654"/><text x="60" y="80" text-anchor="middle" fill="#B59654" font-size="10">MANUSCRIPT</text></g><path d="M280 200 L 480 200" stroke="#B59654" stroke-width="2" stroke-dasharray="5 5"/><path d="M480 200 l -10 -5 v 10 z" fill="#B59654"/><g transform="translate(500, 120)"><rect x="0" y="0" width="180" height="200" rx="10" fill="#0B241A" stroke="#2E8B57"/><rect x="20" y="20" width="140" height="20" rx="4" fill="#153B2A"/><rect x="20" y="50" width="140" height="20" rx="4" fill="#153B2A"/><rect x="20" y="80" width="140" height="20" rx="4" fill="#153B2A"/><text x="90" y="150" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="12">DIGITAL ARCHIVE</text><text x="90" y="170" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="10">METADATA • FIXITY • ACCESS</text></g><text x="380" y="50" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">DIGITAL HERITAGE</text><text x="380" y="80" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="12" font-style="italic">“Preserving memory for a generation that has not yet arrived.”</text><g transform="translate(380, 380)" opacity=".8"><circle cx="0" cy="0" r="20" fill="none" stroke="#B59654"/><path d="M-10 0 H 10 M 0 -10 V 10" stroke="#B59654"/><text x="0" y="35" text-anchor="middle" fill="#B59654" font-size="9">FUTURE GENERATION BRIDGE</text></g></svg><figcaption id="hero-caption" class="diagram-caption">Digital Heritage: The transformation of physical memory into preserved, accessible, and authentic digital records.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 110</title>
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
            <p class="section-label">PAGE 110</p>
            <h2>DIGITAL HERITAGE</h2>
            <p>“Preserving memory for a generation that has not yet arrived.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Heritage once depended heavily on what people could carry. A book. A photograph. A letter. A manuscript. A family document. A memory. Today, heritage can also be carried digitally. A photograph can be scanned. A voice can be recorded. A map can be digitized. A manuscript can be photographed in high resolution. An elder’s story can become an audio archive. A family collection can be catalogued. A village memory can be connected to a place on a map.<br><br>
                But digitization alone does not preserve culture. The file must remain understandable. The source must remain identifiable. The context must remain attached. The rights of the people must be respected. And future generations must still be able to open the file. Digital heritage is therefore not simply about technology. It is about responsibility.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">What is Digital Heritage?</h3>
                <p>Digital heritage includes resources of human knowledge and expression that are born digital or converted from physical material. It encompasses cultural, educational, scientific, and administrative records. Technology should preserve evidence, not manufacture history. We distinguish between physical heritage and its digital representation, and between born-digital material and its long-term preservation.</p>
                <p><strong>DIGITAL HERITAGE = EVIDENCE + METADATA + PRESERVATION + ETHICS</strong></p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digitization vs. Digital Preservation</h3>
                <p>Digitization is the process of creating a digital copy. Digital preservation is the ongoing effort to ensure that material remains accessible, authentic, and usable over time. This requires metadata, secure storage, regular fixity checks, and migration to new formats as technology evolves. We follow the <strong>3-2-1 Strategy</strong>: 3 copies, 2 media types, 1 offsite.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Heritage Evidence Matrix</h3>
                <table class="data-table">
                    <thead>
                        <tr><th>Feature</th><th>Standard / Policy</th><th>Source</th><th>Confidence</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Authenticity</td><td>UNESCO Charter</td><td>UNESCO (2003)</td><td>High</td></tr>
                        <tr><td>Preservation Model</td><td>OAIS (ISO 14721)</td><td>ISO / DPC</td><td>High</td></tr>
                        <tr><td>Metadata (Descriptive)</td><td>Dublin Core</td><td>DCMI</td><td>High</td></tr>
                        <tr><td>Metadata (Preservation)</td><td>PREMIS</td><td>Library of Congress</td><td>High</td></tr>
                        <tr><td>Community Ethics</td><td>Indigenous Protocols</td><td>CWIS / Academic Research</td><td>High</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Born-Digital Heritage Risks</h3>
                <p>Born-digital material—such as digital photographs, social media, and websites—can disappear rapidly due to obsolete formats, broken links, hardware failure, or platform shutdowns. Preservation requires proactive management, stable identifiers, and community governance to ensure that today's digital life becomes tomorrow's history.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI and Ethical Preservation</h3>
                <p>AI can assist with OCR, transcription, and metadata, but it must never manufacture history. AI-generated reconstructions must be clearly labeled as such. We maintain a strict boundary between original historical evidence and synthetic visualizations. Human review remains the final authority on cultural authenticity and historical truth.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Digital Heritage</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Proposed Orakzai Digital Heritage Archive</h3>
                <p>We propose a long-term model for an Orakzai digital archive that balances technological rigor with community humility. This involves a roadmap from discovery and pilot projects to full community governance and sustainability. <strong>PROPOSED MODEL — NOT A CLAIM OF AN EXISTING INSTITUTION.</strong></p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“Digital heritage is more than a database; it is a memory system. It is about creating a bridge between the past we inherited and the future we are building. If we build it responsibly, the archive will not merely preserve where we came from. It will help future generations understand who we became. The map, the photograph, and the voice are all layers of a story that is still moving.”</p>
            </div>

            <div class="final-statement">
                PRESERVE THE EVIDENCE.<br>
                PROTECT THE MEMORY.<br>
                BUILD THE FUTURE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>UNESCO, <em>Charter on the Preservation of Digital Heritage</em>, 2003.</li>
                    <li>Digital Preservation Coalition (DPC), <em>Digital Preservation Handbook</em>, 2025.</li>
                    <li>U. Dutta, "Digital Preservation of Indigenous Culture and Narratives," <em>Humanities</em>, 2019.</li>
                    <li>Library of Congress, <em>PREMIS Editorial Committee</em>, 2024.</li>
                    <li>ISO 14721, <em>Space data and information transfer systems — Open archival information system (OAIS) — Reference model</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            110
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

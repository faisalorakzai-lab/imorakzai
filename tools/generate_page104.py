from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-104-future-of-pashto.html'

GRAPHICS = [
    ("What is Pashto?", "IRANIAN BRANCH", "INDO-EUROPEAN", "LIVING LANGUAGE"),
    ("Pashto and Orakzai", "CULTURAL MEDIUM", "IDENTITY", "ORAKZAI EXPRESSION"),
    ("Language as memory", "WORD", "MEANING", "TRANSMITTED IDENTITY"),
    ("Family transmission", "HOME", "PARENTS", "NEXT GENERATION"),
    ("Education", "MOTHER TONGUE", "LITERACY", "KNOWLEDGE ACCESS"),
    ("Mother-tongue education", "UNDERSTANDING", "LITERACY", "ACADEMIC FOUNDATION"),
    ("Literacy", "READING", "WRITING", "ORTHOGRAPHY"),
    ("Pashto script", "PERSO-ARABIC", "MODIFIED CHARACTERS", "LITERARY NORM"),
    ("Unicode", "ENCODING", "FONT", "DIGITAL TEXT"),
    ("Keyboard", "LAYOUT", "INPUT METHOD", "DIGITAL ACCESS"),
    ("Pashto web", "WEBSITES", "BLOGS", "DIGITAL PRESENCE"),
    ("Social media", "VISIBILITY", "COMMUNITY", "NEW DIALECTS"),
    ("Digital Pashto", "TYPE + SEARCH", "WATCH + LISTEN", "VITALITY"),
    ("Media", "RADIO + TV", "JOURNALISM", "CONTEMPORARY VOICE"),
    ("Literature", "POETRY + PROSE", "NOVELS", "WRITTEN HERITAGE"),
    ("Poetry", "VOICE", "BOOK", "DIGITAL ARCHIVE"),
    ("Storytelling", "ORAL TRADITION", "PODCAST", "DOCUMENTARY"),
    ("Proverbs", "CULTURAL WISDOM", "CONTEXT", "TRANSMISSION"),
    ("Music", "LYRICS", "RECORDING", "IDENTITY REINFORCEMENT"),
    ("Attan", "MOVEMENT", "MUSIC", "IDENTITY PERFORMANCE"),
    ("Religion", "INSTRUCTION", "SERMONS", "COMMUNITY LANGUAGE"),
    ("Hospitality", "VOCABULARY", "POLITENESS", "SOCIAL VALUES"),
    ("Migration", "MAINTENANCE", "SHIFT", "MULTILINGUALISM"),
    ("Cities", "URBAN DOMAINS", "CODE-SWITCHING", "HYBRID IDENTITY"),
    ("Diaspora", "HOME LANGUAGE", "COMMUNITY", "GLOBAL NETWORK"),
    ("Language shift", "DOMAIN LOSS", "INTERFERENCE", "LANGUAGE CHANGE"),
    ("Language maintenance", "USE + LITERACY", "MEDIA + DIGITAL", "VITALITY"),
    ("Language vitality", "TRANSMISSION", "DOMAINS", "INSTITUTIONAL SUPPORT"),
    ("Dialect diversity", "REGIONAL VARIETY", "VOCABULARY", "LIVING RICHNESS"),
    ("Orakzai dialect research", "PRONUNCIATION", "LOCAL WORDS", "DOCUMENTATION NEED"),
    ("Pashto + English", "BILINGUALISM", "ACCESS", "MULTILINGUAL FUTURE"),
    ("Pashto + Urdu", "NATIONAL DOMAINS", "BILINGUALISM", "PAKISTAN CONTEXT"),
    ("Afghanistan", "OFFICIAL STATUS", "EDUCATION", "NATIONAL IDENTITY"),
    ("Pakistan", "REGIONAL STATUS", "EDUCATION", "DIVERSE DOMAINS"),
    ("Language policy", "EDUCATION", "MEDIA", "INSTITUTIONAL SUPPORT"),
    ("Science and technology", "TRANSLATION", "LOCALIZATION", "TECHNICAL PASHTO"),
    ("Technical vocabulary", "COMPUTING", "AI", "TERMINOLOGY NEED"),
    ("AI", "NLP", "TRANSCRIPTION", "ARCHIVE ASSISTANCE"),
    ("Low-resource language", "LIMITED DATA", "ANNOTATION NEED", "NLP CHALLENGE"),
    ("Corpus", "TEXT + ANNOTATION", "METADATA", "RESEARCH DATA"),
    ("Speech recognition", "VOICE TO TEXT", "DIALECT DATA", "ACCESSIBILITY"),
    ("Machine translation", "CROSS-LANGUAGE", "CONTEXT NEED", "TOOL ASSISTANCE"),
    ("AI authenticity", "SOURCE", "AI TOOL", "HUMAN REVIEW"),
    ("Digital dictionary", "SEARCHABLE", "REGIONAL VARIANT", "PRONUNCIATION"),
    ("Spellchecking", "CONSISTENCY", "TYPING", "LITERACY SUPPORT"),
    ("OCR", "SCAN", "TEXT EXTRACTION", "SEARCHABLE ARCHIVE"),
    ("Digital publishing", "E-BOOKS", "WEB NEWS", "EXPANDED ACCESS"),
    ("Children", "STORY", "LANGUAGE", "IMAGINATION"),
    ("Educational technology", "INTERACTIVE", "VIDEO", "DIGITAL LEARNING"),
    ("Youth", "SLANG", "MEDIA", "CONTENT CREATION"),
    ("Women", "FAMILY", "STORYTELLING", "TRANSMISSION ROLE"),
    ("Elders", "VOCABULARY", "PRONUNCIATION", "LIVING ARCHIVE"),
    ("Cultural memory", "STORY + POETRY", "FOOD + PLACE", "IDENTITY"),
    ("Global Pashto", "HOMELAND", "OVERSEAS", "DIGITAL CONNECTION"),
    ("Internet", "CONNECTION", "VISIBILITY", "RISK MANAGEMENT"),
    ("Content creation", "YOUTUBE", "PODCAST", "DIGITAL VOICE"),
    ("Gaming", "INTERFACE", "STORYTELLING", "FUTURE POSSIBILITY"),
    ("Software", "LOCALIZATION", "INTERFACE", "USER ACCESS"),
    ("Accessibility", "TTS + STT", "SCREEN READER", "INCLUSIVE DESIGN"),
    ("Digital economy", "CONTENT", "TRANSLATION", "OPPORTUNITY"),
    ("Continuity scenario", "TRANSMISSION", "HOME USE", "STABILITY"),
    ("Adaptation scenario", "HYBRIDITY", "DIGITAL", "RESILIENCE"),
    ("Fragmentation scenario", "DOMAIN LOSS", "SHIFT", "VULNERABILITY"),
    ("Strong Pashto future", "SCHOOL + BOOKS", "ONLINE + TECH", "VITALITY"),
    ("Preservation", "PRIORITY", "METHOD", "LEGACY"),
    ("Future creation", "DICTIONARIES", "CORPORA", "TECH TOOLS"),
    ("Ethical warnings", "CONSENT", "ACCURACY", "RIGHTS"),
    ("Digital future", "VOICE + TEXT", "ARCHIVE", "GLOBAL ACCESS"),
    ("Orakzai future", "YOUTH", "TECH", "POSSIBILITY"),
    ("Research gap", "DIALECTS", "NLP DATA", "DOCUMENTATION"),
    ("Oral-history questions", "ELDER STORIES", "YOUTH USE", "FUTURE VISION"),
    ("Author reflection", "ADAPTATION", "LIVING", "FUTURE"),
    ("Final statement", "USE", "PEOPLE", "CONTINUITY"),
    ("Voice-to-text", "AUDIO", "TRANSCRIPTION", "DIGITAL TEXT"),
    ("Pashto corpus", "NEWS", "LITERATURE", "SOCIAL MEDIA"),
    ("Language technology", "OCR", "MT", "SPELLCHECK"),
    ("Multilingual identity", "PASHTO", "URDU/ENGLISH", "HYBRID BELONGING"),
    ("Future child", "LISTEN", "LEARN", "SPEAK"),
    ("Digital access", "PHONE", "LAPTOP", "INTERNET"),
    ("Pashto education", "SCHOOL", "BOOK", "LITERACY"),
    ("Pashto media", "VIDEO", "AUDIO", "TEXT"),
    ("Global diaspora", "GULF", "EUROPE", "AMERICAS"),
    ("2050 scenario", "POSSIBILITY", "CHANGE", "CONTINUITY"),
    ("Language continuity", "PAST", "PRESENT", "FUTURE"),
    ("Digital legacy", "DOCUMENT", "PRESERVE", "PASS FORWARD"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g104-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g104-{index}-title g104-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g104-{index}-title">{safe}</title><desc id="g104-{index}-desc">A three-stage conceptual relationship: {left}, {center}, and {right}. This is a linguistic framework.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g104-{index}-caption" class="diagram-caption">{index}. {safe} — linguistic framework.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">The Future of Pashto</title><desc id="hero-desc">A mountain landscape flowing into a digital world. Left: mountains, elder, manuscript. Center: youth, school, phone. Right: laptop, digital library, AI interface.</desc><defs><linearGradient id="h104-bg" x1="0" x2="1"><stop stop-color="#123B2A"/><stop offset=".5" stop-color="#1B1B18"/><stop offset="1" stop-color="#202B35"/></linearGradient><linearGradient id="h104-path" x1="0" x2="1"><stop stop-color="#2E8B57"/><stop offset="1" stop-color="#B59654"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h104-bg)" stroke="#B59654" stroke-opacity=".55"/><path d="M24 286 L104 150 L152 210 L222 110 L320 286Z" fill="#0B241A" stroke="#2E8B57" stroke-opacity=".55"/><path d="M440 286 V226 H472 V286 H490 V180 H526 V286 H544 V142 H585 V286 H606 V198 H642 V286 H660 V160 H736 V386 H440Z" fill="#111B24" stroke="#7894A8" stroke-opacity=".62"/><path d="M176 330 C245 290 286 332 336 286 C382 244 428 262 485 294 C548 329 610 288 710 314" fill="none" stroke="url(#h104-path)" stroke-width="9" stroke-linecap="round"/><g transform="translate(100, 300)" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="12">VOICE</text></g><g transform="translate(350, 250)" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="12">EDUCATION</text></g><g transform="translate(600, 200)" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="12">DIGITAL FUTURE</text></g><g font-family="Arial,sans-serif" text-anchor="middle"><text x="380" y="380" fill="#B59654" font-size="10" letter-spacing="1.3">VOICE → TEXT → EDUCATION → MEDIA → DIGITAL → FUTURE</text></g></svg><figcaption id="hero-caption" class="diagram-caption">The Future of Pashto: A living language connecting ancestral roots to a digital world.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 104</title>
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
            <p class="section-label">PAGE 104</p>
            <h2>THE FUTURE OF PASHTO</h2>
            <p>“A living language needs a future in which it can be spoken, written, taught, created and understood.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “A language does not survive because it belongs to the past.<br><br>
                It survives because people continue to use it. They speak it at home. They teach it to children. They write it. They sing it. They tell stories in it. They argue, joke, pray, work and dream in it.<br><br>
                Pashto has carried generations of memory across mountains, settlements, cities and borders. Its future, however, will not be decided by history alone. It will be shaped by schools, families, literature, media, migration, technology and the choices of young people.<br><br>
                The question is therefore not simply whether Pashto has a past. It does. The more important question is whether Pashto will remain fully usable in the future worlds its speakers are entering.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">What is Pashto?</h3>
                <p>Pashto is an Eastern Iranian language of the Indo-Iranian branch of the Indo-European language family. It is spoken by millions primarily in Afghanistan (where it is a national language) and Pakistan (where it is a major regional language in Khyber Pakhtunkhwa and northern Balochistan), as well as by significant diaspora communities worldwide. While it shares a common identity, Pashto contains significant dialect diversity across its geographic range.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pashto and Orakzai</h3>
                <p>Pashto is the central medium of Orakzai cultural expression, connecting to the proverbs (Page 63), music (Page 61), and oral traditions (Page 65) discussed throughout this book. While Orakzai speakers participate in the broader Pashto linguistic world, local variations in pronunciation and vocabulary reflect the district's specific history and landscape.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Family and Transmission</h3>
                <p>Intergenerational transmission within the family is the primary site of language vitality. Research indicates that while Pashto remains the preferred home language for many, urban environments and migration (Pages 89, 90, 99) introduce multilingual hybridity, where Urdu and English are used for social mobility and education while Pashto maintains its role in home and community identity.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pashto in Education</h3>
                <p>Language policy and education are critical to the future of literacy. Mother-tongue education provides a stronger cognitive foundation for early learning, yet its implementation varies across borders. In Pakistan, Pashto is taught as a subject in KP schools, while in Afghanistan, its status as an official language grants it a broader role in formal instruction.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Pashto: Unicode and Beyond</h3>
                <p>For a language to survive in the modern world, it must be digitally accessible. This requires standard Unicode encoding, reliable fonts, and functional keyboards across all devices. Pashto is currently classified in computational linguistics as a "low-resource" language, meaning it lacks the massive datasets available for languages like English, but recent research in NLP (Natural Language Processing) is closing this gap.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI and the Future of Heritage</h3>
                <p>Artificial Intelligence offers transformative possibilities for Pashto, including speech recognition, machine translation, and OCR (Optical Character Recognition). However, AI is a tool, not a source of authenticity. We do not automatically assume AI output is correct. Human review is essential to ensure that AI-generated content does not fabricate history or erase linguistic nuance. We do not claim that technology can independently preserve culture; evidence is limited regarding AI's ability to capture deep cultural context. AI-generated text is not evidence of historical truth.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Linguistic Claim Matrix</h3>
                <table class="data-table">
                    <thead>
                        <tr><th>Claim</th><th>Language Scope</th><th>Evidence</th><th>Source</th><th>Confidence</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Home Dominance</td><td>Pashto</td><td>Urban Pakistan Study</td><td>Khalid (2026)</td><td>High</td></tr>
                        <tr><td>Low-Resource Status</td><td>Pashto</td><td>NLP Benchmarks</td><td>Haq (2023)</td><td>High</td></tr>
                        <tr><td>Multilingual Hybridity</td><td>Pashto/Urdu/English</td><td>Sociolinguistic Research</td><td>Nature (2026)</td><td>High</td></tr>
                        <tr><td>Digital Archiving Need</td><td>Pashto</td><td>UNESCO Framework</td><td>UNESCO (2021)</td><td>High</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Future Scenarios</h3>
                <div class="atlas-grid">
                    <div class="reflection-box" style="margin: 0;">
                        <h4 style="color: var(--gold);">1. Continuity</h4>
                        <p>Strong intergenerational transmission; Pashto remains the dominant home and community language.</p>
                    </div>
                    <div class="reflection-box" style="margin: 0;">
                        <h4 style="color: var(--gold);">2. Adaptation</h4>
                        <p>Pashto remains strong but becomes increasingly multilingual and digitally hybrid.</p>
                    </div>
                    <div class="reflection-box" style="margin: 0;">
                        <h4 style="color: var(--gold);">3. Fragmentation</h4>
                        <p>Domains shift toward other languages; Pashto remains concentrated in specific social settings.</p>
                    </div>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: The Future of Pashto</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Research Gap: What Still Needs to be Documented</h3>
                <ul style="columns: 2;">
                    <li>Orakzai-specific dialect research</li>
                    <li>Village-level vocabulary</li>
                    <li>Pronunciation variations</li>
                    <li>Kinship terminology</li>
                    <li>Agricultural vocabulary</li>
                    <li>Place names</li>
                    <li>Oral histories</li>
                    <li>Children's language use</li>
                    <li>Women's language experiences</li>
                    <li>Urban Orakzai language use</li>
                    <li>Diaspora language maintenance</li>
                    <li>Pashto digital corpora</li>
                    <li>Speech datasets</li>
                    <li>OCR performance</li>
                    <li>Machine-translation quality</li>
                    <li>Digital dictionaries</li>
                    <li>Educational resources</li>
                    <li>Technical terminology</li>
                    <li>Accessibility tools</li>
                    <li>Social-media language change</li>
                </ul>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Oral History Questions</h3>
                <ol style="columns: 2;">
                    <li>What Pashto words did your grandparents use that young people rarely use today?</li>
                    <li>Which words are unique to your village or region?</li>
                    <li>How did your family teach children Pashto?</li>
                    <li>Did migration change the language spoken at home?</li>
                    <li>Which Pashto books did you read?</li>
                    <li>Which poets influenced your family?</li>
                    <li>Which proverbs were commonly used?</li>
                    <li>Which stories were told to children?</li>
                    <li>How has social media changed Pashto writing?</li>
                    <li>Do young people mix Pashto with Urdu or English?</li>
                    <li>Which Pashto words should be documented?</li>
                    <li>What should schools teach in Pashto?</li>
                    <li>What Pashto content do children need?</li>
                    <li>What technology would make Pashto easier to use?</li>
                    <li>Which dialect differences should researchers document?</li>
                    <li>What should be preserved from today's Pashto?</li>
                    <li>What should change naturally?</li>
                    <li>What should never be fabricated?</li>
                    <li>How can diaspora families maintain Pashto?</li>
                    <li>What should Pashto look like in 2050?</li>
                </ol>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“I do not think the future of Pashto should be imagined as a choice between tradition and modernity. A language does not have to remain unchanged to remain itself. Pashto can live in a village and a city. It can live in a hujra and on a smartphone. It can live in poetry and in software. It can be spoken by an elder and learned by a child thousands of kilometres away.<br><br>
                The challenge is not to prevent change. Languages have always changed. The challenge is to make sure that change does not mean losing the ability to speak, write, create, remember and learn in Pashto. If the next generation can use Pashto to tell stories, study, create technology, make art, build businesses, communicate online and express its deepest memories, then the language is not merely surviving. It is living. And a living language can have a future.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF PASHTO WILL NOT BE WRITTEN BY TECHNOLOGY ALONE.<br>
                IT WILL BE WRITTEN BY THE PEOPLE WHO CONTINUE TO USE IT.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Khalid, A., et al., "Family language policy and identity formation among migrant Pashto community in Lahore," <em>HSS Comms</em>, 2026.</li>
                    <li>Haq, I., et al., "NLPashto: NLP Toolkit for Low-resource Pashto Language," <em>IJACSA</em>, 2023.</li>
                    <li>Ali, I., et al., "Monolingual Paraphrase Detection Corpus for Low Resource Pashto Language," <em>LREC-COLING</em>, 2024.</li>
                    <li>UNESCO, <em>Guidelines for the Preservation of Digital Heritage</em>, 2021.</li>
                    <li>Spolsky, B., <em>Language Policy</em>, Cambridge University Press, 2004.</li>
                    <li>Rahman, T., <em>Language and Politics in Pakistan</em>, Oxford University Press, 2006.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            104
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

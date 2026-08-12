from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-169-building-for-the-next-generation.html'

GRAPHICS = [
    ("Next Gen Build", "NOW", "↔", "NEXT"),
    ("Starting Point", "PAST", "→", "NEW"),
    ("System Inherit", "ALL", "→", "NEXT"),
    ("Digital Infra", "GRID", "↔", "TIME"),
    ("Future Success", "HERE", "→", "LONG"),
    ("Beyond Present", "NOW", "≠", "LONG"),
    ("Intergen Think", "ONE", "↔", "ALL"),
    ("Legacy Definition", "DONE", "↔", "LONG"),
    ("Durability Path", "BASE", "↔", "LONG"),
    ("Strong Foundation", "BASE", "↔", "ALL"),
    ("Institution Serve", "ALL", "↔", "LONG"),
    ("Beyond Founder", "ONE", "→", "ALL"),
    ("Succession Plan", "NOW", "→", "NEXT"),
    ("Knowledge Transfer", "WISE", "→", "LEAR"),
    ("Documentation Rail", "DOC", "↔", "SAVE"),
    ("Digital Memory", "DATA", "↔", "SAVE"),
    ("Preserve History", "PAST", "↔", "SAFE"),
    ("Cultural Heritage", "PASH", "↔", "SAVE"),
    ("Orakzai Heritage", "ORAK", "↔", "SAVE"),
    ("Digital Heritage", "DATA", "↔", "PASH"),
    ("Oral History Rail", "TALK", "↔", "SAVE"),
    ("Tech Memory", "TECH", "↔", "SAVE"),
    ("Knowledge Archive", "WISE", "↔", "SAVE"),
    ("Open Access Rail", "OPEN", "↔", "ALL"),
    ("Privacy Consent", "YES", "↔", "DATA"),
    ("Digital Security", "SEC", "↔", "SAVE"),
    ("Backup Strategy", "TWO", "↔", "ONE"),
    ("Format Pres", "FILE", "↔", "TIME"),
    ("Metadata Search", "DATA", "↔", "FIND"),
    ("Searchable Hist", "FIND", "↔", "WISE"),
    ("Mapping History", "MAP", "↔", "PAST"),
    ("Digital Maps", "MAP", "↔", "DATA"),
    ("Resp Mapping", "MAP", "↔", "SAFE"),
    ("Edu Access", "LEAR", "↔", "ALL"),
    ("Digital Edu", "LEAR", "↔", "NET"),
    ("AI Edu Support", "AI", "→", "LEAR"),
    ("Tech Literacy", "KNOW", "↔", "TECH"),
    ("CS Foundation", "CODE", "↔", "BASE"),
    ("Coding Creativity", "CODE", "↔", "ART"),
    ("Digital Create", "MAKE", "↔", "ALL"),
    ("Research Invest", "SCI", "↔", "GROW"),
    ("Scientific Think", "FACT", "↔", "WISE"),
    ("Critical Think", "WHY", "↔", "TRUE"),
    ("Digital Literacy", "KNOW", "↔", "NET"),
    ("Cybersec Awareness", "SEC", "↔", "KNOW"),
    ("Digital Identity", "SELF", "↔", "NET"),
    ("Privacy Design", "SELF", "↔", "SAFE"),
    ("Data Rights Rail", "OWN", "↔", "DATA"),
    ("Responsible AI", "AI", "↔", "SAFE"),
    ("AI Governance", "RULE", "↔", "AI"),
    ("Human-Centered", "USER", "↔", "NEED"),
    ("Automation Shift", "AUTO", "↔", "WORK"),
    ("Future of Work", "WORK", "↔", "TECH"),
    ("Lifelong Learn", "TIME", "↔", "LEAR"),
    ("Future Skills", "KNOW", "↔", "DONE"),
    ("Entr Opportunity", "IDEA", "→", "DONE"),
    ("Young Founders", "YOUN", "→", "LEAD"),
    ("Mentorship Rail", "WISE", "→", "YOUN"),
    ("Capital Access", "CASH", "↔", "GROW"),
    ("Local Entr", "HERE", "→", "FIX"),
    ("Global Entr", "HERE", "→", "GLOB"),
    ("Pakistan to World", "HOME", "→", "GLOB"),
    ("Digital Exports", "CODE", "→", "GLOB"),
    ("Global Talent", "BEST", "↔", "TEAM"),
    ("Diaspora Link", "DIAS", "↔", "HOME"),
    ("Know Networks", "WISE", "↔", "LINK"),
    ("Open Source Rail", "OPEN", "↔", "CODE"),
    ("Digital Collab", "ALL", "↔", "LINK"),
    ("Future Companies", "NEW", "↔", "GLOB"),
    ("Digital Infra", "GRID", "↔", "BASE"),
    ("Cloud Computing", "GRID", "↔", "USER"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g169-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g169-{index}-title g169-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g169-{index}-title">{safe}</title><desc id="g169-{index}-desc">A building for the next generation relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g169-{index}-caption" class="diagram-caption">{index}. {safe} — Building for the next generation relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Building for the Next Generation Framework</title><desc id="hero-desc">A diagram showing the intergenerational pathway from today's foundations to tomorrow's legacy, featuring digital preservation, knowledge transfer, and institutional resilience.</desc><defs><linearGradient id="h169-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h169-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE INTERGENERATIONAL LEGACY LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DIGITAL PRESERVATION: SECURING HERITAGE (2026)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">KNOWLEDGE TRANSFER & INSTITUTIONAL MEMORY</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">LIFELONG LEARNING & FUTURE SKILLS (AI LITERACY)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SUSTAINABLE INFRASTRUCTURE: GRID & CLOUD</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">AI GOVERNANCE & HUMAN-CENTERED DESIGN</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN LEGACY: PAST TO FUTURE</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">LEGACY: KNOWLEDGE, INSTITUTIONS & OPPORTUNITY</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">BUILDING FOR THE NEXT GENERATION</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“What We Build Today Becomes the Starting Point for Tomorrow.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Intergenerational Legacy Loop: Securing cultural heritage through digital preservation, ensuring knowledge transfer, and building resilient institutions for the 2026 digital era.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 169</title>
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
            <p class="section-label">PAGE 169</p>
            <h2>BUILDING FOR THE NEXT GENERATION</h2>
            <p>“What We Build Today Becomes the Starting Point for Tomorrow.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Every generation inherits systems built by the generations before it. Roads, universities, businesses, technologies, institutions, cultural traditions and knowledge all become part of the environment in which the next generation grows. The same principle applies to the digital age. The infrastructure being created today will influence how future generations communicate, learn, work, govern, trade and create. Building for the next generation therefore requires thinking beyond immediate success. It means asking: Will what we build remain useful after we are gone?”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Digital Preservation & Heritage (2026)</h3>
                <p>The *Digital Preservation Summit 2026* emphasized the urgency of securing cultural heritage in the digital age. By 2026, the digital preservation of intangible cultural heritage (ICH) has become a vital strategy for sustaining cultural diversity [1]. For the Orakzai community, this involves transforming fragile oral traditions, family histories, and languages into accessible digital collections using knowledge graph-driven strategies [2] [3]. Digitization ensures that the next generation can understand their origins through searchable, map-based archives that respect community privacy and consent [4] [5].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Institutional Memory & Knowledge Transfer</h3>
                <p>The ultimate test of a long-term organization is its ability to continue beyond its original founders. Durability requires strong foundations in people, systems, values, and infrastructure [6]. By converting individual experience into documented institutional memory, builders protect the knowledge that future leaders will need. Succession planning and mentorship are critical; experienced entrepreneurs must help younger founders avoid unnecessary mistakes while providing access to international capital and networks [7] [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Future Skills & Lifelong Learning</h3>
                <p>Future citizens will live alongside increasingly capable AI systems, requiring a foundation in computer science, coding, and digital literacy. By 2026, education has extended beyond childhood, with lifelong learning becoming the norm as technology transforms work [9]. Skills such as critical thinking, creativity, and AI literacy are essential for navigating a digital landscape where information is abundant but requires rigorous evaluation [10]. Human-centered technology design ensures that these tools support human needs rather than treating people as mere data points [11].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Sovereign Infrastructure & Global Reach</h3>
                <p>Building for tomorrow means investing in sustainable digital infrastructure, including cloud computing and sovereign grids. These platforms provide the flexible resources that future businesses depend on to reach global customers [12]. A company founded in Pakistan and developed by local talent can serve the world, provided it adheres to international standards of governance and security. By mastering these systems today, we create the starting point from which the next generation of Orakzai builders will thrive [13].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Building for the Next Generation</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, legacy is the bridge between our ancient resilience and our digital future. We do not build for ourselves alone; we build for those who will follow. By securing our heritage, transferring our knowledge, and building resilient institutions, we are ensuring that our dignity and strength endure. We are the architects of a sovereign tomorrow.”</p>
            </div>

            <div class="final-statement">
                BUILD TO ENDURE.<br>
                SERVE TO LAST.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Henry Stewart Events, <em>Digital Preservation Summit 2026: Securing Cultural Heritage (February 2026)</em>.</li>
                    <li>Nature Humanities and Social Sciences Communications, <em>Knowledge Graph-Driven Digital Preservation of ICH (2026)</em>.</li>
                    <li>IFLA, <em>Digital Cultural Heritage: Preservation, Sustainability, and Public Engagement (July 2026)</em>.</li>
                    <li>UNESCO, <em>Advancing Access to Information and Digital Preservation (July 2024)</em>.</li>
                    <li>ICCROM, <em>Sustaining Digital Heritage: Complexity and Rights Management (2026)</em>.</li>
                    <li>OECD, <em>Digital Government Outlook 2026: Building Human-Centred Services (June 2026)</em>.</li>
                    <li>New America, <em>Infrastructure for the Digital Age: Building a Resilient Ecosystem (2026)</em>.</li>
                    <li>MDPI, <em>Leading in the Digital Age: The Role of Institutional Leadership (2025)</em>.</li>
                    <li>ACT, <em>Technology Trends Report 2026: AI, Data, and Human Impact (2026)</em>.</li>
                    <li>In-Tandem, <em>Technology Through a Multi-Generational Lens (January 2025)</em>.</li>
                    <li>Assurant, <em>2026 Global Connected Consumer Trends Report (July 2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Long-Term Institutional Building and Sovereign Infrastructure (August 2026)</em>.</li>
                    <li>Growing Up in the Digital Age Summit, <em>Collaborating to Protect and Empower Future Generations (2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            169
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

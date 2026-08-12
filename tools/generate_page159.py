from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-159-technology-and-human-development.html'

GRAPHICS = [
    ("Human Capability", "USER", "↔", "ABLE"),
    ("Technology Tool", "TOOL", "↔", "DONE"),
    ("Human Progress", "TIME", "→", "LIFE"),
    ("Capability Expand", "KNOW", "→", "ABLE"),
    ("Social Outcome", "IDEA", "↔", "LIFE"),
    ("Human Need Path", "WANT", "→", "DONE"),
    ("Knowledge Base", "READ", "↔", "WISE"),
    ("Digital Age Rail", "NET", "↔", "TIME"),
    ("Internet Impact", "GLOB", "↔", "LINK"),
    ("Cloud Capacity", "CLOU", "↔", "BASE"),
    ("AI Expansion", "AI", "↔", "WISE"),
    ("Blockchain Coordination", "BC", "↔", "LINK"),
    ("Biotech Impact", "LIFE", "↔", "SCI"),
    ("Robotics Extension", "ROBO", "↔", "BODY"),
    ("Human Development", "ALL", "↔", "LIFE"),
    ("Equality Goal", "ONE", "↔", "ONE"),
    ("Connectivity Path", "LINK", "↔", "ALL"),
    ("Dignity Rail", "SELF", "↔", "SAFE"),
    ("Resilience Rail", "HARD", "↔", "SAFE"),
    ("Health Improvement", "DOC", "↔", "LIFE"),
    ("Education Expand", "LEAR", "↔", "WISE"),
    ("Income Potential", "CASH", "↔", "VALU"),
    ("Living Condition", "HOME", "↔", "LIFE"),
    ("Participation Rail", "TALK", "↔", "ALL"),
    ("Information Access", "DATA", "↔", "USER"),
    ("Remote Student", "ONE", "↔", "NET"),
    ("Digital Book", "READ", "↔", "CODE"),
    ("Online Lecture", "TALK", "↔", "NET"),
    ("Scientific Paper", "SCI", "↔", "CODE"),
    ("Knowledge Economy", "WISE", "↔", "CASH"),
    ("Digital Literacy", "USER", "↔", "CODE"),
    ("Life Skill Rail", "LIFE", "↔", "CODE"),
    ("Digital Divide", "HAVE", "≠", "NOT"),
    ("Affordability Path", "CASH", "↔", "LINK"),
    ("Universal Connect", "ALL", "↔", "NET"),
    ("Mobile Access", "USER", "↔", "APP"),
    ("Navigation Path", "MAP", "↔", "APP"),
    ("Rural Connectivity", "FARM", "↔", "NET"),
    ("Remote Community", "VALY", "↔", "NET"),
    ("Digital Classroom", "ROOM", "↔", "NET"),
    ("Online Learning", "LEAR", "↔", "HOME"),
    ("AI Tutoring", "AI", "→", "USER"),
    ("Digital Library", "BOOK", "↔", "CLOU"),
    ("Personalized Learn", "USER", "↔", "AI"),
    ("Language Tech", "TALK", "↔", "CODE"),
    ("Pashto Digital", "PASH", "↔", "CODE"),
    ("Pashto Typing", "TYPE", "↔", "PASH"),
    ("Pashto Speech", "TALK", "↔", "PASH"),
    ("Pashto Preservation", "SAVE", "↔", "PASH"),
    ("Cultural Archive", "PAST", "→", "CODE"),
    ("Digital Humanities", "LIFE", "↔", "DATA"),
    ("Archaeology Tech", "OLD", "↔", "DATA"),
    ("Anthropology Tech", "PEOP", "↔", "DATA"),
    ("Healthcare Transform", "DOC", "↔", "NET"),
    ("Electronic Record", "FILE", "↔", "NET"),
    ("Telemedicine Path", "DOC", "↔", "USER"),
    ("Remote Healthcare", "AWAY", "↔", "DOC"),
    ("Medical Imaging", "EYE", "↔", "DATA"),
    ("AI in Medicine", "AI", "↔", "DOC"),
    ("Wearable Tech", "WEAR", "↔", "LIFE"),
    ("Health Data Rail", "DATA", "↔", "LIFE"),
    ("Public Health Rail", "ALL", "↔", "SAFE"),
    ("Pandemic Response", "WARN", "↔", "NET"),
    ("Agri Transform", "FARM", "↔", "TECH"),
    ("Precision Farming", "DATA", "→", "GROW"),
    ("Soil Sensor", "SOIL", "→", "DATA"),
    ("Drone Agri", "FLY", "→", "DATA"),
    ("Satellite Agri", "SKY", "→", "DATA"),
    ("AI in Farming", "AI", "→", "FARM"),
    ("Food Security", "FOOD", "↔", "SAFE"),
    ("Water Management", "WATR", "↔", "SAFE"),
    ("Clean Water Rail", "PURE", "↔", "SAFE"),
    ("Energy Access", "POWR", "↔", "ALL"),
    ("Renewable Energy", "SUN", "↔", "POWR"),
    ("Smart Grid Rail", "GRID", "↔", "CODE"),
    ("Energy Efficiency", "POWR", "↔", "SAFE"),
    ("Rural Energy", "VALY", "↔", "POWR"),
    ("Economic Opportunity", "JOB", "↔", "NET"),
    ("Remote Work Path", "HOME", "↔", "JOB"),
    ("Digital Commerce", "SHOP", "↔", "NET"),
    ("Software Dev Rail", "CODE", "↔", "JOB"),
    ("HDI Focus 2026", "HDI", "↔", "CODE"),
    ("Divide Narrowing", "HAVE", "↔", "NOT"),
    ("Personalized Education", "USER", "↔", "AI"),
    ("E-Health Framework", "GOV", "↔", "DOC"),
    ("Remote Clinic", "VALY", "↔", "DOC"),
    ("Digital Skill Path", "LEAR", "→", "DONE"),
    ("Geographic Leap", "VALY", "→", "CITY"),
    ("Pashto Future", "PASH", "↔", "TIME"),
    ("Orakzai Progress", "ORAK", "↔", "LIFE"),
    ("Valley Classroom", "ORAK", "↔", "LEAR"),
    ("Valley Clinic", "ORAK", "↔", "DOC"),
    ("Future Rail", "TIME", "↔", "NEW"),
    ("Sovereign Human", "OWN", "↔", "NATL"),
    ("Inclusive Progress", "ALL", "↔", "LIFE"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
    ("Growth Growth", "GROW", "↔", "GROW"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g159-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g159-{index}-title g159-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g159-{index}-title">{safe}</title><desc id="g159-{index}-desc">A technology and human development relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g159-{index}-caption" class="diagram-caption">{index}. {safe} — Technology and human development relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Technology & Human Development Framework</title><desc id="hero-desc">A diagram showing the 2026 human development engine, including AI education, E-health frameworks, digital literacy, and rural connectivity rails.</desc><defs><linearGradient id="h159-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h159-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE HUMAN DEVELOPMENT ENGINE (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AI EDUCATION (Personalized Learning)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">E-HEALTH FRAMEWORK (Telemedicine 2030)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">DIGITAL LITERACY (Basic Life Skill Program)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">RURAL CONNECTIVITY (Narrowing the Divide)</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CULTURAL PRESERVATION (Pashto Digital)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">REMOTE CLINICS & VIRTUAL CLASSROOMS</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SOVEREIGN HUMANITY (EMPOWER → THRIVE)</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">TECHNOLOGY & HUMAN DEVELOPMENT</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“How Technology Shapes Human Progress.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Human Development Engine: The 2026 stack of digital education, e-health, literacy, and the empowerment of individuals through technology.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 159</title>
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
            <p class="section-label">PAGE 159</p>
            <h2>TECHNOLOGY & HUMAN DEVELOPMENT</h2>
            <p>“How Technology Shapes Human Progress.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Technology is more than machines and software; it is a tool for expanding human capability. At its most important level, technological change influences how people learn, work, and access healthcare. The modern digital era has accelerated this transformation, but progress is not automatic. Human development requires a larger objective: technology must expand capability, opportunity, dignity, and resilience for all.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">AI & The Future of Education</h3>
                <p>In 2026, Pakistan is responding to a historic shift in global workforce skills. With nearly **40% of skills** expected to change by 2030, the nation has integrated **AI-powered personalized learning** into its digital classrooms. These systems adapt learning materials to individual student needs, providing high-quality tutoring to youth in both urban centers and remote communities. This transition to a knowledge-based economy ensures that the next generation is prepared for the AI-driven future.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">E-Health & Remote Healthcare</h3>
                <p>The **National Digital Health Framework 2022–2030** is transforming how Pakistanis access medical care. By mid-2026, telemedicine and mobile health interventions are being progressively embedded into the public health system. Electronic health records and advanced medical imaging process data in real-time, allowing clinicians to make informed decisions. For distant regions, remote clinics provide a lifeline, connecting patients with specialists through secure digital rails.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Literacy as a Basic Life Skill</h3>
                <p>In the digital age, literacy extends beyond reading and writing. In 2026, digital literacy is framed as a **basic life skill**, encompassing the ability to use digital tools, evaluate information, and protect digital identities. National programs led by PKCERT and UNESCO are training millions of citizens in these essentials, ensuring that technological progress does not create new classes of digital inequality but instead serves as a tool for national inclusion.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Orakzai Geographic Leapfrog</h3>
                <p>For the Orakzai community, technology is the primary catalyst for human progress. Through **Virtual Classrooms** and **Remote Health Clinics**, valley natives are bypassing geographic barriers to access world-class education and healthcare. This "Geographic Leapfrogging" ensures that human development in Orakzai keeps pace with the rest of the nation. By preserving the **Pashto language** through digital speech and translation tools, technology is also securing the tribe's cultural heritage for the digital future.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Technology & Human Development</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Capability is the true currency of the digital age. For the Orakzai people, technology is our equalizer. It allows a student in a remote valley to learn from the best minds in the world and a family in a distant village to receive the best medical care. We are building a nation where geography is no longer a limit to potential. We are creating a sovereign future where every citizen is empowered to thrive through the power of digital intelligence.”</p>
            </div>

            <div class="final-statement">
                CAPABILITY EXPANDED.<br>
                POTENTIAL UNLOCKED.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>UNDP / BTI Transformation Index, <em>Pakistan Country Report 2026: Socioeconomic Development (April 2026)</em>.</li>
                    <li>UNESCO / World Economic Forum, <em>Empowering Educators for an AI-Driven Future (January 2026)</em>.</li>
                    <li>Frontiers in Digital Health, <em>E-Health Implementation under the National Framework 2022–2030 (June 2026)</em>.</li>
                    <li>MSF Telemedicine Annual Report, <em>Strategic Planning for Remote Healthcare 2026–2030 (April 2026)</em>.</li>
                    <li>NORRAG / Industry Analysis, <em>AI as Digital Capital: Addressing New Inequalities (June 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            159
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

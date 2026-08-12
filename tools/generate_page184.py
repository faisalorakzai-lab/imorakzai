from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-184-education-as-the-future.html'

GRAPHICS = [
    ("Education Future", "PAST", "↔", "NEXT"),
    ("Knowledge Base", "LEAR", "↔", "BASE"),
    ("Character Path", "SELF", "↔", "TRUE"),
    ("Skill Rail", "ABLE", "↔", "DONE"),
    ("Curiosity Path", "WHY", "→", "LEAR"),
    ("Critical Think", "WHY", "↔", "TRUE"),
    ("Problem-Solving", "FIX", "↔", "DONE"),
    ("Creativity Rail", "MAKE", "↔", "MIND"),
    ("Communication", "TALK", "↔", "ALL"),
    ("Collaboration", "ALL", "↔", "ONE"),
    ("Digital Literacy", "KNOW", "↔", "TECH"),
    ("AI Literacy", "KNOW", "↔", "AI"),
    ("Responsible AI", "TRUE", "↔", "SAFE"),
    ("Teacher Mentor", "WISE", "↔", "YOUN"),
    ("Personalized Lrn", "ONE", "↔", "LEAR"),
    ("Human Connect", "TWO", "↔", "ONE"),
    ("Digital Class", "NET", "↔", "LEAR"),
    ("Hybrid Edu Rail", "PHYS", "↔", "DIGI"),
    ("Remote Learning", "HERE", "↔", "THERE"),
    ("Access Rail", "ALL", "↔", "LEAR"),
    ("Digital Divide", "HAVE", "≠", "NONE"),
    ("Afford Connect", "CASH", "↔", "NET"),
    ("Devices Rail", "TOOL", "↔", "LEAR"),
    ("Electricity Base", "GRID", "↔", "LEAR"),
    ("Rural Education", "HERE", "↔", "BASE"),
    ("Urban Education", "CITY", "↔", "BASE"),
    ("Edu Equality", "ALL", "↔", "TRUE"),
    ("Girls Education", "GIRL", "→", "ABLE"),
    ("Boys Education", "BOY", "→", "ABLE"),
    ("Inclusive Edu", "ALL", "↔", "LINK"),
    ("Disability Acc", "SAFE", "↔", "ALL"),
    ("Early Childhood", "BORN", "↔", "BASE"),
    ("Primary Edu", "BASE", "↔", "LEAR"),
    ("Secondary Edu", "LEAR", "↔", "ABLE"),
    ("Higher Edu Rail", "LEAR", "↔", "TOP"),
    ("Vocational Edu", "WORK", "↔", "LEAR"),
    ("Skills-Based", "ABLE", "↔", "NAME"),
    ("CS Foundation", "CODE", "↔", "BASE"),
    ("Math Logic", "RULE", "↔", "TRUE"),
    ("Science Path", "WHY", "↔", "TRUE"),
    ("Engineering Rail", "MAKE", "↔", "DONE"),
    ("Medicine Path", "DOC", "↔", "LIFE"),
    ("Agri Science", "FARM", "↔", "TECH"),
    ("Finance Edu", "CASH", "↔", "WISE"),
    ("Entrepreneurship", "IDEA", "→", "BIZ"),
    ("Research Path", "WHY", "↔", "TRUE"),
    ("Uni Research", "LEAR", "↔", "KNOW"),
    ("Research Cult", "TRUE", "↔", "WISE"),
    ("Academic Free", "FREE", "↔", "TRUE"),
    ("Evidence Rail", "FACT", "↔", "TRUE"),
    ("Info Literacy", "INFO", "↔", "WISE"),
    ("Media Literacy", "NEWS", "↔", "TRUE"),
    ("Digital Safety", "SAFE", "↔", "NET"),
    ("Data Privacy", "DATA", "↔", "SAFE"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("AI-Gen Info", "AI", "≠", "FACT"),
    ("Human Judgment", "WISE", "↔", "DO"),
    ("Future Homework", "PROJ", "↔", "LEAR"),
    ("Project-Based", "MAKE", "↔", "LEAR"),
    ("Experimentation", "TEST", "→", "LEAR"),
    ("Failure Info", "FAIL", "→", "WISE"),
    ("Entr Learning", "BIZ", "↔", "LEAR"),
    ("Maker Culture", "MAKE", "↔", "DO"),
    ("Robotics Path", "BOT", "↔", "CODE"),
    ("Coding Rail", "CODE", "↔", "DO"),
    ("Comp Thinking", "RULE", "↔", "FIX"),
    ("Data Science", "DATA", "↔", "WISE"),
    ("AI Education", "AI", "↔", "LEAR"),
    ("AI Research", "AI", "↔", "KNOW"),
    ("Quantum Path", "ATOM", "↔", "CODE"),
    ("Future Tech", "NEW", "↔", "NEXT"),
    ("Learn How Learn", "LEAR", "→", "LEAR"),
    ("Lifelong Learn", "TIME", "↔", "LEAR"),
    ("Micro-Creds", "ONE", "↔", "NAME"),
    ("Digital Badge", "DONE", "↔", "NAME"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g184-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g184-{index}-title g184-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g184-{index}-title">{safe}</title><desc id="g184-{index}-desc">An education relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g184-{index}-caption" class="diagram-caption">{index}. {safe} — Education relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Education as the Future Framework</title><desc id="hero-desc">A diagram showing the 2026 education landscape, featuring KP's digital education overhaul, the AI in education market growth, and the shift from schooling to meaningful learning.</desc><defs><linearGradient id="h184-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h184-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE EDUCATION TRANSFORMATION LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AI IN EDUCATION MARKET: $10.6B (2026)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">KP DIGITAL REFORM: +30-35% LITERACY GOAL</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">LEARNING PASSPORT: 760,000+ CHILDREN (UNICEF)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">FEDERAL POLICY 2026: BRIDGING THE DIGITAL DIVIDE</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">PERSONALIZED LEARNING: 59% TEACHER ENHANCEMENT</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: KNOWLEDGE AS POWER</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">FUTURE: CAPABLE, ADAPTIVE & SOVEREIGN SOCIETIES</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">EDUCATION AS THE FUTURE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Knowledge, Skills, Character, and the Next Generation: From Schooling to Meaningful Learning.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Education Transformation Loop: Navigating the 2026 landscape where AI-driven personalization, provincial digital reforms, and skills-based learning ensure that societies are prepared to solve the complex problems of tomorrow.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 184</title>
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
            <p class="section-label">PAGE 184</p>
            <h2>EDUCATION AS THE FUTURE</h2>
            <p>“Knowledge, Skills, Character, and the Next Generation.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Education is one of the most powerful forces through which a society prepares for its future. Infrastructure can build cities, technology can connect people, and capital can finance businesses—but education determines whether people have the knowledge and judgment to use these resources effectively. The future will not belong simply to the countries with the most technology; it will belong to societies capable of learning, adapting, researching, creating, and solving problems. For Pakistan, education is more than a social service; it is the foundation for economic development, scientific progress, and individual opportunity.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">AI Transformation & Market Growth (2026)</h3>
                <p>By 2026, the global AI in education market is projected to reach **$10.6 billion**, reflecting a defining moment for universities and schools worldwide [1] [2]. Education systems are becoming more deliberate about AI acceleration, moving beyond hype toward selective investment in time and attention [3]. Generative AI is being integrated into teaching and learning scenarios, helping students learn subject knowledge while enabling teachers to focus on mentorship and human judgment [4] [5].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pakistan's Digital Education Overhaul</h3>
                <p>In Pakistan, the Khyber Pakhtunkhwa (KP) government has launched a **Rs 5 billion digital education reform programme** aiming to increase the literacy rate by **30-35%** over the next two years [6] [7]. The *Federal Education Policy 2026* draft highlights the digital divide as a critical challenge, as transformational technologies like AI outpace current capacity [8]. Meanwhile, UNICEF’s Learning Passport program has provided over **760,000 children** in Pakistan with access to quality digital education by 2026 [9].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">From Schooling to Meaningful Learning</h3>
                <p>A modern education system must focus on meaningful learning rather than just enrollment. The *2026 AI Index Report* indicates that AI is reshaping education from classrooms to career paths, emphasizing **skills-based education**, micro-credentials, and digital badges [10] [11]. In July 2026, the Ministry of Federal Education launched a pilot for a **Digital Life-Skills Learning Platform**, connecting theoretical knowledge with practical application in areas like coding, data science, and entrepreneurship [12].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Research Culture & Intellectual Honesty</h3>
                <p>A strong education system produces researchers capable of generating new knowledge. Universities in 2026 are being redefined as research centers that reward questions, evidence, and intellectual honesty [13]. Students are learning to distinguish evidence from opinion, a critical skill in an internet-connected world [14]. For the Orakzai community, the **Sovereign Grid** provides the infrastructure for locally relevant research, ensuring that our digital future is built on a foundation of authentic knowledge and sovereign values [15].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Education as the Future</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, education is the sacred trust we pass to our children. We do not just put people in classrooms; we prepare them to build the world. By mastering AI literacy and digital skills while remaining rooted in our character and values, we are ensuring that the next generation has the power to solve our problems and reach the world. Our education is sovereign, our learning is meaningful, and our future is built on the foundation of knowledge.”</p>
            </div>

            <div class="final-statement">
                KNOWLEDGE IS POWER.<br>
                LEARNING IS FREEDOM.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Digital Education Council, <em>AI in Higher Education Global Survey 2026 (2026)</em>.</li>
                    <li>OUS Academy Switzerland, <em>Global Education & AI Transformation: Market Projections 2026 (April 2026)</em>.</li>
                    <li>Holon IQ, <em>2026 Education Trends Snapshot: Selective AI Acceleration (January 2026)</em>.</li>
                    <li>UNESCO, <em>Artificial Intelligence in Education: Ethical Use and Learning Enhancement (2026)</em>.</li>
                    <li>OECD, <em>Digital Education Outlook 2026: Generative AI in Teaching and Learning (January 2026)</em>.</li>
                    <li>Pakistan Today, <em>KP Plans Digital Education Push to Lift Literacy by 35% (August 2026)</em>.</li>
                    <li>The Nation, <em>KP Govt to Launch Digital Transformation of Education System (August 2026)</em>.</li>
                    <li>MoFEPT Pakistan, <em>Federal Education Policy 2026 Draft: Addressing the Digital Divide (May 2026)</em>.</li>
                    <li>UNICEF Pakistan, <em>The Digital Transformation of Public Education: Learning Passport Milestones (2026)</em>.</li>
                    <li>Stanford University, <em>2026 AI Index Report: How AI is Reshaping Education (2026)</em>.</li>
                    <li>Digital Learning Institute, <em>Education Technology Trends to Watch in 2026: Personalization and Microcredentials (2026)</em>.</li>
                    <li>Tayarri News, <em>Federal Government Pilots Digital Life-Skills Learning Platform (July 2026)</em>.</li>
                    <li>Engageli, <em>25 AI in Education Statistics: Personalized Learning and Teacher Impact (2026)</em>.</li>
                    <li>ScienceDirect, <em>Artificial Intelligence in Personalized Learning: Higher Education Contexts (2025-2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Education as the Future and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            184
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

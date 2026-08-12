from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-177-the-future-of-work.html'

GRAPHICS = [
    ("Work Evolution", "PAST", "↔", "NEXT"),
    ("Agri Transition", "FARM", "→", "MECH"),
    ("Industrial Rev", "MAKE", "↔", "AUTO"),
    ("Electrification", "GRID", "↔", "MOVE"),
    ("Computer Rev", "DATA", "↔", "FAST"),
    ("Internet Rev", "LINK", "↔", "GLOB"),
    ("AI Transition", "AI", "↔", "WORK"),
    ("Automation Rail", "AUTO", "↔", "DONE"),
    ("Tasks Not Jobs", "ONE", "↔", "MANY"),
    ("Job Transform", "OLD", "→", "NEW"),
    ("AI-Assisted", "AI", "→", "HELP"),
    ("Human Supervis", "USER", "↔", "AI"),
    ("Human Judgment", "SELF", "↔", "WISE"),
    ("AI ≠ Human", "AI", "≠", "MIND"),
    ("Productivity Q", "LOW", "→", "HIGH"),
    ("Productivity Rail", "FAST", "↔", "DONE"),
    ("Prod Dividend", "CASH", "↔", "GROW"),
    ("Job Creation Q", "FIX", "↔", "NEW"),
    ("New Occupations", "NEW", "↔", "WORK"),
    ("AI Engineer", "CODE", "↔", "AI"),
    ("AI Researcher", "SCI", "↔", "AI"),
    ("Data Specialist", "DATA", "↔", "WISE"),
    ("AI Product Mgr", "BIZ", "↔", "AI"),
    ("AI Safety Prof", "SAFE", "↔", "AI"),
    ("AI Governance", "RULE", "↔", "AI"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("Robotics Path", "BOT", "↔", "PHYS"),
    ("Human-AI Inter", "USER", "↔", "AI"),
    ("AI Auditing", "CHECK", "↔", "AI"),
    ("AI Education", "LEAR", "↔", "AI"),
    ("AI-Assisted Prof", "WORK", "↔", "AI"),
    ("Lawyer Assistant", "LAW", "↔", "AI"),
    ("Doctor Assistant", "DOC", "↔", "AI"),
    ("Engineer Assist", "MAKE", "↔", "AI"),
    ("Architect Assist", "PLAN", "↔", "AI"),
    ("Accountant Auto", "DATA", "↔", "AI"),
    ("Fin Professional", "CASH", "↔", "AI"),
    ("Journalist Asst", "NEWS", "↔", "AI"),
    ("Teacher Assist", "LEAR", "↔", "AI"),
    ("Entr Leverage", "IDEA", "↔", "AI"),
    ("One-Person Co", "ONE", "↔", "ALL"),
    ("Small Team Path", "TEAM", "↔", "GRID"),
    ("Global Reach", "HERE", "→", "GLOB"),
    ("Global Freelancer", "ONE", "→", "GLOB"),
    ("Pak Digital Work", "HOME", "↔", "NET"),
    ("Pak Youth Opp", "YOUN", "→", "GLOB"),
    ("Skills > Titles", "ABLE", "↔", "NAME"),
    ("Technical Skills", "CODE", "↔", "BASE"),
    ("Digital Literacy", "KNOW", "↔", "TECH"),
    ("AI Literacy", "KNOW", "↔", "AI"),
    ("Prompt Muscle", "TALK", "→", "AI"),
    ("Domain Expertise", "WISE", "↔", "WORK"),
    ("Human Skills", "SELF", "↔", "ALL"),
    ("Creativity Path", "MAKE", "↔", "MIND"),
    ("Critical Think", "WHY", "↔", "TRUE"),
    ("Communication", "TALK", "↔", "ALL"),
    ("Leadership Rail", "LEAD", "↔", "ALL"),
    ("Empathy Path", "FEEL", "↔", "ALL"),
    ("Trust Asset", "TRUE", "↔", "SAFE"),
    ("Skills Transit", "LEAR", "↔", "TIME"),
    ("Reskilling Path", "OLD", "→", "NEW"),
    ("Upskilling Rail", "BASE", "→", "TOP"),
    ("Lifelong Learn", "TIME", "↔", "LEAR"),
    ("Micro-Creds", "ONE", "↔", "NAME"),
    ("Online Edu Rail", "LEAR", "↔", "NET"),
    ("AI Teacher Asst", "AI", "→", "WISE"),
    ("AI Student Asst", "AI", "→", "LEAR"),
    ("Edu Adaptation", "LEAR", "↔", "TIME"),
    ("Agency Expand", "SELF", "↔", "DO"),
    ("Sovereign Grid", "ORAK", "↔", "GRID"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g177-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g177-{index}-title g177-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g177-{index}-title">{safe}</title><desc id="g177-{index}-desc">A future of work relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g177-{index}-caption" class="diagram-caption">{index}. {safe} — Future of work relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">The Future of Work Framework</title><desc id="hero-desc">A diagram showing the 2026 future of work landscape, featuring AI-human collaboration, Pakistan's $1.76B freelance record, and the shift from jobs to task-based agency.</desc><defs><linearGradient id="h177-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h177-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE FUTURE OF WORK LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AI RESHAPING 55% OF JOBS (BCG 2026-2028)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">PAKISTAN FREELANCE RECORD: $1.76B EXPORT INCOME</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AI AGENTS & HUMAN AGENCY (MICROSOFT 2026)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">ONE-PERSON COMPANIES: SCALING VIA AUTOMATION</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">LIFELONG RESKILLING: FROM TITLES TO CAPABILITIES</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: REMOTE GLOBAL IMPACT</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">WORK: HUMAN-AI COLLABORATION & SHARED VALUES</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">THE FUTURE OF WORK</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“How Technology, AI and Human Capability Are Reshaping Work: Tasks, professions and Evolution.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Future of Work Loop: Navigating the 2026 landscape where AI-human collaboration, task-based agency, and Pakistan's record-breaking digital exports redefine professional capabilities and global reach.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 177</title>
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
            <p class="section-label">PAGE 177</p>
            <h2>THE FUTURE OF WORK</h2>
            <p>“How Technology, AI and Human Capability Are Reshaping Work.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Work has always changed with technology. Artificial intelligence is introducing another major transition. The future of work will not simply be a story about machines replacing people; it will be a story about tasks changing, professions evolving, and humans working alongside increasingly capable digital systems. For young people entering the workforce, the central question may no longer be 'What job will I have?' but 'What capabilities can I continue developing as the nature of work changes?'”
            </div>

            <section class="prose-section">
                <h3 class="section-label">AI Reshaping the Global Workforce (2026-2028)</h3>
                <p>By 2026, research indicates that **50% to 55% of jobs** in major economies will be reshaped by AI within the next two to three years [1]. The *2026 Work Trend Index* highlights a shift where AI agents take on execution, allowing human agency to expand into higher-level strategy, creativity, and judgment [2]. Organizations that intentionally redesign roles for human–AI collaboration are seeing transformative value, moving beyond the initial hype to real productivity gains [3] [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pakistan's Digital Labor & Freelance Record</h3>
                <p>Pakistan's digital services and freelance economy have achieved a record-breaking milestone, with freelancers generating **$1.76 billion** in export income in the fiscal year 2025-26 [5] [6]. In June 2026 alone, freelancers brought in **$164 million**, marking a 69% year-on-year increase [7]. This untapped growth engine allows young Pakistanis to participate in global technology markets through software, AI engineering, design, and cybersecurity, serving international customers from their home foundation [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">From Jobs to Tasks: The Rise of the One-Person Company</h3>
                <p>The nature of work is shifting from rigid job titles to fluid tasks. AI tools now allow very small teams—and even "one-person companies"—to perform a broader range of functions, scaling via automation, cloud infrastructure, and digital marketing [9]. Entry-level work is becoming more complex earlier, requiring new professionals to master AI literacy, critical thinking, and domain expertise from the start [10]. Domain knowledge combined with AI capability is becoming more valuable than either alone [11].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Lifelong Reskilling & Human Agency</h3>
                <p>In a world that changes continuously, education is no longer a single period but a lifelong process of reskilling and upskilling [12]. Human capabilities like leadership, empathy, and collaboration remain central to many professions, as trust becomes a critical asset for organizations using automated systems [13]. For the Orakzai builder, the **Sovereign Grid** provides the infrastructure for remote global impact, ensuring that work remains a form of service and authentic contribution to the community [14].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: The Future of Work</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai worker, the future of work is the modern field of our resilience. We do not fear automation; we master the tools that expand our agency. By combining our cultural values with AI literacy and global connectivity, we are building a sovereign legacy where our skills are respected worldwide. We work to build, we learn to adapt, and we lead to serve a future that is human-centered and authentic.”</p>
            </div>

            <div class="final-statement">
                MASTER THE TOOLS.<br>
                EXPAND YOUR AGENCY.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>BCG Publications, <em>AI Will Reshape More Jobs Than It Replaces: 2026-2028 Projections (April 2026)</em>.</li>
                    <li>Microsoft WorkLab, <em>2026 Work Trend Index: Agents, Human Agency, and Organizational Opportunity (May 2026)</em>.</li>
                    <li>Deloitte Insights, <em>2026 Global Human Capital Trends: Human–AI Collaboration (March 2026)</em>.</li>
                    <li>Gartner, <em>Future of Work Trends 2026: Strategic Insights for CEOs and CHROs (January 2026)</em>.</li>
                    <li>Jobbers.io, <em>The Freelance Industry GDP Contribution by Country 2026 (May 2026)</em>.</li>
                    <li>Instagram / ProPakistani, <em>Pakistan's Freelance Community Record $1.76B Export Income (July 2026)</em>.</li>
                    <li>SDPI Official, <em>Pakistan's Digital Services and Freelance Economy Growth Engine (June 2026)</em>.</li>
                    <li>Trustwave, <em>Pakistan Gig Workers' Export Earnings Reach New High Amid AI Concerns (June 2026)</em>.</li>
                    <li>Taskade Blog, <em>One-Person Company Software: Scaling via AI Agents (March 2026)</em>.</li>
                    <li>PwC, <em>2026 AI Jobs Barometer: Reshaping Entry-Level Roles (June 2026)</em>.</li>
                    <li>World Economic Forum, <em>Artificial Intelligence and the Future of Entry-Level Work (2026)</em>.</li>
                    <li>Nexford University, <em>How Will AI Affect Jobs 2026-2030: Reskilling and Upskilling (August 2026)</em>.</li>
                    <li>Leadership Circle, <em>Workplace Trends for 2026: Wellbeing, Trust and AI Integration (March 2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Future of Work and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            177
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

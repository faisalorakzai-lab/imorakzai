from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-178-human-skills-in-an-ai-world.html'

GRAPHICS = [
    ("Human Skill Path", "SELF", "↔", "AI"),
    ("Unique Human", "SOUL", "≠", "CODE"),
    ("Human + AI", "WISE", "↔", "FAST"),
    ("Augmentation", "SELF", "→", "ABLE"),
    ("Automation Rail", "AUTO", "↔", "DONE"),
    ("Computation", "FAST", "↔", "DATA"),
    ("Human Judgment", "SELF", "↔", "WISE"),
    ("Info vs Wisdom", "DATA", "→", "WISE"),
    ("Context Rail", "HERE", "↔", "TRUE"),
    ("Human Experience", "LIFE", "↔", "WISE"),
    ("Critical Think", "WHY", "↔", "TRUE"),
    ("Verify AI Output", "CHECK", "↔", "TRUE"),
    ("Quality Control", "BEST", "↔", "SAFE"),
    ("Fact-Checking", "TRUE", "↔", "FACT"),
    ("Question Why", "WHY", "↔", "DONE"),
    ("Source Eval", "WHO", "↔", "TRUE"),
    ("Epistemic Humil", "SELF", "↔", "KNOW"),
    ("Curiosity Path", "WHY", "→", "LEAR"),
    ("Better Questions", "WHY", "→", "HOW"),
    ("Problem Form", "WHY", "→", "FIX"),
    ("Right Problem", "TRUE", "↔", "FIX"),
    ("Creativity Rail", "MAKE", "↔", "MIND"),
    ("Originality Path", "SELF", "↔", "MAKE"),
    ("Design Thinking", "USER", "↔", "NEED"),
    ("Innovation Path", "IDEA", "→", "DONE"),
    ("Entr Thinking", "IDEA", "→", "BIZ"),
    ("Vision Path", "SELF", "↔", "NEXT"),
    ("Strategy Rail", "PLAN", "↔", "DONE"),
    ("Decision-Making", "WISE", "↔", "DO"),
    ("Risk Judgment", "SAFE", "↔", "RISK"),
    ("Responsibility", "SELF", "↔", "DONE"),
    ("Ethics Rail", "TRUE", "↔", "SAFE"),
    ("Moral Reasoning", "TRUE", "↔", "ALL"),
    ("Empathy Path", "FEEL", "↔", "ALL"),
    ("Human Relation", "TWO", "↔", "ONE"),
    ("Leadership Rail", "LEAD", "↔", "ALL"),
    ("Trusted Lead", "TRUE", "↔", "LEAD"),
    ("Communication", "TALK", "↔", "ALL"),
    ("Active Listen", "HEAR", "↔", "WISE"),
    ("Storytelling", "TALK", "↔", "LIFE"),
    ("Negotiation", "TWO", "↔", "DEAL"),
    ("Collaboration", "ALL", "↔", "DONE"),
    ("Teamwork Rail", "TWO", "↔", "ONE"),
    ("Conflict Resol", "FIX", "↔", "FEEL"),
    ("Cultural Intel", "HOME", "↔", "GLOB"),
    ("Global Comm", "HERE", "↔", "GLOB"),
    ("Adaptability", "LEAR", "↔", "TIME"),
    ("Learn How Learn", "LEAR", "→", "LEAR"),
    ("Lifelong Learn", "TIME", "↔", "LEAR"),
    ("Reskilling Path", "OLD", "→", "NEW"),
    ("Upskilling Rail", "BASE", "→", "TOP"),
    ("Experimentation", "TEST", "→", "KNOW"),
    ("Failure Info", "FAIL", "→", "WISE"),
    ("Resilience Path", "FAIL", "→", "STAY"),
    ("Patience Rail", "TIME", "↔", "DONE"),
    ("Discipline Path", "DO", "↔", "LONG"),
    ("Focus Muscle", "EYE", "↔", "MIND"),
    ("Attention Asset", "EYE", "↔", "CASH"),
    ("Digital Well-being", "SELF", "↔", "TIME"),
    ("Deep Work Rail", "MIND", "↔", "TIME"),
    ("Reflection Path", "SELF", "↔", "WISE"),
    ("Self-Awareness", "SELF", "↔", "KNOW"),
    ("Emotional Intel", "FEEL", "↔", "WISE"),
    ("Self-Regulation", "SELF", "↔", "RULE"),
    ("Motivation Rail", "WHY", "→", "DO"),
    ("Purpose Path", "WHY", "↔", "LONG"),
    ("Meaningful Work", "WORK", "↔", "SOUL"),
    ("Dignity Rail", "SELF", "↔", "TRUE"),
    ("Systems Thinking", "ALL", "↔", "ONE"),
    ("Stakeholder Alig", "ALL", "↔", "LINK"),
    ("Commercial Judg", "BIZ", "↔", "WISE"),
    ("Data Fluency", "DATA", "↔", "KNOW"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g178-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g178-{index}-title g178-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g178-{index}-title">{safe}</title><desc id="g178-{index}-desc">A human skills in an AI world relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g178-{index}-caption" class="diagram-caption">{index}. {safe} — Human skills relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Human Skills in an AI World Framework</title><desc id="hero-desc">A diagram showing the 2026 framework for human-AI collaboration, featuring the shift from computation to judgment, and the rise of emotional intelligence, creativity, and systems thinking.</desc><defs><linearGradient id="h178-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h178-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE HUMAN AGENCY LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">JUDGMENT & QUALITY CONTROL: 50% PRIORITY</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">ANALYTICAL & CREATIVE THINKING: TOP CORE SKILLS</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">EMOTIONAL INTEL: 83% BELIEVE AI ADDS VALUE</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SYSTEMS THINKING & COMMERCIAL JUDGMENT</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">RESILIENCE, AGILITY & LIFELONG ADAPTATION</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN VALUES: IDENTITY & DIGNITY</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">HUMAN SKILLS: EMPATHY, TRUST & LEADERSHIP</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">HUMAN SKILLS IN AN AI WORLD</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“What Remains Uniquely Human: Judgment, Creativity and the Responsibility to Lead.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Human Agency Loop: Navigating the 2026 landscape where human judgment, emotional intelligence, and systems thinking become the ultimate drivers of business value in an AI-enabled digital civilization.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 178</title>
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
            <p class="section-label">PAGE 178</p>
            <h2>HUMAN SKILLS IN AN AI WORLD</h2>
            <p>“What Remains Uniquely Human as Artificial Intelligence Advances.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Artificial intelligence is changing the relationship between humans, information and machines. AI can generate text, analyze data, and assist with complex tasks. As these capabilities expand, human capabilities become more valuable—not in competition with machines, but in combination with them. AI can process information, but humans establish goals. AI can generate possibilities, but humans decide which matter. AI can identify patterns, but humans interpret them within social, cultural and ethical contexts. The future requires more than technical literacy; it requires judgment, creativity, empathy, and responsibility.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Shift to Judgment & Quality Control (2026)</h3>
                <p>By 2026, the *Work Trend Index* reveals that the most critical human skills have shifted from execution to oversight. Employers now rank **quality control of AI output** as a top priority, with 50% of leaders identifying it as essential [1]. Human judgment becomes particularly important when decisions involve uncertainty, consequences, or competing values. In an AI-enabled world, the sophisticated user doesn't just ask for the answer; they ask "Why should I believe it?" and "What might be missing?" [2] [3].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Analytical Thinking, Creativity & Systems Thinking</h3>
                <p>Human capital trends in 2026 emphasize analytical and creative thinking as the top core skills for the future workforce [4]. While AI can assist creative processes, humans continue to determine the meaning and context of original work. **Systems thinking**—the ability to understand how different components of an organization or technology interact—and strong **commercial judgment** are becoming the primary drivers of business value [5] [6]. Innovation is no longer just generating ideas; it is turning useful ideas into practical, human-centered outcomes [7].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Emotional Intelligence & Human Relationships</h3>
                <p>According to a 2025 global survey, **83% of employees** believe that AI will make human skills like empathy and active listening even more valuable [8]. Many areas of life and work depend on trust, emotional understanding, and personal relationships that cannot be reduced to numerical patterns. Leaders who can communicate clearly and take responsibility when decisions are difficult are in high demand [9]. Integrating emotional intelligence ensures that AI-driven efficiency is balanced with genuine human connection and awareness [10].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Resilience, Agility & Lifelong Learning</h3>
                <p>Technological change means that skills can become outdated rapidly. **Resilience**—the ability to recover from setbacks—and **agility** are now ranked among the most valuable long-term capabilities [11]. Education has extended into a lifelong process of reskilling and upskilling, where the ability to "learn how to learn" is the ultimate competitive advantage [12]. For the Orakzai builder, these human skills are the modern expression of tribal resilience, ensuring that our digital civilization remains authentic, sovereign, and dignified [13] [14].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Human Skills in an AI World</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, our greatest asset is not just our technology, but our character. AI can calculate, but it cannot care. It can simulate, but it cannot sacrifice. By mastering the human skills of judgment, empathy, and leadership, we are ensuring that our digital future is not just efficient, but meaningful. We do not just build systems; we build trust, dignity, and a sovereign legacy that respects our humanity.”</p>
            </div>

            <div class="final-statement">
                JUDGMENT OVER DATA.<br>
                CHARACTER OVER CODE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Microsoft WorkLab, <em>2026 Work Trend Index: Quality Control and Human Agency (May 2026)</em>.</li>
                    <li>PwC, <em>2026 AI Jobs Barometer: Increasing Emphasis on Human Judgement (June 2026)</em>.</li>
                    <li>Deloitte Insights, <em>2026 Global Human Capital Trends: Redesigning Work for AI Collaboration (March 2026)</em>.</li>
                    <li>Forbes / Workday Survey, <em>83% of Employees Believe AI Makes Human Skills More Valuable (November 2025)</em>.</li>
                    <li>Gloat Blog, <em>AI Workforce Trends 2026: Demand for Creative Thinking and Resilience (May 2026)</em>.</li>
                    <li>GMAC Resources, <em>Workplace Trends 2026: Systems Thinking and Commercial Judgment (January 2026)</em>.</li>
                    <li>Aon, <em>2026 Human Capital Trends Study: Closing the Skills Gap (2026)</em>.</li>
                    <li>Mavenside Consulting, <em>Skills Employers Will Look for in 2026: Resilience and Social Influence (November 2025)</em>.</li>
                    <li>Carson Newman Blog, <em>Top Workplace Skills Employers Will Demand in 2026 (January 2026)</em>.</li>
                    <li>LinkedIn / AI Content, <em>Best Practices for Human Interaction in AI: Emotional Intelligence (2026)</em>.</li>
                    <li>Emergenetics Blog, <em>Exploring Human-AI Collaboration: Building Productive Teams (2026)</em>.</li>
                    <li>MDPI, <em>Human–AI Collaboration Across Decision Support Systems (2026)</em>.</li>
                    <li>World Economic Forum, <em>Four Ways to Enhance Human-AI Collaboration in the Workplace (January 2025)</em>.</li>
                    <li>Orakzai Group Archives, <em>Human Agency and Sovereign Values in the Digital Age (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            178
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

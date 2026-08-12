from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-200-references-sources-and-historical-bibliography.html'

GRAPHICS = [
    ("Bibliography", "PAST", "↔", "TRUE"),
    ("Reliable Record", "FACT", "↔", "SAVE"),
    ("Evidence Base", "FACT", "↔", "TRUE"),
    ("Hist Sources", "OLD", "↔", "TRUE"),
    ("Cultural Doc", "SAVE", "↔", "WISE"),
    ("Scientific Res", "WHY", "↔", "FACT"),
    ("Tech Standards", "RULE", "↔", "FIX"),
    ("Economic Data", "CASH", "↔", "FACT"),
    ("Inst Sources", "GRID", "↔", "TRUE"),
    ("Personal Narr", "SELF", "≠", "FACT"),
    ("Ref Purpose", "LEAR", "↔", "TRUE"),
    ("Verification", "WHY", "↔", "TRUE"),
    ("Correction Rail", "FIX", "↔", "DONE"),
    ("Knowledge Orig", "PAST", "→", "NOW"),
    ("Primary Source", "ORIG", "↔", "TRUE"),
    ("Archival Doc", "SAVE", "↔", "TRUE"),
    ("Official Rec", "RULE", "↔", "TRUE"),
    ("Oral History", "TALK", "→", "SAVE"),
    ("Secondary Src", "WHY", "↔", "TRUE"),
    ("Scholarly Book", "WISE", "↔", "TRUE"),
    ("Hist Method", "RULE", "↔", "TRUE"),
    ("Provenance", "ORIG", "↔", "TRUE"),
    ("Chronology", "TIME", "↔", "TRUE"),
    ("Corroboration", "MANY", "↔", "ONE"),
    ("Archival Rel", "SAVE", "↔", "SAFE"),
    ("Cultural Hist", "SAVE", "↔", "TRUE"),
    ("Orakzai Study", "ORAK", "↔", "TRUE"),
    ("Pashtun Study", "PASH", "↔", "TRUE"),
    ("Tribal Hist", "HOME", "↔", "TRUE"),
    ("Colonial Rec", "PAST", "↔", "TRUE"),
    ("South Asia Hist", "GLOB", "↔", "TRUE"),
    ("Pakistan Hist", "FLAG", "↔", "TRUE"),
    ("Partition 1947", "PAST", "↔", "TRUE"),
    ("Pak Statistics", "FACT", "↔", "BASE"),
    ("PBS Data", "FACT", "↔", "TRUE"),
    ("SBP Data", "CASH", "↔", "TRUE"),
    ("HEC Data", "LEAR", "↔", "TRUE"),
    ("PTA Data", "LINK", "↔", "TRUE"),
    ("PSEB Data", "CODE", "↔", "TRUE"),
    ("UN Datasets", "GLOB", "↔", "TRUE"),
    ("UNESCO GEMR", "LEAR", "↔", "TRUE"),
    ("World Bank GEP", "CASH", "↔", "TRUE"),
    ("IMF WEO", "CASH", "↔", "TRUE"),
    ("ITU Standards", "LINK", "↔", "RULE"),
    ("ILO Trends", "WORK", "↔", "TRUE"),
    ("WIPO Innov", "IDEA", "↔", "RULE"),
    ("WHO Health", "LIFE", "↔", "TRUE"),
    ("UNDP Dev", "GLOB", "↔", "TRUE"),
    ("UNICEF Child", "YOUN", "↔", "TRUE"),
    ("OECD Trans", "GLOB", "↔", "TRUE"),
    ("ISO Standards", "RULE", "↔", "BASE"),
    ("NIST Cyber", "SEC", "↔", "SAFE"),
    ("IETF Protocols", "NET", "↔", "RULE"),
    ("W3C Web", "LINK", "↔", "RULE"),
    ("ICANN Domain", "NET", "↔", "RULE"),
    ("Blockchain Res", "GRID", "↔", "TRUE"),
    ("Bitcoin Paper", "CASH", "↔", "TRUE"),
    ("Ethereum Prop", "CODE", "↔", "TRUE"),
    ("Smart Contract", "CODE", "↔", "SAFE"),
    ("Tokenization", "PHYS", "→", "DIGI"),
    ("Digital Ident", "SELF", "↔", "NET"),
    ("Cybersecurity", "SEC", "↔", "SAFE"),
    ("AI Research", "AI", "↔", "TRUE"),
    ("AI Index 2026", "AI", "↔", "FACT"),
    ("AI Governance", "RULE", "↔", "SAFE"),
    ("AI and Work", "AI", "↔", "DO"),
    ("Task Automate", "AI", "→", "DO"),
    ("Agentic Era", "AI", "↔", "DO"),
    ("Data Gov", "RULE", "↔", "SAFE"),
    ("Sovereign Legacy", "ORAK", "↔", "LONG"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g200-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g200-{index}-title g200-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g200-{index}-title">{safe}</title><desc id="g200-{index}-desc">A reference relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g200-{index}-caption" class="diagram-caption">{index}. {safe} — Reference relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">REFERENCES, SOURCES & HISTORICAL BIBLIOGRAPHY Framework</title><desc id="hero-desc">A diagram showing the 2026 reference landscape, featuring the UNESCO GEMR 2026, IMF WEO April 2026, World Bank GEP June 2026, ILO Trends 2026, and the Stanford AI Index 2026.</desc><defs><linearGradient id="h200-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h200-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE RELIABLE RECORD LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">UNESCO GEMR 2026: ACCESS AND EQUITY REPORT</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">IMF WEO APRIL 2026: GLOBAL GROWTH AT 3.1%</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">WORLD BANK GEP JUNE 2026: SLUMP TO 2.5%</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">ILO TRENDS 2026: JOBS GAP AT 408 MILLION</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">STANFORD AI INDEX 2026: MEASURING IMPACT</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: SOURCES AS INFRASTRUCTURE</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">MISSION: BUILD A RELIABLE RECORD FOR THE FUTURE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">REFERENCES & BIBLIOGRAPHY</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Building a Reliable Record: Historical, Cultural, Scientific, Technical, and Economic Evidence.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Reliable Record Loop: Navigating the 2026 landscape where flagship reports from UNESCO, IMF, World Bank, ILO, and Stanford ensure that our knowledge of history, economy, and technology is anchored in verifiable evidence and sovereign integrity.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 200</title>
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
            <p class="section-label">PAGE 200</p>
            <h2>REFERENCES, SOURCES & HISTORICAL BIBLIOGRAPHY</h2>
            <p>“Building a Reliable Record: Historical, Cultural, Scientific, Technical, and Economic Evidence.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “A book about history, identity, culture, technology, and the future should end with something fundamental: sources. The preceding pages bring together subjects that require different kinds of evidence. Historical claims require historical sources; cultural claims require documentation; scientific claims require research; and technology claims require standards. A reference list allows readers to investigate, future researchers to verify, and errors to be corrected. It is a record of where our knowledge came from.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">International Development & Economic Indicators (2026)</h3>
                <p>The **UNESCO Global Education Monitoring Report 2026** provides the definitive analysis of access and equity as we countdown to 2030 [1]. The **IMF World Economic Outlook (April 2026)** projects global growth at 3.1%, while the **World Bank Global Economic Prospects (June 2026)** warns of a slump to 2.5% [2] [3]. These datasets, along with the **ILO Employment and Social Trends 2026**, which identifies a global jobs gap of 408 million, form the economic foundation of our analysis [4] [5].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Technological Standards & AI Trajectory</h3>
                <p>Technical standards for the digital civilization are maintained by the **ITU**, **NIST**, and the **ISO**, with 2026 updates focusing on cybersecurity and AI governance [6] [7]. The **Stanford AI Index 2026 Report** offers a comprehensive analysis of AI's trajectory, adoption, and public opinion [8]. Foundational papers such as Nakamoto (2008) for Bitcoin and Buterin (2014) for Ethereum remain critical references for understanding programmable economies and decentralized ledgers [9] [10].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pakistani Institutional Data & Governance</h3>
                <p>For contemporary Pakistani statistics, priority is given to primary sources such as the **Pakistan Bureau of Statistics (PBS)** and the **State Bank of Pakistan (SBP)** [11]. The **Pakistan Governance Forum 2026**, in collaboration with UNESCO, has established robust data governance frameworks that ensure the integrity of national institutional records [12]. The **PTA** and **PSEB** provide the technical documentation required to understand the country's digital infrastructure and software export record [13] [14].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Orakzai & Pashtun Studies: Historical Method</h3>
                <p>Historical research concerning Orakzai and wider Pashtun history draws on reputable anthropological, linguistic, and ethnographic scholarship [15]. This bibliography distinguishes between primary evidence—archival documents, oral histories, and colonial records—and secondary interpretations [16]. By applying the historical method of provenance, chronology, and corroboration, we ensure that the Orakzai story is part of a credible and verifiable human journey [17] [18].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: References, Sources & Bibliography</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, our sources are our roots. We do not just claim a history; we document it. By anchoring our knowledge in the reports of the UN, UNESCO, and the World Bank while remaining rooted in our own oral traditions and archival records, we are ensuring that the Orakzai legacy is one of truth and intelligence. We are the builders of a record that is sovereign, verifiable, and eternal. Our evidence is our strength, and our bibliography is our responsibility.”</p>
            </div>

            <div class="final-statement">
                VERIFIABLE TRUTH.<br>
                SOVEREIGN RECORD.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>UNESCO, <em>Global Education Monitoring Report 2026 - Access and Equity: Countdown to 2030 (Paris, 2026)</em>.</li>
                    <li>IMF, <em>World Economic Outlook, April 2026: Global Economy in Transition (2026)</em>.</li>
                    <li>World Bank, <em>Global Economic Prospects - June 2026: The Growth Slump (2026)</em>.</li>
                    <li>ILO, <em>Employment and Social Trends 2026: The Global Jobs Gap (January 2026)</em>.</li>
                    <li>UNESCO Institute for Statistics (UIS), <em>2026 Survey of Formal Education and Global Data Collection (2026)</em>.</li>
                    <li>NIST, <em>Technical Standards and Cybersecurity Guidance for Emerging Technologies (2026)</em>.</li>
                    <li>ISO, <em>International Standards for Information Systems and AI Governance (2026)</em>.</li>
                    <li>Stanford HAI, <em>The 2026 AI Index Report: Measuring Impact, Adoption, and Policy (2026)</em>.</li>
                    <li>Nakamoto, S., <em>Bitcoin: A Peer-to-Peer Electronic Cash System (2008)</em>.</li>
                    <li>Buterin, V., <em>A Next-Generation Smart Contract and Decentralized Application Platform (2014)</em>.</li>
                    <li>Pakistan Bureau of Statistics (PBS), <em>National Statistical Datasets and Census Publications (2026)</em>.</li>
                    <li>UNESCO / Pakistan Governance Forum, <em>Ethical AI and Data Governance Framework for Pakistan (February 2026)</em>.</li>
                    <li>Pakistan Telecommunication Authority (PTA), <em>Annual Digital Development and Connectivity Report (2026)</em>.</li>
                    <li>Pakistan Software Export Board (PSEB), <em>Software Exports and IT Sector Growth Analysis (2026)</em>.</li>
                    <li>UNCTAD, <em>Technology and Innovation Report: Science, Technology, and Innovation for Sustainability (2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Historical Bibliography and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            200
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

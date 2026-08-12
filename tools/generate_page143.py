from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-143-national-digital-infrastructure.html'

GRAPHICS = [
    ("National Infra", "PHYS", "↔", "DIGI"),
    ("Digital Foundation", "BASE", "→", "LIFE"),
    ("Connectivity Loop", "PEOP", "↔", "NET"),
    ("Physical Foundation", "CAB", "ROUT", "SERV"),
    ("Antenna Link", "ANT", "↔", "USER"),
    ("Data Center Link", "DC", "↔", "BCK"),
    ("Power Link", "POWR", "↔", "SYS"),
    ("Satellite Link", "SAT", "↔", "REMT"),
    ("Digital Stack", "BASE", "→", "TOP"),
    ("Energy Layer", "POWR", "↔", "BASE"),
    ("Physical Layer", "PHYS", "↔", "BASE"),
    ("Telecom Layer", "TEL", "↔", "BASE"),
    ("Network Layer", "NET", "↔", "BASE"),
    ("Data Layer", "DATA", "↔", "BASE"),
    ("Cloud Layer", "CLD", "↔", "BASE"),
    ("Application Layer", "APP", "↔", "BASE"),
    ("Service Layer", "SERV", "↔", "BASE"),
    ("Fixed Broadband", "FIX", "↔", "NET"),
    ("Mobile Broadband", "MOB", "↔", "NET"),
    ("Fiber Optic Link", "FIBR", "↔", "FAST"),
    ("Wireless Link", "WIRE", "↔", "NET"),
    ("Satellite Link", "SAT", "↔", "NET"),
    ("High Capacity", "BIG", "↔", "DATA"),
    ("Long Distance", "FAR", "↔", "FAST"),
    ("Backbone Arch", "CITY", "↔", "DC"),
    ("City Peering", "CITY", "↔", "CITY"),
    ("IXP Peering", "NET", "↔", "IXP"),
    ("Resilient Back", "SAFE", "↔", "NET"),
    ("Mobile Banking", "BANK", "↔", "MOB"),
    ("Mobile Gov", "GOVT", "↔", "MOB"),
    ("Mobile Edu", "EDU", "↔", "MOB"),
    ("5G Rollout", "5G", "↔", "2026"),
    ("Future Network", "AUTO", "↔", "NET"),
    ("Industrial IoT", "IOT", "↔", "NET"),
    ("Smart Infra", "SMART", "↔", "NET"),
    ("Robotics Link", "ROB", "↔", "NET"),
    ("Local Peering", "LOCL", "↔", "IXP"),
    ("Latency Loop", "REQ", "↔", "RES"),
    ("Network Effic", "FAST", "↔", "SYS"),
    ("Intl Gateway", "GLOB", "↔", "NATL"),
    ("Submarine Cable", "SEA", "↔", "NET"),
    ("Cross-Border", "LAND", "↔", "NET"),
    ("Landing Station", "SEA", "→", "LAND"),
    ("Remote Region", "REMT", "↔", "SAT"),
    ("Disaster Link", "SOS", "↔", "SAT"),
    ("Difficult Ter", "MTN", "↔", "SAT"),
    ("Rural Access", "RURL", "↔", "NET"),
    ("Digital Divide", "HAVE", "≠", "NOT"),
    ("Affordability", "COST", "↔", "USE"),
    ("Digital Skills", "KNOW", "↔", "USE"),
    ("Data Center Env", "DC", "↔", "DATA"),
    ("DC Storage", "STOR", "↔", "DC"),
    ("DC Cooling", "COOL", "↔", "DC"),
    ("National Capacity", "NATL", "↔", "DC"),
    ("Sovereign Cloud", "SOV", "↔", "CLD"),
    ("Edge Computing", "EDGE", "↔", "FAST"),
    ("National Compute", "CPU", "↔", "NATL"),
    ("AI Infra Loop", "DATA", "→", "APP"),
    ("GPU Computing", "GPU", "↔", "AI"),
    ("Energy Planning", "POWR", "↔", "DIGI"),
    ("DC Efficiency", "ECO", "↔", "DC"),
    ("Cooling Tech", "WATR", "↔", "DC"),
    ("Digital ID Link", "ID", "↔", "NATL"),
    ("DPI Identity", "ID", "↔", "DPI"),
    ("DPI Payments", "PAY", "↔", "DPI"),
    ("DPI Exchange", "DATA", "↔", "DPI"),
    ("DPI Credentials", "CERT", "↔", "DPI"),
    ("DPI Services", "SERV", "↔", "DPI"),
    ("Payment Infra", "PAY", "↔", "ECON"),
    ("E-Commerce Link", "BUY", "↔", "NET"),
    ("Fintech Infra", "FIN", "↔", "TECH"),
    ("Remittance Link", "REMT", "↔", "FAST"),
    ("Faisal Orakzai profile", "SYS", "↔", "NATL"),
    ("Orakzai Fiber", "LOCL", "↔", "FIBR"),
    ("OSG Infra Link", "OSG", "↔", "BASE"),
    ("Sovereign-by-Design", "PLAN", "→", "SOV"),
    ("IDI Improvement", "UP", "↔", "IDI"),
    ("5G Site Loop", "SITE", "↔", "5G"),
    ("Theoretical Spd", "FAST", "↔", "5G"),
    ("Phased Roadmap", "TIME", "→", "ALL"),
    ("Interoperable", "ONE", "↔", "MANY"),
    ("NADRA Foundation", "ID", "↔", "PAK"),
    ("Raast Ecosystem", "PAY", "↔", "PAK"),
    ("GDP Boost Loop", "DPI", "→", "GDP"),
    ("AAE-1 Cable", "AAE1", "↔", "SEA"),
    ("Peace Cable", "PEAC", "↔", "SEA"),
    ("SMW-5 Cable", "SMW5", "↔", "SEA"),
    ("Peering Effic", "IXP", "↔", "NET"),
    ("Urban-Rural", "CITY", "↔", "RURL"),
    ("Inclusive Infra", "ALL", "↔", "NET"),
    ("Infrastructure Res", "SAFE", "↔", "TIME"),
    ("Shared Found", "BASE", "↔", "ALL"),
    ("National Backbone", "NATL", "↔", "NET"),
    ("Fiber Capacity", "BIG", "↔", "FIBR"),
    ("Mobile Pen", "MOB", "↔", "POP"),
    ("Broadband Grow", "UP", "↔", "BBD"),
    ("Digital Economy", "DIGI", "↔", "ECON"),
    ("Service Delivery", "SERV", "↔", "NET"),
    ("Strategic Indep", "FREE", "↔", "SOV"),
    ("Institutional Cap", "INST", "↔", "SOV"),
    ("Technological Cap", "TECH", "↔", "SOV"),
    ("Economic Prod", "WORK", "↔", "DIGI"),
    ("National Resil", "SAFE", "↔", "SOV"),
    ("Opportunity Acc", "OPEN", "↔", "ALL"),
    ("Interconnected", "LINK", "↔", "ALL"),
    ("Communication", "TALK", "↔", "NET"),
    ("Computation", "CALC", "↔", "CPU"),
    ("Information Ex", "EXCH", "↔", "DATA"),
    ("Public Services", "GOVT", "↔", "USER"),
    ("Participation", "PART", "↔", "DIGI"),
    ("Digital World", "IDEA", "↔", "REAL"),
    ("Final Infra", "BASE", "↔", "SOV"),
    ("Infrastructure Era", "TIME", "↔", "DIGI"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g143-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g143-{index}-title g143-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g143-{index}-title">{safe}</title><desc id="g143-{index}-desc">A digital infrastructure relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g143-{index}-caption" class="diagram-caption">{index}. {safe} — Digital infrastructure relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">National Digital Infrastructure Framework</title><desc id="hero-desc">A diagram showing the integrated stack of national digital infrastructure, from physical foundations to digital services and economic impact.</desc><defs><linearGradient id="h143-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h143-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">NATIONAL DIGITAL STACK</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DIGITAL SERVICES & ECONOMY</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DIGITAL PUBLIC INFRASTRUCTURE</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">CLOUD & COMPUTING CAPACITY</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">NETWORKS & IXPS</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">TELECOMMUNICATIONS & FIBER</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">PHYSICAL FOUNDATIONS</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">ENERGY & POWER SYSTEMS</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">NATIONAL DIGITAL INFRASTRUCTURE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“The Digital Foundation of a Modern Nation.”</text></svg><figcaption id="hero-caption" class="diagram-caption">National Digital Infrastructure: The collection of physical, digital, and institutional systems that enable a country to participate in the digital economy.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 143</title>
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
        .case-study-card {{ border: 1px solid var(--gold); padding: 30px; margin: 50px 0; background: rgba(181,150,84,0.05); }}
        .final-statement {{ text-align: center; font-size: 1.8rem; font-weight: 700; color: var(--gold); margin: 60px 0; }}
        @media (max-width: 768px) {{ .atlas-grid {{ grid-template-columns: 1fr; }} }}
        svg {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="content-page">
        <header class="page-header">
            <p class="section-label">PAGE 143</p>
            <h2>NATIONAL DIGITAL INFRASTRUCTURE</h2>
            <p>“The Digital Foundation of a Modern Nation.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “National digital infrastructure is the collection of physical, digital, and technological systems that enable a country to communicate, compute, and participate in the digital economy. It is the technological foundation connecting people to services and opportunity. For Pakistan, the quality and resilience of this infrastructure are becoming the primary drivers of economic productivity and national resilience in the 21st century.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">National Performance & Connectivity</h3>
                <p>Digital infrastructure is the backbone of the modern state. As of 2026, Pakistan has shown a <strong>20% improvement</strong> in the ITU ICT Development Index, with its score rising to <strong>67.7</strong>. This progress is driven by the expansion of <strong>Fiber-Optic Networks</strong> and high-capacity connections, which reached <strong>5.10 million</strong> in 2026. The objective is to build a resilient national backbone that connects cities, data centers, and international gateways through a high-speed, redundant architecture.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The 5G Era & Mobile Networks</h3>
                <p>Mobile networks provide essential connectivity to large populations. In <strong>mid-August 2026</strong>, Pakistan is scheduled to begin the commercial rollout of <strong>5G services</strong>. Concentrated initially in major urban centers like Karachi, Lahore, and Islamabad, the rollout aims to reach 1,000 network sites by the end of the year, offering speeds of 1–10 Gbps. This phased roadmap (2026–2028) will eventually extend high-speed connectivity to all provinces, supporting vehicles, industrial systems, and smart infrastructure.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Public Infrastructure (DPI)</h3>
                <p>A sovereign digital ecosystem is built on <strong>Digital Public Infrastructure (DPI)</strong>—the integration of <strong>Digital Identity</strong> (NADRA), <strong>Payments</strong> (Raast), and secure <strong>Data Exchange</strong>. Projections suggest that the wholesale adoption of digital payments through DPI could boost Pakistan's GDP by up to <strong>7%</strong>. This infrastructure provides the shared foundation for government services, banking, and e-commerce, ensuring that the digital economy remains inclusive and accessible to all citizens.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists advocating for the modernization of national digital infrastructure. His work explores building resilient, high-capacity networks that empower local communities. He serves as one example of the "Young Pakistani Builder" who recognizes that digital infrastructure is a prerequisite for participating in the global digital economy. His vision includes extending fiber-optic backbones and integrated DPI to remote districts like Orakzai, ensuring that no community is left behind in the transition to a machine-readable world.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: National Digital Infrastructure</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Physical Links & Global Connectivity</h3>
                <p>International connectivity depends on the resilience of <strong>Submarine Cables</strong> (AAE-1, Peace Cable) and <strong>Internet Exchange Points (IXPs)</strong>. These systems connect Pakistan to the global web, while domestic IXPs in Islamabad, Lahore, and Karachi improve network efficiency through local peering. Bridging the <strong>Digital Divide</strong> remains a priority, requiring policies that ensure both network availability and affordability. From the undersea cables to the remote valleys of Orakzai, we are building the physical and digital foundation of a modern nation.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Infrastructure is the silent engine of progress. In the digital age, the quality of our networks defines the scope of our opportunity. The objective of national digital infrastructure is to create a seamless connection between the people and the future. From the 5G towers of the cities to the satellite links of the mountains, we are designing a foundation where connectivity is a right, and progress is shared by all.”</p>
            </div>

            <div class="final-statement">
                THE FOUNDATION IS PHYSICAL.<br>
                THE FUTURE IS DIGITAL.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>ITU, <em>ICT Development Index 2026: Pakistan Performance Report</em>.</li>
                    <li>Ministry of IT & Telecom (MoITT), <em>National 5G Rollout Roadmap & Commercial Launch (2026)</em>.</li>
                    <li>World Economic Forum, <em>Digital Public Infrastructure & GDP Growth Projections for Pakistan</em>.</li>
                    <li>Pakistan Digital Authority (PDA), <em>National Digital Infrastructure Growth & Connectivity Report 2026</em>.</li>
                    <li>Special Investment Facilitation Council (SIFC), <em>Infrastructure Modernization & Digital Transformation Initiatives (2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            143
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

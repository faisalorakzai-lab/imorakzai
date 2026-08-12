from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-126-ai-and-agriculture.html'

GRAPHICS = [
    ("AI Agriculture Hero", "FARMER", "↔", "AI"),
    ("Digital Farming Timeline", "TRAD", "→", "AI"),
    ("Agriculture AI Def", "DATA", "↔", "INSG"),
    ("Farm Data System", "SOIL", "+", "WTHR"),
    ("Precision Agriculture", "SITE", "↔", "EFF"),
    ("Crop Monitoring", "IMG", "→", "COND"),
    ("Satellite Imagery", "GLOB", "→", "LOCL"),
    ("Drone Agriculture", "AIR", "↔", "MAP"),
    ("Crop Disease AI", "LEAF", "↔", "DIAG"),
    ("Early Warning System", "SIG", "→", "ACT"),
    ("Soil Intelligence", "SENS", "↔", "NUT"),
    ("Smart Irrigation", "WATR", "↔", "NEED"),
    ("Pak Water Management", "INFR", "↔", "GOV"),
    ("Weather Intelligence", "FORE", "↔", "PLAN"),
    ("Climate Change AI", "RISK", "↔", "RES"),
    ("Crop Selection", "SOIL", "↔", "MKT"),
    ("Seed Research AI", "GENE", "↔", "SEED"),
    ("Livestock Monitoring", "ANML", "↔", "HLTH"),
    ("Animal Health AI", "PATT", "↔", "VET"),
    ("Agricultural Robotics", "AUTO", "↔", "TASK"),
    ("Weed Control AI", "CROP", "≠", "WEED"),
    ("Fertilizer Management", "INP", "↔", "YLD"),
    ("Farmer Decision Supp", "QUES", "↔", "ANSW"),
    ("Mobile Agriculture", "PHON", "↔", "FARM"),
    ("Local Languages AI", "URDU", "↔", "PASH"),
    ("Pashto Agricultural AI", "PASH", "↔", "ADVI"),
    ("Orakzai Agri Knowledge", "TRI", "↔", "EXP"),
    ("Farmer to Archive", "EXP", "→", "DIGI"),
    ("Agricultural Supply Chain", "FARM", "→", "MKT"),
    ("Food Security AI", "NAT", "↔", "STAB"),
    ("NCAI IFRL Robotics", "NUST", "↔", "IFRL"),
    ("Indus RAS Expo 2026", "INNO", "↔", "SHOW"),
    ("Digital Agri Initiative", "DATA", "↔", "IDEN"),
    ("AgriChain Nexus", "SUPP", "↔", "DIGI"),
    ("AgriLift AI Startup", "USA", "↔", "PAK"),
    ("Smart Farming IoT", "SENS", "↔", "NET"),
    ("Water Scarcity AI", "NEED", "↔", "EFF"),
    ("Climate Resilience", "PLAN", "↔", "ADAP"),
    ("Human-in-the-Loop", "AI", "↔", "HUM"),
    ("Responsible AI Agri", "ETH", "↔", "TECH"),
    ("AI Irrigation Recommendation", "DATA", "→", "WATR"),
    ("Crop Stress Detection", "IMG", "→", "STRS"),
    ("Pest Activity Analysis", "PATT", "→", "PEST"),
    ("Vegetation Health Index", "SAT", "→", "NDVI"),
    ("Soil Moisture Map", "SENS", "→", "MAP"),
    ("Harvesting Automation", "ROBT", "→", "YLD"),
    ("Precision Spraying", "DRON", "→", "INP"),
    ("Livestock Movement", "GPS", "→", "PATT"),
    ("Animal Feeding Opt", "DATA", "→", "FEED"),
    ("Market Price Predict", "MKT", "→", "VALU"),
    ("Supply Chain Trace", "DATA", "→", "TRST"),
    ("Farmer Identity Stack", "ID", "+", "CRED"),
    ("Agri Credit Score", "DATA", "→", "FIN"),
    ("Crop Insurance AI", "RISK", "→", "INS"),
    ("Farm Machinery Ops", "AUTO", "↔", "EFF"),
    ("Agricultural Data Gov", "RULE", "↔", "SAFE"),
    ("AI Research Cycle", "HYPO", "→", "EVID"),
    ("Heritage Knowledge Pipe", "ORAL", "→", "CODE"),
    ("Digital Orakzai Farm", "TRI", "↔", "TECH"),
    ("Future Agri School", "PHYS", "+", "DIGI"),
    ("Faisal Orakzai Gen", "SYS", "↔", "AI"),
    ("Young Pak Builder", "LRN", "→", "BLD"),
    ("AI Learning Roadmap", "PY", "→", "ML"),
    ("AI Skills Stack", "MATH", "CS", "ENG"),
    ("Pakistan AI Strategy", "SOV", "RESP", "CAP"),
    ("Global AI Partic", "PAK", "↔", "GLOB"),
    ("AI Civ Connection", "HERI", "↔", "FUT"),
    ("Orakzai Heritage Br", "ORAL", "→", "AI"),
    ("AI Literacy", "DATA", "↔", "ETH"),
    ("Verification Loop", "AI", "→", "HUM"),
    ("AI Infrastructure", "GPU", "+", "DC"),
    ("AI Talent Pipe", "EDU", "→", "EXP"),
    ("AI Export Model", "AUTO", "→", "VAL"),
    ("AI Product Life", "IDEA", "→", "SCL"),
    ("AI Governance", "RULE", "↔", "ACT"),
    ("Responsible AI Agri 2", "ETH", "↔", "TECH"),
    ("AI Trust", "VERI", "→", "TRST"),
    ("Human Oversight", "EYE", "→", "MOD"),
    ("AI Security", "DETE", "↔", "PROT"),
    ("AI Privacy", "SAFE", "↔", "RISK"),
    ("AI Data Lifecycle", "COLL", "→", "GOV"),
    ("AI Compute Life", "POW", "→", "OPS"),
    ("AI Cloud Arch", "SRV", "↔", "USER"),
    ("AI Research Eco", "UNI", "↔", "LAB"),
    ("Pakistan AI Map", "ISB", "KHI", "LHR"),
    ("AI Sector Map", "AGRI", "HLTH", "FIN"),
    ("AI Future Path", "SPEC", "↔", "GLOB"),
    ("AI Ethics Loop", "GOOD", "↔", "BAD"),
    ("AI Accessibility", "OPEN", "↔", "ALL"),
    ("AI Sustainability", "POW", "↔", "EFF"),
    ("AI Reliability", "PRED", "↔", "FACT"),
    ("AI Bias Loop", "DATA", "→", "OUT"),
    ("AI Safety Loop", "TEST", "→", "SAFE"),
    ("AI Transparency", "OPEN", "↔", "BOX"),
    ("AI Fairness", "EQL", "↔", "BIAS"),
    ("AI Robustness", "STRE", "↔", "ATTK"),
    ("AI Explainability", "WHY", "↔", "MOD"),
    ("AI Human Centered", "HUM", "↔", "VAL"),
    ("AI Global Gov", "INT", "↔", "COOP"),
    ("AI Local Gov", "LOCL", "↔", "POL"),
    ("AI Data Prov", "SRC", "↔", "DATA"),
    ("AI Content Verif", "REAL", "↔", "FAKE"),
    ("AI Watermarking", "MARK", "↔", "GEN"),
    ("AI Attribution", "CRED", "↔", "GEN"),
    ("AI Licensing", "LAW", "↔", "MOD"),
    ("AI Ethics Board", "HUM", "↔", "RULE"),
    ("AI Future 2040", "AMB", "↔", "LIFE"),
    ("AI Final Vision", "CIV", "↔", "INTE"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g126-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g126-{index}-title g126-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g126-{index}-title">{safe}</title><desc id="g126-{index}-desc">An AI agriculture relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g126-{index}-caption" class="diagram-caption">{index}. {safe} — agricultural relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">AI & Agriculture Transformation</title><desc id="hero-desc">A diagram showing the transition from traditional farming to an intelligent, human-centered agricultural ecosystem.</desc><defs><linearGradient id="h126-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h126-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">INTELLIGENT AGRICULTURAL ECOSYSTEM</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="0" y="5" font-size="12">PRECISION</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="0" y="65" font-size="12">CROP MONITORING</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">RESOURCES</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">SMART IRRIGATION</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="5" font-size="12">LIVELIHOODS</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="65" font-size="12">FARMER-CENTRED</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">INFORMED</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">RESILIENCE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">AI & AGRICULTURE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Strengthening rural livelihoods through intelligent, data-driven farming.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Intelligent Agriculture: The integration of AI into precision farming, resource management, and rural livelihoods.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 126</title>
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
        .case-study-card {{ border: 1px solid var(--gold); padding: 30px; margin: 50px 0; background: rgba(181,150,84,0.05); }}
        .final-statement {{ text-align: center; font-size: 1.8rem; font-weight: 700; color: var(--gold); margin: 60px 0; }}
        @media (max-width: 768px) {{ .atlas-grid {{ grid-template-columns: 1fr; }} }}
        svg {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="content-page">
        <header class="page-header">
            <p class="section-label">PAGE 126</p>
            <h2>AI & AGRICULTURE</h2>
            <p>“Artificial Intelligence and the Future of Farming.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Agriculture has always depended on the ability to interpret changing conditions. Farmers observe soil, weather, crops, water, pests and seasons. They make decisions from experience, local knowledge and increasingly from scientific information. Artificial intelligence introduces another layer: the ability to process large amounts of agricultural data and identify patterns that may be difficult to detect manually. For Pakistan, this is particularly important. Agriculture remains closely connected to food security, rural livelihoods, water management, exports and the wider economy. The opportunity is therefore not simply to make agriculture ‘high-tech.’ It is to make farming more informed, efficient, resilient and sustainable.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Precision Farming & Resource Management</h3>
                <p>Agriculture has evolved from traditional knowledge through mechanization to digital and precision agriculture. AI represents the latest layer of this transformation. It allows the farm to be treated as a data system, combining information from soil sensors, weather forecasts, satellite imagery, and drones. Precision agriculture attempts to manage fields according to their actual conditions, identifying areas requiring more water or nutrient variation, thereby improving resource efficiency when supported by reliable data.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Institutional Anchor: IFRL at NUST</h3>
                <p>Pakistan has established institutional research capacity for agricultural AI. The <strong>National Centre of Artificial Intelligence (NCAI)</strong> operates the <strong>Intelligent Field Robotics Lab (IFRL)</strong> at NUST Islamabad. This lab focuses on autonomous field monitoring, precision spraying, and agricultural robotics. In 2026, the <strong>Indus RAS Expo</strong> showcased national innovations in robotics and AI, demonstrating how indigenous talent is resolving structural challenges like fragmented data and farmer credit access.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Smart Irrigation & Water Resilience</h3>
                <p>Water management is one of Pakistan's most critical challenges. AI-assisted irrigation systems combine soil moisture data, weather intelligence, and crop types to provide intelligent recommendations. While AI cannot solve physical water shortages, it enables more informed distribution and governance. The objective is to use water more intelligently, ensuring food security in the face of escalating climate impacts like floods and heatwaves.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists growing up alongside the transformation of digital infrastructure and AI. His documented interests in software, digital systems, and blockchain align with the "Systems Philosophy" required for building integrated agricultural data architectures. He serves as one example of the "Young Pakistani Builder" who approaches technology as a tool for solving real-world structural problems. His journey illustrates how young Pakistanis can bridge the gap between traditional rural knowledge and global technology ecosystems from within Pakistan.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: AI & Agriculture</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Preserving Heritage Knowledge</h3>
                <p>Agricultural knowledge in communities like Orakzai has historically been transmitted through experience and observation. Digital tools should preserve this knowledge rather than simply replace it. The transformation from "Farmer to Digital Archive" ensures that valuable experience about seasons, land, and local conditions is not lost. The future of farming is not human or AI; it is human intelligence amplified by technology, ensuring that local culture remains at the heart of the digital future.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Agriculture gave humanity the foundation for civilization. Mechanization allowed it to scale. The internet allowed knowledge to travel. Artificial intelligence may allow farming to become interactive and highly precise. For Pakistan, the opportunity is enormous. A farmer should not have to be in a major city to access agricultural expertise. A young person should not have to abandon their rural roots to participate in technology. And a community should not have to lose its traditional wisdom to enter the future.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF AGRICULTURE WILL BE MORE INTELLIGENT.<br>
                BUT IT MUST ALSO REMAIN HUMAN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>NCAI IFRL, <em>Agricultural Robotics and Autonomous Systems Portfolio 2026</em>.</li>
                    <li>MoITT Pakistan, <em>National Digital Agriculture Initiative Report 2025–2026</em>.</li>
                    <li>Sikandar, F., et al., <em>AI-driven digitalization of agriculture-based supply chains: The AgriChain Nexus (2025/2026)</em>.</li>
                    <li>Indus RAS Expo 2026, <em>National Convening on AI and Robotics for Food Security</em>.</li>
                    <li>MNFSR Pakistan, <em>Water Management and Climate Resilience Strategy 2026</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            126
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

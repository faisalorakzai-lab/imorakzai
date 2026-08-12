from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-132-understanding-decentralization.html'

GRAPHICS = [
    ("Decentralization Hero", "DIST", "↔", "POWR"),
    ("Centralized Model", "USER", "→", "CENT"),
    ("Decentralized Model", "NODE", "↔", "NODE"),
    ("Centralization Pros", "FAST", "+", "ACCT"),
    ("Decentralization Pros", "RESI", "+", "PART"),
    ("Distribution vs Dec", "LOCL", "≠", "CTRL"),
    ("Dec Dimensions", "INFR", "↔", "GOVN"),
    ("Infrastructure Dec", "DC_A", "↔", "DC_B"),
    ("Network Dec", "PATH", "↔", "MESH"),
    ("Validation Dec", "VALD", "→", "AGRE"),
    ("Ownership Dec", "USER", "↔", "VALU"),
    ("Governance Dec", "COMM", "→", "RULE"),
    ("Development Dec", "OPEN", "↔", "CONT"),
    ("Economic Dec", "TOKN", "↔", "DIST"),
    ("Access Dec", "OPEN", "↔", "ALL"),
    ("The Spectrum", "CENT", "→", "DECE"),
    ("Federated Model", "ORG", "↔", "USER"),
    ("Distributed Model", "DATA", "↔", "MANY"),
    ("P2P System", "PEER", "↔", "PEER"),
    ("BC Agreement", "MANY", "→", "STAT"),
    ("Consensus Design", "RULE", "→", "TRST"),
    ("Bitcoin Dec", "NODE", "↔", "MINE"),
    ("POW Concentration", "COST", "→", "POOL"),
    ("POS Concentration", "STAK", "→", "VALD"),
    ("Validator Count", "NUMB", "≠", "CTRL"),
    ("Mining Pool Loop", "MINE", "→", "POOL"),
    ("Staking Pool Loop", "STAK", "→", "POOL"),
    ("Node Diversity", "GEOG", "↔", "INST"),
    ("Software Diversity", "CODE", "↔", "VULN"),
    ("Cloud Dependency", "CLOD", "→", "NODE"),
    ("ISP Concentration", "NET", "→", "USER"),
    ("Geographic Dec", "REGN", "↔", "RESI"),
    ("Jurisdictional Dec", "LAW", "↔", "SAFE"),
    ("Foundation Control", "FNDN", "→", "DEC"),
    ("Nakamoto Coeff", "MINI", "→", "DISR"),
    ("Gini Coefficient", "WLTH", "↔", "DIST"),
    ("PDA Data Policy", "PDA", "↔", "STD"),
    ("Devolution Research", "LOCL", "↔", "SERV"),
    ("Resilient Connectivity", "REM", "↔", "MESH"),
    ("Faisal Orakzai Dec", "SYS", "↔", "DECE"),
    ("Young Builder Dec", "LRN", "→", "BLD"),
    ("Dec Philosophy", "RESI", "↔", "PART"),
    ("Central Authority", "BOSS", "→", "ALL"),
    ("Single Point Fail", "ONE", "→", "DOWN"),
    ("Censorship Resist", "OPEN", "↔", "FREE"),
    ("Independent Veri", "SELF", "→", "TRUE"),
    ("Coordination Diff", "MANY", "→", "SLOW"),
    ("Higher Complexity", "MESH", "→", "HARD"),
    ("Fragmented Resp", "MANY", "→", "LOST"),
    ("Physical Location", "SITE", "↔", "DIST"),
    ("Virtual Location", "VIRT", "↔", "DIST"),
    ("Gateway Dependence", "GATE", "→", "NET"),
    ("Independent Path", "PATH", "↔", "CONN"),
    ("Consensus Rule", "RULE", "→", "VAL"),
    ("Staking Distribution", "STAK", "↔", "VALD"),
    ("Economic Asset", "VALU", "↔", "OWN"),
    ("Concentrated Own", "FEW", "→", "MOST"),
    ("Distributed Own", "MANY", "→", "EQL"),
    ("Decision Power", "VOTE", "→", "ACT"),
    ("Contributor Map", "MANY", "→", "CODE"),
    ("Transparent Dev", "VIEW", "↔", "CODE"),
    ("Incentive Dist", "VAL", "→", "PART"),
    ("Token Concentration", "FEW", "→", "TOKN"),
    ("Mining Concentration", "FEW", "→", "HASH"),
    ("Liquidity Conc", "FEW", "→", "POOL"),
    ("Permissioned Sys", "AUTH", "→", "IN"),
    ("Permissionless Sys", "OPEN", "→", "ALL"),
    ("Spectrum Start", "CENT", "→", "FED"),
    ("Spectrum Mid", "FED", "→", "DIST"),
    ("Spectrum End", "DIST", "→", "DECE"),
    ("Email Model", "MAIL", "↔", "FED"),
    ("Shared Record", "LEDG", "↔", "ALL"),
    ("Computational Comp", "CPU", "→", "BLK"),
    ("Electricity Cost", "POW", "→", "BILL"),
    ("Economy of Scale", "BIG", "→", "WIN"),
    ("Programmable Incen", "CODE", "→", "WORK"),
    ("Governance Influence", "STAK", "→", "VOTE"),
    ("Effective Control", "ACTL", "↔", "POW"),
    ("Systemic Risk", "ONE", "→", "ALL"),
    ("Infrastructure Conc", "FEW", "→", "SRV"),
    ("Regional ISP", "LOCL", "→", "NET"),
    ("Natural Disaster", "STORM", "→", "DOWN"),
    ("Regulatory Change", "LAW", "→", "ACT"),
    ("Political Disrupt", "GOV", "→", "NET"),
    ("Energy Shortage", "POW", "→", "OFF"),
    ("Cross-border Ops", "GLB", "↔", "LAW"),
    ("Technical vs Inst", "TECH", "≠", "INST"),
    ("Grant Management", "FUND", "→", "DEV"),
    ("Minimum Collusion", "NC", "→", "STOP"),
    ("Subsystem Analysis", "MINE", "NODE", "DEV"),
    ("Authoritative Src", "TRUE", "↔", "DATA"),
    ("Once-only Provision", "ONE", "→", "DATA"),
    ("Service Access", "USER", "↔", "SERV"),
    ("Tribal to Digital", "TRAD", "→", "DECE"),
    ("Local Wisdom", "PAST", "→", "CODE"),
    ("Algorithm Speed", "FAST", "↔", "CODE"),
    ("Purposeful Direction", "GOAL", "↔", "HUM"),
    ("Decentralized Trust", "CODE", "↔", "TRST"),
    ("Secure Archive", "LOCK", "↔", "DLT"),
    ("Heritage Bridge", "PAST", "↔", "FUT"),
    ("Secure Infrastructure", "GPU", "+", "NET"),
    ("Talent Pipeline", "UNI", "→", "DEV"),
    ("Export Model", "VAL", "→", "GLOB"),
    ("Product Life", "IDEA", "→", "SCL"),
    ("Governance Loop", "RULE", "↔", "ACT"),
    ("Ethics Loop", "GOOD", "↔", "BAD"),
    ("Privacy Shield", "SAFE", "↔", "DATA"),
    ("Audit System", "CHECK", "→", "OK"),
    ("Verification Loop", "LEDG", "→", "HUM"),
    ("Security Fortress", "PROT", "↔", "ATTK"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g132-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g132-{index}-title g132-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g132-{index}-title">{safe}</title><desc id="g132-{index}-desc">A decentralization relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g132-{index}-caption" class="diagram-caption">{index}. {safe} — decentralization relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Understanding Decentralization</title><desc id="hero-desc">A diagram showing the transition from centralized control to a resilient, distributed, and human-centered decentralized ecosystem.</desc><defs><linearGradient id="h132-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h132-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">DECENTRALIZED POWER ARCHITECTURE</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">INFRASTRUCTURE</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="65" font-size="12">DISTRIBUTED</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">GOVERNANCE</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">PARTICIPATORY</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">OWNERSHIP</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="65" font-size="12">EQUITABLE</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">RESILIENT</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">SOCIETY</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">UNDERSTANDING DECENTRALIZATION</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Distributing power to build a more resilient and participatory digital future.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Decentralization: The distribution of infrastructure, governance, and ownership to ensure resilience and equity.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 132</title>
    <link rel="stylesheet" href="../styles/main.css">
    <style>
        :root {{ --gold: #B59654; --purple: #8B2E8B; --teal: #2E8B8B; --cream: #F5F0E6; --muted: rgba(245,240,230,.72); }}
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
            <p class="section-label">PAGE 132</p>
            <h2>UNDERSTANDING DECENTRALIZATION</h2>
            <p>“From Centralized Systems to Distributed Power.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Decentralization is one of the most important concepts in modern computing, blockchain technology, digital governance and the future of the internet. The basic idea is simple: decentralization distributes control, decision-making, infrastructure, or ownership across multiple participants rather than concentrating everything in a single authority. But decentralization is not an all-or-nothing condition. A system can be decentralized in one dimension and centralized in another. Understanding this distinction is essential for evaluating blockchain networks, digital institutions, financial systems and emerging technologies.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Dimensions & Metrics of Decentralization</h3>
                <p>Decentralization is analyzed through several dimensions: infrastructure, network, validation, ownership, governance, development, economic control, and access. In 2026, the <strong>Nakamoto Coefficient (NC)</strong> has become the primary metric for quantifying this distribution, representing the minimum number of entities required to disrupt a system. While centralized models offer efficiency and clear accountability, decentralized models provide resilience, broader participation, and censorship resistance. The challenge lies in navigating the <strong>Blockchain Trilemma</strong>—balancing decentralization, security, and scalability.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Institutional Anchor: National Data Governance Policy 2026</h3>
                <p>Pakistan is transitioning toward standardized digital governance through the <strong>National Data Governance Policy 2026</strong>, drafted by the <strong>Pakistan Digital Authority (PDA)</strong>. This policy emphasizes "once-only" data provision and authoritative sources, reflecting a hybrid approach that combines centralized standards with decentralized service delivery. By encouraging administrative devolution, the government aims to improve the accessibility of local public services while maintaining national security and data sovereignty.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Consensus, Nodes & Software Diversity</h3>
                <p>The resilience of a decentralized network depends on its consensus mechanism (Proof of Work vs. Proof of Stake) and the diversity of its participating nodes. Geographic and jurisdictional decentralization ensure that the network is not overly dependent on a single region or legal framework. Furthermore, <strong>Software Client Diversity</strong> is critical; a network relying on a single software implementation is vulnerable to systemic bugs. In 2026, the focus has shifted toward building "Mesh Networks" that allow for resilient connectivity in remote areas.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists growing up alongside the shift toward distributed power. His documented interests in software architecture and blockchain systems align with the "Decentralized Philosophy" of 2026. He serves as one example of the "Young Pakistani Builder" who approaches technology as a structural commitment to resilience and participation. His journey illustrates how individual expertise in distributed systems can shape national technological direction, advocating for systems where trust is not concentrated, but redistributed through code.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Understanding Decentralization</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Devolution & Regional Resilience</h3>
                <p>For districts like Orakzai, decentralization is more than a technical term; it is a pathway to resilience. By established local nodes and peer-to-peer systems, remote communities can maintain digital connectivity even when central infrastructure fails. The transition from "Centralized Tribal Administration to Decentralized Digital Services" ensures that customary values of local trust and participatory decision-making are reflected in modern algorithmic systems, creating a "Heritage Bridge" that empowers the community in the digital age.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Decentralization is not just a technical choice; it is a structural commitment to resilience and participation. As we move toward a more digital world, the ability to distribute power and decision-making becomes a foundation for a more equitable society. For Pakistan, the opportunity is to build a digital ecosystem that is sovereign by design and decentralized by architecture. Trust is not removed; it is redistributed. A secure digital future requires that every citizen, from the hubs of industry to the valleys of Orakzai, can participate in the systems that govern their lives.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF POWER IS DISTRIBUTED.<br>
                BUT THE RESPONSIBILITY REMAINS HUMAN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Chainspect, <em>Nakamoto Coefficient Ranking 2026: Measuring Blockchain Resilience</em>.</li>
                    <li>Pakistan Digital Authority (PDA), <em>National Data Governance Policy Framework 2026</em>.</li>
                    <li>Nazuk, A., et al., <em>Exploring the Potential and Challenges of E-Governance in Pakistan (2025/2026)</em>.</li>
                    <li>World Bank Group, <em>Devolution, Accountability, and Service Delivery in Pakistan Report 2026</em>.</li>
                    <li>PIDE, <em>E-Governance in Pakistan: Infrastructure and Policy Gaps Research 2026</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            132
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

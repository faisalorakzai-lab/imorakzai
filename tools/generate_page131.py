from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-131-blockchain-technology.html'

GRAPHICS = [
    ("Blockchain Hero", "DLT", "↔", "TRST"),
    ("Blockchain Model", "TXN", "→", "LEDG"),
    ("Blockchain Def", "DIST", "↔", "VERI"),
    ("Traditional vs BC", "CENT", "≠", "DECE"),
    ("Distributed System", "NODE", "↔", "NETW"),
    ("Cryptography Role", "KEY", "→", "SEC"),
    ("Hash Function", "DATA", "→", "HASH"),
    ("Digital Signature", "PRIV", "→", "SIGN"),
    ("Key Pair Model", "PUB", "↔", "PRIV"),
    ("Block Structure", "DATA", "+", "LINK"),
    ("The Chain Link", "BLK1", "→", "BLK2"),
    ("Immutability Prop", "CONS", "+", "CRYP"),
    ("Node Network", "NODE", "↔", "PEER"),
    ("P2P Network", "MESH", "↔", "CONN"),
    ("Distributed Ledger", "REPL", "↔", "STAT"),
    ("Consensus Rules", "VALD", "→", "AGRE"),
    ("Proof of Work", "COMP", "→", "SEC"),
    ("Proof of Stake", "STAK", "→", "VALD"),
    ("Validator Model", "STAK", "↔", "VOTE"),
    ("Miner vs Validator", "POW", "≠", "POS"),
    ("Decentralization", "GOV", "↔", "INFR"),
    ("Decentralized Spec", "CENT", "→", "DECE"),
    ("Public Blockchain", "OPEN", "↔", "VIEW"),
    ("Private Blockchain", "AUTH", "↔", "REST"),
    ("Consortium Net", "ORG1", "↔", "ORG2"),
    ("Layered Arch", "NET", "→", "APPS"),
    ("Smart Contract", "CODE", "→", "ACTN"),
    ("Oracle System", "OFF", "→", "ON"),
    ("Data Bridge", "EXT", "↔", "INT"),
    ("Blockchain Trilemma", "SEC", "SCL", "DEC"),
    ("Layer-2 Network", "L1", "↔", "L2"),
    ("Virtual Assets Act", "LAW", "↔", "VAL"),
    ("PVARA Regulator", "PDA", "↔", "RULE"),
    ("National Crypto Co", "GOV", "↔", "STRT"),
    ("NUST SINES Lab", "UNI", "↔", "TECH"),
    ("Digital Asset Reserve", "BTC", "↔", "NAT"),
    ("Crypto Adoption #3", "PAK", "↔", "GLB"),
    ("Tokenization Model", "ASST", "→", "TOKN"),
    ("Supply Chain BC", "PROD", "→", "TRAC"),
    ("Digital Identity BC", "ID", "↔", "SOV"),
    ("Governance BC", "VOTE", "↔", "LEDG"),
    ("Financial Infra BC", "BANK", "↔", "DLT"),
    ("Shared State", "SYNC", "↔", "ALL"),
    ("Fault Tolerance", "FAIL", "≠", "STOP"),
    ("Replicated State", "COPY", "↔", "CONS"),
    ("Hash Collision Prot", "UNIQ", "↔", "SAFE"),
    ("Private Key Guard", "LOCK", "↔", "KEY"),
    ("Public Address ID", "ADDR", "↔", "USER"),
    ("Timestamp Block", "TIME", "↔", "DATA"),
    ("Reference Link", "PREV", "→", "CURR"),
    ("Detect Modification", "MOD", "→", "FAIL"),
    ("Economic Incentive", "VAL", "→", "WORK"),
    ("Technical Incentive", "RULE", "→", "PART"),
    ("Validator Penalty", "BAD", "→", "SLASH"),
    ("Network Resilience", "FAIL", "↔", "UP"),
    ("Ledger Replication", "DATA", "→", "MANY"),
    ("Byzantine Fault", "NODE", "≠", "TRST"),
    ("Validator Attest", "SIGN", "→", "BLK"),
    ("Miner Hardware", "ASIC", "→", "HASH"),
    ("Energy Efficiency", "POW", "→", "POS"),
    ("Infrastructure Dec", "SRV", "↔", "MANY"),
    ("Ownership Dec", "USER", "↔", "VAL"),
    ("Hybrid Network", "PRIV", "+", "PUB"),
    ("Smart Contract Rule", "IF", "→", "THEN"),
    ("Automated Agreement", "SIGN", "→", "EXEC"),
    ("Off-chain Event", "REAL", "→", "DATA"),
    ("Oracle Trust Model", "SRC", "↔", "TRST"),
    ("Scaling Challenge", "VOL", "↔", "SPD"),
    ("Low Latency BC", "FAST", "↔", "SEC"),
    ("Affordability BC", "COST", "↔", "USER"),
    ("Technical Innovation", "NEW", "→", "FIX"),
    ("Sovereign Identity", "SELF", "↔", "ID"),
    ("Orakzai Diaspora BC", "GLB", "→", "LOCL"),
    ("Remittance Cost BC", "FEES", "→", "LOW"),
    ("Heritage Preservation", "PAST", "→", "DLT"),
    ("Digital Archive BC", "MEM", "↔", "SEC"),
    ("Faisal Orakzai BC", "SYS", "↔", "DLT"),
    ("Young Builder BC", "LRN", "→", "BLD"),
    ("Blockchain Literacy", "CODE", "↔", "ETH"),
    ("Verification Loop BC", "LEDG", "→", "HUM"),
    ("Blockchain Infra", "NODE", "+", "NET"),
    ("Blockchain Talent", "EDU", "→", "DEV"),
    ("Blockchain Export", "VAL", "→", "GLOB"),
    ("Product Lifecycle BC", "DEV", "→", "MKT"),
    ("Blockchain Governance", "RULE", "↔", "SAFE"),
    ("Responsible BC", "ETH", "↔", "TECH"),
    ("Blockchain Trust", "VERI", "→", "TRST"),
    ("Human Oversight BC", "EYE", "→", "MOD"),
    ("Blockchain Security", "DETE", "↔", "PROT"),
    ("Blockchain Privacy", "SAFE", "↔", "RISK"),
    ("Data Lifecycle BC", "COLL", "→", "GOV"),
    ("Compute Lifecycle BC", "POW", "→", "OPS"),
    ("Cloud Architecture BC", "SRV", "↔", "USER"),
    ("Research Eco BC", "UNI", "↔", "LAB"),
    ("Pakistan Crypto Map", "ISB", "KHI", "LHR"),
    ("Sector Map BC", "FIN", "GOV", "ID"),
    ("Future Path BC", "SOV", "↔", "GLOB"),
    ("Ethics Loop BC", "GOOD", "↔", "BAD"),
    ("Accessibility BC", "OPEN", "↔", "ALL"),
    ("Sustainability BC", "POW", "↔", "POS"),
    ("Reliability BC", "PRED", "↔", "FACT"),
    ("Bias Loop BC", "DATA", "→", "OUT"),
    ("Safety Loop BC", "TEST", "→", "SAFE"),
    ("Identity Loop BC", "USER", "↔", "ID"),
    ("Transaction Loop", "SEND", "→", "RECV"),
    ("Validation Loop", "CHECK", "→", "OK"),
    ("Consensus Loop", "AGRE", "→", "SYNC"),
    ("Linkage Loop", "PREV", "↔", "NEXT"),
    ("Security Loop", "PROT", "↔", "ATTK"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g131-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g131-{index}-title g131-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g131-{index}-title">{safe}</title><desc id="g131-{index}-desc">An AI governance relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g131-{index}-caption" class="diagram-caption">{index}. {safe} — blockchain relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Blockchain Technology Framework</title><desc id="hero-desc">A diagram showing the integrated framework for blockchain, distributed ledgers, and decentralized trust.</desc><defs><linearGradient id="h131-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h131-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">DECENTRALIZED TRUST ECOSYSTEM</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DISTRIBUTED</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="65" font-size="12">LEDGER</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CONSENSUS</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">IMMUTABILITY</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">CRYPTOGRAPHY</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="65" font-size="12">SECURITY</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">SOVEREIGN</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">INFRASTRUCTURE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">BLOCKCHAIN TECHNOLOGY</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Distributed Ledgers to a New Digital Infrastructure.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Blockchain Technology: The integrated framework for distributed coordination, verification, and shared state.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 131</title>
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
            <p class="section-label">PAGE 131</p>
            <h2>BLOCKCHAIN TECHNOLOGY</h2>
            <p>“From Distributed Ledgers to a New Digital Infrastructure.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Blockchain technology emerged as a new approach to maintaining a shared digital record without requiring every participant to rely on a single central database. Its development is closely connected with cryptography, distributed systems, peer-to-peer networking and digital currencies. Today, blockchain is used and researched across areas including digital assets, payments, decentralized applications, tokenization, supply chains, digital identity, governance and financial infrastructure. Blockchain should not be understood simply as cryptocurrency. It is better understood as a family of technologies for distributed coordination, verification and shared state.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Distributed Systems & Cryptographic Trust</h3>
                <p>At its core, blockchain is a distributed data structure linked through cryptographic mechanisms. Unlike traditional databases that rely on a central authority, blockchain distributes responsibility across a network of nodes. Cryptography provides the essential tools—hash functions, digital signatures, and public-key pairs—to ensure that data is identified, transactions are verified, and the network's rules are followed. This emergent property of immutability is not magic; it is the result of combining cryptography, consensus, and network participation.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Institutional Anchor: Virtual Assets Act 2026</h3>
                <p>Pakistan has entered a new phase of digital finance with the enactment of the <strong>Virtual Assets Act 2026</strong>. This landmark legislation officially establishes the <strong>Pakistan Virtual Assets Regulatory Authority (PVARA)</strong> as the permanent regulator for the country's $300 billion digital asset market. By formalizing the sector, the government aims to encourage innovation in tokenization and decentralized finance while ensuring security and institutional governance through the <strong>National Crypto Council</strong>.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Consensus, Scalability & Smart Contracts</h3>
                <p>Distributed networks require rules to determine valid states, provided by consensus mechanisms like Proof of Work or Proof of Stake. Modern blockchain ecosystems often use layered architectures, where smart contracts—software executing according to predefined rules—automate digital agreements. The ongoing research challenge, known as the <strong>Blockchain Trilemma</strong>, involves balancing decentralization, security, and scalability. Layer-2 networks and oracles are critical innovations that bridge the gap between secure chains and real-world data.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists growing up alongside the transformation of digital infrastructure and blockchain. His documented interests in software architecture, blockchain systems, and digital infrastructure align with the "Decentralized & Secure" philosophy of 2026. He serves as one example of the "Young Pakistani Builder" who approaches technology as a tool for solving real-world structural problems while advocating for responsible and transparent development. His journey illustrates how individual expertise in distributed systems can shape national technological direction in the age of decentralized trust.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Blockchain Technology</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Sovereign Infrastructure & Regional Impact</h3>
                <p>For regions like Orakzai, blockchain technology offers the potential for sovereign digital identity and lower-cost international remittances for the diaspora. By establishing indigenous research capacity at institutions like <strong>NUST SINES</strong>, Pakistan ensures that its digital infrastructure is resilient and independent. The shift from "Centralized to Distributed Governance" allows for the preservation of cultural heritage and oral histories in secure, immutable archives, bridging the tribal past with a decentralized digital future.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Blockchain is not just about assets; it is about the architecture of trust. As we move toward a more digital world, the ability to maintain shared, verifiable records without central intermediaries becomes a foundation for a new kind of digital infrastructure. For Pakistan, the opportunity is to build a blockchain ecosystem that is sovereign by design and inclusive by policy. Trust is not removed; it is redistributed through code. A secure digital future requires that every participant can trust the systems that govern their data and their identity.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF INFRASTRUCTURE IS DISTRIBUTED.<br>
                BUT THE TRUST REMAINS HUMAN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Parliament of Pakistan, <em>Virtual Assets Act 2026: Legal Framework for Digital Assets</em>.</li>
                    <li>Pakistan Virtual Assets Regulatory Authority (PVARA), <em>Regulatory Guidelines 2026</em>.</li>
                    <li>Ministry of IT & Telecommunication (MoITT), <em>National Blockchain Strategy Update 2026</em>.</li>
                    <li>NUST SINES, <em>Research Portfolio on Distributed Systems and Blockchain 2026</em>.</li>
                    <li>Cabinet Division Pakistan, <em>National Crypto Council Strategic Report 2026</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            131
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

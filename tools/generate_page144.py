from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-144-blockchain-and-national-infrastructure.html'

GRAPHICS = [
    ("Blockchain Infra", "DIST", "↔", "NET"),
    ("Shared Record Layer", "BASE", "→", "TRST"),
    ("Infrastructure Stack", "USER", "→", "LEDG"),
    ("User Layer", "USER", "↔", "BASE"),
    ("Wallet Layer", "WAL", "↔", "BASE"),
    ("App Layer", "APP", "↔", "BASE"),
    ("Smart Contract Layer", "CODE", "↔", "BASE"),
    ("Network Layer", "NET", "↔", "BASE"),
    ("Validator Layer", "VAL", "↔", "BASE"),
    ("Consensus Layer", "AGRE", "↔", "BASE"),
    ("Ledger Layer", "LEDG", "↔", "BASE"),
    ("Distributed Ledger", "SYNC", "↔", "MANY"),
    ("Ledger Transparency", "OPEN", "↔", "LEDG"),
    ("Ledger Auditability", "CHK", "↔", "LEDG"),
    ("Ledger Redundancy", "MANY", "↔", "LEDG"),
    ("Programmable Sett", "CODE", "↔", "SETT"),
    ("Centralized System", "ONE", "↔", "ALL"),
    ("Distributed System", "MANY", "↔", "ALL"),
    ("Central Server", "SERV", "↔", "USER"),
    ("Network Peering", "NODE", "↔", "NODE"),
    ("Shared Ledger Link", "LEDG", "↔", "ALL"),
    ("Trust Model", "MATH", "↔", "TRST"),
    ("Crypto Verification", "VERI", "↔", "SAFE"),
    ("Consensus Trust", "AGRE", "↔", "SAFE"),
    ("Protocol Trust", "RULE", "↔", "SAFE"),
    ("Incentive Trust", "COIN", "↔", "SAFE"),
    ("Consensus Mechanism", "AGRE", "↔", "NET"),
    ("Proof of Work", "WORK", "↔", "AGRE"),
    ("Proof of Stake", "STAK", "↔", "AGRE"),
    ("BFT System", "BFT", "↔", "AGRE"),
    ("Validator Stake", "VAL", "↔", "SAFE"),
    ("Block Validation", "CHK", "→", "BLOK"),
    ("Ledger Entry", "BLOK", "→", "LEDG"),
    ("Node Store", "DATA", "↔", "NODE"),
    ("Node Relay", "SEND", "↔", "NODE"),
    ("Node Verify", "CHK", "↔", "NODE"),
    ("Node Consensus", "AGRE", "↔", "NODE"),
    ("Node API", "API", "↔", "NODE"),
    ("Blockchain Crypto", "MATH", "↔", "SAFE"),
    ("Tx Authentication", "AUTH", "↔", "SAFE"),
    ("Digital Signature", "SIGN", "↔", "SAFE"),
    ("Integrity Link", "SAME", "↔", "SAFE"),
    ("Secure Ownership", "OWN", "↔", "SAFE"),
    ("Private Key Link", "KEY", "↔", "SIGN"),
    ("Signature Flow", "KEY", "→", "TX"),
    ("Network Verify", "CHK", "↔", "TX"),
    ("Key Possession", "KEY", "↔", "OWN"),
    ("Key Loss Risk", "LOST", "≠", "OWN"),
    ("Key Management", "KEYS", "↔", "SAFE"),
    ("Institutional Cust", "INST", "↔", "SAFE"),
    ("Hardware Security", "HARD", "↔", "SAFE"),
    ("Multi-Sig Control", "MANY", "↔", "SAFE"),
    ("Policy Engine", "RULE", "↔", "SAFE"),
    ("Secure Storage", "STOR", "↔", "SAFE"),
    ("Smart Contract App", "CODE", "↔", "APP"),
    ("Token Issuance", "COIN", "↔", "CODE"),
    ("Escrow Contract", "LOCK", "↔", "CODE"),
    ("DApp Architecture", "DAPP", "↔", "CODE"),
    ("Programmable Rules", "RULE", "↔", "DATA"),
    ("Automated Tx", "AUTO", "↔", "TX"),
    ("Verifiable Record", "VERI", "↔", "LEDG"),
    ("National Hybrid", "GOVT", "↔", "BC"),
    ("Existing DB Link", "DB", "↔", "BC"),
    ("API Bridge", "API", "↔", "BC"),
    ("Identity Link", "ID", "↔", "BC"),
    ("On-Chain Reference", "HASH", "↔", "BC"),
    ("Off-Chain Data", "DATA", "↔", "DB"),
    ("Data Hash Link", "HASH", "↔", "DATA"),
    ("Data Integrity", "SAME", "↔", "LEDG"),
    ("Archival Verify", "ARCH", "↔", "VERI"),
    ("Digital Record App", "REC", "↔", "BC"),
    ("Cert Verification", "CERT", "↔", "BC"),
    ("License Verify", "LIC", "↔", "BC"),
    ("Credential Verify", "GRAD", "↔", "BC"),
    ("Ownership Record", "OWN", "↔", "BC"),
    ("Document History", "HIST", "↔", "BC"),
    ("Land Record BC", "LAND", "↔", "BC"),
    ("Property History", "HIST", "↔", "LAND"),
    ("Legal Ownership", "LAW", "↔", "OWN"),
    ("Real Estate Tok", "HOME", "→", "TOK"),
    ("Fractional Own", "PART", "↔", "HOME"),
    ("Asset Token Stack", "ASST", "→", "TOK"),
    ("Commodity Tok", "GOLD", "↔", "TOK"),
    ("Fund Tokenization", "FUND", "↔", "TOK"),
    ("IP Tokenization", "IP", "↔", "TOK"),
    ("Digital Security", "SEC", "↔", "BC"),
    ("Reg Compliance", "RULE", "↔", "SEC"),
    ("Payment Settlement", "PAY", "↔", "SETT"),
    ("Cross-Border Pay", "GLOB", "↔", "PAY"),
    ("Remittance Loop", "REMT", "↔", "BC"),
    ("CBDC Model", "CBDC", "↔", "NATL"),
    ("Wholesale CBDC", "BANK", "↔", "CBDC"),
    ("Retail CBDC", "USER", "↔", "CBDC"),
    ("Interbank Sett", "BANK", "↔", "SETT"),
    ("Trade Finance BC", "TRAD", "↔", "BC"),
    ("Supply Chain BC", "SUPP", "↔", "BC"),
    ("Provenance Record", "ORIG", "↔", "BC"),
    ("Faisal Orakzai profile", "SYS", "↔", "BC"),
    ("Virtual Assets Act", "LAW", "↔", "2026"),
    ("PVARA Establishment", "GOVT", "↔", "PVARA"),
    ("Crypto Ban Lifted", "OPEN", "↔", "BANK"),
    ("Bitcoin Reserve", "BTC", "↔", "NATL"),
    ("Stablecoin Plan", "STBL", "↔", "PAK"),
    ("Raast Integration", "PAY", "↔", "DPI"),
    ("NADRA ID Link", "ID", "↔", "BC"),
    ("Audit Integrity", "CHK", "↔", "SAFE"),
    ("Shared Ledger Era", "TIME", "↔", "LEDG"),
    ("National Infrastructure", "NATL", "↔", "BASE"),
    ("Infrastructure Value", "VALU", "↔", "SYS"),
    ("Tamper-Evident", "SAME", "↔", "TRST"),
    ("Programmable Net", "CODE", "↔", "NET"),
    ("Asset Coordination", "SYNC", "↔", "ASST"),
    ("Infrastructure Layer", "BASE", "↔", "NEW"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g144-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g144-{index}-title g144-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g144-{index}-title">{safe}</title><desc id="g144-{index}-desc">A blockchain infrastructure relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g144-{index}-caption" class="diagram-caption">{index}. {safe} — Blockchain infrastructure relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Blockchain Infrastructure Framework</title><desc id="hero-desc">A diagram showing the integrated stack of blockchain infrastructure, from users and wallets to consensus and distributed ledgers.</desc><defs><linearGradient id="h144-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h144-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">BLOCKCHAIN INFRASTRUCTURE STACK</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">USERS & WALLETS</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">APPLICATIONS & SMART CONTRACTS</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">BLOCKCHAIN NETWORK LAYER</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">VALIDATORS & CONSENSUS</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">DISTRIBUTED LEDGER LAYER</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">CRYPTOGRAPHY & PRIVATE KEYS</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">NATIONAL HYBRID SYSTEMS</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">BLOCKCHAIN & NATIONAL INFRASTRUCTURE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Distributed Networks as a New Infrastructure Layer.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Blockchain Infrastructure: The integrated framework for recording transactions, coordinating digital assets, and creating programmable networks.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 144</title>
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
            <p class="section-label">PAGE 144</p>
            <h2>BLOCKCHAIN & NATIONAL INFRASTRUCTURE</h2>
            <p>“Distributed Networks as a New Infrastructure Layer.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Blockchain technology is a broader infrastructure model for recording transactions, coordinating digital assets, and creating programmable networks. For national infrastructure, blockchain provides a shared, tamper-evident record layer where multiple parties can coordinate without relying entirely on a central operator. Its value depends on strategic implementation—integrating distributed ledgers with existing systems to create measurable infrastructure value for the modern nation.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Distributed Ledgers & Trust Models</h3>
                <p>A blockchain network acts as a shared computational and record-keeping layer. As of 2026, Pakistan has officially recognized this infrastructure through the <strong>Virtual Assets Act 2026</strong> and the establishment of the <strong>Pakistan Virtual Assets Regulatory Authority (PVARA)</strong>. By shifting from purely institutional trust to cryptographic verification and protocol-based <strong>Consensus</strong>, nations can build more resilient digital systems. In April 2026, the State Bank of Pakistan (SBP) officially integrated this layer into the banking system, allowing licensed firms to access national infrastructure.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Programmable Infrastructure & Smart Contracts</h3>
                <p>Smart contracts make infrastructure programmable, allowing predefined logic to execute automatically when conditions are met. This capability is being applied to <strong>Digital Public Infrastructure (DPI)</strong>, including the State Bank's <strong>wholesale CBDC pilot</strong> and the integration of blockchain into <strong>Land Record Registration</strong> systems. By anchoring hashes and proofs to a distributed ledger, Pakistan ensures the integrity of archival records and ownership histories while maintaining sensitive data in secure off-chain databases.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Tokenization & Financial Systems</h3>
                <p>Blockchain infrastructure enables the <strong>Tokenization</strong> of real-world assets, representing rights associated with property, commodities, and securities. While the technical token does not automatically create legal ownership, the 2026 regulatory framework provides the necessary legal bridge. Distributed systems also simplify <strong>Cross-Border Payments</strong> and <strong>Remittances</strong>, which are vital for Pakistan's overseas communities. By building hybrid architectures that connect existing databases with blockchain layers, nations can modernize trade finance and supply-chain infrastructure.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists advocating for blockchain as a "shared record layer" for national infrastructure. His work explores the implementation of secure, verifiable systems for land records, remittances, and digital credentials. He serves as one example of the "Young Pakistani Builder" who recognizes that blockchain is a tool for strategic resilience. His vision includes leveraging distributed ledgers to empower the Orakzai community, ensuring that regional property rights and economic transactions are anchored to a secure, permanent, and sovereign digital foundation.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Blockchain Infrastructure</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Sovereignty & The National Bitcoin Reserve</h3>
                <p>Blockchain infrastructure is increasingly linked to national sovereignty. In May 2026, reports indicated Pakistan's intent to explore a <strong>National Bitcoin Reserve</strong> as part of its digital sovereignty strategy. By managing <strong>Private Keys</strong> and <strong>Custody</strong> architectures through domestic hardware security and policy engines, nations can maintain control over their digital wealth. From the interbank settlement layers to the proposed Orakzai Sovereign Grid, we are building a future where distributed networks provide the permanent record of our progress.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Trust is the currency of cooperation. In the digital age, we are moving from trusting institutions to trusting protocols. The objective of blockchain infrastructure is to create a shared reality that is permanent, verifiable, and secure. From the national stablecoin plans to the digitized land records of the provinces, we are designing a foundation where the ledger is distributed, but the integrity remains sovereign.”</p>
            </div>

            <div class="final-statement">
                THE NETWORK IS DISTRIBUTED.<br>
                THE RECORD IS PERMANENT.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Pakistan TV Global, <em>Enactment of the Virtual Assets Act 2026 & Establishment of PVARA</em>.</li>
                    <li>Reuters / State Bank of Pakistan (SBP), <em>Wholesale CBDC Pilot & Virtual Asset Regulation (2025-2026)</em>.</li>
                    <li>Dawn News, <em>Launch of Blockchain-Based Land Record System to Prevent Tampering (2025)</em>.</li>
                    <li>TechJuice / SBP, <em>Lifting of the 8-Year Crypto Ban & Banking Access for Licensed Firms (April 2026)</em>.</li>
                    <li>Pediastan / Strategic Reports, <em>Pakistan's Proposed National Bitcoin Reserve Plan (May 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            144
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

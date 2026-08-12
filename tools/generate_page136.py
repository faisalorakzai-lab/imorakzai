from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-136-tokenization-of-real-world-assets.html'

GRAPHICS = [
    ("RWA Overview", "REAL", "↔", "TOKN"),
    ("Asset to Token", "ASST", "→", "DATA"),
    ("Token vs Digitization", "RGHT", "≠", "DOCS"),
    ("Tokenization Stack", "LEGL", "TECH", "APPL"),
    ("Legal Layer", "LAW", "↔", "RGHT"),
    ("Custody Layer", "SAFE", "↔", "ASST"),
    ("Oracle Layer", "REAL", "→", "DATA"),
    ("Token Layer", "CODE", "↔", "OWN"),
    ("Compliance Layer", "KYC", "→", "ALLOW"),
    ("Permissioned Model", "AUTH", "→", "TXN"),
    ("Permissionless Model", "OPEN", "↔", "NET"),
    ("Real Estate Token", "PROP", "→", "FRAC"),
    ("Fractional Ownership", "ONE", "→", "MANY"),
    ("Property Income", "RENT", "→", "TOKN"),
    ("Property Registry", "GOVT", "↔", "BC"),
    ("Govt Securities", "DEBT", "→", "TOKN"),
    ("Tokenized Funds", "POOL", "→", "TOKN"),
    ("Corporate Debt", "CORP", "→", "BOND"),
    ("Private Credit", "LOAN", "↔", "TOKN"),
    ("Invoice Tokenization", "BILL", "→", "CASH"),
    ("Commodities", "GOLD", "OIL", "AGRI"),
    ("Gold Tokenization", "VAULT", "↔", "TOKN"),
    ("Proof of Reserves", "AUDT", "→", "TRST"),
    ("RWA + DeFi", "REAL", "↔", "FIN"),
    ("Collateralized RWA", "ASST", "→", "LOAN"),
    ("Collateral Problem", "FAKE", "→", "FAIL"),
    ("Treasury Assets", "T-BIL", "→", "YLD"),
    ("RWA Liquidity", "BUY", "↔", "SELL"),
    ("Secondary Markets", "TRAD", "↔", "TOKN"),
    ("24/7 Markets", "OPEN", "↔", "TIME"),
    ("Atomic Settlement", "DLIV", "+", "PAY"),
    ("DvP Principle", "ASST", "↔", "CASH"),
    ("Programmable Assets", "RULE", "↔", "TOKN"),
    ("Prog Compliance", "AUTO", "→", "LAW"),
    ("Digital Identity", "ID", "↔", "WAL"),
    ("Privacy Model", "HIDE", "↔", "VERI"),
    ("ZK Identity", "PRUF", "↔", "TRUE"),
    ("RWA + Banking", "BANK", "↔", "BC"),
    ("Tokenized Deposits", "CASH", "→", "TOKN"),
    ("Stable vs Deposit", "RESR", "≠", "BANK"),
    ("CBDC Concept", "CENT", "→", "DIGI"),
    ("RWA + CBDC", "ASST", "↔", "GOVT"),
    ("Global Capital", "GLB", "↔", "NET"),
    ("Jurisdiction", "CTRY", "↔", "LAW"),
    ("Legal Finality", "COURT", "↔", "BC"),
    ("Bankruptcy Protect", "SAFE", "↔", "FAIL"),
    ("Issuance Lifecycle", "MINT", "→", "BURN"),
    ("Token Lifecycle", "HOLD", "→", "REDE"),
    ("Token Retirement", "BURN", "↔", "REDE"),
    ("Fractionalization", "$1M", "→", "$1"),
    ("Accessibility", "ALL", "↔", "FIN"),
    ("RWA + Inclusion", "ACC", "↔", "VALU"),
    ("SME Financing", "SME", "→", "CAP"),
    ("Agricultural RWAs", "FARM", "→", "TOKN"),
    ("Infrastructure Fin", "ROAD", "→", "TOKN"),
    ("Renewable Energy", "SOLR", "→", "TOKN"),
    ("Carbon Markets", "CO2", "→", "CRED"),
    ("Intellectual Prop", "IDEA", "→", "TOKN"),
    ("Music Royalties", "SONG", "→", "PAY"),
    ("Entertainment Assets", "FILM", "→", "TOKN"),
    ("Art Tokenization", "ART", "↔", "CERT"),
    ("Data Infrastructure", "INDX", "↔", "VALU"),
    ("RWA Oracles", "PRIC", "→", "CONT"),
    ("Auditing Model", "CHK", "→", "SAFE"),
    ("Attestation Loop", "PROV", "→", "BC"),
    ("Blockchain Finality", "TXN", "↔", "FIXD"),
    ("Tokenization Bridge", "PHYS", "↔", "DIGI"),
    ("Trust Minimization", "LESS", "↔", "TRST"),
    ("Gold Trust Example", "VAULT", "→", "TOKN"),
    ("RWA Trust Stack", "LAW", "BC", "MATH"),
    ("RWA Security", "SAFE", "↔", "CODE"),
    ("Cybersecurity", "ATTK", "↔", "DEF"),
    ("Key Management", "KEY", "↔", "VAUL"),
    ("Governance Loop", "VOTE", "→", "ACT"),
    ("Emergency Controls", "PAUS", "→", "SAFE"),
    ("Immutability vs Control", "FIXD", "↔", "MOD"),
    ("Decentralization Spectrum", "CENT", "→", "DECE"),
    ("Hybrid Finance", "TRAD", "+", "DEFI"),
    ("AI + RWA", "INTE", "→", "ASST"),
    ("AI Asset Management", "AUTO", "→", "PORT"),
    ("Autonomous Markets", "AI", "→", "TRAD"),
    ("RWA + DeFi + AI", "REAL", "FIN", "INTE"),
    ("Pakistan Opportunity", "PAK", "↔", "RWA"),
    ("Pakistan Real Estate", "LAND", "→", "TOKN"),
    ("Pakistan Agriculture", "CROP", "→", "TOKN"),
    ("Diaspora Capital", "SEND", "→", "PAK"),
    ("Faisal Orakzai RWA", "SYS", "↔", "RWA"),
    ("OKBOND RWA", "VALU", "↔", "CONT"),
    ("Orakzai Sovereign Grid", "SOV", "↔", "GRID"),
    ("Digital Sovereignty", "SELF", "↔", "SOV"),
    ("Databases to Networks", "DB", "→", "NET"),
    ("Reconciliation", "MANY", "→", "ONE"),
    ("Settlement Cycle", "FAST", "↔", "SETL"),
    ("Real-Time Finance", "LIVE", "↔", "DATA"),
    ("Global Economy", "GLB", "↔", "TOKN"),
    ("Tokenized Capital", "INV", "→", "ASST"),
    ("Oracle-Legal Gap", "BC", "≠", "LAW"),
    ("Custody-Legal Gap", "VAULT", "≠", "OWN"),
    ("Liquidity Gap", "FRAC", "≠", "BUY"),
    ("Trust Gap", "MATH", "≠", "PHYS"),
    ("Regulatory Gap", "GLB", "≠", "LOCL"),
    ("Responsible Tokenization", "CHK", "→", "BLD"),
    ("What to Tokenize", "PROB", "→", "SOLV"),
    ("Tokenization as Infra", "BASE", "↔", "TOKN"),
    ("Future of Ownership", "PROG", "↔", "OWN"),
    ("Future of Capital", "FLOW", "↔", "CODE"),
    ("Future Financial Infra", "INTE", "↔", "SETL"),
    ("Digital Economic Rights", "MACH", "↔", "RGHT"),
    ("Programmable Capital", "CODE", "→", "FLOW"),
    ("RWA Smart Contracts", "RULE", "↔", "CODE"),
    ("RWA Cloud Infra", "DATA", "↔", "CLD"),
    ("RWA AI Architecture", "AI", "↔", "ASST"),
    ("RWA Cybersecurity", "SAFE", "↔", "DATA"),
    ("RWA Digital Identity", "ID", "↔", "TOKN"),
    ("Final RWA Arch", "GLB", "↔", "SOV"),
    ("Historical Evolution", "PAST", "→", "FUTR"),
    ("Final Conceptual Diagram", "REAL", "↔", "DIGI"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g136-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g136-{index}-title g136-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g136-{index}-title">{safe}</title><desc id="g136-{index}-desc">An RWA relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g136-{index}-caption" class="diagram-caption">{index}. {safe} — RWA relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Tokenization of Real-World Assets Framework</title><desc id="hero-desc">A diagram showing the integrated framework for connecting physical assets and legal rights with programmable digital infrastructure.</desc><defs><linearGradient id="h136-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h136-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">RWA TOKENIZATION STACK</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">LEGAL</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="65" font-size="12">CUSTODY</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">VERIFICATION</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">TOKENIZATION</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">IDENTITY</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="65" font-size="12">COMPLIANCE</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">PROGRAMMABLE</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">CAPITAL</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">TOKENIZATION OF REAL-WORLD ASSETS</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Bringing Physical and Traditional Assets Into Programmable Digital Infrastructure.”</text></svg><figcaption id="hero-caption" class="diagram-caption">RWA: The integrated framework for connecting physical value and legal rights with decentralized blockchain infrastructure.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 136</title>
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
            <p class="section-label">PAGE 136</p>
            <h2>TOKENIZATION OF REAL-WORLD ASSETS (RWA)</h2>
            <p>“Bringing Physical and Traditional Assets Into Programmable Digital Infrastructure.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “If blockchain can create digital assets natively, the next major question is whether it can also represent real-world assets (RWAs). Real-world asset tokenization is the process of creating a digital representation of an asset, claim, or economic interest on a blockchain. This connects legal and economic rights in the physical or traditional financial world with programmable digital infrastructure, enabling faster settlement, fractional ownership, and improved transparency across global capital markets.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The RWA Trust Stack</h3>
                <p>A serious RWA system requires more than a smart contract. It involves an integrated stack covering the <strong>Legal Layer</strong> (what the token legally represents), the <strong>Custody Layer</strong> (safeguarding the underlying asset), and the <strong>Oracle Layer</strong> (connecting blockchain state with external reality). As of July 2026, the global RWA market has surpassed <strong>$60 billion</strong>, with tokenized Treasuries reaching <strong>$12.88 billion</strong>. This transition is described by the IMF and BIS as a fundamental reconfiguration of financial architecture, moving from isolated databases to shared digital networks.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Real Estate, Agriculture & Commodities</h3>
                <p>Tokenization makes fractional interests technically easier to represent, reducing minimum investment sizes for assets like real estate and infrastructure. In Pakistan, research from the <strong>Pakistan Institute of Development Economics (PIDE)</strong> highlights the benefits of tokenization for inclusion and liquidity in the property market. Beyond real estate, agricultural RWAs—such as warehouse receipts and commodity financing—offer potential to improve financing efficiency for farmers, provided there is reliable physical verification and legal finality.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Programmable Compliance & Digital Identity</h3>
                <p>Instead of relying exclusively on manual processes, RWA infrastructure allows for <strong>Programmable Compliance</strong> encoded into smart contracts. This includes automated whitelisting, transfer limits, and jurisdiction-aware restrictions. Future systems will likely combine <strong>Digital Identity</strong> with privacy-preserving technologies like zero-knowledge proofs, allowing institutions to verify investor eligibility without exposing unnecessary personal data publicly. This bridge between the physical and digital worlds requires a multidisciplinary approach involving law, finance, and software engineering.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists exploring the intersection of software and real-world economic assets. His documented involvement in digital-asset initiatives illustrates a broader shift toward understanding the entire RWA stack—not just the blockchain, but the legal, physical, and verification layers required for trustworthy digital rights. He serves as one example of the "Young Pakistani Builder" who advocates for building infrastructure that can connect Pakistan's real estate, agriculture, and diaspora capital with modern, sovereign digital financial systems.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Tokenization of Real-World Assets</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Future of Capital & Digital Sovereignty</h3>
                <p>The long-term opportunity of tokenization is the creation of machine-readable economic rights. Once financial rights become programmable, software can interact with them automatically, forming the foundation of <strong>Programmable Capital Markets</strong>. For countries like Pakistan, this infrastructure can contribute to <strong>Digital Sovereignty</strong> by providing greater control over financial registries and settlement. However, the future will be determined not by how many tokens are created, but by whether those tokens can create legally meaningful digital representations of real economic value.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Tokenization is fundamentally a bridge between two worlds. The weakest connection between the physical legal system and the digital blockchain becomes the largest risk. To build a secure tokenized economy, we must bridge the gap between what the blockchain says and what the real world recognizes. For Pakistan, the opportunity is to leverage this technology to create transparent, inclusive, and efficient markets that empower every citizen to participate in the global economy. The token is the interface, but the trust is the foundation.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF OWNERSHIP IS PROGRAMMABLE.<br>
                BUT THE LEGAL RIGHTS REMAIN HUMAN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>International Monetary Fund (IMF), <em>Tokenized Finance: A Fundamental Reconfiguration of Financial Architecture (2026)</em>.</li>
                    <li>Bank for International Settlements (BIS), <em>Annual Economic Report 2026: Innovation Beyond Stablecoins</em>.</li>
                    <li>Yahoo Finance / Brickken, <em>Global RWA Tokenization Market Data & Institutional Adoption (July 2026)</em>.</li>
                    <li>Pakistan Institute of Development Economics (PIDE), <em>Transforming Real Estate through Blockchain (2026 Research)</em>.</li>
                    <li>RWA.xyz / MetaMask, <em>State of Tokenized Treasuries & Private Credit (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            136
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

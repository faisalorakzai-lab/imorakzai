from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-147-digital-assets-and-regulation.html'

GRAPHICS = [
    ("Digital Assets", "VALU", "↔", "NET"),
    ("Regulatory Framework", "LAW", "→", "SAFE"),
    ("Asset Categories", "BASE", "→", "TYPE"),
    ("Payment Assets", "PAY", "↔", "BASE"),
    ("Stablecoins", "STBL", "↔", "BASE"),
    ("Utility Tokens", "UTIL", "↔", "BASE"),
    ("Security Tokens", "SEC", "↔", "BASE"),
    ("Digital Collectibles", "NFT", "↔", "BASE"),
    ("RWA Tokenization", "REAL", "→", "TOK"),
    ("Crypto vs Assets", "COIN", "≠", "ASST"),
    ("Regulation Matters", "RISK", "→", "RULE"),
    ("Fraud Prevention", "FAKE", "≠", "SAFE"),
    ("Market Integrity", "FAIR", "↔", "MKT"),
    ("AML Compliance", "CLEAN", "↔", "RULE"),
    ("KYC Process", "WHO", "↔", "ID"),
    ("Travel Rule", "INFO", "→", "TX"),
    ("Sanctions Check", "LIST", "↔", "TX"),
    ("Consumer Protect", "USER", "↔", "SAFE"),
    ("Cybersecurity", "SEC", "↔", "NET"),
    ("Operational Risk", "FAIL", "≠", "STAY"),
    ("Conflict Interest", "SELF", "≠", "FAIR"),
    ("Function Principle", "ACT", "→", "RULE"),
    ("Bitcoin Model", "BTC", "↔", "BASE"),
    ("Ethereum Model", "ETH", "↔", "BASE"),
    ("Smart Contract Law", "CODE", "↔", "LAW"),
    ("Asset Exchange", "BUY", "↔", "SELL"),
    ("Custody Architecture", "KEY", "↔", "STOR"),
    ("Self-Custody", "OWN", "↔", "KEY"),
    ("Private Key Authorization", "KEY", "→", "TX"),
    ("Public Key Verify", "PUB", "↔", "CHK"),
    ("Zero-Knowledge", "HIDE", "↔", "PROV"),
    ("On-Chain Analytics", "DATA", "→", "VIEW"),
    ("Virtual Assets Act", "LAW", "↔", "2026"),
    ("PVARA Establishment", "GOVT", "↔", "PVARA"),
    ("SBP Policy Pivot", "BANK", "↔", "OPEN"),
    ("Crypto Ban Lifted", "2018", "→", "2026"),
    ("VASP Licensing", "LIC", "↔", "PVARA"),
    ("Capital Adequacy", "CASH", "↔", "SAFE"),
    ("Token Issuance", "ISS", "→", "MKT"),
    ("Stablecoin Reserve", "BACK", "↔", "STBL"),
    ("Fiat Backing", "CASH", "→", "STBL"),
    ("Crypto Backing", "COIN", "→", "STBL"),
    ("Algo Backing", "MATH", "→", "STBL"),
    ("Security Laws", "SEC", "↔", "RULE"),
    ("Fractional Own", "PART", "↔", "REAL"),
    ("Investor Protect", "USER", "↔", "SEC"),
    ("Market Manipulation", "FAKE", "≠", "FAIR"),
    ("Insider Trading", "INFO", "≠", "FAIR"),
    ("Wash Trading", "LOOP", "≠", "FAIR"),
    ("Disclosure Rule", "OPEN", "↔", "INFO"),
    ("Suitability Rule", "USER", "↔", "TYPE"),
    ("Complaint Flow", "USER", "→", "RULE"),
    ("Taxation Treatment", "TAX", "↔", "PAY"),
    ("Capital Gains", "GAIN", "→", "TAX"),
    ("Income Tax", "INC", "→", "TAX"),
    ("Trading Tax", "TRAD", "→", "TAX"),
    ("Mining Tax", "WORK", "→", "TAX"),
    ("Staking Tax", "STAK", "→", "TAX"),
    ("Accounting Standards", "BOOK", "↔", "RULE"),
    ("Digital Reporting", "REPT", "→", "GOV"),
    ("Audit Trail", "HIST", "↔", "CHK"),
    ("Regulatory Sandbox", "TEST", "↔", "SAFE"),
    ("Innovation Hub", "NEW", "↔", "GOV"),
    ("Regional Access", "ORAK", "↔", "GLOB"),
    ("Financial Inclusion", "ALL", "↔", "PAY"),
    ("Remittance Loop", "GLOB", "→", "HOME"),
    ("Interbank Sett", "BANK", "↔", "NET"),
    ("Digital Sovereignty", "OWN", "↔", "NATL"),
    ("Sovereign Assets", "BTC", "↔", "NATL"),
    ("National Reserve", "RESR", "↔", "NATL"),
    ("Identity Link", "ID", "↔", "ASST"),
    ("DPI Integration", "DPI", "↔", "ASST"),
    ("Raast Bridge", "PAY", "↔", "ASST"),
    ("NADRA Verification", "ID", "↔", "PVARA"),
    ("Cyber Standards", "SEC", "↔", "LIC"),
    ("Data Privacy", "PRIV", "↔", "RULE"),
    ("Cross-Border Rule", "GLOB", "↔", "RULE"),
    ("Global Interop", "SYNC", "↔", "GLOB"),
    ("FATF Alignment", "FATF", "↔", "PAK"),
    ("Travel Rule Sync", "INFO", "↔", "GLOB"),
    ("VASP Oversight", "CHK", "↔", "VASP"),
    ("Token Governance", "GOV", "↔", "CODE"),
    ("Protocol Upgrade", "NEW", "↔", "STAY"),
    ("Emergency Stop", "LOCK", "↔", "SAFE"),
    ("Dispute Resolution", "LAW", "↔", "ACT"),
    ("Enforceable Proof", "VERI", "↔", "LAW"),
    ("Digital Legacy", "TIME", "↔", "OWN"),
    ("Asset Portability", "MOVE", "↔", "USER"),
    ("Network Security", "SAFE", "↔", "NET"),
    ("Validator Stake", "STAK", "↔", "SAFE"),
    ("Consensus Trust", "AGRE", "↔", "TRST"),
    ("Mathematical Proof", "MATH", "↔", "VERI"),
    ("Transparent Ledger", "OPEN", "↔", "LEDG"),
    ("Immutable Record", "SAME", "↔", "LEDG"),
    ("Decentralized ID", "DID", "↔", "ASST"),
    ("Verifiable Cred", "CERT", "↔", "ASST"),
    ("Oracle Bridge", "DATA", "↔", "CODE"),
    ("Legal Oracle", "LAW", "↔", "CODE"),
    ("Physical Oracle", "SENS", "↔", "CODE"),
    ("Hybrid Reality", "REAL", "↔", "DIGI"),
    ("Digital Economy", "ECON", "↔", "NET"),
    ("Future Value", "TIME", "↔", "NEW"),
    ("Sovereign Tech", "OWN", "↔", "TECH"),
    ("National Growth", "GROW", "↔", "ASST"),
    ("Identity Power", "POWR", "↔", "ID"),
    ("Asset Rights", "RITE", "↔", "OWN"),
    ("Governance Trust", "TRST", "↔", "GOV"),
    ("Inclusive Future", "ALL", "↔", "TIME"),
    ("Orakzai Digital", "ORAK", "↔", "NEW"),
    ("The Permanent Record", "STAY", "↔", "DONE"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g147-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g147-{index}-title g147-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g147-{index}-title">{safe}</title><desc id="g147-{index}-desc">A digital asset regulation relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g147-{index}-caption" class="diagram-caption">{index}. {safe} — Digital asset regulation relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Digital Asset Regulatory Framework</title><desc id="hero-desc">A diagram showing the integrated stack of digital asset regulation, from primary law to market integrity.</desc><defs><linearGradient id="h147-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h147-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">PVARA REGULATORY STACK (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">VIRTUAL ASSETS ACT 2026 (Primary Law)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">PVARA LICENSING & SUPERVISION</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">SBP BANKING ACCESS & PAYMENTS</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AML / CFT & FATF TRAVEL RULE</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CONSUMER PROTECTION & DISCLOSURE</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">MARKET INTEGRITY & CYBERSECURITY</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">RWA TOKENIZATION & SECP RULES</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">DIGITAL ASSETS & REGULATION</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Restriction to Regulation: The 2026 Policy Pivot.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Digital Asset Regulatory Framework: The integrated stack of law, licensing, and oversight for the 2026 digital economy.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 147</title>
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
            <p class="section-label">PAGE 147</p>
            <h2>DIGITAL ASSETS & REGULATION</h2>
            <p>“From Restriction to Regulation: The 2026 Policy Pivot.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Digital assets have developed from an experimental technology into a broad technological and financial category. As adoption has expanded, the fundamental question is no longer whether to regulate, but how to regulate without eliminating innovation. For Pakistan, 2026 marks a historical pivot—from the restrictions of the past to a comprehensive, compliance-based framework that integrates digital value into the national financial fabric.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Virtual Assets Act 2026</h3>
                <p>The enactment of the **Virtual Assets Act 2026** in March 2026 provided Pakistan with its first comprehensive legal foundation for digital value. This legislation established the **Pakistan Virtual Assets Regulatory Authority (PVARA)** as the primary oversight body. By shifting from a restrictive stance to a licensing regime, the Act ensures that **Virtual Asset Service Providers (VASPs)** operate within a transparent, auditable, and secure framework, protecting both the consumer and the national economy.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Banking Pivot & SBP Policy</h3>
                <p>A significant milestone in the 2026 transition was the **State Bank of Pakistan (SBP)** circular issued in April 2026, which officially ended the 2018 crypto banking ban. This policy pivot allows licensed VASPs to access formal banking services, facilitating seamless on-ramps and off-ramps for digital value. This integration is critical for **Financial Inclusion**, allowing regional entrepreneurs and the diaspora to utilize digital assets for payments and remittances within a regulated environment.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Compliance, AML & The Travel Rule</h3>
                <p>Effective regulation follows the principle of "Regulation by Function," addressing economic risks such as fraud, money laundering, and market manipulation. The 2026 framework aligns with global standards, including the **FATF Travel Rule**, which requires information sharing for digital asset transfers. By integrating **On-Chain Analytics** and **KYC processes**, Pakistan ensures that its digital asset ecosystem remains resilient against illicit activities while supporting legitimate technological growth.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Asset Categories & Market Integrity</h3>
                <p>The PVARA framework classifies digital assets into distinct categories—**Payment Assets**, **Stablecoins**, **Utility Tokens**, and **Security Tokens**—each with specific regulatory requirements. For **Real-World Asset (RWA) Tokenization**, PVARA works alongside the **Securities and Exchange Commission of Pakistan (SECP)** to bridge the gap between blockchain records and legal ownership. This collaborative approach ensures **Market Integrity**, providing clear rules for token issuance, custody, and disclosure.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Digital Assets & Regulation</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Regulation is the bridge between innovation and institutional trust. In the digital age, we are moving from the uncertainty of the unregulated to the clarity of the compliant. The objective of the 2026 framework is to create a safe harbor for digital value—ensuring that from the markets of Karachi to the valleys of Orakzai, every citizen can participate in the digital economy with the protection of the law and the speed of the network.”</p>
            </div>

            <div class="final-statement">
                INNOVATION IS PROTECTED.<br>
                COMPLIANCE IS SOVEREIGN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Parliament of Pakistan, <em>The Virtual Assets Act 2026: Comprehensive Regulatory Framework (March 2026)</em>.</li>
                    <li>Reuters / State Bank of Pakistan (SBP), <em>Ending the 8-Year Crypto Ban: Banking Access for Licensed VASPs (April 2026)</em>.</li>
                    <li>Dawn News, <em>Reviewing the Virtual Assets Act 2026: Compliance-Based Entry into the Financial System (June 2026)</em>.</li>
                    <li>PVARA, <em>Public Consultation: Virtual Asset Services Regulations, 2026 (July 2026)</em>.</li>
                    <li>TechJuice / Industry Reports, <em>Pakistan's Policy Pivot: From Restriction to Regulation in the Digital Asset Sector (May 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            147
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

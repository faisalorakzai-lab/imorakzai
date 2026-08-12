from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-148-financial-infrastructure-of-the-future.html'

GRAPHICS = [
    ("Financial Infra", "VALU", "↔", "NET"),
    ("Traditional Stack", "BANK", "→", "USER"),
    ("Digital Stack", "CODE", "→", "USER"),
    ("Raast Rails", "PAY", "↔", "DPI"),
    ("Instant Payments", "FAST", "→", "DONE"),
    ("P2P Transfer", "USER", "↔", "USER"),
    ("P2M Payment", "USER", "→", "MERC"),
    ("Bulk Disbursement", "CORP", "→", "MANY"),
    ("QR Payment", "SCAN", "→", "PAY"),
    ("Digital Banking", "APP", "↔", "BANK"),
    ("Fintech Layer", "TECH", "↔", "FIN"),
    ("Embedded Finance", "SHOP", "→", "PAY"),
    ("Banking-as-a-Service", "API", "→", "BANK"),
    ("Open Banking", "OPEN", "↔", "DATA"),
    ("API Architecture", "APP", "→", "API"),
    ("Cloud Finance", "CLOU", "↔", "FIN"),
    ("AI in Finance", "AI", "↔", "DATA"),
    ("Real-time Risk", "TIME", "→", "SAFE"),
    ("Fraud Detection", "SCAN", "↔", "FAKE"),
    ("Credit Scoring", "DATA", "→", "LOAN"),
    ("Digital Identity", "ID", "↔", "FIN"),
    ("KYC Process", "WHO", "↔", "CHK"),
    ("Verifiable Cred", "CERT", "↔", "ID"),
    ("Privacy Finance", "PRIV", "↔", "SAFE"),
    ("Zero-Knowledge", "HIDE", "↔", "PROV"),
    ("Blockchain Infra", "BC", "↔", "LEDG"),
    ("Distributed Ledger", "SYNC", "↔", "MANY"),
    ("Tokenization", "REAL", "→", "TOK"),
    ("Tokenized Sec", "SEC", "↔", "TOK"),
    ("RWA Tokenization", "ASST", "→", "TOK"),
    ("Digital Bonds", "BOND", "↔", "TOK"),
    ("Digital Settlement", "SETT", "↔", "BC"),
    ("Atomic Settlement", "ONE", "→", "ALL"),
    ("DvP Model", "PAY", "↔", "ASST"),
    ("Central Securities", "CSD", "↔", "MKT"),
    ("Central Counterparty", "CCP", "↔", "RISK"),
    ("Digital Custody", "KEY", "↔", "STOR"),
    ("Self-Custody", "OWN", "↔", "KEY"),
    ("Programmable Money", "CODE", "↔", "CASH"),
    ("Programmable Pay", "IF", "→", "PAY"),
    ("Smart Contracts", "RULE", "↔", "ACT"),
    ("M2M Payments", "IOT", "↔", "PAY"),
    ("AI Agents Finance", "BOT", "↔", "FIN"),
    ("Raast Milestone", "20T", "↔", "DONE"),
    ("Digital Licenses", "5", "↔", "SBP"),
    ("Operational Banks", "3", "↔", "LIVE"),
    ("HugoBank", "HUGO", "↔", "LIVE"),
    ("Easypaisa Bank", "EASY", "↔", "LIVE"),
    ("Mashreq Bank", "MASH", "↔", "LIVE"),
    ("Regulatory Sandbox", "TEST", "↔", "SAFE"),
    ("Merchant Digital", "1M", "↔", "QR"),
    ("DPI Integration", "DPI", "↔", "NATL"),
    ("Raast Bulk Module", "BULK", "↔", "PAY"),
    ("Remittance Loop", "GLOB", "→", "HOME"),
    ("Orakzai Finance", "ORAK", "↔", "NEW"),
    ("Regional Inclusion", "ALL", "↔", "PAY"),
    ("Financial Power", "POWR", "↔", "SYS"),
    ("Sovereign Assets", "OWN", "↔", "VALU"),
    ("National Reserve", "RESR", "↔", "NATL"),
    ("Asset Portability", "MOVE", "↔", "USER"),
    ("Network Security", "SAFE", "↔", "NET"),
    ("Validator Stake", "STAK", "↔", "SAFE"),
    ("Consensus Trust", "AGRE", "↔", "TRST"),
    ("Mathematical Proof", "MATH", "↔", "VERI"),
    ("Transparent Ledger", "OPEN", "↔", "LEDG"),
    ("Immutable Record", "SAME", "↔", "LEDG"),
    ("Decentralized ID", "DID", "↔", "FIN"),
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
    ("The Permanent Record", "STAY", "↔", "DONE"),
    ("Payment Rail", "RAIL", "↔", "BASE"),
    ("Clearing House", "CLR", "↔", "SETT"),
    ("Settlement Cycle", "TIME", "→", "ZERO"),
    ("Counterparty Risk", "RISK", "≠", "SAFE"),
    ("Liquidity Pool", "POOL", "↔", "PAY"),
    ("Collateral Loop", "LOCK", "↔", "LOAN"),
    ("Yield Generation", "GROW", "↔", "ASST"),
    ("Market Integrity", "FAIR", "↔", "MKT"),
    ("Audit Trail", "HIST", "↔", "CHK"),
    ("Compliance Flow", "RULE", "↔", "TX"),
    ("Reporting Module", "REPT", "→", "GOV"),
    ("Standardized API", "STD", "↔", "API"),
    ("Secure Gateway", "GATE", "↔", "SAFE"),
    ("User Consent", "YES", "↔", "DATA"),
    ("Data Minimization", "LESS", "↔", "SAFE"),
    ("Financial Resilience", "STAY", "↔", "SAFE"),
    ("Legacy Migration", "OLD", "→", "NEW"),
    ("System Interop", "SYNC", "↔", "MANY"),
    ("Cross-Border Pay", "GLOB", "↔", "PAY"),
    ("Remittance Rail", "REMT", "↔", "BC"),
    ("Stablecoin Back", "BACK", "↔", "STBL"),
    ("CBDC Model", "CBDC", "↔", "NATL"),
    ("Wholesale CBDC", "BANK", "↔", "CBDC"),
    ("Retail CBDC", "USER", "↔", "CBDC"),
    ("Interbank Sett", "BANK", "↔", "NET"),
    ("Trade Finance", "TRAD", "↔", "BC"),
    ("Supply Chain", "SUPP", "↔", "BC"),
    ("Provenance", "ORIG", "↔", "BC"),
    ("Infrastructure Value", "VALU", "↔", "SYS"),
    ("The Future Rail", "TIME", "↔", "NEW"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g148-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g148-{index}-title g148-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g148-{index}-title">{safe}</title><desc id="g148-{index}-desc">A financial infrastructure relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g148-{index}-caption" class="diagram-caption">{index}. {safe} — Financial infrastructure relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Financial Infrastructure Framework</title><desc id="hero-desc">A diagram showing the integrated stack of financial infrastructure, from traditional layers to programmable digital rails.</desc><defs><linearGradient id="h148-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h148-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE DIGITAL FINANCIAL STACK (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DIGITAL IDENTITY (NADRA / Pak ID)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">RAAST INSTANT PAYMENT RAILS (DPI)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">DIGITAL BANKS & OPEN BANKING APIs</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">PROGRAMMABLE MONEY & SMART CONTRACTS</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">TOKENIZED ASSETS & RWA (BC/DLT)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AI RISK ENGINE & REAL-TIME ANALYTICS</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">USERS, BUSINESSES & AI AGENTS</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">FINANCIAL INFRASTRUCTURE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Institutions to Infrastructure: The Era of Programmable Value.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Financial Infrastructure Framework: The integrated stack of identity, payments, banking, and programmable assets for the 2026 economy.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 148</title>
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
            <p class="section-label">PAGE 148</p>
            <h2>FINANCIAL INFRASTRUCTURE OF THE FUTURE</h2>
            <p>“From Institutions to Infrastructure: The Era of Programmable Value.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Financial infrastructure is the invisible architecture that allows economies to move money, manage assets, and record ownership. For centuries, this depended on physical institutions and centralized systems. The next generation combines those institutions with cloud computing, AI, blockchain, and digital identity. The result is a new financial architecture where conventional trust meets cryptographic verification, enabling a programmable economy for the modern nation.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Digital Financial Stack in 2026</h3>
                <p>As of 2026, Pakistan's financial landscape has been redefined by the integration of **Digital Public Infrastructure (DPI)**. The traditional stack of central and commercial banks is now augmented by a programmable layer including **Digital Identity (NADRA)** and **Instant Payment Rails (Raast)**. This transformation allows for **Atomic Settlement**, where asset delivery and payment occur simultaneously, reducing counterparty risk and compressing the settlement cycle from days to milliseconds.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Raast & The Instant Payment Revolution</h3>
                <p>Pakistan's **Raast** platform has emerged as a global benchmark for instant payments, hitting the **Rs 20 trillion milestone** in early 2026. With over 892 million transactions handled, Raast supports P2P, P2M, and Bulk disbursements. The expansion of **QR-enabled merchants** to 1.09 million by June 2026 has brought digital payments to the smallest stalls in Orakzai, removing the geographic and physical barriers that once limited regional economic participation.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Banks & Open Banking</h3>
                <p>A major structural shift occurred in April 2026 with the operationalization of the first three digital banks: **Easypaisa Bank**, **Mashreq Bank**, and **HugoBank**. These institutions operate without physical branches, using **API-based Finance** and **Banking-as-a-Service (BaaS)** models to reach underserved populations. The SBP's **Open Banking Sandbox**, launched in January 2026, has enabled a new era of competition, where users can securely share their financial data to access personalized products and automated wealth management.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI, Risk & Programmable Money</h3>
                <p>Artificial Intelligence is no longer just an application; it is a core infrastructure layer for **Real-time Risk** management. Modern risk engines analyze transactions continuously, detecting fraud and assessing creditworthiness in milliseconds. This capability supports **Programmable Money**, where payments are triggered automatically when predefined conditions are met. From **M2M (Machine-to-Machine) payments** to AI agents managing corporate treasuries, the financial infrastructure of 2026 is designed for speed, security, and scale.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Financial Infrastructure</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Trust is being recoded. We are moving from trusting the building to trusting the protocol. The objective of future financial infrastructure is to create a system that is inclusive by design and resilient by architecture. From the bulk salary disbursements in Islamabad to the instant remittances in the Orakzai valleys, we are building a foundation where value moves at the speed of thought and the record remains permanent.”</p>
            </div>

            <div class="final-statement">
                INFRASTRUCTURE IS DESTINY.<br>
                VALUE IS PROGRAMMABLE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>State Bank of Pakistan (SBP), <em>Raast Hits Rs 20 Trillion Milestone: A Pillar of Digital Public Infrastructure (Jan 2026)</em>.</li>
                    <li>Fintech News Singapore, <em>Operational Status of Digital Banks in Pakistan: Easypaisa, Mashreq, and HugoBank (April 2026)</em>.</li>
                    <li>SBP / LinkedIn, <em>Launch of the Open Banking Regulatory Sandbox: First Cohort Shortlisted (Jan 2026)</em>.</li>
                    <li>Bizinjo / Industry Reports, <em>Merchant Digitalization in Pakistan: 1.09 Million QR Merchants (June 2026)</em>.</li>
                    <li>Lightspark Knowledge Base, <em>Instant Payments Pakistan: Bulk Modules and P2M Settlement Infrastructure (2025-2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            148
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

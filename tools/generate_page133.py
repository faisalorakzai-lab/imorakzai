from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-133-bitcoin-and-digital-money.html'

GRAPHICS = [
    ("Bitcoin Hero", "BTC", "↔", "GOLD"),
    ("Digital Money Model", "VALU", "→", "ELEC"),
    ("Bitcoin Innovation", "SCAR", "↔", "DIST"),
    ("Money Evolution", "BART", "→", "BTC"),
    ("Digital Scarcity", "DATA", "≠", "COPY"),
    ("Double Spend Prob", "ALIC", "↔", "BOB"),
    ("Satoshi Whitepaper", "P2P", "↔", "CASH"),
    ("Genesis Block", "JAN", "→", "2009"),
    ("Bitcoin Concepts", "NET", "↔", "ASST"),
    ("Digital Ownership", "KEY", "↔", "VALU"),
    ("Private Key Flow", "KEY", "→", "SIGN"),
    ("Address Generation", "PRIV", "→", "ADDR"),
    ("Bitcoin Transaction", "SEND", "→", "RECV"),
    ("Block Linkage", "BLK1", "→", "BLK2"),
    ("Shared History", "LEDG", "↔", "MANY"),
    ("Full Node Model", "VERI", "↔", "RULE"),
    ("Bitcoin Miner", "CPU", "→", "BLK"),
    ("Proof of Work Sec", "WORK", "→", "SEC"),
    ("Bitcoin Supply", "21M", "↔", "MAX"),
    ("Predictable Schedule", "CODE", "→", "TIME"),
    ("Bitcoin Halving", "SUBS", "→", "HALF"),
    ("Satoshi Division", "1BTC", "→", "100M"),
    ("Bitcoin Functions", "MEDM", "STOR", "UNIT"),
    ("Store of Value", "TIME", "↔", "VALU"),
    ("Medium of Exchange", "USER", "↔", "USER"),
    ("Unit of Account", "PRIC", "↔", "BTC"),
    ("Bitcoin Volatility", "UP", "↔", "DOWN"),
    ("BTC vs Fiat", "CODE", "≠", "INST"),
    ("Central Bank Money", "GOV", "→", "LEDG"),
    ("Commercial Bank", "BANK", "→", "DEPO"),
    ("Trust Minimization", "VERI", "↔", "TRST"),
    ("Custodial Model", "THRD", "↔", "USER"),
    ("Non-Custodial", "SELF", "↔", "KEY"),
    ("Virtual Assets Act", "LAW", "↔", "BTC"),
    ("PVARA Regulator", "PDA", "↔", "RULE"),
    ("Mining Allocation", "2GW", "↔", "MINE"),
    ("Crypto Adoption #3", "PAK", "↔", "GLB"),
    ("Institutional Int", "INST", "→", "BTC"),
    ("Remittance Loop", "GLB", "→", "LOCL"),
    ("Orakzai Digital", "TRI", "↔", "TECH"),
    ("Faisal Orakzai BTC", "SYS", "↔", "BTC"),
    ("Young Builder BTC", "LRN", "→", "BLD"),
    ("Blockchain History", "PAST", "→", "LEDG"),
    ("Digital Signature", "SIGN", "→", "AUTH"),
    ("Hashing Function", "DATA", "→", "HASH"),
    ("Distributed Time", "TIME", "↔", "NET"),
    ("Economic Incentive", "VAL", "→", "WORK"),
    ("Reliable History", "TRUE", "↔", "DATA"),
    ("No Central Issuer", "CODE", "↔", "VAL"),
    ("Transferable Value", "USER", "→", "USER"),
    ("Electronic Cash", "P2P", "↔", "PAY"),
    ("Online Payments", "NET", "→", "VAL"),
    ("No Intermediary", "SELF", "↔", "SELF"),
    ("Cryptographic Key", "KEY", "↔", "OWN"),
    ("Secret Value", "PRIV", "↔", "HIDE"),
    ("Public Info", "PUB", "↔", "SHOW"),
    ("Destination Addr", "SEND", "→", "ADDR"),
    ("Enforced Control", "CODE", "→", "SEC"),
    ("Previous Output", "PAST", "→", "SPND"),
    ("Cryptographic Auth", "SIGN", "→", "OK"),
    ("Organized Blocks", "TXN", "→", "BLK"),
    ("Independent Veri", "SELF", "→", "RULE"),
    ("Decentralized Arch", "MANY", "↔", "NET"),
    ("Verify Rules", "CHECK", "→", "OK"),
    ("Avoid Trust", "SELF", "≠", "THRD"),
    ("Computational Comp", "MINE", "↔", "MINE"),
    ("Protocol Reward", "BLK", "→", "BTC"),
    ("Economic Cost", "CASH", "→", "SEC"),
    ("Rewrite Defense", "COST", "→", "SAFE"),
    ("Software Scarcity", "CODE", "→", "LIMT"),
    ("Geological Gold", "EARTH", "≠", "BTC"),
    ("Consensus Scarcity", "AGRE", "→", "LIMT"),
    ("Block Subsidy", "REWD", "→", "MINE"),
    ("Zero New Subsidy", "END", "→", "2140"),
    ("Predictable Schedule", "PLAN", "↔", "TIME"),
    ("Smallest Unit", "SAT", "↔", "DIV"),
    ("Everyday Payments", "PAY", "↔", "DAY"),
    ("Suitability Affect", "FEE", "TIME", "VOL"),
    ("Long Term Store", "YEAR", "↔", "VAL"),
    ("Global Access", "ALL", "↔", "NET"),
    ("Price Standard", "PRIC", "↔", "CURR"),
    ("Dominant Unit", "MOST", "↔", "USD"),
    ("Purchasing Power", "BUY", "↔", "VAL"),
    ("Institutional Policy", "GOV", "→", "VAL"),
    ("Permissionless", "OPEN", "↔", "ALL"),
    ("Physical Cash", "CASH", "≠", "DIGI"),
    ("Banking Records", "BANK", "→", "DATA"),
    ("Technology Trust", "CODE", "↔", "TRST"),
    ("Intermediary Red", "LESS", "↔", "MANY"),
    ("Company Holding", "THRD", "→", "VAL"),
    ("User Control", "SELF", "→", "VAL"),
    ("Key Distincion", "KEY", "↔", "OWN"),
    ("Digital Infrastructure", "NODE", "+", "NET"),
    ("Mining Hardware", "ASIC", "→", "HASH"),
    ("Electricity Mix", "RENE", "+", "GRID"),
    ("Industrial Tool", "MINE", "→", "IND"),
    ("Energy Balancing", "GRID", "↔", "MINE"),
    ("Sovereign Compute", "GPU", "↔", "NAT"),
    ("Indigenous Tech", "LOCL", "↔", "SOLU"),
    ("Digital Jobs 2030", "SKIL", "→", "WORK"),
    ("Heritage Knowledge", "PAST", "→", "FUTR"),
    ("Algorithm Purpose", "FAST", "↔", "GOAL"),
    ("Faisal Orakzai Gen", "SYS", "↔", "DIGI"),
    ("Young Pak Builder", "LRN", "→", "BLD"),
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
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g133-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g133-{index}-title g133-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g133-{index}-title">{safe}</title><desc id="g133-{index}-desc">A Bitcoin relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#3C2D1A" stroke="#8B5E2E"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g133-{index}-caption" class="diagram-caption">{index}. {safe} — Bitcoin relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Bitcoin & Digital Money Framework</title><desc id="hero-desc">A diagram showing the integrated framework for Bitcoin, digital scarcity, and decentralized financial architecture.</desc><defs><linearGradient id="h133-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h133-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">DECENTRALIZED FINANCIAL ARCHITECTURE</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C2D1A" stroke="#8B5E2E"/><text x="0" y="5" font-size="12">SCARCITY</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C2D1A" stroke="#8B5E2E"/><text x="0" y="65" font-size="12">FIXED SUPPLY</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CONSENSUS</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">PROOF OF WORK</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">OWNERSHIP</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="65" font-size="12">PRIVATE KEYS</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">SOVEREIGN</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">MONEY</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">BITCOIN &amp; DIGITAL MONEY</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Electronic Cash to a New Digital Financial Architecture.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Bitcoin: The integrated framework for digital scarcity, Proof of Work consensus, and sovereign ownership.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 133</title>
    <link rel="stylesheet" href="../styles/main.css">
    <style>
        :root {{ --gold: #B59654; --rust: #8B5E2E; --teal: #2E8B8B; --cream: #F5F0E6; --muted: rgba(245,240,230,.72); }}
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
            <p class="section-label">PAGE 133</p>
            <h2>BITCOIN & DIGITAL MONEY</h2>
            <p>“From Electronic Cash to a New Digital Financial Architecture.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Bitcoin represents one of the most significant experiments in the history of digital money. It introduced a system in which people can transfer digital value across a network without requiring a traditional bank to maintain the central transaction ledger. Bitcoin did not invent digital payments, cryptography, electronic banking or online finance. Its major innovation was combining existing technologies into a system designed to enable scarce, transferable digital value without a central issuer controlling the ledger.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Digital Scarcity & The Double-Spending Problem</h3>
                <p>Digital information is normally trivial to copy, but money requires scarcity to function. Bitcoin solves the <strong>Double-Spending Problem</strong>—the risk of spending the same digital unit twice—through a distributed network and <strong>Proof of Work</strong> consensus. By organizing transactions into cryptographically linked blocks, the network creates a shared history that participants can independently verify. This ensures that control of a digital asset is enforced through cryptography rather than a centralized administrator.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Institutional Anchor: Virtual Assets Act 2026</h3>
                <p>Pakistan has formally recognized the role of digital money with the <strong>Virtual Assets Act 2026</strong>. This legislation establishes the <strong>Pakistan Virtual Assets Regulatory Authority (PVARA)</strong> as the primary oversight body, providing licenses for exchanges and digital wallets. Furthermore, the government has launched a national initiative to allocate <strong>2,000 megawatts of electricity</strong> for Bitcoin mining and AI data centers, framing these activities as critical components of the country's industrial and energy infrastructure.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Monetary Policy & The 21 Million Limit</h3>
                <p>Bitcoin's protocol specifies a maximum supply of 21 million units, with issuance decreasing periodically through <strong>Halving</strong> events. This predictable, code-based monetary schedule contrasts with the discretionary issuance of fiat currencies. While Bitcoin's market price remains volatile, its characteristics—limited supply, portability, and censorship resistance—have led to its emergence as a global store of value, with Pakistan climbing to <strong>3rd place globally</strong> in crypto adoption by 2026.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists growing up alongside the formalization of digital assets. His documented interests in software architecture and blockchain systems align with the "Secure & Decentralized" philosophy of 2026. He serves as one example of the "Young Pakistani Builder" who approaches Bitcoin not just as an asset, but as a structural innovation in financial infrastructure. His journey illustrates how individual expertise in private key management and distributed ledgers can shape national technological direction in the age of sovereign digital money.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Bitcoin & Digital Money</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Remittances & Financial Inclusion</h3>
                <p>For communities like Orakzai, Bitcoin and digital money offer a pathway to global financial access. By bypassing traditional banking barriers, the diaspora can send international remittances at a lower cost, while residents can participate in the global digital economy. The shift from "Custodial to Non-Custodial" models ensures that users maintain direct control over their assets, reflecting the traditional Pashtun value of individual autonomy within a secure, verifiable digital framework.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Money is not just a tool for exchange; it is a system of records. Bitcoin's contribution is the demonstration that those records can be maintained through an open protocol rather than an exclusive institution. For Pakistan, the opportunity is to integrate this new financial architecture into its national strategy for industrialization and digital jobs. The private key is the ultimate proof of digital ownership. A secure financial future requires that every citizen, from the hubs of commerce to the valleys of Orakzai, can trust the systems that store their value.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF MONEY IS PROGRAMMABLE.<br>
                BUT THE VALUE REMAINS HUMAN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Parliament of Pakistan, <em>Virtual Assets Act 2026: Legal Framework for Digital Assets</em>.</li>
                    <li>PVARA, <em>Official Portal: Licensing and Compliance Guidelines 2026</em>.</li>
                    <li>Reuters, <em>Pakistan allocates 2,000 MW of electricity to Bitcoin mining and AI data centers (2025/2026)</em>.</li>
                    <li>EY, <em>Institutional Investor Digital Assets Survey: 2026 Global Outlook</em>.</li>
                    <li>Nakamoto, S., <em>Bitcoin: A Peer-to-Peer Electronic Cash System (2008)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            133
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

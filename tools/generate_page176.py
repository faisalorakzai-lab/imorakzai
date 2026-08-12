from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-176-blockchain-native-economies.html'

GRAPHICS = [
    ("Blockchain Econ", "NET", "↔", "OWN"),
    ("Shared State", "MANY", "↔", "ONE"),
    ("Decentralization", "ALL", "↔", "RULE"),
    ("Consensus Rail", "YES", "↔", "DONE"),
    ("PoW Mechanism", "WORK", "↔", "TRUE"),
    ("PoS Validator", "STAK", "↔", "TRUE"),
    ("Node Network", "LINK", "↔", "ALL"),
    ("Cryptography", "SEC", "↔", "TRUE"),
    ("Private Key", "SELF", "↔", "OWN"),
    ("Digital Sign", "YES", "↔", "TRUE"),
    ("Wallet Interface", "USER", "↔", "NET"),
    ("Self-Custody", "SELF", "↔", "SAFE"),
    ("Custody Service", "THEY", "↔", "SAFE"),
    ("Digital Ownership", "OWN", "↔", "CODE"),
    ("Token Rep", "OWN", "↔", "NET"),
    ("Fungible Token", "SAME", "↔", "ALL"),
    ("NFT Record", "ONE", "↔", "UNIQUE"),
    ("Stablecoin Rail", "SAFE", "↔", "CASH"),
    ("Digital Payment", "PAY", "↔", "FAST"),
    ("Settlement Path", "DONE", "↔", "FAST"),
    ("Cross-Border", "HERE", "→", "GLOB"),
    ("Remittance Path", "GLOB", "→", "HOME"),
    ("Pak Diaspora", "GLOB", "↔", "HOME"),
    ("Fin Inclusion", "ALL", "↔", "CASH"),
    ("Digital Identity", "SELF", "↔", "TRUE"),
    ("Verif Creds", "TRUE", "↔", "SAFE"),
    ("Data Ownership", "OWN", "↔", "DATA"),
    ("Smart Contract", "RULE", "→", "DO"),
    ("Programmable $", "CASH", "↔", "CODE"),
    ("Prog Finance", "BIZ", "↔", "CODE"),
    ("DeFi Protocol", "ALL", "↔", "BIZ"),
    ("DEX Mechanism", "SWAP", "↔", "CODE"),
    ("Liquidity Pool", "MANY", "↔", "SWAP"),
    ("Lending Protocol", "LOAN", "↔", "CODE"),
    ("Collateral Path", "OWN", "↔", "LOAN"),
    ("Oracle Bridge", "OFF", "→", "ON"),
    ("Oracle Problem", "OFF", "≠", "TRUE"),
    ("RWA Tokenization", "PHYS", "→", "NET"),
    ("Token Securities", "LAW", "↔", "NET"),
    ("Treasury Token", "CASH", "↔", "NET"),
    ("Real Estate Tok", "LAND", "↔", "NET"),
    ("Property Record", "LAND", "↔", "TRUE"),
    ("Supply Chain", "SHIP", "↔", "TRUE"),
    ("Product Prov", "PAST", "↔", "TRUE"),
    ("Digital Cert", "TRUE", "↔", "NET"),
    ("IP Protection", "ART", "↔", "TRUE"),
    ("Royalty Auto", "CASH", "↔", "RULE"),
    ("Creator Economy", "MAKE", "↔", "ALL"),
    ("Digital Commerce", "BUY", "↔", "SELL"),
    ("Token Gating", "OWN", "→", "IN"),
    ("Digital Member", "OWN", "↔", "IN"),
    ("DAO Governance", "ALL", "↔", "RULE"),
    ("DAO Voting", "YES", "↔", "ALL"),
    ("Governance Risk", "WHY", "≠", "TRUE"),
    ("Voting Power", "OWN", "↔", "VOTE"),
    ("Governance Attk", "BAD", "→", "RULE"),
    ("Digital Treasury", "CASH", "↔", "RULE"),
    ("Prog Treasury", "RULE", "→", "CASH"),
    ("Decentral Infra", "GRID", "↔", "ALL"),
    ("Layer-1 Net", "BASE", "↔", "ALL"),
    ("Layer-2 Net", "FAST", "↔", "BASE"),
    ("Scalability Path", "GROW", "↔", "FAST"),
    ("Tx Fees Rail", "PAY", "↔", "MOVE"),
    ("Finality Speed", "DONE", "↔", "FAST"),
    ("Interoperability", "LINK", "↔", "LINK"),
    ("Cross-Chain", "NET", "↔", "NET"),
    ("Blockchain Bridge", "LINK", "↔", "ALL"),
    ("Programmable Economy", "RULE", "↔", "CASH"),
    ("Digital Settlement", "DONE", "↔", "NET"),
    ("Sovereign Grid", "ORAK", "↔", "GRID"),
    ("Future Builder", "SELF", "↔", "NEXT"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g176-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g176-{index}-title g176-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g176-{index}-title">{safe}</title><desc id="g176-{index}-desc">A blockchain-native economy relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g176-{index}-caption" class="diagram-caption">{index}. {safe} — Blockchain-native economy relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Blockchain-Native Economies Framework</title><desc id="hero-desc">A diagram showing the 2026 blockchain-native landscape, featuring RWA tokenization, Pakistan's $25B digital currency holdings, and the integration of programmable finance into global capital flows.</desc><defs><linearGradient id="h176-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h176-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE BLOCKCHAIN-NATIVE ECONOMY LOOP (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">MARKET CAP: $2.6T STABILIZED (APRIL 2026)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">RWA TOKENIZATION: $60B ACROSS 7000+ PRODUCTS</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">PAKISTAN: 3RD GLOBALLY IN ADOPTION ($25B HELD)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">REMITTANCES: $50B POTENTIAL VIA REGULATION</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">VIRTUAL ASSETS ACT & SBP POLICY REFORMS (2026)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">ORAKZAI SOVEREIGN GRID: PROGRAMMABLE OWNERSHIP</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">ECONOMY: DECENTRALIZED, PROGRAMMABLE & GLOBAL</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">BLOCKCHAIN-NATIVE ECONOMIES</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Digital Networks to Programmable Economies: Ownership, Settlement and Scale.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Blockchain-Native Economy Loop: Navigating the 2026 landscape where digital ownership, RWA tokenization, and decentralized finance converge to reshape global capital flows and sovereign infrastructure.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 176</title>
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
            <p class="section-label">PAGE 176</p>
            <h2>BLOCKCHAIN-NATIVE ECONOMIES</h2>
            <p>“From Digital Networks to Programmable Economies.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “The internet changed how information moves; blockchain technology introduced digital networks capable of maintaining shared records and enabling programmable ownership without a single operator. A blockchain-native economy imagines economic activity increasingly organized around programmable digital assets, decentralized networks, and smart contracts. This does not mean traditional institutions disappear; instead, these systems become another layer of economic infrastructure. For Pakistan, the significance lies in building new forms of digital ownership, settlement, and cross-border commerce.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Digital Assets & Market Maturity (2026)</h3>
                <p>By 2026, the global digital asset market has reached a point of institutional maturity, with the total market capitalization stabilized around **$2.6 trillion** after peaking at $4.4 trillion in late 2025 [1] [2]. Institutional volume in crypto markets is expected to surpass **$500 billion** in 2026, driven by the integration of programmable finance into global capital flows [3]. This "Second Digital Economy" moves beyond information distribution toward the management of shared state and programmable ownership across distributed networks [4].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Real-World Asset (RWA) Tokenization</h3>
                <p>The tokenization of real-world assets (RWAs) has hit a major milestone, reaching **$60 billion** across more than 7,000 products by 2026 [5]. Driven by crypto volatility and the need for yield, RWA total value locked (TVL) is projected to exceed **$100 billion** by the end of the year [6]. Entire asset classes—from real estate and treasury products to intellectual property—are becoming tradable on-chain, reshaping investment liquidity and global finance through decentralized settlement and verifiable credentials [7] [8].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pakistan's Crypto Adoption & Remittances</h3>
                <p>Pakistan ranks **third globally** in cryptocurrency adoption, with citizens collectively holding between **$20 to $25 billion** in digital currencies as of 2026 [9]. The introduction of the *Virtual Assets Act* and SBP policy reforms has created a pathway for formalization, with projections suggesting that remittance inflows could jump to **$50 billion** if digital financial infrastructure is properly regulated [10] [11]. For the Pakistani diaspora, blockchain provides an alternative rail for cross-border value transfer, improving financial inclusion through self-custody and stablecoin-based settlement [12].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Smart Contracts, DAOs & Sovereign Infrastructure</h3>
                <p>Programmable economies rely on smart contracts to automate financial functions, from lending protocols and decentralized exchanges (DEXs) to royalty payments for the creator economy [13]. Decentralized Autonomous Organizations (DAOs) use these mechanisms to coordinate activities and manage digital treasuries, though they face ongoing challenges in governance and security [14]. For the Orakzai community, the **Sovereign Grid** represents a blockchain-native approach to infrastructure, securing digital identity and ownership while ensuring interoperability across global networks [15].</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Blockchain-Native Economies</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“For the Orakzai people, blockchain is the digital ledger of our resilience. We do not just participate in global markets; we build the networks that protect our ownership. By mastering programmable finance and RWA tokenization while securing our sovereign data, we are ensuring that our economic future is decentralized and authentic. We are the architects of a programmable tomorrow where our assets and our identity remain ours.”</p>
            </div>

            <div class="final-statement">
                PROGRAMMABLE OWNERSHIP.<br>
                DECENTRALIZED IMPACT.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>World Economic Forum, <em>Digital Economy Inflection Point: What to Expect for Digital Assets in 2026 (January 2026)</em>.</li>
                    <li>OECD, <em>Asia Capital Markets Report 2026: Developments in Crypto-Asset Markets (June 2026)</em>.</li>
                    <li>LinkedIn / Karthik Swamy, <em>5 Blockchain Trends Reshaping the Global Economy in 2026 (July 2026)</em>.</li>
                    <li>MarketsandMarkets, <em>Blockchain Technology Market Size and Projections 2026-2031 (2026)</em>.</li>
                    <li>Yahoo Finance, <em>Reality of RWA Tokenization in 2026: Institutional Readiness (July 2026)</em>.</li>
                    <li>Centrifuge Blog, <em>2026: What to Expect from Real-World Asset Tokenization (December 2025)</em>.</li>
                    <li>Investax, <em>Real World Asset Tokenization: Trends and Outlook for 2026 (May 2026)</em>.</li>
                    <li>Mordor Intelligence, <em>Asset Tokenization Market Forecast, Size & Growth 2031 (January 2026)</em>.</li>
                    <li>Asian Development Bank / ProPakistani, <em>Pakistan's Digital Currency Holdings and Remittance Potential (May 2026)</em>.</li>
                    <li>Binance Square, <em>Pakistan Cryptocurrency Adoption in 2026: Virtual Assets Act and SBP Reforms (May 2026)</em>.</li>
                    <li>Express News PK, <em>Cryptocurrency Regulation in Pakistan: New Taxes and Legal Framework (June 2026)</em>.</li>
                    <li>TRM Labs, <em>2026 Crypto Crime Report: Trends in the Illicit Crypto Economy (January 2026)</em>.</li>
                    <li>Coherent Market Insights, <em>Blockchain Technology Market Size and Forecast 2026-2033 (2026)</em>.</li>
                    <li>Research and Markets, <em>Real-World Asset (RWA) Tokenization Market Report 2026 (2026)</em>.</li>
                    <li>Orakzai Group Archives, <em>Blockchain-Native Economy and Sovereign Infrastructure Framework (August 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            176
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

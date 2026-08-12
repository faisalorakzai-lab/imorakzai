from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-135-decentralized-finance.html'

GRAPHICS = [
    ("DeFi Hero", "FIN", "↔", "CODE"),
    ("DeFi Architecture", "USER", "→", "ACTN"),
    ("TradFi Model", "BANK", "→", "SETL"),
    ("DeFi Model", "PROT", "→", "SETL"),
    ("Logic as Code", "RULE", "→", "EXEC"),
    ("Programmable Finance", "CODE", "↔", "VALU"),
    ("Open Access", "ALL", "↔", "NET"),
    ("Non-Custodial", "SELF", "↔", "KEY"),
    ("Self-Custody", "KEY", "↔", "OWN"),
    ("Trust Shift", "INST", "→", "MATH"),
    ("Transparency", "VIEW", "↔", "LEDG"),
    ("Composability", "LEGO", "↔", "LEGO"),
    ("Money Legos", "APP", "↔", "APP"),
    ("Interconnected Risk", "FAIL", "→", "ALL"),
    ("DEX vs CEX", "PROT", "≠", "INST"),
    ("AMM Pattern", "MATH", "→", "POOL"),
    ("Liquidity Pool", "ASST", "↔", "TRAD"),
    ("Liquidity Provider", "DEP", "→", "FEE"),
    ("Impermanent Loss", "PRIC", "↔", "LOSS"),
    ("Slippage", "EXPC", "≠", "ACTL"),
    ("Price Impact", "SIZE", "→", "PRIC"),
    ("Oracles", "REAL", "→", "DATA"),
    ("Oracle Problem", "FAKE", "→", "FAIL"),
    ("Lending Protocol", "BORR", "↔", "LEND"),
    ("Collateral Model", "VALU", "→", "LOAN"),
    ("Overcollateralized", "$150", "→", "$100"),
    ("Liquidation Loop", "FALL", "→", "SELL"),
    ("Liquidation Cascade", "SELL", "→", "FALL"),
    ("Interest Rates", "UTIL", "→", "RATE"),
    ("Algorithmic Market", "CODE", "→", "MARK"),
    ("Stablecoins", "PEGD", "↔", "VALU"),
    ("Fiat-Backed", "RESR", "↔", "STBL"),
    ("Crypto-Collateral", "ASST", "↔", "STBL"),
    ("Algorithmic Stable", "MECH", "↔", "STBL"),
    ("Programmable Pay", "AUTO", "→", "PAY"),
    ("Cross-Border", "GLB", "↔", "SETL"),
    ("Remittance Loop", "SEND", "→", "RECV"),
    ("On-Ramp", "CASH", "→", "DIGI"),
    ("Off-Ramp", "DIGI", "→", "CASH"),
    ("DeFi Pakistan", "PAK", "↔", "PROT"),
    ("Financial Inclusion", "ALL", "↔", "FIN"),
    ("Digital Divide", "TECH", "≠", "ACC"),
    ("DeFi Entrepreneur", "BLD", "→", "PROT"),
    ("Faisal Orakzai DeFi", "SYS", "↔", "FIN"),
    ("OKBOND DeFi", "VALU", "↔", "CONT"),
    ("Orakzai Sovereign Grid", "SOV", "↔", "GRID"),
    ("DeFi Infra Stack", "APP", "PRT", "BC"),
    ("Wallet Layer", "KEY", "↔", "INTF"),
    ("Smart Contract Layer", "RULE", "↔", "CODE"),
    ("Oracle Layer", "DATA", "↔", "TRST"),
    ("Settlement Layer", "CONS", "→", "SETL"),
    ("Data Layer", "INDX", "↔", "ANLY"),
    ("Front-End Layer", "UI", "↔", "USR"),
    ("Front-End Central", "CLD", "→", "UI"),
    ("Governance Loop", "VOTE", "→", "ACT"),
    ("Governance Tokens", "TOKN", "↔", "VOTE"),
    ("Multisig Model", "MANY", "→", "ONE"),
    ("Timelock", "TIME", "↔", "ACT"),
    ("Protocol Upgrade", "NEW", "→", "LOGC"),
    ("DeFi Security", "SAFE", "↔", "CODE"),
    ("Flash Loan", "BORR", "→", "REPY"),
    ("Flash Loan Attack", "CAP", "→", "XPLT"),
    ("Economic Security", "VAL", "↔", "INCN"),
    ("Formal Verification", "MATH", "→", "TRUE"),
    ("DeFi vs TradFi", "CODE", "≠", "INST"),
    ("Market Efficiency", "FAST", "↔", "CODE"),
    ("Resource Allocation", "GAS", "→", "CAP"),
    ("Global Liquidity", "GLB", "↔", "POOL"),
    ("Yield Farming", "VAL", "→", "REWD"),
    ("Staking Rewards", "STAK", "→", "FEE"),
    ("Derivative Engine", "OPTN", "↔", "FUTR"),
    ("Synthetic Assets", "SYNT", "↔", "REAL"),
    ("Insurance Mutual", "PROT", "↔", "POOL"),
    ("Asset Management", "AUTO", "→", "PORT"),
    ("Portfolio Tracker", "VIEW", "↔", "ASST"),
    ("Bridge Protocol", "CHIN", "↔", "CHIN"),
    ("Interoperability", "X", "↔", "Y"),
    ("MEV Concept", "VALU", "↔", "ORDR"),
    ("Frontrunning", "FAST", "→", "GAIN"),
    ("Sandwich Attack", "BUY", "MID", "SELL"),
    ("Governance Minim", "LESS", "↔", "RULE"),
    ("Immutable Finance", "CODE", "↔", "FIXD"),
    ("Compliance Interface", "LAW", "↔", "CODE"),
    ("KYC/AML Bridge", "ID", "↔", "PROT"),
    ("Privacy DeFi", "HIDE", "↔", "TXN"),
    ("ZK DeFi", "PRUF", "↔", "TRUE"),
    ("Institutional DeFi", "CORP", "→", "PROT"),
    ("Real-World Yield", "REAL", "→", "DEFI"),
    ("Credit Markets", "CRED", "↔", "DEFI"),
    ("Undercollateralized", "ID", "→", "LOAN"),
    ("Reputation Score", "PAST", "→", "CRDT"),
    ("DeFi for SMEs", "SME", "↔", "CAP"),
    ("Remittance Cost", "LESS", "↔", "FEES"),
    ("Digital Literacy", "EDU", "→", "ACC"),
    ("Consumer Protect", "LAW", "↔", "USR"),
    ("Infrastructure Opportunity", "BLD", "→", "BASE"),
    ("Software Rules", "CODE", "↔", "RULE"),
    ("Autonomous Economy", "AI", "→", "DEFI"),
    ("Machine Payments", "IOT", "→", "DEFI"),
    ("Sovereign Finance", "NAT", "↔", "DEFI"),
    ("Transparent Settlement", "VIEW", "↔", "SETL"),
    ("Verification Bridge", "HUM", "↔", "CODE"),
    ("DeFi Evolution", "MONY", "→", "SYS"),
    ("Next Gen Builder", "SKIL", "→", "BLD"),
    ("Final DeFi Arch", "GLB", "↔", "SOV"),
    ("Orakzai Heritage DeFi", "PAST", "→", "FUTR"),
    ("Digital Trust Loop", "MATH", "↔", "TRST"),
    ("Security Fortress", "PROT", "↔", "ATTK"),
    ("Audit Lifecycle", "CODE", "CHK", "SAFE"),
    ("Economic Audit", "INCN", "CHK", "STBL"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g135-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g135-{index}-title g135-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g135-{index}-title">{safe}</title><desc id="g135-{index}-desc">A DeFi relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g135-{index}-caption" class="diagram-caption">{index}. {safe} — DeFi relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Decentralized Finance Framework</title><desc id="hero-desc">A diagram showing the transition from traditional institutional finance to a programmable, composable, and decentralized financial ecosystem.</desc><defs><linearGradient id="h135-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h135-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">PROGRAMMABLE FINANCIAL ECOSYSTEM</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">LIQUIDITY</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="65" font-size="12">DEX / AMM</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">LENDING</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">COLLATERAL</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">STABILITY</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="65" font-size="12">STABLECOINS</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">DECENTRALIZED</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">FINANCE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">DECENTRALIZED FINANCE (DEFI)</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Reimagining Financial Infrastructure Through Software.”</text></svg><figcaption id="hero-caption" class="diagram-caption">DeFi: The integrated framework for liquidity, lending, and stability through programmable blockchain protocols.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 135</title>
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
            <p class="section-label">PAGE 135</p>
            <h2>DECENTRALIZED FINANCE (DEFI)</h2>
            <p>“Reimagining Financial Infrastructure Through Software.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “If Bitcoin introduced the concept of decentralized digital money, and Ethereum introduced programmable blockchain infrastructure, Decentralized Finance (DeFi) brought those ideas into financial services. DeFi refers broadly to financial applications built using blockchain networks and smart contracts. Its ambition is significant: to make financial functions programmable, transparent, composable, and accessible through open digital infrastructure. DeFi does not eliminate every intermediary, but experiments with moving specific financial functions from traditional institutions into software-based protocols.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Financial Logic as Code</h3>
                <p>Traditional financial systems encode rules through institutional policies, legal agreements, and centralized software. DeFi shifts this paradigm by encoding rules directly into <strong>Smart Contracts</strong>, enabling automated execution. This turns financial infrastructure into programmable systems where interest-rate curves, trading formulas, and collateral ratios are transparent and verifiable. The core idea is <strong>Composability</strong>—the ability for protocols to interact like "Money Legos," accelerating innovation by building on existing primitives.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Institutional Anchor: Virtual Assets Act 2026</h3>
                <p>Pakistan has formally recognized the shift toward digital finance with the <strong>Virtual Assets Act 2026</strong>. This landmark legislation establishes a comprehensive regulatory framework for virtual assets, including stablecoins and tokenized assets, moving the sector from a legal "grey zone" to a regulated environment. The <strong>State Bank of Pakistan (SBP)</strong> and the <strong>Pakistan Virtual Assets Regulatory Authority (PVARA)</strong> are aligning to oversee a market where Pakistanis collectively hold an estimated <strong>$20 to $25 billion</strong> in digital currencies as of 2026.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">DEXs, AMMs & Lending Protocols</h3>
                <p>Decentralized exchanges (DEXs) allow users to trade assets directly from their wallets using <strong>Automated Market Makers (AMMs)</strong> and liquidity pools. Lending protocols enable users to deposit assets and borrow against collateral, often requiring <strong>Overcollateralization</strong> to buffer against market volatility. While these systems offer open access and transparency, they also introduce technical and economic trust assumptions, including risks like <strong>Impermanent Loss</strong>, oracle failure, and liquidation cascades during extreme volatility.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists approaching blockchain not merely as an asset class, but as infrastructure for programmable financial systems. His documented involvement in digital-asset initiatives, such as <strong>Orakzai Bond (OKBOND)</strong>, illustrates the shift toward building verifiable, code-based financial rules. He serves as one example of the "Young Pakistani Builder" who advocates for systems where trust is redistributed through mathematics and code, ensuring that financial infrastructure remains transparent, resilient, and inclusive for remote districts like Orakzai.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Decentralized Finance</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Financial Inclusion & The Digital Divide</h3>
                <p>DeFi is often presented as a tool for financial inclusion, offering internet-based access to global liquidity and programmable payments. For communities like Orakzai, this could mean lower remittance costs and access to secure digital savings. However, technology alone cannot eliminate exclusion; <strong>Digital Literacy</strong>, reliable internet, and consumer protection remain essential. The shift from "Custodial to Self-Custody" models empowers users but places greater responsibility on them to secure their private keys and understand the underlying protocol risks.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“DeFi does not eliminate trust; it redistributes it. By moving financial logic into open protocols, we create an infrastructure that is verifiable by design. For Pakistan, the opportunity is to leverage this programmable architecture to build financial products that serve the unbanked and lower the friction of global commerce. A secure financial future requires that every citizen, from the hubs of industry to the valleys of Orakzai, can participate in the systems that manage their value. The private key is the ultimate proof of ownership, and the code is the ultimate rule.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF FINANCE IS COMPOSABLE.<br>
                BUT THE RESPONSIBILITY REMAINS HUMAN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Parliament of Pakistan, <em>Virtual Assets Act 2026: Regulatory Framework for Digital Financial Services</em>.</li>
                    <li>Asian Development Bank (ADB), <em>Pakistan Virtual Asset Landscape Report 2026</em>.</li>
                    <li>OECD, <em>Developments in Crypto-Asset Markets: Asia Capital Markets Report 2026</em>.</li>
                    <li>Hidayat-ur-Rehman, I., et al., <em>Digital Financial Inclusion, DeFi Capability, and AI Research 2026</em>.</li>
                    <li>State Bank of Pakistan (SBP), <em>Digital Financial Services & Regulatory Checklist 2026</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            135
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

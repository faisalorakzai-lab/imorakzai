from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-134-ethereum-smart-contracts.html'

GRAPHICS = [
    ("Ethereum Concept", "DECE", "↔", "PROG"),
    ("BTC-to-ETH Evolution", "BTC", "→", "ETH"),
    ("Ethereum Ecosystem", "DEFI", "NFT", "DAO"),
    ("ETH Asset", "FEE", "↔", "SEC"),
    ("EVM Environment", "CODE", "→", "EXEC"),
    ("Smart Contract", "RULE", "↔", "CODE"),
    ("Blockchain Execution", "TXN", "→", "STAT"),
    ("Deterministic Exec", "SAME", "↔", "RSLT"),
    ("Ethereum State", "ACCT", "BAL", "STOR"),
    ("Account Categories", "EOA", "↔", "CONT"),
    ("EOA Model", "KEY", "→", "AUTH"),
    ("Contract Accounts", "CODE", "→", "ACTN"),
    ("Gas Concept", "WORK", "↔", "COST"),
    ("Gas Fees", "RES", "→", "PAY"),
    ("Computational Res", "CPU", "MEM", "STOR"),
    ("Ethereum Blocks", "TXN", "→", "BLK"),
    ("Proof of Stake", "STAK", "↔", "CONS"),
    ("Validators", "ETH", "→", "SEC"),
    ("Staking Loop", "DEP", "→", "REWD"),
    ("Slashing Mechanism", "BAD", "→", "LOST"),
    ("The Merge", "POW", "→", "POS"),
    ("Ethereum Energy", "LESS", "↔", "CONS"),
    ("Decentralization", "CLNT", "GEOG", "STAK"),
    ("Client Diversity", "MANY", "→", "RESI"),
    ("Solidity Language", "CODE", "↔", "CONT"),
    ("Contract Deployment", "DEV", "→", "NET"),
    ("Immutable Contracts", "CODE", "↔", "FIXD"),
    ("Upgradeable Contracts", "PROX", "→", "LOGC"),
    ("Admin Keys", "AUTH", "→", "MOD"),
    ("Smart Contract Audit", "CHK", "→", "SAFE"),
    ("Security Vulnerability", "BUG", "→", "RISK"),
    ("Reentrancy Pattern", "CALL", "→", "BACK"),
    ("Oracles", "REAL", "→", "DATA"),
    ("Oracle Problem", "FAKE", "→", "FAIL"),
    ("Tokens", "ASST", "↔", "CONT"),
    ("ERC-20 Standard", "FUNG", "↔", "EQL"),
    ("ERC-721 Standard", "NFT", "≠", "NFT"),
    ("ERC-1155 Standard", "MULT", "↔", "FLEX"),
    ("Fungibility", "1=1", "↔", "SAME"),
    ("dApps", "UI", "CONT", "WAL"),
    ("dApp Architecture", "USR", "→", "BC"),
    ("DeFi Ecosystem", "FIN", "↔", "CODE"),
    ("DEX Model", "SWAP", "↔", "POOL"),
    ("AMM Pattern", "MATH", "→", "PRIC"),
    ("Liquidity Pools", "ASST", "↔", "TRAD"),
    ("Liquidity Providers", "DEP", "→", "FEE"),
    ("Lending Protocol", "BORR", "↔", "LEND"),
    ("Collateral Model", "VALU", "→", "LOAN"),
    ("Liquidation Loop", "FALL", "→", "SELL"),
    ("Stablecoins", "PEGD", "↔", "VALU"),
    ("Tokenized Assets", "REAL", "→", "TOKN"),
    ("Tokenization", "RGHT", "↔", "DATA"),
    ("Digital Ownership", "TOKN", "↔", "OWN"),
    ("NFTs", "UNIQ", "↔", "DATA"),
    ("NFT Art", "CRTV", "↔", "BC"),
    ("DAOs", "VOTE", "→", "ACT"),
    ("Governance Model", "RULE", "↔", "COMM"),
    ("Ethereum Governance", "EIP", "↔", "SOCL"),
    ("EIP Process", "PROP", "→", "STD"),
    ("Layer-2 Scaling", "L2", "→", "L1"),
    ("Rollups", "BAT", "→", "ETH"),
    ("Optimistic Rollups", "TRST", "↔", "CHAL"),
    ("ZK Rollups", "PRUF", "↔", "TRUE"),
    ("Modular Blockchain", "EXEC", "SETL", "DATA"),
    ("Ethereum Settlement", "L2", "→", "SAFE"),
    ("Mainnet", "REAL", "↔", "VALU"),
    ("Testnets", "TEST", "↔", "SAFE"),
    ("Wallet Infra", "KEY", "↔", "INTF"),
    ("Private Keys", "HIDE", "→", "OWN"),
    ("Account Abstraction", "PROG", "↔", "WAL"),
    ("Smart Wallets", "RECV", "↔", "LIMT"),
    ("Decentralized ID", "SELF", "↔", "ID"),
    ("Blockchain Privacy", "HIDE", "↔", "VERI"),
    ("ZK Proofs", "TRUE", "≠", "DATA"),
    ("Ethereum + AI", "CODE", "↔", "AI"),
    ("AI Wallets", "AI", "→", "KEY"),
    ("AI Agents", "AUTO", "→", "ACT"),
    ("Ethereum + Finance", "24/7", "↔", "CODE"),
    ("24/7 Markets", "OPEN", "↔", "TIME"),
    ("Global Ethereum", "GLB", "↔", "NET"),
    ("Ethereum + Pakistan", "PAK", "↔", "DEV"),
    ("Pakistani Developers", "LRN", "→", "BLD"),
    ("Faisal Orakzai", "SYS", "↔", "CODE"),
    ("Orakzai Bond", "OKB", "↔", "L2"),
    ("OKBOND", "VALU", "↔", "CONT"),
    ("Orakzai Sovereign Grid", "SOV", "↔", "GRID"),
    ("Ethereum vs Bitcoin", "PROG", "≠", "MONY"),
    ("Ethereum vs Cloud", "DECE", "≠", "CENT"),
    ("On-chain vs Off-chain", "VERI", "≠", "SIZE"),
    ("Hybrid Architecture", "BC", "+", "CLD"),
    ("Smart-Contract Finance", "AUTO", "→", "SETL"),
    ("Tokenized Finance", "PROG", "→", "ASST"),
    ("RWA Architecture", "LEGL", "↔", "TOKN"),
    ("Legal/Oracle Layer", "LAW", "↔", "DATA"),
    ("Security Infra", "SAFE", "↔", "CODE"),
    ("Formal Verification", "MATH", "→", "TRUE"),
    ("Bug Bounty", "FIND", "→", "REWD"),
    ("Systemic Risk", "FAIL", "→", "ALL"),
    ("Composability", "LEGO", "↔", "LEGO"),
    ("Money Legos", "APP", "↔", "APP"),
    ("Ethereum Network Effects", "USER", "→", "VALU"),
    ("Developer Ecosystem", "TOOL", "→", "DEV"),
    ("Ethereum Dev Stack", "UI", "WAL", "BC"),
    ("RPC Infrastructure", "CALL", "↔", "NODE"),
    ("Indexing", "QURY", "↔", "DATA"),
    ("Storage", "OFF", "↔", "HASH"),
    ("Ethereum Economics", "BURN", "↔", "MINT"),
    ("EIP-1559", "BASE", "→", "BURN"),
    ("ETH Supply", "DYN", "↔", "RULE"),
    ("ETH Utility", "GAS", "↔", "SEC"),
    ("Decentralized Computation", "MANY", "→", "TRUE"),
    ("Blockchain Computing", "CONS", "→", "STAT"),
    ("Future Smart Contracts", "AI", "↔", "IOT"),
    ("AI + Smart Contracts", "INTE", "→", "EXEC"),
    ("Autonomous Agents", "SELF", "→", "PAY"),
    ("Digital Sovereignty", "SELF", "↔", "SOV"),
    ("Decentralization Spectrum", "CENT", "→", "DECE"),
    ("Blockchain Limitations", "SLOW", "↔", "COST"),
    ("When to use Ethereum", "VERI", "↔", "AGRE"),
    ("When not to use Ethereum", "FAST", "↔", "PRIV"),
    ("Ethereum Historical Impact", "PAST", "→", "FUTR"),
    ("Faisal Orakzai Programmable-Future", "IDEA", "→", "CODE"),
    ("Blockchain-to-Infrastructure Evolution", "MONY", "→", "SYS"),
    ("Future Blockchain Builder", "SKIL", "→", "BLD"),
    ("Final Ethereum Architecture", "GLB", "↔", "SOV"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g134-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g134-{index}-title g134-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g134-{index}-title">{safe}</title><desc id="g134-{index}-desc">An Ethereum relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g134-{index}-caption" class="diagram-caption">{index}. {safe} — Ethereum relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Ethereum & Smart Contracts Framework</title><desc id="hero-desc">A diagram showing the integrated framework for Ethereum, smart contracts, and programmable digital infrastructure.</desc><defs><linearGradient id="h134-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h134-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">PROGRAMMABLE DIGITAL INFRASTRUCTURE</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">EVM</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="65" font-size="12">EXECUTION</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CONTRACTS</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">PROGRAMMABLE</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">STAKING</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="65" font-size="12">CONSENSUS</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">SOVEREIGN</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">COMPUTE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">ETHEREUM &amp; SMART CONTRACTS</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Digital Money to Programmable Infrastructure.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Ethereum: The integrated framework for EVM execution, smart contract programmability, and Proof-of-Stake consensus.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 134</title>
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
            <p class="section-label">PAGE 134</p>
            <h2>ETHEREUM & SMART CONTRACTS</h2>
            <p>“From Digital Money to Programmable Infrastructure.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Bitcoin established decentralized digital money; Ethereum expanded blockchain technology toward programmable digital infrastructure. Proposed by Vitalik Buterin in 2013, Ethereum introduced a general-purpose platform on which developers could deploy programs—smart contracts—that execute according to predefined rules. This transition shifted the narrative from simple peer-to-peer payments to a decentralized blockchain network capable of hosting a wide range of applications, from finance and identity to governance and tokenized assets.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The EVM & Deterministic Execution</h3>
                <p>One of Ethereum's most important concepts is the <strong>Ethereum Virtual Machine (EVM)</strong>, which provides a common execution environment for smart contracts. Every node in the network must arrive at the same result when executing transactions, ensuring <strong>Deterministic Execution</strong> and consensus. The network uses <strong>Gas</strong> to measure and price computational work, creating an economic mechanism that prevents resource abuse while allowing for complex, programmable software logic to operate on a distributed network.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Consensus & The Merge</h3>
                <p>In 2022, Ethereum completed <strong>The Merge</strong>, transitioning from Proof of Work to <strong>Proof of Stake</strong>. This significantly reduced the network's energy consumption and established a new consensus architecture based on validators who stake ETH. By August 2026, approximately **34% of the total ETH supply** (~41.4 million ETH) is staked by over **1.2 million active validators**, ensuring robust security and a decentralized foundation for the global Web3 ecosystem.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">DeFi, DAOs & Layer-2 Scaling</h3>
                <p>Ethereum has become the foundation for **Decentralized Finance (DeFi)**, enabling lending protocols, decentralized exchanges (DEXs), and stablecoins that operate 24/7 without traditional intermediaries. **Decentralized Autonomous Organizations (DAOs)** use smart contracts to coordinate groups through on-chain voting and treasury systems. To address scalability, the ecosystem has adopted a **Rollup-Centric Roadmap**, using Layer-2 networks (Optimistic and ZK-rollups) to process transactions while relying on Ethereum for final settlement and security.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists growing up alongside the shift toward programmable infrastructure. His documented involvement in blockchain and digital-asset initiatives, such as **Orakzai Bond (OKBOND)** on Polygon L2, illustrates how Pakistani builders are engaging with global Web3 technologies. He serves as one example of the "Young Pakistani Builder" who approaches technology as a conceptual bridge between software engineering and decentralized consensus. His journey emphasizes the importance of understanding how code, cryptography, and economics can become a new, sovereign infrastructure layer for the digital age.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Ethereum & Smart Contracts</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Security, Oracles & The Future</h3>
                <p>As smart contracts manage trillions in value, security infrastructure—including <strong>Formal Verification</strong>, audits, and bug bounties—has become essential. **Oracles** provide a critical bridge between blockchain state and external reality, though they introduce the "Oracle Problem" of data reliability. Looking forward, the integration of **AI Agents** with programmable wallets and smart contracts promises to create autonomous digital economies where machine-to-machine transactions occur securely on decentralized infrastructure, further expanding the concept of digital sovereignty.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Ethereum transformed blockchain from a monetary experiment into a programmable platform. Its significance lies in the idea that software can become part of a shared, sovereign economic infrastructure. For Pakistan, the opportunity is to leverage this open-source tooling to build applications that are verifiable by design and decentralized by architecture. The next generation of builders must bridge computer science, economics, and ethics to ensure that the programmable future remains transparent, resilient, and inclusive for all.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF CODE IS PROGRAMMABLE.<br>
                BUT THE TRUST REMAINS HUMAN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Beaconcha.in, <em>Ethereum Network Status: Staking and Validator Metrics August 2026</em>.</li>
                    <li>Ethereum Foundation, <em>EIP-1559 and The Merge: Technical Specifications</em>.</li>
                    <li>GoodFirms, <em>Top Blockchain Development Companies in Pakistan 2026 Survey</em>.</li>
                    <li>Orakzai Bond (OKBOND), <em>Technical Architecture and Polygon L2 Deployment Records (April 2026)</em>.</li>
                    <li>Vitalik Buterin, <em>Ethereum Roadmap: The Surge, The Verge, and The Splurge (2026 Status)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            134
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

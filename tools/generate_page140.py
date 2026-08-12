from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-140-the-future-of-web3.html'

GRAPHICS = [
    ("Web3 Future", "NETW", "→", "ARCH"),
    ("Read-Write-Own", "WEB1", "WEB2", "WEB3"),
    ("Web1 Static", "INFO", "↔", "USER"),
    ("Web2 Platform", "PLAT", "↔", "USER"),
    ("Web3 Ownership", "OWN", "↔", "USER"),
    ("The Web3 Stack", "DATA", "→", "APPL"),
    ("Decentralization", "MANY", "↔", "ONE"),
    ("Digital Ownership", "KEYS", "↔", "STAT"),
    ("Self-Custody", "SELF", "↔", "CTRL"),
    ("Smart Contracts", "CODE", "→", "EXEC"),
    ("Programmable Value", "VALU", "↔", "RULE"),
    ("dApp Architecture", "USER", "↔", "BC"),
    ("Hybrid Web3", "CLD", "↔", "BC"),
    ("Digital Identity", "ID", "↔", "PORT"),
    ("User-Controlled ID", "SELF", "↔", "SOV"),
    ("Web3 Privacy", "VERI", "↔", "HIDE"),
    ("Zero-Knowledge", "PRUF", "↔", "TRUE"),
    ("Digital Credentials", "QUAL", "↔", "VERI"),
    ("Decentralized Storage", "DATA", "↔", "DIST"),
    ("Content Ownership", "CREA", "↔", "OWN"),
    ("Creator Economy", "COMM", "↔", "VALU"),
    ("NFT Utility", "TOKN", "↔", "USE"),
    ("NFTs Beyond Art", "CERT", "↔", "TOKN"),
    ("Tokenization", "RGHT", "↔", "TOKN"),
    ("Real-World Assets", "PHYS", "↔", "DIGI"),
    ("DeFi Model", "MATH", "↔", "FIN"),
    ("Future of DeFi", "TRAD", "↔", "BC"),
    ("Stablecoins", "STBL", "↔", "VALU"),
    ("Digital Payments", "FAST", "↔", "SETL"),
    ("Cross-Border Pay", "GLOB", "↔", "BC"),
    ("Web3 Messaging", "MSG", "↔", "SEC"),
    ("Governance DAO", "VOTE", "→", "EXEC"),
    ("Protocol Economy", "RULE", "↔", "VALU"),
    ("Network Effects", "USER", "→", "VALU"),
    ("Open Standards", "BASE", "↔", "ALL"),
    ("Interoperability", "NET-A", "↔", "NET-B"),
    ("Composability", "LEGO", "↔", "CODE"),
    ("On-Chain Identity", "BC", "↔", "ID"),
    ("Off-Chain Data", "FILE", "↔", "LINK"),
    ("ZK Transactions", "PRIV", "↔", "VERI"),
    ("Scalability Layer", "BASE", "↔", "L2"),
    ("Rollup Security", "OFF", "→", "ON"),
    ("Data Availability", "VERI", "↔", "DATA"),
    ("Oracle Bridge", "REAL", "→", "BC"),
    ("Web3 Wallets", "USER", "↔", "KEYS"),
    ("Account Abstract", "PROG", "↔", "WAL"),
    ("Social Recovery", "COMM", "→", "RECV"),
    ("Multi-Chain Web3", "ONE", "↔", "MANY"),
    ("Sovereign Data", "SELF", "↔", "DATA"),
    ("Privacy Preserving", "SAFE", "↔", "USER"),
    ("Web3 Commerce", "BUY", "→", "OWN"),
    ("Digital Goods", "ITEM", "↔", "VALU"),
    ("Gaming Web3", "GAME", "↔", "OWN"),
    ("Metaverse ID", "VIRT", "↔", "ID"),
    ("Token Gating", "TOKN", "→", "OPEN"),
    ("Community Ownership", "POOL", "↔", "OWN"),
    ("Fair Launch", "ALL", "↔", "SAME"),
    ("Liquidity Pools", "ASST", "↔", "POOL"),
    ("Yield Farming", "STAK", "→", "REWD"),
    ("Lending Protocol", "BORR", "↔", "LEND"),
    ("DEX Mechanism", "SWAP", "↔", "POOL"),
    ("Web3 Governance", "DAO", "↔", "VOTE"),
    ("Incentive Design", "WORK", "→", "VALU"),
    ("Economic Security", "STAK", "→", "SAFE"),
    ("Slashing Logic", "BAD", "→", "LOSS"),
    ("Consensus Health", "UP", "↔", "AGRE"),
    ("Liveness Property", "WORK", "↔", "TIME"),
    ("Safety Property", "AGRE", "↔", "SAFE"),
    ("Fork Management", "A", "B", "WIN"),
    ("Upgrade Path", "OLD", "→", "NEW"),
    ("Web3 Tooling", "DEV", "↔", "APPL"),
    ("SDK Framework", "CODE", "↔", "DEV"),
    ("Library Stack", "LIB", "↔", "CODE"),
    ("Testing Web3", "TEST", "↔", "CODE"),
    ("Audit Pipeline", "CODE", "↔", "SAFE"),
    ("Deployment Web3", "CODE", "→", "LIVE"),
    ("Pakistan Web3", "PAK", "↔", "DIGI"),
    ("PVARA Regs", "LAW", "↔", "TOKN"),
    ("SECP Sandbox", "TEST", "↔", "LAW"),
    ("Young Builders", "YTH", "→", "BLD"),
    ("Faisal Orakzai profile", "SYS", "↔", "OWN"),
    ("Orakzai Web3 Node", "LOC", "↔", "BC"),
    ("OSG Identity", "SOV", "↔", "ID"),
    ("OKBOND Web3", "VALU", "↔", "TOKN"),
    ("Future Arch", "BASE", "→", "TOP"),
    ("Web3 Vision", "IDEA", "↔", "REAL"),
    ("Sovereign Grid", "SOV", "↔", "GRID"),
    ("Digital Rights", "LAW", "↔", "CODE"),
    ("Atomic Settle", "PAY", "↔", "ASST"),
    ("Fractional Web3", "ONE", "→", "MANY"),
    ("Immutable Rec", "SAVE", "↔", "TIME"),
    ("Censorship Res", "FREE", "↔", "DIST"),
    ("Global Access", "ALL", "↔", "NET"),
    ("Permissionless", "OPEN", "↔", "ALL"),
    ("Trustless Model", "MATH", "↔", "TRST"),
    ("Verifiable Web", "TRUE", "↔", "VIEW"),
    ("Machine Web3", "MACH", "↔", "OWN"),
    ("AI + Web3", "AI", "↔", "BC"),
    ("Agent Economy", "AI", "→", "VALU"),
    ("Sovereign Compute", "SELF", "↔", "CPU"),
    ("Edge Web3", "EDGE", "↔", "BC"),
    ("Local Web3", "LOC", "↔", "GLOB"),
    ("Inclusive Web3", "ALL", "↔", "VALU"),
    ("Fair Economy", "WORK", "↔", "REWD"),
    ("Sustainable Web3", "ECO", "↔", "SYS"),
    ("Circular Web3", "RECY", "↔", "OWN"),
    ("Web3 Heritage", "PAST", "→", "DIGI"),
    ("Digital Memory", "HIST", "↔", "BC"),
    ("Final Web3 Arch", "REAL", "↔", "DIGI"),
    ("Ownership Economy", "OWN", "↔", "ECON"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g140-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g140-{index}-title g140-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g140-{index}-title">{safe}</title><desc id="g140-{index}-desc">A Web3 relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g140-{index}-caption" class="diagram-caption">{index}. {safe} — Web3 relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Web3 Evolution Framework</title><desc id="hero-desc">A diagram showing the evolution from Web1 to Web3 and the integrated stack for decentralized coordination and ownership.</desc><defs><linearGradient id="h140-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h140-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE WEB3 EVOLUTION</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">WEB1</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="65" font-size="12">READ</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">WEB2</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">WRITE</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">WEB3</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="65" font-size="12">OWN</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">DECENTRALIZED</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">COORDINATION</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">THE FUTURE OF WEB3</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Decentralized Networks to a New Digital Architecture.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Web3: The integrated framework for digital ownership, programmable value, and decentralized coordination as native components of the internet.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 140</title>
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
            <p class="section-label">PAGE 140</p>
            <h2>THE FUTURE OF WEB3</h2>
            <p>“From Decentralized Networks to a New Digital Architecture.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Web3 is often described as the next generation of the internet, but its future is broader than cryptocurrencies. At its core, Web3 represents an attempt to build digital systems in which users, organizations, and communities have greater control over assets, identity, and data. The emerging Web3 architecture seeks to make digital ownership, programmable value, and decentralized coordination native components of the internet, transitioning from the platform-centric model of Web2 to an owner-centric model.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Evolution: Read, Write, Own</h3>
                <p>The history of the internet is a progression of capability. <strong>Web1</strong> (Read) enabled access to static information. <strong>Web2</strong> (Read+Write) introduced interactive platforms and social networks, but often at the cost of centralized data control. <strong>Web3</strong> (Read+Write+Own) attempts to add programmable ownership and decentralized coordination. As of 2026, the global Web3 market is estimated at <strong>$12.61 billion</strong>, reflecting a shift toward independently verifiable ownership and transaction records that do not rely entirely on centralized intermediaries.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Identity, Privacy & Programmable Value</h3>
                <p>Web3 introduces new approaches to <strong>Digital Identity</strong> through decentralized identifiers (DIDs) and verifiable credentials. This allows users to carry credentials across services without creating separate identities at every platform. <strong>Zero-Knowledge Proofs (ZKPs)</strong> enable verification without unnecessary disclosure, bridging the gap between privacy and compliance. Combined with <strong>Smart Contracts</strong>, Web3 makes value programmable, allowing financial and organizational logic to be embedded directly into software for automated settlement and exchange.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pakistan's Web3 Integration</h3>
                <p>Pakistan is actively participating in the Web3 transition. In <strong>April 2026</strong>, the country ended a 7-year crypto banking ban, positioning itself as a top global adoption hub. The <strong>Pakistan Virtual Assets Regulatory Authority (PVARA)</strong> has released draft regulations to provide a legal framework for Web3 startups. These policy shifts, combined with the efforts of the <strong>SECP</strong> to build a robust blockchain ecosystem, are creating opportunities for young Pakistani technologists to build decentralized applications (dApps) that connect local communities with global digital markets.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists exploring the transition from platform-centric to decentralized digital architectures. His work illustrates the shift toward building applications that integrate decentralized identity, smart contracts, and user-controlled data. He serves as one example of the "Young Pakistani Builder" who advocates for Web3 systems that empower local communities in Orakzai and beyond, providing them with portable credentials and direct control over their digital assets through verifiable and inclusive digital infrastructure.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: The Future of Web3</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Future is Hybrid</h3>
                <p>Web3 does not require every component of an application to be decentralized. The future is increasingly seen as a <strong>Hybrid Architecture</strong>, combining the performance of centralized cloud infrastructure with the sovereignty of decentralized identity and blockchain settlement. The objective is not to make every object a token, but to make legitimate rights and transactions more verifiable, interoperable, and accessible. As we redesign how we represent value, the trust shifts from institutions to mathematics, protocols, and transparent governance.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Web3 is more than a technical stack; it is a coordination paradigm. To build a secure digital world, we must bridge the gap between technical control and social trust. The objective of Web3 is to create a decentralized internet where ownership is a native feature and coordination is transparent. From the urban centers of Pakistan to the valleys of Orakzai, we are building the foundation for a more equitable and sovereign digital future.”</p>
            </div>

            <div class="final-statement">
                THE INTERNET IS EVOLVING.<br>
                THE FUTURE IS DECENTRALIZED.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>The Business Research Company, <em>Web3 Market Forecast Analysis Report 2026–2030</em>.</li>
                    <li>Pakistan Virtual Assets Regulatory Authority (PVARA), <em>Draft Virtual Asset Services Regulations 2026</em>.</li>
                    <li>Precedence Research, <em>Global Decentralized Identity Market Size Report 2026</em>.</li>
                    <li>Fortune Business Insights, <em>Web 3.0 Market Size & Industry Share Forecast 2026–2034</em>.</li>
                    <li>SECP Pakistan, <em>Ecosystem Development for Blockchain and Digital Finance (2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            140
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

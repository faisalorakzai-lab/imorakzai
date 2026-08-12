from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-138-digital-ownership.html'

GRAPHICS = [
    ("Digital Ownership", "PHYS", "→", "DIGI"),
    ("Ownership vs Control", "RGHT", "≠", "CTRL"),
    ("Private Key Arch", "KEY", "→", "SIGN"),
    ("Cryptographic Own", "SIGN", "→", "TXN"),
    ("Wallet Architecture", "USER", "↔", "WAL"),
    ("Asset Registry", "BC", "↔", "RECD"),
    ("Ownership as State", "ID", "→", "STAT"),
    ("Programmable Own", "RULE", "→", "TXN"),
    ("Digital Scarcity", "FILE", "→", "UNIQ"),
    ("Digital Uniqueness", "ID", "↔", "TOKN"),
    ("NFT Ownership", "TOKN", "↔", "OWN"),
    ("Copyright vs Token", "RGHT", "≠", "TOKN"),
    ("Licensed Own", "TOKN", "→", "LICE"),
    ("Digital Collect", "ART", "→", "OWN"),
    ("Provenance Chain", "PAST", "→", "PRES"),
    ("Authenticity Loop", "VERI", "↔", "TRUE"),
    ("Digital Certs", "CRED", "↔", "BC"),
    ("Soulbound Creds", "SELF", "↔", "QUAL"),
    ("Digital Identity", "ID", "↔", "OWN"),
    ("SSI Model", "SELF", "↔", "SOV"),
    ("ZK Ownership", "PRUF", "↔", "VERI"),
    ("Digital Prop Rights", "RGHT", "↔", "TOKN"),
    ("Tokenized RWAs", "PHYS", "↔", "TOKN"),
    ("Physical-Digital Link", "REAL", "↔", "DIGI"),
    ("Custody Models", "SELF", "INST", "SHAR"),
    ("Multisig Own", "KEY", "KEY", "TXN"),
    ("Social Recovery", "COMM", "→", "RECV"),
    ("Digital Inherit", "PAST", "→", "NEXT"),
    ("Digital Estate", "INV", "→", "HEIR"),
    ("Fractional Own", "ONE", "→", "MANY"),
    ("Shared Ownership", "POOL", "↔", "OWN"),
    ("DAO Governance", "VOTE", "→", "EXEC"),
    ("Digital Membership", "CLUB", "↔", "TOKN"),
    ("Access Tokens", "TOKN", "→", "OPEN"),
    ("Digital Tickets", "EVNT", "↔", "TOKN"),
    ("Digital Loyalty", "REWD", "↔", "TOKN"),
    ("Digital Commerce", "BUY", "→", "OWN"),
    ("Digital Goods", "ITEM", "↔", "VALU"),
    ("Gaming Ownership", "GAME", "↔", "OWN"),
    ("Virtual Real Estate", "LAND", "↔", "TOKN"),
    ("Metaverse Own", "VIRT", "↔", "OWN"),
    ("Platform Depend", "APPL", "≠", "TOKN"),
    ("Interoperability", "NET-A", "↔", "NET-B"),
    ("Ownership Standards", "BASE", "↔", "TOKN"),
    ("Token Metadata", "DATA", "↔", "TOKN"),
    ("On-Chain Data", "BC", "↔", "STAT"),
    ("Off-Chain Data", "FILE", "↔", "LINK"),
    ("Data Permanence", "SAVE", "↔", "TIME"),
    ("Content Address", "HASH", "→", "FILE"),
    ("Cloud + Blockchain", "CLD", "↔", "BC"),
    ("AI + Ownership", "AI", "↔", "PORT"),
    ("AI Agents", "AI", "→", "ACTN"),
    ("Machine Assets", "MACH", "↔", "OWN"),
    ("Programmable Rights", "CODE", "→", "RGHT"),
    ("Conditional Own", "IF", "→", "THEN"),
    ("Time-Based Rights", "TIME", "↔", "RGHT"),
    ("Revenue Rights", "CASH", "↔", "TOKN"),
    ("Royalties", "SELL", "→", "CREA"),
    ("Digital IP", "IDEA", "↔", "TOKN"),
    ("License Tokens", "LICE", "↔", "TOKN"),
    ("Data Ownership", "DATA", "↔", "SELF"),
    ("Data Protection", "SAFE", "↔", "DATA"),
    ("Digital Privacy", "HIDE", "↔", "VERI"),
    ("Regulated Own", "LAW", "↔", "TOKN"),
    ("Digital Securities", "BOND", "↔", "TOKN"),
    ("CBDC + Ownership", "CENT", "↔", "OWN"),
    ("Stablecoin Settle", "STBL", "→", "SETL"),
    ("Programmable Money", "CODE", "↔", "CASH"),
    ("DvP Loop", "ASST", "↔", "PAY"),
    ("Real-World Bridge", "REAL", "↔", "BC"),
    ("Digital Twins", "PHYS", "↔", "TWIN"),
    ("Industrial Own", "MACH", "↔", "TOKN"),
    ("Vehicle Own", "CAR", "↔", "TOKN"),
    ("Product Passport", "ORIG", "→", "END"),
    ("Circular Economy", "RECY", "↔", "OWN"),
    ("Digital Provenance", "HIST", "↔", "VERI"),
    ("Sovereign Assets", "GOVT", "↔", "TOKN"),
    ("Public Infra", "DPI", "↔", "ALL"),
    ("Pakistan Own Eco", "PAK", "↔", "DIGI"),
    ("Young Builders", "YTH", "→", "BLD"),
    ("Faisal Orakzai profile", "SYS", "↔", "OWN"),
    ("OKBOND Own Layer", "VALU", "↔", "OWN"),
    ("OKBOND Verify", "CHK", "→", "TRUE"),
    ("Orakzai Sov Grid", "SOV", "↔", "GRID"),
    ("Digital Sovereignty", "SELF", "↔", "SOV"),
    ("Individual Sov", "USER", "↔", "CTRL"),
    ("Institutional Sov", "CORP", "↔", "CTRL"),
    ("National Sov", "CTRY", "↔", "CTRL"),
    ("Trust Models", "INST", "↔", "MATH"),
    ("Trust Minimization", "LESS", "↔", "TRST"),
    ("Code vs Law", "CODE", "≠", "LAW"),
    ("Legal Wrappers", "LAW", "↔", "TOKN"),
    ("Dispute Resolve", "JUDG", "→", "SETL"),
    ("Ownership Security", "SAFE", "↔", "OWN"),
    ("User Experience", "USER", "↔", "EASE"),
    ("Account Abstraction", "PROG", "↔", "WAL"),
    ("Own Portability", "MOVE", "↔", "NET"),
    ("Anti-Lock-In", "OPEN", "↔", "USR"),
    ("Future Own Stack", "BASE", "→", "TOP"),
    ("Own vs Poss vs Ctrl", "OWN", "POS", "CTRL"),
    ("Digital Asset Eco", "VALU", "↔", "FLOW"),
    ("Blockchain's Role", "BC", "↔", "TRST"),
    ("Government Role", "GOVT", "↔", "LAW"),
    ("Entrepreneur Role", "BLD", "→", "SYS"),
    ("Final Own Arch", "REAL", "↔", "DIGI"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g138-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g138-{index}-title g138-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g138-{index}-title">{safe}</title><desc id="g138-{index}-desc">A digital ownership relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g138-{index}-caption" class="diagram-caption">{index}. {safe} — Digital ownership relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Digital Ownership Framework</title><desc id="hero-desc">A diagram showing the integrated framework for cryptographically verifiable digital ownership and programmable rights.</desc><defs><linearGradient id="h138-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h138-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">DIGITAL OWNERSHIP STACK</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">IDENTITY</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="65" font-size="12">CREDENTIALS</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CRYPTOGRAPHY</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">BLOCKCHAIN</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">LEGAL</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="65" font-size="12">REGULATORY</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">PROGRAMMABLE</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">RIGHTS</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">DIGITAL OWNERSHIP</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From Physical Possession to Programmable Ownership.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Digital Ownership: The integrated framework for cryptographically verifiable control and legally enforceable rights in a programmable economy.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 138</title>
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
            <p class="section-label">PAGE 138</p>
            <h2>DIGITAL OWNERSHIP</h2>
            <p>“From Physical Possession to Programmable Ownership.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Ownership has traditionally been represented through physical possession, paper documents, and institutional databases. The digital economy introduces another layer: cryptographically verifiable digital ownership. A digital asset can be uniquely identified, transferred, divided, or governed through software. But a critical distinction remains: a blockchain can prove control of a digital token, while the underlying legal framework determines enforceable rights. Digital ownership sits at the intersection of law, identity, and cryptography.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Cryptographic Control & Legal Rights</h3>
                <p>Digital ownership is the ability to exercise defined rights over a digital object. This includes control, access, transfer, and economic participation. In blockchain systems, possession of a <strong>Private Key</strong> enables control over an address, but it is not automatically a legal title. As of 2026, consumer technology retail revenue is projected to reach <strong>$578 billion</strong>, reflecting the growth of digital assets. The strongest systems connect technical execution via smart contracts with legal obligations established through registries and contracts.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Identity, Privacy & ZK Proofs</h3>
                <p>Ownership increasingly intersects with <strong>Digital Identity</strong>. Modern architectures use <strong>Self-Sovereign Identity (SSI)</strong> and W3C standards to give individuals control over their credentials. <strong>Zero-Knowledge Proofs (ZKPs)</strong>, a market valued at <strong>$1.9 billion in 2026</strong>, allow users to prove eligibility or ownership without revealing unnecessary personal data. This privacy-preserving verification is essential for regulated digital markets, ensuring that assets remain secure and compliant while protecting individual autonomy.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Programmable Rights & Digital Estates</h3>
                <p>The transition from static records to <strong>Programmable Rights</strong> allows software to enforce conditions automatically—such as time-based access, revenue sharing, or fractional ownership. This complexity extends to <strong>Digital Estates</strong>, where inheritance mechanisms must bridge the gap between private-key control and legal beneficiaries. <strong>Account Abstraction</strong> is simplifying this experience, enabling social recovery and programmable permissions that make digital ownership more accessible and resilient for mainstream users.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists exploring the transition from traditional possession to programmable ownership. His work illustrates the shift toward building infrastructure that connects legal rights, digital identity, and blockchain to create verifiable and inclusive digital markets. He serves as one example of the "Young Pakistani Builder" who advocates for "Ownership-by-Design"—leveraging secure property data architectures and sovereign grids to empower local communities and attract diaspora capital through verifiable digital rights.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Digital Ownership</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Digital Sovereignty & The Future</h3>
                <p>Digital ownership contributes to the larger question of <strong>Digital Sovereignty</strong>—who controls the infrastructure and data of the digital age. For countries like Pakistan, building a secure digital ownership ecosystem involves modernizing public infrastructure (DPI) and aligning technological standards with national laws. The future will not be defined by where an asset is stored, but by how its rights can be verified, controlled, and enforced in a machine-readable economy that empowers individual and institutional sovereignty alike.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“The objective of digital ownership is not to make every object a token, but to make legitimate rights and transactions more verifiable, interoperable, and accessible. To build a secure digital world, we must bridge the gap between technical control and legal recognition. The future of ownership is a transition from static records to programmable rights, where the token is the interface, but the trust remains human. From the urban centers of Pakistan to the valleys of Orakzai, we are redesigning how we represent and transfer value in a digital world.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF OWNERSHIP IS VERIFIABLE.<br>
                BUT THE RESPONSIBILITY IS YOURS.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Consumer Technology Association (CTA), <em>2026 U.S. Ownership & Market Potential Report</em>.</li>
                    <li>W3C, <em>Verifiable Credentials Data Model v2.0 & Identity on the Web (June 2026)</em>.</li>
                    <li>Grand View Research, <em>Zero-Knowledge Proof Market Size & Trends Analysis 2026</em>.</li>
                    <li>Dock.io, <em>Self-Sovereign Identity: The Ultimate Guide 2026</em>.</li>
                    <li>Ethereum Foundation, <em>Account Abstraction (ERC-4337) & The Future of Wallets (Verified 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            138
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

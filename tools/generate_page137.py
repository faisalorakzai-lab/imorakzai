from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-137-real-estate-tokenization.html'

GRAPHICS = [
    ("RE Tokenization", "PROP", "↔", "TOKN"),
    ("Basic Model", "STRC", "→", "RGHT"),
    ("Property Interests", "OWN", "DEBT", "RENT"),
    ("Why Real Estate?", "VALU", "↔", "LIQD"),
    ("Direct Ownership", "TOKN", "↔", "LAND"),
    ("Indirect Ownership", "TOKN", "→", "SPV"),
    ("SPV Structure", "INV", "→", "ASST"),
    ("Legal Foundation", "LAW", "↔", "CODE"),
    ("Property Title", "RECD", "≠", "TITL"),
    ("Registry Link", "GOVT", "↔", "BC"),
    ("Property Verify", "CHK", "→", "TRST"),
    ("Trust Stack", "LAW", "VAL", "TECH"),
    ("Fractionalization", "$10M", "→", "$10"),
    ("Fractional Own", "ONE", "→", "MANY"),
    ("Rental Income", "RENT", "→", "DIST"),
    ("Smart Dist", "CODE", "→", "PAY"),
    ("Operating Exp", "RENT", "−", "COST"),
    ("Net Income", "GROS", "→", "DIST"),
    ("Property Val", "MKT", "↔", "APPR"),
    ("NAV Formula", "ASST", "−", "DEBT"),
    ("Price vs Value", "MKT", "≠", "PROP"),
    ("Liquidity Gap", "FRAC", "≠", "BUY"),
    ("Secondary Market", "TRAD", "↔", "TOKN"),
    ("24/7 Trading", "OPEN", "↔", "TIME"),
    ("Settlement Loop", "DLIV", "+", "PAY"),
    ("DvP Concept", "TOKN", "↔", "CASH"),
    ("Global Invest", "GLB", "↔", "NET"),
    ("KYC/AML Bridge", "ID", "↔", "WAL"),
    ("Whitelisted Wal", "AUTH", "→", "TXN"),
    ("PropTech Pakistan", "PAK", "↔", "BC"),
    ("PIDE Research", "SIM", "→", "EFFI"),
    ("Digital Land Rec", "GOVT", "↔", "DIGI"),
    ("Diaspora Capital", "SEND", "→", "PROP"),
    ("Faisal Orakzai RE", "SYS", "↔", "LAND"),
    ("OKBOND RE", "VALU", "↔", "CONT"),
    ("Orakzai Sovereign Grid", "SOV", "↔", "GRID"),
    ("Digital Sovereignty", "SELF", "↔", "SOV"),
    ("Registry Future", "PAST", "→", "DIGI"),
    ("Ownership Evolution", "PAPER", "→", "CODE"),
    ("Asset Interop", "PROP", "↔", "DEFI"),
    ("Collateralized RE", "PROP", "→", "LOAN"),
    ("Economic Rights", "RGHT", "↔", "DATA"),
    ("Transparency", "VIEW", "↔", "LEDG"),
    ("Audit Lifecycle", "CHK", "→", "SAFE"),
    ("Oracle Feed", "REAL", "→", "VAL"),
    ("Market Efficiency", "FAST", "↔", "BC"),
    ("Investor Access", "ALL", "↔", "FIN"),
    ("Minimum Unit", "LESS", "↔", "ACC"),
    ("Compliance Rules", "CODE", "↔", "LAW"),
    ("Identity Layer", "ID", "↔", "TOKN"),
    ("Verification Loop", "CHK", "→", "TRUE"),
    ("Property Lifecycle", "BLD", "HOLD", "SELL"),
    ("Token Lifecycle", "MINT", "TRAD", "BURN"),
    ("Redemption Model", "TOKN", "→", "ASST"),
    ("Insolvency Prot", "SAFE", "↔", "FAIL"),
    ("Custody Security", "VAUL", "↔", "KEY"),
    ("API Integration", "DATA", "↔", "BC"),
    ("Real-Time Report", "LIVE", "↔", "ANLY"),
    ("Risk Monitoring", "RISK", "→", "ACTN"),
    ("Emergency Pausing", "STOP", "→", "SAFE"),
    ("Governance Voted", "VOTE", "→", "MOD"),
    ("Parameter Adjust", "RATE", "↔", "GOVN"),
    ("Yield Calculation", "RENT", "÷", "VAL"),
    ("Appreciation", "UP", "↔", "VAL"),
    ("Sale Proceeds", "SELL", "→", "DIST"),
    ("Maintenance Fund", "RESR", "↔", "COST"),
    ("Insurance Token", "SAFE", "↔", "PROP"),
    ("Tax Automation", "TAX", "→", "GOVT"),
    ("Utility Rights", "USE", "↔", "TOKN"),
    ("Access Control", "KEY", "→", "DOOR"),
    ("IoT Integration", "SENS", "→", "DATA"),
    ("Smart Building", "DATA", "→", "EFFI"),
    ("Energy Token", "SOLR", "→", "TOKN"),
    ("Sustainable RE", "GRN", "↔", "VALU"),
    ("Carbon Offset", "CO2", "→", "CRED"),
    ("Regional Growth", "LOCL", "→", "GLB"),
    ("Community Fund", "COMM", "↔", "PROP"),
    ("Jirga to Smart", "TRAD", "→", "TECH"),
    ("Orakzai Heritage", "PAST", "→", "FUTR"),
    ("Digital Identity", "SELF", "↔", "ID"),
    ("Privacy Preserve", "HIDE", "↔", "VERI"),
    ("ZK Proof RE", "PRUF", "↔", "TRUE"),
    ("Institutional RE", "CORP", "→", "TOKN"),
    ("Bank RE Bridge", "BANK", "↔", "BC"),
    ("Mortgage Token", "DEBT", "→", "TOKN"),
    ("Credit Score RE", "PAST", "→", "CRDT"),
    ("Underwriting AI", "INTE", "→", "LOAN"),
    ("Fraud Detection", "SCAN", "→", "SAFE"),
    ("Legal Finality", "COURT", "↔", "BC"),
    ("Dispute Resolve", "RULE", "→", "SETL"),
    ("Registry Sync", "MANY", "→", "ONE"),
    ("Shared Ledger", "BC", "↔", "ALL"),
    ("Cost Reduction", "LESS", "↔", "FEES"),
    ("Administrative", "AUTO", "↔", "MANU"),
    ("Speed of Trade", "FAST", "↔", "SETL"),
    ("Global Liquidity", "GLB", "↔", "POOL"),
    ("Capital Flow", "SEND", "→", "RECV"),
    ("Market Access", "OPEN", "↔", "ACC"),
    ("Inclusive Finance", "ALL", "↔", "VALU"),
    ("Digital Divide", "TECH", "≠", "ACC"),
    ("Education Gap", "EDU", "→", "ACC"),
    ("Consumer Prot", "LAW", "↔", "USR"),
    ("Secure Wallet", "KEY", "↔", "OWN"),
    ("Private Key RE", "HIDE", "→", "TITL"),
    ("Account Abstr", "PROG", "↔", "WAL"),
    ("Social Recovery", "MANY", "→", "ONE"),
    ("Smart Wallet RE", "RECV", "↔", "LIMT"),
    ("Future Ownership", "PROG", "↔", "OWN"),
    ("Programmable Cap", "CODE", "→", "FLOW"),
    ("RWA Smart Cont", "RULE", "↔", "CODE"),
    ("RWA Cloud RE", "DATA", "↔", "CLD"),
    ("RWA AI Arch", "AI", "↔", "ASST"),
    ("RWA Cyber RE", "SAFE", "↔", "DATA"),
    ("Final RE Arch", "GLB", "↔", "SOV"),
    ("Historical Evol", "PAST", "→", "FUTR"),
    ("Final Conceptual", "REAL", "↔", "DIGI"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g137-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g137-{index}-title g137-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g137-{index}-title">{safe}</title><desc id="g137-{index}-desc">A real estate relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g137-{index}-caption" class="diagram-caption">{index}. {safe} — Real estate relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Real Estate Tokenization Framework</title><desc id="hero-desc">A diagram showing the integrated framework for connecting physical property and legal titles with programmable digital ownership.</desc><defs><linearGradient id="h137-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h137-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">PROPERTY TOKENIZATION STACK</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">REGISTRY</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="65" font-size="12">TITLES</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">FRACTIONAL</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">OWNERSHIP</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">RENTAL</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="65" font-size="12">INCOME</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">PROGRAMMABLE</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">PROPERTY</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">REAL ESTATE TOKENIZATION</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Turning Property Rights Into Programmable Digital Infrastructure.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Real Estate Tokenization: The integrated framework for connecting physical land value and legal titles with decentralized digital ownership.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 137</title>
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
            <p class="section-label">PAGE 137</p>
            <h2>REAL ESTATE TOKENIZATION</h2>
            <p>“Turning Property Rights Into Programmable Digital Infrastructure.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Real estate is one of the world's largest asset classes, yet ownership, financing, and property records are often managed through fragmented systems. Real estate tokenization explores how blockchain technology can represent defined legal or economic interests in property through digital tokens. This connects physical assets with programmable digital infrastructure, enabling fractional ownership, faster settlement, and improved transparency across the property market.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Property Trust Stack</h3>
                <p>A serious real estate tokenization system requires an integrated stack covering the <strong>Legal Foundation</strong> (SPVs and ownership structures), <strong>Property Verification</strong> (title, location, and valuation), and the <strong>Token Layer</strong> (smart contracts defining rights). As of 2026, the global real estate tokenization market is valued at approximately <strong>$4.81 billion</strong>, with projections reaching over <strong>$24 billion by 2035</strong>. This transition is described by industry leaders as a shift from paper-based registries to shared digital networks that provide legal finality and cryptographic proof.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Fractional Ownership & Rental Income</h3>
                <p>One of the most significant benefits of tokenization is <strong>Fractionalization</strong>, which allows a single property to be divided into thousands of digital units. This reduces minimum investment sizes, enabling multiple investors to participate in a single economic asset. Smart contracts can automate the distribution of <strong>Rental Income</strong>, calculating investor shares based on eligible tokens and distributing distributable cash flow once expenses are deducted. This turns property into a programmable financial instrument with transparent accounting and real-time reporting.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">PropTech Pakistan & Digital Land Records</h3>
                <p>Pakistan's real estate market is undergoing a digital transformation, with the <strong>PropTech Convention 2026</strong> advocating for blockchain-enabled land records and e-governance. Research from the <strong>Pakistan Institute of Development Economics (PIDE)</strong> highlights the potential for blockchain to improve market efficiency and inclusion, particularly in urban centers like Islamabad. Platforms like <strong>DAO PropTech</strong> are already simplifying property investment through secure digital ownership units, bridging the gap between traditional land titles and modern digital registries.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists approaching real estate not just as land, but as a system where legal rights, physical assets, and digital infrastructure intersect. His documented interest in digital-asset infrastructure illustrates the shift toward building secure, transparent property data architectures. He serves as one example of the "Young Pakistani Builder" who advocates for systems that can bring transparency to regional land records in districts like Orakzai, empowering local communities and attracting diaspora capital through verifiable digital rights.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Real Estate Tokenization</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Liquidity, Oracles & The Future</h3>
                <p>While tokenization makes transfers technically easier, <strong>Automatic Liquidity</strong> is not guaranteed; it requires an active secondary market and legal transferability. <strong>Oracles</strong> provide a critical bridge between real-world property values and blockchain state, though they introduce dependencies on professional appraisals and market data. Looking forward, the integration of <strong>Digital Identity</strong> and whitelisted wallets will allow for programmable compliance, ensuring that property markets remain secure, regulated, and globally accessible while preserving digital sovereignty.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Tokenization is not a magic solution, but a fundamental reconfiguration of how we represent value. For Pakistan, the opportunity is to leverage this technology to create transparent, inclusive property markets that empower every citizen. A secure future for real estate requires bridging the gap between what the blockchain says and what the real world recognizes. The token is the interface, but the trust remains human. From the urban centers of Islamabad to the valleys of Orakzai, the future of ownership is digital, programmable, and shared.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF PROPERTY IS PROGRAMMABLE.<br>
                BUT THE LAND REMAINS REAL.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Precedence Research, <em>Global Tokenization Market Size, Share, and Forecast 2026–2035</em>.</li>
                    <li>Pakistan Institute of Development Economics (PIDE), <em>Transforming Real Estate in Pakistan through Blockchain (2025/2026 Research)</em>.</li>
                    <li>PropTech Convention Pakistan, <em>The Future of Real Estate: Blockchain and Digital Land Records (May 2026)</em>.</li>
                    <li>Custom Market Insights, <em>Global Real Estate Tokenization Market Analysis and Forecast (July 2026)</em>.</li>
                    <li>DAO PropTech, <em>Fractional Ownership Units & Digital Investment Platforms (Verified 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            137
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

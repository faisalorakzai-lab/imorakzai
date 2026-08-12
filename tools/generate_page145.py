from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-145-digital-identity.html'

GRAPHICS = [
    ("Digital Identity", "PERS", "↔", "ID"),
    ("Identity Credentials", "DOC", "→", "ID"),
    ("Authentication", "USER", "↔", "SAFE"),
    ("Biometrics", "BODY", "→", "VERI"),
    ("Cryptographic Keys", "KEY", "↔", "SAFE"),
    ("Verifiable Credentials", "CERT", "↔", "VERI"),
    ("Digital Certificates", "SIG", "↔", "CERT"),
    ("Identity Providers", "IDP", "→", "USER"),
    ("Trust Frameworks", "RULE", "↔", "TRST"),
    ("Identity Claim", "USER", "→", "CLAIM"),
    ("Identity Proofing", "CHK", "↔", "REAL"),
    ("Enrollment", "IN", "→", "SYS"),
    ("Verification", "CHK", "↔", "DATA"),
    ("Credential Issuance", "ISS", "→", "USER"),
    ("Authentication Flow", "TRY", "→", "OK"),
    ("Authorization", "ALLOW", "↔", "USER"),
    ("Renewal / Revocation", "NEW", "≠", "OLD"),
    ("Identification", "WHO", "↔", "ME"),
    ("Multi-Factor Auth", "MANY", "→", "SAFE"),
    ("Something You Know", "BRAIN", "→", "SAFE"),
    ("Something You Have", "KEY", "→", "SAFE"),
    ("Something You Are", "FACE", "→", "SAFE"),
    ("Password Weakness", "PASS", "≠", "SAFE"),
    ("Passkeys", "CRYP", "↔", "SAFE"),
    ("Public-Key Crypt", "PUB", "↔", "PRIV"),
    ("Digital Signature", "SIGN", "↔", "ACT"),
    ("Private Key Control", "OWN", "↔", "KEY"),
    ("Public Key Verify", "OPEN", "↔", "CHK"),
    ("Certificate Authority", "CA", "→", "TRST"),
    ("Single Sign-On", "ONE", "→", "ALL"),
    ("Federated Identity", "MANY", "↔", "TRST"),
    ("Identity Ecosystem", "ALL", "↔", "NET"),
    ("National Digital ID", "NATL", "↔", "ID"),
    ("NADRA Infrastructure", "PAK", "↔", "ID"),
    ("Pak ID App", "MOB", "↔", "ID"),
    ("Nishan Pakistan", "GATE", "↔", "VERI"),
    ("Digital Nation Act", "LAW", "↔", "2025"),
    ("QR-Based Verify", "QR", "↔", "FAST"),
    ("Facial Recognition", "FACE", "↔", "BIO"),
    ("IRIS Scanning", "EYE", "↔", "BIO"),
    ("Biometric Control", "LOCK", "↔", "USER"),
    ("Public Service ID", "GOVT", "↔", "USER"),
    ("Digital Government", "GOV", "↔", "NET"),
    ("Payment Identity", "PAY", "↔", "ID"),
    ("KYC Process", "CHK", "↔", "BANK"),
    ("Fintech Identity", "TECH", "↔", "ID"),
    ("Remittance Identity", "GLOB", "↔", "ID"),
    ("Healthcare ID", "MED", "↔", "ID"),
    ("Educational ID", "GRAD", "↔", "ID"),
    ("Professional Cred", "WORK", "↔", "ID"),
    ("Digital License", "DRIV", "↔", "ID"),
    ("Digital Passport", "TRVL", "↔", "ID"),
    ("Digital Visa", "VISA", "↔", "ID"),
    ("Organizational ID", "CORP", "↔", "ID"),
    ("Device Identity", "IOT", "↔", "ID"),
    ("Self-Sovereign ID", "OWN", "↔", "ID"),
    ("Decentralized ID", "DID", "↔", "BC"),
    ("Privacy by Design", "SAFE", "↔", "PRIV"),
    ("Zero-Knowledge", "HIDE", "↔", "PROV"),
    ("Identity Wallet", "WAL", "↔", "CRED"),
    ("Trust Anchor", "BASE", "↔", "TRST"),
    ("Identity Registry", "LIST", "↔", "SYS"),
    ("Identity Lifecycle", "LIFE", "↔", "ID"),
    ("Authentication Level", "LOA", "↔", "SAFE"),
    ("Identity Attribute", "ATTR", "↔", "ID"),
    ("Identity Linkage", "LINK", "↔", "MANY"),
    ("Identity Federation", "FED", "↔", "NET"),
    ("Identity Standards", "STD", "↔", "RULE"),
    ("Interoperability", "SYNC", "↔", "MANY"),
    ("Data Minimization", "LESS", "↔", "SAFE"),
    ("User Consent", "YES", "↔", "DATA"),
    ("Identity Security", "SAFE", "↔", "NET"),
    ("Phishing Risk", "FISH", "≠", "SAFE"),
    ("Credential Theft", "STEAL", "≠", "OWN"),
    ("Identity Recovery", "BACK", "↔", "ID"),
    ("Digital Persona", "SOC", "↔", "ID"),
    ("Legal Identity", "LAW", "↔", "ID"),
    ("Foundational ID", "BASE", "↔", "NATL"),
    ("Functional ID", "FUNC", "↔", "SERV"),
    ("Identity Inclusion", "ALL", "↔", "ID"),
    ("Identity for Orakzai", "ORAK", "↔", "ID"),
    ("Tribal Identity", "TRIBE", "↔", "ID"),
    ("Digital Citizenship", "CITI", "↔", "NET"),
    ("Identity Governance", "GOV", "↔", "RULE"),
    ("Identity Policy", "RULE", "↔", "ID"),
    ("Identity Auditing", "AUDT", "↔", "SYS"),
    ("Identity Analytics", "DATA", "↔", "ID"),
    ("Identity Threats", "WAR", "≠", "SAFE"),
    ("Identity Resilience", "STAY", "↔", "SAFE"),
    ("Future of Identity", "TIME", "↔", "NEW"),
    ("Digital ID Wallet", "APP", "↔", "ID"),
    ("Smart Identity", "AI", "↔", "ID"),
    ("Identity at Edge", "EDGE", "↔", "ID"),
    ("Identity Persistence", "STAY", "↔", "ID"),
    ("Identity Portability", "MOVE", "↔", "ID"),
    ("Identity Privacy", "PRIV", "↔", "ID"),
    ("Identity Trust", "TRST", "↔", "ID"),
    ("Identity Value", "VALU", "↔", "ID"),
    ("Identity Power", "POWR", "↔", "ID"),
    ("Identity Rights", "RITE", "↔", "ID"),
    ("Identity Duty", "DUTY", "↔", "ID"),
    ("Identity Harmony", "PEAC", "↔", "ID"),
    ("Identity Growth", "GROW", "↔", "ID"),
    ("Identity Future", "NEXT", "↔", "ID"),
    ("Identity Vision", "EYE", "↔", "ID"),
    ("Identity Mission", "GOAL", "↔", "ID"),
    ("Identity Strategy", "PLAN", "↔", "ID"),
    ("Identity Action", "DO", "↔", "ID"),
    ("Identity Result", "DONE", "↔", "ID"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g145-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g145-{index}-title g145-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g145-{index}-title">{safe}</title><desc id="g145-{index}-desc">A digital identity relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g145-{index}-caption" class="diagram-caption">{index}. {safe} — Digital identity relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Digital Identity Framework</title><desc id="hero-desc">A diagram showing the integrated stack of digital identity, from enrollment to service delivery.</desc><defs><linearGradient id="h145-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h145-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">DIGITAL IDENTITY ECOSYSTEM</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">ENROLLMENT & PROOFING</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">CREDENTIAL ISSUANCE (NADRA / Pak ID)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AUTHENTICATION (Biometrics / Passkeys)</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">AUTHORIZATION & TRUST FRAMEWORKS</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">SERVICE DELIVERY (DPI / Raast / Govt)</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">PRIVACY & BIOMETRIC CONTROL</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">SELF-SOVEREIGN IDENTITY (SSI)</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">DIGITAL IDENTITY</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Identity is the Foundation of the Digital Nation.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Digital Identity Framework: The integrated ecosystem for enrollment, verification, and secure access to digital services.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 145</title>
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
            <p class="section-label">PAGE 145</p>
            <h2>DIGITAL IDENTITY</h2>
            <p>“Identity is the Foundation of the Digital Nation.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Identity has always been fundamental to society. In the digital age, identity is no longer just a physical document; it is the collection of information, credentials, and mechanisms used to represent and authenticate an entity online. The objective is to create secure, interoperable, and privacy-conscious ways for people to prove who they are and what they are authorized to do, ensuring that every citizen—from the urban centers to the Orakzai valleys—has a voice in the digital nation.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Digital Identity Landscape in 2026</h3>
                <p>As of 2026, Pakistan has solidified its position as a leader in digital identity through the **Digital Nation Act (2025)** and the continued evolution of the **National Database and Registration Authority (NADRA)**. The **Pak ID App** has surpassed 18 million downloads, serving as the primary interface for digital citizenship. The rollout of the **Nishan Pakistan** platform in February 2026 has standardized identity verification across the financial, telecommunications, and government sectors, creating a unified trust framework for the entire country.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Biometrics & The Shift to Facial Recognition</h3>
                <p>A significant milestone in early 2026 was the transition to **Facial Recognition** and **IRIS scanning** as primary biometric markers. This shift, formalized in January 2026, has improved accessibility for senior citizens and individuals with medical conditions who previously struggled with fingerprint verification. Furthermore, the introduction of the **Biometric Control system** in June 2026 allows citizens to lock and unlock their biometric records via the Pak ID app, providing unprecedented control over their personal data.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Self-Sovereign Identity (SSI) & Privacy</h3>
                <p>The 2026 roadmap emphasizes **Self-Sovereign Identity (SSI)** principles, where users manage their own credentials via decentralized identifiers (DIDs) and verifiable credentials (VCs). By leveraging **Zero-Knowledge proofs**, citizens can verify their attributes (such as age or residency) without revealing sensitive underlying data. This "Privacy by Design" approach is essential for building trust in the national digital public infrastructure (DPI), ensuring that identity is a tool for empowerment rather than surveillance.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Identity in the Orakzai Context</h3>
                <p>For the Orakzai community, digital identity is a bridge to inclusion. It enables secure access to direct benefit transfers, healthcare, and educational services, even in remote valleys. By anchoring tribal identity to the national digital framework, we ensure that regional rights and ownership records are protected by the same cryptographic security that safeguards the nation's capital. Digital identity is not just a card; it is the key to our shared future.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Digital Identity</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“To be identified is to be recognized. To be authenticated is to be trusted. In the digital nation, our identity is our sovereign asset. From the QR-based verification on our NICs to the cryptographic keys in our digital wallets, we are building a foundation where every Pakistani is recognized, every transaction is secure, and every individual is empowered to participate in the global digital economy.”</p>
            </div>

            <div class="final-statement">
                IDENTITY IS SOVEREIGN.<br>
                THE NATION IS DIGITAL.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Biometric Update, <em>Pak ID surpasses 18M downloads as Pakistan's digital ID adoption grows (July 2026)</em>.</li>
                    <li>ID Tech Wire / NADRA, <em>Pakistan's NADRA Formally Rolls Out Nishan Pakistan for Unified Identity Verification (Feb 2026)</em>.</li>
                    <li>Government of Pakistan, <em>The Digital Nation Pakistan Act (2025) — Legal Framework for Digital Transformation</em>.</li>
                    <li>NADRA Media Release, <em>Upgrades to NIC and POC Rules: Introducing QR-based Verification (Feb 2026)</em>.</li>
                    <li>Profit PK / Dawn News, <em>NADRA introducing facial recognition-based biometric system (Jan 2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            145
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

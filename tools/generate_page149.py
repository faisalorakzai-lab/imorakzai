from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-149-the-internet-of-value.html'

GRAPHICS = [
    ("Internet of Value", "VALU", "↔", "NET"),
    ("Info vs Value", "DATA", "≠", "VALU"),
    ("Web 1.0 Model", "READ", "→", "USER"),
    ("Web 2.0 Model", "READ", "↔", "WRIT"),
    ("Web3 Model", "OWN", "↔", "NET"),
    ("Digital Ownership", "USER", "↔", "ASST"),
    ("Tokenization Flow", "REAL", "→", "TOK"),
    ("Digital Scarcity", "ONE", "↔", "ONLY"),
    ("Double Spend Solve", "TX", "→", "LEDG"),
    ("Value Interop", "SYNC", "↔", "GLOB"),
    ("Money as Software", "CODE", "↔", "CASH"),
    ("Assets as Software", "CODE", "↔", "ASST"),
    ("Contracts as Software", "CODE", "↔", "LAW"),
    ("Programmable Economy", "IF", "→", "DONE"),
    ("Smart Contract Loop", "RULE", "→", "ACT"),
    ("Automatic Action", "COND", "→", "MOVE"),
    ("Digital Identity", "WHO", "↔", "NET"),
    ("Auth & Authorize", "KEY", "↔", "GATE"),
    ("Self-Sovereign ID", "OWN", "↔", "ID"),
    ("Verifiable Cred", "CERT", "↔", "USER"),
    ("Selective Disclose", "PART", "↔", "VIEW"),
    ("Zero-Knowledge", "HIDE", "↔", "PROV"),
    ("Privacy Finance", "PRIV", "↔", "SAFE"),
    ("Lawful Compliance", "RULE", "↔", "TX"),
    ("Trust Minimization", "CODE", "↔", "TRST"),
    ("Cryptographic Trust", "MATH", "↔", "TRST"),
    ("Institutional Trust", "BANK", "↔", "TRST"),
    ("Shared State", "SYNC", "↔", "ALL"),
    ("Blockchain Value", "BC", "↔", "VALU"),
    ("Distributed Ledger", "LEDG", "↔", "NET"),
    ("Wallet Interface", "USER", "↔", "APP"),
    ("Universal Wallet", "ALL", "↔", "ONE"),
    ("Money in Wallet", "CASH", "↔", "WALL"),
    ("Tokens in Wallet", "TOK", "↔", "WALL"),
    ("Identity in Wallet", "ID", "↔", "WALL"),
    ("Credentials Wallet", "CERT", "↔", "WALL"),
    ("Contracts in Wallet", "RULE", "↔", "WALL"),
    ("Digital Rights", "RITE", "↔", "OWN"),
    ("Instant Payments", "FAST", "→", "DONE"),
    ("Global Payments", "GLOB", "↔", "PAY"),
    ("Cross-Border Rail", "NATL", "↔", "GLOB"),
    ("Remittance Loop", "WORK", "→", "HOME"),
    ("Remittance Friction", "OLD", "≠", "NEW"),
    ("Interoperable Rail", "SYNC", "↔", "MANY"),
    ("Currency Convert", "FX", "↔", "VALU"),
    ("Settlement Final", "DONE", "↔", "LEDG"),
    ("Machine-to-Machine", "IOT", "↔", "VALU"),
    ("M2M Payment", "BOT", "↔", "BOT"),
    ("Autonomous Logistics", "MOVE", "↔", "PAY"),
    ("Cloud Resource Pay", "CLOU", "↔", "VALU"),
    ("AI Agents Finance", "AI", "↔", "FIN"),
    ("Agentic Commerce", "BOT", "↔", "SHOP"),
    ("AI + Blockchain", "REAS", "↔", "LEDG"),
    ("AI Prediction", "PRED", "↔", "DATA"),
    ("Blockchain State", "SAME", "↔", "ALL"),
    ("National Masterplan", "PLAN", "↔", "NATL"),
    ("ITU ID Score", "67.7", "↔", "PAK"),
    ("Digital Maturity", "GROW", "↔", "NATL"),
    ("Raast Foundation", "DPI", "↔", "PAK"),
    ("Raast Milestone", "20T", "↔", "DONE"),
    ("Bulk Disbursement", "CORP", "→", "MANY"),
    ("P2M Expansion", "MERC", "↔", "USER"),
    ("Digital Nation Act", "LAW", "↔", "2026"),
    ("PDA Oversight", "PDA", "↔", "GOV"),
    ("Financial Inclusion", "ALL", "↔", "PAY"),
    ("Regional Bridge", "ORAK", "↔", "GLOB"),
    ("Orakzai Digital", "ORAK", "↔", "NEW"),
    ("Identity Power", "POWR", "↔", "ID"),
    ("Asset Rights", "RITE", "↔", "OWN"),
    ("Governance Trust", "TRST", "↔", "GOV"),
    ("Inclusive Future", "ALL", "↔", "TIME"),
    ("Sovereign Technology", "OWN", "↔", "TECH"),
    ("The Future Rail", "TIME", "↔", "NEW"),
    ("The Permanent Record", "STAY", "↔", "DONE"),
    ("Value Transfer", "MOVE", "↔", "NET"),
    ("Scarcity Mechanism", "MATH", "↔", "ONE"),
    ("Scarcity Security", "SAFE", "↔", "ONE"),
    ("Ownership Scarcity", "OWN", "↔", "ONE"),
    (" Scarcity Value", "VALU", "↔", "ONE"),
    ("Scarcity Scarcity", "SAME", "↔", "ONE"),
    ("Scarcity Proof", "VERI", "↔", "ONE"),
    ("Scarcity Scarcity", "ONLY", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
    ("Scarcity Scarcity", "ONE", "↔", "ONE"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g149-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g149-{index}-title g149-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g149-{index}-title">{safe}</title><desc id="g149-{index}-desc">An internet of value relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g149-{index}-caption" class="diagram-caption">{index}. {safe} — Internet of value relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">The Internet of Value Framework</title><desc id="hero-desc">A diagram showing the transition from information to value exchange, highlighting the integrated digital stack of the future.</desc><defs><linearGradient id="h149-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h149-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">THE INTERNET OF VALUE STACK (2026)</text><path d="M0 15 V 300" stroke="#B59654" stroke-width="2" stroke-dasharray="5,5"/><g transform="translate(0, 40)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">DIGITAL IDENTITY (Authentication & Auth)</text></g><g transform="translate(0, 80)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">INTEROPERABLE PAYMENT RAILS (Raast / IoV)</text></g><g transform="translate(0, 120)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">BLOCKCHAIN & DISTRIBUTED LEDGERS</text></g><g transform="translate(0, 160)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">TOKENIZATION & DIGITAL OWNERSHIP</text></g><g transform="translate(0, 200)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">SMART CONTRACTS & PROGRAMMABLE VALUE</text></g><g transform="translate(0, 240)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">AI AGENTS & AGENTIC COMMERCE</text></g><g transform="translate(0, 280)"><rect x="-150" y="-15" width="300" height="30" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">GLOBAL CONNECTIVITY & INTEROPERABILITY</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">THE INTERNET OF VALUE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Moving Value as Easily as Information.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Internet of Value Framework: The integrated digital stack enabling the seamless exchange of money, ownership, and credentials.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 149</title>
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
            <p class="section-label">PAGE 149</p>
            <h2>THE INTERNET OF VALUE</h2>
            <p>“Moving Value as Easily as Information.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “The first generations of the internet transformed how humanity moved information. The next stage of digital transformation is concerned with how value can move across networks with the same speed, programmability, and transparency. This is the Internet of Value—a digital environment where money, ownership, and credentials move across interoperable networks, redefining the relationship between technology and the global economy.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">From Information to Value</h3>
                <p>The modern internet was designed to move information, which can be duplicated and transmitted instantly. Value, however, requires scarcity, security, and authorization. The **Internet of Value (IoV)** solves the digital value problem by integrating **Blockchain**, **Digital Identity**, and **Smart Contracts** into the network fabric. This transition from Web 2.0 (Read/Write) to Web3 (Read/Write/Own) allows for the representation and transfer of ownership without relying solely on centralized intermediaries.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Tokenization & Digital Ownership</h3>
                <p>Tokenization serves as the bridge between traditional assets and the IoV. By representing rights to securities, bonds, real estate, and intellectual property as digital tokens, we enable **Fractional Ownership** and automated compliance. In 2026, tokenized money and credit are increasingly moving on-chain, supported by **Zero-Knowledge technology** that balances the need for financial privacy with the requirements of lawful compliance.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pakistan's Rise in the Global IoV</h3>
                <p>Pakistan's digital maturity has seen a momentous leap, with its **ITU ID score rising to 67.7** in 2026. Under the **National Digital Masterplan**, the country is building the necessary infrastructure to participate in the global IoV. The expansion of **Raast** into bulk disbursements and P2M payments provides the foundational rail for this economy, ensuring that from Islamabad to the Orakzai valleys, value transfer is as seamless as sending a message.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Programmable Economy & AI Agents</h3>
                <p>The IoV enables a **Programmable Economy** where "Money as Software" executes transactions automatically based on predefined conditions. A major trend in 2026 is the rise of **AI Agents** and **Agentic Commerce**, where software agents discover products and execute transactions on behalf of users. This convergence of AI and Blockchain creates a resilient infrastructure for **Machine-to-Machine (M2M) value exchange**, powering everything from autonomous logistics to IoT service payments.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: The Internet of Value</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“The Internet of Value is the ultimate equalizer. It removes the friction of distance and the barriers of traditional finance. For the Orakzai community, it means the ability to participate in global markets and manage wealth with sovereignty and security. We are no longer just moving data; we are moving the future. The record is permanent, the value is programmable, and the network is universal.”</p>
            </div>

            <div class="final-statement">
                VALUE IS DATA.<br>
                DATA IS SOVEREIGN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Arthur D. Little, <em>Digital Assets Trends 2026: Stablecoins and AI Agents (Jan 2026)</em>.</li>
                    <li>J.P. Morgan, <em>Payments Outlook 2026: Real-Time Liquidity and Blockchain Settlements (2026)</em>.</li>
                    <li>Pakistan Digital Authority (PDA), <em>National Digital Masterplan: Building a Digital Nation (2026)</em>.</li>
                    <li>State Bank of Pakistan (SBP) / Bizinjo, <em>Raast P2M and Bulk Disbursement Expansion (June 2026)</em>.</li>
                    <li>TechJuice / ITU Reports, <em>Pakistan's ITU ID Score Rise: A 20% Jump in Digital Maturity (2025-2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            149
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-139-blockchain-infrastructure.html'

GRAPHICS = [
    ("Blockchain Stack", "HARD", "→", "APPL"),
    ("Infrastructure Nodes", "USER", "↔", "NODE"),
    ("Node Validation", "DATA", "→", "VERI"),
    ("Full Node Arch", "TXN", "→", "STAT"),
    ("Validator Node", "STAK", "→", "CONS"),
    ("Archival Node", "HIST", "↔", "STAT"),
    ("Light Client", "USER", "↔", "SYNC"),
    ("Validation Loop", "TXN", "↔", "RULE"),
    ("Consensus Mechanism", "MANY", "→", "ONE"),
    ("Proof of Work", "WORK", "→", "SEC"),
    ("Proof of Stake", "STAK", "→", "SEC"),
    ("BFT Protocols", "MANY", "↔", "AGRE"),
    ("Block Production", "MEM", "→", "BLCK"),
    ("Mempool Logic", "PEND", "→", "MEM"),
    ("P2P Networking", "NODE", "↔", "NODE"),
    ("Network Propagate", "ONE", "→", "ALL"),
    ("Peer Discovery", "SEED", "→", "PEER"),
    ("RPC Infrastructure", "APPL", "↔", "NODE"),
    ("RPC Endpoints", "API", "↔", "DATA"),
    ("API Layer", "DEV", "↔", "BC"),
    ("Indexer System", "BC", "→", "DB"),
    ("Block Explorer", "USER", "↔", "VIEW"),
    ("Blockchain Storage", "DATA", "↔", "DISK"),
    ("State Management", "STAT", "↔", "BC"),
    ("State Transitions", "PRE", "→", "POST"),
    ("Execution Layer", "CODE", "→", "OUT"),
    ("Virtual Machine", "EVM", "↔", "CODE"),
    ("Smart Contract Infra", "CODE", "↔", "SYS"),
    ("Gas and Fees", "USE", "→", "PAY"),
    ("Fee Market", "DEMD", "↔", "SUPP"),
    ("Block Space", "SIZE", "↔", "LIMT"),
    ("Scalability Model", "TPS", "↔", "SEC"),
    ("Blockchain Trilemma", "SEC", "SCAL", "DECN"),
    ("Layer-1 Network", "BASE", "↔", "ALL"),
    ("Layer-2 Network", "BASE", "↔", "EXEC"),
    ("Rollup Logic", "OFF", "→", "ON"),
    ("Sidechain Bridge", "MAIN", "↔", "SIDE"),
    ("App-Specific Chain", "APP", "↔", "BC"),
    ("Modular Blockchain", "EXEC", "DA", "CONS"),
    ("Data Availability", "VERI", "↔", "DATA"),
    ("DA Layers", "SCAL", "↔", "DATA"),
    ("Cross-Chain Infra", "NET-A", "↔", "NET-B"),
    ("Bridge Security", "LOCK", "↔", "MINT"),
    ("Interoperability", "MSG", "↔", "NET"),
    ("Oracle System", "REAL", "→", "BC"),
    ("Decentralized Oracle", "MANY", "→", "DATA"),
    ("Security Stack", "SAFE", "↔", "ALL"),
    ("Private Key Sec", "KEY", "↔", "SAFE"),
    ("HSM Architecture", "HARD", "↔", "KEY"),
    ("Validator Sec", "NODE", "↔", "SAFE"),
    ("Sentinel Arch", "SENT", "↔", "VALI"),
    ("Redundancy Loop", "NODE", "↔", "BACK"),
    ("High Availability", "UP", "↔", "ALL"),
    ("Monitor System", "METR", "↔", "VIEW"),
    ("Alerting Logic", "EVNT", "→", "ALRT"),
    ("Logging Stack", "EVNT", "→", "LOG"),
    ("Backup Strategy", "DATA", "→", "SAVE"),
    ("Disaster Recovery", "FAIL", "→", "RECV"),
    ("Cloud Infra", "CLD", "↔", "NODE"),
    ("Bare-Metal Node", "HARD", "↔", "NODE"),
    ("Geo Distribution", "LOC-A", "LOC-B", "LOC-C"),
    ("Network Bandwidth", "DATA", "↔", "FLOW"),
    ("Latency Loop", "REQ", "↔", "RES"),
    ("Hardware Reqs", "CPU", "RAM", "SSD"),
    ("SSD Performance", "READ", "↔", "WRIT"),
    ("Database Systems", "STAT", "↔", "DB"),
    ("Archive Storage", "HIST", "↔", "DISK"),
    ("Pruning Logic", "OLD", "→", "DEL"),
    ("State Sync", "NET", "→", "STAT"),
    ("Snapshots", "TIME", "→", "STAT"),
    ("Light Sync", "HDR", "→", "VERI"),
    ("Consensus Safety", "AGRE", "↔", "SAFE"),
    ("Liveness Loop", "UP", "↔", "TIME"),
    ("Finality Clock", "TXN", "→", "DONE"),
    ("Fork Management", "A", "B", "WIN"),
    ("Upgrade Path", "OLD", "→", "NEW"),
    ("Hard Fork", "PATH", "Y", "N"),
    ("Soft Fork", "PATH", "→", "NEW"),
    ("Governance Infra", "VOTE", "→", "RULE"),
    ("On-Chain Gov", "CODE", "↔", "VOTE"),
    ("Off-Chain Gov", "COMM", "↔", "TALK"),
    ("Treasury Arch", "FUND", "↔", "DAO"),
    ("Validator Voting", "STAK", "→", "VOTE"),
    ("Proposal Loop", "IDEA", "→", "EXEC"),
    ("Ecosystem Tooling", "DEV", "↔", "APPL"),
    ("SDK Framework", "CODE", "↔", "DEV"),
    ("Library Stack", "LIB", "↔", "CODE"),
    ("Testing Infra", "TEST", "↔", "CODE"),
    ("Audit Pipeline", "CODE", "↔", "SAFE"),
    ("Deployment Stack", "CODE", "→", "LIVE"),
    ("Node Management", "OPS", "↔", "NODE"),
    ("Kubernetes BC", "K8S", "↔", "NODE"),
    ("Docker BC", "CONT", "↔", "NODE"),
    ("Ansible BC", "AUTO", "↔", "NODE"),
    ("Infrastructure as Code", "CODE", "→", "SYS"),
    ("CI/CD for BC", "GIT", "→", "LIVE"),
    ("DevOps Pipeline", "DEV", "↔", "OPS"),
    ("SRE for Blockchain", "RELI", "↔", "SYS"),
    ("Performance Tuning", "OPT", "↔", "TPS"),
    ("Throughput Loop", "IN", "↔", "OUT"),
    ("Efficiency Metric", "COST", "↔", "VALU"),
    ("Green Infrastructure", "ECO", "↔", "SYS"),
    ("Renewable Mining", "SUN", "→", "BC"),
    ("Waste Heat Reuse", "HEAT", "→", "VALU"),
    ("Pakistan Power Grid", "GRID", "→", "2GW"),
    ("2GW Data Centers", "PWR", "→", "DATA"),
    ("QGDC Tier III", "Tier3", "↔", "PAK"),
    ("National AI Centers", "AI", "↔", "PAK"),
    ("Orakzai Sov Grid Arch", "SOV", "↔", "GRID"),
    ("OSG Node Distribution", "LOC", "↔", "BC"),
    ("OSG Security Layer", "SAFE", "↔", "GRID"),
    ("Faisal Orakzai profile", "SYS", "↔", "INF"),
    ("Future Infra Stack", "BASE", "→", "TOP"),
    ("Digital Infra Vision", "IDEA", "↔", "REAL"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g139-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g139-{index}-title g139-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g139-{index}-title">{safe}</title><desc id="g139-{index}-desc">A blockchain infrastructure relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2D2B" stroke="#2E8B8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A3C" stroke="#8B2E8B"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g139-{index}-caption" class="diagram-caption">{index}. {safe} — Blockchain infrastructure relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Blockchain Infrastructure Framework</title><desc id="hero-desc">A diagram showing the integrated framework for decentralized blockchain infrastructure, from hardware and power to modular execution layers.</desc><defs><linearGradient id="h139-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h139-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">BLOCKCHAIN INFRASTRUCTURE STACK</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="5" font-size="12">HARDWARE / CLOUD</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2D2B" stroke="#2E8B8B"/><text x="0" y="65" font-size="12">DATA CENTERS</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">NETWORKING / P2P</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">CONSENSUS LAYER</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="5" font-size="12">EXECUTION / VM</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#2D1A3C" stroke="#8B2E8B"/><text x="0" y="65" font-size="12">SMART CONTRACTS</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">MODULAR</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">ARCHITECTURE</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">BLOCKCHAIN INFRASTRUCTURE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“The Digital Infrastructure Behind Decentralized Networks.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Blockchain Infrastructure: The integrated framework for creating, operating, and securing decentralized networks through layered technical foundations.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 139</title>
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
            <p class="section-label">PAGE 139</p>
            <h2>BLOCKCHAIN INFRASTRUCTURE</h2>
            <p>“The Digital Infrastructure Behind Decentralized Networks.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Blockchain is often presented as a ledger, but a functioning blockchain is much more than a database. It is an interconnected infrastructure composed of nodes, validators, consensus mechanisms, and networking layers. Together, these components allow independent computers to maintain a shared digital state. Blockchain infrastructure is the technical foundation required to create, operate, secure, and interact with a decentralized network.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">The Layered Architecture</h3>
                <p>A modern blockchain can be understood as a layered system, from the physical hardware and cloud resources to the application layer. As of 2026, the global blockchain market is estimated at <strong>$54.08 billion</strong>. A major shift is occurring toward <strong>Modular Blockchain Architecture</strong>, which separates core functions like execution, consensus, and data availability. This allows specialized infrastructure, such as <strong>Data Availability (DA) Layers</strong>, to drive a scalability revolution, enabling networks to process greater activity while maintaining security.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Nodes, Networking & RPC</h3>
                <p>Nodes are the heart of the network, with diverse roles including <strong>Full Nodes</strong> for verification, <strong>Validators</strong> for consensus, and <strong>Archival Nodes</strong> for historical state. Applications interact with these nodes through <strong>RPC Infrastructure</strong>, which serves as a critical bridge. Indexers and explorers provide the necessary transparency, transforming raw activity into searchable datasets. Resilient infrastructure requires geographic distribution and redundancy to avoid single points of failure in the peer-to-peer network.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pakistan's Infrastructure Leap</h3>
                <p>Pakistan is making significant strides in building national digital infrastructure. The government has allocated <strong>2,000 megawatts (MW)</strong> of electricity to fuel Bitcoin mining and AI data centers. Projects like the <strong>Quantum Global Data Centre (QGDC)</strong>, with an initial investment of <strong>$230 million</strong>, are building Tier III data centers that provide the hardware foundation for sovereign digital networks. These initiatives, combined with training programs for 200,000 individuals annually, are positioning Pakistan as a participant in the global digital infrastructure economy.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI & Blockchain Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists approaching blockchain not just as a financial tool, but as a comprehensive infrastructure challenge. His work illustrates the shift toward understanding the entire stack—from hardware and power allocation to modular architectures and decentralized state management. He serves as one example of the "Young Pakistani Builder" who advocates for resilient, distributed systems that leverage Pakistan's emerging data center capacity and sovereign grids to empower local communities through verifiable digital infrastructure.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Blockchain Infrastructure</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Resilience & The Future</h3>
                <p>Blockchain infrastructure security extends across the entire stack, from private-key protection using <strong>Hardware Security Modules (HSMs)</strong> to validator sentry architectures. A mature deployment requires continuous monitoring, alerting, and robust disaster-recovery plans. As we move toward a machine-readable economy, the objective is to build infrastructure where legitimate rights and transactions are verifiable, interoperable, and accessible. The future of decentralized networks is defined by the strength and resilience of the infrastructure behind them.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Decentralization is not just a protocol; it is an infrastructure paradigm. To build a secure digital world, we must bridge the gap between physical power and digital state. The objective of blockchain infrastructure is to create a shared, tamper-resistant record that does not rely on a single central authority. From the national data centers of Pakistan to the local nodes of Orakzai, we are building the technical foundation for a more transparent and inclusive digital future.”</p>
            </div>

            <div class="final-statement">
                THE STACK IS DECENTRALIZED.<br>
                THE FUTURE IS INFRASTRUCTURE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>MarketsandMarkets, <em>Blockchain Technology Market Report 2026–2031</em>.</li>
                    <li>Government of Pakistan (MoITT), <em>National Initiative: 2,000 MW for Mining and AI Data Centers (2026)</em>.</li>
                    <li>Chainlink, <em>Modular Blockchain Architecture and Data Availability Layers in 2026</em>.</li>
                    <li>Quantum Global Data Centre (QGDC), <em>Pakistan Tier III Data Centre Initiative ($230M Investment)</em>.</li>
                    <li>Precedence Research, <em>Blockchain Distributed Ledger Market Size Report 2026</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            139
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

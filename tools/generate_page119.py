from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-119-cloud-computing.html'

GRAPHICS = [
    ("Cloud Computing Hero", "INFRA", "CLOUD", "APPS"),
    ("What is Cloud?", "POOL", "NET", "SRV"),
    ("NIST Characteristics", "5", "KEY", "TRAITS"),
    ("On-demand Service", "REQ", "→", "GET"),
    ("Broad Network Access", "ANY", "NET", "ANY"),
    ("Resource Pooling", "SRV", "↔", "POOL"),
    ("Rapid Elasticity", "TRAF", "↔", "CAP"),
    ("Measured Service", "USE", "→", "$$$"),
    ("Traditional vs Cloud", "OWN", "vs", "USE"),
    ("Cloud vs Internet", "NET", "≠", "SRV"),
    ("Cloud vs Data Centre", "FACIL", "≠", "MODEL"),
    ("Why Cloud Exists", "PEAK", "↔", "BASE"),
    ("Virtualization Logic", "PHYS", "→", "VIRT"),
    ("Hypervisor Logic", "HARD", "OS", "VM"),
    ("Virtual Machines", "BOX", "OS", "APP"),
    ("Containers Logic", "APP", "BOX", "KERN"),
    ("Kubernetes Logic", "BOX", "ORCH", "SRV"),
    ("Service Models", "IaaS", "PaaS", "SaaS"),
    ("IaaS Logic", "CPU", "RAM", "NET"),
    ("PaaS Logic", "OS", "DB", "CODE"),
    ("SaaS Logic", "SOFT", "WEB", "USER"),
    ("Deployment Models", "PUB", "PRIV", "HYB"),
    ("Public Cloud", "MANY", "ONE", "SRV"),
    ("Private Cloud", "ONE", "ONE", "SRV"),
    ("Hybrid Cloud", "PRIV", "↔", "PUB"),
    ("Multi-cloud Logic", "AWS", "AZ", "GC"),
    ("Regions & Zones", "GEO", "→", "ZONE"),
    ("Vertical Scaling", "SMALL", "→", "BIG"),
    ("Horizontal Scaling", "1", "→", "100"),
    ("Load Balancing", "REQ", "BAL", "SRV"),
    ("Autoscaling Logic", "AUTO", "UP", "DOWN"),
    ("Object Storage", "FILE", "ID", "BUCK"),
    ("Block Storage", "DISK", "VOL", "SRV"),
    ("File Storage", "PATH", "DIR", "FILE"),
    ("Cloud Databases", "SQL", "DATA", "SRV"),
    ("Cloud Networking", "VPC", "SUB", "RTE"),
    ("DNS Logic", "NAME", "→", "IP"),
    ("CDN Logic", "FAST", "EDGE", "USER"),
    ("Serverless Logic", "CODE", "RUN", "OFF"),
    ("Event-driven Cloud", "EVT", "→", "FUNC"),
    ("Shared Responsibility", "PROV", "+", "CUST"),
    ("IAM Logic", "ID", "AUTH", "RES"),
    ("Authentication", "WHO", "→", "ID"),
    ("Authorization", "WHAT", "→", "PERM"),
    ("Encryption Logic", "KEY", "LOCK", "DATA"),
    ("Backup Logic", "DATA", "→", "SAVE"),
    ("Disaster Recovery", "FAIL", "→", "REST"),
    ("RTO Logic", "TIME", "TO", "LIVE"),
    ("RPO Logic", "DATA", "TO", "LOSS"),
    ("High Availability", "UP", "+", "RED"),
    ("Observability Logic", "LOG", "MET", "TRAC"),
    ("Cloud Costs", "USE", "→", "BILL"),
    ("Cost Optimization", "SIZE", "AUTO", "SAVE"),
    ("Vendor Lock-in", "DEP", "≠", "PORT"),
    ("Open Source Cloud", "FREE", "CODE", "SRV"),
    ("Infra as Code", "CODE", "→", "SRV"),
    ("DevOps & Cloud", "BUILD", "→", "LIVE"),
    ("Cloud-native Logic", "CONT", "MICRO", "OBS"),
    ("Cloud + AI", "DATA", "GPU", "MOD"),
    ("GPU Computing", "PARAL", "FAST", "AI"),
    ("Big Data Cloud", "PIPE", "PROC", "INS"),
    ("Cloud + Fintech", "PAY", "SEC", "SRV"),
    ("Cloud + E-commerce", "BUY", "CART", "ORDER"),
    ("Cloud + Education", "LAB", "WEB", "LEARN"),
    ("Cloud + Remote Work", "HOME", "WEB", "OFF"),
    ("Pakistan Cloud Eco", "MOITT", "NITB", "BIZ"),
    ("Data Residency", "LAW", "GEO", "DATA"),
    ("Pak Cloud Policy", "FIRST", "GOVT", "2022"),
    ("Digital Sovereignty", "CTRL", "DATA", "PAK"),
    ("Orakzai and Cloud", "REM", "→", "GLOB"),
    ("Faisal Case Study", "TECH", "REM", "SRV"),
    ("Faisal Philosophy", "IDEA", "SYS", "GLOB"),
    ("Cloud Preservation", "SAVE", "MEM", "DATA"),
    ("Cloud Risks", "OUT", "SEC", "LOCK"),
    ("Future of Cloud", "AI", "EDGE", "QUANT"),
    ("Cloud-edge-device", "C", "↔", "E"),
    ("Cloud + Quantum", "QBIT", "REM", "LAB"),
    ("What Cloud Changed", "HARD", "→", "PROG"),
    ("What Cloud Didn't", "POW", "SRV", "ENG"),
    ("Physical Infra", "CABLE", "DC", "COOL"),
    ("Server Racks", "UNIT", "RACK", "ROW"),
    ("Cooling Logic", "HEAT", "→", "OUT"),
    ("Power Logic", "GRID", "UPS", "SRV"),
    ("Network Logic", "LINK", "SWIT", "RTE"),
    ("Data Centre Node", "SEC", "POW", "COOL"),
    ("API Node", "APP", "↔", "SRV"),
    ("Microservices Node", "SMALL", "FAST", "SRV"),
    ("Service Discovery", "FIND", "NAME", "SRV"),
    ("Message Queues", "SEND", "WAIT", "GET"),
    ("Caching Node", "MEM", "FAST", "RES"),
    ("Secrets Management", "KEY", "SEC", "APP"),
    ("Monitoring Node", "EYE", "SRV", "DATA"),
    ("Logging Node", "ACT", "→", "LOG"),
    ("Tracing Node", "REQ", "→", "PATH"),
    ("CI/CD Logic", "CODE", "TEST", "LIVE"),
    ("Container Registry", "PUSH", "IMG", "PULL"),
    ("DB Replication", "DB", "→", "DB"),
    ("Cloud Backup Node", "DATA", "→", "S3"),
    ("DR Architecture", "FAIL", "SWIT", "LIVE"),
    ("Infra Resilience", "SAFE", "FAST", "UP"),
    ("Digital Inclusion", "ACC", "AFF", "USE"),
    ("Evidence Matrix", "DATA", "CONF", "SAVE"),
    ("Research Gap Node", "MISS", "NEED", "FIND"),
    ("Oral History Node", "PAST", "NOW", "NEXT"),
    ("Final Statement", "SRV", "PROG", "WORLD"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g119-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g119-{index}-title g119-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g119-{index}-title">{safe}</title><desc id="g119-{index}-desc">A cloud relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g119-{index}-caption" class="diagram-caption">{index}. {safe} — cloud concept.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Cloud Computing Architecture</title><desc id="hero-desc">A conceptual diagram showing a cloud layer made of interconnected nodes, with physical infrastructure below and digital services above.</desc><defs><linearGradient id="h119-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h119-bg)" stroke="#B59654" stroke-opacity=".55"/><path d="M200 200 Q 380 100 560 200 T 200 200" fill="none" stroke="#B59654" stroke-width="2" stroke-dasharray="4 4" opacity=".4"/><circle cx="380" cy="215" r="90" fill="none" stroke="#B59654" stroke-width="1" opacity=".3"/><g transform="translate(380, 215)"><path d="M-40 -20 Q 0 -60 40 -20 Q 80 -20 80 20 Q 80 60 40 60 Q 0 60 -40 60 Q -80 60 -80 20 Q -80 -20 -40 -20" fill="#3C3020" stroke="#B59654" stroke-width="2"/><text x="0" y="25" text-anchor="middle" fill="#F5F0E6" font-size="14" font-weight="bold">CLOUD</text></g><g transform="translate(380, 360)" opacity=".8"><rect x="-200" y="0" width="400" height="40" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="0" y="25" text-anchor="middle" fill="#F5F0E6" font-size="10">INFRASTRUCTURE: DATA CENTRES • SERVERS • STORAGE • POWER</text></g><g transform="translate(380, 70)"><rect x="-200" y="0" width="400" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="25" text-anchor="middle" fill="#F5F0E6" font-size="10">SERVICES: AI • FINTECH • E-COMMERCE • EDUCATION</text></g><path d="M380 360 L 380 275" stroke="#B59654" stroke-width="1.5" marker-end="url(#arrow)"/><path d="M380 110 L 380 155" stroke="#B59654" stroke-width="1.5" marker-end="url(#arrow)"/><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">CLOUD COMPUTING</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Turning computing infrastructure into an on-demand service.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Cloud Computing: The programmable abstraction of physical infrastructure into scalable digital services.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 119</title>
    <link rel="stylesheet" href="../styles/main.css">
    <style>
        :root {{ --gold: #B59654; --green: #2E8B57; --blue: #7894A8; --cream: #F5F0E6; --muted: rgba(245,240,230,.72); }}
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
            <p class="section-label">PAGE 119</p>
            <h2>CLOUD COMPUTING</h2>
            <p>“Turning computing infrastructure into an on-demand service.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Once, building a digital service meant buying physical machines. A company needed servers, storage, networking equipment, space, electricity, and cooling. And when the service grew, the company had to buy more. Cloud computing changed the model. Instead of treating computing power as something every organization must physically own, cloud computing made computing resources available as services. A developer can request computing capacity, create a database, store files, deploy an application, scale infrastructure, and release software to users around the world. The machines still exist somewhere. The electricity is still required. The networks still carry the data. But the relationship between the user and the physical infrastructure has changed. The cloud is therefore not magic. It is infrastructure made programmable.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Defining the Cloud: The NIST Framework</h3>
                <p>Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources. According to the <strong>NIST framework</strong>, it is defined by five essential characteristics: <strong>On-demand self-service</strong>, <strong>Broad network access</strong>, <strong>Resource pooling</strong>, <strong>Rapid elasticity</strong>, and <strong>Measured service</strong>. These traits distinguish the cloud from traditional data centers by making infrastructure elastic and responsive to demand.</p>
                <p>The ecosystem is further categorized into service models—<strong>IaaS</strong> (Infrastructure), <strong>PaaS</strong> (Platform), and <strong>SaaS</strong> (Software)—and deployment models, including <strong>Public</strong>, <strong>Private</strong>, <strong>Hybrid</strong>, and <strong>Community</strong> clouds.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pakistan's Cloud Landscape (2025–2026)</h3>
                <p>Pakistan has adopted a <strong>Cloud First Policy (2022)</strong>, requiring federal entities to prioritize cloud solutions. In June 2026, the <strong>National Data Governance Policy</strong> was finalized, establishing a framework for data residency and sovereignty, mandating that sensitive national data be stored on physical servers within the country. The public cloud market in Pakistan reached an estimated <strong>US$332 million</strong> in 2025, driven by the growth of startups, fintech, and digital government initiatives.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Building Systems from a Remote-First Perspective</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur</strong></p>
                    <p>Faisal Orakzai serves as a personal case study of how cloud abstraction enables individuals from remote regions to participate in the global software economy. His work, focused on software development and digital platforms (e.g., <strong>OkzByte Hub</strong>, <strong>Orakzai Group</strong>), illustrates a "Systems Philosophy"—leveraging programmable infrastructure to build services that are not limited by physical geography. By adopting cloud-native methodologies, he shows how mountain-based memory can be combined with global-scale computing to create international value.</p>
                    <p><em>“This case study illustrates how an individual founder can move between software and digital platforms... It should not be interpreted as a statistical representation of Orakzai entrepreneurs.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Cloud Computing</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Future of Cloud: AI, Edge & Sovereignty</h3>
                <p>The next generation of cloud computing is being shaped by <strong>AI infrastructure</strong> (GPU-accelerated compute), <strong>Edge computing</strong> (processing closer to the user), and <strong>Sovereign cloud</strong> initiatives. While the cloud reduces barriers, it introduces new risks around vendor lock-in, data residency, and shared security responsibility. A resilient digital economy requires both the software people see and the programmable infrastructure that allows it to exist.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Research Gap: What Still Needs to be Documented</h3>
                <ul>
                    <li>Detailed cloud adoption rates across different sectors of the Pakistani economy.</li>
                    <li>The long-term impact of data residency requirements on local cloud innovation.</li>
                    <li>Records of women working in specialized cloud engineering and DevOps roles.</li>
                    <li>Usage patterns of cloud-enabled services in tribal districts and remote regions.</li>
                </ul>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“When I first understood cloud computing, I realized that distance does not have to determine access to computing. A developer can write software from a laptop, and the infrastructure can be provisioned remotely. This changes the scale of possibility for someone in Pakistan. But the cloud is not magic; it is physical. It depends on cables, electricity, and cooling. What changed was the abstraction—infrastructure became programmable. For the next generation of Pakistani builders, understanding the cloud is about understanding how ideas become systems, and how systems become global services.”</p>
            </div>

            <div class="final-statement">
                THE CLOUD DID NOT REMOVE THE MACHINE.<br>
                IT MADE THE MACHINE PROGRAMMABLE.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>NIST, <em>The NIST Definition of Cloud Computing (SP 800-145)</em>.</li>
                    <li>Ministry of IT & Telecom, <em>Pakistan Cloud First Policy (2022)</em>.</li>
                    <li>MoITT, <em>National Data Governance Policy 2026 (Finalized June)</em>.</li>
                    <li>6Wresearch, <em>Pakistan Public Cloud Market Report 2026</em>.</li>
                    <li>NITB, <em>E-Government Cloud Infrastructure & Accreditation Updates 2026</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            119
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-120-the-future-of-computing.html'

GRAPHICS = [
    ("Future Computing Hero", "MACHINES", "→", "SYSTEMS"),
    ("Computing Timeline", "PAST", "NOW", "NEXT"),
    ("What is Computing?", "INPUT", "PROC", "OUT"),
    ("Classical Computer", "CPU", "MEM", "IO"),
    ("Moore's Law", "TRANS", "↑", "SIZE"),
    ("Beyond Transistors", "ARCH", "PACK", "SOFT"),
    ("Specialized Computing", "CPU", "GPU", "NPU"),
    ("CPU Logic", "GEN", "PURP", "INST"),
    ("GPU Logic", "PARAL", "MATH", "PIX"),
    ("NPU Logic", "AI", "INF", "MATR"),
    ("FPGA Logic", "RECON", "HARD", "CHIP"),
    ("ASIC Logic", "SPEC", "HARD", "EFF"),
    ("Edge Computing", "USER", "↔", "EDGE"),
    ("Distributed Computing", "NODE", "↔", "NET"),
    ("IoT Logic", "SENS", "NET", "ACT"),
    ("Ambient Computing", "ENV", "IS", "COMP"),
    ("Spatial Computing", "3D", "REAL", "VIRT"),
    ("Wearables Logic", "BODY", "SENS", "DATA"),
    ("HCI Evolution", "GUI", "NUI", "BCI"),
    ("Multimodal Logic", "TEXT", "IMG", "AUD"),
    ("Artificial Intelligence", "DATA", "MOD", "OUT"),
    ("Generative AI", "PROMPT", "→", "CREAT"),
    ("AI Agents", "PLAN", "ACT", "LEARN"),
    ("Edge AI", "LOCAL", "AI", "PRIV"),
    ("AI Robotics", "BRAIN", "↔", "BODY"),
    ("Autonomous Systems", "AUTO", "DECIS", "ACT"),
    ("Quantum Computing", "QBIT", "SUP", "ENT"),
    ("Classical Bit", "0", "OR", "1"),
    ("Qubit Logic", "0", "AND", "1"),
    ("Quantum Gates", "QBIT", "→", "GATE"),
    ("Quantum Apps", "CHEM", "OPT", "CRYPT"),
    ("Quantum Limits", "NOISE", "ERR", "DECO"),
    ("Quantum Error Corr", "RED", "CHECK", "FIX"),
    ("Post-Quantum Crypt", "SAFE", "FROM", "QUAN"),
    ("Neuromorphic Logic", "NEUR", "SYN", "SPIK"),
    ("Photonic Logic", "LIGHT", "NOT", "ELEC"),
    ("In-memory Logic", "COMP", "+", "MEM"),
    ("3D Chips", "LAY1", "LAY2", "LAY3"),
    ("Chiplets Logic", "DIE", "+", "DIE"),
    ("RISC-V Logic", "OPEN", "ISA", "FREE"),
    ("Open Hardware", "BLUE", "PRINT", "CHIP"),
    ("Cloud Computing", "SRV", "WEB", "USER"),
    ("Cloud-Edge-Device", "C", "E", "D"),
    ("Quantum-Cloud", "USER", "WEB", "QUAN"),
    ("Biology Computing", "DNA", "CODE", "LIFE"),
    ("BCI Logic", "BRAIN", "↔", "COMP"),
    ("Robotics Architecture", "SENS", "BRAI", "ACT"),
    ("Humanoid Robotics", "HUMAN", "LIKE", "ROB"),
    ("Automation Logic", "TASK", "→", "AUTO"),
    ("Future Programming", "INT", "→", "CODE"),
    ("AI Coding", "GEN", "FIX", "OPT"),
    ("Future Engineer", "SYS", "AI", "SEC"),
    ("Cybersecurity Future", "AI", "vs", "AI"),
    ("Privacy Logic", "OWN", "DATA", "PRIV"),
    ("Confidential Comp", "TEE", "SEC", "PROC"),
    ("Digital Sovereignty", "CTRL", "TECH", "LAW"),
    ("Semiconductor Eco", "DES", "FAB", "PACK"),
    ("Chip Design", "SPEC", "HDL", "LOG"),
    ("Semiconductor Fab", "WAFER", "ETCH", "CHIP"),
    ("Packaging Logic", "CHIP", "BOX", "PIN"),
    ("Testing Logic", "TRY", "VER", "OK"),
    ("Pakistan Semiconductors", "TAL", "EDU", "DES"),
    ("Pakistan AI", "NCAI", "LAB", "PROD"),
    ("Pakistan Quantum", "UNI", "RES", "FUT"),
    ("Pakistan Robotics", "LAB", "COMP", "IND"),
    ("Young Pakistan", "LEARN", "BUILD", "SCALE"),
    ("Faisal Future Comp", "SYS", "AI", "INF"),
    ("Faisal Framework", "SOFT", "AI", "BC"),
    ("Orakzai and Future", "REM", "→", "GLOB"),
    ("Computing for Humanity", "SOLV", "PROB", "LIVE"),
    ("Future Risks", "MIS", "SURV", "INEQ"),
    ("Computing Divide", "ACC", "AFF", "SKIL"),
    ("Energy Logic", "POW", "COOL", "COMP"),
    ("Green Computing", "EFF", "RENE", "RECY"),
    ("Five-Year Outlook", "AI", "EDGE", "AUTO"),
    ("Ten-Year Outlook", "QUAN", "ROB", "AGI"),
    ("2040 Questions", "WHAT", "IF", "FUT"),
    ("What Will Not Change", "HUM", "NEED", "ETH"),
    ("Most Important Comp", "SOLV", "RESP", "RELI"),
    ("Classical + AI", "CPU", "+", "NPU"),
    ("CPU + GPU", "SEQ", "+", "PARA"),
    ("Memory Hierarchy", "REG", "CACH", "RAM"),
    ("Data Movement", "MEM", "→", "PROC"),
    ("Accelerator Arch", "SPEC", "PIPEL", "OUT"),
    ("AI Training", "DATA", "→", "MOD"),
    ("AI Inference", "MOD", "→", "RES"),
    ("Robotics Perception", "SEE", "HEAR", "FEEL"),
    ("Robotics Planning", "MAP", "PATH", "GOAL"),
    ("Robotics Control", "BRAI", "→", "MOT"),
    ("Sensor Fusion", "S1", "+", "S2"),
    ("Autonomous Loop", "PERC", "DEC", "ACT"),
    ("Edge Inference", "MOD", "ON", "DEV"),
    ("Quantum Measure", "STAT", "→", "BIT"),
    ("Quantum Noise", "HEAT", "RAD", "ERR"),
    ("QEC Logic", "LOG", "PHY", "QBIT"),
    ("Crypt Transition", "RSA", "→", "PQC"),
    ("Chiplet Arch", "DIE1", "BUS", "DIE2"),
    ("3D Packaging", "VERT", "STAC", "VIAS"),
    ("Open Instruction", "RISC", "V", "STD"),
    ("Open Hardware Eco", "COMM", "DES", "CHIP"),
    ("Cloud-Edge Cont", "C", "↔", "E"),
    ("Distributed Intel", "DIST", "AI", "COLL"),
    ("Smart Environment", "WALL", "OBJ", "SENS"),
    ("Wearable Eco", "WAT", "RING", "GLAS"),
    ("Spatial Interface", "3D", "HAND", "EYE"),
    ("Multimodal Interface", "TALK", "LOOK", "DO"),
    ("Human-AI Collab", "HUM", "+", "AI"),
    ("AI Governance", "RULE", "LAW", "ETH"),
    ("Technology Ethics", "GOOD", "BAD", "CHOI"),
    ("Digital Inequality", "HAVE", "≠", "NOT"),
    ("Energy-Efficient", "WATT", "↓", "OPS"),
    ("Semiconductor Supply", "MAT", "FAB", "LOG"),
    ("Research Ecosystem", "UNI", "GOV", "BIZ"),
    ("Pakistan Opportunity", "BRAI", "CODE", "GLOB"),
    ("Future Workforce", "SKIL", "NEW", "JOB"),
    ("Research Gap Node", "MISS", "NEED", "FIND"),
    ("Evidence Matrix", "DATA", "CONF", "SAVE"),
    ("Classification Sys", "CUR", "EMER", "RES"),
    ("Oral History Node", "PAST", "NOW", "NEXT"),
    ("Final Statement", "MACH", "PEOP", "IDEA"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g120-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g120-{index}-title g120-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g120-{index}-title">{safe}</title><desc id="g120-{index}-desc">A future computing relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g120-{index}-caption" class="diagram-caption">{index}. {safe} — computing concept.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">The Future of Computing</title><desc id="hero-desc">A chronological progression of computing technology from vacuum tubes to quantum and robotics.</desc><defs><linearGradient id="h120-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h120-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(40, 100)" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6" text-anchor="middle"><circle cx="0" cy="50" r="20" fill="#3C3020" stroke="#B59654"/><text x="0" y="90">VACUUM</text><path d="M20 50 H40" stroke="#B59654"/><circle cx="60" cy="50" r="20" fill="#3C3020" stroke="#B59654"/><text x="60" y="90">TRANS</text><path d="M80 50 H100" stroke="#B59654"/><circle cx="120" cy="50" r="20" fill="#3C3020" stroke="#B59654"/><text x="120" y="90">MICRO</text><path d="M140 50 H160" stroke="#B59654"/><circle cx="180" cy="50" r="20" fill="#153B2A" stroke="#2E8B57"/><text x="180" y="90">PC</text><path d="M200 50 H220" stroke="#B59654"/><circle cx="240" cy="50" r="20" fill="#153B2A" stroke="#2E8B57"/><text x="240" y="90">SMART</text><path d="M260 50 H280" stroke="#B59654"/><circle cx="300" cy="50" r="20" fill="#153B2A" stroke="#2E8B57"/><text x="300" y="90">CLOUD</text><path d="M320 50 H340" stroke="#B59654"/><circle cx="360" cy="50" r="20" fill="#202B35" stroke="#7894A8"/><text x="360" y="90">AI</text><path d="M380 50 H400" stroke="#B59654"/><circle cx="420" cy="50" r="20" fill="#202B35" stroke="#7894A8"/><text x="420" y="90">EDGE</text><path d="M440 50 H460" stroke="#B59654"/><circle cx="480" cy="50" r="20" fill="#202B35" stroke="#7894A8"/><text x="480" y="90">QUAN</text><path d="M500 50 H520" stroke="#B59654"/><circle cx="540" cy="50" r="20" fill="#202B35" stroke="#7894A8"/><text x="540" y="90">ROB</text><path d="M560 50 H580" stroke="#B59654"/><circle cx="600" cy="50" r="20" fill="#B59654" stroke="#F5F0E6"/><text x="600" y="90">FUTURE</text></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">THE FUTURE OF COMPUTING</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“From machines that calculate to systems that perceive, learn and act.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Computing Continuum: The vertical and horizontal evolution of processing power and intelligence.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 120</title>
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
        .classification-tag {{ font-size: 0.7rem; font-weight: bold; padding: 2px 6px; border-radius: 3px; margin-right: 5px; }}
        .tag-current {{ background: var(--green); color: white; }}
        .tag-emerging {{ background: var(--blue); color: white; }}
        .tag-research {{ background: var(--gold); color: black; }}
        .tag-speculative {{ background: #444; color: white; }}
        @media (max-width: 768px) {{ .atlas-grid {{ grid-template-columns: 1fr; }} }}
        svg {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="content-page">
        <header class="page-header">
            <p class="section-label">PAGE 120</p>
            <h2>THE FUTURE OF COMPUTING</h2>
            <p>“From machines that calculate to systems that perceive, learn and act.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Computing has never been a finished invention. The machines changed. The interfaces changed. The networks changed. The scale changed. A room-sized computer became a desktop. The desktop became a laptop. The laptop became a smartphone. The internet connected them. The cloud moved computation into large distributed infrastructure. Artificial intelligence changed what software could do. And now another transition is beginning. Computing is moving into more places, more devices and more forms. It is becoming more distributed. More specialized. More intelligent. More autonomous. And potentially more connected to the physical world. The future of computing will not be one machine replacing another. It will be an ecosystem of different machines working together.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Beyond Classical Architecture</h3>
                <p><span class="classification-tag tag-current">[CURRENT]</span> Classical computing, based on the von Neumann architecture, remains the bedrock of modern technology. However, as we approach the physical limits of transistor scaling, the focus is shifting toward <strong>Specialized Computing</strong>. This includes GPUs for parallel math, NPUs for AI inference, and custom ASICs for specific tasks. <strong>3D Chip Packaging</strong> and <strong>Chiplets</strong> are emerging to maintain performance gains beyond the traditional Moore's Law curve.</p>
                <p><span class="classification-tag tag-emerging">[EMERGING]</span> <strong>Edge Computing</strong> and the <strong>Internet of Things (IoT)</strong> are distributing intelligence closer to the source of data, reducing latency and bandwidth requirements. This enables <strong>Ambient Computing</strong>, where digital interaction becomes embedded in our physical environment through wearables and spatial interfaces.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The Quantum & Neuromorphic Frontier</h3>
                <p><span class="classification-tag tag-research">[RESEARCH]</span> <strong>Quantum Computing</strong> leverages superposition and entanglement to solve problems currently impossible for classical machines, such as molecular simulation and complex optimization. Parallel to this, <strong>Neuromorphic Computing</strong> mimics the brain's neural structure to achieve massive energy efficiency. <strong>Post-Quantum Cryptography (PQC)</strong> is already being standardized by NIST to protect today's data from future quantum threats.</p>
                <p><span class="classification-tag tag-speculative">[SPECULATIVE]</span> Looking toward 2040, we may see <strong>DNA Computing</strong> for ultra-dense data storage and mature <strong>Brain-Computer Interfaces (BCI)</strong> for direct human-machine interaction, though these remain in early experimental phases.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Thinking Beyond the Next Application</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai serves as a case study of a builder thinking beyond simple applications toward integrated digital systems. His interests, spanning software, blockchain, AI, and digital infrastructure (e.g., <strong>OkzByte Hub</strong>, <strong>Orakzai Group</strong>), reflect a "Systems-First" philosophy. By focusing on how these technologies converge, he illustrates how individuals from remote regions can contribute to the global future of computing. His framework suggests that the future belongs not to those with the largest machines, but to those who understand how machines, people, and ideas connect.</p>
                    <p><em>“This case study illustrates one individual's vision... It should not be interpreted as a representation of all Orakzai technology interests.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Future Computing</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Young Pakistan & The Opportunity</h3>
                <p>For the next generation of Pakistanis, the future of computing offers pathways in <strong>AI Research</strong>, <strong>Semiconductor Design</strong>, and <strong>Robotics</strong>. Institutions like the <strong>National Center of AI (NCAI)</strong> are already developing local products, while youth programs at <strong>NUST</strong> and other universities are training the workforce of 2030. The challenge remains the <strong>Computing Divide</strong>—ensuring that access to these advanced systems reaches remote districts like Orakzai.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Research Gap: What Still Needs to be Documented</h3>
                <ul>
                    <li>Pakistan's specific national AI compute capacity and GPU availability for researchers.</li>
                    <li>The status of quantum information science education in Pakistani universities.</li>
                    <li>Detailed mapping of robotics and automation research in non-urban districts.</li>
                    <li>The role of the Pakistani diaspora in global semiconductor and quantum research.</li>
                </ul>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“When I think about the future of computing, I do not imagine one giant machine replacing everything. I imagine layers. Classical processors will continue to calculate, while specialized accelerators handle AI and robotics. The future is an ecosystem. For Pakistan, we don't need to manufacture every component to participate; we need people who understand the systems. You don't have to wait for the future to arrive—you can learn, experiment, and build today. The future belongs to those who understand what machines can be used to build.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF COMPUTING IS NOT ONE MACHINE.<br>
                IT IS AN ECOSYSTEM OF MACHINES, PEOPLE AND IDEAS.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>NIST, <em>Post-Quantum Cryptography Standardization (FIPS 203, 204, 205)</em>.</li>
                    <li>NCAI Pakistan, <em>Annual Research & Product Portfolio 2026</em>.</li>
                    <li>Forbes, <em>7 Quantum Computing Trends That Will Shape 2026</em>.</li>
                    <li>Deloitte, <em>Technology Signals 2026: Neuromorphic & Edge AI</em>.</li>
                    <li>IBM Quantum / Google Quantum AI, <em>Hardware Roadmap & Error Correction Updates 2026</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            120
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

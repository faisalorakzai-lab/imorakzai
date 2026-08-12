from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-127-ai-and-finance.html'

GRAPHICS = [
    ("AI Finance Hero", "BANK", "↔", "AI"),
    ("Digital Finance Timeline", "CASH", "→", "AI"),
    ("Finance AI Def", "DATA", "↔", "DEC"),
    ("Finance Data System", "TRX", "+", "MKT"),
    ("Fraud Detection AI", "PATT", "↔", "SIG"),
    ("Real-Time Monitoring", "LIVE", "→", "SAFE"),
    ("AML AI System", "NETW", "↔", "COMP"),
    ("KYC AI Verification", "DOC", "↔", "IDEN"),
    ("Credit Scoring AI", "DATA", "↔", "RISK"),
    ("Financial Inclusion", "ACC", "↔", "OPP"),
    ("Bias in Finance AI", "DATA", "≠", "FAIR"),
    ("Personal Finance AI", "BUDG", "↔", "SAV"),
    ("Digital Assistant", "USER", "↔", "AI"),
    ("Financial Education AI", "LRN", "↔", "KNOW"),
    ("AI and Accounting", "RULE", "↔", "REC"),
    ("Document Processing", "AUTO", "↔", "ADM"),
    ("AI and Auditing", "DATA", "↔", "EVID"),
    ("Financial Forecasting", "HIST", "→", "EST"),
    ("Investment Research", "FILI", "↔", "ACC"),
    ("Algorithmic Trading", "MKT", "↔", "EXEC"),
    ("Market Sentiment AI", "TEXT", "→", "SIG"),
    ("Risk Management AI", "CRED", "↔", "LIQ"),
    ("AI and Insurance", "CLAM", "↔", "MOD"),
    ("AI and Payments", "ROUT", "↔", "FAST"),
    ("Mobile Finance Convergence", "PHON", "↔", "BANK"),
    ("Pak Digital Finance", "FIN", "↔", "TECH"),
    ("Fintech and AI", "SOFT", "↔", "FIN"),
    ("Pak Fintech Opportunity", "POP", "↔", "GROW"),
    ("RAAST AI Monitoring", "INST", "↔", "SAFE"),
    ("SBP AI Checklist", "RULE", "↔", "RESP"),
    ("NCAI NED Fintech", "LAB", "↔", "INNO"),
    ("SME Finance AI", "DATA", "↔", "CRED"),
    ("Rural Finance AI", "LOCL", "↔", "ACC"),
    ("Pashto Financial AI", "PASH", "↔", "ADVI"),
    ("Trust Architecture", "VERI", "→", "TRST"),
    ("Human-in-the-Loop", "AI", "↔", "HUM"),
    ("Responsible AI Finance", "ETH", "↔", "TECH"),
    ("Cybersecurity in Finance", "PROT", "↔", "RISK"),
    ("Data Governance", "RULE", "↔", "SAFE"),
    ("AI Audit Trail", "ACT", "→", "LOG"),
    ("Fraud Signal Alert", "DETE", "→", "ALRT"),
    ("KYC Anomaly Detect", "ID", "≠", "USER"),
    ("Credit Risk Model", "CAP", "↔", "RISK"),
    ("Liquidity Risk AI", "CASH", "↔", "NEED"),
    ("Market Risk Model", "VOLA", "↔", "VALU"),
    ("Operational Risk AI", "PROC", "↔", "FAIL"),
    ("Claims Processing AI", "DOC", "→", "SETL"),
    ("Insurance Risk Model", "HIST", "→", "PREM"),
    ("Payment Routing Opt", "PATH", "↔", "EFF"),
    ("Transaction Pattern", "FREQ", "+", "LOC"),
    ("Account Behavior AI", "NORM", "≠", "ANOM"),
    ("Device Info Verification", "IP", "+", "IMEI"),
    ("Document Extraction", "OCR", "→", "DATA"),
    ("Invoice Reconciliation", "BILL", "↔", "PAY"),
    ("Regulatory Reporting", "DATA", "→", "GOV"),
    ("Duplicate Payment Det", "PAY", "==", "PAY"),
    ("Unexpected Relation", "ENTI", "↔", "ENTI"),
    ("Market Forecast AI", "ECON", "→", "VAL"),
    ("Earnings Report Proc", "TEXT", "→", "NUM"),
    ("Sentiment Signal", "PUB", "→", "FEEL"),
    ("Trading Execution", "ORD", "→", "FILL"),
    ("Portfolio Optimization", "ASST", "↔", "YLD"),
    ("Budgeting Insight", "INC", "-", "EXP"),
    ("Savings Goal AI", "CURR", "→", "GOAL"),
    ("Interest Rate Calc", "PRIN", "↔", "TIME"),
    ("Financial Risk Ed", "KNOW", "↔", "SAFE"),
    ("Digital Onboarding", "USER", "→", "OPEN"),
    ("Microfinance AI", "SMAL", "↔", "GROW"),
    ("Agri Finance AI", "CROP", "↔", "LOAN"),
    ("Lending Fairness AI", "EQL", "↔", "DATA"),
    ("Transparency Loop", "OPEN", "↔", "MOD"),
    ("Monitoring Cycle", "TEST", "→", "FIX"),
    ("Privacy Shield AI", "DATA", "↔", "HIDE"),
    ("Security Wall AI", "ATTK", "≠", "PASS"),
    ("Financial Data Gov", "LAW", "↔", "CODE"),
    ("AI Talent in Finance", "EDU", "→", "PRO"),
    ("Pakistan AI Strategy 2", "NAT", "↔", "FIN"),
    ("Global Fintech Map", "PAK", "↔", "GLOB"),
    ("AI Future Finance", "CIV", "↔", "VAL"),
    ("Orakzai Heritage Fin", "TRI", "→", "DIGI"),
    ("AI Literacy Finance", "DATA", "↔", "ETH"),
    ("Verification Loop 2", "AI", "→", "HUM"),
    ("AI Infra Finance", "GPU", "+", "SEC"),
    ("AI Talent Pipe 2", "UNI", "→", "FIN"),
    ("AI Export Finance", "VAL", "→", "GLB"),
    ("AI Product Life 2", "DEV", "→", "MKT"),
    ("AI Governance 2", "RULE", "↔", "SAFE"),
    ("Responsible AI Fin 2", "ETH", "↔", "TECH"),
    ("AI Trust 2", "VERI", "→", "TRST"),
    ("Human Oversight 2", "EYE", "→", "MOD"),
    ("AI Security 2", "DETE", "↔", "PROT"),
    ("AI Privacy 2", "SAFE", "↔", "RISK"),
    ("AI Data Lifecycle 2", "COLL", "→", "GOV"),
    ("AI Compute Life 2", "POW", "→", "OPS"),
    ("AI Cloud Arch 2", "SRV", "↔", "USER"),
    ("AI Research Eco 2", "UNI", "↔", "LAB"),
    ("Pakistan AI Map 2", "KHI", "LHR", "ISB"),
    ("AI Sector Map 2", "FIN", "AGRI", "HLTH"),
    ("AI Future Path 2", "SPEC", "↔", "GLOB"),
    ("AI Ethics Loop 2", "GOOD", "↔", "BAD"),
    ("AI Accessibility 2", "OPEN", "↔", "ALL"),
    ("AI Sustainability 2", "POW", "↔", "EFF"),
    ("AI Reliability 2", "PRED", "↔", "FACT"),
    ("AI Bias Loop 2", "DATA", "→", "OUT"),
    ("AI Safety Loop 2", "TEST", "→", "SAFE"),
    ("AI Transparency 2", "OPEN", "↔", "BOX"),
    ("AI Fairness 2", "EQL", "↔", "BIAS"),
    ("AI Robustness 2", "STRE", "↔", "ATTK"),
    ("AI Explainability 2", "WHY", "↔", "MOD"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g127-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g127-{index}-title g127-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g127-{index}-title">{safe}</title><desc id="g127-{index}-desc">An AI finance relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#1A2B3C" stroke="#2E5C8B"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#2D1A1A" stroke="#8B2E2E"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g127-{index}-caption" class="diagram-caption">{index}. {safe} — financial relationship.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">AI & Finance Transformation</title><desc id="hero-desc">A diagram showing the transition from traditional banking to an intelligent, secure financial ecosystem.</desc><defs><linearGradient id="h127-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h127-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 60)" text-anchor="middle" font-family="Arial,sans-serif" fill="#F5F0E6"><text x="0" y="0" font-size="18" font-weight="bold" fill="#B59654">INTELLIGENT FINANCIAL ECOSYSTEM</text><path d="M0 15 V 60" stroke="#B59654" stroke-width="2"/><path d="M-240 60 H 240" stroke="#B59654" stroke-width="2"/><path d="M-240 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M0 60 V 90" stroke="#B59654" stroke-width="2"/><path d="M240 60 V 90" stroke="#B59654" stroke-width="2"/><g transform="translate(-240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#1A2B3C" stroke="#2E5C8B"/><text x="0" y="5" font-size="12">BANKING</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#1A2B3C" stroke="#2E5C8B"/><text x="0" y="65" font-size="12">FRAUD DETECTION</text></g><g transform="translate(0, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="5" font-size="12">INVESTMENT</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#3C3020" stroke="#B59654"/><text x="0" y="65" font-size="12">RISK ANALYSIS</text></g><g transform="translate(240, 110)"><rect x="-70" y="-20" width="140" height="40" rx="4" fill="#2D1A1A" stroke="#8B2E2E"/><text x="0" y="5" font-size="12">INCLUSION</text><path d="M0 20 V 40" stroke="#B59654"/><rect x="-70" y="40" width="140" height="40" rx="4" fill="#2D1A1A" stroke="#8B2E2E"/><text x="0" y="65" font-size="12">DIGITAL ACCESS</text></g><path d="M-240 190 V 220 H 240 V 190" fill="none" stroke="#B59654" stroke-width="2"/><path d="M0 220 V 250" stroke="#B59654" stroke-width="2"/><g transform="translate(0, 280)"><rect x="-100" y="-30" width="200" height="60" rx="8" fill="#0E1110" stroke="#B59654" stroke-width="3"/><text x="0" y="-5" font-size="16" font-weight="bold" fill="#B59654">RESPONSIBLE</text><text x="0" y="15" font-size="16" font-weight="bold" fill="#B59654">INNOVATION</text></g></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">AI & FINANCE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Securing the future through intelligent, responsible financial systems.”</text></svg><figcaption id="hero-caption" class="diagram-caption">Intelligent Finance: The integration of AI into banking, investment research, and financial inclusion.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 127</title>
    <link rel="stylesheet" href="../styles/main.css">
    <style>
        :root {{ --gold: #B59654; --blue: #2E5C8B; --red: #8B2E2E; --cream: #F5F0E6; --muted: rgba(245,240,230,.72); }}
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
            <p class="section-label">PAGE 127</p>
            <h2>AI & FINANCE</h2>
            <p>“Artificial Intelligence and the Future of Finance.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Finance has always depended on information. Banks evaluate risk. Investors study markets. Businesses manage cash flows. Governments monitor economies. Individuals make decisions about savings, payments and borrowing. Artificial intelligence is changing how financial information can be processed. AI can analyze large datasets, identify patterns, automate repetitive processes and support financial decision-making. But finance is also a high-stakes environment. A wrong recommendation can cost money. A fraudulent transaction can affect a person's livelihood. A biased lending system can deny someone access to opportunity. The future of financial AI therefore requires both innovation and responsibility.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Intelligent Banking & Fraud Detection</h3>
                <p>Banking is a natural environment for AI due to the sheer volume of transactions and documents. AI systems analyze transaction frequency, location signals, and behavioral patterns to identify potential fraud in near real-time. This is particularly valuable in Pakistan's rapidly growing digital payment ecosystem, where systems like <strong>RAAST</strong> manage millions of transactions. However, a suspicious signal is not a definitive diagnosis; human review remains essential to maintain trust and accuracy.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Institutional Anchor: SBP & NCAI</h3>
                <p>Pakistan's financial sector is guided by institutional research and robust regulation. The <strong>National Centre of Artificial Intelligence (NCAI)</strong>, particularly through its network including <strong>NED University Karachi</strong>, drives innovation in smart financial services. In 2026, the <strong>State Bank of Pakistan (SBP)</strong> implemented a comprehensive <em>Regulatory Checklist for AI in Financial Services</em>, ensuring that banks and fintechs deploy AI with transparency, accountability, and strong privacy controls.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Financial Inclusion & SME Growth</h3>
                <p>AI represents a powerful tool for expanding financial access. By analyzing alternative data—such as mobile usage and utility payments—AI-driven credit scoring models can assess the creditworthiness of previously unbanked individuals and SMEs. The SBP's updated <strong>Prudential Regulations for SME Financing (2026)</strong> support these digital assessment models, fostering economic growth in rural and remote regions like Orakzai, where traditional credit histories may be limited.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — The AI Generation</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai represents the generation of young Pakistani technologists growing up alongside the transformation of digital infrastructure and finance. His documented interests in software, digital systems, and blockchain align with the "Systems Philosophy" required for building integrated financial data architectures. He serves as one example of the "Young Pakistani Builder" who approaches technology as a tool for solving real-world structural problems. His journey illustrates how young Pakistanis can bridge the gap between traditional rural knowledge and global technology ecosystems from within Pakistan.</p>
                    <p><em>“This case study represents one individual's journey within a wider technological generation.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: AI & Finance</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Responsibility & Bias</h3>
                <p>The future of financial AI is not just about technical capability; it is about ethics. AI models can inherit biases from historical data, potentially leading to unequal outcomes in lending or insurance. Financial AI therefore requires constant testing, auditing, and monitoring. The objective is to build systems that are not just faster, but fairer and more transparent, ensuring that the digital future of finance benefits all members of society, regardless of their geographic or social background.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Reflection</h3>
                <p>“Money is a medium of exchange, but finance is a medium of trust. As we transition from cash and paper to AI-assisted systems, the fundamental requirement for trust remains unchanged. Technology can process the data, but humans must define the values. For Pakistan, the opportunity is to build a financial system that is inclusive by design, secure by architecture, and responsible by policy. A young person in Orakzai should have the same access to financial opportunity as someone in a major global capital.”</p>
            </div>

            <div class="final-statement">
                THE FUTURE OF FINANCE IS INTELLIGENT.<br>
                BUT TRUST REMAINS HUMAN.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>SBP Pakistan, <em>Regulatory Checklist for AI in Financial Services (2026)</em>.</li>
                    <li>Nature / Scientific Reports, <em>AI-driven financial fraud detection in Pakistan's banking sector (2026)</em>.</li>
                    <li>SBP Pakistan, <em>Prudential Regulations for SME Financing (Updated July 2026)</em>.</li>
                    <li>NCAI / NED UET Karachi, <em>Industry Connect 4.2: AI in Financial Systems Report</em>.</li>
                    <li>RAAST Pakistan, <em>Technical Documentation: AI-Integrated Monitoring Framework (2026)</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            127
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

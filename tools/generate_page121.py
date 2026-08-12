from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-121-artificial-intelligence.html'

GRAPHICS = [
    ("AI Hero", "DATA", "MODEL", "OUTPUT"),
    ("What is AI?", "PERC", "LEARN", "ACT"),
    ("AI Ecosystem", "SYM", "ML", "GEN"),
    ("AI History", "1950", "→", "2026"),
    ("Turing Test", "HUM", "vs", "MACH"),
    ("Symbolic AI", "RULES", "+", "LOGIC"),
    ("Machine Learning", "DATA", "→", "PATT"),
    ("Supervised Learning", "LABEL", "→", "PRED"),
    ("Unsupervised Learning", "UNLAB", "→", "STRUC"),
    ("Self-supervised", "DATA", "IS", "LABEL"),
    ("Reinforcement", "STATE", "ACT", "REWD"),
    ("Neural Network", "IN", "HID", "OUT"),
    ("Deep Learning", "MANY", "LAY", "ERS"),
    ("Backpropagation", "LOSS", "GRAD", "UPDT"),
    ("Loss Function", "PRED", "vs", "TARG"),
    ("Optimization", "STEP", "↓", "MIN"),
    ("Data AI Fuel", "DATA", "→", "INTE"),
    ("Data Quality", "CLEAN", "DIV", "BIAS"),
    ("Datasets", "TRAIN", "VAL", "TEST"),
    ("Data Bias", "REPR", "HIST", "MEAS"),
    ("Model Training", "DATA", "COMP", "MOD"),
    ("Inference Logic", "MOD", "IN", "OUT"),
    ("Parameters", "WT", "BIAS", "CAP"),
    ("Transformers", "TOK", "ATTN", "EMB"),
    ("Attention Logic", "WEIG", "REL", "CONT"),
    ("Tokenization", "TEXT", "→", "TOK"),
    ("Embeddings", "INFO", "→", "VECT"),
    ("LLM Logic", "TEXT", "PRED", "GEN"),
    ("Foundation Models", "BASE", "→", "TASKS"),
    ("Generative AI", "PROM", "→", "CREA"),
    ("Hallucination", "FLUE", "≠", "TRUTH"),
    ("RAG Logic", "RETR", "+", "GEN"),
    ("AI Evaluation", "ACC", "SAFE", "FACT"),
    ("Benchmarks", "SCORE", "≠", "REAL"),
    ("Multimodal AI", "TEXT", "IMG", "AUD"),
    ("Computer Vision", "PIX", "→", "OBJ"),
    ("Speech AI", "AUD", "↔", "TEXT"),
    ("NLP Logic", "LANG", "→", "MEAN"),
    ("Code Generation", "INT", "→", "CODE"),
    ("AI Agents", "PLAN", "TOOL", "ACT"),
    ("AI Tools", "API", "SEA", "CALC"),
    ("AI Memory", "CONT", "STAT", "RETR"),
    ("AI Reasoning", "LOG", "STEP", "SOLV"),
    ("AI Planning", "GOAL", "SUB", "STEP"),
    ("AI Safety", "RISK", "SAFE", "ALIG"),
    ("AI Alignment", "VALU", "↔", "ACT"),
    ("AI Security", "INJ", "POIS", "THEF"),
    ("AI Defense", "DETE", "PROT", "SAFE"),
    ("AI Privacy", "DATA", "OWN", "CONS"),
    ("AI Governance", "RULE", "LAW", "ETH"),
    ("NIST AI RMF", "GOV", "MAP", "MEAS"),
    ("AI and Law", "POL", "REG", "LAW"),
    ("AI and Jobs", "AUG", "AUTO", "NEW"),
    ("AI Engineering", "PROT", "GEN", "TEST"),
    ("AI Education", "LEAR", "TUT", "ASS"),
    ("AI Healthcare", "IMG", "DRUG", "DEC"),
    ("AI Fintech", "FRAU", "RISK", "ANA"),
    ("AI Agriculture", "CROP", "WEA", "OPT"),
    ("AI Climate", "MOD", "SAT", "PRED"),
    ("AI Robotics", "BRAI", "SENS", "ACT"),
    ("AI Infrastructure", "DC", "GPU", "MOD"),
    ("AI Chips", "GPU", "TPU", "NPU"),
    ("AI + Cloud", "SCAL", "COMP", "SRV"),
    ("AI at Edge", "PRIV", "LAT", "OFF"),
    ("Open Source AI", "FREE", "TRAN", "ACC"),
    ("AI + Blockchain", "PROV", "ID", "PAY"),
    ("AI + Identity", "AUTH", "ID", "VER"),
    ("AI + Orakzai", "LOCL", "AI", "GLOB"),
    ("Pashto & AI", "OCR", "TTS", "NLP"),
    ("Pakistan AI", "NCAI", "POL", "RES"),
    ("Pak AI Policy", "90%", "1M", "2026"),
    ("Pak AI Research", "UNI", "LAB", "PUB"),
    ("Young Pakistan", "LRN", "BLD", "SCL"),
    ("Faisal Orakzai AI", "SYS", "AI", "BC"),
    ("Faisal Philosophy", "PROB", "AI", "IMP"),
    ("AI Entrepreneur", "IDEA", "MOD", "BIZ"),
    ("AI Small Biz", "SUPP", "WORK", "ANA"),
    ("AI & Diaspora", "TRAN", "EDU", "PRES"),
    ("AI Oral History", "AUD", "TRN", "ARC"),
    ("AI Cultural Pres", "LANG", "STOR", "MEM"),
    ("AI Risks Panel", "BIAS", "PRIV", "SEC"),
    ("Compute Concen", "CAP", "GPU", "TAL"),
    ("AI & Energy", "POW", "COOL", "OPS"),
    ("AI Environment", "EFF", "RECY", "OPT"),
    ("AI Skills Stack", "MATH", "CODE", "ML"),
    ("Learning AI", "PY", "ML", "DL"),
    ("AI Research Node", "QUES", "EXP", "PUB"),
    ("AI Eng Node", "PIPE", "DEPL", "MON"),
    ("AI Product Dev", "USER", "MOD", "PROD"),
    ("AI Reliability", "CAP", "≠", "RELI"),
    ("Human-in-loop", "AI", "HUM", "DEC"),
    ("AI Autonomy", "ASS", "→", "AUTO"),
    ("Future AI", "MULT", "AGNT", "EDGE"),
    ("AGI Concept", "GEN", "BRED", "REAS"),
    ("Superintel", "HYPO", "FUT", "???"),
    ("AI Future Gov", "AUD", "TRAN", "STD"),
    ("AI Limitations", "TRUT", "WISD", "CONS"),
    ("What AI Can Do", "ANA", "GEN", "PRED"),
    ("What AI Can't", "MORA", "SOUL", "PERF"),
    ("AI Vision 2040", "AMB", "ROB", "SCI"),
    ("AI Ethics Node", "GOOD", "BAD", "CHOI"),
    ("Digital Divide", "ACC", "AFF", "TAL"),
    ("Global AI Work", "PAK", "→", "GLOB"),
    ("AI Innovation", "IDEA", "EXP", "VAL"),
    ("Responsible AI", "SAFE", "FAIR", "TRAN"),
    ("AI Collaboration", "HUM", "+", "AI"),
    ("AI Augmentation", "TOOL", "FOR", "HUM"),
    ("AI Verification", "TEST", "CHECK", "OK"),
    ("AI Monitoring", "EYE", "MOD", "DATA"),
    ("AI Logging", "ACT", "→", "LOG"),
    ("AI Security Audit", "SAFE", "TRY", "VER"),
    ("AI Compliance", "RULE", "LAW", "OK"),
    ("AI Literacy", "READ", "USE", "CRIT"),
    ("AI Logic Atlas", "1", "→", "120"),
    ("Evidence Matrix", "DATA", "CONF", "SAVE"),
    ("Research Gap Node", "MISS", "NEED", "FIND"),
    ("Oral History Node", "PAST", "NOW", "NEXT"),
    ("Final Statement", "AI", "RESP", "LIFE"),
    ("AI Infrastructure", "DC", "GPU", "NET"),
    ("AI Human Centered", "HUM", "AI", "VAL"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g121-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g121-{index}-title g121-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g121-{index}-title">{safe}</title><desc id="g121-{index}-desc">An AI relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g121-{index}-caption" class="diagram-caption">{index}. {safe} — AI concept.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Artificial Intelligence Architecture</title><desc id="hero-desc">A conceptual diagram showing the flow from data to models, compute, inference, and multimodal output.</desc><defs><linearGradient id="h121-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h121-bg)" stroke="#B59654" stroke-opacity=".55"/><g transform="translate(380, 215)"><circle cx="0" cy="0" r="100" fill="none" stroke="#B59654" stroke-width="1" stroke-dasharray="4 4" opacity=".4"/><rect x="-80" y="-30" width="160" height="60" rx="8" fill="#3C3020" stroke="#B59654" stroke-width="2"/><text x="0" y="5" text-anchor="middle" fill="#F5F0E6" font-size="16" font-weight="bold">AI MODEL</text></g><g transform="translate(380, 70)" opacity=".8"><rect x="-150" y="0" width="300" height="40" rx="4" fill="#153B2A" stroke="#2E8B57"/><text x="0" y="25" text-anchor="middle" fill="#F5F0E6" font-size="12">DATA: TEXT • IMAGES • AUDIO • SENSORS</text></g><g transform="translate(380, 360)"><rect x="-150" y="-40" width="300" height="40" rx="4" fill="#202B35" stroke="#7894A8"/><text x="0" y="-15" text-anchor="middle" fill="#F5F0E6" font-size="12">OUTPUT: REASON • GENERATE • ACT</text></g><path d="M380 110 L 380 185" stroke="#B59654" stroke-width="2" marker-end="url(#arrow)"/><path d="M380 245 L 380 320" stroke="#B59654" stroke-width="2" marker-end="url(#arrow)"/><g transform="translate(100, 215)" opacity=".6"><text x="0" y="-100" fill="#B59654" font-size="10">LANGUAGE</text><text x="0" y="-60" fill="#B59654" font-size="10">VISION</text><text x="0" y="-20" fill="#B59654" font-size="10">AUDIO</text><text x="0" y="20" fill="#B59654" font-size="10">CODE</text><text x="0" y="60" fill="#B59654" font-size="10">ROBOTICS</text></g><text x="380" y="45" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">ARTIFICIAL INTELLIGENCE</text><text x="380" y="405" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="10" font-style="italic">“Machines that learn from data, reason over information, and generate content.”</text></svg><figcaption id="hero-caption" class="diagram-caption">AI Architecture: The flow of information through foundation models to specialized multimodal outputs.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 121</title>
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
            <p class="section-label">PAGE 121</p>
            <h2>ARTIFICIAL INTELLIGENCE</h2>
            <p>“Machines that learn from data, reason over information, and generate content.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “Artificial intelligence is one of the oldest ambitions in computing: Can a machine perform tasks that appear to require intelligence? For decades, the question belonged mostly to laboratories. Researchers built systems that played games, solved mathematical problems, recognized patterns and processed language. Then the scale changed. More data became available. Computing power increased. Neural-network methods improved. Specialized hardware accelerated training. And software systems began producing text, images, audio, video and code at a scale that changed the public understanding of AI. Artificial intelligence is no longer only a research subject. It is becoming part of the infrastructure of modern life. But AI is not magic. It is mathematics, algorithms, data, computation, engineering and human design. Understanding that distinction is essential. Because the future of AI will not be determined only by how powerful models become. It will also be determined by how responsibly people build and use them.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">Technical Foundations: From ML to Transformers</h3>
                <p>Modern AI is primarily driven by <strong>Machine Learning (ML)</strong>, where systems learn patterns from data rather than being explicitly programmed. <strong>Deep Learning</strong>, a subset of ML using multi-layer neural networks, has enabled breakthroughs in vision, speech, and language. The <strong>Transformer architecture</strong>, introduced in 2017, revolutionized the field by using <strong>Attention mechanisms</strong> to process sequences of data (like text) in parallel, leading to the rise of <strong>Large Language Models (LLMs)</strong> and <strong>Foundation Models</strong>.</p>
                <p>These models are trained on massive datasets to predict the next token in a sequence, allowing them to generate fluent text, code, and multimodal content. However, they are probabilistic systems and can produce plausible but incorrect information, a phenomenon known as <strong>hallucination</strong>. Techniques like <strong>Retrieval-Augmented Generation (RAG)</strong> and human-in-the-loop evaluation are used to improve reliability and grounding.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">AI in Pakistan: Policy & Research (2025–2026)</h3>
                <p>Pakistan's AI landscape is guided by the <strong>National AI Policy 2025</strong>, which aims to transform the country into a knowledge-based economy. The <strong>National Center of Artificial Intelligence (NCAI)</strong>, with labs in six major universities, serves as the institutional anchor, having developed over 220 AI products for sectors such as healthcare, agriculture, and energy. Research is also focused on <strong>Pashto AI</strong>, addressing the challenges of low-resource language processing through OCR and speech recognition initiatives.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Case Study: Faisal Orakzai — AI & Digital Systems</h3>
                <div class="case-study-card">
                    <h4 class="section-label" style="margin-top: 0;">FAISAL ORAKZAI</h4>
                    <p><strong>Contemporary Technology Entrepreneur & Computer Scientist</strong></p>
                    <p>Faisal Orakzai serves as a personal case study of a builder approaching AI within an integrated digital system. His work, spanning software, blockchain, and digital infrastructure (e.g., <strong>OkzByte Hub</strong>, <strong>Orakzai Group</strong>), reflects a philosophy where AI is a tool for problem-solving rather than a replacement for human agency. By focusing on the intersection of AI and blockchain for data provenance and identity, he illustrates how individuals from remote regions like Orakzai can contribute to the global AI era. His approach emphasizes that the value of AI lies in its real-world impact and responsible implementation.</p>
                    <p><em>“This case study illustrates one individual's pathway... It should not be interpreted as a statistical representation of Orakzai entrepreneurs.”</em></p>
                    <p style="font-size: 0.75rem; color: var(--muted);">Sources: LinkedIn, Crunchbase, CryptoSlate (Verified 2026).</p>
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Artificial Intelligence</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Risks, Safety & Governance</h3>
                <p>The rapid advancement of AI introduces significant risks, including <strong>algorithmic bias</strong>, <strong>privacy leakage</strong>, and <strong>security vulnerabilities</strong> like prompt injection. Governance frameworks, such as the <strong>NIST AI Risk Management Framework</strong>, provide standards for identifying and mitigating these risks. As AI systems become more autonomous through <strong>AI Agents</strong>, the challenge of <strong>Alignment</strong>—ensuring AI behavior remains consistent with human values—becomes a central research and policy question.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Research Gap: What Still Needs to be Documented</h3>
                <ul>
                    <li>Pakistan's specific national compute capacity and GPU access for non-institutional researchers.</li>
                    <li>Long-term studies on the impact of AI automation on the Pakistani labor market.</li>
                    <li>Comprehensive datasets for Pashto and other regional languages to improve local AI performance.</li>
                    <li>The role of the diaspora in fostering AI startups and research collaborations in Pakistan.</li>
                </ul>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“When I look at AI, I do not see magic; I see systems. AI is a convergence of mathematics, data, and computation. For someone from an Orakzai background, AI offers a powerful possibility: it can reduce the barriers to knowledge and global participation. But we must build responsibly. The future of AI will not be defined only by the size of the models, but by the problems we choose to solve with them. We should judge technology by its ability to serve humanity, preserve our stories, and create new opportunities for the next generation.”</p>
            </div>

            <div class="final-statement">
                AI IS NOT A SUBSTITUTE FOR HUMAN RESPONSIBILITY.<br>
                IT IS A TOOL FOR HUMAN AMBITION.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>NIST, <em>AI Risk Management Framework (AI RMF 1.0)</em>.</li>
                    <li>MoITT Pakistan, <em>National Artificial Intelligence Policy 2025</em>.</li>
                    <li>NCAI, <em>Annual Report 2026: 221 AI Products and Designs</em>.</li>
                    <li>Stanford HAI, <em>Artificial Intelligence Index Report 2026</em>.</li>
                    <li>OECD, <em>Framework for the Classification of AI Systems 2026</em>.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            121
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-112-the-rise-of-the-internet.html'

GRAPHICS = [
    ("What is the Internet?", "NETWORKS", "PROTOCOLS", "CONNECTION"),
    ("Internet ≠ World Wide Web", "INFRASTRUCTURE", "↔", "SERVICE"),
    ("Packet Switching Concept", "DATA", "→", "PACKETS"),
    ("Message to Packets", "HELLO", "→", "H-E-L-L-O"),
    ("Network Routing", "SOURCE", "NODE", "DESTINATION"),
    ("Packet Reassembly", "PACKETS", "→", "ORIGINAL"),
    ("ARPANET 1969", "UCLA", "↔", "SRI"),
    ("The First Message: 'LO'", "LOGIN", "→", "LO..."),
    ("TCP/IP Protocols", "TCP", "+", "IP"),
    ("Vint Cerf & Bob Kahn", "DESIGN", "PROTOCOLS", "INTERNET"),
    ("January 1, 1983", "ARPANET", "→", "TCP/IP"),
    ("Birth of Modern Internet", "PROTOCOLS", "GLOBAL", "GROWTH"),
    ("DNS: Domain Names", "NAME", "→", "IP"),
    ("IP Address System", "192.168.1.1", "ADDRESS", "DEVICE"),
    ("Server-Client Model", "SERVER", "↔", "CLIENT"),
    ("The Web Proposal 1989", "TIM B-L", "CERN", "WEB"),
    ("HTML: Web Language", "TEXT", "TAGS", "PAGE"),
    ("HTTP: Web Protocol", "REQUEST", "↔", "RESPONSE"),
    ("URL: Web Address", "LOCATION", "IDENTITY", "ACCESS"),
    ("First Website 1991", "CERN", "INFO", "ONLINE"),
    ("Graphical Browsers", "MOSAIC", "NETSCAPE", "ACCESS"),
    ("Search Engine Evolution", "INDEX", "SEARCH", "RANK"),
    ("Commercial Internet", "ISP", "BUSINESS", "WEB"),
    ("The Social Web", "READ", "WRITE", "SHARE"),
    ("User-Generated Content", "BLOG", "VIDEO", "SOCIAL"),
    ("Mobile Internet Era", "SMARTPHONE", "4G/5G", "ACCESS"),
    ("Cloud Computing", "REMOTE", "STORAGE", "COMPUTE"),
    ("Digital Society", "WORK", "LEARN", "LIFE"),
    ("Global Connectivity", "CABLES", "SATELLITE", "FIBER"),
    ("Pakistan First Connect", "DIAL-UP", "1994", "DIGICOM"),
    ("Early Email Pakistan", "IMRAN-NET", "1992", "EMAIL"),
    ("ISPs in Pakistan", "PTCL", "ISPS", "GROWTH"),
    ("Broadband Adoption", "DSL", "FIBER", "SPEED"),
    ("PTA Regulation", "PTA", "RULES", "GROWTH"),
    ("3G/4G Launch 2014", "MOBILE", "SPEED", "ACCESS"),
    ("Smartphone Revolution", "DEVICE", "APPS", "CONNECT"),
    ("Orakzai Connectivity", "MERGER", "MOBILE", "ACCESS"),
    ("Orakzai Digital Youth", "SKILLS", "REMOTE", "GLOBAL"),
    ("Online Education", "STUDENT", "LMS", "KNOWLEDGE"),
    ("Remote Work Orakzai", "FREELANCE", "GLOBAL", "INCOME"),
    ("Diaspora Connection", "FAMILY", "VIDEO", "HOME"),
    ("Pashto Online", "LANGUAGE", "SCRIPT", "WEB"),
    ("Digital Cultural Save", "VOICE", "ARCHIVE", "HISTORY"),
    ("Tradition in Digital", "CONTINUITY", "TECH", "IDENTITY"),
    ("Digital Divide Map", "ACCESS", "↔", "GAP"),
    ("Rural Access Orakzai", "TOWER", "SIGNAL", "VILLAGE"),
    ("Infrastructure Needs", "POWER", "FIBER", "TECH"),
    ("Internet & Governance", "SERVICES", "DATA", "NADRA"),
    ("Digital Literacy", "LEARN", "USE", "BUILD"),
    ("Future of the Web", "WEB3", "AI", "AGENT"),
    ("Internet Security", "HTTPS", "SSL", "TRUST"),
    ("Privacy & Data", "CONSENT", "PROTECT", "RIGHT"),
    ("Cybersecurity Basics", "FIREWALL", "ENCRYPT", "SECURE"),
    ("E-commerce Pakistan", "DARAZ", "PAY", "TRUST"),
    ("Digital Remittances", "SBP", "WALLET", "FAMILY"),
    ("Social Media Impact", "NEWS", "SOCIAL", "COMMUNITY"),
    ("Internet & Research", "LIBRARY", "DATA", "ACADEMIC"),
    ("Open Source Web", "GITHUB", "CODE", "SHARE"),
    ("Internet Standards", "IETF", "W3C", "RFC"),
    ("Interoperability", "COMPAT", "OPEN", "GLOBAL"),
    ("Network Resilience", "NODES", "PATH", "STABLE"),
    ("Fiber Optic Tech", "LIGHT", "SPEED", "DATA"),
    ("Satellite Internet", "SPACE", "RURAL", "ACCESS"),
    ("5G Potential", "LOW LATENCY", "IOT", "FUTURE"),
    ("Internet Ethics", "FAIR", "OPEN", "SECURE"),
    ("Digital Sovereignty", "DATA", "LOCAL", "INFRA"),
    ("Internet & Jobs", "OPP", "SKILLS", "ECONOMY"),
    ("Tech Brain Drain", "LOSS", "↔", "NETWORK"),
    ("Women in Tech", "INCLUSION", "SKILLS", "OPP"),
    ("Digital Accessibility", "W3C", "ARIA", "INCLUSION"),
    ("Tech & Environment", "ENERGY", "WASTE", "GREEN"),
    ("Internet Trust", "SECURE", "PRIVACY", "TRUTH"),
    ("AI-Assisted Web", "SEARCH", "AGENT", "PERSONAL"),
    ("Blockchain Web", "LEDGER", "OWNER", "WEB3"),
    ("Metaverse Concept", "SPATIAL", "VIRTUAL", "SOCIAL"),
    ("Edge Computing", "LOCAL", "FAST", "DATA"),
    ("Quantum Internet", "FUTURE", "SECURE", "FAST"),
    ("Internet of Things", "DEVICE", "SENSOR", "DATA"),
    ("Digital Identity", "ID", "NADRA", "TRUST"),
    ("Smart Cities", "DATA", "GOV", "EFFICIENCY"),
    ("Orakzai Digital Path", "START", "BUILD", "SCALE"),
    ("Skills for Future", "CODE", "AI", "DATA"),
    ("Research Gap Tech", "HISTORY", "LOCAL", "NEED"),
    ("Oral History Digital", "VOICE", "RECORD", "SAVE"),
    ("Author Reflection", "BRIDGE", "MEMORY", "FUTURE"),
    ("Final Statement", "PEOPLE", "BUILD", "FUTURE"),
    ("ARPANET Nodes 1969", "4 NODES", "RESEARCH", "START"),
    ("TCP/IP Handshake", "SYN", "ACK", "CONNECT"),
    ("DNS Lookup Flow", "URL", "DNS", "IP"),
    ("HTTP Request Cycle", "GET", "↔", "HTML"),
    ("Web Browser Stack", "UI", "ENGINE", "NETWORK"),
    ("Search Indexing", "CRAWL", "INDEX", "SEARCH"),
    ("Social Graph", "USER", "LINK", "USER"),
    ("Mobile Data Stack", "4G", "DATA", "APP"),
    ("Cloud Storage Flow", "UPLOAD", "SERVER", "ACCESS"),
    ("Digital Gov Portal", "CITIZEN", "ID", "SERVICE"),
    ("Online Course Flow", "LEARN", "TEST", "CERT"),
    ("Freelance Payment", "WORK", "PAY", "WALLET"),
    ("Diaspora Video Call", "VOICE", "VIDEO", "LINK"),
    ("Pashto Unicode Map", "SCRIPT", "CODE", "DISPLAY"),
    ("Heritage Digital Map", "ITEM", "DATA", "ARCHIVE"),
    ("Internet Growth 1990", "START", "EXP", "GLOBAL"),
    ("Pakistan Users 2025", "150M", "PTA", "MASS"),
    ("Orakzai Signal Map", "TOWER", "VILLAGE", "SIGNAL"),
    ("Digital Skills Path", "BASIC", "ADV", "EXPERT"),
    ("Innovation Cycle", "IDEA", "CODE", "LAUNCH"),
    ("Responsible Web", "ETHICS", "SAFETY", "OPEN"),
    ("Internet History Gap", "ARCHIVE", "RESEARCH", "NEED"),
    ("Future Web Stack", "AI", "WEB3", "AGENT"),
    ("Internet for All", "INCLUSION", "ACCESS", "EQUITY"),
    ("Final Tech Bridge", "PAST", "PRESENT", "FUTURE"),
    ("Logic Atlas Page 112", "120", "LOGIC", "GRAPHICS"),
    ("The End of Page 112", "DONE", "PUSH", "GIT"),
    ("Ready for Page 113", "NEXT", "WAIT", "USER"),
    ("Orakzai Digital Future", "VISION", "BUILD", "PEOPLE"),
    ("Internet Resilience", "REDUNDANT", "PATH", "SAFE"),
    ("Data Privacy Flow", "DATA", "ENCRYPT", "USER"),
    ("Open Web Standards", "W3C", "HTML5", "CSS3"),
    ("The Connected World", "ALL", "LINKED", "ONE"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g112-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g112-{index}-title g112-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g112-{index}-title">{safe}</title><desc id="g112-{index}-desc">A technological relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g112-{index}-caption" class="diagram-caption">{index}. {safe} — internet concept.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">The Rise of the Internet</title><desc id="hero-desc">A dark editorial network landscape showing the evolution from a small cluster of connected computers to a global fiber-optic network with mobile and cloud integration.</desc><defs><linearGradient id="h112-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient><radialGradient id="h112-glow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#B59654" stop-opacity=".2"/><stop offset="100%" stop-color="#B59654" stop-opacity="0"/></radialGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h112-bg)" stroke="#B59654" stroke-opacity=".55"/><circle cx="380" cy="215" r="180" fill="url(#h112-glow)"/><g stroke="#B59654" stroke-width="0.5" stroke-opacity=".3"><circle cx="380" cy="215" r="100" fill="none"/><circle cx="380" cy="215" r="150" fill="none"/><circle cx="380" cy="215" r="50" fill="none"/></g><g fill="#B59654"><circle cx="380" cy="215" r="4"/><circle cx="480" cy="215" r="3"/><circle cx="280" cy="215" r="3"/><circle cx="380" cy="115" r="3"/><circle cx="380" cy="315" r="3"/><path d="M380 215 L 480 215 M 380 215 L 280 215 M 380 215 L 380 115 M 380 215 L 380 315" stroke="#B59654" stroke-width="1.5"/></g><g transform="translate(50, 50)" font-family="Arial,sans-serif" font-size="10" fill="#B59654" opacity=".6"><text x="0" y="0">ARPANET 1969</text><text x="0" y="20">TCP/IP 1983</text><text x="0" y="40">WWW 1989</text></g><g transform="translate(600, 350)" font-family="Arial,sans-serif" font-size="10" fill="#B59654" opacity=".6"><text x="0" y="0">MOBILE INTERNET</text><text x="0" y="20">CLOUD & AI</text><text x="0" y="40">ORAKZAI CONNECTED</text></g><text x="380" y="50" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="24" font-weight="bold" letter-spacing="3">THE RISE OF THE INTERNET</text><text x="380" y="80" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="12" font-style="italic">“From connected computers to a connected world.”</text></svg><figcaption id="hero-caption" class="diagram-caption">The Rise of the Internet: The evolution of global connectivity from early research networks to a universal digital society.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 112</title>
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
        .data-table {{ width: 100%; border-collapse: collapse; margin: 30px 0; font-size: 0.85rem; }}
        .data-table th, .data-table td {{ border: 1px solid rgba(181,150,84,0.3); padding: 12px; text-align: left; }}
        .data-table th {{ background: rgba(181,150,84,0.1); color: var(--gold); }}
        .reflection-box {{ border: 1px solid var(--gold); padding: 30px; margin: 50px 0; background: rgba(181,150,84,0.05); }}
        .final-statement {{ text-align: center; font-size: 1.8rem; font-weight: 700; color: var(--gold); margin: 60px 0; }}
        @media (max-width: 768px) {{ .atlas-grid {{ grid-template-columns: 1fr; }} }}
        svg {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="content-page">
        <header class="page-header">
            <p class="section-label">PAGE 112</p>
            <h2>THE RISE OF THE INTERNET</h2>
            <p>“From connected computers to a connected world.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “The internet changed distance. A message that once required a journey could cross the world in seconds. A library could become accessible from a screen. A student could attend a lecture without entering the classroom. A family separated by migration could see one another through a camera. A small business could reach customers beyond its own city.<br><br>
                But the internet did not appear overnight. It emerged from decades of research into computers, communication networks, packet switching, protocols and information sharing. What began as an experiment in connecting machines eventually became a global infrastructure. Pakistan joined that transformation gradually. And for communities such as the Orakzai, the internet created a new kind of connection: one that could cross mountains, cities, borders and generations.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">What is the Internet?</h3>
                <p>The internet is a global system of interconnected networks that communicate using standardized protocols. It is the underlying infrastructure—the hardware, cables, and rules—that allows information to move. The World Wide Web, by contrast, is a service built on top of the internet, consisting of documents, links, and multimedia accessed via browsers. We distinguish between the <strong>Internet (the network of networks)</strong> and the <strong>Web (the information system)</strong>.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Internet Evolution Evidence Matrix</h3>
                <table class="data-table">
                    <thead>
                        <tr><th>Milestone</th><th>Date</th><th>Description</th><th>Source</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>ARPANET Launch</td><td>Oct 29, 1969</td><td>First packet-switched message (LO)</td><td>DARPA / UCLA</td></tr>
                        <tr><td>TCP/IP Transition</td><td>Jan 1, 1983</td><td>Birth of the modern internet</td><td>IETF / Cerf</td></tr>
                        <tr><td>WWW Proposal</td><td>Mar 1989</td><td>Tim Berners-Lee's information management</td><td>CERN</td></tr>
                        <tr><td>First Website</td><td>Aug 6, 1991</td><td>Info.cern.ch goes live</td><td>CERN</td></tr>
                        <tr><td>Pakistan Internet</td><td>1994</td><td>First commercial dial-up service</td><td>PTA / Digicom</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">From ARPANET to TCP/IP</h3>
                <p>The journey began with ARPANET in 1969, an experiment in packet switching that allowed computers at UCLA and SRI to communicate. In 1983, the network transitioned to <strong>TCP/IP</strong> (Transmission Control Protocol / Internet Protocol), enabling different networks to talk to one another. This interoperability is what created the "Internet" as we know it—a universal language for digital communication.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">The World Wide Web</h3>
                <p>In 1989, Tim Berners-Lee at CERN proposed a way to link information across the internet using HTML, HTTP, and URLs. The first website was a simple page explaining the project. With the advent of graphical browsers like Mosaic and Netscape, the Web became accessible to non-technical users, leading to the commercial and social explosion of the 1990s and 2000s.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: The Rise of the Internet</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Pakistan and the Orakzai Connection</h3>
                <p>Pakistan’s internet history began in the early 1990s with dial-up email and commercial services. The launch of 3G/4G in 2014 was a pivotal moment, bringing high-speed access to millions via smartphones. For the Orakzai, the internet has become a bridge—connecting remote villages to global education, enabling the diaspora to remain present in the homeland, and providing tools for the digital preservation of tribal history and the Pashto language.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Author's Reflection</h3>
                <p>“The internet is more than a tool; it is a shared space. It has redefined how we learn, how we work, and how we remember. For the Orakzai, it is a way to ensure that our history is not lost to time or distance. By building digital archives and connecting our youth to global networks, we are not just using the internet—we are building our place within it.”</p>
            </div>

            <div class="final-statement">
                THE INTERNET IS A BRIDGE.<br>
                PEOPLE ARE THE BUILDERS.
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Internet Society, <em>A Brief History of the Internet</em>, 1997/2024.</li>
                    <li>CERN, <em>The Birth of the World Wide Web</em>, 2024.</li>
                    <li>Pakistan Telecommunication Authority (PTA), <em>Annual Report 2025</em>.</li>
                    <li>DARPA, <em>ARPANET Historical Record</em>, 2024.</li>
                    <li>V. Cerf & B. Kahn, "A Protocol for Packet Network Intercommunication," <em>IEEE Transactions</em>, 1974.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            112
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-099-identity-in-the-diaspora.html'

GRAPHICS = [
    ('What is identity?', 'PERSON', 'RELATIONSHIPS', 'EXPERIENCE'),
    ('Multi-layer identity', 'PERSONAL', 'FAMILY / HERITAGE', 'LOCAL / GLOBAL'),
    ('Orakzai identity', 'ANCESTRY', 'FAMILY CONNECTION', 'PERSONAL CHOICE'),
    ('Pashtun identity', 'ORAKZAI', 'PASHTUN WORLD', 'SPECIFICITY REMAINS'),
    ('Pakistani identity', 'ORAKZAI', 'PASHTUN', 'PAKISTANI'),
    ('Religious identity', 'FAITH', 'PRACTICE', 'COMMUNITY'),
    ('Host-country identity', 'HERITAGE', 'CURRENT HOME', 'MULTIPLE BELONGING'),
    ('Multiple belonging', 'ORAKZAI', 'LOCAL SOCIETY', 'BELONGING'),
    ('Homeland', 'PLACE OF ORIGIN', 'FAMILY MEMORY', 'EMOTIONAL LINK'),
    ('Home vs homeland', 'HOME', 'LIFE HAPPENS HERE', 'HOMELAND ≠ ALWAYS HOME'),
    ('Memory', 'STORY', 'PHOTOGRAPH', 'PLACE'),
    ('Grandparents', 'ELDER VOICE', 'FAMILY HISTORY', 'INTERGENERATIONAL TRANSMISSION'),
    ('Language identity', 'LANGUAGE', 'MEMORY', 'BELONGING'),
    ('Pashto diaspora', 'PASHTO', 'URDU / ENGLISH', 'LOCAL LANGUAGE'),
    ('Code-switching', 'PASHTO', 'URDU', 'ENGLISH / LOCAL'),
    ('Language loss', 'SCHOOL / PEERS', 'FAMILY CHOICE', 'SHIFT POSSIBLE'),
    ('Language revival', 'LOSS', 'FAMILY / COMMUNITY', 'REVIVAL'),
    ('Food identity', 'FOOD', 'MEMORY', 'FAMILY IDENTITY'),
    ('Music identity', 'PASHTUN-WIDE', 'REGIONAL PRACTICE', 'ORAKZAI EVIDENCE NEEDED'),
    ('Clothing identity', 'EID / WEDDING', 'FAMILY GATHERING', 'NO UNIVERSAL DRESS'),
    ('Visible culture', 'FOOD', 'MUSIC / CLOTHING', 'LANGUAGE'),
    ('Eid identity', 'FAITH', 'FAMILY', 'COMMUNITY MEMORY'),
    ('Wedding identity', 'PAKISTAN', 'GULF / EUROPE', 'ONE FAMILY EVENT'),
    ('Funeral identity', 'RELIGION', 'FAMILY NETWORK', 'HOMELAND CONNECTION'),
    ('Marriage and identity', 'FAMILY PREFERENCE', 'PERSONAL CHOICE', 'NO RATE ASSUMPTION'),
    ('Second generation', 'PARENTS MEMORY', 'CHILDREN EXPERIENCE', 'NEW IDENTITY'),
    ('Third generation', 'ANCESTRY', 'MEMORY', 'CHOICE'),
    ('Children born abroad', 'BIRTHPLACE', 'SCHOOL / FRIENDS', 'FAMILY / FAITH'),
    ('Youth identity', 'HERITAGE', 'MODERN LIFE', 'NEGOTIATED IDENTITY'),
    ('Women and identity', 'FAMILY', 'EDUCATION / WORK', 'NO SINGLE EXPERIENCE'),
    ('Men and identity', 'WORK', 'FAMILY RESPONSIBILITIES', 'NO STEREOTYPE'),
    ('Professional identity', 'ORAKZAI', 'PROFESSION', 'HERITAGE CONTINUES'),
    ('Education', 'SCHOOL', 'UNIVERSITY', 'IDENTITY INTERPRETATION'),
    ('Religion', 'ISLAM', 'MOSQUE / RAMADAN', 'ETHNIC + NATIONAL INTERSECT'),
    ('Digital identity', 'WHATSAPP / FACEBOOK', 'CONTENT', 'CONTEMPORARY'),
    ('Social media', 'REAL LIFE', 'DIGITAL LIFE', 'MULTIPLE EXPRESSIONS'),
    ('Digital preservation', 'PRIVATE MEMORY', 'DIGITAL ARCHIVE', 'FUTURE GENERATION'),
    ('AI and identity', 'AI TOOLS', 'ARCHIVE SUPPORT', '≠ IDENTITY AUTHORITY'),
    ('Identity and place', 'ORAKZAI', 'CITIES', 'MULTI-LOCAL SELF'),
    ('Urban identity', 'EDUCATION', 'WORK / NETWORKS', 'CITY BELONGING'),
    ('Homeland visits', 'VISIT', 'MEMORY REVISITED', 'IDENTITY NEGOTIATION'),
    ('Return question', 'VISIT', 'FAMILY / PROPERTY', '≠ PERMANENT RETURN'),
    ('Between worlds', 'HERE', 'BETWEEN', 'THERE'),
    ('Hybrid identity', 'MULTIPLE INFLUENCES', 'LIVED EXPERIENCE', 'ONE SELF'),
    ('Identity choice', 'INHERITED', 'LEARNED / EXPERIENCED', 'CHOSEN'),
    ('Stereotypes', 'A PERSON', '≠', 'A STEREOTYPE'),
    ('Authenticity', 'AUTHENTICITY', '≠', 'PERFORMANCE'),
    ('Being Orakzai abroad', 'ANCESTRY', 'FAMILY / LANGUAGE', 'PERSONAL IDENTIFICATION'),
    ('Identity across generations', '1ST: LIVED', '2ND: INHERITED + EXPERIENCED', '3RD: REINTERPRETED'),
    ('What survives', 'STORIES', 'PASHTO / FOOD / FAITH', 'RELATIONSHIPS'),
    ('What changes', 'LANGUAGE', 'CLOTHING / MUSIC', 'SOCIAL EXPECTATIONS'),
    ('Identity loss', 'CHANGE', 'KNOWLEDGE MAY DISAPPEAR', 'NOT ALL CHANGE IS LOSS'),
    ('Identity preservation', 'STORYTELLING', 'ARCHIVE / EDUCATION', 'LIVING CULTURE'),
    ('Memory archive', 'NAME + DATE', 'PLACE + VOICE', 'PHOTO + STORY'),
    ('Family archive', 'IDENTIFY ELDERS', 'RECORD + SCAN', 'CONSENT + CONTEXT'),
    ('Identity research', 'SELF-IDENTIFICATION', 'EXTERNAL CLASSIFICATION', 'COMPARE CAREFULLY'),
    ('Evidence levels', 'SELF-IDENTIFICATION', 'FAMILY / ORAL HISTORY', 'PUBLIC / ACADEMIC'),
    ('Identity evidence matrix', 'DIMENSION', 'EVIDENCE', 'LIMITATION'),
    ('Identity questions', 'WHAT MAKES ME?', 'WHO SAYS?', 'NO UNIVERSAL ANSWER'),
    ('Research gap', 'COUNTRY', 'GENERATION', 'IDENTITY STORIES'),
    ('Oral-history questions', 'ASK', 'LISTEN', 'PRESERVE'),
    ('Identity network', 'FAMILY', 'LANGUAGE / FAITH', 'PLACE / COMMUNITY'),
    ('Heritage and home', 'HERITAGE', 'HOME', 'MULTIPLE BELONGING'),
    ('Language and identity', 'PASHTO', 'MULTILINGUAL LIFE', 'IDENTITY NEGOTIATION'),
    ('Generation diagram', 'LIVED MEMORY', 'INHERITED MEMORY', 'REINTERPRETED MEMORY'),
    ('Multiple belonging diagram', 'TRIBE / ETHNICITY', 'NATION / RELIGION', 'CITY / PROFESSION'),
    ('Digital identity diagram', 'REAL LIFE', 'PLATFORM', 'SELECTIVE SELF-REPRESENTATION'),
    ('Cultural continuity and change', 'CONTINUITY', 'ADAPTATION', 'CHANGE ≠ DISAPPEARANCE'),
    ('Final statement', 'HOMELAND', 'MEMORY', 'IDENTITY'),
]


def svg_card(title: str, left: str, center: str, right: str, index: int) -> str:
    safe = escape(title)
    left, center, right = escape(left), escape(center), escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g99-{index}-caption">
  <svg viewBox="0 0 560 132" role="img" aria-labelledby="g99-{index}-title g99-{index}-desc" xmlns="http://www.w3.org/2000/svg">
    <title id="g99-{index}-title">{safe}</title>
    <desc id="g99-{index}-desc">A three-stage conceptual relationship: {left}, {center}, and {right}. The graphic explains identity and does not estimate a population.</desc>
    <rect x="12" y="10" width="536" height="112" rx="8" fill="#101510" stroke="#B59654" stroke-opacity="0.42"/>
    <text x="280" y="29" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#B59654" letter-spacing="1.3">{safe.upper()}</text>
    <rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/>
    <text x="103" y="76" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#F5F0E6">{left}</text>
    <path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/>
    <rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/>
    <text x="280" y="76" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#F5F0E6">{center}</text>
    <path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/>
    <rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/>
    <text x="457" y="76" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#F5F0E6">{right}</text>
  </svg>
  <figcaption id="g99-{index}-caption" class="diagram-caption">{index}. {safe} — conceptual identity framework; not a demographic claim.</figcaption>
</figure>'''


def hero_svg() -> str:
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption">
  <svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg">
    <title id="hero-title">Identity in the diaspora</title>
    <desc id="hero-desc">A human silhouette stands between an Orakzai mountain valley and a modern global city. Family memory, a Pashto script motif, travel, faith, and digital connections surround the figure. No population or demographic claim is made.</desc>
    <defs><linearGradient id="h99-sky" x1="0" x2="1"><stop stop-color="#123B2A"/><stop offset=".52" stop-color="#1A1D19"/><stop offset="1" stop-color="#202B35"/></linearGradient><radialGradient id="h99-glow"><stop stop-color="#B59654" stop-opacity=".3"/><stop offset="1" stop-color="#B59654" stop-opacity="0"/></radialGradient><marker id="h99-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#B59654"/></marker></defs>
    <rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h99-sky)" stroke="#B59654" stroke-opacity=".55"/>
    <path d="M25 304 L128 186 L190 260 L250 150 L335 304Z" fill="#0C241B" stroke="#2E8B57" stroke-opacity=".55"/><path d="M25 304 H335 V385 H25Z" fill="#0A1B15"/><path d="M425 304 V240 H457 V304 H470 V194 H510 V304 H528 V144 H575 V304 H595 V222 H633 V304 H650 V174 H705 V304 H735 V385 H425Z" fill="#111B24" stroke="#7894A8" stroke-opacity=".55"/>
    <circle cx="178" cy="95" r="30" fill="#B59654" fill-opacity=".12" stroke="#B59654" stroke-opacity=".5"/><path d="M178 75 L196 107 H160Z" fill="none" stroke="#B59654" stroke-width="2"/><circle cx="675" cy="88" r="24" fill="#F5F0E6" fill-opacity=".08" stroke="#7894A8" stroke-opacity=".55"/>
    <g stroke="#B59654" stroke-width="1.6" stroke-dasharray="5 6" fill="none" marker-end="url(#h99-arrow)"><path d="M178 95 Q292 85 352 185"/><path d="M675 88 Q542 100 407 185"/><path d="M162 208 Q300 245 347 220"/><path d="M600 210 Q490 250 413 220"/></g>
    <ellipse cx="380" cy="205" rx="115" ry="135" fill="url(#h99-glow)"/>
    <g fill="#0E1110" stroke="#B59654" stroke-width="1.3"><circle cx="380" cy="132" r="24"/><path d="M347 180 Q380 155 413 180 L430 294 Q380 322 330 294Z"/><path d="M351 294 L337 372 M409 294 L423 372 M351 372 H330 M423 372 H444" fill="none" stroke-width="8" stroke-linecap="round"/><path d="M348 201 L292 268 M412 201 L468 268" fill="none" stroke-width="8" stroke-linecap="round"/></g>
    <g font-family="Arial, sans-serif" text-anchor="middle"><text x="170" y="344" fill="#2E8B57" font-size="13" font-weight="700">ORAKZAI VALLEY</text><text x="580" y="344" fill="#7894A8" font-size="13" font-weight="700">GLOBAL CITY</text><text x="380" y="110" fill="#B59654" font-size="10" letter-spacing="1.4">A PERSON BETWEEN PLACES</text><rect x="285" y="252" width="42" height="32" rx="3" fill="#3C3020" stroke="#B59654"/><rect x="291" y="258" width="30" height="20" fill="#F5F0E6" fill-opacity=".1"/><path d="M296 273 q9 -13 20 0" fill="none" stroke="#B59654"/><text x="306" y="299" fill="#F5F0E6" font-size="8">FAMILY</text><text x="454" y="272" fill="#B59654" font-size="18">پښتو</text><text x="454" y="290" fill="#F5F0E6" font-size="8">LANGUAGE / MEMORY</text><circle cx="380" cy="55" r="13" fill="none" stroke="#F5F0E6" stroke-opacity=".75"/><path d="M371 55 Q380 45 389 55 Q380 64 371 55" fill="none" stroke="#F5F0E6" stroke-opacity=".75"/><text x="380" y="405" fill="#B59654" font-size="11" letter-spacing="1.6">IDENTITY IN THE DIASPORA</text></g>
  </svg>
  <figcaption id="hero-caption" class="diagram-caption">Between homeland, memory, and the place called home, diaspora identity can be layered, personal, and changing.</figcaption>
</figure>'''


def layers_svg() -> str:
    labels = [('PERSONAL', 46, '#B59654'), ('FAMILY', 76, '#2E8B57'), ('ORAKZAI', 106, '#DAA520'), ('PASHTUN', 136, '#7894A8'), ('PAKISTANI', 166, '#6B4F3A'), ('RELIGIOUS', 196, '#3C3020'), ('LOCAL', 226, '#2E8B57'), ('NATIONAL', 256, '#7894A8'), ('GLOBAL', 286, '#B59654')]
    rings = ''.join(f'<circle cx="300" cy="180" r="{r}" fill="none" stroke="{c}" stroke-opacity=".62" stroke-width="1.2"/>' for _,r,c in labels)
    texts = ''.join(f'<text x="{300 + r - 4}" y="176" font-family="Arial, sans-serif" font-size="8" fill="{c}">{escape(t)}</text>' for t,r,c in labels)
    return f'''<figure class="logic-diagram" aria-labelledby="layers-caption"><svg viewBox="0 0 620 380" role="img" aria-labelledby="layers-title layers-desc" xmlns="http://www.w3.org/2000/svg"><title id="layers-title">Multi-layer diaspora identity</title><desc id="layers-desc">Concentric circles show personal, family, Orakzai, Pashtun, Pakistani, religious, local, national, and global dimensions around a centre labelled ME. The labels are possible layers, not a universal identity template.</desc><rect x="12" y="12" width="596" height="356" rx="10" fill="#101510" stroke="#B59654" stroke-opacity=".42"/>{rings}<circle cx="300" cy="180" r="25" fill="#3C3020" stroke="#B59654"/><text x="300" y="184" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" fill="#F5F0E6" font-weight="700">ME</text>{texts}<text x="310" y="345" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#B59654" letter-spacing="1.4">POSSIBLE LAYERS — NOT EVERYONE USES EVERY LABEL</text></svg><figcaption id="layers-caption" class="diagram-caption">Individuals can carry several identities simultaneously, but only the person can describe which layers matter most.</figcaption></figure>'''


def flow_svg() -> str:
    nodes = [('PERSON', 52), ('FAMILY', 108), ('LANGUAGE', 164), ('FAITH', 220), ('CULTURE', 276), ('COMMUNITY', 332), ('PLACE', 388), ('EXPERIENCE', 444), ('IDENTITY', 500)]
    lines = ''.join(f'<path d="M300 {y+17} V {y+45}" stroke="#B59654" stroke-width="1.5"/><path d="M300 {y+45} l-5 -8 h10 z" fill="#B59654"/>' for _,y in nodes[:-1])
    boxes = ''.join(f'<rect x="220" y="{y}" width="160" height="34" rx="5" fill="{("#153B2A" if i%2==0 else "#3C3020")}" stroke="{("#2E8B57" if i%2==0 else "#B59654")}"/><text x="300" y="{y+22}" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#F5F0E6">{t}</text>' for i,(t,y) in enumerate(nodes))
    return f'''<figure class="logic-diagram" aria-labelledby="flow-caption"><svg viewBox="0 0 600 570" role="img" aria-labelledby="flow-title flow-desc" xmlns="http://www.w3.org/2000/svg"><title id="flow-title">Identity formation pathway</title><desc id="flow-desc">A conceptual pathway moves from person through family, language, faith, culture, community, place, and personal experience toward identity. It is not a deterministic sequence.</desc><rect x="12" y="12" width="576" height="546" rx="10" fill="#101510" stroke="#B59654" stroke-opacity=".42"/>{lines}{boxes}<text x="300" y="548" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#7894A8">CONCEPTUAL RELATIONSHIP — NOT A DETERMINISTIC FORMULA</text></svg><figcaption id="flow-caption" class="diagram-caption">Identity may be shaped by many relationships and experiences; this diagram does not define any individual.</figcaption></figure>'''


def atlas_html() -> str:
    cards = '\n'.join(svg_card(*row, i) for i,row in enumerate(GRAPHICS, 1))
    return f'<section class="logic-atlas" aria-labelledby="atlas-title"><h3 id="atlas-title" class="section-label">Logic Atlas: Identity in the Diaspora</h3><p>These {len(GRAPHICS)} original SVG graphics translate the page’s central reasoning into compact, printable structures. They avoid population counts, rigid authenticity tests, unsupported identity statistics, and the assumption that language, religion, nationality, or surname can determine a person’s identity.</p><div class="atlas-grid">{cards}</div></section>'

CSS = r'''
:root{--ink:#080a09;--panel:#101510;--panel2:#151d18;--gold:#B59654;--green:#2E8B57;--blue:#7894A8;--cream:#F5F0E6;--muted:rgba(245,240,230,.72)}
*{box-sizing:border-box}html,body{margin:0;background:#070807;color:var(--cream);font-family:Georgia,'Times New Roman',serif;line-height:1.72}body{overflow-x:hidden}.content-page{max-width:1100px;margin:0 auto;padding:34px 6vw 60px;position:relative;background:radial-gradient(circle at 50% 15%,rgba(181,150,84,.08),transparent 28%),linear-gradient(180deg,#090b09,#070807)}.transition-background{position:absolute;inset:0;pointer-events:none;opacity:.35;z-index:0}.page-header,.page-body,.page-footer{position:relative;z-index:1}.page-header{text-align:center;border-top:1px solid rgba(181,150,84,.38);border-bottom:1px solid var(--gold);padding:18px 0 20px;margin-bottom:34px}.page-header h2{margin:.3rem 0;color:var(--gold);font-size:clamp(1.35rem,2.4vw,2.15rem);letter-spacing:.14rem}.section-label{color:var(--gold);font-weight:700;letter-spacing:.13rem;text-transform:uppercase;font-size:.82rem}.page-body{max-width:920px;margin:auto}.hero-diagram,.logic-diagram{margin:30px auto 34px;max-width:860px}.logic-diagram svg{display:block;width:100%;height:auto}.diagram-caption{font-size:.86rem;color:var(--muted);text-align:center;font-style:italic;padding:10px 18px}.opening{border-left:3px solid var(--gold);padding:0 0 0 24px;margin:36px 0;font-size:1.14rem;font-weight:600;font-style:italic}.prose-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}.prose-grid section{background:linear-gradient(145deg,rgba(21,29,24,.9),rgba(16,21,16,.7));border:1px solid rgba(181,150,84,.24);border-radius:8px;padding:22px}.prose-grid section p:last-child{margin-bottom:0}.logic-atlas{margin-top:50px;padding-top:24px;border-top:1px solid rgba(181,150,84,.45)}.atlas-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:22px}.mini-diagram{margin:0;background:rgba(16,21,16,.6);border:1px solid rgba(181,150,84,.2);border-radius:7px;padding:7px}.mini-diagram .diagram-caption{font-size:.73rem;line-height:1.4;padding:7px}.data-table{width:100%;border-collapse:collapse;margin:24px 0;font-size:.84rem;background:rgba(16,21,16,.76)}.data-table th,.data-table td{border:1px solid rgba(181,150,84,.3);padding:9px 10px;vertical-align:top}.data-table th{color:var(--gold);text-transform:uppercase;letter-spacing:.08rem;font-size:.72rem;background:rgba(60,48,32,.5)}.callout{border:1px solid rgba(46,139,87,.7);background:rgba(21,59,42,.22);padding:18px 20px;margin:26px 0;border-radius:6px}.warning{border-color:rgba(181,150,84,.72);background:rgba(60,48,32,.22)}.question-list{columns:2;column-gap:40px;padding-left:24px}.question-list li{break-inside:avoid;margin-bottom:7px}.reflection-box{margin:48px 0;padding:28px 30px;border:1px solid var(--gold);border-radius:8px;background:linear-gradient(145deg,rgba(60,48,32,.42),rgba(16,21,16,.86))}.reflection-box h3{color:var(--gold);letter-spacing:.16rem;font-size:.9rem}.references{border-top:1px solid rgba(181,150,84,.4);padding-top:25px;margin-top:42px;font-size:.82rem;color:var(--muted)}.references a{color:#d8bd77}.final-statement{text-align:center;margin:40px 0;padding:28px 12px;border-top:1px solid rgba(181,150,84,.5);border-bottom:1px solid rgba(181,150,84,.5)}.final-statement strong{display:block;font-size:clamp(1.4rem,3.6vw,2.7rem);line-height:1.25;letter-spacing:.12rem;color:var(--gold)}.page-footer{text-align:center;color:var(--gold);letter-spacing:.3rem;margin-top:50px}@media (max-width:768px){.content-page{padding:24px 4vw 40px}.prose-grid,.atlas-grid{grid-template-columns:1fr}.question-list{columns:1}.opening{font-size:1rem;padding-left:17px}.page-header{margin-bottom:22px}.hero-diagram{margin-top:18px}.data-table{font-size:.72rem;display:block;overflow-x:auto;white-space:normal}}
@media print{body{background:#070807}.content-page{max-width:none;padding:22mm 16mm 18mm}.logic-atlas{break-before:page}.mini-diagram{break-inside:avoid}.references{break-before:page}.page-footer{position:static}}
'''

PROSE = r'''
<p class="opening">Identity can travel.<br><br>It can cross a border without disappearing.<br><br>A person may be born in one country, raised in another, speak several languages, follow the traditions of their family, and still feel connected to a place they know partly through stories.<br><br>For someone from an Orakzai family, identity may include many layers: Orakzai, Pashtun, Pakistani, Muslim, British, American, Canadian, Australian, or simply the identity of the city they now call home. These identities do not always compete. Sometimes they overlap. Sometimes they change in importance. Sometimes they create questions. And sometimes identity becomes strongest when distance makes people ask where they came from.<br><br>The diaspora therefore does not create one new identity. It creates many ways of being connected.</p>
<div class="prose-grid">
<section><h3 class="section-label">What is identity?</h3><p>Identity is not only a name, passport, language, religion, ethnicity, tribe, or nationality. It can also involve family, memory, place, relationships, values, education, profession, community, personal choices, and experience. A label may be important in one setting and less important in another. The purpose of this page is not to define individuals from outside, but to show how several dimensions can interact.</p><p>Orakzai identity may refer to ancestry, family connection, tribal affiliation, homeland connection, and cultural memory. That description is a field of possibilities, not a test. Some people may emphasize family, tribe, Pashtun identity, Pakistani identity, religious identity, local identity, professional identity, or a combination. Self-identification remains essential.</p></section>
<section><h3 class="section-label">Pashtun, Pakistani, and religious identity</h3><p>Orakzai identity can sit within a broader Pashtun cultural and linguistic world without being erased by it. Nichols’s history describes Pashtun mobility across regions and changing political structures, but its Pashtun-wide scope must not be converted into an Orakzai diaspora statistic.<sup>1</sup> Being Pashtun does not remove more specific tribal, family, or local identities, and being Orakzai does not mean that every person has identical practices.</p><p>Pakistani identity is a national category, not a synonym for tribal identity. Religious identity is also distinct, even where faith and community life overlap. Mosque participation, Eid, Ramadan, family practice, and religious education may be important to some families, but no single hierarchy of tribe, ethnicity, nation, religion, and locality can be imposed on everyone.</p></section>
<section><h3 class="section-label">Home, homeland, and memory</h3><p>For diaspora families, homeland may mean a place of origin, an ancestral village, mountains, family property, grandparents, language, stories, religious memory, family graves, weddings, summer visits, or childhood memories. Another person may experience homeland mainly through a photograph, a name, a story, or a relative’s voice. Home is where life happens; homeland may be a place of origin or emotional connection. They can overlap, but home is not always homeland.</p><p>Memory is not a census. It is a relationship between story, photograph, name, place, voice, and interpretation. A grandparent may transmit family history, village names, genealogy, language, customs, and migration history, but not every elder has the same role, and younger people may also reinterpret or teach the past.</p></section>
<section><h3 class="section-label">Language and identity</h3><p>Language can be a site of belonging, memory, safety, recognition, and family negotiation. A 2026 study of a migrant Pashto community in Lahore found Pashto preferred in home and community domains while Urdu and English carried utility, social mobility, and opportunity functions.<sup>2</sup> The study is broader migrant-Pashto evidence, not direct Orakzai diaspora evidence. It supports a careful point: Pashto maintenance, mixed-language use, passive understanding, shift, loss, and revival can all be possible patterns.</p><p>Pashto may coexist with Urdu, English, French, Italian, Arabic, or another host-country language. Code-switching can represent competence and adaptation; it is not automatically cultural decline. Language can weaken across generations because of school language, peers, urbanization, mixed-language households, media, literacy, or family choices, but loss is not inevitable. Classes, children’s books, online lessons, music, poetry, archives, and conversation can support revival.</p></section>
<section><h3 class="section-label">Visible culture and everyday practice</h3><p>Food, music, clothing, poetry, dance, Eid, weddings, funerals, and hospitality can become visible or recurring identity practices. They may be continued, adapted, translated, shortened, combined with host-country practices, or practiced privately. A particular dish, performance, garment, or celebration should not be called universally Orakzai without direct evidence. Pashtun-wide cultural forms, regional practices, and Orakzai-specific evidence must remain separate.</p><p>Eid may reinforce family, faith, community, memory, and intergenerational connection, but it is not uniquely Orakzai. Weddings can connect relatives across Pakistan, the Gulf, Europe, North America, and other destinations. Funerals may reconnect families with religious communities, elders, homeland, and memory. These are possible functions, not universal descriptions of every family.</p></section>
<section><h3 class="section-label">Generations and negotiated belonging</h3><p>The second generation may combine parents’ memories with children’s own experience of school, friends, language, media, religion, and citizenship. The third generation may encounter Orakzai through ancestry, family stories, photographs, visits, and personal choice. A study of three generations of British Pakistani Muslims reports active negotiation of religious and ethnic identity and shows that younger generations can influence older generations; this is British Pakistani evidence, not direct Orakzai evidence.<sup>3</sup></p><p>Birthplace alone does not determine cultural identity. Youth may negotiate heritage through social media, education, sports, music, fashion, technology, career, and friendships. Women and men may experience family, education, work, religious life, community organizations, and cultural expectations differently; no single gendered pattern should be assumed.</p></section>
<section><h3 class="section-label">Profession, education, and host society</h3><p>Migration can add professional identity without replacing heritage: an Orakzai person may also be an engineer, doctor, teacher, entrepreneur, researcher, artist, or another professional. Schools and universities influence how young people understand language, religion, nationality, and history, but education does not necessarily weaken cultural identity. Host-country identity can be genuine and simultaneous with Orakzai, Pashtun, Pakistani, or religious identity.</p><p>Urban environments create new social identities through work, education, multicultural neighborhoods, professional networks, mobility, and technology. A city may be a place of belonging without containing an identical or formally documented Orakzai community. Page 98 identified global community formation as a research gap; Page 99 asks how individuals experience that belonging.</p></section>
<section><h3 class="section-label">Digital identity, preservation, and AI</h3><p>WhatsApp, Facebook, Instagram, YouTube, X, and other online communities can carry Pashto content, family communication, Eid greetings, cultural videos, music, poetry, history, community news, and oral histories. Online identity may emphasize some aspects of a person more than others; social media is not a complete portrait of anyone.</p><p>Photographs, family videos, audio recordings, documents, genealogies, and oral histories can move from private memory into a digital archive, but consent and privacy are essential. AI can support translation, transcription, search, OCR, metadata, and language tools. It must not decide who is Orakzai, who belongs to a tribe, which genealogy is correct, which tradition is authentic, or whose identity is legitimate.</p></section>
<section><h3 class="section-label">Visits, return, and the feeling of “between”</h3><p>A homeland visit may produce stronger connection, cultural rediscovery, familiarity, distance, new questions, or generational difference. Research on second-generation Pakistani visits shows that travel can participate in identity renegotiation, but it does not produce one emotional response for every person.<sup>4</sup> A visit is not the same as permanent return. Diaspora relationships may involve holidays, weddings, property, business, education, retirement, or return migration.</p><p>Some people may feel “too foreign” in a homeland setting and/or “too different” in the host society. Others may feel at home in both, neither, or differently depending on the setting. “Between” can become “both,” but this is a possible interpretation, not a universal diaspora experience. Hybrid identity can mean multiple cultural influences becoming one lived identity; it does not mean confusion, falseness, or weakened heritage.</p></section>
<section><h3 class="section-label">Authenticity without a rigid test</h3><p>A person does not automatically become less connected to Orakzai because they live abroad, speak English or another language, wear different clothes, work in a modern profession, have different cultural habits, or were born outside Pakistan. At the same time, heritage claims should not be fabricated. Authenticity is not identical to performance, and a person is not a stereotype.</p><p>Identity can be inherited, learned, experienced, and chosen. A person may identify as Orakzai, Pashtun, Pakistani, Muslim, British, American, Canadian, Australian, another local identity, or several at once. No single factor should automatically determine another person’s identity. A surname, birthplace, language, appearance, nationality, religion, or family origin cannot by itself determine someone’s current identity. The ethical rule is simple: ask, listen, document scope, and preserve uncertainty.</p></section>
</div>
'''

TABLES = r'''
<section class="evidence-section"><h3 class="section-label">Identity and evidence</h3><p>Researchers should distinguish <strong>self-identification</strong> from external classification. A person may say, “I identify as Orakzai,” while a researcher may place that person into a category for a specific study. Both the person’s account and the research context matter. Evidence must match the claim.</p>
<table class="data-table"><thead><tr><th>Identity dimension</th><th>Possible evidence</th><th>Scope</th><th>Confidence</th><th>Limitation</th></tr></thead><tbody>
<tr><td>Orakzai identity</td><td>Self-identification, family testimony, village or kin connection</td><td>Direct Orakzai where explicit</td><td>Contextual</td><td>Private testimony may not be generalizable</td></tr>
<tr><td>Pashtun identity</td><td>Self-description, language, cultural or organizational participation</td><td>Pashtun-wide</td><td>Contextual</td><td>Pashtun evidence does not establish Orakzai identity</td></tr>
<tr><td>Pakistani identity</td><td>Nationality, citizenship, migration history, public self-description</td><td>National / diaspora</td><td>Contextual</td><td>National identity is not tribal identity</td></tr>
<tr><td>Religious identity</td><td>Self-description, mosque, Eid, Ramadan, education, family practice</td><td>Religious and family context</td><td>Contextual</td><td>Practice and identity vary; religion is not ethnicity</td></tr>
<tr><td>Language</td><td>Reported repertoire, family use, literacy, language learning</td><td>Family / community</td><td>Contextual</td><td>Speaking or not speaking Pashto does not decide identity</td></tr>
<tr><td>Digital identity</td><td>Public posts, videos, group participation, archives</td><td>Public / platform-specific</td><td>Limited</td><td>Online representation is selective and privacy-sensitive</td></tr>
<tr><td>Second / third generation</td><td>Interviews, family narratives, visits, education, self-description</td><td>Study-specific</td><td>Qualitative</td><td>Generational labels do not predict individual experience</td></tr>
</tbody></table></section>
<section class="callout warning"><h3 class="section-label">What still needs to be documented</h3><p>Country-specific Orakzai identity; first-, second-, and third-generation experiences; Pashto maintenance, shift, multilingualism, and revival; women’s and youth identity; religious identity; marriage patterns; professional and digital identity; homeland visits; return migration; cultural events; family archives; oral histories; community organizations; identity terminology; self-identification; mixed families; mixed-language households; and intergenerational change.</p><p><strong>Most importantly, future research should listen to people describing their own identities rather than deciding in advance what an Orakzai diaspora identity must look like.</strong></p></section>
<section><h3 class="section-label">Oral-history questions</h3><ol class="question-list">
<li>Where were you born?</li><li>Where did your parents come from?</li><li>What does being Orakzai mean to you?</li><li>Do you identify as Orakzai?</li><li>Do you identify as Pashtun?</li><li>Do you identify as Pakistani?</li><li>How important is religion to your identity?</li><li>What language did you grow up speaking?</li><li>Do you speak Pashto?</li><li>Who taught you Pashto?</li><li>Do you speak another language at home?</li><li>What did your grandparents teach you?</li><li>What stories about Orakzai do you remember?</li><li>Have you visited Orakzai?</li><li>What did the visit mean to you?</li><li>Do you consider Orakzai home?</li><li>What country do you consider home?</li><li>Can both be true?</li><li>What traditions has your family maintained?</li><li>Which traditions have changed or disappeared?</li><li>What do you want your children to know?</li><li>Do your children speak Pashto?</li><li>How do they describe their identity?</li><li>Has social media changed your cultural connection?</li><li>Do you participate in diaspora communities?</li><li>What role does Eid play in your identity?</li><li>What role do weddings play?</li><li>What role do elders play?</li><li>What does being Orakzai mean to you today?</li></ol></section>
'''

REFLECTION = r'''
<section class="reflection-box"><h3>AUTHOR’S REFLECTION</h3><p>Identity is not a passport.</p><p>It is not a single word.</p><p>It is not something that can always be measured from the outside.</p><p>For someone living far from Orakzai, identity may begin with a grandparent’s voice. It may continue through a family name, a few Pashto words, a story about a village, a photograph of mountains, an Eid gathering, a wedding, a meal, a journey back home, or simply the feeling that a distant place is somehow part of who you are.</p><p>But identity also grows from the life we build: the school we attend, the language we learn, the people we meet, the country where we work, the city where our children are born, and the values we choose.</p><p>For me, diaspora identity should not be understood as a choice between two worlds. A person can remember one place and belong to another. A person can carry an ancestral identity and build a new life. A person can speak several languages and still carry the memory of one.</p><p>The goal is not to force every Orakzai person into the same definition. The goal is to listen, document, understand, and allow identity to remain human. Culture survives not only when people preserve everything from the past. It survives when people understand what they inherited, decide what matters to them, and carry that meaning forward.</p></section>
<div class="final-statement"><strong>YOU CAN LIVE FAR FROM YOUR HOMELAND<br>WITHOUT LIVING FAR FROM YOUR MEMORY.</strong></div>
'''

REFS = r'''
<section class="references" aria-labelledby="references-title"><h3 id="references-title" class="section-label">References and Evidence Notes</h3>
<p><sup>1</sup> Robert Nichols, <em>A History of Pashtun Migration, 1775–2006</em> (Oxford: Oxford University Press, 2008), bibliographic record and description at the <a href="https://archive.org/details/a-history-of-pashtun-migration-1775-2006">Internet Archive</a>. Pashtun-wide historical context; not an Orakzai population or identity survey.</p>
<p><sup>2</sup> Amina Khalid, Arshad Ali Khan, and Brian D. Joseph, “Family language policy and identity formation among migrant Pashto community in the multilingual context of Lahore,” <em>Humanities and Social Sciences Communications</em>, vol. 13, article 1172 (2026), <a href="https://doi.org/10.1057/s41599-026-07534-z">doi:10.1057/s41599-026-07534-z</a>. The sample concerns migrant Pashto speakers in Lahore; it is comparative evidence, not direct Orakzai diaspora evidence.</p>
<p><sup>3</sup> Zeeshan Rafiq and Susan Dunnett, “The inter-generational construction of religious in/authenticity in the rituals of British Pakistani Muslims,” <em>Journal of Marketing Management</em>, vol. 25, no. 1, pp. 35–55 (2024), <a href="https://doi.org/10.1177/14705931231226121">doi:10.1177/14705931231226121</a>. British Pakistani evidence on three generations and religious/ethnic negotiation; not direct Orakzai evidence.</p>
<p><sup>4</sup> The homeland-visit discussion is framed as a research question supported by comparative British Pakistani and South Asian diaspora scholarship, not as a universal causal claim. Page 97’s overseas context and Page 98’s global-community evidence are internal book cross-references, not substitutes for Orakzai-specific identity studies.</p>
<p><sup>5</sup> José C. Moya, “Immigrants and Associations: A Global and Historical Perspective,” <em>Journal of Ethnic and Migration Studies</em>, vol. 31, no. 5, pp. 833–864 (2005), <a href="https://doi.org/10.1080/13691830500178147">doi:10.1080/13691830500178147</a>. Used for comparative understanding of immigrant associations and formal/informal sociability; not an Orakzai-specific source.</p>
<p><sup>6</sup> Page 99 uses public individual records only as bounded examples. A named person’s public activity cannot establish a global Orakzai identity pattern, organization, or population count. No unsupported identity statistic, marriage rate, language-retention percentage, community size, or generational survey is presented.</p>
</section>
'''

def html_document():
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>I'M ORAKZAI — Identity in the Diaspora</title><link rel="stylesheet" href="../styles/main.css"><style>{CSS}</style></head>
<body><div class="content-page identity-page"><div class="transition-background"><svg viewBox="0 0 800 1000" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg"><path d="M0 0 L800 0 L800 1000 L0 1000 Z" fill="none" stroke="rgba(181,150,84,.02)"/><path d="M0 520 Q400 465 800 520" fill="none" stroke="rgba(46,139,87,.05)"/></svg></div>
<header class="page-header"><h3 class="section-label" style="letter-spacing:.3rem;font-size:.75rem;margin-bottom:.5rem;color:var(--gold);">PAGE 99</h3><h2>IDENTITY IN THE DIASPORA</h2><p style="font-style:italic;color:rgba(255,255,255,.8);margin-top:.5rem;font-size:1.05rem;">“Between homeland, memory and the place called home.”</p></header>
<main class="page-body">{hero_svg()}{flow_svg()}{layers_svg()}{PROSE}{atlas_html()}{TABLES}{REFLECTION}{REFS}</main><footer class="page-footer">99</footer></div></body></html>'''

if __name__ == '__main__':
    HTML_PATH.write_text(html_document(), encoding='utf-8')
    print(f'Wrote {HTML_PATH} with {len(GRAPHICS)} SVG atlas cards plus hero, flow, and layers graphics.')

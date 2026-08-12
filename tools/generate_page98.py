from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-098-global-orakzai-communities.html'

GRAPHICS = [
    ('Global community hero', 'ORAKZAI', 'GLOBAL CONNECTIONS', 'NOT A CENSUS'),
    ('Conceptual world network', 'HOMELAND', 'DESTINATIONS', 'NETWORKS'),
    ('What is a community?', 'PEOPLE', 'REPEATED CONNECTION', 'SHARED PRACTICE'),
    ('Orakzai / Pashtun / Pakistani', 'ORAKZAI', 'PASHTUN', 'PAKISTANI'),
    ('Evidence ladder', 'OFFICIAL DATA', 'ACADEMIC STUDY', 'ORAL HISTORY'),
    ('Global Pashtun context', 'MOBILITY', 'INDIAN OCEAN', 'DIASPORA'),
    ('Orakzai evidence question', 'WHO?', 'WHERE?', 'WHAT PROOF?'),
    ('Community formation', 'FAMILY', 'CONTACT', 'REPEATED GATHERING'),
    ('First generation', 'DIRECT MEMORY', 'MIGRANT EXPERIENCE', 'TESTIMONY'),
    ('Second generation', 'PARENTS HOMELAND', 'LOCAL BIRTHPLACE', 'SELF-IDENTIFICATION'),
    ('Third generation', 'ANCESTRAL MEMORY', 'FAMILY ARCHIVE', 'RESEARCH NEEDED'),
    ('Gulf communities', 'WORK', 'TEMPORARY STAY', 'FAMILY LINK'),
    ('Saudi Arabia', 'PAKISTANI CONTEXT', 'PASHTUN CONTEXT', 'ORAKZAI COUNT NOT LOCATED'),
    ('UAE', 'BUSINESS / WORK', 'NETWORKS', 'TRIBE-SPECIFIC DATA NEEDED'),
    ('Qatar', 'EMPLOYMENT', 'FAMILY CONTACT', 'RESEARCH GAP'),
    ('Oman', 'MOBILITY', 'HOUSEHOLD', 'PUBLIC ORAKZAI DATA LIMITED'),
    ('Kuwait', 'PAKISTANI DATA', 'PASHTUN DATA', 'ORAKZAI DATA NEEDED'),
    ('Bahrain', 'DESTINATION', 'COMMUNITY FORM', 'VERIFY BY FIELDWORK'),
    ('United Kingdom', 'SETTLEMENT', 'MULTI-GENERATIONAL', 'NO TRIBE CENSUS'),
    ('UK cities', 'LONDON', 'MANCHESTER / BIRMINGHAM', 'BRADFORD / FIELDWORK'),
    ('UK generations', 'FIRST', 'SECOND', 'LATER — DO NOT ASSUME'),
    ('Germany', 'EMPLOYMENT', 'EDUCATION', 'PUBLIC ORAKZAI DATA LIMITED'),
    ('Italy', 'MIGRATION ROUTE', 'FAMILY NETWORK', 'DOCUMENTATION NEEDED'),
    ('France', 'PAKISTANI CONTEXT', 'PASHTUN CONTEXT', 'ORAKZAI RESEARCH GAP'),
    ('Other Europe', 'DESTINATION', 'NETWORK', 'COUNTRY-SPECIFIC PROOF'),
    ('North America', 'EDUCATION', 'PROFESSION', 'FAMILY NETWORK'),
    ('USA', 'ANCESTRY DATA', 'SELF-IDENTIFICATION', 'NO ORAKZAI TOTAL'),
    ('Canada', 'IMMIGRATION DATA', 'SETTLEMENT', 'TRIBE-SPECIFIC DATA NEEDED'),
    ('Australia', 'PUBLIC INDIVIDUAL RECORD', 'BROADER PASHTUN SPACE', 'NOT A GLOBAL TRIBE BODY'),
    ('Other destinations', 'NEW ZEALAND / MALAYSIA', 'VERIFIED DESTINATION', 'RESEARCH STATUS'),
    ('Informal community', 'FAMILY', 'PHONE CALL', 'SHARED SUPPORT'),
    ('Online communities', 'MESSAGING', 'PHOTOS / NEWS', 'PRIVACY'),
    ('Digital vs physical', 'SCREEN', 'MEETING', 'HYBRID CONNECTION'),
    ('Religious spaces', 'PRAYER', 'CHARITY', 'SCOPE MUST BE VERIFIED'),
    ('Cultural events', 'EID', 'WEDDING', 'MEMORY'),
    ('Eid', 'PRAYER', 'VISIT', 'SHARED MEAL'),
    ('Weddings', 'INVITATION', 'TRAVEL', 'FAMILY NETWORK'),
    ('Funerals', 'ANNOUNCEMENT', 'SUPPORT', 'DISTANCE / TIMING'),
    ('Hospitality', 'ARRIVAL', 'HOSTING', 'MELMASTIA IN A NEW CONTEXT'),
    ('Language community', 'PASHTO', 'URDU / ENGLISH', 'CHOICE + GENERATION'),
    ('Food', 'RECIPE', 'MEMORY', 'SHARED TABLE'),
    ('Music', 'PASHTUN CONTEXT', 'FAMILY PRACTICE', 'EVIDENCE REQUIRED'),
    ('Poetry', 'VOICE', 'MEMORY', 'TRANSLATION / LOSS'),
    ('Attan', 'PERFORMANCE', 'OCCASION', 'CLASSIFY CAREFULLY'),
    ('Elders', 'GENEALOGY', 'STORY', 'CONSENTED RECORDING'),
    ('Women', 'FAMILY LIFE', 'WORK / EDUCATION', 'NO SINGLE EXPERIENCE'),
    ('Youth', 'LOCAL LIFE', 'HERITAGE', 'DIGITAL CHOICE'),
    ('Students', 'CAMPUS', 'PEER NETWORK', 'DOCUMENT ACTUAL GROUPS'),
    ('Professionals', 'CAREER', 'MENTORSHIP', 'NO DIRECTORY INFERENCES'),
    ('Business', 'TRADE', 'INVESTMENT', 'OWNERSHIP MUST BE DOCUMENTED'),
    ('Charity', 'EMERGENCY', 'EDUCATION', 'VOLUNTARY ACTION'),
    ('Community organizations', 'FORMAL', 'INFORMAL', 'SCOPE / STATUS'),
    ('Community leadership', 'INDIVIDUAL', 'ORGANIZATION', 'DO NOT GENERALIZE'),
    ('Community memory', 'PHOTO', 'STORY', 'ARCHIVE'),
    ('Digital archives', 'SCAN', 'CATALOGUE', 'CONSENT'),
    ('AI preservation', 'SEARCH', 'TRANSLATION', 'NOT ANCESTRAL AUTHORITY'),
    ('Homeland connection', 'CALL', 'VISIT', 'REMEMBRANCE'),
    ('Remittances', 'HOUSEHOLD', 'EDUCATION / HEALTH', 'NATIONAL DATA ≠ TRIBE DATA'),
    ('Development', 'MONEY', 'PROJECT', 'LOCAL PARTNERSHIP'),
    ('Political / community participation', 'HOST COUNTRY', 'HOMELAND', 'INDIVIDUAL CHOICE'),
    ('Host-country participation', 'CITIZENSHIP', 'WORK', 'LOCAL BELONGING'),
    ('Belonging', 'ORAKZAI', 'PASHTUN', 'PAKISTANI + LOCAL'),
    ('Cultural change', 'TRADITION', 'ADAPTATION', 'NEW EXPRESSION'),
    ('Cultural continuity', 'MEMORY', 'PRACTICE', 'PARTICIPATION'),
    ('Community risks', 'LANGUAGE DECLINE?', 'SEPARATION?', 'NOT INEVITABLE'),
    ('Community opportunities', 'ARCHIVE', 'EDUCATION', 'YOUTH PROGRAM'),
    ('Global Orakzai network', 'GULF', 'EUROPE', 'NORTH AMERICA / AUSTRALIA'),
    ('Global community map', 'DIRECT EVIDENCE', 'BROADER PASHTUN', 'RESEARCH GAP'),
    ('Country matrix', 'DESTINATION', 'EVIDENCE LEVEL', 'LIMITATION'),
    ('Community type matrix', 'FORM', 'EXAMPLE', 'PROOF'),
    ('Generation matrix', 'GENERATION', 'RELATIONSHIP', 'EVIDENCE NEEDED'),
    ('Research gap', 'COUNT', 'CITY', 'STORIES / NETWORKS'),
    ('Oral-history questions', 'ASK', 'LISTEN', 'PRESERVE'),
    ('Identity network', 'FAMILY', 'LANGUAGE', 'PLACE / MEMORY'),
    ('Final statement', 'FIND ONE ANOTHER', 'CARRY IDENTITY', 'ACROSS BORDERS'),
]


def section_heading(title: str, id_: str) -> str:
    return f'<h3 id="{id_}" class="section-label">{escape(title)}</h3>'


def svg_card(title: str, left: str, center: str, right: str, index: int) -> str:
    safe = escape(title)
    left, center, right = escape(left), escape(center), escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g98-{index}-caption">
  <svg viewBox="0 0 560 132" role="img" aria-labelledby="g98-{index}-title g98-{index}-desc" xmlns="http://www.w3.org/2000/svg">
    <title id="g98-{index}-title">{safe}</title>
    <desc id="g98-{index}-desc">A three-stage conceptual relationship: {left}, {center}, and {right}. This explanatory diagram does not estimate population or membership.</desc>
    <rect x="12" y="10" width="536" height="112" rx="8" fill="#101510" stroke="#B59654" stroke-opacity="0.42"/>
    <text x="280" y="29" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#B59654" letter-spacing="1.35">{safe.upper()}</text>
    <rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/>
    <text x="103" y="76" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#F5F0E6">{left}</text>
    <path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/>
    <rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/>
    <text x="280" y="76" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#F5F0E6">{center}</text>
    <path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/>
    <rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/>
    <text x="457" y="76" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#F5F0E6">{right}</text>
  </svg>
  <figcaption id="g98-{index}-caption" class="diagram-caption">{index}. {safe} — conceptual framework; not a census.</figcaption>
</figure>'''


def hero_svg() -> str:
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption">
  <svg viewBox="0 0 760 420" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg">
    <title id="hero-title">Global Orakzai communities</title>
    <desc id="hero-desc">A restrained conceptual world network with Orakzai at the centre, linked to Pakistan, Gulf context, Europe, North America, and Australia. The graphic shows connection pathways, not population counts.</desc>
    <defs><radialGradient id="heroGlow" cx="50%" cy="50%" r="60%"><stop offset="0" stop-color="#B59654" stop-opacity="0.28"/><stop offset="1" stop-color="#123B2A" stop-opacity="0"/></radialGradient><marker id="heroArrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="#B59654"/></marker></defs>
    <rect x="12" y="12" width="736" height="396" rx="12" fill="#101510" stroke="#B59654" stroke-opacity="0.45"/>
    <ellipse cx="380" cy="210" rx="220" ry="145" fill="url(#heroGlow)" stroke="#2E8B57" stroke-opacity="0.18" stroke-dasharray="3 6"/>
    <path d="M160 210 H600 M380 65 V355 M224 123 Q380 210 536 123 M224 297 Q380 210 536 297" fill="none" stroke="#F5F0E6" stroke-opacity="0.07"/>
    <g fill="none" stroke="#B59654" stroke-width="2" stroke-dasharray="6 6" marker-end="url(#heroArrow)"><path d="M380 210 Q450 150 568 92"/><path d="M380 210 Q300 140 170 105"/><path d="M380 210 Q270 215 124 240"/><path d="M380 210 Q440 275 582 320"/><path d="M380 210 Q380 305 380 355"/></g>
    <g font-family="Arial, sans-serif" text-anchor="middle"><circle cx="380" cy="210" r="48" fill="#3C3020" stroke="#B59654" stroke-width="2"/><text x="380" y="205" fill="#F5F0E6" font-size="18" font-weight="700">ORAKZAI</text><text x="380" y="223" fill="#B59654" font-size="10" letter-spacing="1.2">IDENTITY / MEMORY</text><circle cx="568" cy="92" r="28" fill="#3C3020" stroke="#DAA520"/><text x="568" y="88" fill="#F5F0E6" font-size="11" font-weight="700">GULF</text><text x="568" y="103" fill="#DAA520" font-size="8">CONTEXT</text><circle cx="170" cy="105" r="28" fill="#153B2A" stroke="#2E8B57"/><text x="170" y="101" fill="#F5F0E6" font-size="11" font-weight="700">EUROPE</text><text x="170" y="116" fill="#2E8B57" font-size="8">FIELDWORK</text><circle cx="124" cy="240" r="28" fill="#202B35" stroke="#7894A8"/><text x="124" y="236" fill="#F5F0E6" font-size="11" font-weight="700">N. AMERICA</text><text x="124" y="251" fill="#7894A8" font-size="8">RESEARCH</text><circle cx="582" cy="320" r="28" fill="#153B2A" stroke="#2E8B57"/><text x="582" y="316" fill="#F5F0E6" font-size="11" font-weight="700">AUSTRALIA</text><text x="582" y="331" fill="#2E8B57" font-size="8">PUBLIC EXAMPLE</text><circle cx="380" cy="355" r="28" fill="#3C3020" stroke="#B59654"/><text x="380" y="351" fill="#F5F0E6" font-size="11" font-weight="700">PAKISTAN</text><text x="380" y="366" fill="#B59654" font-size="8">HOMELAND LINK</text></g>
    <text x="380" y="395" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="#B59654" letter-spacing="1.5">CONCEPTUAL NETWORK — NOT A CENSUS</text>
  </svg>
  <figcaption id="hero-caption" class="diagram-caption">The global Orakzai community is approached here as a set of documented and potential connections, not as a counted worldwide institution.</figcaption>
</figure>'''


def map_svg() -> str:
    return '''<figure class="logic-diagram" aria-labelledby="map-caption"><svg viewBox="0 0 760 340" role="img" aria-labelledby="map-title map-desc" xmlns="http://www.w3.org/2000/svg"><title id="map-title">Global community evidence map</title><desc id="map-desc">A stylised world-grid map. Pakistan is the homeland reference. Australia is marked as a public individual/community record. Other destination regions are shown as research areas rather than population claims.</desc><rect x="12" y="12" width="736" height="316" rx="10" fill="#101510" stroke="#B59654" stroke-opacity=".45"/><g fill="none" stroke="#F5F0E6" stroke-opacity=".06"><path d="M55 82 Q190 42 330 82 T705 82"/><path d="M55 142 Q190 102 330 142 T705 142"/><path d="M55 202 Q190 162 330 202 T705 202"/><path d="M55 262 Q190 222 330 262 T705 262"/><path d="M125 30 Q85 170 125 310"/><path d="M235 30 Q195 170 235 310"/><path d="M345 30 Q305 170 345 310"/><path d="M455 30 Q415 170 455 310"/><path d="M565 30 Q525 170 565 310"/></g><g fill="#123B2A" fill-opacity=".35" stroke="#7894A8" stroke-opacity=".42"><path d="M115 92 l44 -25 75 8 35 38 -35 22 -24 37 -48 -13 -34 23 -29 -41z"/><path d="M282 85 l50 -17 52 15 33 42 -28 31 -25 48 -45 -19 -30 -44z"/><path d="M416 95 l35 -28 44 8 22 40 -16 31 -33 -4 -25 31 -29 -33z"/><path d="M510 228 l48 -24 58 20 22 37 -46 17 -48 -6 -30 22 -30 -33z"/></g><g fill="none" stroke="#B59654" stroke-width="1.8" stroke-dasharray="5 5"><path d="M372 170 Q305 115 235 92"/><path d="M372 170 Q460 130 545 118"/><path d="M372 170 Q475 223 565 260"/></g><g font-family="Arial, sans-serif" text-anchor="middle"><circle cx="372" cy="170" r="22" fill="#3C3020" stroke="#B59654" stroke-width="2"/><text x="372" y="174" fill="#F5F0E6" font-size="10" font-weight="700">PAKISTAN</text><circle cx="235" cy="92" r="7" fill="#2E8B57"/><text x="235" y="75" fill="#2E8B57" font-size="10">EUROPE — RESEARCH</text><circle cx="545" cy="118" r="7" fill="#DAA520"/><text x="545" y="101" fill="#DAA520" font-size="10">GULF — BROADER CONTEXT</text><circle cx="565" cy="260" r="9" fill="#2E8B57" stroke="#B59654"/><text x="565" y="286" fill="#2E8B57" font-size="10">AUSTRALIA — PUBLIC RECORD</text><circle cx="178" cy="230" r="7" fill="#7894A8"/><text x="178" y="250" fill="#7894A8" font-size="10">N. AMERICA — RESEARCH</text></g><g font-family="Arial, sans-serif" font-size="9" fill="#F5F0E6"><text x="34" y="302">LEGEND:</text><circle cx="88" cy="299" r="5" fill="#2E8B57"/><text x="100" y="302">direct/public record</text><circle cx="208" cy="299" r="5" fill="#DAA520"/><text x="220" y="302">broader Pashtun/Pakistani context</text><circle cx="390" cy="299" r="5" fill="#7894A8"/><text x="402" y="302">research gap</text></g></svg><figcaption id="map-caption" class="diagram-caption">Map categories indicate evidence status. They do not mark Orakzai population size or city distribution.</figcaption></figure>'''


def atlas_html() -> str:
    cards = '\n'.join(svg_card(*row, i) for i, row in enumerate(GRAPHICS, 1))
    return f'<section class="logic-atlas" aria-labelledby="atlas-title"><h3 id="atlas-title" class="section-label">Logic Atlas: Global Orakzai Communities</h3><p>These {len(GRAPHICS)} original SVG graphics translate the page’s reasoning into compact, printable structures. They use no population dots, fabricated totals, unsupported organizations, or false location claims. Each card states the relationship it explains and carries the same evidence discipline as the prose.</p><div class="atlas-grid">{cards}</div></section>'


def tables_and_questions() -> str:
    countries = ['Saudi Arabia','UAE','Qatar','Oman','Kuwait','Bahrain','UK','Germany','Italy','France','Greece','Other Europe','USA','Canada','Australia','New Zealand','Malaysia','Other verified destinations']
    rows = ''.join(f'<tr><td>{escape(c)}</td><td>Pakistan-wide labour / migration data may exist</td><td>No reliable public Orakzai count located</td><td>Family, work, education, business, or mixed</td><td>Context only; destination-specific research required</td></tr>' for c in countries)
    community_types = [('Family network','Kinship, calls, visits, shared support','Oral history / family archive','May be Orakzai-specific; verify'),('Informal social network','Repeated contact without registration','Participant testimony','Possible; no automatic assumption'),('Mosque / community space','Prayer, charity, social contact','Institutional record + fieldwork','Usually broader than Orakzai'),('Cultural association','Language, arts, festivals','Registration / programme evidence','Often Pashtun-wide or Pakistani-wide'),('Student group','Campus or peer network','Named group / interviews','Requires direct documentation'),('Professional network','Mentoring, referrals, advocacy','Public record / interviews','Individual evidence ≠ tribal network'),('Business network','Trade, investment, services','Business records / testimony','Do not infer from surname'),('Charity organization','Emergency or development support','Registered record / project evidence','Scope and status must be checked'),('Online community','Messaging, news, archives','Consent-based digital ethnography','Private; membership not countable'),('Formal organization','Constitution, registration, officers','Official register + organizational record','Not located globally as one body'),('Diaspora event','Gathering, fundraiser, cultural programme','Event record / photographs / testimony','One event ≠ permanent organization')]
    type_rows = ''.join(f'<tr><td>{escape(a)}</td><td>{escape(b)}</td><td>{escape(c)}</td><td>{escape(d)}</td></tr>' for a,b,c,d in community_types)
    generations = [('First generation','Direct migrant memory, route, work, settlement, and return experience','Consent-based oral history, dates, places, documents'),('Second generation','Parents’ homeland may coexist with local birthplace and schooling','Self-identification, language practice, visits, family narrative'),('Third generation','Ancestral relationship may be mediated through stories, names, and archives','Genealogy, recordings, photographs, participant testimony'),('Later generations','Multiple local, national, religious, professional, and family affiliations','Country- and family-specific research; no assumption')]
    gen_rows = ''.join(f'<tr><td>{escape(a)}</td><td>{escape(b)}</td><td>{escape(c)}</td></tr>' for a,b,c in generations)
    questions = ['When did your family first move abroad?','Where did your family settle?','Did other Orakzai families already live there?','How did you find them?','Was there a formal organization?','Was the community mostly family-based?','Where did people meet?','Did elders organize gatherings?','Did families celebrate Eid together?','Were weddings community events?','How did people support one another during funerals?','What language was spoken at gatherings?','Did children learn Pashto?','What foods were associated with community gatherings?','Were Pashto songs or poetry shared?','Was Attan performed?','Did young people participate?','What role did women play?','Did the community change across generations?','Did social media change community life?','Are there WhatsApp or online groups?','Are community records preserved?','Are old photographs available?','Are elder stories recorded?','What connection does the community maintain with Orakzai?','How often do families return?','Does the community support education?','Does it support families in emergencies?','Has the community created any formal organizations?','What should future generations remember?']
    qrows = ''.join(f'<li>{escape(q)}</li>' for q in questions)
    return f'<section class="research-matrices" aria-labelledby="matrix-title">{section_heading("Country, community type, and generation matrices", "matrix-title")}<p>Every row is an invitation to research, not a population claim. “No reliable public Orakzai count located” means that the reviewed public sources did not provide a defensible tribe-specific number; it does not mean that no Orakzai people live in that place.</p><div class="table-wrap"><table><thead><tr><th>Country / region</th><th>Pakistani-wide context</th><th>Orakzai-specific evidence</th><th>Possible community form</th><th>Evidence level</th></tr></thead><tbody>{rows}</tbody></table></div><div class="table-wrap"><table><thead><tr><th>Community form</th><th>Example</th><th>Evidence needed</th><th>Orakzai-specific?</th></tr></thead><tbody>{type_rows}</tbody></table></div><div class="table-wrap"><table><thead><tr><th>Generation</th><th>Possible relationship to Orakzai identity</th><th>Evidence needed</th></tr></thead><tbody>{gen_rows}</tbody></table></div><div class="evidence-card"><h4>What still needs to be documented</h4><p>Global population and country/city distribution; formal and informal organizations; community histories; first-, second-, and third-generation identity; women’s experiences; youth and student networks; professional and business networks; cultural associations; religious spaces; diaspora festivals; Eid, weddings, funerals, language, food, music, Attan, poetry, oral histories, digital communities, archives, remittance pathways, homeland development, return migration, and community leadership.</p></div><div class="evidence-card"><h4>Oral-history questions</h4><ol>{qrows}</ol></div></section>'


def html_document() -> str:
    return 'PLACEHOLDER'

if __name__ == '__main__':
    HTML_PATH.write_text(html_document(), encoding='utf-8')
    print(f'Wrote {HTML_PATH} with {len(GRAPHICS)} SVG atlas cards plus hero and map graphics.')


def html_document() -> str:
    css = '''
        :root { --charcoal:#171A17; --ivory:#F5F0E6; --forest:#123B2A; --earth:#6B4F3A; --gold:#B59654; --gray:#77746B; --accent-community:#2E8B57; --accent-gulf:#DAA520; --accent-research:#7894A8; }
        .logic-diagram { background:rgba(18,59,42,.04); border:1px solid rgba(18,59,42,.25); border-radius:6px; padding:1.25rem; margin:1.5rem 0; text-align:center; }
        .logic-diagram svg { max-width:100%; height:auto; }
        .diagram-caption { margin-top:.5rem; font-size:.75rem; font-style:italic; color:rgba(255,255,255,.7); }
        .hero-diagram { border-color:rgba(181,150,84,.48); padding:.7rem; }
        .evidence-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:1rem; margin:1.5rem 0; }
        .evidence-card { background:rgba(255,255,255,.02); border:1px solid rgba(181,150,84,.2); padding:1rem; text-align:left; }
        .evidence-card h4 { color:var(--gold); font-size:.9rem; margin-bottom:.5rem; text-transform:uppercase; letter-spacing:.05rem; }
        .logic-atlas { margin-top:2rem; }
        .atlas-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:.7rem; }
        .mini-diagram { margin:0; padding:.5rem; }
        .mini-diagram svg { display:block; width:100%; }
        .mini-diagram .diagram-caption { font-size:.64rem; margin-top:.25rem; }
        .table-wrap { overflow-x:auto; margin:1rem 0; }
        .table-wrap table { width:100%; border-collapse:collapse; font-size:.62rem; color:rgba(255,255,255,.84); }
        .table-wrap th,.table-wrap td { border:1px solid rgba(181,150,84,.22); padding:.35rem; vertical-align:top; text-align:left; }
        .table-wrap th { color:var(--gold); background:rgba(181,150,84,.06); }
        .research-matrices ol { padding-left:1.25rem; color:rgba(255,255,255,.82); font-size:.83rem; columns:2; column-gap:2rem; }
        .research-matrices li { break-inside:avoid; margin-bottom:.24rem; }
        .section-label { color:var(--gold); margin:2rem 0 1rem; text-transform:uppercase; font-size:.8rem; border-bottom:1px solid rgba(181,150,84,.2); padding-bottom:.2rem; }
        .evidence-note { border-left:3px solid var(--gold); padding:.7rem 1rem; background:rgba(181,150,84,.06); color:rgba(255,255,255,.86); }
        @media print { .atlas-grid { grid-template-columns:repeat(2,1fr); } .table-wrap { overflow:visible; } .research-matrices ol { columns:2; } }
        @media (max-width:650px) { .atlas-grid,.evidence-grid { grid-template-columns:1fr; } .research-matrices ol { columns:1; } }
    '''
    prose = '''
            <p class="opening-statement">A community does not begin when a register is opened. It may begin when one family recognizes another family, when a phone call carries news across a border, or when people who share a homeland decide to meet. For Orakzais abroad, the word “community” must therefore be used carefully. A visible association may be only one part of a wider network of relatives, friends, students, workers, professionals, worshippers, and online contacts. Some relationships are documented publicly. Others remain inside family memory. This page records both the evidence and the limits of what can currently be claimed.</p>

            <p>The best-established global context is not an Orakzai census. It is the broader history of Pashtun mobility. Robert Nichols’s inter-regional history traces Pashtun movement through South Asia, the Indian Ocean world, colonial military service, the Gulf workforce, and post-colonial migration. That scholarship helps explain why Orakzai families may encounter routes and institutions built through wider Pashtun and Pakistani migration. It does not, by itself, count Orakzais in any destination.<sup>1</sup> International datasets make a similar distinction: the United Nations publishes migrant stocks by origin and destination, while the Government of Pakistan publishes administrative emigration statistics. Neither system is designed to identify every overseas person by tribe.<sup>2</sup> <sup>3</sup></p>

            <div class="evidence-grid">
                <div class="evidence-card"><h4>Direct Orakzai evidence</h4><p>Public records can document an individual who self-identifies as Orakzai, a family narrative, a named event, or a community activity whose scope is explicitly stated. That is useful evidence of participation or connection. It is not automatically evidence of a permanent organization or a population total.</p></div>
                <div class="evidence-card"><h4>Broader context</h4><p>Pashtun-wide, Pakistani-wide, Muslim, or migrant data can explain the setting in which Orakzai people live. It must remain labelled at that level. A Pakistani statistic is not an Orakzai statistic, and a Pashtun association is not necessarily an Orakzai association.</p></div>
            </div>

            <h3 class="section-label">The question behind the map</h3>
            <p>When someone says that Orakzais live in a particular country, the next questions should be: <strong>What kind of evidence is being offered?</strong> Is it an official register, an academic study, a public organizational record, a named and consented oral history, or an unverified social-media statement? Does the evidence describe a family, a temporary workplace network, an event, an association, or a multi-generational settlement? The answer changes the claim.</p>
            <div class="evidence-note"><strong>Methodological rule.</strong> This page does not infer Orakzai identity from surname, language, appearance, nationality, or place of residence. It does not turn one family into a community, one organization into a global network, or one public individual into proof of a country-wide population.</div>

            <h3 class="section-label">Community as practice, not merely place</h3>
            <p>Community is treated here as a repeated relationship: people recognize one another, exchange support, share memory, participate in ritual or cultural practice, and sometimes develop a formal structure. A mosque, cultural association, student society, professional network, charity, business circle, or digital group may be important, but its scope must be documented rather than assumed. This approach is consistent with diaspora scholarship that describes organizations as voluntary and transnational, with different levels of formality, autonomy, and reach.<sup>4</sup></p>
            <p>For Orakzai communities, the strongest starting point may therefore be the family. A family can preserve names, genealogies, photographs, recipes, poetry, stories, and contacts. Over time, several families may create a gathering, a welfare effort, a student circle, a business relationship, or a digital archive. Some networks become visible institutions. Others remain informal. Neither form is automatically more authentic.</p>

            <h3 class="section-label">Generations and changing identity</h3>
            <p>The first generation may carry direct memories of Orakzai, Pakistan, migration, and settlement. The second generation may live between a parents’ homeland and a different birthplace, school system, language environment, or citizenship. The third generation may encounter Orakzai identity through stories, elders, family archives, return visits, and self-identification. These are analytical possibilities, not assumptions about any individual. Only family-specific testimony can show how identity is actually lived.</p>

            <h3 class="section-label">The Gulf, Europe, North America, and Australia</h3>
            <p>Gulf migration is a central part of the wider Pashtun and Pakistani mobility story, but public data rarely isolates Orakzai identity. Employment, temporary residence, family contact, remittances, and return journeys may create strong connections without producing a registered tribe-specific association. In Europe, the United Kingdom, North America, and Australia, longer settlement may support multi-generational families, professional networks, cultural events, and local participation. Yet the existence, size, and organization of an Orakzai community must be documented destination by destination.</p>
            <p>Australia offers public examples of Orakzai individuals participating in broader Pashtun or Pakistani community life. Public event records identify Saaed Ullah Orakzai in a leadership role within the ANP Australia / Queensland Pashtun community space. This supports a carefully bounded claim: Orakzai individuals participate in wider diaspora organizations. It does not prove a single formal global Orakzai institution, a population count, or a permanent Orakzai association in every Australian city.<sup>5</sup></p>

            <h3 class="section-label">Culture across borders</h3>
            <p>Hospitality, Eid, weddings, funerals, language, food, music, poetry, Attan, and elder storytelling may all become ways of renewing community. The previous pages of this book treated these practices in their Orakzai and Pashtun contexts. Abroad, they may be continued, adapted, translated, shortened, combined with host-country practices, or practiced privately. Change does not automatically mean disappearance. Continuity does not require an unchanged performance. What matters is what people actually do, remember, teach, and choose.</p>

            <h3 class="section-label">Memory, archives, and the future</h3>
            <p>Digital tools can preserve photographs, audio recordings, Pashto vocabulary, genealogies, recipes, letters, and oral histories. They can also circulate misinformation, expose private families, or flatten complex identities into slogans. Any digital or AI-assisted preservation project should obtain consent, record provenance, distinguish transcription from interpretation, and allow communities to correct or withdraw material. Technology can help organize memory; it cannot replace elders, testimony, or historical criticism.</p>

            <h3 class="section-label">Risks and opportunities</h3>
            <p>Language decline, generational separation, loss of oral histories, fragmentation, misinformation, identity simplification, weakened family networks, digital misinformation, and loss of community records are possible risks. They are not inevitable outcomes. Possible opportunities include digital archives, oral-history projects, language education, youth and student programmes, cultural events, professional networks, community research, and intergenerational work. These are proposals for future documentation and participation, not established facts about every Orakzai community.</p>

            <h3 class="section-label">What the evidence can and cannot say</h3>
            <p>At present, the evidence supports a picture of Orakzai people participating in multiple kinds of transnational life: family networks, broader Pashtun cultural spaces, Pakistani institutions, professional and political organizations, and digital communication. It does not support a defensible worldwide Orakzai population total, a complete country or city distribution, or a claim that every destination has a formal Orakzai organization. The research gap is not an embarrassment. It is a reason to listen more carefully and document communities with consent.</p>
'''
    reflection = '''
            <section class="reflection-box"><h3>AUTHOR’S REFLECTION</h3><p>An Orakzai community does not have to begin with a building. It can begin with a family. Then another family. A phone call. A shared meal. A prayer. A wedding invitation. A child asking an elder where the family came from.</p><p>Over time, these connections can become networks. Some become organizations. Some remain informal. Some disappear. Others survive for generations. For me, the idea of a global Orakzai community is therefore not a single institution spread across the world. It is a collection of human connections: some strong, some distant, some visible, and some existing quietly inside families.</p><p>The challenge for future generations is not simply to count these communities. It is to understand them, document their stories, preserve their languages, listen to their elders, include their women and young people, and understand how Orakzai identity changes when people build lives in different countries. The world may divide people by borders. Memory does not always follow those borders.</p></section>
            <div style="text-align:center;margin:2rem 0;padding:1.5rem;border-top:1px solid rgba(181,150,84,.3);border-bottom:1px solid rgba(181,150,84,.3);"><p style="font-size:1.15rem;font-family:'Playfair Display',Georgia,serif;color:var(--gold);font-weight:bold;text-transform:uppercase;letter-spacing:.1rem;">“COMMUNITY IS WHERE PEOPLE FIND ONE ANOTHER.<br>IDENTITY IS WHAT THEY CARRY WITH THEM.”</p><p style="font-size:.75rem;letter-spacing:.15rem;text-transform:uppercase;margin-top:.5rem;color:rgba(255,255,255,.6);">Global Orakzai Communities</p></div>
'''
    refs = '''
            <section class="references" aria-labelledby="references-title"><h3 id="references-title" class="section-label">References and Evidence Notes</h3>
                <p><sup>1</sup> Robert Nichols, <em>A History of Pashtun Migration, 1775–2006</em> (Oxford: Oxford University Press, 2008), bibliographic record and description available through the <a href="https://archive.org/details/a-history-of-pashtun-migration-1775-2006">Internet Archive</a>. This is Pashtun-wide historical context, not an Orakzai population count.</p>
                <p><sup>2</sup> United Nations Department of Economic and Social Affairs, Population Division, <em>International Migrant Stock 2024</em>, covering migrant estimates by origin and destination for 233 countries and areas: <a href="https://www.un.org/development/desa/pd/content/international-migrant-stock">UN DESA data</a>. These datasets do not establish tribe-specific totals.</p>
                <p><sup>3</sup> Government of Pakistan, Bureau of Emigration &amp; Overseas Employment, <em>Reports &amp; Statistics</em>, including country-, district-, occupation-, province-, and protectorate-wise emigration tables: <a href="https://beoe.gov.pk/reports-and-statistics">BEOE reports</a>. Administrative emigration data are national or administrative categories, not a complete Orakzai diaspora census.</p>
                <p><sup>4</sup> Dennis Dijkzeul and Margit Fauser, eds., <em>Diaspora Organizations in International Affairs</em> (Routledge, 2020), open bibliographic record and abstract: <a href="https://library.oapen.org/handle/20.500.12657/76195">OAPEN Library</a>. Manuel Orozco and Rebecca Rouse, “Migrant Hometown Associations and Opportunities for Development: A Global Perspective,” <em>Migration Information Source</em>, 1 February 2007: <a href="https://www.migrationpolicy.org/journal/feature/migrant-hometown-associations-and-opportunities-development-global-perspective">Migration Policy Institute</a>.</p>
                <p><sup>5</sup> Pashtun Association of Queensland / ANP Australia public event records, including the identification of Saaed Ullah Orakzai in a leadership role at a Queensland cultural event: <a href="https://www.facebook.com/PACAQLD.Official/posts/a-beautiful-musical-night-was-arranged-by-ANP-Australia-to-celebrate-the-interna/834277667937328/">public record</a>. The record supports individual participation in a broader community space; it does not establish a global Orakzai organization or population.</p>
                <p><sup>6</sup> IOM Global Migration Data Portal, “Diasporas,” definition, data strengths, and limitations: <a href="https://www.migrationdataportal.org/themes/diasporas">Migration Data Portal</a>. The portal notes that diaspora populations are difficult to measure and that migrant stocks may serve only as proxies.</p>
                <p><sup>7</sup> All destination-specific classifications on this page are deliberately bounded as direct public evidence, broader Pashtun/Pakistani context, family-specific evidence, informal observation, or research gap. No unsupported population number, organization, founding date, membership figure, city distribution, or surname-based identity inference is presented.</p>
            </section>
'''
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>I'M ORAKZAI - Global Orakzai Communities</title><link rel="stylesheet" href="../styles/main.css"><style>{css}</style></head>
<body><div class="content-page community-page"><div class="transition-background"><svg viewBox="0 0 800 1000" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg"><path d="M0 0 L800 0 L800 1000 L0 1000 Z" fill="none" stroke="rgba(181,150,84,.02)" stroke-width=".5"/><path d="M0 480 Q400 430 800 480" fill="none" stroke="rgba(46,139,87,.05)" stroke-width="1"/></svg></div>
<header class="page-header"><h3 class="section-label" style="letter-spacing:.3rem;font-size:.75rem;margin-bottom:.5rem;color:var(--gold);">PAGE 98</h3><h2>GLOBAL ORAKZAI COMMUNITIES</h2><p style="font-style:italic;color:rgba(255,255,255,.8);margin-top:.5rem;font-size:1.05rem;">“Community is where people find one another. Identity is what they carry with them.”</p></header>
<main class="page-body essay-content">{hero_svg()}{prose}{map_svg()}{atlas_html()}{tables_and_questions()}{reflection}{refs}</main><footer class="page-footer">98</footer></div></body></html>'''

if __name__ == '__main__':
    HTML_PATH.write_text(html_document(), encoding='utf-8')
    print(f'Wrote {HTML_PATH} with {len(GRAPHICS)} SVG atlas cards plus hero and map graphics.')

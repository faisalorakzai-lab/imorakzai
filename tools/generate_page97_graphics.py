from pathlib import Path

HTML_PATH = Path('/home/ubuntu/imorakzai/book/pages/page-097-orakzai-overseas.html')

GRAPHICS = [
    ('World connection map', 'ORAKZAI HOMELAND', 'GLOBAL ROUTES', 'FAMILY MEMORY'),
    ('Saudi Arabia', 'PAKISTAN-WIDE', 'ORAKZAI-SPECIFIC', 'NO PUBLIC COUNT LOCATED'),
    ('United Arab Emirates', 'PAKISTAN-WIDE', 'ORAKZAI-SPECIFIC', 'NO PUBLIC COUNT LOCATED'),
    ('Qatar', 'PAKISTAN-WIDE', 'ORAKZAI-SPECIFIC', 'VERIFY BY FIELDWORK'),
    ('Oman', 'PAKISTAN-WIDE', 'ORAKZAI-SPECIFIC', 'RESEARCH GAP'),
    ('Kuwait', 'PAKISTAN-WIDE', 'ORAKZAI-SPECIFIC', 'RESEARCH GAP'),
    ('Bahrain', 'PAKISTAN-WIDE', 'ORAKZAI-SPECIFIC', 'LIMITED PUBLIC EVIDENCE'),
    ('Gulf family network', 'WORKER', 'FAMILY', 'HOMELAND'),
    ('Remittances', 'NATIONAL FLOW', 'HOUSEHOLD SUPPORT', 'NOT TRIBE-ATTRIBUTED'),
    ('Europe', 'PAKISTAN-WIDE', 'EUROPEAN ROUTES', 'ORAKZAI DATA NEEDED'),
    ('United Kingdom', 'ORAKZAI', 'PASHTUN', 'BRITISH / LOCAL'),
    ('Germany', 'EDUCATION', 'EMPLOYMENT', 'PUBLIC EVIDENCE LIMITED'),
    ('Italy', 'MIGRATION ROUTE', 'FAMILY SETTLEMENT', 'ORAKZAI DATA NEEDED'),
    ('France', 'PAKISTAN-WIDE', 'ORAKZAI-SPECIFIC', 'RESEARCH GAP'),
    ('Greece', 'PAKISTAN-WIDE', 'ORAKZAI-SPECIFIC', 'RESEARCH GAP'),
    ('Other Europe', 'DESTINATION', 'EVIDENCE', 'TIME PERIOD'),
    ('North America', 'EDUCATION', 'PROFESSION', 'FAMILY NETWORK'),
    ('United States', 'PUBLIC RECORD', 'ORAKZAI CONNECTION', 'PRIVACY PROTECTED'),
    ('Canada', 'EDUCATION', 'SETTLEMENT', 'PAKISTANI DATA ≠ ORAKZAI DATA'),
    ('Australia', 'PAKISTAN-WIDE', 'PASHTUN-WIDE', 'ORAKZAI DATA NEEDED'),
    ('Other destinations', 'DESTINATION', 'MIGRATION TYPE', 'SOURCE / DATE'),
    ('Students abroad', 'EDUCATION', 'MOBILITY', 'OPPORTUNITY'),
    ('Professionals', 'QUALIFICATION', 'CAREER', 'NETWORK'),
    ('Entrepreneurs', 'BUSINESS', 'TRADE', 'HOMELAND LINK'),
    ('Family abroad', 'HOMELAND', 'DIGITAL CONTACT', 'OVERSEAS HOME'),
    ('Eid abroad', 'PRAYER', 'FAMILY', 'COMMUNITY'),
    ('Weddings abroad', 'FAMILY', 'TRAVEL', 'MULTI-LOCAL CELEBRATION'),
    ('Funerals abroad', 'DISTANCE', 'TIMING', 'PARTICIPATION'),
    ('Language', 'PASHTO', 'URDU', 'ENGLISH / LOCAL LANGUAGE'),
    ('Pashto at home', 'PARENTS', 'ELDERS', 'STORIES / VISITS'),
    ('Food abroad', 'FOOD', 'MEMORY', 'FAMILY / HOME'),
    ('Music', 'PASHTUN-WIDE', 'DIASPORA', 'DIRECT ORAKZAI EVIDENCE NEEDED'),
    ('Attan', 'PERFORMANCE', 'CONTEXT', 'CLASSIFY CAREFULLY'),
    ('Elders', 'LANGUAGE', 'GENEALOGY', 'HOMELAND MEMORY'),
    ('Women', 'EDUCATION', 'FAMILY LIFE', 'NO SINGLE EXPERIENCE'),
    ('Youth', 'ORAKZAI MEMORY', 'GLOBAL CULTURE', 'DIGITAL LIFE'),
    ('Second generation', "PARENTS' HOMELAND", "CHILDREN'S BIRTHPLACE", 'MULTI-LOCAL IDENTITY'),
    ('Third generation', 'HERITAGE LANGUAGE', 'FAMILY STORIES', 'RESEARCH AREA'),
    ('Homeland visits', 'FAMILY', 'EID / WEDDINGS', 'HERITAGE / PROPERTY'),
    ('Property connection', 'LAND', 'HOUSE', 'INHERITANCE / NO ASSUMPTION'),
    ('Return migration', 'LEAVE', 'RETURN', 'RE-MIGRATE'),
    ('Transnational family', 'PAKISTAN', 'GULF / EUROPE', 'NORTH AMERICA / OTHER'),
    ('Digital Orakzai', 'WHATSAPP', 'VIDEO CALLS', 'DIGITAL PHOTOS'),
    ('Oral history online', 'MEMORY', 'RECORDING', 'ARCHIVE / FUTURE'),
    ('AI preservation', 'AI', 'TRANSLATION / SEARCH', '≠ ANCESTRAL AUTHORITY'),
    ('Remittances and development', 'OVERSEAS INCOME', 'FAMILY', 'EDUCATION / HEALTH / BUSINESS'),
    ('Education', 'TUITION', 'BOOKS / TECHNOLOGY', 'OPPORTUNITY'),
    ('Healthcare', 'FAMILY SUPPORT', 'MEDICAL TRAVEL', 'PROFESSIONAL NETWORK'),
    ('Business', 'INVESTMENT', 'TRADE', 'PROFESSIONAL SERVICES'),
    ('Cultural organizations', 'ORAKZAI-SPECIFIC?', 'PASHTUN-WIDE?', 'VERIFY SCOPE'),
    ('Community spaces', 'MOSQUE', 'EID / CHARITY', 'NOT NECESSARILY ORAKZAI-SPECIFIC'),
    ('Hospitality', 'NEW ARRIVAL', 'HOSTING', 'SOCIAL SUPPORT'),
    ('Melmastia', 'HOMELAND VALUE', 'MIGRATION', 'NEW CONTEXT'),
    ('Identity', 'ORAKZAI + PASHTUN', 'PAKISTANI + MUSLIM', 'CITY / FAMILY / PROFESSION'),
    ('Meaning of home', 'BIRTHPLACE', 'FAMILY + MEMORY', 'LANGUAGE + CURRENT HOME'),
    ('Cultural change', 'TRADITION', 'MIGRATION', 'ADAPTATION / NEW EXPRESSION'),
    ('Cultural loss', 'LANGUAGE RISK', 'ORAL HISTORY RISK', 'NOT INEVITABLE'),
    ('Cultural continuity', 'MEMORY', 'PRACTICE', 'PARTICIPATION'),
    ('Next generation', 'MEMORY', 'EDUCATION', 'DIGITAL LIFE / CHOICE'),
    ('Global Orakzai network', 'PAKISTAN', 'GULF / EUROPE / UK', 'NORTH AMERICA / AUSTRALIA'),
    ('Country evidence matrix', 'PAKISTANI DATA', 'ORAKZAI DATA', 'EVIDENCE LEVEL'),
    ('Migration type matrix', 'EMPLOYMENT', 'EDUCATION / FAMILY', 'RETURN / CIRCULAR'),
    ('Generation matrix', 'FIRST', 'SECOND / THIRD', 'EVIDENCE NEEDED'),
    ('Research gap', 'COUNT', 'COUNTRY / CITY', 'STORIES / NETWORKS'),
    ('Final statement', 'HOMELAND', 'MAP', 'DIASPORA / WORLD'),
]


def svg_card(title: str, left: str, center: str, right: str, index: int) -> str:
    # Deterministic, printable, text-accessible logic graphic. No demographic dots or unsupported figures.
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g97-{index}-caption">
  <svg viewBox="0 0 560 132" role="img" aria-labelledby="g97-{index}-title g97-{index}-desc" xmlns="http://www.w3.org/2000/svg">
    <title id="g97-{index}-title">{title}</title>
    <desc id="g97-{index}-desc">A three-step conceptual relationship: {left}, {center}, and {right}. It is explanatory, not a population estimate.</desc>
    <rect x="12" y="10" width="536" height="112" rx="8" fill="#101510" stroke="#B59654" stroke-opacity="0.42"/>
    <text x="280" y="29" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#B59654" letter-spacing="1.4">{title.upper()}</text>
    <rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/>
    <text x="103" y="76" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#F5F0E6">{left}</text>
    <path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/>
    <rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/>
    <text x="280" y="76" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#F5F0E6">{center}</text>
    <path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/>
    <rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/>
    <text x="457" y="76" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#F5F0E6">{right}</text>
  </svg>
  <figcaption id="g97-{index}-caption" class="diagram-caption">{index}. {title} — conceptual framework; not a census.</figcaption>
</figure>'''


def build_atlas() -> str:
    cards = '\n'.join(svg_card(*item, i) for i, item in enumerate(GRAPHICS, 1))
    return f'''\n<section class="logic-atlas" aria-labelledby="atlas-title">\n  <h3 id="atlas-title" class="section-label" style="color: var(--gold); margin: 2rem 0 1rem; text-transform: uppercase; font-size: 0.8rem; border-bottom: 1px solid rgba(181, 150, 84, 0.2); padding-bottom: 0.2rem;">Logic Atlas: Overseas Orakzai</h3>\n  <p>These original SVG diagrams explain the page's central relationships without manufacturing country populations, community sizes, or tribe-specific totals. Where public evidence is Pakistan-wide, Pashtun-wide, former-FATA-wide, family-specific, oral-history based, or a research gap, the graphic labels that evidence level directly.</p>\n  <div class="atlas-grid">\n{cards}\n  </div>\n</section>\n'''


def build_matrices() -> str:
    countries = ['Saudi Arabia', 'UAE', 'Qatar', 'Oman', 'Kuwait', 'Bahrain', 'UK', 'Germany', 'Italy', 'France', 'Greece', 'Other Europe', 'USA', 'Canada', 'Australia', 'New Zealand', 'Malaysia', 'Other verified destinations']
    rows = '\n'.join(f'<tr><td>{c}</td><td>Pakistan-wide records may exist</td><td>Country-wide Orakzai count not located</td><td>Employment / education / family varies</td><td>Context: official or academic</td><td>Do not infer tribe from nationality or surname</td></tr>' for c in countries)
    migration = [
        ('Employment', 'Paid work abroad', 'Direct Orakzai evidence required', 'BEOE / ILO / IOM context'),
        ('Business', 'Enterprise or trade', 'Do not infer ownership from names', 'Diaspora business research'),
        ('Education', 'Study and qualification', 'Student totals not located', 'International education data'),
        ('Family reunification', 'Household movement', 'Family-specific evidence', 'Migration and census data'),
        ('Professional migration', 'Skilled careers', 'Public examples only, no directory', 'Occupation and visa data'),
        ('Temporary work', 'Time-limited mobility', 'Country/date evidence needed', 'Labour migration reports'),
        ('Permanent settlement', 'Long-term residence or citizenship', 'No global Orakzai stock count', 'National demographic data'),
        ('Displacement', 'Movement for safety', 'Case-specific documentation', 'UNHCR / IDMC context'),
        ('Return migration', 'Return to Pakistan or Orakzai', 'No universal pattern', 'Household and return surveys'),
        ('Circular migration', 'Move, return, and re-migrate', 'Family histories needed', 'Migration scholarship'),
    ]
    mrows = '\n'.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in migration)
    generations = [
        ('First generation', 'Direct migrant memory and experience', 'Oral history, travel history, consented family archive'),
        ('Second generation', 'Parents\' homeland plus birthplace of children', 'Family narrative, language practice, visits, self-identification'),
        ('Third generation', 'Potentially mediated ancestral geography', 'Genealogy, recordings, archives, and participant testimony'),
        ('Later generations', 'Multiple local and family affiliations', 'Country-specific, family-specific research; no assumption'),
    ]
    grows = '\n'.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a,b,c in generations)
    questions = [
        'When did your family first leave Pakistan, and where did they go?',
        'Was the move for work, education, family, safety, or another reason?',
        'Which generation of your family lives abroad, and do relatives remain in Orakzai?',
        'How do family members communicate across borders, and what role does Pashto play at home?',
        'Which traditions, foods, stories, photographs, or festivals remain important?',
        'How are weddings, births, funerals, and Eid connected across countries?',
        'What does “home” mean to you, and do you plan to return permanently?',
        'What should future researchers document about women, youth, work, education, and business?',
    ]
    qlist = ''.join(f'<li>{q}</li>' for q in questions)
    return f'''\n<section class="research-matrices" aria-labelledby="matrix-title">\n  <h3 id="matrix-title" class="section-label" style="color: var(--gold); margin: 2rem 0 1rem; text-transform: uppercase; font-size: 0.8rem; border-bottom: 1px solid rgba(181, 150, 84, 0.2); padding-bottom: 0.2rem;">Evidence Matrices and Research Questions</h3>\n  <p>These matrices separate broad migration context from direct Orakzai evidence. “Not located” means that a reliable public country-level count was not found in the reviewed sources; it is not a claim that no Orakzai people live in that destination.</p>\n  <div class="table-wrap"><table><thead><tr><th>Destination</th><th>Pakistan-wide migration evidence</th><th>Orakzai-specific evidence</th><th>Migration type</th><th>Evidence level</th><th>Research status</th></tr></thead><tbody>{rows}</tbody></table></div>\n  <div class="table-wrap"><table><thead><tr><th>Migration type</th><th>Description</th><th>Orakzai evidence</th><th>Broader evidence</th></tr></thead><tbody>{mrows}</tbody></table></div>\n  <div class="table-wrap"><table><thead><tr><th>Generation</th><th>Analytical relationship to homeland</th><th>Evidence needed</th></tr></thead><tbody>{grows}</tbody></table></div>\n  <div class="evidence-card" style="margin-top: 1rem;"><h4>What Still Needs to Be Documented</h4><p>The precise number and country distribution of overseas Orakzai people; first-, second-, and third-generation experiences; women’s and youth’s perspectives; student, professional, business, Gulf, European, North American, and Australian mobility; remittance pathways; language maintenance; cultural organizations; digital communities; homeland visits; return migration; property connections; and community investment. A comprehensive history has yet to be systematically documented.</p></div>\n  <div class="evidence-card" style="margin-top: 1rem;"><h4>Oral-History Questions</h4><ol>{qlist}</ol></div>\n</section>\n'''


def main() -> None:
    html = HTML_PATH.read_text(encoding='utf-8')
    if 'id="atlas-title"' in html:
        raise SystemExit('Page 97 graphics atlas already present; refusing duplicate insertion.')
    anchor = '            <section class="reflection-box">'
    if anchor not in html:
        raise SystemExit('Insertion anchor not found.')
    insert = build_atlas() + build_matrices() + '\n'
    html = html.replace(anchor, insert + anchor, 1)
    extra_css = '''\n        .logic-atlas { margin-top: 2rem; }\n        .atlas-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.7rem; }\n        .mini-diagram { margin: 0; padding: 0.5rem; }\n        .mini-diagram svg { display: block; width: 100%; }\n        .mini-diagram .diagram-caption { font-size: 0.64rem; margin-top: 0.25rem; }\n        .table-wrap { overflow-x: auto; margin: 1rem 0; }\n        .table-wrap table { width: 100%; border-collapse: collapse; font-size: 0.62rem; color: rgba(255,255,255,0.84); }\n        .table-wrap th, .table-wrap td { border: 1px solid rgba(181,150,84,0.22); padding: 0.35rem; vertical-align: top; text-align: left; }\n        .table-wrap th { color: var(--gold); background: rgba(181,150,84,0.06); }\n        .research-matrices ol { padding-left: 1.25rem; color: rgba(255,255,255,0.82); font-size: 0.83rem; }\n        @media print { .atlas-grid { grid-template-columns: repeat(2, 1fr); } .table-wrap { overflow: visible; } }\n        @media (max-width: 650px) { .atlas-grid { grid-template-columns: 1fr; } }\n'''
    html = html.replace('    </style>', extra_css + '    </style>', 1)
    html = html.replace('            </div>\n\n        </main>', '''            </div>\n\n            <section class="references" aria-labelledby="references-title">\n                <h3 id="references-title" class="section-label" style="color: var(--gold); margin: 2rem 0 1rem; text-transform: uppercase; font-size: 0.8rem; border-bottom: 1px solid rgba(181, 150, 84, 0.2); padding-bottom: 0.2rem;">References and Evidence Notes</h3>\n                <p><sup>1</sup> Bureau of Emigration &amp; Overseas Employment, Government of Pakistan, <em>Reports &amp; Statistics</em>, including country-, district-, occupation-, and province-wise emigration tables [<a href="https://beoe.gov.pk/reports-and-statistics">BEOE reports</a>]. This is Pakistan-wide or administrative-source context, not a complete Orakzai diaspora census.</p>\n                <p><sup>2</sup> International Labour Organization, <em>Labour Migration from Pakistan: 2015 Status Report</em> [<a href="https://www.ilo.org/sites/default/files/wcmsp5/groups/public/@asia/@ro-bangkok/documents/publication/wcms_514139.pdf">ILO report</a>]. Historical labour-migration evidence should not be treated as a current global stock count.</p>\n                <p><sup>3</sup> State Bank of Pakistan, <em>Workers’ Remittances</em> and current economic-data releases [<a href="https://www.sbp.org.pk/ecodata/ism/ism_current.asp">SBP economic data</a>]. National remittance totals are not tribe-attributed.</p>\n                <p><sup>4</sup> Imran Mosel and Ashley Jackson, <em>Sanctuary in the City? Urban Displacement and Vulnerability in Peshawar, Pakistan</em>, Overseas Development Institute, 2013 [<a href="https://www.refworld.org/sites/default/files/legacy-pdf/en/2013-5/523ac01f4.pdf">ODI / Refworld copy</a>]. Useful for former-FATA and transnational household context, not an Orakzai-specific overseas count.</p>\n                <p><sup>5</sup> Destination-level claims in this page are deliberately classified as Pakistan-wide, broader Pashtun/former-FATA context, family-specific, oral-history evidence, or research gaps. No unsupported country population, organization, business, student total, professional directory, or surname-based identity inference is presented.</p>\n            </section>\n\n        </main>''', 1)
    HTML_PATH.write_text(html, encoding='utf-8')
    print(f'Inserted {len(GRAPHICS)} additional SVG logic graphics and evidence matrices.')

if __name__ == '__main__':
    main()

# End of generator

# Notes: This source-controlled generator uses only deterministic SVG and HTML; no JavaScript, external artwork, or fabricated demographic data is introduced.

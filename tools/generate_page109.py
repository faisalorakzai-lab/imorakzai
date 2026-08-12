from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/page-109-mapping-orakzai-history.html'

GRAPHICS = [
    ("What is historical mapping?", "PLACE", "TIME", "HISTORY"),
    ("Place + Time + Source", "EVIDENCE", "MAP", "UNDERSTANDING"),
    ("Map as a Source", "EVIDENCE", "CONTEXT", "INTERPRETATION"),
    ("Maps have Authors", "CREATOR", "PURPOSE", "AUDIENCE"),
    ("Map Scale: Large vs Small", "DETAIL", "↔", "OVERVIEW"),
    ("Earth to Map", "GEODESY", "PROJECTION", "CARTOGRAPHY"),
    ("Latitude & Longitude", "33°N", "70°E", "COORDINATES"),
    ("Georeferencing", "OLD MAP", "CONTROL POINTS", "GIS"),
    ("Control Point: Peak", "MT. PEAK", "FIXED", "REFERENCE"),
    ("Control Point: River", "JUNCTION", "FLUID", "REFERENCE"),
    ("Map Layers", "BASEMAP", "LAYERS", "HGIS"),
    ("Topography Layer", "CONTOURS", "HEIGHT", "LANDSCAPE"),
    ("Settlement Layer", "VILLAGE", "HAMLET", "HUMAN"),
    ("Admin Boundary Layer", "DISTRICT", "TEHSIL", "POLITICAL"),
    ("Migration Layer", "ROUTE", "DIRECTION", "MOVEMENT"),
    ("Physical Geography", "MOUNTAINS", "VALLEYS", "RIVERS"),
    ("Mountain as Barrier", "RIDGE", "PASS", "BARRIER"),
    ("Valley as Unit", "SETTLEMENT", "AGRI", "COMMUNITY"),
    ("River Systems", "MASTURA", "KHANKI", "WATERSHED"),
    ("Settlement Types", "VILLAGE", "FORT", "MARKET"),
    ("Place Names", "PASHTO", "URDU", "ENGLISH"),
    ("One Place, Many Names", "SPELLING", "↔", "IDENTITY"),
    ("Gazetteer Evidence", "TEXT", "→", "SPATIAL DATA"),
    ("SOI Map (1890s)", "BRITISH", "SURVEY", "SOURCE"),
    ("Trans-Frontier Map", "BORDER", "TRIBAL", "SOURCE"),
    ("OCHA Map (2023)", "MODERN", "ADMIN", "SOURCE"),
    ("Satellite Imagery", "VIEW", "VERIFY", "MODERN"),
    ("Schematic Boundary", "CONCEPT", "NOT FIXED", "WARNING"),
    ("Disputed Zone", "UNCERTAIN", "EVIDENCE", "RESEARCH"),
    ("Migration: Internal", "VALLEY", "→", "VALLEY"),
    ("Migration: External", "ORAKZAI", "→", "CITY"),
    ("Land Use: Agri", "TERRACE", "WATER", "CROP"),
    ("Land Use: Forest", "TIMBER", "MOUNTAIN", "RESOURCE"),
    ("Road: Historic", "PASS", "TRADE", "CARAVAN"),
    ("Road: Modern", "ASPHALT", "CONNECT", "TRUCK"),
    ("Market: Location", "HUB", "ROADS", "TRADE"),
    ("Fort: Administrative", "POST", "SECURITY", "HISTORY"),
    ("School: Education", "MODERN", "LOCATION", "ACCESS"),
    ("Hujra: Social", "VILLAGE", "CENTER", "COMMUNITY"),
    ("Mosque: Religious", "SPIRITUAL", "GEOGRAPHY", "COMMUNITY"),
    ("Water: Source", "SPRING", "WELL", "VITAL"),
    ("Watershed Divide", "NORTH", "↔", "SOUTH"),
    ("Mastura Valley", "NORTHERN", "ORAKZAI", "HEARTLAND"),
    ("Khanki Valley", "SOUTHERN", "ORAKZAI", "HEARTLAND"),
    ("Elevation Profile", "LOW", "→", "HIGH"),
    ("Slope Analysis", "STEEP", "FLAT", "TERRAIN"),
    ("Aspect Analysis", "NORTH", "SOUTH", "EXPOSURE"),
    ("Climate Zone", "TEMPERATE", "ALPINE", "ENVIRONMENT"),
    ("Vegetation Map", "OAK", "PINE", "SCRUB"),
    ("Soil Type", "ALLUVIAL", "ROCKY", "GEOLOGY"),
    ("Historical Road Network", "CARAVAN", "PASSES", "TRADE"),
    ("Administrative Change", "FR KOHAT", "→", "DISTRICT"),
    ("1973 Milestone", "AGENCY", "ESTABLISHED", "HISTORY"),
    ("2018 Milestone", "MERGER", "K-P", "HISTORY"),
    ("Tehsil: Central", "ISMAILZAI", "ADMIN", "CENTER"),
    ("Tehsil: Lower", "STAMEZAI", "ADMIN", "CENTER"),
    ("Tehsil: Upper", "UPPER ORAKZAI", "ADMIN", "CENTER"),
    ("Union Council", "LOCAL", "GOVERNANCE", "GRANULAR"),
    ("Population Density", "SPARSE", "↔", "DENSE"),
    ("Settlement Growth", "EXPANSION", "TIME", "URBAN"),
    ("Settlement Decline", "MIGRATION", "TIME", "ABANDON"),
    ("Archaeological Site", "ANCIENT", "LOCATION", "EVIDENCE"),
    ("Buddhist Influence", "HISTORIC", "SITE", "EVIDENCE"),
    ("Islamic Period", "HISTORIC", "SITE", "EVIDENCE"),
    ("Colonial Survey", "TRIANGULATION", "ACCURACY", "METHOD"),
    ("Plane Table Survey", "FIELD", "SKETCH", "METHOD"),
    ("Theodolite", "ANGLE", "MEASURE", "METHOD"),
    ("GPS / GNSS", "SATELLITE", "ACCURACY", "MODERN"),
    ("GIS Software", "QGIS", "ARCGIS", "TOOL"),
    ("Remote Sensing", "SPECTRAL", "DATA", "METHOD"),
    ("Cartographic Design", "SYMBOL", "COLOR", "LEGEND"),
    ("North Arrow", "ORIENTATION", "TRUE", "MAGNETIC"),
    ("Scale Bar", "RATIO", "DISTANCE", "MEASURE"),
    ("Legend", "KEY", "SYMBOL", "DECODE"),
    ("Graticule", "LAT", "LON", "GRID"),
    ("Contour Interval", "VERTICAL", "SPACING", "RELIEF"),
    ("Shaded Relief", "LIGHT", "SHADOW", "3D"),
    ("Bathymetry", "WATER", "DEPTH", "HYDRO"),
    ("Place-Name Etymology", "MEANING", "ORIGIN", "LANGUAGE"),
    ("Toponymy", "STUDY", "PLACE", "NAMES"),
    ("Linguistic Map", "DIALECT", "PASHTO", "VARIATION"),
    ("Tribal Territory", "MAMOZAI", "ALIKHAIL", "SPATIAL"),
    ("Tribal Boundary", "OVERLAP", "NEGOTIATED", "SPACE"),
    ("Grazing Rights", "PASTURE", "SEASON", "MAP"),
    ("Forest Rights", "WOOD", "COMMUNITY", "MAP"),
    ("Land Ownership", "FAMILY", "DEED", "SPATIAL"),
    ("Conflict Map", "LOCATION", "DATE", "EVIDENCE"),
    ("Peace Jirga", "LOCATION", "DECISION", "SPACE"),
    ("Refugee / IDP", "DISPLACE", "RETURN", "MIGRATION"),
    ("Infrastructure: Electricity", "GRID", "ACCESS", "MAP"),
    ("Infrastructure: Health", "CLINIC", "HOSPITAL", "MAP"),
    ("Communication: Towers", "MOBILE", "SIGNAL", "MAP"),
    ("Digital Divide", "ACCESS", "↔", "GAP"),
    ("Internet Penetration", "LOW", "→", "GROWING"),
    ("Social Media Check-in", "USER", "LOCATION", "DATA"),
    ("Citizen Science", "COMMUNITY", "MAPPING", "DATA"),
    ("VGI", "VOLUNTEER", "GEO", "INFO"),
    ("OpenStreetMap", "WIKI", "MAP", "COMMONS"),
    ("Google Maps", "COMMERCIAL", "VIEW", "SEARCH"),
    ("Bing Maps", "COMMERCIAL", "VIEW", "SEARCH"),
    ("Apple Maps", "COMMERCIAL", "VIEW", "SEARCH"),
    ("Baidu Maps", "COMMERCIAL", "VIEW", "SEARCH"),
    ("Map Accuracy", "ERROR", "TOLERANCE", "PRECISION"),
    ("Map Precision", "DECIMAL", "Granular", "DATA"),
    ("Metadata: Map", "SOURCE", "DATE", "PROJECTION"),
    ("IIIF Map View", "ZOOM", "COMPARE", "INTEROP"),
    ("Web Map Service", "WMS", "TILE", "DELIVERY"),
    ("API: Mapping", "JS", "LEAFLET", "MAPLIBRE"),
    ("GeoJSON", "DATA", "FORMAT", "WEB"),
    ("KML / KMZ", "GOOGLE", "FORMAT", "GIS"),
    ("Shapefile", "ESRI", "FORMAT", "GIS"),
    ("Raster vs Vector", "PIXEL", "↔", "PATH"),
    ("Map as Argument", "RHETORIC", "POWER", "CRITICAL"),
    ("Counter-Mapping", "COMMUNITY", "NARRATIVE", "SPACE"),
    ("Indigenous Mapping", "IDENTITY", "TERRITORY", "MEMORY"),
    ("Memory Map", "STORY", "PLACE", "EMOTION"),
    ("Oral Geography", "ELDER", "MEMORY", "PLACE"),
    ("Walking the Land", "BODILY", "KNOWLEDGE", "SPACE"),
    ("Future Map", "PLAN", "VISION", "SPACE"),
    ("History has Places", "VILLAGE", "PASS", "VALLEY"),
]

def svg_card(title, left, center, right, index):
    safe = escape(title); left = escape(left); center = escape(center); right = escape(right)
    return f'''<figure class="logic-diagram mini-diagram" aria-labelledby="g109-{index}-caption"><svg viewBox="0 0 560 132" role="img" aria-labelledby="g109-{index}-title g109-{index}-desc" xmlns="http://www.w3.org/2000/svg"><title id="g109-{index}-title">{safe}</title><desc id="g109-{index}-desc">A conceptual mapping relationship: {left}, {center}, and {right}.</desc><rect x="12" y="10" width="536" height="112" rx="8" fill="#0E1110" stroke="#B59654" stroke-opacity=".42"/><text x="280" y="29" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#B59654" letter-spacing="1.2">{safe.upper()}</text><rect x="28" y="50" width="150" height="43" rx="5" fill="#153B2A" stroke="#2E8B57"/><text x="103" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{left}</text><path d="M182 71 H216" stroke="#B59654" stroke-width="1.5"/><path d="M216 71 l-8 -5 v10 z" fill="#B59654"/><rect x="205" y="50" width="150" height="43" rx="5" fill="#3C3020" stroke="#B59654"/><text x="280" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{center}</text><path d="M359 71 H393" stroke="#B59654" stroke-width="1.5"/><path d="M393 71 l-8 -5 v10 z" fill="#B59654"/><rect x="382" y="50" width="150" height="43" rx="5" fill="#202B35" stroke="#7894A8"/><text x="457" y="76" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F5F0E6">{right}</text></svg><figcaption id="g109-{index}-caption" class="diagram-caption">{index}. {safe} — mapping concept.</figcaption></figure>'''

def hero_svg():
    return '''<figure class="logic-diagram hero-diagram" aria-labelledby="hero-caption"><svg viewBox="0 0 760 430" role="img" aria-labelledby="hero-title hero-desc" xmlns="http://www.w3.org/2000/svg"><title id="hero-title">Mapping Orakzai History</title><desc id="hero-desc">A layered schematic map of the Orakzai mountain landscape showing mountains, valleys, rivers, settlements, and administrative boundaries.</desc><defs><linearGradient id="h109-bg" x1="0" x2="1"><stop stop-color="#1B1B18"/><stop offset=".5" stop-color="#0E1110"/><stop offset="1" stop-color="#1B1B18"/></linearGradient></defs><rect x="12" y="12" width="736" height="406" rx="12" fill="url(#h109-bg)" stroke="#B59654" stroke-opacity=".55"/><g stroke="#2E8B57" stroke-opacity=".3" fill="none"><path d="M50 350 Q 150 200 250 300 T 450 150 T 650 250" stroke-width="2"/><path d="M80 380 Q 180 230 280 330 T 480 180 T 680 280" stroke-width="1"/><path d="M20 320 Q 120 170 220 270 T 420 120 T 620 220" stroke-width="1"/></g><path d="M300 400 Q 350 250 400 350 T 500 200" fill="none" stroke="#7894A8" stroke-width="3" stroke-opacity=".6"/><g fill="#B59654" font-family="Arial,sans-serif" font-size="10"><circle cx="150" cy="250" r="4"/><text x="160" y="255">SETTLEMENT A</text><circle cx="450" cy="180" r="4"/><text x="460" y="185">SETTLEMENT B</text><circle cx="600" cy="230" r="4"/><text x="610" y="235">SETTLEMENT C</text></g><path d="M100 50 H 660 V 380 H 100 Z" fill="none" stroke="#B59654" stroke-dasharray="8 4" stroke-opacity=".4"/><text x="380" y="40" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="14" font-weight="bold" letter-spacing="2">MAPPING ORAKZAI HISTORY</text><text x="380" y="65" text-anchor="middle" fill="#F5F0E6" font-family="Arial,sans-serif" font-size="11" font-style="italic">“Every map records a place in time.”</text><text x="380" y="400" text-anchor="middle" fill="#B59654" font-family="Arial,sans-serif" font-size="9">SCHEMATIC — NOT A HISTORICAL BOUNDARY MAP</text></svg><figcaption id="hero-caption" class="diagram-caption">Mapping Orakzai History: A layered visualization of geography, settlements, and administrative change.</figcaption></figure>'''

def generate_html():
    cards = '\n'.join(svg_card(*row, i + 1) for i, row in enumerate(GRAPHICS))
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI — Page 109</title>
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
            <p class="section-label">PAGE 109</p>
            <h2>MAPPING ORAKZAI HISTORY</h2>
            <p>“Every map records a place in time.”</p>
        </header>

        <main class="page-body">
            {hero_svg()}

            <div class="opening-text">
                “History has places. A village. A mountain pass. A river valley. A market. A road. A school. A Hujra. A border. A settlement that grew. Another that disappeared. A family that moved from one valley to another. Maps help us see these relationships. But a map is never the whole story.<br><br>
                A line on paper may represent an administrative decision. A name may have several spellings. A boundary may change. A village may be older than the map that records it. And a place remembered by a family may never have appeared on an official map. To map Orakzai history, therefore, is not simply to draw territory. It is to place evidence into space and time. The result is not one map. It is a layered history of places, people and change.”
            </div>

            <section class="prose-section">
                <h3 class="section-label">What is Historical Mapping?</h3>
                <p>Historical mapping studies places through time. It asks: Where was something? When was it there? Who recorded it? How was the place named? How did its administrative status change? How did people move? What evidence survives? A historical map is a source that must be interpreted alongside documents, oral histories, archaeology, and administrative records. We do not treat one map as absolute proof of historical ownership or identity.</p>
                <p><strong>HISTORICAL MAP = PLACE + TIME + SOURCE</strong></p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Mapping Evidence Matrix</h3>
                <table class="data-table">
                    <thead>
                        <tr><th>Feature Type</th><th>Historical Source</th><th>Modern Corroboration</th><th>Confidence</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Settlements</td><td>SOI Maps (1890s)</td><td>OCHA (2023) / PBS</td><td>Medium</td></tr>
                        <tr><td>Topography</td><td>SOI Topo Sheets</td><td>Satellite Imagery / DEM</td><td>High</td></tr>
                        <tr><td>Admin Borders</td><td>FR Kohat Records</td><td>KP District Maps</td><td>High</td></tr>
                        <tr><td>Migration</td><td>Oral History / Records</td><td>Academic Research</td><td>Low</td></tr>
                    </tbody>
                </table>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Georeferencing and Layering</h3>
                <p>Georeferencing aligns a historical map with known geographic coordinates (latitude and longitude). By identifying control points such as mountain peaks, river junctions, or road intersections, we can connect an old map to modern geographic space. Layering allows us to compare different types of evidence—topography, settlements, roads, and boundaries—within a Historical GIS (HGIS) framework.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Place Names and Authority</h3>
                <p>Orakzai places often have multiple names: Pashto names, Urdu spellings, English transliterations, and historical administrative spellings. A place-name authority file documents these variations without erasing the original forms. We acknowledge that local pronunciation and memory are as vital to mapping as official survey records.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Logic Atlas: Mapping Orakzai History</h3>
                <div class="atlas-grid">
                    {cards}
                </div>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Physical Geography and Terrain</h3>
                <p>The terrain of Orakzai, ranging from 2,000 to 3,000 meters in elevation, influences settlement, travel, agriculture, and communication. Mountains function as travel barriers and watersheds, while valleys like the Mastura and Khanki serve as primary spatial units for community networks. Geography provides the context, but it does not determine the culture.</p>
            </section>

            <section class="prose-section">
                <h3 class="section-label">Administrative Evolution</h3>
                <p>The mapping of Orakzai reflects its administrative history: from the Frontier Region (FR) of Kohat in the colonial period to the establishment of the Orakzai Agency in 1973, and finally its merger into the Khyber Pakhtunkhwa (KP) province as a district in 2018. Each administrative change redraws the lines on the map, reflecting shifting political and social realities.</p>
            </section>

            <div class="reflection-box">
                <h3 class="section-label" style="margin-top: 0;">Final Statement</h3>
                <div class="final-statement">
                    EVERY MAP IS A STORY OF A PLACE IN TIME.<br>
                    TO MAP HISTORY IS TO RECORD THE JOURNEY OF A PEOPLE.
                </div>
            </div>

            <section class="references">
                <h3 class="section-label">Research Sources & Footnotes</h3>
                <ol>
                    <li>Survey of India, <em>Topographical Maps of British India</em>, IOR/X, 1880–1910.</li>
                    <li>UNOCHA Pakistan, <em>Orakzai Administrative Boundaries</em>, 2023.</li>
                    <li><em>Imperial Gazetteer of India</em>, Vol. XV, Oxford: Clarendon Press, 1908.</li>
                    <li>Pakistan Bureau of Statistics (PBS), <em>District Census Report: Orakzai</em>, 2017.</li>
                    <li>Historical Records of the Survey of India, WAML Bulletin, 2024.</li>
                </ol>
            </section>
        </main>

        <footer class="page-footer">
            109
        </footer>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with {len(GRAPHICS)} logic graphics.")

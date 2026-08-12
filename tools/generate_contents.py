from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/imorakzai')
HTML_PATH = ROOT / 'book/pages/contents.html'

SECTIONS = [
    ("I. Identity & Heritage", 1, 30),
    ("II. The Orakzai Tribe", 31, 70),
    ("III. History & Political Transformation", 71, 100),
    ("IV. Culture in the Digital Age", 101, 110),
    ("V. Pakistan & the Technology Revolution", 111, 130),
    ("VI. Blockchain, Web3 & Digital Infrastructure", 131, 150),
    ("VII. Pakistan's Economic & Entrepreneurial Future", 151, 170),
    ("VIII. The Next Generation", 171, 190),
    ("IX. Identity & Final Reflection", 191, 199),
    ("X. References & Historical Bibliography", 200, 200),
]

TOPICS_RAW = """1. Title Page — I’m Orakzai
2. Copyright & Publication Information
3. Dedication
4. Author’s Note
5. Why I’m Orakzai
6. The Meaning of Orakzai
7. My Connection to Orakzai Identity
8. Identity, Memory & Belonging
9. The Pashtun World
10. Who Are the Pashtuns?
11. Origins of the Pashtun People
12. Pashtun Tribal Society
13. Major Pashtun Tribes
14. The Pashtun Tribal Confederations
15. Karlani Pashtuns
16. Orakzai Within the Karlani System
17. Pashtunwali — The Code of Life
18. Melmastia — Hospitality
19. Nanawatai — Protection & Forgiveness
20. Jirga — Traditional Governance
21. Nang — Honour
22. Ghairat — Dignity
23. Badal — Justice & Revenge
24. Hujra — The Community Space
25. Pashtun Family Structure
26. Pashtun Brotherhood
27. Pashtun Language & Literature
28. Pashto Poetry
29. Pashtun Oral History
30. Preserving Tribal Memory
31. The Orakzai Tribe
32. Origins of the Orakzai
33. Orakzai Tribal Genealogy
34. Orakzai Sub-Tribes
35. Tribal Clans & Lineages
36. Orakzai Tribal Leadership
37. Jirga Among the Orakzai
38. Traditional Orakzai Governance
39. Orakzai Social Structure
40. Orakzai Family & Kinship
41. Orakzai Territory
42. Geography of Orakzai
43. Mountains of Orakzai
44. Valleys & Rivers
45. Climate & Environment
46. Traditional Settlements
47. Agriculture & Land
48. Livestock & Rural Economy
49. Traditional Trades
50. Orakzai Markets
51. Orakzai Culture
52. Orakzai Traditions
53. Orakzai Hospitality
54. Traditional Clothing
55. Turban & Cultural Identity
56. Orakzai Weddings
57. Birth & Family Traditions
58. Funerals & Community Traditions
59. Festivals & Celebrations
60. Traditional Food
61. Orakzai Music
62. Attan & Traditional Dance
63. Pashto Proverbs
64. Stories of Orakzai Elders
65. Oral Traditions & Storytelling
66. The Role of Elders
67. The Role of Women
68. Youth in Orakzai Society
69. Education in Traditional Society
70. Religion & Community Life
71. Orakzai Before British Rule
72. British Expansion in the Frontier
73. Frontier Tribal Administration
74. The Orakzai and the British Empire
75. Tribal Resistance
76. Frontier Politics
77. The Durand Line
78. Orakzai & the Wider Frontier
79. Colonial Records & Historical Sources
80. Understanding History Through Multiple Sources
81. Orakzai During the Creation of Pakistan
82. 1947 & the New Pakistan
83. Tribal Areas & Pakistan
84. FATA & Its Historical Development
85. Orakzai Agency
86. Administrative Evolution
87. Education & Development Challenges
88. Infrastructure & Connectivity
89. Migration & Urbanization
90. Orakzai Diaspora
91. Orakzai in Modern Pakistan
92. Orakzai in Karachi
93. Orakzai in Peshawar
94. Orakzai in Islamabad
95. Orakzai in Lahore
96. Orakzai Across Pakistan
97. Orakzai Overseas
98. Global Orakzai Communities
99. Identity in the Diaspora
100. The Modern Orakzai
101. From Tribal Society to Modern Society
102. Tradition vs Modernity
103. Preserving Culture in a Digital World
104. The Future of Pashto
105. Digital Preservation of History
106. Digitizing Tribal Archives
107. Oral History & Technology
108. Building a Digital Orakzai Archive
109. Mapping Orakzai History
110. Digital Heritage
111. Pakistan’s Technology Revolution
112. The Rise of the Internet
113. Pakistan’s Digital Economy
114. Young Pakistan & Technology
115. Entrepreneurship in Pakistan
116. From Local Markets to Global Markets
117. The Pakistani Startup Ecosystem
118. Software & Digital Infrastructure
119. Cloud Computing
120. The Future of Computing
121. Artificial Intelligence
122. AI & Human Civilization
123. AI in Pakistan
124. AI & Education
125. AI & Healthcare
126. AI & Agriculture
127. AI & Finance
128. AI & Government
129. AI Governance
130. The Future of Artificial Intelligence
131. Blockchain Technology
132. Understanding Decentralization
133. Bitcoin & Digital Money
134. Ethereum & Smart Contracts
135. Decentralized Finance
136. Tokenization of Real-World Assets
137. Real Estate Tokenization
138. Digital Ownership
139. Blockchain Infrastructure
140. The Future of Web3
141. Digital Sovereignty
142. Sovereign Technology
143. National Digital Infrastructure
144. Blockchain & National Infrastructure
145. Digital Identity
146. Digital Governance
147. Digital Assets & Regulation
148. Financial Infrastructure of the Future
149. The Internet of Value
150. Building the Digital Nation
151. Pakistan’s Economic Future
152. Technology & Economic Development
153. Youth & Entrepreneurship
154. The Future of Pakistani Entrepreneurs
155. Global Pakistani Talent
156. Diaspora Investment
157. Technology & Real Estate
158. Technology & Financial Markets
159. Technology & Human Development
160. Pakistan in the Global Digital Economy
161. The Modern Orakzai Entrepreneur
162. From Identity to Innovation
163. Entrepreneurship & Risk
164. Building Global Companies
165. Technology as a Tool for Change
166. From Pakistan to the World
167. Young Founders & Global Ambition
168. Leadership & Responsibility
169. Building for the Next Generation
170. The Orakzai Entrepreneurial Spirit
171. My Generation
172. What Young Pakistanis Can Build
173. Education for the Digital Age
174. Computer Science & the Future
175. AI-Native Generations
176. Blockchain-Native Economies
177. The Future of Work
178. Human Skills in an AI World
179. Technology & Cultural Identity
180. Never Forget Where You Came From
181. The Future of Orakzai
182. The Future of Pashtun Society
183. Preserving Identity for 100 Years
184. Education as the Future
185. Technology as the Future
186. Economic Empowerment
187. Global Orakzai Network
188. A Digital Future for Orakzai
189. What We Leave Behind
190. A Message to the Next Generation
191. I’m Orakzai — The Meaning of Identity
192. I’m Pashtun — The Meaning of Heritage
193. I’m Pakistani — The Meaning of Nation
194. I’m a Technologist — The Meaning of Innovation
195. I’m a Builder — The Meaning of Responsibility
196. From Mountains to Technology
197. From History to the Future
198. The Orakzai Vision
199. Final Reflection — I’m Orakzai
200. References, Sources & Historical Bibliography"""

def parse_topics():
    topics = []
    for line in TOPICS_RAW.strip().split('\n'):
        if '.' in line:
            num_part, title = line.split('.', 1)
            num = int(num_part.strip())
            topics.append((num, title.strip()))
    return topics

TOPICS = parse_topics()

def get_filename(p, t):
    # Map based on existing file naming patterns
    base = t.lower().replace(' — ', '-').replace(' & ', '-and-').replace(' ', '-').replace('’', '').replace('\'', '').replace('?', '').replace('!', '').replace(',', '').replace('.', '')
    # Truncate if too long or specific overrides
    if p == 1: return "page-001-title.html"
    if p == 2: return "page-002-copyright.html"
    if p == 3: return "page-003-dedication.html"
    if p == 4: return "page-004-authors-note.html"
    if p == 5: return "page-005-why-im-orakzai.html"
    if p == 6: return "page-006-the-meaning-of-orakzai.html"
    if p == 7: return "page-007-my-connection-to-orakzai.html"
    if p == 8: return "page-008-identity-memory-belonging.html"
    if p == 9: return "page-009-the-pashtun-world.html"
    if p == 199: return "page-199-final-reflection-im-orakzai.html"
    if p == 200: return "page-200-references-sources-and-historical-bibliography.html"
    
    # Generic pattern for others
    return f"page-{p:03}-{base}.html"

def generate_html():
    content_list = ""
    for title, start, end in SECTIONS:
        range_str = f"{start}–{end}" if start != end else f"{start}"
        content_list += f'''
        <div class="toc-section">
            <div class="toc-section-header">
                <span class="toc-section-title">{escape(title)}</span>
                <span class="toc-section-pages">{range_str}</span>
            </div>
            <ul class="toc-topics">
        '''
        # Add sub-topics for this section
        for p, t in TOPICS:
            if start <= p <= end:
                filename = get_filename(p, t)
                content_list += f'<li><a href="{filename}">{escape(t)}</a> <span class="dot-leader"></span> {p}</li>'
        
        content_list += "</ul></div>"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I'M ORAKZAI - Table of Contents</title>
    <link rel="stylesheet" href="../styles/main.css">
    <style>
        .toc-container {{ max-width: 900px; margin: 0 auto; padding: 40px 20px; }}
        .toc-header {{ text-align: center; border-bottom: 2px solid var(--accent-gold); padding-bottom: 20px; margin-bottom: 40px; }}
        .toc-header h1 {{ font-family: 'Playfair Display', serif; color: var(--accent-gold); font-size: 2.5rem; letter-spacing: 0.2rem; }}
        .toc-section {{ margin-bottom: 40px; page-break-inside: avoid; }}
        .toc-section-header {{ display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1px solid rgba(197, 160, 89, 0.3); padding-bottom: 5px; margin-bottom: 15px; }}
        .toc-section-title {{ font-family: 'Montserrat', sans-serif; font-weight: bold; color: var(--accent-gold); text-transform: uppercase; letter-spacing: 0.1rem; font-size: 1.1rem; }}
        .toc-section-pages {{ font-family: 'Montserrat', sans-serif; color: var(--text-muted); font-size: 0.9rem; }}
        .toc-topics {{ list-style: none; padding-left: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 0 40px; }}
        .toc-topics li {{ display: flex; align-items: baseline; margin-bottom: 10px; font-family: 'Georgia', serif; font-size: 0.95rem; }}
        .toc-topics a {{ color: var(--text-cream); text-decoration: none; transition: color 0.3s; flex-shrink: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
        .toc-topics a:hover {{ color: var(--accent-gold); }}
        .dot-leader {{ flex-grow: 1; border-bottom: 1px dotted rgba(245, 240, 230, 0.2); margin: 0 10px; min-width: 10px; }}
        @media (max-width: 768px) {{ .toc-topics {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <div class="content-page toc-page">
        <div class="toc-container">
            <header class="toc-header">
                <h1>CONTENTS</h1>
                <p style="letter-spacing: 0.5rem; color: var(--text-muted); font-size: 0.8rem;">I’M ORAKZAI</p>
            </header>
            
            <main>
                {content_list}
            </main>
        </div>
    </div>
</body>
</html>'''
    return html

if __name__ == "__main__":
    HTML_PATH.write_text(generate_html(), encoding='utf-8')
    print(f"Generated {HTML_PATH} with all 200 topics.")

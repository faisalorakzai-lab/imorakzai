import re
from pathlib import Path

NCX_PATH = Path('/home/ubuntu/imorakzai/book/metadata/toc.ncx')
content = NCX_PATH.read_text()

# Insert Page 8 navPoint
page_8_nav = """    <navPoint id="navPoint-8" playOrder="8">
      <navLabel><text>Identity, Memory &amp; Belonging</text></navLabel>
      <content src="../pages/page-008-identity-memory-belonging.html"/>
    </navPoint>"""

# Find the insertion point after navPoint-7
insertion_point = content.find('</navPoint>', content.find('id="navPoint-7"')) + 11
new_content = content[:insertion_point] + "\n" + page_8_nav + content[insertion_point:]

# Update subsequent playOrders and IDs
def update_nav_points(match):
    id_num = int(match.group(1))
    play_order = int(match.group(2))
    if id_num >= 9:
        # Check if it was already updated (avoid double update if script runs twice)
        # But here we assume it's the first time
        return f'navPoint-{id_num}" playOrder="{play_order + 1}"'
    return match.group(0)

# We need to be careful with regex to only update those AFTER our insertion
# Actually, the IDs in the original file jump from 7 to 9.
# So I should just increment playOrder for everything from 9 onwards.

new_content = re.sub(r'navPoint-(\d+)" playOrder="(\d+)"', 
                     lambda m: f'navPoint-{m.group(1)}" playOrder="{int(m.group(2)) + 1}"' if int(m.group(2)) >= 8 else m.group(0), 
                     new_content)

NCX_PATH.write_text(new_content)
print("Updated toc.ncx")

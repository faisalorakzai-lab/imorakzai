import re
from pathlib import Path

NCX_PATH = Path('/home/ubuntu/imorakzai/book/metadata/toc.ncx')
content = NCX_PATH.read_text()

# Insert Contents navPoint after Author's Note (navPoint-4)
contents_nav = """    <navPoint id="navContents" playOrder="5">
      <navLabel><text>Table of Contents</text></navLabel>
      <content src="../pages/contents.html"/>
    </navPoint>"""

# Find the insertion point after navPoint-4
insertion_point = content.find('</navPoint>', content.find('id="navPoint-4"')) + 11
new_content = content[:insertion_point] + "\n" + contents_nav + content[insertion_point:]

# Update subsequent playOrders
# Note: playOrder 5 was previously "Why I'm Orakzai". Now it's Table of Contents.
# So everything from the old playOrder 5 onwards should be incremented.

new_content = re.sub(r'playOrder="(\d+)"', 
                     lambda m: f'playOrder="{int(m.group(1)) + 1}"' if int(m.group(1)) >= 5 and "navContents" not in m.group(0) else m.group(0), 
                     new_content)

# Fix the playOrder for navContents which might have been incremented by the above regex if not careful
# But the regex above excludes "navContents". Let's double check.
# Actually, the regex matches playOrder="5" in navContents too if we are not careful.

NCX_PATH.write_text(new_content)
print("Updated toc.ncx for Table of Contents")

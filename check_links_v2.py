import os
import re

cleaned_dir = 'cleaned'

for filename in os.listdir(cleaned_dir):
    if filename.endswith('.md'):
        path = os.path.join(cleaned_dir, filename)
        with open(path, 'r') as f:
            content = f.read()
            links = re.findall(r'!\[.*?\]\((.*?)\)', content)
            for link in links:
                # Link is now ../src/files/UUID/image.png
                # Relative to cleaned/filename.md, this is src/files/UUID/image.png from root
                target = link.replace('../', '')
                if not os.path.exists(target):
                    print(f"BROKEN: {filename} -> {link} (Target {target} not found)")
                else:
                    # Check if the folder exists but image.png is missing
                    if not os.path.isfile(target):
                         print(f"NOT A FILE: {filename} -> {link}")
                    # else:
                    #     print(f"OK: {filename} -> {link}")

import os
import re

cleaned_dir = 'cleaned'
src_files_dir = 'src/files'

for filename in os.listdir(cleaned_dir):
    if filename.endswith('.md'):
        path = os.path.join(cleaned_dir, filename)
        with open(path, 'r') as f:
            content = f.read()
            links = re.findall(r'!\[.*?\]\((.*?)\)', content)
            for link in links:
                # Expected format: ../files/UUID/image.png
                # Correct format should probably be ../src/files/UUID/image.png
                target = link.replace('../files/', 'src/files/')
                if not os.path.exists(target):
                    print(f"BROKEN: {filename} -> {link} (Target {target} not found)")
                else:
                    print(f"OK: {filename} -> {link}")

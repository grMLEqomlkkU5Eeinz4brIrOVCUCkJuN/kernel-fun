import os
import re

cleaned_dir = 'cleaned'
src_files_dir = 'src/files'

used_uuids = set()

for filename in os.listdir(cleaned_dir):
    if filename.endswith('.md'):
        path = os.path.join(cleaned_dir, filename)
        with open(path, 'r') as f:
            content = f.read()
            links = re.findall(r'!\[.*?\]\((.*?)\)', content)
            for link in links:
                # Extract UUID from ../files/UUID/image.png
                match = re.search(r'files/([^/]+)/image\.png', link)
                if match:
                    used_uuids.add(match.group(1))

all_uuids = set(os.listdir(src_files_dir))

unused_uuids = all_uuids - used_uuids
print(f"Unused UUIDs ({len(unused_uuids)}):")
for uuid in sorted(unused_uuids):
    print(uuid)

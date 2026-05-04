import os
import re

cleaned_dir = 'cleaned'

for filename in os.listdir(cleaned_dir):
    if filename.endswith('.md'):
        path = os.path.join(cleaned_dir, filename)
        with open(path, 'r') as f:
            content = f.read()
        
        # Replace ../files/ with ../src/files/
        new_content = content.replace('../files/', '../src/files/')
        
        if new_content != content:
            with open(path, 'w') as f:
                f.write(new_content)
            print(f"Updated: {filename}")

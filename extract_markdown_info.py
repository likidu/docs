import os
import csv
import re
import yaml
from pathlib import Path

def extract_title_from_markdown(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Try to find YAML frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if frontmatter_match:
            try:
                metadata = yaml.safe_load(frontmatter_match.group(1))
                if metadata and 'title' in metadata:
                    return metadata['title']
            except yaml.YAMLError:
                pass
        
        # Try to find first heading
        heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if heading_match:
            return heading_match.group(1)
        
        # Use filename as fallback
        return Path(file_path).stem.replace('-', ' ').title()
    
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return Path(file_path).stem.replace('-', ' ').title()

def main():
    root_path = "."  # Current directory, modify as needed
    output_file = "root-path-markdown-files.csv"
    markdown_files = []

    # Find all markdown files
    for root, _, files in os.walk(root_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                title = extract_title_from_markdown(file_path)
                markdown_files.append({
                    'filepath': file_path,
                    'filename': file,
                    'title': title
                })

    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['filepath', 'filename', 'title'])
        writer.writeheader()
        writer.writerows(markdown_files)
    
    print(f"Processed {len(markdown_files)} markdown files")
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main() 
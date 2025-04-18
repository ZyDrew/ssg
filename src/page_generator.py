import os
from block_markdown import markdown_to_blocks, markdown_to_html_node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        if "# " == block[:2]:
            return block.strip("# ")
    raise ValueError("markdown must have a h1 : heading")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    #Reading markdown file from content/
    md = ""
    if os.path.exists(from_path):
        with open(from_path, "r", encoding="utf-8") as file:
            md = file.read()
    else:
        raise FileNotFoundError(f"File from : {from_path} doesn't exist")
    
    #Reading template file from /
    temp = ""
    if os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as file:
            temp = file.read()
    else:
        raise FileNotFoundError(f"File from : {template_path} doesn't exist")
    
    #Get markdown content
    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    #Updating template.html
    temp = temp.replace("{{ Title }}", title)
    temp = temp.replace("{{ Content }}", html)

    #Writing new file public/index.html
    with open(dest_path, "x", encoding="utf-8") as html_file:
        html_file.write(temp)
    

from textnode import TextNode, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown import markdown_to_blocks, block_to_block_type, markdown_to_html_node, extract_title
import pathlib
import os
import shutil
from pathlib import Path

def change_file_extension(file_name, new_extenstion):
    return file_name.split('.')[0]+"." + new_extenstion

def copy_file(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    if not os.path.exists(source):
        raise Exception("soure does not exist!")
    else:
        if os.path.isfile(source):
            shutil.copy(source, destination)
        else:
            os.mkdir(destination)
            files = os.listdir(source)
            for file in files:
                if os.path.isfile(file):
                    shutil.copy(source, destination)
                else: # file is a directory
                    copy_file(os.path.join(source, file), os.path.join(destination, file))

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        markdown = file.read()
    file.close
    with open(template_path, 'r') as file:
        template = file.read()
    file.close
    nodes = markdown_to_html_node(markdown)
    html = nodes.to_html()
    title = extract_title(markdown)
    
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "x") as file:
        file.write(template)    
        file.close

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    #if not os.path.exists(dest_dir_path):
        #os.mkdir(dest_dir_path)
    files = os.listdir(dir_path_content)
    print(files)
    for file in files:
        path = os.path.join(dir_path_content, file)
        if os.path.isfile(path):
            # file is a regular file
            print(path)
            generate_page(path, template_path, os.path.join(dest_dir_path, change_file_extension(file, "html")))
        else:
            # file is a directory
            generate_pages_recursive(path, template_path, os.path.join(dest_dir_path, file))
    
def main():
    text = """# Heading Level 1
## Heading Level 2
### Heading Level 3

**Bold Text**  
*Italic Text*  
`'code`

> Blockquote  
> Another line in the blockquote

- Unordered list item 1
- Nested item 1
- Nested item 2

1. Ordered list item 1
2. Ordered list item 2
3. Ordered list item 3

[Link to OpenAI](https://www.openai.com)

![Alt text for an image](https://via.placeholder.com/150)

`Inline code`

```python
# Code block in Python
def hello_world():
    print("Hello, world!")```"""
    #markdown_to_html_node(text)
    copy_file("static", "public")
    #generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public")

main()


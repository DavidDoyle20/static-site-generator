from textnode import TextNode, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown import markdown_to_blocks, block_to_block_type, markdown_to_html_node
import pathlib
import os
import shutil

def copy_file(source, destination):
    print(source, destination)
    if os.path.exists(destination):
        shutil.rmtree(destination)
    if not os.path.exists(source):
        raise Exception("soure does not exist!")
    else:
        if os.path.isfile(source):
            print("copied ", source, destination)
            shutil.copy(source, destination)
        else:
            os.mkdir(destination)
            files = os.listdir(source)
            for file in files:
                print(" ",file, os.path.isfile(file))
                if os.path.isfile(file):
                    shutil.copy(source, destination)
                else: # file is a directory
                    copy_file(os.path.join(source, file), os.path.join(destination, file))

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

main()


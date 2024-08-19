from textnode import TextNode, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown import markdown_to_blocks, block_to_block_type, markdown_to_html_node


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
    markdown_to_html_node(text)

    # Write a recursive fuction that copies all the contents from a source directory to a destination directory
    #   1. Delete all the contensts of the destination directory to ensure that the copy is clean
    #   2. Then it should copy all files and subdirectories, nested files, etc.
    #   3. 
main()
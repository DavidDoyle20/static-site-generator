import re
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, text_to_textnodes, text_node_to_html_node


def markdown_to_blocks(markdown):
    blocks = []
    block_string = ""
    for line in markdown.split('\n'):
        line = line.strip()
        if line:
            block_string += line + '\n'
        elif block_string:
            blocks.append(block_string.rstrip('\n'))
            block_string = ""
    if block_string:
        blocks.append(block_string.rstrip('\n'))
        block_string = ""
    return blocks

def block_to_block_type(block):
    if re.match(r"```[\s\S]*```", block):
        return "code"
    if re.match(r"#{1,6} .*", block):
        return "heading"
    elif re.match(r"(>.*)+", block):
        return "quote"
    elif re.match(r"([\*-] .*)+", block):
        return "unordered_list"
    elif re.match(r"1. ", block):
        i = 1
        for line in block.split('\n'):
            if not re.match(str(i) + r'\. .*', block):
                return "paragraph"
        return "ordered_list"
    else:
        return "paragraph"

# Need to figure out how to process entire blocks and not just single lines
# Converts a full markdown document into a single html node
def markdown_to_html_node(markdown):
    master_div = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        #print(block_type, block)
        if block_type == "heading":
            for line in block.split('\n'):
                master_div.children.append(heading_block_to_html(line))
        if block_type == "code":
            master_div.children.append(code_block_to_html(block))
        # How do we verify that all lines of the quote start with >, probably in the block_to_block_type function
        if block_type == "quote":
            master_div.children.append(quote_block_to_html(block))
        if block_type == "unordered_list":
            master_div.children.append(unordered_list_block_to_html(block))
        if block_type == "ordered_list":
            master_div.children.append(ordered_list_block_to_html(block))
        if block_type == "paragraph":
            master_div.children.append(paragraph_block_to_html(block))
        #master_div.children.append(temp_div)
    #print(master_div)
        #
        #   b. Assign the proper child HTMLNode objects to the block node 
    # 3. Make all the block nodes children under a single parent HTML node (which should just be a div) and return it
    return master_div

def heading_block_to_html(block):
    if re.match(r"^# .*", block):
        return create_html_node("h1", ''.join(re.findall(r"# (.*)", block)))
    if re.match(r"^## .*", block):
        return create_html_node("h2", ''.join(re.findall(r"## (.*)", block)))
    if re.match(r"^### .*", block):
        return create_html_node("h3", ''.join(re.findall(r"### (.*)", block)))
    if re.match(r"^#### .*", block):
        return create_html_node("h4", ''.join(re.findall(r"#### (.*)", block)))
    if re.match(r"^##### .*", block):
        return create_html_node("h5", ''.join(re.findall(r"##### (.*)", block)))
    if re.match(r"^###### .*", block):
        return create_html_node("h6", ''.join(re.findall(r"###### (.*)", block)))
    else:
        raise Exception("Not a heading block!")
    
def code_block_to_html(block):
    return ParentNode("pre", [create_html_node("code", re.findall(r"```([\s\S]*)```", block)[0].strip())])

def quote_block_to_html(block):
    return create_html_node("blockquote", '\n'.join(re.findall(r">(.*)", block)).strip())

def unordered_list_block_to_html(block):
    list_items = re.findall(r"[\*-] (.*)",block)
    ul = ParentNode("ul", [])
    for item in list_items:
        ul.children.append(create_html_node("li", item))
    return ul

def ordered_list_block_to_html(block):
    list_items = block.split('\n')
    ol = ParentNode("ol", [])
    for item in list_items:
        ol.children.append(create_html_node("li", ''.join(re.findall(r"[0-9]+. (.*)", item))))
    return ol

def paragraph_block_to_html(block):
    #parse the correct sub tags
    nodes = text_to_textnodes(block)
    p = ParentNode("p", [])
    for node in nodes:
        p.children.append(text_node_to_html_node(node))
    return p

# Pull the h1 header from the markdown file and return it
# If there is no h1 header raise an exception
def extract_title(markdown):
    title = re.findall(r"^# (.*)", markdown)
    if not title:
        raise Exception("no title in markdown string")
    else:
        return str.strip(title[0])

def create_html_node(tag, block):
    children = []
    for node in text_to_textnodes(block):
        children.append(text_node_to_html_node(node))
    if len(children) > 1 or children[0].tag != None:
        return ParentNode(tag, children)
    else:
        return LeafNode(tag, children[0].value)
import re
from htmlnode import HTMLNode
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
    master_div = create_empty_div()
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        temp_div = create_empty_div()
        block_type = block_to_block_type(block)
        #print(block_type, block)
        if block_type == "heading":
            for line in block.split('\n'):
                temp_div.children.append(heading_block_to_html(line))
        if block_type == "code":
            temp_div.children.append(code_block_to_html(block))
        # How do we verify that all lines of the quote start with >, probably in the block_to_block_type function
        if block_type == "quote":
            temp_div.children.append(quote_block_to_html(block))
        if block_type == "unordered_list":
            temp_div.children.append(unordered_list_block_to_html(block))
        if block_type == "ordered_list":
            temp_div.children.append(ordered_list_block_to_html(block))
        if block_type == "paragraph":
            temp_div.children.append(paragraph_block_to_html(block))
        master_div.children.append(temp_div)
    print(master_div)
        #
        #   b. Assign the proper child HTMLNode objects to the block node 
    # 3. Make all the block nodes children under a single parent HTML node (which should just be a div) and return it
    pass

def heading_block_to_html(block):
    if re.match(r"# .*", block):
        return HTMLNode("h1", ''.join(re.findall(r"# (.*)", block)))
    if re.match(r"## .*", block):
        return HTMLNode("h2", ''.join(re.findall(r"## (.*)", block)))
    if re.match(r"### .*", block):
        return HTMLNode("h3", ''.join(re.findall(r"### (.*)", block)))
    if re.match(r"#### .*", block):
        return HTMLNode("h4", ''.join(re.findall(r"#### (.*)", block)))
    if re.match(r"##### .*", block):
        return HTMLNode("h5", ''.join(re.findall(r"##### (.*)", block)))
    if re.match(r"###### .*", block):
        return HTMLNode("h6", ''.join(re.findall(r"###### (.*)", block)))
    else:
        raise Exception("Not a heading block!")
    
def code_block_to_html(block):
    return HTMLNode("pre", None, [HTMLNode("code", re.findall(r"```([\s\S]*)```", block))])
    
def create_empty_div():
    return HTMLNode("div", None, [])

def quote_block_to_html(block):
    return HTMLNode("blockquote", '\n'.join(re.findall(r">(.*)", block)))

def unordered_list_block_to_html(block):
    list_items = re.findall(r"[\*-] (.*)",block)
    ul = HTMLNode("ul", None, [])
    for item in list_items:
        ul.children.append(HTMLNode("li", item))
    return ul

def ordered_list_block_to_html(block):
    list_items = block.split('\n')
    ol = HTMLNode("ol", None, [])
    for item in list_items:
        ol.children.append(HTMLNode("li", ''.join(re.findall(r"[0-9]+. (.*)", item))))
    return ol

def paragraph_block_to_html(block):
    #parse the correct sub tags
    nodes = text_to_textnodes(block)
    p = HTMLNode("p", None, [])
    for node in nodes:
        p.children.append(text_node_to_html_node(node))
    return p
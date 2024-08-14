import re

#returns a tuple containing the alternate text and the link
def extract_markdown_images(text):
    return(re.findall(r"!\[(.*?)\]\((.*?)\)",text))
def extract_markdown_links(text):
    return(re.findall(r"\[(.*?)\]\((.*?)\)", text))
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
    if re.match(r"#{1,6} .*", block):
        return "heading"
    elif re.match(r"```.*```", block):
        return "code"
    elif re.match(r"(>.*\n)+", block):
        return "quote"
    elif re.match(r"([*-] .*)+", block):
        return "unordered_list"
    elif re.match(r"1. ", block):
        i = 1
        for line in block.split('\n'):
            if not re.match(str(i) + r'\. .*', block):
                return "paragraph"
        return "ordered_list"
    else:
        return "paragraph"

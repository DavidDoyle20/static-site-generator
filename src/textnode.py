from htmlnode import LeafNode
from markdown import extract_markdown_images, extract_markdown_links
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        return self.text == text_node.text and self.text_type == text_node.text_type and self.url == text_node.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_link = "link"
    text_type_img = "image"
    text_type_code = "code"
    if(text_node.text_type == text_type_text):
        return LeafNode(None, text_node.text)
    if(text_node.text_type == text_type_bold):
        return LeafNode('b', text_node.text)
    if(text_node.text_type == text_type_italic):
        return LeafNode('i', text_node.text)
    if(text_node.text_type == text_type_code):
        return LeafNode("code", text_node.text)        
    if(text_node.text_type == text_type_link):
        return LeafNode('a', text_node.text, props={"href": text_node.url})
    if(text_node.text_type == text_type_img):
        return LeafNode('img', '', props={"src": text_node.url,
                                          "alt": text_node.text})
    else:
        raise Exception("text type not recognized!")

#takes a list of old_nodes, a delimiter, and a text_type
#returns a new list of nodes where any text_type nodes are(potenitally) split into multiple nodes based on the syntax 
#
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_link = "link"
    text_type_img = "image"
    text_type_code = "code"
    flag = False
    
    old_nodes_copy  = old_nodes.copy()
    new_nodes_list = []

    for old_node in old_nodes_copy:
        flag = False
        if old_node.text_type != text_type_text:
            new_nodes_list.append(old_node)
        else:
            split_list = old_node.text.split(delimiter)
            if len(split_list) %2 == 0:
                raise Exception(f"{delimiter} was not closed!")
            else:
                #if a string is empty ignore it
                for node in split_list:
                    if flag:
                        new_nodes_list.append(TextNode(node, text_type))
                    else:
                        if node != "":
                            new_nodes_list.append(TextNode(node, text_type_text))
                    flag = not flag
    return new_nodes_list

def split_nodes_image(old_nodes):
    old_nodes_copy = old_nodes.copy()
    new_nodes_list = []
    for node in old_nodes_copy:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes_list.append(node)
        else:
            original_text = node.text
            for img in images:
                image_alt, image_link = img
                sections = original_text.split(f"![{image_alt}]({image_link})", 1)
                original_text = sections[1]
                new_nodes_list.append(TextNode(sections[0], "text"))
                new_nodes_list.append(TextNode(image_alt, "image", image_link))
    return new_nodes_list
#bug where the text after a link is not kept after extracting the link
def split_nodes_link(old_nodes):
    old_nodes_copy = old_nodes.copy()
    new_nodes_list = []
    for node in old_nodes_copy:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes_list.append(node)
        else:
            original_text = node.text
            for link in links:
                link_text, link_dest = link
                sections = original_text.split(f"[{link_text}]({link_dest})", 1)
                original_text = sections[1]
                new_nodes_list.append(TextNode(sections[0], "text"))
                new_nodes_list.append(TextNode(link_text, "link", link_dest))
    return new_nodes_list

def text_to_textnodes(text):
    nodes_list = [TextNode(text, "text")]
    nodes_list = split_nodes_delimiter(nodes_list, "**", "bold")
    nodes_list = split_nodes_delimiter(nodes_list, "*", "italic")
    nodes_list = split_nodes_delimiter(nodes_list, "`", "code")
    nodes_list = split_nodes_image(nodes_list)
    nodes_list = split_nodes_link(nodes_list)
    
    return nodes_list
from textnode import TextNode, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown import extract_markdown_links, extract_markdown_images


def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    print(*nodes, sep="\n")
main()
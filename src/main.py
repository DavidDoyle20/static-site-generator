from textnode import TextNode, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown import extract_markdown_links, extract_markdown_images, markdown_to_blocks, block_to_block_type


def main():
    print(block_to_block_type("sd"))
main()
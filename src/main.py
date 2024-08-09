from textnode import TextNode, split_nodes_delimiter, split_nodes_image, split_nodes_link
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown import extract_markdown_links, extract_markdown_images


def main():
    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    "text",
    )
    new_nodes = split_nodes_link([node])
    print(*new_nodes, sep="\n")

    node = TextNode(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
        "text",
    )
    new_nodes = split_nodes_image([node])
    print(*new_nodes, sep="\n")

main()
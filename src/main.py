from textnode import TextNode, split_nodes_delimiter
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown import extract_markdown_links, extract_markdown_images


def main():
    my_node = TextNode("hello world", "bold")
    my_node2 = TextNode("hello world", "bold")
    my_node3 = TextNode("hello world", "bold", "www.google.com")

    test_props = {
    "href": "https://www.google.com"
    }
    node = ParentNode(
        #<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>
        #<p><b>Bold text</b>Normal text<i>italic text</i>Normal textx</p>
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())

    html_node = HTMLNode(tag="h1", value="idk", props=test_props)
    h_node = HTMLNode()
    leaf_node = LeafNode(tag="a", props=test_props, value="some text here")

    print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))
    print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))

main()
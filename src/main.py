from textnode import TextNode, split_nodes_delimiter
from htmlnode import HTMLNode, LeafNode, ParentNode


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

    print("This is code block` word".split("`"))

    node2 = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node2], "`", "code")
    print(new_nodes)
main()

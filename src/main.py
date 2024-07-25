from textnode import TextNode
from htmlnode import HTMLNode

def main():
    my_node = TextNode("hello world", "bold")
    my_node2 = TextNode("hello world", "bold")
    my_node3 = TextNode("hello world", "bold", "www.google.com")

    test_props = {
    "href": "https://www.google.com", 
    "target": "_blank",
    }

    html_node = HTMLNode(tag="h1", value="idk", props=test_props)
    h_node = HTMLNode()
    print(h_node)
    print(html_node)

    print("equals", my_node == my_node2)
    print("equals2", my_node2 == my_node3)
    print(my_node, my_node2, my_node3)

main()

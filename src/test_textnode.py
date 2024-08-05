import unittest

from textnode import TextNode, text_node_to_html_node
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    #both areent equal when one has no url and the other does
    def test_no_url(self):
        node = TextNode("This is a text node", "bold", "www.google.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    #different text
    def test_different_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text", "bold")
        self.assertNotEqual(node, node2)
    #different text_type
    def test_different_text_type(self):
        node = TextNode("This is a text node", "underline")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    #different url
    def test_different_url(self):
        node = TextNode("This is a text node", "bold", "www.google.com")
        node2 = TextNode("This is a text node", "bold", "www.bing.com")
        self.assertNotEqual(node, node2)
    #different caps
    def test_different_capitalization(self):
        node = TextNode("This is a TEXT node", "BOLD")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    def test_to_string(self):
        node = TextNode("This is a text node", "bold", "www.google.com")
        self.assertEqual(str(node), "TextNode(This is a text node, bold, www.google.com)")
    def test_to_string_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(str(node), "TextNode(This is a text node, bold, None)")

    def test_text_node_to_text(self):
        node = TextNode("this is a text node", "text")
        self.assertEqual(text_node_to_html_node(node), HTMLNode(None, "this is a text node"))
    def test_text_node_to_bold(self):
        node = TextNode("this is a text node", "bold")
        self.assertEqual(text_node_to_html_node(node), HTMLNode("b", "this is a text node"))
    def test_text_node_to_italic(self):
        node = TextNode("this is a text node", "italic")
        self.assertEqual(text_node_to_html_node(node), HTMLNode("i", "this is a text node"))
    def test_text_node_to_code(self):
        node = TextNode("this is a text node", "code")
        self.assertEqual(text_node_to_html_node(node), HTMLNode("code", "this is a text node"))
    def test_text_node_to_link(self):
        node = TextNode("this is a text node", "link", "www.google.com")
        self.assertEqual(text_node_to_html_node(node), HTMLNode("a", "this is a text node",  props={"href": "www.google.com"}))
    def test_text_node_to_image(self):
        node = TextNode("this is a text node", "image", "www.google.com")
        self.assertEqual(text_node_to_html_node(node), HTMLNode("img", "", props={"src": "www.google.com",
                                                                                  "alt": "this is a text node"}))
    def test_text_node_to_html_invalid_arg(self):
        node = TextNode("this is a text node", "invalid")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()
import unittest

from textnode import TextNode, text_node_to_html_node, split_nodes_delimiter, split_nodes_image, split_nodes_link
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

    #tests for split_nodes_delimiter
    def test_split_bold(self):
        node = TextNode("This is text with a **bold block** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(new_nodes, [TextNode("This is text with a ", "text"),
                                     TextNode("bold block", "bold"),
                                     TextNode(" word", "text")])
    def test_split_italic(self):
        node = TextNode("This is text with a *italic block* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertEqual(new_nodes, [TextNode("This is text with a ", "text"),
                                     TextNode("italic block", "italic"),
                                     TextNode(" word", "text")]) 
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(new_nodes, [TextNode("This is text with a ", "text"),
                                     TextNode("code block", "code"),
                                     TextNode(" word", "text")])
    def test_split_multiple(self):
        node = TextNode("This is text with a *block* and *another block* in it", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertEqual(new_nodes, [TextNode("This is text with a ", "text"),
                                     TextNode("block", "italic"),
                                     TextNode(" and ", "text"),
                                     TextNode("another block", "italic"),
                                     TextNode(" in it", "text")])
    def test_split_none(self):
        node = TextNode("This is text with a word", "text")
        new_nodes = split_nodes_delimiter([node], "aaaaa", "bold")
        self.assertEqual(new_nodes, [TextNode("This is text with a word", "text")])
    def test_split_not_closed(self):
        node = TextNode("This is text with a **bold block word", "text")
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "**", "bold")
    def test_split_back_to_back(self):
        node = TextNode("This is text with a `code``code`", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(new_nodes, [TextNode("This is text with a ", "text"),
                                     TextNode("code", "code"),
                                     TextNode("code", "code")])
    def test_split_front_and_back(self):
        node = TextNode("`code` This is text with a `code`", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(new_nodes, [TextNode("code", "code"),
                                     TextNode(" This is text with a ", "text"),
                                     TextNode("code", "code")])
        
    #tests for split_nodes_image
    def test_split_nodes_image_default(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", "text")
        correct_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif")
        ]
        nodes = split_nodes_image([node])
        self.assertEqual(nodes, correct_nodes)
        
    def test_split_nodes_image_multiple(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", "text")
        correct_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", "text"),
            TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        nodes = split_nodes_image([node])
        self.assertEqual(nodes, correct_nodes)
    def test_split_nodes_image_none(self):
        node = TextNode("This has no images", "text")
        self.assertEqual(split_nodes_image([node]), [node])
    def test_split_nodes_image_empty(self):
        self.assertEqual(split_nodes_image([]), [])
    #tests for split_nodes_link
    def test_split_nodes_link_default(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", "text")
        correct_nodes = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev")
        ]
        nodes = split_nodes_link([node])
        self.assertEqual(nodes, correct_nodes)
        
    def test_split_nodes_link_multiple(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", "text")
        correct_nodes = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev")
        ]
        nodes = split_nodes_link([node])
        self.assertEqual(nodes, correct_nodes)
    def test_split_nodes_link_none(self):
        node = TextNode("This has no links", "text")
        self.assertEqual(split_nodes_link([node]), [node])
    def test_split_nodes_link_empty(self):
        self.assertEqual(split_nodes_link([]), [])

if __name__ == "__main__":
    unittest.main()
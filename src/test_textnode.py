import unittest

from textnode import TextNode


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
    def teset_to_string_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(str(node), "TextNode(This is a text node, bold, None)")


if __name__ == "__main__":
    unittest.main()
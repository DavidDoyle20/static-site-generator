import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    #test no args
    def test_no_args(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
    #test print
    def test_to_string(self):
        test_props = {
            "href": "https://www.google.com", 
            "target": "_blank",
            }
        html_node = HTMLNode(tag="h1", value="idk", props=test_props)
        self.assertEqual(str(html_node), "HTMLNode(h1, idk, None, {'href': 'https://www.google.com', 'target': '_blank'})")
    #test props_to_html
    def test_props_to_html(self):
            test_props = {
                "href": "https://www.google.com", 
                "target": "_blank",
                }
            html_node = HTMLNode(props=test_props)
            self.assertEqual(html_node.props_to_html(), 'href="https://www.google.com" target="_blank"')
    #new leafnode tests
    def test_no_props(self):
        node = LeafNode("b", "test")
        self.assertEqual(node.to_html(), "<b>test</b>")
    def test_no_value_passed(self):
        node = LeafNode(None, "test")
        self.assertEqual(node.to_html(), "test")
    def test_no_tag_passed(self):
        with self.assertRaises(TypeError):
              node = LeafNode(value = "b")         
    #new parentnode tests
    def test_no_props(self):
        node = ParentNode("p", [LeafNode("b", "test")])
        self.assertEqual(node.to_html(), "<p><b>test</b></p>")
    def test_no_children(self):
         with self.assertRaises(TypeError):
              node = ParentNode("p")
    def test_no_tag(self):
         with self.assertRaises(TypeError):
              node = ParentNode(children=[LeafNode("b", "test")])
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    def test_to_html_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {
                "href": "https://www.google.com"
            }
        )
        self.assertEqual(node.to_html(), '<p href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

            
if __name__ == "__main__":
    unittest.main()
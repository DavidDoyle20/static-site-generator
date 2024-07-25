import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()
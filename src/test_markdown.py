import unittest

from markdown import extract_markdown_images, extract_markdown_links, block_to_block_type


class TestHTMLNode(unittest.TestCase):
    #extract markdown images
    def test_extract_images_default(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
    def test_extract_images_empty(self):
        text = ""
        self.assertEqual(extract_markdown_images(text), [])
    def test_extract_images_not_found(self):
        text = "This is text with a "
        self.assertEqual(extract_markdown_images(text), [])
    #extract markdown links
    def test_extract_links_default(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
    def test_extract_links_empty(self):
        text = ""
        self.assertEqual(extract_markdown_links(text), [])
    def test_extract_links_not_found(self):
        text = "This is text with a "
        self.assertEqual(extract_markdown_links(text), [])






    def test_block_to_block_type_none(self):
        self.assertEqual("paragraph", block_to_block_type(""))
    def test_block_to_block_type_heading(self):
        text = """### heading"""
        self.assertEqual("heading", block_to_block_type(text))
    def test_block_to_block_type_code(self):
        text = """``` sfsfsfsf```"""
        self.assertEqual("code", block_to_block_type(text))
    def test_block_to_block_type_quote(self):
        text = """> sofnsf
        >sfsdf
        >sfdsdf"""
        self.assertEqual("quote", block_to_block_type(text))
    def test_block_to_block_type_unordered_list(self):
        text = """* sfdsfsf
        - sdfsfs
        * sdfs"""
        self.assertEqual("unordered_list", block_to_block_type(text))
    def test_block_to_block_type_ordered_list(self):
        text = """1. sdfsf
        2. sdfsdf
        3. sfsfd"""
        self.assertEqual("ordered_list", block_to_block_type(text))
    def test_block_to_block_type_paragraph(self):
        text = "sfsfsfsfsfsfsfsdf"
        self.assertEqual("paragraph", block_to_block_type(text))
            
if __name__ == "__main__":
    unittest.main()
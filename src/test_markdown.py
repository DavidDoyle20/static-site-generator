import unittest

from markdown import block_to_block_type


class TestHTMLNode(unittest.TestCase):
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
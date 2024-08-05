import unittest

from markdown import extract_markdown_images, extract_markdown_links


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
            
if __name__ == "__main__":
    unittest.main()
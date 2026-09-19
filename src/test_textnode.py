import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, None)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, None)
        self.assertEqual(node, node2)

    def test_asseq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, None)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, None)
        self.assertEqual(node, node2)
        
    def test_assnoeq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, None)
        node2 = TextNode("This is a text node", TextType.TEXT, None)
        self.assertNotEqual(node, node2)
        
    def test_urlnone(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, None)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, None)
        self.assertEqual(node, node2)
        
    def test_ttdiff(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, None)
        node2 = TextNode("This is a text node", TextType.TEXT, None)
        self.assertNotEqual(node, node2)
        
def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT, None)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

def test_link(self):
    node = TextNode("Click me", TextType.LINK, "https://example.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "Click me")
    self.assertEqual(html_node.props, {"href": "https://example.com"})

def test_image(self):
    node = TextNode("A cat", TextType.IMAGE, "https://example.com/cat.png")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(html_node.props, {"src": "https://example.com/cat.png", "alt": "A cat"})

if __name__ == "__main__":
    unittest.main()
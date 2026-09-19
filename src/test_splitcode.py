import unittest

from splitcode import split_nodes_delimiter, split_nodes_image, split_nodes_link, textsplitter
from textnode import TextNode, TextType
from blocks import markdown_to_blocks

class TestTextNode(unittest.TestCase):
    def test_eq_split(self):
        node = TextNode("This is a text with a `code block` word", TextType.TEXT, None)
        split = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        node2 = [
            TextNode("This is a text with a ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE_TEXT, None),
            TextNode(" word", TextType.TEXT, None),
        ]
        self.assertEqual(split, node2)
        
    def test_eq_bold(self):
        node = TextNode("This is a text with a `bold block` word", TextType.TEXT, None)
        split = split_nodes_delimiter([node], "`", TextType.BOLD_TEXT)
        node2 = [
            TextNode("This is a text with a ", TextType.TEXT, None),
            TextNode("bold block", TextType.BOLD_TEXT, None),
            TextNode(" word", TextType.TEXT, None),
        ]
        self.assertEqual(split, node2)
        
    def test_eq_notwice(self):
        node = TextNode("This is a text with a `code block word", TextType.TEXT, None)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
            
            
    def test_eq_nosplit(self):
        node = TextNode("This is a text with a code block word", TextType.TEXT, None)
        split = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        node2 = TextNode("This is a text with a code block word", TextType.TEXT, None)
        
        self.assertEqual(split, [node2])
        
    
    def test_split_images(self):
        node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
    )
        
    def test_split_images(self):
        node = TextNode(
                "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINKS, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINKS, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
    )
        
    def test_split_all(self):
        node = [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD_TEXT),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC_TEXT),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE_TEXT),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINKS, "https://boot.dev"),
        ]
        new_nodes = textsplitter("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(node, new_nodes)
        
    def test_split_none(self):
        node = [TextNode("this is a test", TextType.TEXT)]
        new_nodes = textsplitter("this is a test")
        self.assertEqual(node, new_nodes)
        
    def test_split_bolds(self):
        node2 = [
            TextNode("This is a ", TextType.TEXT, None),
            TextNode("text", TextType.BOLD_TEXT, None),
            TextNode(" with a ", TextType.TEXT, None),
            TextNode("bold block", TextType.BOLD_TEXT, None),
            TextNode(" word", TextType.TEXT, None),
        ]
        new_nodes = textsplitter("This is a **text** with a **bold block** word")
        self.assertEqual(node2, new_nodes)
        
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
"This is **bolded** paragraph",
"This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
"- This is a list\n- with items",
            ],
        )
    def test_markdown_to_blocks(self): 
        md = """This is **bolded** paragraph"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, 
        [
"This is **bolded** paragraph"
        ])
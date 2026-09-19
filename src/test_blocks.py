import unittest

from blocks import BlockType, markdown_to_blocks, block_to_block_type


class TestTextNode(unittest.TestCase):
    def test_basic_markdown(self):
        node = BlockType.PARAGRAPH
        node2 = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
            """
        test = block_to_block_type(node2)
        self.assertEqual(node, test)
        
    def test_basic_heading(self):
        node = BlockType.HEADING
        node2 = """## This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

This is a list
with items
            """
        test = block_to_block_type(node2)
        self.assertEqual(node, test)
        
    def test_basic_code(self):
        node = BlockType.CODE
        node2 = """```
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

This is a list
with items```"""
        test = block_to_block_type(node2)
        self.assertEqual(node, test)
        
    def test_basic_quote(self):
        node = BlockType.QUOTE
        node2 = """> This is **bolded** paragraph
> This is another paragraph with _italic_ text and `code` here
> This is the same paragraph on a new line
> This is a list
> with items"""
        test = block_to_block_type(node2)
        self.assertEqual(node, test)
        
    def test_basic_unordered(self):
        node = BlockType.UNORDERED_LIST
        node2 = """- This is **bolded** paragraph
- This is another paragraph with _italic_ text and `code` here
- This is the same paragraph on a new line
- This is a list
- with items"""
        test = block_to_block_type(node2)
        self.assertEqual(node, test)
        
    def test_basic_ordered(self):
        node = BlockType.ORDERED_LIST
        node2 = """1. This is **bolded** paragraph
2. This is another paragraph with _italic_ text and `code` here
3. This is the same paragraph on a new line
4. This is a list
5. with items"""
        test = block_to_block_type(node2)
        self.assertEqual(node, test)
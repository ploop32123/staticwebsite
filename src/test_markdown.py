import unittest
from blocks import BlockType, block_to_block_type, markdown_to_blocks
from textnode import TextNode, TextType
from regexr import extract_markdown_images, extract_markdown_links
from splitcode import split_nodes_delimiter, split_nodes_image, split_nodes_link, textsplitter
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_html import markdown_to_html_node, text_to_children, blocktype_heading_count, blocktype_paragraph

class TestTextNode(unittest.TestCase):
    def test_markdown_eqpara(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>")
        
        
    def test_markdown_eqhash(self):
            md = """
# This is **bolded** paragraph text    
"""
            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(html, "<div><h1>This is <b>bolded</b> paragraph text</h1></div>")
            
            
    def test_markdown_eqhashnpara(self):
            md = """
# This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here    
"""
            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(html, "<div><h1>This is <b>bolded</b> paragraph</h1><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>")
            
    def test_markdown_blockquotebase(self):
            md = """
> This is **bolded** paragraph text   
"""
            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(html, "<div><blockquote>This is <b>bolded</b> paragraph text</blockquote></div>")
            
    def test_markdown_blockquotetests(self):
                md = """
> This is **bolded** paragraph text


> This is **bolded** paragraph text 
    """
                node = markdown_to_html_node(md)
                html = node.to_html()
                self.assertEqual(html, "<div><blockquote>This is <b>bolded</b> paragraph text</blockquote><blockquote>This is <b>bolded</b> paragraph text</blockquote></div>")
                
    def test_markdown_unordered(self):
                md = """
- This is **bolded** paragraph text   
    """
                node = markdown_to_html_node(md)
                html = node.to_html()
                self.assertEqual(html, "<div><ul><li>This is <b>bolded</b> paragraph text</li></ul></div>")
                
    def test_markdown_ordered(self):
                    md = """
1. first item
2. second with _italic_
3. third item
"""
                    node = markdown_to_html_node(md)
                    html = node.to_html()
                    self.assertEqual(html, "<div><ol><li>first item</li><li>second with <i>italic</i></li><li>third item</li></ol></div>")
                    
                    
    def test_markdown_codeblock(self):
            md = """
```
some code here
```
"""
            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(html, "<div><pre><code>some code here\n</code></pre></div>")
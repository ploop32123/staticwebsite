from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    ITALIC_TEXT = "Italic text"
    CODE_TEXT = "Code text"
    BOLD_TEXT = "Bold text"
    LINKS = "text with a link"
    IMAGES = "text that gives an image"

class TextNode:
    
    def __init__(self,text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else: return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(text_node: TextNode) -> LeafNode:
        if text_node.text_type == None:
            raise Exception
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None,text_node.text)
        if text_node.text_type == TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        if text_node.text_type == TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        if text_node.text_type == TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        if text_node.text_type == TextType.LINKS:
            return LeafNode("a", "anchor", {"href": text_node.url})
        if text_node.text_type == TextType.IMAGES:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        else:
            raise ValueError(f"invalid text type: {text_node.text_type}")
    
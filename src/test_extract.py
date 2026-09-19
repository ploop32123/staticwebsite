import unittest
from extract_title import extract_title


class TestTextNode(unittest.TestCase):
    def test_basic_extract(self):
        node1 = """# Hello"""
        node2 = "Hello"
        stnode = extract_title(f"{node1}")
        self.assertEqual(node2, stnode)
        
        
    def test_basic_extracttwo(self):
            node1 = """# Hello
            Mario
            This is not supposed to be there."""
            node2 = "Hello"
            stnode = extract_title(f"{node1}")
            self.assertEqual(node2, stnode)
            
    def test_basic_extractspaced(self):
            node1 = """
            
# Hello"""
            node2 = "Hello"
            stnode = extract_title(f"{node1}")
            self.assertEqual(node2, stnode)
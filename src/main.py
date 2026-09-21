from textnode import TextNode
from textnode import TextType
from library import cleanpath, filepath
import os
import shutil
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive
import sys

def main():
    if len(sys.argv) <= 1:
        basepath = "/"
    elif len(sys.argv) > 1:    
        basepath = sys.argv[1]
    cleanpath("./docs")
    filepath("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)
main()

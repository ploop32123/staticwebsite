from textnode import TextNode
from textnode import TextType
from library import cleanpath, filepath
import os
import shutil
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive

def main():
    cleanpath("./public")
    filepath("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")
main()

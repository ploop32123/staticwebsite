import os
from generate_page import generate_page
from pathlib import Path




def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        frompath = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(frompath) and frompath.endswith(".md"):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(frompath, template_path, dest_path, basepath)
        elif os.path.isdir(frompath):
            generate_pages_recursive(frompath, template_path, dest_path, basepath)
import os
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    openpath = open(from_path)
    opentemp = open(template_path)
    readfrom = openpath.read()
    readtemp = opentemp.read()
    openpath.close()
    opentemp.close()
    htmlstring = markdown_to_html_node(readfrom)
    strong = htmlstring.to_html()
    titleofpage = extract_title(readfrom)
    replacedtitle = readtemp.replace("{{ Title }}", titleofpage)
    replacedcontent = replacedtitle.replace("{{ Content }}", strong)
    replacedhref = replacedcontent.replace(f'href="/', 'href="' + basepath)
    replacedsrc = replacedhref.replace(f'src="/', 'src="'+ basepath)
    paths = os.path.dirname(dest_path)
    os.makedirs(paths, exist_ok=True)
    f = open(dest_path, "w")
    f.write(replacedsrc)
    f.close()
        
    
    
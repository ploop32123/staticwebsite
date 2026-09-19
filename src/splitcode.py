from textnode import TextNode, TextType
from regexr import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    newlist = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            newlist.append(old_node)
            continue
        cutlist = old_node.text.split(delimiter)
        if len(cutlist) % 2 == 0:
            raise ValueError("Even number after split")
        for i, part in enumerate(cutlist):
            if i % 2 == 0:
                newlist.append(TextNode(part, TextType.TEXT, None))
            else:
                newlist.append(TextNode(part, text_type, None))
    return newlist

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    newlist = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            newlist.append(old_node)
            continue
        originaltext = old_node.text
        images = extract_markdown_images(originaltext)
        if len(images) == 0:
             newlist.append(old_node)
             continue
        for alt, url in images:
            splitimage = f"![{alt}]({url})"
            before = originaltext.split(splitimage, maxsplit=1)
            if before[0] != "":
                newlist.append(TextNode(before[0], TextType.TEXT, None))
            newlist.append(TextNode(alt, TextType.IMAGES, url))
            originaltext =before[1]
        if originaltext != "":
            newlist.append(TextNode(originaltext, TextType.TEXT, None))
    return newlist
              
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    newlist = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            newlist.append(old_node)
            continue
        originaltext = old_node.text
        links = extract_markdown_links(originaltext)
        if len(links) == 0:
             newlist.append(old_node)
             continue
        for alt, url in links:
            splitlink = f"[{alt}]({url})"
            before = originaltext.split(splitlink, maxsplit=1)
            if before[0] != "":
                newlist.append(TextNode(before[0], TextType.TEXT, None))
            newlist.append(TextNode(alt, TextType.LINKS, url))
            originaltext =before[1]
        if originaltext != "":
            newlist.append(TextNode(originaltext, TextType.TEXT, None))
    return newlist


def textsplitter(text) -> list[TextNode]:
    node = TextNode(text, TextType.TEXT)
    boldnode = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
    italicnode = split_nodes_delimiter(boldnode, "_", TextType.ITALIC_TEXT)
    codenode = split_nodes_delimiter(italicnode, "`", TextType.CODE_TEXT)
    imagesplitnode = split_nodes_image(codenode)
    linksplitnode = split_nodes_link(imagesplitnode)
    return linksplitnode


    
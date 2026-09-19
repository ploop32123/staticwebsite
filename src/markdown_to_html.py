from blocks import BlockType, block_to_block_type, markdown_to_blocks
from textnode import TextNode, TextType
from regexr import extract_markdown_images, extract_markdown_links
from splitcode import split_nodes_delimiter, split_nodes_image, split_nodes_link, textsplitter
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_to_children(text):
    children = []
    splittext = textsplitter(text)
    for split in splittext:
        htmlnoded = TextNode.text_node_to_html_node(split)
        children.append(htmlnoded)
    return children



def markdown_to_html_node(markdown):
    blocked = markdown_to_blocks(markdown)
    results = []
    for blocks in blocked:
        block = block_to_block_type(blocks)
        if block == BlockType.HEADING:
            blockhead = blocktype_heading_count(blocks)
            results.append(blockhead)
        elif block == BlockType.PARAGRAPH:
            blockpara = blocktype_paragraph(blocks)
            results.append(blockpara)
        elif block == BlockType.QUOTE:
            blockquote = blocktype_quote(blocks)
            results.append(blockquote)
        elif block == BlockType.UNORDERED_LIST:
            unorderedblock = blocktype_unorded(blocks)
            results.append(unorderedblock)
        elif block == BlockType.ORDERED_LIST:
            orderedblock = blocktype_ordered(blocks)
            results.append(orderedblock)
        elif block == BlockType.CODE:
            codeblock = blocktype_code(blocks)
            results.append(codeblock)
            
    return ParentNode("div", results)
        
def blocktype_paragraph(typeblock):
    lines = typeblock.split("\n")
    paragraph = " ".join(lines)
    childline = text_to_children(paragraph)
    pnodes = ParentNode("p", childline)
    return pnodes
    
def blocktype_quote(typeblock):
    endresult = []
    lines = typeblock.split("\n")
    for line in lines:
        splitedlines = line.lstrip(">").strip()
        endresult.append(splitedlines)
    rejoined = " ".join(endresult)
    textedlines = text_to_children(rejoined)    
    return ParentNode("blockquote", textedlines)
    
        
    
def blocktype_heading_count(typeblock):
    count = 0
    for char in typeblock:
        if char == "#":
            count += 1
        if char != "#":
            break
    if count > 6:
        raise ValueError(f"invalid heading level: {count}")
    editedtext = typeblock[count+1:]
    if editedtext == "":
        raise ValueError("only had # in text")
    textchild = text_to_children(editedtext)
    pnode = ParentNode(f"h{count}", textchild)
    return pnode

def blocktype_unorded(typeblock):
    items = typeblock.split("\n")
    empitemlist = []
    for item in items:
        splitedlines = item.lstrip("- ").strip()
        children = text_to_children(splitedlines)
        empitemlist.append(ParentNode("li", children))

    return ParentNode("ul", empitemlist)

def blocktype_ordered(typeblock):
    items = typeblock.split("\n")
    empitemlist = []
    for item in items:
        splitedlines = item.split(". ", 1)
        children = text_to_children(splitedlines[1])
        empitemlist.append(ParentNode("li", children))

    return ParentNode("ol", empitemlist)

def blocktype_code(typeblock):
    if typeblock[0] == "`" and typeblock[2] == "`" and typeblock[-3] == "`" and typeblock[-1] == "`":
        stripedofsne = typeblock[4:-3]
        plainnode = TextNode(stripedofsne, TextType.CODE_TEXT)
        nodetext = TextNode.text_node_to_html_node(plainnode)
        return ParentNode("pre", [nodetext])
    return ValueError(f"{typeblock} did not contain the right number of `")
        
    
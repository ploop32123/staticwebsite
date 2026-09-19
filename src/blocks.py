from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph" 
    HEADING = "heading" 
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"
    
def markdown_to_blocks(markdown):
    emplist = []
    splited = markdown.split("\n\n")
    for splits in splited:
        cleaned = splits.strip()
        if cleaned != "":
            emplist.append(cleaned)
    return emplist

def block_to_block_type(text):
    if text.startswith(("# ","## ", "### ", "#### ", "##### ", "###### ")): 
        return BlockType.HEADING
    elif text.startswith("```\n") and text.endswith("```"):
        return  BlockType.CODE
    splittext = text.split("\n")
    quotes = True
    for lines in splittext:
        if not lines.startswith(">"):
            quotes = False 
            break
    if quotes:
        return BlockType.QUOTE
    unorded = True
    for lines in splittext:
        if not lines.startswith("- "):
            unorded = False
            break
    if unorded:
        return BlockType.UNORDERED_LIST
    n = 0
    ordered = True
    for lines in splittext:
        n += 1
        if not lines.startswith(f"{n}. "):
            ordered = False
            break
    if ordered:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
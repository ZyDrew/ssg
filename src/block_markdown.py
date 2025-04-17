from enum import Enum
import re
from htmlnodes import HTMLNode
from parentnodes import ParentNode
from textnodes import text_to_textnodes, text_node_to_leaf_node, TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"

def markdown_to_blocks(markdown):
    #From end to top :
    # - Split on the double \n\n to separate the markdown to block of lines
    # - Split each block to individual line (separated by \n) and apply a strip() to remove starting and trailing whitespace
    # - Apply a filter function to remove from the list of lines every empty or "\n" line
    # - Apply a join on "\n" to merge lines together as a list of blocks 
    # - Apply a filter to remove excessive newline ("\n\n") within the list of blocks

    result = list(
        filter(None,                                        #None -> Delete auto all falsy elements (empty strings, None, etc.)
            map(lambda block: "\n".join(
                filter(None, 
                    map(str.strip,                          #str.strip built-in function
                        block.split("\n"))                   
                )
            ), 
            markdown.split("\n\n")
        )))
    return result

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_node = ParentNode("div", [])

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                blocknode = ParentNode("p", [])
                blocknode.children.extend(block_nodes_to_children(block.replace("\n"," ")))

            case BlockType.HEADING:
                count = 0
                for char in block:
                    if char == '#':
                        count += 1
                    else:
                        break
                blocknode = ParentNode(f"h{count}", [])
                blocknode.children.extend(block_nodes_to_children(block.strip("# ")))

            case BlockType.CODE:
                textnode = TextNode(block[4:-3], TextType.TEXT)
                blocknode = ParentNode("pre", [ParentNode("code", [text_node_to_leaf_node(textnode)])])

            case BlockType.QUOTE:
                blocknode = ParentNode("blockquote", [])
                cleaned = re.sub(r"^\>\s*", "", block, flags=re.MULTILINE)
                blocknode.children.extend(block_nodes_to_children(cleaned.replace("\n"," ")))

            case BlockType.UL:
                blocknode = process_list_blocktype("ul", r"^\-\s*", block)

            case BlockType.OL:
                blocknode = process_list_blocktype("ol", r"^\d+\.\s*", block)
            
            case _:
                raise ValueError("Invalid block type")
        
        html_node.children.append(blocknode)

    return html_node

def block_nodes_to_children(block):
    text_nodes = text_to_textnodes(block)
    
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_leaf_node(text_node))
    return children

#FOR LIST : UL / OL
def process_list_blocktype(tag, regex, block):
    blocknode = ParentNode(tag, [])
    lines = block.split("\n")
    for line in lines:
        cleaned = re.sub(regex, "", line, flags=re.MULTILINE)
        li_node = ParentNode("li", block_nodes_to_children(cleaned))
        blocknode.children.append(li_node)

    return blocknode

def block_to_block_type(block):
    lines = block.split("\n")

    #HEADING
    if len(re.findall(r"^[#]{1,6} (.*?)", block)) > 0:
        return BlockType.HEADING
    
    #CODE
    if len(re.findall(r"^`{3}(.*?)`{3}$", block, re.DOTALL)) > 0:
        return BlockType.CODE
    
    #QUOTE
    count = 0
    for line in lines:
        count += len(re.findall(r"^>(.*?)", line))
    if len(lines) == count:
        return BlockType.QUOTE
    
    #UL
    count = 0
    for line in lines:
        count += len(re.findall(r"^- (.*?)", line))
    if len(lines) == count:
        return BlockType.UL
    
    #OL
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OL

    #PARAGRAPH
    return BlockType.PARAGRAPH
from enum import Enum
from leafnodes import LeafNode
from regex_function import *

#ENUM FOR TEXTNODE MARKDOWN
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    #END __init__

    def __eq__(self, other):
        if (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        ):
            return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

#Transform text node to leaf node as HTML code
def text_node_to_leaf_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href" : text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src" : text_node.url, "alt" : text_node.text})
        case _:
            raise ValueError(f"Value text_type not in TextType ENUM : {text_node.text_type}")

#Transform inline text node (markdown) as a list of text node object
#TEXT - BOLD - ITALIC - CODE
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter not in ("**", "_", "`"):
        raise ValueError(f"Invalid markdown syntax : {delimiter}")

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            splitted_node = node.text.split(delimiter)
            if (len(splitted_node)-1) % 2 != 0:
                raise ValueError("The markdown syntax is incorrect : probably not close")
            
            for i in range(0, len(splitted_node)):
                if splitted_node[i] == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(splitted_node[i], TextType.TEXT))
                elif i % 2 != 0:
                    new_nodes.append(TextNode(splitted_node[i], text_type))
                    
    return new_nodes

#IMAGE
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue

        sections = []
        next_split = node.text
        for image in images:
            splitted_node = next_split.split(f"![{image[0]}]({image[1]})", 1)
            
            next_split = splitted_node[1]

            if splitted_node[0] != "":
                sections.append(TextNode(splitted_node[0], TextType.TEXT))
            sections.append(TextNode(image[0], TextType.IMAGE, image[1]))
        
        if next_split != "":
            sections.append(TextNode(next_split, TextType.TEXT))

        new_nodes.extend(sections)
    return new_nodes

#LINK
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue

        sections = []
        next_split = node.text
        for link in links:
            splitted_node = next_split.split(f"[{link[0]}]({link[1]})", 1)
            
            next_split = splitted_node[1]

            if splitted_node[0] != "":
                sections.append(TextNode(splitted_node[0], TextType.TEXT))
            sections.append(TextNode(link[0], TextType.LINK, link[1]))
        
        if next_split != "":
            sections.append(TextNode(next_split, TextType.TEXT))

        new_nodes.extend(sections)
    return new_nodes

#ALL IN ONE
# ON VA PRENDRE LE TEXTE ENTIER ET LE FAIRE PASSER DANS CHAQUE SPLIT METHOD
# LA LISTE "NODES" SERA REMISE A JOUR DU DEBUT A LA FIN A CHAQUE APPEL DE METHOD
# DE CE FAIT, ON N'A PAS BESOIN DE REVENIR EN ARRIERE POUR RE-TESTER CHAQUE PARTIE DE TEXTE
# CECI EST REALISABLE GRACE A L'IMPLEMENTATION INTELLIGENTE DES METHODES
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
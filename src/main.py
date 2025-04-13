from textnodes import TextNode, TextType

def main():
    try:
        node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        print(node)
    except ValueError as v:
        print(v)

main()
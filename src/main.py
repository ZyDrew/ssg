from textnodes import TextNode, TextType

def main():
    try:
        dummy = TextNode("This is some anchor text", TextType.link, "https://www.boot.dev")
        print(dummy)
    except ValueError as v:
        print(v)

main()
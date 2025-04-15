from textnodes import TextNode, TextType

def main():
    try:
        node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        print(node)
    except ValueError as v:
        print(v)

    s = "This is a **bold word** and **another**"
    slist = s.split("**")
    print(slist)

main()
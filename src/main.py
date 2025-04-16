from textnodes import TextNode, TextType

def main():
    try:
        node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        print(node)
    except ValueError as v:
        print(v)

    s = "This is text with an ![image(https://i.imgur.com/zjjcJKZ.png) blablabla ![image2](https://w.imgur.com/zjjcJKZ.png) text"
    image_alt = "image"
    image_url = "https://i.imgur.com/zjjcJKZ.png"
    image_alt2 = "image2"
    image_url2 = "https://w.imgur.com/zjjcJKZ.png"
    slist = s.split(f"![{image_alt}]({image_url})", 1)
    #slist2 = slist[1].split(f"![{image_alt2}]({image_url2})", 1)
    print(len(slist))
    print(slist)
    #print(slist2)

main()
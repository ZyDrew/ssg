import unittest

from textnodes import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.sloth.io")
        node2 = TextNode("This is an italic text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_neq2(self):
        node = TextNode("This is a image node", TextType.IMAGE, "image.jpeg")
        node2 = TextNode("This is a link node", TextType.LINK, "https://www.sloth.io")
        self.assertNotEqual(node, node2)

    def test_neq3(self):
        node = TextNode("This is a bold text node", TextType.BOLD, "https://www.sloth.io")
        node2 = TextNode("This is a code text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_neq4(self):
        node = TextNode("This is a bold text node", TextType.TEXT)
        node2 = TextNode("This is a code text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.sloth.io")
        node2 = TextNode("This is a link node", TextType.LINK, "https://www.sloth.io")
        self.assertEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is a link node", TextType.LINK, "https://sloth.io")
        node2 = TextNode("This is a link node", TextType.LINK, "https://www.sloth.io")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()
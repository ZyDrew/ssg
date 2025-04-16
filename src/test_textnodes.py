import unittest

from textnodes import *


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

#Test for the method "text_node_to_leaf_node"
class TestTextNodeToLeafNode(unittest.TestCase):
    def test_italic(self):
        text_node = TextNode("This is italic", TextType.ITALIC)
        leaf_node = text_node_to_leaf_node(text_node)
        self.assertEqual(leaf_node.tag, "i")
        self.assertEqual(leaf_node.value, "This is italic")
        print(f"leaf : {leaf_node.to_html()}")

    def test_invalid_type(self):
        try:
            text_node = TextNode("This is italic", "underline")
            leaf_node = text_node_to_leaf_node(text_node)
            self.assertEqual(leaf_node.tag, "i")
            self.assertEqual(leaf_node.value, "This is italic")
            print(f"leaf : {leaf_node.to_html()}")
        except ValueError as v:
            print(v)
    
    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.sloth.io")
        leaf_node = text_node_to_leaf_node(node)
        self.assertEqual(leaf_node.tag, "a")
        self.assertEqual(leaf_node.value, "This is a link")
        self.assertEqual(
            leaf_node.props,
            {"href": "https://www.sloth.io"},
        )
        print(f"leaf link : {leaf_node.to_html()}")

    #Course's tests
    def test_textnode_text(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        leaf_node = text_node_to_leaf_node(text_node)
        self.assertEqual(leaf_node.tag, None)
        self.assertEqual(leaf_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        leaf_node = text_node_to_leaf_node(node)
        self.assertEqual(leaf_node.tag, "img")
        self.assertEqual(leaf_node.value, "")
        self.assertEqual(
            leaf_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )
        print(f"leaf image : {leaf_node.to_html()}")

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        leaf_node = text_node_to_leaf_node(node)
        self.assertEqual(leaf_node.tag, "b")
        self.assertEqual(leaf_node.value, "This is bold")

#Test for the method "split_nodes_delimiter"
class TestSplitNodesDelimiteur(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is a **bold word**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold word", TextType.BOLD)
            ],
            new_nodes
        )

    def test_two_bold(self):
        node = TextNode("This is a **bold word** and **another**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD)
            ],
            new_nodes
        )
    
    def test_markdown_syntax_error(self):
        try:
            node = TextNode("This is a **bold word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
            self.assertListEqual(
                [
                    TextNode("This is a ", TextType.TEXT),
                    TextNode("bold word", TextType.BOLD)
                ],
                new_nodes
            )
        except ValueError as v:
            print(v)

    #Course's tests to ensure functional method
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

#Tests for method "split_nodes_image" "split_nodes_link"
class TestSplitNodesImageAndLink(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                )
            ],
            new_nodes
        )
        print(f"Split img-link 1 : {new_nodes}")

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [sloth](https://www.sloth.io) and another [fox](https://www.fox.io)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("sloth", TextType.LINK, "https://www.sloth.io"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("fox", TextType.LINK, "https://www.fox.io")
            ],
            new_nodes
        )
        print(f"Split img-link 2 : {new_nodes}")

    def test_split_start_with_link(self):
        node = TextNode(
            "[sloth](https://www.sloth.io) Before this is a link",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("sloth", TextType.LINK, "https://www.sloth.io"),
                TextNode(" Before this is a link", TextType.TEXT),
            ],
            new_nodes
        )
        print(f"Split img-link 3 : {new_nodes}")
    
    def test_split_start_with_image(self):
        node = TextNode(
            "![image](https://www.imgur.jpeg) Before this is an image",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.imgur.jpeg"),
                TextNode(" Before this is an image", TextType.TEXT),
            ],
            new_nodes
        )

    def test_split_error_syntax_image(self):
        try:
            node = TextNode(
                "![image(https://www.imgur.jpeg) Before this is an image",
                TextType.TEXT,
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("![image(https://www.imgur.jpeg) Before this is an image", TextType.TEXT)
                ],
                new_nodes
            )
        except ValueError as v:
            print(v)

if __name__ == "__main__":
    unittest.main()
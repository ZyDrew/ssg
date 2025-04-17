import unittest

from htmlnodes import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        node = HTMLNode("p", "Simple paragraph")
        #print(repr(node))

    def test_2(self):
        node = HTMLNode("a", "Simple link",props={"href" : "http://www.sloth.io"})
        #print(repr(node))

    def test_3(self):
        node_a = HTMLNode("a", "Simple link", props={"href" : "http://www.sloth.io"})
        node_li = HTMLNode("li", "Simple list text")
        node = HTMLNode("ol", "Ordered list", [node_li, node_a], {"type" : "i"})
        #print(repr(node))

    def test_4(self):
        node_p = HTMLNode("li", "Simple paragraph")
        node_footer = HTMLNode("footer", "Simple footer")
        node = HTMLNode("div", "Generic container", [node_p, node_footer])
        #print(repr(node))

    #Course's tests to ensure functional class
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

if __name__ == "__main__":
    unittest.main()
import unittest

from leafnodes import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        node = LeafNode("p", "Simple paragraph")
        print(node.to_html())
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        print(node.to_html())

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href" : "http://www.sloth.io"})
        self.assertEqual(node.to_html(), '<a href="http://www.sloth.io">Hello, world!</a>')
        print(node.to_html())

    def test_notequal_leaf_to_html(self):
        node = LeafNode("b", "Some bold text")
        self.assertNotEqual(node.to_html(), "<b>Some italic text</b>")
        print(node.to_html())
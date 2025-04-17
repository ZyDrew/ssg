import unittest
from parentnodes import ParentNode
from leafnodes import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        #print(parent_node.to_html())

    def test_to_html_with_grandchild(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        #print(parent_node.to_html())

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("b", "bold child text")
        child_node3 = LeafNode(None, "raw child text")
        parent_node = ParentNode("div", [child_node, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><b>bold child text</b>raw child text</div>")
        #print(parent_node.to_html())
    
    def test_to_html_no_children(self):
        try:
            parent_node = ParentNode("div", None)
            self.assertEqual(parent_node.to_html(), "<div></div>")
        except ValueError as v:
            print(v)
    
    def test_to_html_with_children_grandchildren(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("b", "bold child text")
        child_node3 = LeafNode(None, "raw child text")
        grandchild_node = LeafNode("b", "bold grandchild", {"attr" : "attribute"})
        grandchild_node2 = LeafNode("i", "italic grandchild")
        child_node4 = ParentNode("p", [grandchild_node, grandchild_node2])
        parent_node = ParentNode("div", [child_node, child_node2, child_node3, child_node4])
        self.assertEqual(parent_node.to_html(), '<div><span>child</span><b>bold child text</b>raw child text<p><b attr="attribute">bold grandchild</b><i>italic grandchild</i></p></div>')
        #print(parent_node.to_html())
    
    def test_to_html_with_child_and_parenthref(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"attr" : "attribute"})
        self.assertEqual(parent_node.to_html(), '<div attr="attribute"><span>child</span></div>')
        #print(parent_node.to_html())

    #Course's tests to ensure functional class
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
from htmlnodes import HTMLNode
from leafnodes import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag property")
        
        if not self.children:
            raise ValueError("All parent nodes must have a children property")
        
        parent_render = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            parent_render += child.to_html()

        parent_render += f"</{self.tag}>"
        return parent_render

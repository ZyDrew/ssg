class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value= value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Do not use parent class for this method")
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        result = ""
        for prop in self.props:
            result += f' {prop}="{self.props[prop]}"'
        return result
    
    def __repr__(self):
        if not self.children and not self.props:
            return f"HTMLNode({self.tag}, {self.value})"
        elif not self.children:
            return f"HTMLNode({self.tag}, {self.value}, {self.props_to_html()})"
        elif not self.props:
            return f"HTMLNode({self.tag}, {self.value}, {self.children})"
        
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
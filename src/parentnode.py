from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parentnode must have a tag")
        if self.children is None:
            raise ValueError("Parentnode must have children")
        props_str = ""
        if self.props:
            props_str = " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
        children_html = "".join(child.to_html() for child in self.children)
        
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
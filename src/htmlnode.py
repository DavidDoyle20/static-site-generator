from functools import reduce
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props != None:
            return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        else:
            return "None"
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other_node):
        return self.tag == other_node.tag and self.value == other_node.value and self.children == other_node.children and self.props == other_node.props
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("No value given")
        elif self.tag == None:
            return str(self.value)
        else:
            return f"<{self.tag}{super().props_to_html() if self.props != None else ''}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node needs a tag!")
        elif self.children == None:
            raise ValueError("No children in the provided list!")
        else:
            return f"<{self.tag}{' ' + super().props_to_html() if self.props != None else ''}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
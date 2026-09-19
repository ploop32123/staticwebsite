class HTMLNode():
    def __init__(self, tag= None, value= None, children= None, props= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        empstr = ""
        if self.props == None:
            return empstr
        for key, value in self.props.items():
            empstr += f' {key}="{value}"'
        return empstr
        
    def __repr__(self):
        print(f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")
    
class LeafNode(HTMLNode):
    def __init__(self, value, tag, props= None):
        super().__init__(value, tag, None, props)
        
    def to_html(self):
        empstr = ""
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        empstr += f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        return empstr
           
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"     
    
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
   
    def to_html(self):
        emplist = ""
        if self.tag == None:
            raise ValueError
        if self.children == None:
            raise ValueError("missing children")
        for child in self.children:
            emplist += child.to_html()
        emplist = f"<{self.tag}{self.props_to_html()}>{emplist}</{self.tag}>" 
        return emplist
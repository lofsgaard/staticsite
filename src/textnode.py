class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, __value: object) -> bool:
        if self.text == __value.text and self.text_type == __value.text_type and self.url == __value.url:
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

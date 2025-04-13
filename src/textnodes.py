from enum import Enum

#ENUM FOR TEXTNODE MARKDOWN
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text

        if text_type not in TextType:
            raise ValueError("Value text_type not in TextType ENUM")
        
        self.text_type = text_type
        self.url = url
    #END __init__

    def __eq__(self, other):
        if (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        ):
            return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
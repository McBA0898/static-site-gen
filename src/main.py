from textnode import TextNode
from textnode import TextType

def main():
    text_node = TextNode("This is text", TextType.ITALIC_TEXT, None)
    print(text_node)

main()
import unittest
from leafnode import LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise TypeError("Expected a TextNode instance")
    
    if text_node.text_type == TextType.NORMAL_TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE_TEXT:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINKS:
        if not text_node.url:
            raise ValueError("Links TextNode must have a url")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGES:
        if not text_node.url:
            raise ValueError("Images TextNode must have a url")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Unsupported text type: {text_node.text_type}")

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is text", TextType.NORMAL_TEXT)
        node2 = TextNode("This is text", TextType.NORMAL_TEXT)
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = TextNode("This is text", TextType.BOLD_TEXT)
        node2 = TextNode("This is not text", TextType.BOLD_TEXT)
        self.assertNotEqual(node1, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_link(self):
        node = TextNode("Click here", TextType.LINKS, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_image(self):
        node = TextNode("An image", TextType.IMAGES, "https://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://example.com/image.jpg", "alt": "An image"})

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("Invalid", "unsupported_type"))

if __name__ == "__main__":
    unittest.main


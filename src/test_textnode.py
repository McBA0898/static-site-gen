import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is text", TextType.NORMAL_TEXT)
        node2 = TextNode("This is text", TextType.NORMAL_TEXT)
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = TextNode("This is text", TextType.BOLD_TEXT)
        node2 = TextNode("This is not text", TextType.BOLD_TEXT)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main
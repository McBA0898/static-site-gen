import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag(self):
        node = LeafNode("p", "I wish I could read")
        self.assertEqual(node.to_html(), "<p>I wish I could read</p>")

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me!</a>')

    def test_to_html_without_tag(self):
        node = LeafNode(None, "No tags allowed")
        self.assertEqual(node.to_html(), "No tags allowed")

    def test_to_html_with_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

if __name__=="__main__":
    unittest.main
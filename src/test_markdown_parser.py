import unittest
from markdown_parser import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_bold(self):
        node = TextNode("This is **bold text** in a sentence", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("bold text", TextType.BOLD_TEXT),
            TextNode(" in a sentence", TextType.NORMAL_TEXT)
        ])

    def test_basic_italic(self):
        node = TextNode("This is _italic text_ example", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("italic text", TextType.ITALIC_TEXT),
            TextNode(" example", TextType.NORMAL_TEXT)
        ])

    def test_inline_code(self):
        node = TextNode("This is `code` inside text", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("code", TextType.CODE_TEXT),
            TextNode(" inside text", TextType.NORMAL_TEXT)
        ])

    def test_unmatched_delimiter(self):
        node = TextNode("This is **bold without closing", TextType.NORMAL_TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

    def test_no_delimiters(self):
        node = TextNode("This is plain text", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, [node])

    def text_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def text_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

if __name__ == "__main__":
    unittest.main()

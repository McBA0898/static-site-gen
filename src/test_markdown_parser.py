import unittest
from markdown_parser import *
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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL_TEXT,
    )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", TextType.NORMAL_TEXT),
            TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.NORMAL_TEXT),
            TextNode("second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"),
    ]
        assert new_nodes == expected

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL_TEXT,
    )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"),
    ]
        assert new_nodes == expected

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.NORMAL_TEXT),
            TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL_TEXT),
            TextNode("link", TextType.LINKS, "https://boot.dev"),
        ]

        result = text_to_textnodes(text)
        self.assertEqual(result, expected_nodes)

if __name__ == "__main__":
    unittest.main()

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid Markdown: Unmatched {delimiter}")

        for i, part in enumerate(parts):
            if part == "":
                continue  # Ignore empty splits
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.NORMAL_TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

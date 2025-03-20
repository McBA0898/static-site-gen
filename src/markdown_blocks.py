def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result_blocks = []
    for block in blocks:
        lines = block.strip().split("\n")
        cleaned_lines = [line.strip() for line in lines]
        cleaned_block = "\n".join(cleaned_lines)
        if cleaned_block:
            result_blocks.append(cleaned_block)
    return result_blocks
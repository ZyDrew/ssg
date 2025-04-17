import unittest

from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
## This is an heading 2

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [
                "## This is an heading 2",
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            blocks
        )
        #print(f"BLOCKS 1 : {blocks}")
    
    def test_markdown_to_blocks_two(self):
        md = """
This is **bolded** paragraph
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [
                "This is **bolded** paragraph\n" \
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\n" \
                "- This is a list\n- with items"
            ],
            blocks
        )
        #print(f"BLOCKS 2 : {blocks}")

    def test_markdown_to_blocks_three(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
with an ![image](https://imgur.jpeg)



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\nwith an ![image](https://imgur.jpeg)",
                "- This is a list\n- with items"
            ],
            blocks
        )
        #print(f"BLOCKS 3 : {blocks}")


class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph_block(self):
        block = "This block is a paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_heading_block(self):
        block = "### This block is an heading 3"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)
    
    def test_heading_block_error(self):
        block = "######### This block is an heading 3"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_code_block(self):
        block = "```\nThis block contains some code\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, block_type)
    
    def test_code_block_error(self):
        block = "```\ncode\n"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)
        print(block_type)
    
    def test_quote_block(self):
        block = "> quote1\n> quote2\n> quote3"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, block_type)
    
    def test_quote_block_error(self):
        block = "- quote1\n* quote2\n> quote3"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_ul_block(self):
        block = "- ul1\n- ul2\n- ul3"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.UL, block_type)

    def test_ol_block(self):
        block = "1. ol1\n2. ol2\n3. ol3"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.OL, block_type)
    
    def test_ol_block_error(self):
        block = "1. ol1\n1. ol2\n1. ol3"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    #Course tests
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UL)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OL)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)



class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
### This is an heading 3

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"HTML NODE 1 : {html}")
        self.assertEqual(
            html,
            "<div><h3>This is an heading 3</h3><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
        

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"HTML NODE 2 : {html}")
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"HTML NODE 3 : {html}")
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )


    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"HTML NODE 4 : {html}")
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
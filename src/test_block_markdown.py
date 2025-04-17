import unittest

from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
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
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            blocks
        )
        print(f"BLOCKS 1 : {blocks}")
    
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
        print(f"BLOCKS 2 : {blocks}")

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
        print(f"BLOCKS 3 : {blocks}")
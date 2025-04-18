import unittest

from page_generator import *


class TestPageGenerator(unittest.TestCase):
    def test_extract_title(self):
        md = """
Heading 1

# Heading 10

This is a paragraph
"""

        title = extract_title(md)
        self.assertEqual("Heading 10", title)
        print(f"Extract title : {title}")
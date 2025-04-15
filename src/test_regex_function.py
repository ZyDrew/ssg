import unittest

from regex_function import *


class TestRegex(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        print(f"REGEX1 : {matches}")

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to sloth](https://www.sloth.io)"
        )
        self.assertListEqual([("to sloth", "https://www.sloth.io")], matches)
        print(f"REGEX2 : {matches}")

    def test_extract_markdown_two_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
        print(f"REGEX3 : {matches}")
    
    def test_extract_markdown_two_images(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
        print(f"REGEX4 : {matches}")

    def test_extract_markdown_links_and_images(self):
        matches = extract_markdown_links(
            "This is text with a link [to sloth](https://www.sloth.io) and this is an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("to sloth", "https://www.sloth.io")], matches)
        matches_2 = extract_markdown_images(
            "This is text with a link [to sloth](https://www.sloth.io) and this is an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches_2)
        print(f"REGEX5 : {matches}")
        print(f"REGEX5-2 : {matches_2}")
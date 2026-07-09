"""
Testing Your Solutions

Create tests/test_day02.py:

import unittest
from utils.text import clean_text, tokenize, count_chars
from utils.collections import frequencies, dedupe, group_by

class TestTextUtils(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("  HELLO  "), "hello")

    # Add more tests...

class TestCollections(unittest.TestCase):
    def test_frequencies(self):
        self.assertEqual(frequencies(["a", "b", "a"]), {"a": 2, "b": 1})

    # Add more tests...

if __name__ == "__main__":
    unittest.main()
"""

import unittest

from utils.collections import dedupe, frequencies, group_by
from utils.text import clean_text, count_chars, tokenize


class TestTextUtils(unittest.TestCase):

    def test_clean_text(self):

        self.assertEqual(clean_text("  HELLO  "), "hello")
        self.assertEqual(clean_text("messy   SPACES"), "messy spaces")

    def test_tokenize(self):
        self.assertEqual(tokenize("apple,banana", ","), ["apple", "banana"])
        self.assertEqual(tokenize("hello world"), ["hello", "world"])

    def test_count_chars(self):
        self.assertEqual(count_chars("hello"), {"h": 1, "e": 1, "l": 2, "o": 1})


class TestCollections(unittest.TestCase):

    def test_frequencies(self):
        self.assertEqual(frequencies(["a", "b", "a"]), {"a": 2, "b": 1})
        self.assertEqual(frequencies([]), {})

    def test_dedupe(self):
        self.assertEqual(dedupe(["a", "b", "a"]), ["a", "b"])
        self.assertEqual(dedupe(["apple", "apple"]), ["apple"])

    def test_group_by(self):
        data = [
            {"status": "todo", "id": 1},
            {"status": "done", "id": 2},
            {"status": "todo", "id": 3},
        ]
        expected_output = {
            "todo": [{"status": "todo", "id": 1}, {"status": "todo", "id": 3}],
            "done": [{"status": "done", "id": 2}],
        }
        self.assertEqual(group_by(data, "status"), expected_output)


if __name__ == "__main__":
    unittest.main()

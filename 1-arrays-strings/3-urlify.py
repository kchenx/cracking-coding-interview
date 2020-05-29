# URLify
# Write a method to replace all spaces in a string with '%20'. You may assume
# that the string has sufficient space at the end to hold the additional
# characters, and that you are given the "true" length of the string.
#
# EXAMPLE
# Input: "Mr John Smith    ", 13
# Output: "Mr%20John%20Smith"

import unittest


def urlify(s: str, n: int):
    """Returns first `n` chars of string `s`, with spaces replaced with `%20`"""
    result = []
    for i in range(n):
        result.append(s[i]) if s[i] != " " else result.append("%20")
    return ''.join(result)


class TestUrlify(unittest.TestCase):
    def test_urlify(self):
        self.assertEqual(urlify("abcde   ", 5), "abcde")
        self.assertEqual(urlify("Mr John Smith    ", 13),
                         "Mr%20John%20Smith")
        self.assertEqual(urlify("Mr  John Smith    ", 14),
                         r"Mr%20%20John%20Smith")
        self.assertEqual(urlify("", 0), "")
        self.assertEqual(urlify(" ", 1), "%20")


if __name__ == "__main__":
    unittest.main()

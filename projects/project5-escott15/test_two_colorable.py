import unittest

from two_colorable import is_two_colorable


class Tests(unittest.TestCase):
    def test_simple(self) -> None:
        edges = [["v1", "v2"]]

        self.assertTrue(is_two_colorable(edges))


if __name__ == "__main__":
    unittest.main()

import unittest

from two_colorable import is_two_colorable


class Tests(unittest.TestCase):
    def test_empty_graph(self) -> None:
        edges = []
    
    def test_simple(self) -> None:
        edges = [["v1", "v2"]]

        self.assertTrue(is_two_colorable(edges))
    
    def test_path_graph(self) -> None:
        edges = [["v1", "v2"], ["v2", "v3"], ["v3", "v4"]]

        self.assertTrue(is_two_colorable(edges))

    def test_even_cycle(self) -> None:
        edges = [["v1", "v2"], ["v2", "v3"], ["v3", "v4"], ["v4", "v1"]]

        self.assertTrue(is_two_colorable(edges))

    def test_odd_cycle(self) -> None:
        edges = [["v1", "v2"], ["v2", "v3"], ["v3", "v1"]]

        self.assertFalse(is_two_colorable(edges))

    def test_disconnected_two_colorable(self) -> None:
        edges = [["a", "b"], ["c", "d"], ["d", "e"]]

        self.assertTrue(is_two_colorable(edges))

    def test_disconnected_with_non_two_colorable_component(self) -> None:
        edges = [["a", "b"], ["x", "y"], ["y", "z"], ["z", "x"]]

        self.assertFalse(is_two_colorable(edges))

    def test_self_loop(self) -> None:
        edges = [["v1", "v1"]]

        self.assertFalse(is_two_colorable(edges))


if __name__ == "__main__":
    unittest.main()

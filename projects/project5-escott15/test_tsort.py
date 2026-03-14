import unittest

from tsort import tsort


class Tests(unittest.TestCase):
    # Because topological sorts are not necessarily unique, here's a
    # function to check if the result is valid.
    def check_valid_tsort(self, edges: list[list[str]], result: list[str]) -> None:
        vertices = {v for edge in edges for v in edge}

        # check that your result has all the right vertices
        self.assertCountEqual(result, vertices)

        # for every edge from v1 to v2, check that v1 occurs in the
        # topological sort before v2
        for v1, v2 in edges:
            self.assertLess(result.index(v1), result.index(v2))

    def test_simple(self) -> None:
        edges = [["101", "202"]]

        self.check_valid_tsort(edges, tsort(edges))

    def test_chain(self) -> None: 
        edges = [["a", "b"], ["b", "c"], ["c", "d"]]

        self.check_valid_tsort(edges, tsort(edges))

    def test_branching(self) -> None:
        edges = [["a", "c"], ["b", "c"]]

        self.check_valid_tsort(edges, tsort(edges))
        
    def test_multiple_dependencies(self) -> None:
        edges = [["a", "d"], ["b", "d"], ["c", "d"]]

        self.check_valid_tsort(edges, tsort(edges))

    def test_disconnected(self) -> None:
        edges = [["a", "b"], ["c", "d"]]

        self.check_valid_tsort(edges, tsort(edges))

    def test_cycle(self) -> None:
        edges = [["a", "b"], ["b", "c"], ["c", "a"]]

        with self.assertRaises(ValueError):
            tsort(edges)


if __name__ == "__main__":
    unittest.main()

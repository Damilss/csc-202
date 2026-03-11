import unittest

from linked_list import *

# NOTE: I have previded some basic tests to get you started.  Add more!

#Student Note: I didn't know how to check for index errors 
# since it prevented the tests from finishing


class Tests(unittest.TestCase):
    #empty list test
    def test_empty_list (self):
        self.assertEqual(empty_list(), None)

    #test length
    def test_length_empty_list(self) -> None:
        self.assertEqual(length(None), 0)
    def test_length_LinkedList(self) -> int: 
        self.assertEqual(
            length(Node(0,Node(1,Node(2,None)))),
            3
        )

    #test add item
    def test_add_empty_list(self) -> None:
        self.assertEqual(
            add_item(None, 0, "hello"),
            Node("hello", None)
        )
    def test_add_item_three(self):
        self.assertEqual(
            add_item(Node("Banana", Node("Apple", None)), 1, "Cherry"),
            Node("Banana", Node("Cherry", Node("Apple", None)))
        )
    #test get_item
    def test_get_item_apple(self):
        self.assertEqual(
            get_item(Node("Banana", Node("Apple", None)), 1),
            "Apple",
        )
    def test_get_item_none(self):
        self.assertEqual(
            get_item(None, 0),
            None
        )
    #test set_item
    def test_set_item_none(self):
        self.assertEqual(
            set_item(None, 0, "Apple"),
            Node("Apple", None)
        )
    def test_set_item_list(self):
        self.assertEqual(
            set_item(Node("Banana", Node("Apple", None)), 1, "Cherry"),
            Node("Banana", Node("Cherry", None))
        )
    #test remove
    def test_remove_none(self):
        self.assertEqual(
            remove(None, 0),
            (None, None)
        )
    def remove_list(self):
        self.assertEqual(
            remove(Node("Banana", Node("Apple", None)), 1),
            ("Apple", Node("Banana", None))
        )
    
    # TODO: Add more tests!


if __name__ == "__main__":
    unittest.main()

import unittest

from array_list import add_item, empty_list, get_item, length, remove, set_item

# NOTE: These tests check that the underlying fields of the ArrayList
# are correct after the given operations.  This is arguably quite
# brittle, but is easier than other options.


class Tests(unittest.TestCase):
    def test_length_empty_list(self) -> None:
        self.assertEqual(length(empty_list()), 0)

    def test_add_to_list1(self) -> None:
        my_list = empty_list()
        add_item(my_list, 0, "hello")
        self.assertEqual(my_list.array, ["hello"])

    def test_add_to_list2(self) -> None:
        my_list = empty_list()
        add_item(my_list, 0, "a")
        add_item(my_list, 1, "b")
        add_item(my_list, 2, "c")
        self.assertEqual(my_list.array, ["a", "b", "c", None])

    def test_length_empty(self) -> None:
        my_list = empty_list()
        self.assertEqual(length(my_list), 0)
    
    def test_get_item_empty_list_raises(self) -> None:
        my_list = empty_list()
        with self.assertRaises(IndexError):
            get_item(my_list, 0)
    
    def test_small_add(self) -> None:
        my_list = empty_list()
        add_item(my_list, 0, "a")
        self.assertEqual(my_list.array, ["a"])

    def test_small_add_none(self) -> None:
        my_list = empty_list()
        add_item(my_list, 0, None)
        self.assertEqual(my_list.array, [None])

    def test_add_past_end(self) -> None:
        my_list = empty_list()
        add_item(my_list, 0, "a")
        add_item(my_list, 1, "b")
        add_item(my_list, 2, "c")
        self.assertEqual(my_list.array[:3], ["a", "b", "c"])


    def test_medium_add(self) -> None:
        my_list = empty_list()
        add_item(my_list, 0, "b")
        add_item(my_list, 1, "c")
        add_item(my_list, 0, "a") 
        self.assertEqual(my_list.array[:3], ["a", "b", "c"])
   
        
    def test_large_add_and_get(self) -> None:
        my_list = empty_list()
        add_item(my_list, 0, "a")
        add_item(my_list, 1, "b")
        add_item(my_list, 2, "c")
        add_item(my_list, 3, "d")
        add_item(my_list, 4, "e")
        add_item(my_list, 5, "f")
        self.assertEqual(get_item(my_list, 0), "a")
        self.assertEqual(get_item(my_list, 3), "d")
        self.assertEqual(get_item(my_list, 5), "f")

    def test_set_on_empty_list_raises(self) -> None:
        my_list = empty_list()
        with self.assertRaises(IndexError):
            set_item(my_list, 0, "a")
    
    def test_set_none(self) -> None:
        my_list = empty_list()
        add_item(my_list, 0, "a")
        set_item(my_list, 0, None)
        self.assertIsNone(get_item(my_list, 0))
    
    def test_set_past_end_raises(self) -> None:
        my_list = empty_list()
        add_item(my_list, 0, "a")
        with self.assertRaises(IndexError):
            set_item(my_list, 1, "b")
    
    def test_remove_from_empty_list_raises(self) -> None:
        my_list = empty_list()
        with self.assertRaises(IndexError):
            remove(my_list, 0)

    def test_small_remove(self) -> None:
        my_list = empty_list()
        add_item(my_list, 0, "a")
        removed = remove(my_list, 0)
        self.assertEqual(removed, "a")

    def test_remove_with_none_value(self) -> None:
        my_list = empty_list()
        add_item(my_list, 0, None)
        removed = remove(my_list, 0)
        self.assertIsNone(removed)
        self.assertEqual(my_list.size, 0)

    def test_remove_past_end_raises(self) -> None:
        my_list = empty_list()
        add_item(my_list, 0, "a")
        with self.assertRaises(IndexError):
            remove(my_list, 1) 
    def test_add_item_invalid_index_raises(self) -> None:
        my_list = empty_list()
        with self.assertRaises(IndexError):
            add_item(my_list, 1, "a") 

if __name__ == "__main__":
    unittest.main()

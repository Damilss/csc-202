import unittest

from hash_table import (
    _contents,
    contains,
    djbx33a,
    empty_table,
    get_item,
    keys,
    remove,
    set_item,
    size,
    values,
)


def identity_hash(x: int) -> int:
    return x

def constant_hash(_) -> int:
    return 0

class Tests(unittest.TestCase):
    def test_hash_table_set_twice_then_remove(self) -> None:
        ht = empty_table(identity_hash)
        set_item(ht, 0, "cat")

        self.assertEqual(get_item(ht, 0), "cat")
        self.assertEqual(size(ht), 1)
        self.assertTrue(contains(ht, 0))
        # self.assertCountEqual checks that two lists have the same
        # elements but possibly in a different order
        self.assertCountEqual(keys(ht), [0])
        self.assertCountEqual(values(ht), ["cat"])
        self.assertEqual(_contents(ht), [[(0, "cat")], [], [], [], []])

        # re-insert the same key, replacing the existing key-value pair
        set_item(ht, 0, "dog")

        self.assertEqual(get_item(ht, 0), "dog")
        self.assertEqual(size(ht), 1)
        self.assertTrue(contains(ht, 0))
        self.assertCountEqual(keys(ht), [0])
        self.assertCountEqual(values(ht), ["dog"])
        self.assertEqual(_contents(ht), [[(0, "dog")], [], [], [], []])

        # remove the key, emptying the table
        self.assertEqual(remove(ht, 0), "dog")

        self.assertEqual(size(ht), 0)
        self.assertFalse(contains(ht, 0))
        self.assertCountEqual(keys(ht), [])
        self.assertCountEqual(values(ht), [])
        self.assertEqual(_contents(ht), [[], [], [], [], []])

        with self.assertRaises(KeyError):
            get_item(ht, 0)

    def test_set_item_single_insert(self) -> None:
        ht = empty_table(identity_hash)
        set_item(ht, 0, "cat")

        self.assertEqual(get_item(ht, 0), "cat")
        self.assertEqual(size(ht), 1)
        self.assertTrue(contains(ht, 0))
        self.assertCountEqual(keys(ht), [0])
        self.assertCountEqual(values(ht), ["cat"])
        self.assertEqual(_contents(ht), [[(0, "cat")], [], [], [], []])

    def test_set_item_replace_existing_key(self) -> None:
        ht = empty_table(identity_hash)
        set_item(ht, 0, "cat")
        set_item(ht, 0, "dog")

        self.assertEqual(get_item(ht, 0), "dog")
        self.assertEqual(size(ht), 1)
        self.assertTrue(contains(ht, 0))
        self.assertCountEqual(keys(ht), [0])
        self.assertCountEqual(values(ht), ["dog"])
        self.assertEqual(_contents(ht), [[(0, "dog")], [], [], [], []])

    def test_set_item_separate_chaining_collision(self) -> None:
        ht = empty_table(constant_hash)
        set_item(ht, "a", 1)
        set_item(ht, "b", 2)

        self.assertEqual(size(ht), 2)
        self.assertTrue(contains(ht, "a"))
        self.assertTrue(contains(ht, "b"))
        self.assertEqual(get_item(ht, "a"), 1)
        self.assertEqual(get_item(ht, "b"), 2)

        self.assertEqual(_contents(ht), [[("a", 1), ("b", 2)], [], [], [], []])

    def test_set_item_collision_replace_does_not_duplicate(self) -> None:
        ht = empty_table(constant_hash)
        set_item(ht, "a", 1)
        set_item(ht, "a", 99)

        self.assertEqual(size(ht), 1)
        self.assertEqual(get_item(ht, "a"), 99)
        self.assertEqual(_contents(ht), [[("a", 99)], [], [], [], []])

    def test_set_item_up_to_capacity_no_resize(self) -> None:
        ht = empty_table(identity_hash)

        set_item(ht, 0, "v0")
        set_item(ht, 1, "v1")
        set_item(ht, 2, "v2")
        set_item(ht, 3, "v3")
        set_item(ht, 4, "v4")

        self.assertEqual(ht.capacity, 5)
        self.assertEqual(size(ht), 5)
        self.assertEqual(
            _contents(ht),
            [[(0, "v0")], [(1, "v1")], [(2, "v2")], [(3, "v3")], [(4, "v4")]],
        )

    def test_set_item_resize_on_exceeding_load_factor(self) -> None:
        ht = empty_table(identity_hash)

        for k in range(5):
            set_item(ht, k, f"v{k}")
        self.assertEqual(ht.capacity, 5)
        self.assertEqual(size(ht), 5)

        set_item(ht, 5, "v5")

        self.assertEqual(ht.capacity, 10)
        self.assertEqual(size(ht), 6)

        self.assertEqual(
            _contents(ht),
            [
                [(0, "v0")],
                [(1, "v1")],
                [(2, "v2")],
                [(3, "v3")],
                [(4, "v4")],
                [(5, "v5")],
                [],
                [],
                [],
                [],
            ],
        )

        for k in range(6):
            self.assertEqual(get_item(ht, k), f"v{k}")
            self.assertTrue(contains(ht, k))

    def test_set_item_replace_does_not_trigger_resize(self) -> None:
        ht = empty_table(identity_hash)

        for k in range(5):
            set_item(ht, k, f"v{k}")
        self.assertEqual(ht.capacity, 5)
        self.assertEqual(size(ht), 5)

        set_item(ht, 3, "NEW")
        self.assertEqual(ht.capacity, 5)
        self.assertEqual(size(ht), 5)
        self.assertEqual(get_item(ht, 3), "NEW")

    def test_remove_raises_keyerror_when_missing_empty_table(self) -> None:
        ht = empty_table(identity_hash)

        with self.assertRaises(KeyError):
            remove(ht, 0)

    def test_djbx33a_basic_cases(self) -> None:
        self.assertEqual(djbx33a(""), 5381)

        self.assertEqual(djbx33a("a"), 5381 * 33 + ord("a"))

        expected_ab = (5381 * 33 + ord("a")) * 33 + ord("b")
        self.assertEqual(djbx33a("ab"), expected_ab)

        self.assertNotEqual(djbx33a("ab"), djbx33a("ba"))
        
if __name__ == "__main__":
    unittest.main()

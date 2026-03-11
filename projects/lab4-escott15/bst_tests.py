import unittest

from bst import (
    TreeNode,
    delete,
    find_max,
    find_min,
    height,
    insert,
    is_empty,
    search,
    TreeNode
)



class Tests(unittest.TestCase):
    def test_is_empty(self):
        self.assertTrue(is_empty(None))

    def test_is_not_empty_tree(self):
        self.assertFalse(is_empty(TreeNode(7, None, None)))


    def test_delete_empty(self):
        self.assertIsNone(delete(None, 5))

    def test_delete_not_present(self):
        tree = TreeNode(5, None, None)
        self.assertEqual(delete(tree, 7), tree)

    def test_delete_leaf(self):
        tree = TreeNode(5, TreeNode(3, None, None), None)
        result = delete(tree, 3)
        self.assertEqual(result, TreeNode(5, None, None))

    def test_delete_one_child_left(self):
        tree = TreeNode(5, TreeNode(3, None, None), None)
        result = delete(tree, 5)
        self.assertEqual(result, TreeNode(3, None, None))

    def test_delete_one_child_right(self):
        tree = TreeNode(5, None, TreeNode(7, None, None))
        result = delete(tree, 5)
        self.assertEqual(result, TreeNode(7, None, None))

    def test_delete_two_children(self):
        tree = TreeNode(
            5,
            TreeNode(3, None, None),
            TreeNode(7, None, None)
        )
        result = delete(tree, 5)
        self.assertEqual(result.value, 7)


    def test_find_max_empty(self):
        self.assertIsNone(find_max(None))

    def test_find_max_single(self):
        self.assertEqual(find_max(TreeNode(7, None, None)), 7)

    def test_find_max_general(self):
        tree = TreeNode(
            5,
            TreeNode(3, None, None),
            TreeNode(8, TreeNode(7, None, None), None)
        )
        self.assertEqual(find_max(tree), 8)


    def test_find_min_empty(self):
        self.assertIsNone(find_min(None))

    def test_find_min_single(self):
        self.assertEqual(find_min(TreeNode(7, None, None)), 7)

    def test_find_min_general(self):
        tree = TreeNode(
            5,
            TreeNode(3, None, None),
            TreeNode(8, TreeNode(6, None, None), None)
        )
        self.assertEqual(find_min(tree), 3)


    def test_height_empty(self):
        self.assertEqual(height(None), -1)

    def test_height_single(self):
        self.assertEqual(height(TreeNode(7, None, None)), 0)

    def test_height_left_heavy(self):
        tree = TreeNode(5, TreeNode(3, TreeNode(1, None, None), None), None)
        self.assertEqual(height(tree), 2)

    def test_height_right_heavy(self):
        tree = TreeNode(5, None, TreeNode(7, None, TreeNode(9, None, None)))
        self.assertEqual(height(tree), 2)

    def test_insert_empty(self):
        self.assertEqual(insert(None, 5), TreeNode(5, None, None))

    def test_insert_left(self):
        tree = TreeNode(5, None, None)
        self.assertEqual(
            insert(tree, 3),
            TreeNode(5, TreeNode(3, None, None), None)
        )

    def test_insert_right(self):
        tree = TreeNode(5, None, None)
        self.assertEqual(
            insert(tree, 7),
            TreeNode(5, None, TreeNode(7, None, None))
        )

    def test_insert_duplicate(self):
        tree = TreeNode(5, None, None)
        self.assertEqual(insert(tree, 5), tree)


    def test_search_empty(self):
        self.assertFalse(search(None, 5))

    def test_search_single_found(self):
        self.assertTrue(search(TreeNode(7, None, None), 7))

    def test_search_single_not_found(self):
        self.assertFalse(search(TreeNode(7, None, None), 3))

    def test_search_left_subtree(self):
        tree = TreeNode(5, TreeNode(3, None, None), None)
        self.assertTrue(search(tree, 3))

    def test_search_right_subtree(self):
        tree = TreeNode(5, None, TreeNode(8, None, None))
        self.assertTrue(search(tree, 8))


if __name__ == "__main__":
    unittest.main()

import unittest

from sorts import insertion_sort, merge_sort, selection_sort


class Tests(unittest.TestCase):
    # I provided tests for full coverage of merge sort.
    def test_merge_sort_01(self) -> None:
        lst = [10]

        comps = merge_sort(lst)

        # Sorting an singleton list should do no comparisons
        self.assertEqual(comps, 0)

        # The list shouldn't change, it's already sorted
        self.assertEqual(lst, [10])

    def test_merge_sort_02(self) -> None:
        lst = [50, 60, 10, 20, 80, 40, 30, 70]

        comps = merge_sort(lst)

        # A list of size 8 should be doing fewer than 8 * log_2(8) comparisons
        # (the worst case is roughly n * log_2(n)).
        self.assertLessEqual(comps, 8 * 3)

        # The list should now be sorted
        self.assertEqual(lst, [10, 20, 30, 40, 50, 60, 70, 80])

    def test_selection_sort_01(self):
        """Sort all the way through + one already sorted"""
        lst = [12, 14, 10 , 8, 6] 
        count = selection_sort(lst)

        expected_lst = [6, 8, 10, 12, 14] 
        expected_count: int = 25 

        self.assertEqual(expected_lst, lst)
        self.assertGreater(expected_count, count)

    def test_seleection_sort_02(self):
        lst = [10] 
        count = selection_sort(lst)

        expected_lst = [10]
        expected_count: int = 0

        self.assertEqual(expected_lst, lst)
        self.assertEqual(expected_count, count)

    def test_seleection_sort_03(self):
        lst = [20, 10] 
        count = selection_sort(lst)

        expected_lst = [10, 20]
        expected_count: int = 4

        self.assertEqual(expected_lst, lst)
        self.assertGreater(expected_count, count)
    
    def test_selection_sort_04(self):
        lst = []
        count = selection_sort(lst)

        expected_lst = [] 
        expected_count: int = 0 

        self.assertEqual(expected_lst, lst)
        self.assertEqual(expected_count, count)

    def test_insertion_sort_01(self):
        lst = [12, 14, 10, 8, 6] 
        count = insertion_sort(lst)

        expected_lst = [6, 8, 10, 12, 14] 
        expected_count: int =  25

        self.assertEqual(expected_lst, lst)
        self.assertGreater(expected_count, count)

    def test_insertion_sort_02  (self):
        lst = [] 
        count = insertion_sort(lst)

        expected_lst = [] 
        expected_count: int = 0 

        self.assertEqual(expected_lst, lst)
        self.assertEqual(expected_count, count)

    def test_insertion_sort_03(self):
        lst = [25]
        count = insertion_sort(lst)

        expected_lst = [25] 
        expected_count: int = 0 

        self.assertEqual(expected_lst, lst)
        self.assertEqual(expected_count, count)


if __name__ == "__main__":
    unittest.main()

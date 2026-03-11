import unittest

from heap import (
    _contents,
    dequeue,
    empty_heap,
    enqueue,
    heap_sort,
    heapify,
    peek,
    size,
)


class Tests(unittest.TestCase):
    def test_heap_simple_operations(self):
        my_heap = empty_heap()
        enqueue(my_heap, 10)

        self.assertEqual(size(my_heap), 1)
        self.assertEqual(_contents(my_heap), [10])
        self.assertEqual(peek(my_heap), 10)

    def test_sift_down_no_children_does_nothing(self):
        heap = empty_heap()
        heap.items += [10]
        heap._sift_down(1)
        self.assertEqual(_contents(heap), [10])

    def test_sift_down_swaps_with_left_child_when_left_is_smaller(self):
        heap = empty_heap()
        heap.items += [9, 1, 8]
        heap._sift_down(1)
        self.assertEqual(_contents(heap), [1, 9, 8])
    
    def test_sift_down_swaps_with_right_child_when_right_is_smaller(self):
        heap = empty_heap()
        heap.items += [9, 8, 1]
        heap._sift_down(1)
        self.assertEqual(_contents(heap), [1, 8, 9])

    def test_sift_down_can_continue_multiple_levels(self):
        heap = empty_heap()
        heap.items += [9, 1, 2, 0]
        heap._sift_down(1)
        self.assertEqual(_contents(heap), [1,0,2,9])

    def test_sift_up_no_swap_when_heap_property_holds(self):
        heap=empty_heap()
        heap.items+=[1,3]
        heap._sift_up(2)
        self.assertEqual(_contents(heap),[1,3])

    def test_sift_up_single_swap(self):
        heap=empty_heap()
        heap.items+=[5,1]
        heap._sift_up(2)
        self.assertEqual(_contents(heap),[1,5])

    def test_sift_up_multiple_swaps(self):
        heap=empty_heap()
        heap.items+=[3,5,6,1]
        heap._sift_up(4)
        self.assertEqual(_contents(heap),[3, 1, 6, 5])

    def test_empty_heap_initial_state(self):
        heap=empty_heap()
        self.assertEqual(size(heap),0)
        self.assertEqual(_contents(heap),[])

    def test_empty_heap_independent_instances(self):
        heap1=empty_heap()
        heap2=empty_heap()
        enqueue(heap1,10)
        self.assertEqual(size(heap1),1)
        self.assertEqual(size(heap2),0)

    def test_enqueue_single_element(self):
        heap=empty_heap()
        enqueue(heap,10)
        self.assertEqual(size(heap),1)
        self.assertEqual(_contents(heap),[10])

    def test_enqueue_triggers_sift_up(self):
        heap=empty_heap()
        enqueue(heap,10)
        enqueue(heap,5)
        self.assertEqual(_contents(heap),[5,10])

    def test_enqueue_multiple_elements(self):
        heap=empty_heap()
        enqueue(heap,10)
        enqueue(heap,7)
        enqueue(heap,3)
        enqueue(heap,8)
        self.assertEqual(_contents(heap),[3,8,7,10])

    def test_dequeue_raises_on_empty(self):
        heap=empty_heap()
        with self.assertRaises(IndexError):
            dequeue(heap)

    def test_dequeue_single_element(self):
        heap=empty_heap()
        enqueue(heap,10)
        self.assertEqual(dequeue(heap),10)
        self.assertEqual(size(heap),0)
        self.assertEqual(_contents(heap),[])

    def test_dequeue_returns_largest(self):
        heap=empty_heap()
        enqueue(heap,5)
        enqueue(heap,2)
        enqueue(heap,8)
        enqueue(heap,1)
        self.assertEqual(dequeue(heap),8)

    def test_dequeue_updates_structure(self):
        heap=empty_heap()
        enqueue(heap,4)
        enqueue(heap,1)
        enqueue(heap,7)
        enqueue(heap,3)
        dequeue(heap)
        self.assertEqual(_contents(heap),[1,3,4])

    def test_peek_raises_on_empty(self):
        heap=empty_heap()
        with self.assertRaises(IndexError):
            peek(heap)

    def test_peek_single_element(self):
        heap=empty_heap()
        enqueue(heap,10)
        self.assertEqual(peek(heap),10)
        self.assertEqual(_contents(heap),[10])

    def test_peek_returns_largest(self):
        heap=empty_heap()
        enqueue(heap,5)
        enqueue(heap,2)
        enqueue(heap,8)
        enqueue(heap,1)
        self.assertEqual(peek(heap),8)

    def test_peek_does_not_modify_heap(self):
        heap=empty_heap()
        enqueue(heap,4)
        enqueue(heap,1)
        enqueue(heap,7)
        enqueue(heap,3)
        before=_contents(heap)
        peek(heap)
        self.assertEqual(_contents(heap),before)
    
    def test_size_empty(self):
        heap=empty_heap()
        self.assertEqual(size(heap),0)

    def test_size_after_enqueue(self):
        heap=empty_heap()
        enqueue(heap,10)
        self.assertEqual(size(heap),1)

    def test_size_after_multiple_operations(self):
        heap=empty_heap()
        enqueue(heap,5)
        enqueue(heap,2)
        enqueue(heap,8)
        dequeue(heap)
        self.assertEqual(size(heap),2)

    #not sure if you wanted these but I added them anyway.
    def test_contents_empty(self):
        heap=empty_heap()
        self.assertEqual(_contents(heap),[])

    def test_contents_single_element(self):
        heap=empty_heap()
        enqueue(heap,10)
        self.assertEqual(_contents(heap),[10])

    def test_contents_multiple_elements(self):
        heap=empty_heap()
        enqueue(heap,5)
        enqueue(heap,2)
        enqueue(heap,8)
        self.assertEqual(_contents(heap),[2,5,8])

    def test_heapify_empty_list(self):
        heap=heapify([])
        self.assertEqual(size(heap),0)
        self.assertEqual(_contents(heap),[])

    def test_heapify_single_element(self):
        heap=heapify([10])
        self.assertEqual(_contents(heap),[10])

    def test_heapify_unsorted_list(self):
        heap=heapify([5,3,8,1])
        self.assertEqual(_contents(heap),[1,3,8,5])

    def test_heapify_does_not_modify_input(self):
        lst=[4,2,7,1]
        heap=heapify(lst)
        self.assertEqual(lst,[4,2,7,1])
    
    def test_heap_sort_empty(self):
        lst=[]
        heap_sort(lst)
        self.assertEqual(lst,[])

    def test_heap_sort_single_element(self):
        lst=[10]
        heap_sort(lst)
        self.assertEqual(lst,[10])

    def test_heap_sort_multiple_elements(self):
        lst=[5,2,8,1]
        heap_sort(lst)
        self.assertEqual(lst,[8, 5, 2, 1])

    def test_heap_sort_with_duplicates(self):
        lst=[4,1,3,1]
        heap_sort(lst)
        self.assertEqual(lst,[4, 3, 1, 1])

    def test_peek_updates_largest_during_scan(self):
        heap=empty_heap()
        heap.items+=[1,2,3,4,10,6]
        self.assertEqual(peek(heap),10)






if __name__ == "__main__":
    unittest.main()

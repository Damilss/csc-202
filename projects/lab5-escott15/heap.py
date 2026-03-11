"""
parent idx = i // 2 
child left idx = i * 2
child right idx = i * 2 + 1 

Use helper functions in order to sift up and to sift down. 
"""
from dataclasses import dataclass

from typing import Any


@dataclass
class MinHeap:
    items: list[Any]


    def _sift_down(self, i):
        n = len(self.items) - 1
        while 2 * i <= n:
            left_idx = 2 * i
            right_idx = 2 * i + 1 
            smallest_idx = left_idx

            if right_idx <= n and self.items[right_idx] < self.items[left_idx]:
                smallest_idx = right_idx

            if self.items[smallest_idx] < self.items[i]:
                self.items[i], self.items[smallest_idx] = self.items[smallest_idx], self.items[i]
                i = smallest_idx
            else:
                break
    
    def _sift_up(self, idx: int) -> None: 
        parent_idx = idx // 2 
        while idx > 1:
            if self.items[idx]  < self.items[parent_idx]:
                self.items[idx], self.items[parent_idx] = self.items[parent_idx], self.items[idx] 
                idx = parent_idx
            else: 
                break


def empty_heap() -> MinHeap:
    """Returns Empty Heap"""
    return MinHeap([None])


def enqueue(heap: MinHeap, item: Any) -> None:
    """adds item to the heap in the appropriate position."""
    heap.items.append(item)
    heap._sift_up(len(heap.items)-1)


def dequeue(heap: MinHeap) -> Any:
    """removes and returns the largest item in the Heap"""
    if len(heap.items) == 1:
        raise IndexError

    idx = (len(heap.items) - 1) // 2 + 1
    largest_idx = idx

    while idx < len(heap.items):
        if heap.items[idx] > heap.items[largest_idx]:
            largest_idx = idx
        idx += 1

    largest = heap.items[largest_idx]

    heap.items[largest_idx] = heap.items[-1]
    heap.items.pop()

    return largest


def peek(heap: MinHeap) -> Any:
    """returns largest item in the heap without removing it"""
    if len(heap.items) == 1:
        raise IndexError

    idx = (len(heap.items) - 1) // 2 + 1
    largest = heap.items[idx]

    while idx < len(heap.items):
        if heap.items[idx] > largest:
            largest = heap.items[idx]
        idx += 1

    return largest


def size(heap: MinHeap) -> Any:
    """returns the number of items in the heap"""
    return len(heap.items) - 1 


# NOTE: To be used for testing, the "contents" of the heap are
# everything except index 0 (which we leave blank).
def _contents(heap: MinHeap) -> list[Any]:
    """returns a minimum binary Heap"""
    return heap.items[1:]


def heapify(lst: list[Any]) -> MinHeap:
    """sort lst to be min binary heap and returns MinHeap"""
    heap = empty_heap()
    heap.items += lst[:]

    idx = (len(heap.items) - 1) // 2

    while idx >= 1:
        heap._sift_down(idx)
        idx -= 1

    return heap


def heap_sort(lst: list[Any]) -> None:
    """Mutates list to be sorted in ascending order, returns none"""
    heap = heapify(lst)

    idx = 0
    while idx < len(lst):
        lst[idx]=dequeue(heap)
        idx += 1


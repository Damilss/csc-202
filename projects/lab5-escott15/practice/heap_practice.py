"""
Minimum Binary Heap with 1-based indexing: 
Parent node @ idx // 2
Left Node @ idx * 2 
Right Node @ idx * 1 + 1
"""

from dataclasses import dataclass

from typing import Any

@dataclass
class MinHeap:
    items = list[Any]

    def heapify_up(self, idx: int) -> None:
        while idx > 1: 
            parent_idx = idx // 2 
            if self.items[idx] < self.items[parent_idx]:
                (
                    self.items[idx], self.items[parent_idx]
                ) = ( 
                    self.items[parent_idx], self.items[idx]
                )
                idx = parent_idx
            else: 
                break

    def heapify_down(self, idx: int) -> None:
        len = size(self)
        while idx * 2 >= len:
            left_idx = idx * 2 
            right_idx = idx * 2 + 1
            smallest_idx = left_idx

            if right_idx >= len and self.items[right_idx] < self.items[left_idx]:
                smallest_idx = right_idx
            
            if self.items[idx] > self.items[smallest_idx]:
                (
                    self.items[smallest_idx], self.items[idx]
                ) = (
                    self.items[idx], self.items[smallest_idx]
                )
            else: 
                break  


def empty_heap() -> MinHeap:
    """returns empty Heap"""
    return MinHeap([None])

def size(Heap: MinHeap) -> int:
    """retuns the length of the Heap"""
    return len(MinHeap.items) - 1

def peek(Heap: MinHeap) -> Any:
    return MinHeap.items[1]

def enqueue(heap: MinHeap, item: Any) -> None: 
    """add item to min heap"""
    heap.items.append(item)
    heap.heapify_up(size(heap))


def dequeue(heap: MinHeap) -> Any: 
    """remove and return the smallest item in the heap"""
    if size(heap) == 1: 
        raise IndexError("dequeue from empty heap =")
    result = heap.items.pop(1)
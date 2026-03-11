from dataclasses import dataclass

from typing import Any

type List = Node | None


@dataclass(frozen=True)
class Node:
    first: Any
    rest: List


@dataclass(frozen=True)
class LinkedQueue:
    front: List
    end: List


def empty_queue() -> LinkedQueue:
    return LinkedQueue(None,None)



def enqueue(queue: LinkedQueue, value: Any) -> LinkedQueue:
    node = Node(value, None)

    if queue.front is None:
        return LinkedQueue(node, node)

    def copy(lst):
        if lst.rest is None:
            return Node(lst.first, node)
        return Node(lst.first, copy(lst.rest))

    return LinkedQueue(copy(queue.front), node)


def dequeue(queue: LinkedQueue) -> tuple[Any, LinkedQueue]:
    if queue.front is None:
        raise IndexError("dequeue from empty queue")
    
    value = queue.front.first
    new_front = queue.front.rest

    if new_front is None:
        return value, LinkedQueue(None, None)

    return value, LinkedQueue(new_front, queue.end)

def peek(queue: LinkedQueue) -> Any:
    if queue.front is None:
        raise IndexError("peek from empty queue")
    return queue.front.first


def is_empty(queue: LinkedQueue) -> bool:
    return queue.front == None


def size(queue: LinkedQueue) -> int:
    def count(lst):
        if lst is None:
            return 0
        return 1 + count(lst.rest)

    return count(queue.front)
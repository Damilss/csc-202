from dataclasses import dataclass

from typing import Any


@dataclass
class CircularQueue:
    array: list[Any]
    capacity: int
    size: int
    front: int


def empty_queue() -> CircularQueue:
    """returns empty queue
    :return: Description
    :rtype: CircularQueue"""
    return CircularQueue([None], 1, 0, 0)


def enqueue(queue: CircularQueue, value: Any) -> None:
    """Adds item to front of queue
    :param queue: Description
    :type queue: CircularQueue
    :param value: Description
    :type value: Any"""
    if queue.size == queue.capacity:
        new_capacity = queue.capacity * 2
        new_array = [None] * new_capacity

        for i in range(queue.size):
            new_array[i] = queue.array[(queue.front + i) % queue.capacity]

        queue.array = new_array
        queue.capacity = new_capacity
        queue.front = 0

    rear = (queue.front + queue.size) % queue.capacity
    queue.array[rear] = value
    queue.size += 1
                


def dequeue(queue: CircularQueue) -> Any:
    '''Returns item at end of queue (FIFO)
    :param queue: Description
    :type queue: CircularQueue
    :return: Description
    :rtype: Any'''
    if queue.size == 0:
        raise IndexError("dequeue from empty queue")

    value = queue.array[queue.front]
    queue.array[queue.front] = None  # optional, helps debugging
    queue.front = (queue.front + 1) % queue.capacity
    queue.size -= 1
    return value


def peek(queue: CircularQueue) -> Any:
    '''Returns the front of the queue
    :param queue: Description
    :type queue: CircularQueue
    :return: Description
    :rtype: Any'''
    if queue.size == 0:
        raise IndexError("peek from empty queue")
    return queue.array[queue.front]


def is_empty(queue: CircularQueue) -> bool:
    """Returns size of circular queue
    :param queue: Description
    :type queue: CircularQueue
    :return: Description
    :rtype: bool"""
    return queue.size == 0 


def size(queue: CircularQueue) -> int:
    """Returns size of CircularQueue
    :param queue: Description
    :type queue: CircularQueue
    :return: Description
    :rtype: int"""
    return queue.size
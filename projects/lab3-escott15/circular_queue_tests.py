import unittest

from circular_queue import (
    dequeue,
    empty_queue,
    enqueue,
    is_empty,
    peek,
    size,
)


class Tests(unittest.TestCase):
    def test_enqueue_one_value(self) -> None:
        my_queue = empty_queue()
        enqueue(my_queue, 10)

        self.assertEqual(my_queue.capacity, 1)
        self.assertEqual(my_queue.array[0], 10)
        self.assertEqual(my_queue.front, 0)
        self.assertEqual(my_queue.size, 1)

    # TODO: add more tests!


if __name__ == "__main__":
    unittest.main()

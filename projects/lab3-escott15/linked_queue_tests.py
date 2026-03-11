import unittest

from linked_queue import (
    LinkedQueue,
    Node,
    dequeue,
    empty_queue,
    enqueue,
    is_empty,
    peek,
    size,
)


class Tests(unittest.TestCase):
    def test_enqueue_one_value(self) -> None:
        self.assertEqual(
            enqueue(empty_queue(), 10),
            LinkedQueue(Node(10, None), None),
        )

    def test_enqueue_on_nonempty(self) -> None:
        q0 = LinkedQueue(Node(1, None), Node(1, None))
        q1 = enqueue(q0, 2)
        self.assertEqual(q1, LinkedQueue(Node(1, Node(2, None)), Node(2, None)))
        self.assertEqual(q0, LinkedQueue(Node(1, None), Node(1, None)))

    def test_dequeue_single_value(self) -> None:
        q = LinkedQueue(Node(42, None), None)
        value, q2 = dequeue(q)
        self.assertEqual(value, 42)
        self.assertEqual(q2, LinkedQueue(None, None))

    def test_dequeue_multiple_values(self) -> None:
        q = LinkedQueue(Node(1, Node(2, Node(3, None))), Node(3, None))
        val, q2 = dequeue(q)
        self.assertEqual(val, 1)
        self.assertEqual(q2, LinkedQueue(Node(2, Node(3, None)), Node(3, None)))

    def test_dequeue_empty_raises(self) -> None:
        with self.assertRaises(IndexError):
            dequeue(empty_queue())

    def test_peek_and_peek_empty(self) -> None:
        q = LinkedQueue(Node("a", None), None)
        self.assertEqual(peek(q), "a")
        with self.assertRaises(IndexError):
            peek(empty_queue())

    def test_is_empty_true_false(self) -> None:
        self.assertTrue(is_empty(empty_queue()))
        self.assertFalse(is_empty(LinkedQueue(Node(0, None), None)))

    def test_size_counts(self) -> None:
        self.assertEqual(size(empty_queue()), 0)
        q = LinkedQueue(Node(1, Node(2, None)), Node(2, None))
        self.assertEqual(size(q), 2)
        q_single = LinkedQueue(Node(99, None), None)
        self.assertEqual(size(q_single), 1)

    def test_fifo_order_preserved(self) -> None:
        q = empty_queue()
        q1 = enqueue(q, "x")
        q2 = enqueue(q1, "y")
        v1, q3 = dequeue(q2)
        v2, q4 = dequeue(q3)
        self.assertEqual((v1, v2), ("x", "y"))
        self.assertTrue(is_empty(q4))


if __name__ == "__main__":
    unittest.main()

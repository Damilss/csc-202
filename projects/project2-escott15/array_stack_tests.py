import unittest

from array_stack import (empty_stack, is_empty, peek, pop, push, size, ArrayStack)


class Tests(unittest.TestCase):
    def test_empty_stack(self):
        stack = empty_stack()

        self.assertEqual(stack.size, 0)
        self.assertEqual(stack.capacity, 1)
        self.assertEqual(stack.array, [None])
    
    def test_push_empty(self):
        stack = empty_stack()
        push(stack, 10)

        self.assertEqual(stack.size, 1)
        self.assertEqual(stack.capacity, 1)
        self.assertEqual(stack.array[0], 10)
    
    def test_push_resize(self):
        stack = empty_stack()
        push(stack, 1)
        push(stack, 2)  # triggers resize

        self.assertEqual(stack.size, 2)
        self.assertEqual(stack.capacity, 2)
        self.assertEqual(stack.array[0], 1)
        self.assertEqual(stack.array[1], 2)

    def test_is_empty_empty_stack(self):
        stack = empty_stack()
        self.assertTrue(is_empty(stack))

    def test_is_empty_not_empty(self):
        stack = empty_stack()
        push(stack, 10)
        self.assertFalse(is_empty(stack))

    def test_peek_empty(self):
        stack = empty_stack()
        with self.assertRaises(IndexError):
            peek(stack)

    def test_peek_not_empty(self):
        stack = empty_stack()
        push(stack, 10)
        push(stack, 20)

        self.assertEqual(peek(stack), 20)
        self.assertEqual(stack.size, 2)

    def test_pop_empty(self):
        stack = empty_stack()
        with self.assertRaises(IndexError):
            pop(stack)

    def test_pop_not_empty(self):
        stack = empty_stack()
        push(stack, 10)
        push(stack, 20)

        value = pop(stack)

        self.assertEqual(value, 20)
        self.assertEqual(stack.size, 1)
        self.assertEqual(stack.array[0], 10)

    def test_size_empty(self):
        stack = empty_stack()
        self.assertEqual(size(stack), 0)

    def test_size_non_empty(self):
        stack = empty_stack()
        push(stack, 10)
        push(stack, 20)

        self.assertEqual(size(stack), 2)


if __name__ == "__main__":
    unittest.main()
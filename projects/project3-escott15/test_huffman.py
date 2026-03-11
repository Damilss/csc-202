import io
import unittest

# NOTE: Do not import anything else from huffman.  If you do, your tests
# will crash when I test them.  You shouldn't need to test your helper
# functions directly, just via testing the required functions.
# If you do want to test your helpers directly, please put those tests
# in test_huffman_helper.py
from huffman import (
    HuffmanLeaf,
    HuffmanNode,
    build_huffman_tree,
    count_frequencies,
    create_codes,
    create_header,
    huffman_encode
)


class TestList(unittest.TestCase):
    def test_count_frequencies_01(self) -> None:
        # Create fake file to use for testing
        with io.StringIO("ddddddddddddddddccccccccbbbbaaff") as in_file:
            frequencies = count_frequencies(in_file)

        expected = [0] * 256
        expected[97:103] = [2, 4, 8, 16, 0, 2]

        self.assertEqual(frequencies, expected)

    # NOTE: This is the same test as count_frequencies_01 but with a real file
    def test_count_frequencies_02(self) -> None:
        with open("file2.txt", encoding="utf8") as in_file:
            frequencies = count_frequencies(in_file)

        expected = [0] * 256
        expected[97:103] = [2, 4, 8, 16, 0, 2]

        self.assertEqual(frequencies, expected)

    def test_huffman_encode_01(self) -> None:
        with io.StringIO("abcd abc ab a") as in_file, io.StringIO() as out_file:
            huffman_encode(in_file, out_file)
            result = out_file.getvalue()

        correct_out_text = "32 3 97 4 98 3 99 2 100 1\n11011011000011011010011010011"

        self.assertEqual(result, correct_out_text)

    # NOTE: This is the same test as encode_01, but with real files
    def test_huffman_encode_02(self) -> None:
        with open("file1.txt", encoding="utf8") as in_file, io.StringIO() as out_file:
            huffman_encode(in_file, out_file)
            result = out_file.getvalue()

        with open("file1_encoded.txt", encoding="utf8") as correct_out:
            self.assertEqual(result, correct_out.read())

    def test_count_frequencies_empty(self) -> None:
        with io.StringIO("") as in_file:
            frequencies = count_frequencies(in_file)

        self.assertEqual(frequencies, [0] * 256)

    def test_count_frequencies_multiple_chars(self) -> None:
        with io.StringIO("abcabc") as in_file:
            frequencies = count_frequencies(in_file)

        expected = [0] * 256
        expected[ord('a')] = 2
        expected[ord('b')] = 2
        expected[ord('c')] = 2
        self.assertEqual(frequencies, expected)

    def test_count_frequencies_newline(self) -> None:
        with io.StringIO("a\nb") as in_file:
            frequencies = count_frequencies(in_file)

        expected = [0] * 256
        expected[ord('a')] = 1
        expected[ord('\n')] = 1
        expected[ord('b')] = 1
        self.assertEqual(frequencies, expected)

    def test_build_tree_all_zeros(self) -> None:
        freqs = [0] * 256
        tree = build_huffman_tree(freqs)
        self.assertIsNone(tree)

    def test_build_tree_single_char(self) -> None:
        freqs = [0] * 256
        freqs[ord('x')] = 5
        tree = build_huffman_tree(freqs)

        self.assertIsInstance(tree, HuffmanLeaf)
        self.assertEqual(tree.char, ord('x'))
        self.assertEqual(tree.frequency, 5)

    def test_build_tree_two_chars(self) -> None:
        freqs = [0] * 256
        freqs[ord('a')] = 1
        freqs[ord('b')] = 3
        tree = build_huffman_tree(freqs)

        self.assertIsInstance(tree, HuffmanNode)
        self.assertEqual(tree.frequency, 4)
        self.assertEqual(tree.char, ord('a'))

        self.assertIsInstance(tree.left, HuffmanLeaf)
        self.assertIsInstance(tree.right, HuffmanLeaf)
    
    def test_build_tree_(self):
        ...

    
    def test_build_tree_tie_break_left_is_smaller_char(self) -> None:
        freqs = [0] * 256
        freqs[ord('a')] = 2
        freqs[ord('b')] = 2
        tree = build_huffman_tree(freqs)

        self.assertIsInstance(tree, HuffmanNode)
        self.assertEqual(tree.frequency, 4)
        self.assertEqual(tree.char, ord('a'))

        self.assertEqual(tree.left.char, ord('a'))
        self.assertEqual(tree.right.char, ord('b'))

    def test_build_tree_three_chars(self) -> None:
        freqs = [0] * 256
        freqs[ord('c')] = 1
        freqs[ord('a')] = 2
        freqs[ord('b')] = 3
        tree = build_huffman_tree(freqs)

        self.assertIsInstance(tree, HuffmanNode)
        self.assertEqual(tree.frequency, 6)
        self.assertEqual(tree.char, ord('a'))

    def test_create_codes_none(self) -> None:
        codes = create_codes(None)
        self.assertEqual(len(codes), 256)
        self.assertEqual(codes, [""] * 256)
    
    def test_create_codes_single_leaf(self) -> None:
        tree = HuffmanLeaf(ord('x'), 7)
        codes = create_codes(tree)

        self.assertEqual(len(codes), 256)
        self.assertEqual(codes[ord('x')], "0")

    def test_create_codes_two_leaves(self) -> None:
        left = HuffmanLeaf(ord('a'), 1)
        right = HuffmanLeaf(ord('b'), 1)
        tree = HuffmanNode(min(left.char, right.char), left.frequency + right.frequency, left, right)

        codes = create_codes(tree)

        self.assertEqual(codes[ord('a')], "0")
        self.assertEqual(codes[ord('b')], "1")

    def test_create_codes_deeper_tree(self) -> None:
        a = HuffmanLeaf(ord('a'), 5)
        b = HuffmanLeaf(ord('b'), 2)
        c = HuffmanLeaf(ord('c'), 1)

        right = HuffmanNode(min(b.char, c.char), b.frequency + c.frequency, b, c)
        tree = HuffmanNode(min(a.char, right.char), a.frequency + right.frequency, a, right)

        codes = create_codes(tree)

        self.assertEqual(codes[ord('a')], "0")
        self.assertEqual(codes[ord('b')], "10")
        self.assertEqual(codes[ord('c')], "11")

    def test_create_header_all_zeros(self) -> None:
        freqs = [0] * 256
        header = create_header(freqs)
        self.assertEqual(header, "")

    def test_create_header_single_char(self) -> None:
        freqs = [0] * 256
        freqs[ord('x')] = 7
        header = create_header(freqs)
        self.assertEqual(header, f"{ord('x')} 7")
    
    def test_create_header_multiple_chars_ordered(self) -> None:
        freqs = [0] * 256
        freqs[ord('b')] = 4
        freqs[ord('a')] = 2
        freqs[ord('d')] = 1

        header = create_header(freqs)

        self.assertEqual(header, f"{ord('a')} 2 {ord('b')} 4 {ord('d')} 1")
    
    def test_create_header_includes_newline_and_orders(self) -> None:
        freqs = [0] * 256
        freqs[ord('\n')] = 1
        freqs[ord('a')] = 1

        header = create_header(freqs)

        self.assertEqual(header, f"{ord(chr(10))} 1 {ord('a')} 1")

    def test_huffman_encode_empty(self) -> None:
        with io.StringIO("") as in_file, io.StringIO() as out_file:
            huffman_encode(in_file, out_file)
            out = out_file.getvalue()

        self.assertEqual(out, "\n")
    
    def test_huffman_encode_single_char(self) -> None:
        with io.StringIO("aaaa") as in_file, io.StringIO() as out_file:
            huffman_encode(in_file, out_file)
            out = out_file.getvalue()

        header, body = out.split("\n", 1)
        self.assertEqual(header, f"{ord('a')} 4")
        self.assertEqual(body, "0" * 4)
    
    def test_huffman_encode_two_chars_properties(self) -> None:
        text = "aaab"  # a=3, b=1
        with io.StringIO(text) as in_file, io.StringIO() as out_file:
            huffman_encode(in_file, out_file)
            out = out_file.getvalue()

        header, body = out.split("\n", 1)
        self.assertEqual(header, f"{ord('a')} 3 {ord('b')} 1")

        self.assertTrue(all(ch in "01" for ch in body))

        freqs = [0] * 256
        freqs[ord('a')] = 3
        freqs[ord('b')] = 1
        tree = build_huffman_tree(freqs)
        codes = create_codes(tree)

        expected_len = sum(freqs[i] * len(codes[i]) for i in range(256) if freqs[i] > 0)
        self.assertEqual(len(body), expected_len)
    
    def test_huffman_encode_includes_newline(self) -> None:
        text = "a\n"
        with io.StringIO(text) as in_file, io.StringIO() as out_file:
            huffman_encode(in_file, out_file)
            out = out_file.getvalue()

        header, body = out.split("\n", 1)
        self.assertEqual(header, "10 1 97 1")
        self.assertTrue(all(ch in "01" for ch in body))

        freqs = [0] * 256
        freqs[ord('a')] = 1
        freqs[ord('\n')] = 1
        tree = build_huffman_tree(freqs)
        codes = create_codes(tree)
        expected_len = sum(freqs[i] * len(codes[i]) for i in range(256) if freqs[i] > 0)
        self.assertEqual(len(body), expected_len)


if __name__ == "__main__":
    unittest.main()

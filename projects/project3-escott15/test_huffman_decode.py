import io 
import unittest 

from huffman_decode import huffman_decoding, parse_header


class Testdecode(unittest.TestCase):
    def test_huffman_decoding_empty(self) -> None:
        encoded = "\n"
        with io.StringIO(encoded) as in_file, io.StringIO() as out_file:
            returned = huffman_decoding(in_file, out_file)

            self.assertIs(returned, out_file)
            self.assertEqual(out_file.getvalue(), "")

    def test_huffman_decoding_single_char(self) -> None:
        original = "aaaaaa"
        encoded = "97 6\n000000"

        with io.StringIO(encoded) as encoded_in, io.StringIO() as decoded_out: 
            returned = huffman_decoding(encoded_in, decoded_out)
            
            self.assertIs(returned, decoded_out)
            self.assertEqual(decoded_out.getvalue(), original)

    def test_huffman_decoding_general_case(self) -> None:
        original = "aaaaabbc"
        encoded = "97 5 98 2 99 1\n11111010100"

        with io.StringIO(encoded) as encoded_in, io.StringIO() as decoded_out: 
            returned = huffman_decoding(encoded_in, decoded_out)

            self.assertIs(returned, decoded_out)
            self.assertEqual(decoded_out.getvalue(), original)

    def test_huffman_decoding_ignores_non_bits(self) -> None:
        original = "aaaaabbc"
        header = "97 5 98 2 99 1"
        body = "11111010100"

        corrupted = header + "\n" + body[:5] + "\n" + body[5:]

        with io.StringIO(corrupted) as encoded_in, io.StringIO() as decoded_out:
            returned = huffman_decoding(encoded_in, decoded_out)
            decoded_text = decoded_out.getvalue()

            self.assertIs(returned, decoded_out)
            self.assertEqual(decoded_text, original)

    def test_parse_header_empty(self) -> None:
        freqs = parse_header("")
        self.assertEqual(freqs, [0] * 256)

    def test_parse_header_whitespace(self) -> None:
        freqs = parse_header("   \t  ")
        self.assertEqual(freqs, [0] * 256)
    
    def test_parse_header_single_pair(self) -> None:
        freqs = parse_header("97 4")
        expected = [0] * 256
        expected[97] = 4
        self.assertEqual(freqs, expected)

    def test_parse_header_multiple_pairs(self) -> None:
        freqs = parse_header("98 2 97 3 10 1")
        expected = [0] * 256
        expected[98] = 2
        expected[97] = 3
        expected[10] = 1
        self.assertEqual(freqs, expected)

    
if __name__ == "__main__":
    unittest.main()
        
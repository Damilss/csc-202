from base_convert import convert
import unittest


class Tests(unittest.TestCase):
    def test_conbert_base02_1(self):
        self.assertEqual(convert(0, 2), "0")

    def test_convert_base16_1(self):
        self.assertEqual(convert(107, 16), "6B")

    def test_convert_base4_1(self):
        self.assertEqual(convert (8, 4), '20')

    def test_convert_base2_2(self):
        self.assertEqual(convert(13, 2), "1101")

    def test_convert_base8_1(self):
        self.assertEqual(convert(64, 8), "100")

    def test_convert_base10_1(self):
        self.assertEqual(convert(123, 10), "123")

    def test_convert_base16_2(self):
        self.assertEqual(convert(255, 16), "FF")


if __name__ == "__main__":
    unittest.main()

import unittest

from exp_eval import infix_to_postfix, postfix_eval


class Tests(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("1 2 +"), 3)

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("1 + 2"), "1 2 +")

    def test_postfix_eval_simple(self):
        self.assertAlmostEqual(postfix_eval("1 2 +"), 3)
    
    def test_postfix_eval_complex(self):
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ^ + 3 -"), 83)

    def test_postfix_eval_empty(self):
        with self.assertRaises(ValueError) as ve:
            postfix_eval("")
        self.assertEqual(str(ve.exception), "empty input")

    def test_postfix_eval_invalid_token(self):
        with self.assertRaises(ValueError) as ve:
            postfix_eval("2 a +")
        self.assertEqual(str(ve.exception), "invalid token")

    def test_postfix_eval_insufficient_operands(self):
        with self.assertRaises(ValueError) as ve:
            postfix_eval("2 +")
        self.assertEqual(str(ve.exception), "not enough operands")

    def test_postfix_eval_too_many_operands(self):
        with self.assertRaises(ValueError) as ve:
            postfix_eval("2 3 4 +")
        self.assertEqual(str(ve.exception), "too many operands")

    def test_infix_to_postfix_simple(self):
        self.assertEqual(infix_to_postfix("1 + 2"), "1 2 +")

    def test_infix_to_postfix_precedence(self):
        self.assertEqual(infix_to_postfix("1 + 2 * 3"), "1 2 3 * +")

    def test_infix_to_postfix_parentheses(self):
        self.assertEqual(infix_to_postfix("( 1 + 2 ) * 3"), "1 2 + 3 *")
    
    def test_infix_to_postfix_right_assoc(self):
        self.assertEqual(infix_to_postfix("2 ^ 3 ^ 2"), "2 3 2 ^ ^")

    def test_infix_to_postfix_floor_div(self):
        self.assertEqual(infix_to_postfix("8 // 3 + 1"), "8 3 // 1 +")

    def test_infix_to_postfix_handout_sample(self):
        self.assertEqual(
            infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"),
            "3 4 2 * 1 5 - 2 3 ^ ^ / +"
        )
    
    def test_infix_to_postfix_empty(self):
        with self.assertRaises(ValueError) as ve:
            infix_to_postfix("")
        self.assertEqual(str(ve.exception), "empty input")

    def test_infix_to_postfix_mismatched_paren_right(self):
        with self.assertRaises(ValueError) as ve:
            infix_to_postfix("1 + 2 )")
        self.assertEqual(str(ve.exception), "mismatched parenthesis")

    def test_infix_to_postfix_mismatched_paren_left(self):
        with self.assertRaises(ValueError) as cm:
            infix_to_postfix("( 1 + 2")
        self.assertEqual(str(cm.exception), "mismatched parenthesis")
    




if __name__ == "__main__":
    unittest.main()

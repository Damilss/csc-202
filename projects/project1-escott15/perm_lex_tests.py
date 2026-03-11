import unittest

from perm_lex import perm_gen_lex

class Tests(unittest.TestCase):
    def test_perm_gen_lex_empty(self):
        self.assertEqual(perm_gen_lex(""), [""])
    def test_perm_gen_lex(self):
        self.assertEqual(
                perm_gen_lex("abc"),
                ["abc","acb","bac","bca","cab","cba"]
            )
    def test_perm_gen_lex_two_chars(self):
        self.assertEqual(
            perm_gen_lex("ab"),
            ["ab", "ba"]
        )
    def test_perm_gen_lex_four_chars(self):
        self.assertEqual(
            perm_gen_lex("abcd"),
            [
                "abcd", "abdc", "acbd", "acdb",
                "adbc", "adcb", "bacd", "badc",
                "bcad", "bcda", "bdac", "bdca",
                "cabd", "cadb", "cbad", "cbda",
                "cdab", "cdba", "dabc", "dacb",
                "dbac", "dbca", "dcab", "dcba"
            ]
        )
    def test_perm_gen_lex_five_chars(self):
        self.assertEqual(
            perm_gen_lex("abcde"),
            [
            "abcde","abced","abdce","abdec","abecd","abedc",
            "acbde","acbed","acdbe","acdeb","acebd","acedb",
            "adbce","adbec","adcbe","adceb","adebc","adecb",
            "aebcd","aebdc","aecbd","aecdb","aedbc","aedcb",

            "bacde","baced","badce","badec","baecd","baedc",
            "bcade","bcaed","bcdae","bcdea","bcead","bceda",
            "bdace","bdaec","bdcae","bdcea","bdeac","bdeca",
            "beacd","beadc","becad","becda","bedac","bedca",

            "cabde","cabed","cadbe","cadeb","caebd","caedb",
            "cbade","cbaed","cbdae","cbdea","cbead","cbeda",
            "cdabe","cdaeb","cdbae","cdbea","cdeab","cdeba",
            "ceabd","ceadb","cebad","cebda","cedab","cedba",

            "dabce","dabec","dacbe","daceb","daebc","daecb",
            "dbace","dbaec","dbcae","dbcea","dbeac","dbeca",
            "dcabe","dcaeb","dcbae","dcbea","dceab","dceba",
            "deabc","deacb","debac","debca","decab","decba",

            "eabcd","eabdc","eacbd","eacdb","eadbc","eadcb",
            "ebacd","ebadc","ebcad","ebcda","ebdac","ebdca",
            "ecabd","ecadb","ecbad","ecbda","ecdab","ecdba",
            "edabc","edacb","edbac","edbca","edcab","edcba"
        ]
    )


if __name__ == "__main__":
    unittest.main()
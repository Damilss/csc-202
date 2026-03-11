import io
import unittest

from concordance import (
    build_concordance_table,
    build_stop_words_table,
    write_concordance_table,
)


class Tests(unittest.TestCase):
    def test_stop_words_small(self) -> None:
        with io.StringIO("a\nan\nthe\n") as small_stop_words_file:
            stop_words = build_stop_words_table(small_stop_words_file)

        self.assertEqual(stop_words, {"a", "an", "the"})

    def test_build_concordance_small(self) -> None:
        with io.StringIO("a\nan\nthe\n") as small_stop_words_file:
            stop_words = build_stop_words_table(small_stop_words_file)

        with io.StringIO("this is a file\n") as small_file:
            concordance_table = build_concordance_table(small_file, stop_words)

        self.assertEqual(concordance_table, {"this": [1], "is": [1], "file": [1]})

    def test_file1(self) -> None:
        with open("stop_words.txt", encoding="utf8") as stop_words_file:
            stop_words = build_stop_words_table(stop_words_file)

        with open("file1.txt", encoding="utf8") as in_file:
            concordance_table = build_concordance_table(in_file, stop_words)

        with io.StringIO() as out_file:
            write_concordance_table(out_file, concordance_table)
            result = out_file.getvalue()

        with open("file1_sol.txt", encoding="utf8") as correct_out:
            self.assertEqual(result, correct_out.read())

    def test_build_concordance_appends_new_line_num(self) -> None:

        stop_words: set[str] = set()

        with io.StringIO("hello\nhello\n") as small_file:
            concordance_table = build_concordance_table(small_file, stop_words)

        self.assertEqual(concordance_table, {"hello": [1, 2]})


if __name__ == "__main__":
    unittest.main()

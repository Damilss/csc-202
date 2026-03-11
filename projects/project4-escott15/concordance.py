from typing import TextIO


def build_stop_words_table(stop_words_file: TextIO) -> set[str]:
    """Return a hash table whose keys are the stop words.

    This will read the stop words from the file and add them to the stop
    words table.
    """
    stop = set()
    for line in stop_words_file:
        w = line.strip().lower()
        if w != "":
            stop.add(w)
    return stop


def build_concordance_table(file: TextIO, stop_table: set[str]) -> dict[str, list[int]]:
    """Return the concordance table for the given file.

    This will read the given file and build a concordance table
    containing all valid words in the file.
    """
    concord: dict[str, list[int]] = {}

    # constant pythonic variable name, but ran error so is lowercase
    punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    trans = str.maketrans(punct, " " * len(punct))

    for line_num, line in enumerate(file, start=1):
        line = line.lower()
        line = line.replace("'", "")
        line = line.translate(trans)
        tokens = line.split()

        for tok in tokens:
            if tok.isalpha() and tok not in stop_table:
                if tok not in concord:
                    concord[tok] = [line_num]
                else:
                    if concord[tok][-1] != line_num:
                        concord[tok].append(line_num)

    return concord


def write_concordance_table(file: TextIO, concordance: dict[str, list[int]]) -> None:
    """Write the concordance table to the given file.

    This will sort the strings in the concordance table alphabetically
    and write them to the given file along with the line numbers on
    which they occurred.
    """

    for word in sorted(concordance):
        line_nums = concordance[word]
        nums_text = " ".join(str(n) for n in line_nums)
        file.write(f"{word}: {nums_text}\n")

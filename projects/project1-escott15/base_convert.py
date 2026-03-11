LOOKUP_NUM = (
    ('A', '10'),
    ('B', '11'),
    ('C', '12'),
    ('D', '13'),
    ('E', '14'),
    ('F', '15')
)


def convert(num: int, base: int) -> str:
    """Docstring for convert: Purpose of this function is to convert a
    base 10 number into base n, which n is the given argument. All the
    way up to base 16.

    :param n: Description
    :type n: int
    :return: Description
    :rtype: str"""

    """READ ONLY USAGE"""
    global LOOKUP_NUM

    if num < base:
        result = str(num)
        if num > 9:
            for _alpha, LOOKUP in LOOKUP_NUM:
                if result == LOOKUP:
                    result = _alpha
        return result


    _subnum = divmod(num, base)
    return convert(_subnum[0], base) + convert(_subnum[1], base)

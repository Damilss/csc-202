def perm_gen_lex(_string: str,) -> list[str]:
    """Docstring for perm_gen_lex: takes unique single 
    str argument and generates all of the permutations of that string in 
    lexiographic order 
    
    :param _string: Description
    :type _string: str
    :return: Description
    :rtype: list[str]"""

    if len(_string) <=1: 
       return [_string] 
    
    result = []
    for i, char in enumerate(_string):
        _substr = _string[:i] + _string[i+1:]
        for permutation in perm_gen_lex(_substr):
            result.append(char+permutation)


    return result 

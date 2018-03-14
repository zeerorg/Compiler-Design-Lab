import string
from toolz import compose
from functools import partial, reduce
import re

def main():
    file_name = input("Enter file name: ")
    with open(file_name) as file:
        program = file.read()

    identifiers, operators, literals, keywords = get_tokens(program)

    # print tokens
    compose(print, "Identifiers: \t {}".format, '\t '.join, partial(map, str)) (identifiers)
    compose(print, "Operators: \t {}".format, '\t '.join, partial(map, str)) (operators)
    compose(print, "Literals: \t {}".format, '\t '.join, partial(map, str)) (literals)
    compose(print, "Keywords: \t {}".format, '\t '.join, partial(map, str)) (keywords)


def get_tokens(program: str, delimiter=set([" ", "\n"])):
    """
    extract tokens from program
    """
    identifiers = get_lexeme(program, delimiter, is_identifier)
    operators = get_lexeme(program, delimiter, is_operator)
    literals = get_lexeme(program, delimiter, is_literal)
    keywords = get_lexeme(program, delimiter, is_keyword)

    return [
        identifiers,
        operators,
        literals,
        keywords
    ]


def get_lexeme(program: str, delimiters: set, check_func) -> list:
    word = []
    ans = set()
    for char in program:
        if char not in delimiters:
            word.append(char)
        else:
            if check_func(''.join(word)):
                ans.add(''.join(word))
            word = []
    if check_func(''.join(word)):
        ans.add(''.join(word))
    return ans


def is_identifier(word: str) -> bool:
    """
    Check if a word is identifier or not
    >>> is_identifier("lorem")
    True
    >>> is_identifier("6lorem")
    False
    >>> is_identifier("Lor_m3")
    True
    >>> is_identifier("Lor+em")
    False
    """
    reg = r'^[a-zA-Z]\w*$'
    match = re.fullmatch(reg, word)
    return ( not not match ) and ( not is_keyword(word) )

def is_operator(word: str) -> bool:
    if word in "+ * / - = == <= >= > < !=".split(" "):
        return True
    return False


def is_literal(word: str) -> bool:
    """
    Check if word is literal
    >>> is_literal("3223")
    True
    >>> is_literal("\\" rri sh\\"")
    True
    >>> is_literal("lorem")
    False
    >>> is_literal("Lor_m3")
    False
    """
    reg1 = r'^\"[^\"]*\"$'
    reg2 = r'^\d+$'
    match1 = re.fullmatch(reg1, word)
    match2 = re.fullmatch(reg2, word)
    return ( not not match1 ) or ( not not match2 )

def is_keyword(word: str) -> bool:
    if word in "if then endif".split(" "):
        return True
    return False

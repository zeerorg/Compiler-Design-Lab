from algo_lib import find_tokens

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

if __name__ == '__main__':
    main()

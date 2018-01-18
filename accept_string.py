from core_lib import nfa as nfa_lib
from core_lib import dfa as dfa_lib

from algo_lib import nfa_help
from algo_lib import dfa_help
from algo_lib import convert


def main():
    print("Enter NFA:\n")

    nfa = nfa_help.get_nfa()
    dfa = convert.nfa_to_dfa(nfa)

    print("DFA is\n")
    print(dfa)

    current_string = " "
    while current_string != "-1":
        print("Enter string to check (-1) to quit:")
        current_string = input()

        if current_string == "-1":
            break

        flag = nfa_help.check_string_nfa(current_string, nfa)
        if flag:
            print("This string is accepted by NFA")
        else:
            print("This string is not accepted by NFA")

        flag = dfa_help.check_string_dfa(current_string, dfa)
        if flag:
            print("This string is accepted by DFA")
        else:
            print("This string is not accepted by DFA")

        print()
    pass

if __name__ == '__main__':
    main()

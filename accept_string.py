from core_lib import nfa as nfa_lib
from core_lib import dfa as dfa_lib

from algo_lib import nfa_help
from algo_lib import dfa_help
from algo_lib import convert

def check_string_nfa(string: str, nfa: nfa_lib.NFA) -> bool:
    current_states = set([nfa.init_state])
    for x in string:
        if len(current_states) == 0:
            return False
        
        next_states = set()
        for state in current_states:
            next_states.update(nfa[state][x])

        current_states = set(next_states)

    for x in nfa.final_states:
        if x in current_states:
            return True

    return False


def check_string_dfa(string: str, dfa: dfa_lib.DFA) -> bool:
    current_state = dfa.init_state
    for x in string:
        next_state = dfa[current_state][x]
        current_state = next_state

    if current_state in dfa.final_states:
        return True

    return False

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

        flag = check_string_nfa(current_string, nfa)
        if flag:
            print("This string is accepted by NFA")
        else:
            print("This string is not accepted by NFA")

        flag = check_string_dfa(current_string, dfa)
        if flag:
            print("This string is accepted by DFA")
        else:
            print("This string is not accepted by DFA")

        print()
    pass

if __name__ == '__main__':
    main()

from core_lib import nfa
from core_lib import dfa
from algo_lib import nfa_help
from algo_lib import convert

def main():
    my_nfa = nfa_help.get_nfa()
    my_dfa = convert.nfa_to_dfa(my_nfa)
    print("\n")
    print(str(my_dfa))

if __name__ == '__main__':
    main()


from core_lib import nfa as nfa_lib

def get_nfa() -> nfa_lib.NFA:
    states = 0
    current_state = 0
    print(" '-1' for no next state\n")
    print("STATE\t\tINPUT\t\tNext State")
    nfa = {}
    while current_state <= states:
        nfa[current_state] = None
        node = {}
        for y in ['a', 'b']:
            print(" {}\t\t  {} \t\t".format(current_state, y), end='')
            next_states = set([int(x) for x in input().split(" ")])
            states = max(states, max(next_states))
            next_states.difference_update(set([-1]))
            node[y] = set(next_states)
        
        nfa[current_state] = nfa_lib.NFA_Node(node['a'], node['b'])

        current_state += 1

    final_states = [int(x) for x in input("Enter final states: ").split(" ")]
    # initial_state = int(input("Enter initial state: "))
    init_state = 0
    nfa = nfa_lib.NFA(init_state, final_states, nfa)
    return nfa

def dict_to_nfa(raw_nfa: dict, init_state: int, final_states: list):
    nfa_dict = {}

    for x in raw_nfa:
        nfa_dict[x] = nfa_lib.NFA_Node(set(raw_nfa[x]['a']), set(raw_nfa[x]['b']))
        
    return nfa_lib.NFA(init_state, final_states, nfa_dict)


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

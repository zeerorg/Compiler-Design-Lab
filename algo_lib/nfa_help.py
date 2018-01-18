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

    final_state = int(input("Enter (single) final state: "))
    # initial_state = int(input("Enter initial state: "))
    init_state = 0
    nfa = nfa_lib.NFA(init_state, final_state, nfa)
    return nfa

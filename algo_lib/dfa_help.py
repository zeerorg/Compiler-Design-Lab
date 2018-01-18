from core_lib import dfa as dfa_lib

def get_dfa() -> dfa_lib.DFA:
    states = 0
    current_state = 0
    print("STATE\t\tINPUT\t\tNext State")
    dfa = {}
    while current_state <= states:
        dfa[current_state] = None
        node = {}
        for y in ['a', 'b']:
            print(" {}\t\t  {} \t\t".format(current_state, y), end='')
            next_states = set([int(x) for x in input().split(" ")])
            states = max(states, max(next_states))
            next_states.difference_update(set([-1]))
            node[y] = set(next_states)
        
        dfa[current_state] = nfa_lib.NFA_Node(node['a'], node['b'])

        current_state += 1

    final_state = int(input("Enter final states: "))
    final_states = [int(x) for x in final_state.splie(" ")]
    # initial_state = int(input("Enter initial state: "))
    init_state = 0
    dfa = dfa_lib.DFA(init_state, final_states, dfa)
    return dfa


def check_string_dfa(string: str, dfa: dfa_lib.DFA) -> bool:
    current_state = dfa.init_state
    for x in string:
        next_state = dfa[current_state][x]
        current_state = next_state

    if current_state in dfa.final_states:
        return True

    return False

from lib import nfa
from lib import dfa

def nfa_to_dfa(my_nfa: nfa.NFA):
    # dfa = {}
    # dfa['initial_state'] = frozenset(nfa.init_state)
    # dfa = form_dfa(set([nfa.init_state]), nfa, dfa)
    map_dfa_to_nfa = []
    my_dfa_dict = {}
    to_visit = [frozenset([my_nfa.init_state])]
    visited = []
    final_states = []
    while len(to_visit) > 0:
        current_states = to_visit.pop(0)
        if current_states in visited:
            continue
        if current_states not in map_dfa_to_nfa:
            map_dfa_to_nfa.append(current_states)
        state_a = set()
        state_b = set()
        for state in current_states:
            state_a.update(my_nfa[state].a)
            state_b.update(my_nfa[state].b)
            
        state_a = frozenset(state_a)
        state_b = frozenset(state_b)

        if state_a not in map_dfa_to_nfa:
            map_dfa_to_nfa.append(state_a)
        if state_b not in map_dfa_to_nfa:
            map_dfa_to_nfa.append(state_b)

        curr_ind = map_dfa_to_nfa.index(current_states)
        a_ind = map_dfa_to_nfa.index(state_a)
        b_ind = map_dfa_to_nfa.index(state_b)

        my_dfa_dict[curr_ind] = dfa.DFA_Node(a_ind, b_ind)
        if my_nfa.final_state in current_states and curr_ind not in final_states:
            final_states.append(curr_ind)

    my_dfa = dfa.DFA(my_nfa.init_state, final_states, my_dfa_dict)
    return my_dfa

# def form_dfa(state_: set, nfa: dict, dfa_):
#     dfa = dict(dfa_)
#     state = frozenset(state_)
#     if state in dfa:
#         return dfa

#     a, b = set(), set()
#     for x in state_:
#         for y in nfa[x]['a']:
#             a.union(get_abs_state(y, nfa))

#         for y in nfa[x]['b']:
#             b.union(get_abs_state(y, nfa))

#     print(state)

#     dfa[state] = {
#         'a': frozenset(a),
#         'b': frozenset(b)
#     }
#     dfa = form_dfa(a, nfa, dfa)
#     dfa = form_dfa(b, nfa, dfa)
#     return dfa

def main():
    my_nfa = nfa.get_nfa()
    print(str(my_nfa))
    my_dfa = nfa_to_dfa(my_nfa)
    print(str(my_dfa))
    # dfa = nfa_to_dfa(nfa)
    # print_dfa(dfa)
    pass

if __name__ == '__main__':
    main()


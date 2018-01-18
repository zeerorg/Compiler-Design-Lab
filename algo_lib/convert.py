from core_lib import nfa
from core_lib import dfa

def nfa_to_dfa(my_nfa: nfa.NFA) -> dfa.DFA:
    # is a list of set of states of nfa which map to dfa used to generate intermediate dfa
    map_dfa_to_nfa = []
    # the dfa dictionary
    my_dfa_dict = {}
    # contains states to be visited
    to_visit = [frozenset([my_nfa.init_state])]
    # contains states which have been visited hence no need to visit
    visited = []
    final_states = []
    while len(to_visit) > 0:
        current_states = to_visit.pop(0)
        # if state is visited don't visit
        if current_states in visited:
            continue
        if current_states not in map_dfa_to_nfa:
            map_dfa_to_nfa.append(current_states)

        # the next states of current state
        state_a = set()
        state_b = set()

        # updating state
        for state in current_states:
            state_a.update(my_nfa[state].a)
            state_b.update(my_nfa[state].b)
            
        state_a = frozenset(state_a)
        state_b = frozenset(state_b)

        # visit next
        to_visit.append(state_a)
        to_visit.append(state_b)

        # for intermediate dfa -> normal dfa
        if state_a not in map_dfa_to_nfa:
            map_dfa_to_nfa.append(state_a)
        if state_b not in map_dfa_to_nfa:
            map_dfa_to_nfa.append(state_b)

        # get normal dfa states (from index of intermediate states)
        curr_ind = map_dfa_to_nfa.index(current_states)
        a_ind = map_dfa_to_nfa.index(state_a)
        b_ind = map_dfa_to_nfa.index(state_b)

        my_dfa_dict[curr_ind] = dfa.DFA_Node(a_ind, b_ind)
        if my_nfa.final_state in current_states and curr_ind not in final_states:
            final_states.append(curr_ind)

        visited.append(current_states)

    my_dfa = dfa.DFA(my_nfa.init_state, final_states, my_dfa_dict)
    print("\nIntermediate DFA")
    print(my_dfa.get_raw_dfa_str(map_dfa_to_nfa))
    return my_dfa

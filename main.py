from lib import nfa

def nfa_to_dfa(nfa: nfa.NFA):
    dfa = {}
    dfa['initial_state'] = frozenset(nfa.init_state)
    dfa = form_dfa(set([nfa.init_state]), nfa, dfa)
    return dfa


def get_abs_state(state: int, nfa: nfa.NFA):
    final_state = [state]
    for x in final_state:
        for y in nfa[x].E:
            if y not in final_state:
                final_state.append(y)
    return final_state


def form_dfa(state_: set, nfa: dict, dfa_):
    dfa = dict(dfa_)
    state = frozenset(state_)
    if state in dfa:
        return dfa

    a, b = set(), set()
    for x in state_:
        for y in nfa[x]['a']:
            a.union(get_abs_state(y, nfa))

        for y in nfa[x]['b']:
            b.union(get_abs_state(y, nfa))

    print(state)

    dfa[state] = {
        'a': frozenset(a),
        'b': frozenset(b)
    }
    dfa = form_dfa(a, nfa, dfa)
    dfa = form_dfa(b, nfa, dfa)
    return dfa


def print_dfa(dfa):
    print(dfa)

def main():
    my_nfa = nfa.get_nfa()
    print(str(my_nfa))
    # dfa = nfa_to_dfa(nfa)
    # print_dfa(dfa)
    pass

if __name__ == '__main__':
    main()


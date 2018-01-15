from lib import nfa

def print_nfa(nfa):
    max_state = max(nfa.keys())
    print("STATE\t\tINPUT\t\tNext State")
    for x in range(max_state):
        for y in nfa[x]:
            if x == nfa['initial_state']:
                print("-", end='')
            if x == nfa['final_state']:
                print("+", end='')
            print(" {}\t\t {}\t\t {}".format(x, y, nfa[x][y]))


def nfa_to_dfa(nfa: nfa.NFA):
    dfa = {}
    dfa['initial_state'] = frozenset(nfa.init_state)
    dfa = form_dfa(set([nfa.init_state]), nfa, dfa)
    return dfa


def get_abs_state(state, nfa):
    final_state = set([state])
    for x in final_state:
        final_state.union(nfa[x]['E'])
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
    # print("STATE\t\tINPUT\t\tNext State")
    # for x in dfa:
    #     for y in dfa[x]:
    #         print("{}\t\t{}\t\t{}".format(x, y, dfa[x][y]))
    print(dfa)

def main():
    nfa = nfa.get_nfa()
    dfa = nfa_to_dfa(nfa)
    print_dfa(dfa)
    pass

if __name__ == '__main__':
    main()


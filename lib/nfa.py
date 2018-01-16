class NFA_Node:

    def __init__(self, a: set, b: set):
        self.a = a
        self.b = b

    def as_dict():
        return {
            'a': self.a,
            'b': self.b,
        }

    def __iter__(self):
        yield ('a', self.a)
        yield ('b', self.b)

    def __str__(self):
        return ' '.join(self.__iter__())

class NFA:
    """
    Class which implements nfa and a dict from 

    self.graph = {
        0: NFA_Node(),
        2: NFA_Node()
    }
    """

    def __init__(self, init_state: int, final_state: int, graph: dict):

        self.init_state = init_state
        self.final_state = final_state
        self.graph = graph
    
    def __getitem__(self, key) -> NFA_Node:
        return self.graph[key]

    def __setitem__(self, name, val):
        self.graph[name] = val

    def get(self, key):
        return self.graph.get(key, set())

    def __str__(self):
        final_str = ["STATE\t\tINPUT\t\tNext State"]
        to_check = [self.init_state]
        checked = []
        while len(to_check) > 0:
            state = to_check.pop(0)
            if state in checked:
                continue
            checked.append(state)
            for inp, next_states in self.__getitem__(state):
                for node in next_states:
                    to_check.append(node)
                final_str.append(" {}\t\t {}\t\t {}".format(state, inp, next_states))

        return '\n'.join(final_str)

    def __repr__(self):
        return self.__str__()

def get_nfa() -> NFA:
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
        
        nfa[current_state] = NFA_Node(node['a'], node['b'])

        current_state += 1

    final_state = int(input("Enter (single) final state: "))
    # initial_state = int(input("Enter initial state: "))
    init_state = 0
    nfa = NFA(init_state, final_state, nfa)
    return nfa

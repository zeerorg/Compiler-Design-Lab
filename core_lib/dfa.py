class DFA_Node:
    def __init__(self, a: int, b: int):
        
        self.a = a
        self.b = b

    def __iter__(self):
        yield ('a', self.a)
        yield ('b', self.b)

    def as_dict():
        return {
            'a': self.a,
            'b': self.b
        }

    def __str__(self):
        return "a: {}, b: {}".format(self.a, self.b)

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, k):
        return self.__getattribute__(k)

class DFA:
    """
    Class which implements dfa and a dict from 

    self.graph = {
        0: DFA_Node,
        2: DFA_Node
    }
    """

    def __init__(self, init_state: int, final_states: list, graph: dict):

        self.init_state = init_state
        self.final_states = final_states
        self.graph = graph
    
    def __getitem__(self, key) -> DFA_Node:
        return self.graph[key]

    def __setitem__(self, name, val):
        self.graph[name] = val

    def __str__(self):
        final_str = ["STATE\t\tINPUT\t\tNext State"]
        to_check = [self.init_state]
        checked = []
        while len(to_check) > 0:
            state = to_check.pop(0)
            if state in checked:
                continue
            checked.append(state)
            for inp, next_state in self.__getitem__(state):
                to_check.append(next_state)
                string = []
                if state in self.final_states:
                    string.append("+")
                else:
                    string.append(" ")

                if state == self.init_state:
                    if string[-1] == " ":
                        string.pop()
                    string.append("-")
                string.append("{}\t\t {}\t\t {}".format(state, inp, next_state))
                final_str.append(''.join(string))

        return '\n'.join(final_str)

    def get(self, key):
        return self.graph.get(key, set())

    def get_raw_dfa_str(self, mapping: list):
        final_str = ["STATE\t\tINPUT\t\tNext State"]
        to_check = [self.init_state]
        checked = []
        while len(to_check) > 0:
            state = to_check.pop(0)
            if state in checked:
                continue
            checked.append(state)
            for inp, next_state in self.__getitem__(state):
                to_check.append(next_state)
                string = []
                if state in self.final_states:
                    string.append("+")
                else:
                    string.append(" ")

                if state == self.init_state:
                    if string[-1] == " ":
                        string.pop()
                    string.append("-")
                string.append("{}\t\t {}\t\t {}".format(list(mapping[state]), inp, list(mapping[next_state])))
                final_str.append(''.join(string))

        return '\n'.join(final_str)

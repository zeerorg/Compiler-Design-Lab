class DFA:
    """
    Class which implements nfa and a dict from 

    self.graph = {
        0: DFA_Node,
        2: DFA_Node
    }
    """

    def __init__(self, init_state: int, final_state: int, graph: dict):

        self.init_state = init_state
        self.final_state = final_state
        self.graph = graph
    
    def __getitem__(self, key) -> Node:
        return self.graph[key]

    def __setitem__(self, name, val):
        self.graph[name] = val

    def get(self, key):
        return self.graph.get(key, set())


class DFA_Node:

    def __init__(self, a: int, b: int):
        
        self.a = a
        self.b = b

    def __iter__(self):
        yield self.a
        yield self.b

    def as_dict():
        return {
            'a': self.a,
            'b': self.b
        }
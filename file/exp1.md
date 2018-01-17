<h1 style="text-align: center;"> Practical 1</h1>

## AIM
Write a program to convert non deterministic finite automata to deterministic finite automata.

## Description of aim and related theory
Deterministic finite automata is a finite-state machine that accepts and rejects strings of symbols and only produces a unique computation (or run) of the automaton for each input string. Deterministic refers to the uniqueness of the computation. 
A deterministic finite automaton M is a 5-tuple, consisting of
* a finite set of states 
* a finite set of input symbols called the alphabet 
* a transition function 
* an initial or start state 
* a set of accept states

A non-deterministic finite automata is type of finite automata where there may be more than one path for a unique string from start state to end state, in contrast to deterministic finite automata where there is only one path.

## Algorithm
Suppose there is an NFA N < Q, ∑, q0, δ, F > which recognizes a language L. Then the DFA D < Q’, ∑, q0, δ’, F’ > can be constructed for language L as:
1. Initially Q’ = ɸ.
2. Add q0 to Q’.
3. For each state in Q’, find the possible set of states for each input symbol using transition function of NFA. If this set of states is not in Q’, add it to Q’.
4. Final state of DFA will be all states with contain F (final states of NFA)

## Code
#### nfa.py
```python
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
```

#### dfa.py

```python
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
```

#### nfatodfa.py
```python
from lib import nfa
from lib import dfa

def nfa_to_dfa(my_nfa: nfa.NFA):
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

def main():
    my_nfa = nfa.get_nfa()
    my_dfa = nfa_to_dfa(my_nfa)
    print("\n")
    print(str(my_dfa))

if __name__ == '__main__':
    main()

```
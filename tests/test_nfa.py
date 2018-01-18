from algo_lib import nfa_help
from algo_lib import dfa_help
from algo_lib import convert

nfa_dict = {
    0: {
        'a': [1],
        'b': [0, 2]
    },
    1: {
        'a': [2,3],
        'b': [1,3]
    },
    2: {
        'a': [2],
        'b': [3]
    },
    3: {
        'a': [3],
        'b': [1]
    }
}

init_state = 0
final_state = 0

nfa = nfa_help.dict_to_nfa(nfa_dict, init_state, [final_state])
dfa = convert.nfa_to_dfa(nfa)

strings = []
# contains fixtures for all tests
import pytest

from algo_lib import nfa_help
from algo_lib import dfa_help
from algo_lib import convert

def resource_nfa():
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
    final_states = [0, 1]
    return nfa_help.dict_to_nfa(nfa_dict, init_state, final_states)

@pytest.fixture
def nfa():
    return resource_nfa()

@pytest.fixture
def dfa():
    return convert.nfa_to_dfa(resource_nfa())
import pytest
from unittest import mock

from algo_lib import nfa_help
from algo_lib import dfa_help
from core_lib import nfa as nfa_lib
from core_lib import dfa as dfa_lib

def absorb_args(func):
    def wrapper(*args, **kwargs):
        return func()
    return wrapper


def test_nfa_inp(nfa: nfa_lib.NFA):
    inp_statements = [
        "1",
        "0 2",
        "2 3",
        "1 3",
        "2",
        "3",
        "3",
        "1",
        "0 1"
    ]
    with mock.patch('builtins.input', side_effect=absorb_args(inp_statements.__iter__().__next__)):
        inp_nfa = nfa_help.get_nfa()
        assert inp_nfa.final_states == nfa.final_states
        assert inp_nfa[0]['a'] == nfa[0]['a']
        assert inp_nfa.init_state == nfa.init_state

def test_dfa_inp(dfa: dfa_lib.DFA):
    inp_statements = [ str(x) for x in [1,2,3,4,5,6,3,4,3,4,3,4,7,8,3,4,7,8] ]
    inp_statements.append(' '.join([ str(x) for x in [0, 1, 2, 4, 5, 6, 7, 8] ]))
    with mock.patch('builtins.input', side_effect=absorb_args(inp_statements.__iter__().__next__)):
        inp_dfa = dfa_help.get_dfa()
        assert inp_dfa.final_states == dfa.final_states

    pass

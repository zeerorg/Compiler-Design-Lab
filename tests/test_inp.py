import pytest
from unittest import mock

from algo_lib import nfa_help
from algo_lib import dfa_help
from core_lib import nfa as nfa_lib

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

import pytest

from algo_lib import nfa_help
from algo_lib import dfa_help

from core_lib import nfa as nfa_lib
from core_lib import dfa as dfa_lib

def test_nfa_string_accept(nfa):
    string = "bb"
    assert nfa_help.check_string_nfa(string, nfa) == True

def test_nfa_string_decline(nfa):
    string = "aa"
    assert nfa_help.check_string_nfa(string, nfa) == False

def test_dfa_string_decline(dfa):
    string = "baaa"
    assert dfa_help.check_string_dfa(string, dfa) == False

def test_dfa_string_accept(dfa):
    string = "bbbbbbbb"
    assert dfa_help.check_string_dfa(string, dfa) == True

def test_nfa_and_dfa_equal(nfa, dfa):
    import random
    options = "ab"
    length = 7
    times = 10
    for x in range(10):
        string = random.choices(options, k=length)
        assert nfa_help.check_string_nfa(string, nfa) == dfa_help.check_string_dfa(string, dfa)

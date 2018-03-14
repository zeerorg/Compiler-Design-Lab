import pytest

from algo_lib import find_tokens

def test_tokens():
    ids, ops, lits, keys = find_tokens.get_tokens('hello = 23\nif hello\nthen "good"\nendif')
    assert 'hello' in ids and ids.__len__() == 1
    assert '=' in ops and ops.__len__() == 1
    assert '"good"' in lits
    assert '23' in lits and lits.__len__() == 2
    assert set('if then endif'.split()) == keys
    # assert tokens == [['hello'], ['='], ['"good"', '23'], ['if', 'then', 'endif']]
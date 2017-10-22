import pytest

NUMBERS = [
    (39, 3), (4, 0), (25, 2), (999, 4), 
    (1111111, 1), (34985692, 2), (8436923053, 1)
]

@pytest.mark.parametrize('n, result', NUMBERS)
def test_persistence(n, result):
    from persistence import persistence
    assert(persistence(n) == result)
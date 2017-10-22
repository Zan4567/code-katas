import pytest

NUMBERS = [
    (5, 8, 1080), (7, 10, 23100), (10, 15, 1663200)
]

@pytest.mark.parametrize('n, m, result', NUMBERS)
def test_sum_multi_triangnum(n, m, result):
    from sum_mult_triangnum import sum_mult_triangnum
    assert(sum_mult_triangnum(n, m) == result)
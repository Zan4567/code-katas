import pytest

NUMBERS = [
    ([], 0), ([3], 0), ([3, 5], 0), ([6, 2, 1, 8, 10], 16), ([6, 0, 1, 10, 10], 17), 
    ([-6, -20, -1, -10, -12], -28)
]

@pytest.mark.parametrize('arr, result', NUMBERS)
def test_sum_array(arr, result):
    from sum_without_highest_and_lowest_number import sum_array
    assert(sum_array(arr) == result)
import pytest

NUMBERS = [
    ([5, 8, 12, 18, 22], 13), ([7, 15, 12, 18, 22], 19), ([25, 42, 12, 18, 22], 30),
    ([5, 10, 5, 12, 14], 10), ([7, -15, 12, 8, 11], 15), ([-102, -45, 0, 1234, -305], 1234)
]

@pytest.mark.parametrize('numbers, result', NUMBERS)
def test_sum_two_smallest_numbers(numbers, result):
    from sum_two_smallest_numbers import sum_two_smallest_numbers
    assert(sum_two_smallest_numbers(numbers) == result)
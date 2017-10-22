'''
I was able to get it working, but it times out on the official submission.
solutions are locked for kata "far above your rank"'''

def sum_mult_triangnum(n, m):
    '''get the sum of multiples of triangle numbers'''
    triangle_numbers = []
    for i in range(1, n + 1):
        triangle_numbers.append(i * (i + 1) // 2)

    least_common_multiple = get_least_common_multiple(triangle_numbers)
    sum_of_multiples = 0
    for i in range(1, m + 1):
        sum_of_multiples += least_common_multiple * i

    return sum_of_multiples

def get_least_common_multiple(numbers):
    '''return the least common multiple of a list of integers'''
    total_factors = set(numbers)

    for number in numbers:
        factors = get_factors(number)
        total_factors.update(factors)

    i = max(total_factors)
    while True:
        if(number_is_common_multiple(i, total_factors)): return i
        i += 1

def get_factors(number):
    '''return the factors of a number, excluding 1 and itself'''
    factors = []
    for i in range(2, number // 2 + 1):
        if number % i is 0: factors.append(i)
    return factors

def number_is_common_multiple(number, factor_set):
    '''determine if a number is a common factor of the elements in a set'''
    for factor in factor_set:
        if number % factor != 0: return False

    return True
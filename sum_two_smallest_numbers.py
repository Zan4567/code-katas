'''
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
'''

def sum_two_smallest_numbers(numbers):
    '''return the sum of the two smallest positive integers in a list'''
    sorted_numbers = sorted(numbers)
    index = 0
    while(sorted_numbers[index] <= 0): index += 1

    total = 0
    for i in range(2):
        if(index >= len(sorted_numbers)): return total
        total += sorted_numbers[index]
        index += 1
    return total

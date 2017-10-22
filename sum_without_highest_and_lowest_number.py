'''
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
'''

def sum_array(arr):
    '''return the sum of the elements of a list, except the largest and smallest values'''
    if arr is None: return 0
    if len(arr) <= 2: return 0

    sorted_list = sorted(arr)[1:-1]

    return sum(sorted_list)
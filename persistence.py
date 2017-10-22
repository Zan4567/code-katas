'''
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
'''

def persistence(n):
    '''return the persistence of the given number: the number of times needed 
    to multiply the digits of the number together to get a 1-digit number'''
    if n < 10: return 0

    digits = []

    while n:
        digits.append(n % 10)
        n = n // 10

    multiply = 1
    for digit in digits: multiply *= digit

    return persistence(multiply) + 1
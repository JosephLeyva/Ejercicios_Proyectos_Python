'''
EXERCISE: Create a function that returns the  sum of the divisors of a certain numbers
'''


def sum_of_divisors(n):
    sum_ = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum_ += i

    return sum_


print(sum_of_divisors(15))

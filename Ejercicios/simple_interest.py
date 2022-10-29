'''
EXERCISE: Create a method that computes a total of interests, given an amount of money, the percentage
of interest and the number of years
'''


def calculate_simple_interest(principal, interest, duration_in_years):
    total_interest = principal * (interest / 100) * duration_in_years
    return principal + total_interest


print(calculate_simple_interest(10000, 5, 5))

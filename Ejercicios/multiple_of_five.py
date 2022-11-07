'''
EXERCISE: Wrtie a program that finds all the multiples of 5 that are less
than a given value
'''

flag = True

while flag:
    try:
        n = int(input("Give me a number: "))
        print("You entered this value: ", n)

        i = 5
        while i < n:
            print(i, end=' ')
            i += 5
        print('\n')

        flag = False
    except ValueError:
        print("You did not enter a integer value... Try again")

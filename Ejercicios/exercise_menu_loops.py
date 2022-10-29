'''
EXERCISE: Choosing Loops
What would we use for the Menu if we would want to run the Menu again and again?
'''

number_1 = int(input("Enter Number1:\n"))
number_2 = int(input("Enter Number2:\n"))

print(
    '''
1 - Add
2 - Subtract
3 - Divide
4 - Multiply
5 - Exit
'''
)
option = int(input("Choose Operation: "))
while option != 5:
    result = None
    if option == 1:
        result = number_1 + number_2    
    elif option == 2:
        result = number_1 - number_2
    elif option == 3:
        result = number_1 / number_2
    elif option == 4:
        result = number_1 * number_2
    else:
        print("Invalid Option")
    
    
    print(f"Result is: {result}\n")

    option = int(input("Choose Operation: "))

print("Thank You!")
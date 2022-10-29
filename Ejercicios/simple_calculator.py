'''
EXERCISE: Create a program where:
* Ask user for input
* Enter two numbers
* choose an operation
  * add
  * multiply
  * divide
  * substract
* Publish the result!
'''

from cgitb import reset


num1 = int(input("Enter Number1:\n"))
num2 = int(input("Enter Number2:\n"))

print(
    '''
========= OPERATIONS =================
    1 - Add
    2 - Subtract
    3 - Divide
    4 - Multiply
======================================
''')

operation = int(input("Choose Operation: "))

result = None

if operation == 1:
    result = num1 + num2
elif operation == 2:
    result = num1 - num2
elif operation == 3:
    result = num1 / num2
elif operation == 4:
    result = num1 * num2
else:
    print("Error... You need to select a correct option")

if result != None:
    print(f'Result is - {result}')

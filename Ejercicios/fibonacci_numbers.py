'''
EXERCISE: Print the Fibonnaci numbers
'''
try:
    n = int(input("Give a integer value: "))
except ValueError:
    print("Error, you need to enter a integer value...")
    exit()

a, b = 0, 1

for i in range(n):
    b, a = a, a+b
    print(b)

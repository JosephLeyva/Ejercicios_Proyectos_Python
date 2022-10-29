'''
EXERCISE: Create a function that print a triangle-rectangle

Example
==============

print_a_number_triangle(5)
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

def print_a_number_triangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=' ')
        print()
            
            

print_a_number_triangle(10)
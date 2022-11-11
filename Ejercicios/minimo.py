n1 = int(input("Dame un número: "))
n2 = int(input("Dame un número: "))
n3 = int(input("Dame un número: "))

# mínimo = min(n1, n2, n3)


mínimo = n1

if n2 < mínimo:
    mínimo = n2
if n3 < mínimo:
    mínimo = n3

print(f'El mínimo es: {mínimo}')

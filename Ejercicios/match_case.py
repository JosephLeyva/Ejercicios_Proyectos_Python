n1 = int(input("Dame un número: "))
n2 = int(input("Dame otro número: "))

operador = input("Qué operación deseas realizar? ")

resultado = None

match operador:
    case '+':
        resultado = n1 + n2
    case '-':
        resultado = n1 - n2
    case '*':
        resultado = n1 * n2
    case '/':
        resultado = n1 / n2
    case _:
        print("Operador incorrecto")

if resultado is not None:
    print(f'{n1} {operador} {n2} = {resultado}')

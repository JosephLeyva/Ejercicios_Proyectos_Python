VOCALES = 'AEIOUaeiou'

palabra = input("Dame una palabra: ")

numero_vocales = len([x for x in palabra if x in VOCALES])

resultado = len(palabra) * numero_vocales
print(resultado)

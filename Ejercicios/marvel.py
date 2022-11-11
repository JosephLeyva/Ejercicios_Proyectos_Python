print("Bienvenido Usuario. En este programa adivinaremos un personaje de Marvel")
print("Responde con Y o N")


def conversion(res):
    return True if res in 'yY' else False


respuestas = 'yYnN'
try:
    puede_volar = input("Tu personaje puede volar? ")
    es_humano = input("Tu personaje es humano? ")
    tiene_mascara = input("Tu personaje tiene máscara? ")

    assert puede_volar in respuestas
    assert es_humano in respuestas
    assert tiene_mascara in respuestas

    puede_volar = conversion(puede_volar)
    es_humano = conversion(es_humano)
    tiene_mascara = conversion(tiene_mascara)

    if puede_volar:
        if es_humano:
            if tiene_mascara:
                print("Ironman")
            else:
                print("Captain Marvel")
        elif tiene_mascara:
            print("Ronan Accuser")
        else:
            print("Vision")
    elif es_humano:
        if tiene_mascara:
            print("Spiderman")
        else:
            print("Hulk")
    elif tiene_mascara:
        print("Black Bolt")
    else:
        print("Thanos")

except:
    print("Error... Respuesta invalida")

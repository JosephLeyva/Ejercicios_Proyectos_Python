persona1 = input("Jugador 1 - Opcion: ").lower()
persona2 = input("Jugador 2 - Opcion: ").lower()

if persona1 == "piedra":
    if persona2 == "piedra":
        print("Empate.")
    elif persona2 == "papel":
        print("Gana persona2. El papel envuelve a la piedra")
    elif persona2 == "tijeras":
        print("Gana persona1. La piedra rompe tijera")
    else:
        print("Opció invalida...")
elif persona1 == "papel":
    if persona2 == "piedra":
        print("Gana persona1. El papel envuelve a la piedra")
    elif persona2 == "papel":
        print("Empate.")
    elif persona2 == "tijeras":
        print("Gana persona2. Las tijeras cortan el papel")
    else:
        print("Opción inválida")
elif persona1 == "tijeras":
    if persona2 == "piedra":
        print("Gana persona2. La piedra rompe tijera")
    elif persona2 == "papel":
        print("Gana persona1. Las tijeras cortan el papel")
    elif persona2 == "tijeras":
        print("Empate.")
    else:
        print("Opción inválida")
else:
    print("Opción inválida")

año = int(input("Dame un año: "))

es_bisiesto = True if ((año % 4 == 0 and año % 100 != 0)
                       or año % 400 == 0) else False

print(es_bisiesto)

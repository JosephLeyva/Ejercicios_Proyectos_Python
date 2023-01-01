def dec_to_bin(cociente):
    binarios = []
    while cociente != 0:
        residuo = cociente % 2
        cociente = cociente // 2
        binarios.append(str(residuo))
    
    
    resultado = ""
    return resultado.join(binarios[::-1])
        

res = dec_to_bin(22)
print(res)
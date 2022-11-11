rutas = '//1.1.1.1/eoi/python'
lista_ruta = rutas.split('/')
equipo = lista_ruta[2]
ruta = '/' + lista_ruta[3] + '/' + lista_ruta[4]
print(f'{equipo=}; {ruta=}')
# '''
# RESTO	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22
# LETRA	T	R	W	A	G	M	Y	F	P	D	X	B	N	J	Z	S	Q	V	H	L	C	K	E
# '''

numero = int(input("Dame tu NIF: "))
LETRAS = 'TRWAGMYFPDXBNJZSQVHLCKE'

residuo = numero % 23

resultado = str(numero) + LETRAS[residuo]

print(resultado)

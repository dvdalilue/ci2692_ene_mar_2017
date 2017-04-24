"""

mensaje.py

Descripcion:	Programa que descifra un mensaje secreto utilizando
			 	heap

Autor: Orlando Chaparro Salazar. Carnet 12-11499
email: orlancss1@gmail.com
febrero, 16 de 2017

"""
from heap_functions import *
from arrayT import ArrayT

A = []
C = []
contador = 0
ConjuntoFinal = []
palabraFinal = ''

f = open('mensaje-cifrado.txt', 'r+')

for line in f.readlines():				#Fragmento de codigo que separa las palabras por *
	A.append(line)						#y cuenta en la variable contador la cantidad de palabras que debemos tomar
	l = line.split('*')

for i in range(0, len(A[0])):
	if A[0][i] == '*':
		contador += 1

for i in range(0, contador):
	if l[i] == '':
		pass	
	else:
		C.append(l[i])


print("El mensaje que ha introducido es: " + str(A[0]))



arreglo1 = ArrayT(len(C))				#Arreglo creado para almacenar cada palabra  separada por *
arreglo2 = ArrayT(len(C))				#Arreglo creado para almacenar todas las palabras ordenadas por letras 

for i in range(0, len(C)):

	aux_array = ArrayT(len(C[i]))		#Arreglo que almacena las letras de cada palabra que tiene arreglo1


	arreglo1[i] = aux_array				#Cada palabra almacenada en aux_array es introducida en arreglo1
	for j in range(0, len(C[i])):		

		arreglo1[i][j] = C[i][j]		#Debemos desfragmentar cada palabra separada por * en letras que posteriormente
										#seran ordenadas. Luego, ordenamos las palabras mediante el heap sort y volvemos
	heap_sort(aux_array)				#a unir cada palabra
	arreglo2[i] = arreglo1[i]



#arregloDefinitivo = ArrayT(len(C[i]))

for i in range(len(arreglo2)):
	ConjuntoFinal.append(arreglo2[i][0])
	palabraFinal += str(ConjuntoFinal[i]) 

print("Para el mensaje dado, la palabra descifrada es: " + str(palabraFinal))

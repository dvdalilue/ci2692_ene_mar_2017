	
from arrayT import ArrayT
from mergesort import *

"""

torta.py

Descripcion: Algoritmo que ordena los ingredientes para una torta e indica si esta se puede realizar o no

Autor: Orlando Chaparro Salazar. Carnet 12-11499

email: orlancss1@gmail.com

febrero, 16 de 2017

"""


f = open('ing2.txt', 'r+')

p = []

contador = 0

arregloDeIngredientes = []

for line in f.readlines():
	l = line.split('\t')
	if len(l) < 2:
		pass
	else: 
		l[2] = l[2].split('\n')[0]

	p.append(l)

# print(p)

for i in range(1, len(p)):
	arregloDeIngredientes.append(p[i])

#Primero ordenamos los ingredientes que si se poseen, luego los que no:

# print(arregloDeIngredientes)

arreglo_auxiliar = ArrayT(len(arregloDeIngredientes))

for i in range(0, len(arregloDeIngredientes)):
	if arregloDeIngredientes[i][2] == 'Si':
		arreglo_auxiliar[i] = 1
	else:
		arreglo_auxiliar[i] = 0

merge_sort_para_dos_arreglos(arreglo_auxiliar, arregloDeIngredientes)

print(arregloDeIngredientes)

for i in range(0, len(arregloDeIngredientes)):
	contador += arreglo_auxiliar[i]

if contador <= len(arregloDeIngredientes):
	print("La torta se puede preparar")

else:
	print("La torta no se puede preparar")

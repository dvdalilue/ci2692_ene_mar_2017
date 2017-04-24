#
#Universidad Simon Bolivar
#Laboratorio de Algoritmos II
#Examen 2
#Autor: ANgel Morante
#Carnet: 13-10931
#

#Descripccion: CLiente que prueba la implementacion de una
#			   clase publica de python denominada conjunto
#			   La cual es una lista enlazada simple 
#			   que es el equivalente al concepto matematico de un conjunto finito.

from conjunto import*
import random, sys, argparse

def prueba_conjunto(m):
	#Generamos arreglos de numeros aleatorios

	elementos1 = [random.randint(0,m) for x in range(50)]
	elementos2 = [random.randint(0,m*2) for x in range(100)]
	#Creamos los conjuntos
	Conjunto1 = Conjunto()
	Conjunto2 = Conjunto()

	for i in range(len(elementos1)):
		c1 = elementos1[i]
		Conjunto1.Agregar(c1) #Agregamos elementos en los conjuntos
		
	for i in range(len(elementos2)):
		c2 = elementos2[i]
		Conjunto2.Agregar(c2) #Agregamos elementos en los conjuntos
		

	Conjunto3 = Conjunto1.Union(Conjunto2) #Unimos los conjuntos
	Conjunto4 = Conjunto1.Interseccion(Conjunto2) #Intersectamos los conjuntos

	#Se muestran los conjuntos
	print("\nCONJUNTO INICIAL 1: \n")
	Conjunto1.Mostrar()
	print("\nCONJUNTO INICIAL 2: \n")
	Conjunto2.Mostrar()
	print("\nConjunto UNION de inicial 1 e inicial 2: \n")
	Conjunto3.Mostrar()
	print("\nConjunto Interseccion de inicial 1 e inicial 2: \n")
	Conjunto4.Mostrar()

#Inicia la prueba:
if __name__ == "__main__":
	# Recibe el valor m introducido por terminal, recuerde:
	# python test_htable.py < m >
    m = int(sys.argv[1])
    prueba_conjunto(m)







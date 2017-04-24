""" Laboratorio 1 .algoritmos II .ene-mar 2017 
	fecha: 19/01/2017
    Descripcion: Modulo con la implementacion de algoritmos de ordenamientos
              que son aplicados sobre listas de elementos de tipo numerico
	autores: Edymar Mijares 12-10882
	         Jose Carmona 11-10156

	correo: - edys.beccaria@gmail.com
		- carmona621@hotmail.com
ultima edicion :09/02/2017"""

import random 
from arrayT import ArrayT
from heap_functions import heap_sort
from quick_fuctions import quicksort_basico
from quick_fuctions import quicksort_aleatorio


#def InsertionSort(a):
#    """
#    Ordenamiento por medio del algoritmo de Insertion
#
#    Parametros:
#        a: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
#    Completar

#def BubbleSort(a):
#    """
#    Ordenamiento por medio del algoritmo de Bubble Sort
#
#    Parametros:
#        a: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
#   Completar

#def SelectionSort(A):
#    """
#    Ordenamiento por medio del algoritmo de Selection Sort
#
#    Parametros:
#        A: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
#   Completar

#def mergesort(A):
#    """
#    Ordenamiento por medio del algoritmo de mergesort
#
#    Parametros:
#        A: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
#   Completar

 #ordenamiento burbuja (0)Kaldewaij

#ordenamiento mergesort kaldewaij
def mergesort(A):
	k = 1
	N = len(A)
	A3 = []
	while k < N:
		a = 0
		b = k
		c = min((2*k),N)
		while  b < N:
			for x in range(a,c):
				A3.append("")
			p,q,r = a,b,a
			while p!=b and q!=c:
				if A[p] <= A[q]:
					A3[r] = A[p]
					r += 1
					p += 1
				elif A[q] <= A[p]:
					A3[r] = A[q]
					r += 1
					q += 1
			while p!=b:
				A3[r] = A[p]
				r += 1
				p += 1
			while q!=c:
				A3[r] = A[q]
				r += 1
				q += 1
			r = a
			while r!=c:
				A[r] = A3[r]
				r += 1
			a,b,c = a+(2*k),b+(2*k),min((c+(2*k)),N)
		k = k*2

	return A


####### se hicieron 3 implementaciones comparando heapsort con mergesort y quicsort con las llamadas:


#lab4 prueba 1 ./cliente_ordenamiento.py -g -p 1 -t 3 1000 2000 4000 5000
#lab4 prueba 2 ./cliente_ordenamiento.py -g -p 2 -t 3 100 200 400 500 
#lab4 prueba 3 ./cliente_ordenamiento.py -g -p 3 -t 3 100 200 400 500
#intentamos hacer la llamada para las pruebas 2 y 3  con el respectivo comando ./cliente_ordenamiento.py -g -p 2 -t 3 1000 2000 4000 5000 y ./cliente_ordenamiento.py -g -p 3 -t 3 1000 2000 4000 5000 respectivamente sin embargo las prubas generan un error por excederse el numero de 



"""
# Descripcion: Modulo con la implementacion de algoritmos de ordenamientos
#              que son aplicados sobre listas de elementos de tipo numerico
# Autores: Angelica Acosta 14-10005 - Yeferson Licet 14-10572 
# emails:  14-10005@usb.ve 14-10572@usb.ve
"""
from arrayT import ArrayT
from heap_functions  import heap_sort
from quick_functions import quicksort_basico, quicksort_aleatorio
import time

def merge_sort(A):
	"""
	Implementacion del algoritmo Mergesort del libro 
	Programming: the derivation of algorithms de Kaldewaij.
	
	Parametros:
		A: Un arreglo a ordenar

	Efecto Secundario:
		El arreglo de entrada es ordenado en orden ascendente
	"""
	n = len(A)
	k = 1

	while k < n:
		a,b,c = 0, k, min((2*k),n)

		while b < n:
			p,q,r = a,b,a
			z = ArrayT(c)

			while p!= b and q != c:
				if A[p] <= A[q]: 
					z[r] = A[p]
					r,p  = r+1, p+1
				else:
					
					z[r] = A[q]
					r,q  = r+1, q+1

			while p != b:
				z[r] = A[p]
				r,p = r+1, p+1

			while q != c:
				z[r] = A[q]
				r,q = r+1, q+1
			r = a

			while r != c:
				A[r] = z[r]
				r = r+1

			a,b,c = a+2*k,b+2*k, min((c+2*k), n)
		k = k*2
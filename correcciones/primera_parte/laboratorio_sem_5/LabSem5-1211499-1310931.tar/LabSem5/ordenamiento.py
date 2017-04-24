"""
# Descripcion: Modulo con la implementacion de algoritmos de ordenamientos
#              que son aplicados sobre listas de elementos de tipo numerico
# Autor: Orlando Chaparro Carnet: 12-11499
         Angel Morante Carnet: 13-10931
# email: 12-11499@usb.ve
         13-10931@usb.ve // morante413@gmail.com

"""


import random #Importacion de Bibliotecas
from arrayT import ArrayT
from heap_functions import heap_sort
import quick_functions

'''
#    ORDENAMIENTO POR INSERCION
#    Ordenamiento por medio del algoritmo de Insertion
#
#    Parametros:
#        a: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """

def insertion_sort(seq):
    j=1
    for j in range(0,len(seq)):
        key = seq[j]
        #Inserto seq[j]
        i = j-1
        while i >= 0 and seq[i] > key:
            seq[i+1] = seq[i]
            i = i - 1
        seq[i+1] = key
    pass

#    ORDENAMIENTO BURBUJA
#    Ordenamiento por medio del algoritmo de Bubble Sort
#
#    Parametros:
#        a: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    Implementacion del algoritmo Bubble Sort (0) del libro 
#    Programming: the derivation of algorithms de Kaldewaij.

def bubble_sort(a):
    n = 0
    N = len(a)
    while n != N:
        k = N - 1
        while k !=  n:
            if a[k-1] <= a[k]:
                 pass
            elif a[k-1] > a[k]:
               a[k] = a[k-1]
            k = k -1
        n = n + 1


#    ORDENAMIENTO POR SELECCION
#    Ordenamiento por medio del algoritmo de Selection Sort
#
#    Parametros:
#        a: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    Implementacion del algoritmo Selection Sort  del libro 
#    Programming: the derivation of algorithms de Kaldewaij

def selection_sort(a):

    n = 0
    N = len(a)
    while n != N:
        c,b = n, N-1
        while c != b:
            if a[c] <= a[b]:
                b = b -1
            elif a[b] <= a[c]:
                c = c + 1
        a[n] = a[c]
        n = n + 1

'''

def merge_sort(A):
	"""
	Implementacion del algoritmo MergeSort pag 186 del libro 
	Programming: the derivation of algorithms de Kaldewaij.
		
	Parametros:
	A: Un arreglo a ordenar

	Efecto Secundario:
	El arreglo de entrada es ordenado en orden ascendente
	"""	
	k = 1
	while k < len(A):
		a, b, c = 0, k, min(2*k, len(A))
		while b < len(A):
			p, q, r = a, b, a
			z = ArrayT(c-a)
			while p != b and q != c:
				if A[p] <= A[q]:
					z[r-a] = A[p]
					r += 1
					p += 1
				elif A[q] <= A[p]:
					z[r-a] = A[q] 
					r += 1
					q += 1
					
			while p != b:
				z[r-a] = A[p]
				r += 1
				p += 1
			
			while q != c:
				z[r-a] = A[q] 
				r += 1
				q += 1
			
			r = a
			while r != c:
				A[r] = z[r-a] 
				r += 1
			
			a, b, c = a + 2*k, b + 2*k, min(c + 2*k, len(A))
		
		k = k * 2
	
	return A


def quicksort_basico(A):
	r=len(A) - 1
	p=0
	return quick_functions.quicksort_basico(A,p,r)

def quicksort_aleatorio(A):
	r=len(A) - 1
	p=0
	return quick_functions.quicksort_aleatorio(A,p,r)


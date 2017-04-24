"""
# Descripcion: Modulo con la implementacion del algoritmo mergesort
			   que fue usado para realizacion de los laboratorios

# Autor: Orlando Chaparro Carnet: 12-11499


# email: 12-11499@usb.ve

"""


import random #Importacion de Bibliotecas
from arrayT import ArrayT


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


def merge_sort_para_dos_arreglos(A, B):
	"""
	Implementacion del algoritmo MergeSort pag 186 del libro 
	Programming: the derivation of algorithms de Kaldewaij.
		
	Parametros:
	A: Un arreglo a ordenar
	B: Arreglo que debe seguir el mismo ordenamiento de A

	Efecto Secundario:
	El arreglo de entrada A es ordenado en orden ascendente
	El arreglo de entrada B es ordenado siguiendo el mismo patron de cambios que A
	"""	
	k = 1
	while k < len(A):
		a = 0 
		b = k
		c = min(2*k, len(A))
		while b < len(A):
			p = a 
			q = b 
			r = a
			z = ArrayT(c-a)
			ArregloB = ArrayT(c-a)           
			


			while p != b and q != c:

				if A[p] <= A[q]:                # (1)

					if A[p] < A[q]:             #Recordemos que las variables p, q, r y a son usadas como
						ArregloB[r-a] = B[p]    #subindices de los elementos de las listas. Como solo ocurre (1)
						z[r-a] = A[p]           #o (2), separamos por casos y posteriormente ordenamos las listas.
					elif A[p] == A[q]:
						ArregloB[r-a] = B[q]    #Primero ordenamos la lista A y a partir de ella ordenamos la
						z[r-a] = A[q] 	        #lista B
					r += 1
					p += 1

				elif A[p] >= A[q]:	            # (2)					
					ArregloB[r-a] = B[q]
					z[r-a] = A[q] 
					r += 1
					q += 1

					
			while p != b:
				z[r-a] = A[p]
				ArregloB[r-a] = B[p]
				r += 1
				p += 1
			
			while q != c:

				z[r-a] = A[q]
				ArregloB[r-a] = B[q]
				r += 1
				q += 1
			
			r = a

			while r != c:
				A[r] = z[r-a] 
				B[r] = ArregloB[r-a]
				r += 1
			
			a, b, c = a + 2*k, b + 2*k, min(c + 2*k, len(A))
		
		k = k * 2
	
	return A, B

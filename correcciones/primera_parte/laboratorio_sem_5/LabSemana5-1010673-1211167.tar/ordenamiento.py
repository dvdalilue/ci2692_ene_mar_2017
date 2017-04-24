"""
# Descripcion: Laboratorio 4
# Autores: 10-10673 Jorge Sanchez
           12-11167 Greanny Vivas
# email: jorges1002@gmail.com
		 vivas.anny@gmail.com
"""
from arrayT import ArrayT
import random
from funciones import quicksort_basico, heap_sort, quicksort_aleatorio
"""
#Insertion_sort
#Extraido del Cormen 

    Ordenamiento por medio del algoritmo de Insertion

    Parametros:
        a: Un arreglo a ordenar

    Efecto Secundario:
        El arreglo de entrada es ordenado en orden ascendente

def insertion_sort(a):
	n = len(a)
	for i in range (1,n):
		key = a[i]
		j = i-1
		while j >= 0 and a[j] > key:
			a[j+1] = a[j]
			j -= 1
		a[j+1] = key	
	return a



#Bubble_sort
#Extraido del Cormen

    Ordenamiento por medio del algoritmo de Bubble Sort

    Parametros:
        a: Un arreglo a ordenar

    Efecto Secundario:
        El arreglo de entrada es ordenado en orden ascendente

def bubble_sort(a):
	N = len(a)
	n = 0
	while n != N:
		k = N-1
		while k != n:
			if a[k-1] <= a[k]:
				pass
			elif a[k-1] > a[k]:
				a[k-1],a[k] = a[k],a[k-1]
			k -= 1
		n += 1
	return a


 # Selection_Sort	
#Extraido del Cormen

    Ordenamiento por medio del algoritmo de Selection Sort

    Parametros:
       a: Un arreglo a ordenar

    Efecto Secundario:
        El arreglo de entrada es ordenado en orden ascendente

def selection_sort(a):
	n = len(a)
	for i in range (0,n):
		j = i+1
		while j < n:
			if a[j]<=a[i]:
				a[i],a[j] = a[j],a[i]
			j += 1	
	return 

def bubble_sort_modificado(a):

    Implementacion del algoritmo Bubble Sort (1) del libro 
    Programming: the derivation of algorithms de Kaldewaij.
    
    Parametros:
        a: Un arreglo a ordenar

    Efecto Secundario:
        El arreglo de entrada es ordenado en orden ascendente

    N = len(a)
    n = 0
    b = False
    while (n != N) and (not b):
        k = N - 1
        b = True
        while k != n:
            if a[k-1] > a[k]:
                b = False
                a[k-1], a[k] = a[k], a[k-1]
            k -= 1
        n += 1
"""

# Mergesort Kaldewaij
def Mergesort (z):
	k = 1
	N = len(z)
	h = ArrayT(N)
	for i in range(N):
		h[i] = z[i]
	while k < N :
		a,b,c = 0,k,min((2*k),N)
		while b < N:
			p,q,r = a,b,a
			while p != b and q != c:
				if h[p]<=h[q]:
					z[r],r,p = h[p],r+1,p+1 
				elif h[q]<= h[p]:
					z[r],r,q = h[q],r+1,q+1  
			while p != b:
				z[r],r,p = h[p], r+1,p+1
			while q != c:
				z[r],r,q = h[q], r+1,q+1
			r = a
			while r!=c:
				h[r], r = z[r], r+1
			a,b,c = a+2*k,b+2*k,min(c+2*k,N)
		k = k*2

	return z

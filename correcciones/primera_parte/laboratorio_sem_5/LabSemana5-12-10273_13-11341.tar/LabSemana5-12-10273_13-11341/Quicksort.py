"""
# Descripcion: Modulo con la implementacion del algoritmo de ordenamiento
#              Quicksort
# Autor: Jesus Kauze y David Segura
# email: 12-10273@usb.ve y 13-11341@usb.ve
"""
from random import *

def Quicksort(A,p,r):
    if p<r:
    	q = Partition(A,p,r)
    	Quicksort(A,p,q-1)
    	Quicksort(A,q+1,r)

def Partition(A,p,r):
	x = A[r]
	i = p -1
	for j in range(p,r):
		if A[j] <= x:
			i = i + 1 
			A[i], A[j] = A[j], A[i]
	A[i+1], A[r]= A[r], A[i+1]
	return i+1 


def quicksort_basico(A):
	p=0
	r=len(A)-1
	Quicksort(A,p,r)
	return A

def Randomized_Partition(A,p,r):
	i = randint(p,r)
	A[r],A[i]=A[i],A[r]
	return Partition(A,p,r)

def Randomized_Quicksort(A,p,r):
	if p<r:
		q= Randomized_Partition(A,p,r)
		Randomized_Quicksort(A,p,q-1)
		Randomized_Quicksort(A,q+1,r)

def quicksort_aleatorio(A):
	p=0
	r=len(A)-1
	Randomized_Quicksort(A,p,r)
	return A

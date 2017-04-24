"""
# Descripcion: Laboratorio 4
# Autores: 10-10673 Jorge Sanchez
           12-11167 Greanny Vivas
# email: jorges1002@gmail.com
         vivas.anny@gmail.com
"""
import random


# Heapsort
def swap(array, i, j):
    array [i],array[j] = array[j] , array[i]
    return
    
def parent(i):
    return [(i + 1) // 2]-1

def left(i):
    return (2*(i+1)-1)

def right(i):
    return (2*(i+1))

def heapify(array, i, length):
    l = left(i)
    r = right(i)
    largest = i
    if l < length and array[l] > array[i]:
        largest = l
    if r < length and array [r] > array [largest]:
        largest = r
    if i != largest:
        swap (array,i,largest)
        heapify(array,largest, length)
    return array    

def build_max_heap(array):
    for i in range (len(array)//2,-1,-1): 
        heapify(array,i,len(array))
    return array

def heap_sort(array):
    build_max_heap(array)
    for i in range (len(array)-1,0,-1):
        swap(array,0,i)
        heapify(array,0,i)
    return array

def dequeue(array):
    assert ((len(array) < 2), "ERROR: El arreglo debe tener mas de un elemento")    
    aux_array =ArrayT(len(array)-1)
    for i in range (0,len(array)-1):
        aux_array[i] = array[i+1]  
    heapify(aux_array,0,len(aux_array))         
    return(array[0],aux_array)
#Hasta aqui Heap


#Quicksort y Randomized Quicksort

def partition(A,p,r):
	x, i = A[r], p-1
	for j in range(p,r):
		if A[j] <= x:
			i = i + 1
			swap(A,i,j)
	swap(A,i+1,r)
	return (i+1)

def quicksort(A,p,r):
	if p < r:
		q = partition(A,p,r)
		quicksort(A,p,q-1)
		quicksort(A,q+1,r)
	return A

def quicksort_basico(A):
	quicksort(A,0,len(A)-1)
	return A

def rPartition(A,p,r):
	i = random.randint(p,r)
	swap(A,r,i)
	return partition(A,p,r)

def rQuicksort(A,p,r):
	if p < r:
		q = rPartition(A,p,r)
		rQuicksort(A,p,q-1)
		rQuicksort(A,q+1,r)
	return A
	
# Aleatorio
def quicksort_aleatorio(A):
	rQuicksort(A,0,len(A)-1)
	return A


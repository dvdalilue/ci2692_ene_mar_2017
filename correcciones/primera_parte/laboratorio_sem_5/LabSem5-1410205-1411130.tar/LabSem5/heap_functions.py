from arrayT import ArrayT
from random import randint

def heapify(array, i, lenght):
	hizq=left(i)
	hder=right(i)
	mayor = i
	if hizq < lenght and array[hizq] > array[i]:
		mayor = hizq
	if hder < lenght and array[hder] > array[mayor]:
		mayor = hder
	if mayor!= i:
		array=swap(array,mayor,i)
		array=heapify(array,mayor,lenght)
	return array

def build_max_heap(array):
	i=len(array)//2
	while i>=0:
		array=heapify(array,i,len(array)-1)
		i-=1
	return array

def heap_sort(array):
	array=build_max_heap(array)
	i=len(array)-1
	while i!=0:
		array=swap(array,0,i)
		array=heapify(array,0,i)
		i-=1
	return array

def swap(array, i, j):
	array[i],array[j]=array[j],array[i]
	return array

def dequeue(array):
	if len(array) < 1:
		print('El arreglo debe tener mas de un elemento.')
	else:
		auxarray=ArrayT(len(array)-1)
		for i in range(len(array)-1):
			auxarray[i]=array[i+1]
		auxarray=heapify(auxarray,0,len(auxarray)-1)
		return (array[0],auxarray)

def parent(i):
	return ((i + 1) // 2)-1 

def left(i):
	return (2*(i+1)-1)

def right(i):
	return (2*(i+1))

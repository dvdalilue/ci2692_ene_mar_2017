from arrayT import ArrayT

def heapify(array, i, length):
	left_child  = left(i)
	right_child = right(i)

	father = i

	if left_child < length and array[left_child] > array[i]:
		father = left_child

	if right_child < length and array[right_child] > array[father]:
		father = right_child

	if father != i:
		swap(array, father, i)
		heapify(array, father, length)


def build_max_heap(array):
	n = len(array)
	for i in range(0,n//2+1):
		heapify(array,(n // 2) - i, n)

def heap_sort(array):
	build_max_heap(array)

	n = len(array)
	for i in range(1,n):
		swap(array,0,n-i)
		heapify(array, 0, n-i)
		

def swap(array, i, j):
	array[i], array[j] = array[j], array[i]

def dequeue(array):
	if len(array) < 1:
		print("El arreglo debe tener mas de un elemento")
	aux_array = ArrayT(len(array)-1)
	for i in range(1,len(array)):
		aux_array[i-1] = array[i]
	heapify(aux_array,0, len(aux_array))
	return (array[0], aux_array)

def parent(i):
	return  ((i + 1) // 2) - 1

def left(i):
	return (2*(i+1)-1)

def right(i):
	return (2*(i+1))
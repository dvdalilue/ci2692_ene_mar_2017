"""
# Descripcion: 
# Modulo con la implementacion de algoritmos de ordenamientos
# que son aplicados sobre listas de elementos de tipo numerico
#
# Autores: Angelica Acosta 14-10005 - Yeferson Licet 14-10572 
# emails:  14-10005@usb.ve 14-10572@usb.ve
"""

import random
import math
from arrayT import ArrayT

"""
# *************************************
#
#          Funciones de ayuda
#
# *************************************
"""
SIZE_THRESHOLD = 10
def heapify(array, i, length):
	"""
	Convierte un arreglo en heap desde el nodo i

	Parametros:	
		array   -- arreglo a procesar
		i       -- indice de la hoja donde comienza el proceso
		length  -- tamaño del arreglo

	Retorna:
		Arreglo con estructura de heap
	"""
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


def build_max_heap(array, p, r):
	"""
	Convierte un subarreglo en heap

	Parametros:	
		array   -- arreglo a procesar
		p       -- indice donde comienza el subarreglo
		r  		-- indice donde termina el subarreglo

	Retorna:
		Arreglo con estructura de heap
	"""
	n = r-p+1
	for i in range(p, n//2+1):
		heapify(array,(n // 2) - i, n)

def heap_sort_loop(array, p , r):
	"""
	Ordena los elementos de un subarreglo

	Parametros:	
		array   -- arreglo a procesar
		p       -- indice donde comienza el subarreglo
		r  		-- indice donde termina el subarreglo

	Retorna:
		Arreglo ordenado de manera no decreciente
	"""
	build_max_heap(array, p , r)

	n = r-p+1
	for i in range(1,n):
		swap(array,p,n-i)
		heapify(array, p, n-i)
		

def swap(array, i, j):
	"""
	Intercambia dos elementos de un arreglo

	Parametros:	
		array   -- arreglo a procesar
		i       -- indice cuyo contenido será intercambiado
		j  		-- indice cuyo contenido será intercambiado

	Retorna:
		Arreglo con los valores intercambiados en los indices i,j
	"""
	array[i], array[j] = array[j], array[i]

def parent(i):
	"""
	Padre de un nodo

	Parametros:	
		i   -- nodo a calcular parent

	Retorna:
		La posicion del padre de un nodo i
	"""
	return  ((i + 1) // 2) - 1

def left(i):
	"""
	Hijo izquierdo de un nodo

	Parametros:	
		i   -- nodo a calcular hijo

	Retorna:
		La posicion del hijo izquierdo de un nodo i
	"""
	return (2*(i+1)-1)

def right(i):
	"""
	Hijo derecho de un nodo

	Parametros:	
		i   -- nodo a calcular hijo

	Retorna:
		La posicion del hijo derecho de un nodo i
	"""
	return (2*(i+1))


def insertion_sort(A, p, r):
	"""
	Realiza insertion sort sobre un subarreglo

	Parametros:	
		array   -- arreglo a procesar
		p       -- indice donde comienza el subarreglo
		r  		-- indice donde termina el subarreglo

	Retorna:
		Arreglo ordenado de manera no decreciente
	"""
	for i in range(p+1, r+1):
		key = A[i]
		j = i-1
		while j >= 0 and A[j] > key:
			A[j+1] = A[j]
			j = j-1

		if j+1 != i: 
			A[j+1] = key

def bigger(a, b, c):
	"""
	Obtiene el mayor de tres valores dados

	Parametros:	
		a   -- valor 1
		b   -- valor 2
		c   -- valor 3, en caso de c = None, compara sólo a y b

	Retorna:
		Mayor valor
	"""
	if c == None:
		if a > b:
			return a
		return b
	else:
		return bigger(bigger(a, b,  None), c, None)

def medianOf3(a, b, c):
	"""
	Obtiene la media de tres elementos

	Parametros:	
		a   -- valor 1
		b   -- valor 2
		c   -- valor 3

	Retorna:
		Media
	"""
	big = bigger(a, b, c)

	if big == a:
		return bigger(b, c, None)
	elif big == b:
		return bigger(a, c, None)

	return bigger(a, b, None)


def partition(A, p, r, x):
	"""
	Implementacion de la particion de Hoare en un subarreglo

	Parametros:	
		A   -- Arreglo a particionar
		p   -- indice donde comienza el subarreglo
		r  	-- indice donde termina el subarreglo
		x   -- valor del pivote

	Retorna:
		Posicion del pivote
	"""
	i = p-1
	j = r
	while True: 
		while True:
			j = j-1
			if A[j] <= x:
				break
		
		while True:
			i = i+1
			if A[i] >= x:
				break
				
		if i < j:
			A[i], A[j] = A[j], A[i]
		else:
			return j

def randomized_partition(A, p , r):
	"""
	Realiza una particion tomando un pivote aleatorio

	Parametros:	
		A   -- Arreglo a particionar
		p   -- indice donde comienza el subarreglo
		r  	-- indice donde termina el subarreglo

	Retorna:
		Posicion del pivote
	"""
	i = random.randint(p,r)
	A[r], A[i] =  A[i], A[r]
	return normalPartition(A, p , r)

def normalPartition(A,p,r):
	"""
	Realiza una particion sencilla vista en el laboratorio

	Parametros:	
		A   -- Arreglo a particionar
		p   -- indice donde comienza el subarreglo
		r  	-- indice donde termina el subarreglo

	Retorna:
		Posicion del pivote
	"""
	x = A[r]
	i = p-1
	for j in range(p,r):
		if A[j] <= x:
			i = i+1
			A[i], A[j] = A[j], A[i]
	A[i+1], A[r] = A[r], A[i+1]
	return i+1

"""
# *************************************
#
#     Implementaciones recursivas
#
# *************************************
"""

def quicksort_loop(A, p, r):
	
	if r-p > SIZE_THRESHOLD:
		q = partition(A, p, r,  medianOf3(A[p], A[p + (r-p)//2 +1], A[r]))
		quicksort_loop(A, p, q)
		quicksort_loop(A, q+1, r)
	else:
		insertion_sort(A, p, r)

def introsort_loop(A, p, r, limit):
	x = 0
	if r-p > SIZE_THRESHOLD:
		if limit == 0:
			heap_sort_loop(A, p, r)
			return
		limit = limit - 1
		m = medianOf3(A[p], A[p + (r-p)//2 +1], A[r])
		q = partition(A, p, r,  m)
		introsort_loop(A, p, q, limit)
		introsort_loop(A, q+1, r, limit)
	else:
		insertion_sort(A, p, r)

def quicksort_with_3_way_partitioning_loop(A,l,r):
	if r <= l:
		return

	i = l-1
	j = r
	p = l-1
	q = r
	v = A[r]

	while True:
		
		while True:
			i = i+1
			if A[i] >= v:
				break
		
		while True: 
			j = j-1
			if j == l:
				break 
			if A[j] < v:
				break

		if i >= j:
			break

		A[i], A[j] = A[j], A[i]
		
		if A[i] == v:
			p = p+1
			A[p], A[i] = A[i], A[p]
		
		if A[j] == v:
			q = q-1
			A[j], A[q] = A[q], A[j]


	A[i], A[r] = A[r], A[i]
	j = i-1

	i = i+1
	k = l
	while k < p:
		A[k], A[j] = A[j], A[k]
		k = k+1
		j = j-1

	k = r-1
	while k > q:
		A[i], A[k] = A[k], A[i]
		k = k-1
		i = i+1

	quicksort_with_3_way_partitioning_loop(A, l, j)
	quicksort_with_3_way_partitioning_loop(A, i, r)

def randomized_quicksort_loop(A, p ,r):
	if p<r:
		q = randomized_partition(A,p,r)
		randomized_quicksort_loop(A,p,q-1)
		randomized_quicksort_loop(A,q+1,r)

def quicksort_yaroslavskiy_loop(A, left, right):
	if right-left+1 < SIZE_THRESHOLD:
		insertion_sort(A,left,right)
	else:
		if A[left] > A[right]:
			p = A[right]
			q = A[left]
		else:
			p = A[left]
			q = A[right]
		l = left + 1
		g = right - 1
		k = l
		while k <= g:
			if A[k] < p:
				A[k] , A[l] = A[l], A[k]
				l = l+1
			else:
				if A[k] >= q:
					while A[g] > q and k < g:
						g = g - 1
					if A[g] >= p:
						A[k] , A[g] = A[g], A[k]
					else:
						A[k] , A[g] = A[g], A[k]
						A[k] , A[l] = A[l], A[k]
						l = l+1
					g = g-1
			k = k + 1
		l = l-1
		g = g+1
		A[left] = A[l]
		A[l] = p
		A[right] = A[g]
		A[g] = q
		quicksort_yaroslavskiy_loop(A,left,l-1)
		quicksort_yaroslavskiy_loop(A,l+1,g-1)
		quicksort_yaroslavskiy_loop(A,g+1,right)


"""
# *************************************
#
# Funciones alcanzables por el cliente
#
# *************************************
"""

def median_of_3_quicksort(A):
	quicksort_loop(A, 0, len(A)-1)
	
def introsort(A):
	introsort_loop(A, 0, len(A)-1, 2*math.floor(len(A)))

def quicksort_3_way_partitioning(A):
	quicksort_with_3_way_partitioning_loop(A, 0, len(A)-1)
	
def dual_pivot_quicksort(A):
	quicksort_yaroslavskiy_loop(A, 0, len(A)-1)

def randomized_quicksort(A):
	randomized_quicksort_loop(A,0,len(A)-1)

def heap_sort(A):
	heap_sort_loop(A, 0, len(A)-1)

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
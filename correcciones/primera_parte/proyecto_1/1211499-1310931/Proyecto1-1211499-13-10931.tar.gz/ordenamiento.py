"""
# Descripcion: Módulo que contiene la implementación de los algoritmos
			   de ordenamiento.

# Autor: Orlando Chaparro Carnet: 12-11499
         Angel Morante Carnet: 13-10931

# email: 12-11499@usb.ve
         13-10931@usb.ve // morante413@gmail.com

"""


import random, math #Importacion de Bibliotecas
from arrayT import ArrayT


##################################################################################
##                      DEFINICION DE LA FUNCION MERGE-SORT                     ##
##################################################################################

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

##################################################################################
##        DEFINICION DE LA FUNCION QUICK-SORT Y LAS FUNCIONES QUE UTILIZA       ##
##################################################################################


#DEFINCION DE LA FUNCION QUICKSORT BASICO
def quicksort_basico(A):
	r=len(A) - 1
	p=0
	return quicksort_basico_(A,p,r)


#DEFINCION DE LA FUNCION QUICKSORT ALEATORIO
def quicksort_aleatorio(A):
	r=len(A) - 1
	p=0
	return quicksort_aleatorio_(A,p,r)


#PARTICION DEL QUICKSORT                
def Partition_Quicksort(A, p, r):

	x = A[r]
	i = p - 1
	for j in range(p, r):
		if A[j] <= x:
			i = i + 1
			A[i],A[j] = A[j],A[i]
	A[i + 1],A[r] = A[r],A[i+1]
	
	return(i + 1)


#PROCEDIMIENTO PARA QUICKSORT BASICO
def quicksort_basico_(A, p, r):
	
	#procedimiento que recibe un arreglo A de 
	#tipo arrayT y ordena sus elementos con la 
	#implementacion de esta version 
	#de Quicksort.
	if p<r:
		q = Partition_Quicksort(A, p, r)
		quicksort_basico_(A, p, q - 1)
		quicksort_basico_(A, q + 1, r)

	
#PARTICION RANDOMIZADA DE QUICKSORT
def randomized_Partition(A, p, r):
	i = random.randint(p, r)
	A[r],A[i] = A[i],A[r]
	
	return Partition_Quicksort(A, p, r)


#PROCEDIMIENTO PARA QUICKSORT ALEATORIO
def quicksort_aleatorio_(A, p, r):
	
	#funcion que
	#recibe un arreglo A de tipo arrayT y 
	#ordena sus elementos con la implementacion
	#de la version aleatoria de Quicksort.
	
	if p < r:
		q = randomized_Partition(A, p, r)
		quicksort_aleatorio_(A, p, q - 1)
		quicksort_aleatorio_(A, q + 1, r)


##################################################################################
##         DEFINICION DE LA FUNCION HEAP-SORT Y LAS FUNCIONES QUE UTILIZA       ##
##################################################################################


#INICIO DE LA FUNCION HEAPIFY
def heapify(array, i, lenght):
    hijo_izq = left(i)
    hijo_der = right(i)
    el_mayor = i

    if hijo_izq < lenght and array[hijo_izq] > array[i]:
        el_mayor = hijo_izq
    if hijo_der < lenght and array[hijo_der] > array[el_mayor]:
        el_mayor = hijo_der
    if el_mayor != i:
        swap(array, el_mayor, i)
        heapify (array, el_mayor, lenght)


#INICIO DE LA FUNCION BUILD MAX HEAP
def build_max_heap(array):

    a = (len(array)-1) // 2
    for i in range(a,-1,-1):
        heapify(array,i,len(array))   


#HEAPSORT (ORDENAMIENTO POR MONTICULO)
def heap_sort(array):
    build_max_heap(array)
    a = len(array) - 1
    for i in range(a,0,-1):
        swap(array,0,i)
        heapify(array,0,i)


#FUNCION SWAP QUE INTERCAMBIA ELEMENTOS EN EL HEAP
def swap(array, i, j):
    array[i], array[j] = array[j] , array[i]


#FUNCION HIJO IZQUIERO
def left(i):
    return (2*(i+1)-1)


#FUNCION HIJO DERECHO
def right(i):
    return (2*(i+1))


##################################################################################
##         DEFINICION DE LA FUNCION INSERTION_SORT (RECIBE 3 PARAMETROS)        ##
##################################################################################

def insertion_sort(A, p, r):
	for j in range (p + 1, r):
		key = A[j]
		#Inserta A[j] de forma ordenada dentro del arreglo A
		i = j -1 
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key


##################################################################################
##                   DEFINICION DE (2.4) Dual_pivot_Quicksort                   ##
##																				##
##                ALGORITMO IMPLEMENTADO POR YAROSLAVSKIY EN 2009               ##
##################################################################################

def Dual_pivot_Quicksort(A, left, right):

	if right - left < 1:
		insertion_sort(A, left, right)
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
				A[k], A[l] = A[l], A[k]
				l += 1
			else:
				if A[k] >= q:
					while A[g] > q and k < g:
						g -= 1
					if A[g] >= p:
						A[k], A[g] = A[g], A[k]
					else:
						A[k], A[g] = A[g], A[k]
						A[k], A[l] = A[l], A[k]
						l += 1
					g -= 1

			k += 1

		l -= 1
		g += 1
		A[left] = A[l]
		A[l] = p
		A[right] = A[g]
		A[g] = q
		Dual_pivot_Quicksort(A, left, l-1)
		Dual_pivot_Quicksort(A, l+1, g-1)
		Dual_pivot_Quicksort(A, g+1, right)



##################################################################################
##               DEFINICION DE (2.3) Quicksort-WITH-3-PARTITIONING              ##
##																				##
##################################################################################


def QUICKSORT_w_3_PARTITIONING(a, l, r):

	if len(a) <= 10:
		insertion_sort(a, l, r+1)
	else:
		i = l - 1
		j = r
		p = l - 1
		q = r
		if r <= l:
			return
		v = a[r]
		while True:
			i += 1
			while a[i] < v:
				i += 1
			j -= 1
			while (v < a[j]):
				
				if j == l:
					break
				j -= 1				
			if i >= j:
				break
			a[i], a[j] = a[j], a[i]
			if a[i] == v:
				p += 1
				a[p], a[i] = a[i], a[p]
			if v == a[j]:
				q -= 1
				a[j], a[q] = a[q], a[j]

		a[i], a[r] = a[r], a[i]
		j = i - 1
		i = i + 1
		
		for k in range(l, p):
			a[k], a[j] = a[j], a[k]
			j -= 1

		for k in range(r-1, q-1, -1):
			a[i], a[k] = a[k], a[i]
			i += 1

		QUICKSORT_w_3_PARTITIONING(a, l, j)
		QUICKSORT_w_3_PARTITIONING(a, i, r)



##################################################################################
##       																		##
##             DEFINICION DE LA FUNCION Median-of-3 quicksort (2.1)             ##
##                                          									##
##################################################################################

# EMPEZAREMOS INDICANDO EL PROCEDIMIENTO PARTITION

def partition(A,p,r,x):
	i = p -1
	j = r
	while True:
		
		j = j-1
		while A[j] > x:
			j = j - 1

		i = i + 1
		while  A[i] < x:
			i = i + 1
		
		
		if i < j:

			A[i],A[j] = A[j],A[i]

			
		
		else: 
			return (j)
	return(j)

#FUNCION MEDIA DE TRES

def media_of_3(a,b,c):
	
	B=sorted([a,b,c])
	return B[1]
		
#FUNCION QUICKSORT LOOP
	
def quicksort_loop(A,f,b):
	size_threshold = 10
	while b - f > size_threshold:
		m = media_of_3(A[f],A[f+(b-f)//2],A[b-1])

		p = partition(A,f,b,m)

		if (p-f >= b-p):
			quicksort_loop(A,p,b)
			b = p
		else:
			
			if f == p:
				quicksort_loop(A,f,p)
				f = p + 1
			else:
				quicksort_loop(A,f,p)
				f = p

#PROCEDIMIENTO FINAL : FUNCION Median-of-3 quicksort (2.1) 			

def quicksort3(A,f,b):     
	quicksort_loop(A,f,b)
	insertion_sort(A,f,b)


##################################################################################
##       																		##
##                   DEFINICION DE LA FUNCION INTROSORT (2.2)                   ##
##                                          									##
##################################################################################


# FUNCION INTROSORT
def introsort(A,f,b):      #f = 0, b = len(A)
	floor_LG =2 * math.floor(math.log((b-f),2))
	introsort_loop(A,f,b,floor_LG)
	insertion_sort(A,f,b)

# FUNCION INTROSORT LOOP
def introsort_loop(A,f,b,floor_LG):
	while (b-f) > 10:
		if floor_LG == 0:
			insertion_sort(A,f,b)
			return
		floor_LG = floor_LG -1
		p = partition(A,f,b,media_of_3(A[f],A[f+(b-f)//2],A[b-1]))
		introsort_loop(A,p,b,floor_LG)
		b = p


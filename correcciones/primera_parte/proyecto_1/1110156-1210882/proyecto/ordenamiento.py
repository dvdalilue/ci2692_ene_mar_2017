""" Laboratorio 1 .algoritmos II .ene-mar 2017 
	fecha: 19/01/2017
    Descripcion: Modulo con la implementacion de algoritmos de ordenamientos
              que son aplicados sobre listas de elementos de tipo numerico
	autores: Edymar Mijares 12-10882
	         Jose Carmona 11-10156

	correo: - edys.beccaria@gmail.com
		- carmona621@hotmail.com
ultima edicion :22/02/2017"""
import math
import random 
from arrayT import ArrayT

#def mergesort(A):
#    """
#    Ordenamiento por medio del algoritmo de mergesort
#
#    Parametros:
#        A: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
#   La version que presentamos es la version iterativa del libro Kaldewaij

#def heap_sort(array):
#    """
#    Ordenamiento por medio del algoritmo de heaps
#
#    Parametros:
#        A: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """

#def quicksort_aleatorio(A):
#    """
#    Ordenamiento por medio del algoritmo de Quicksort randomizado
#
#    Parametros:
#        A: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """

#def Median_of3_Quicksort(A):
#    """
#    Ordenamiento por medio del algoritmo de median of 3 quicsort
#
#    Parametros:
#        A: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """

#def Introsort(A):
#    """
#    Ordenamiento por medio del algoritmo de Introsort
#
#    Parametros:
#        A: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """

#def Dual_piv_Quicksort(A):
#    """
#    Ordenamiento por medio del algoritmo de Quicksort with 3-way partitioning
#
#    Parametros:
#        A: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """

#def Dual_piv_Quicksort(A):
#    """
#    Ordenamiento por medio del algoritmo de Dual pivot Quicksort
#
#    Parametros:
#        A: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """


##########################################################################
##########################      MERGESORT     ############################
##########################################################################


def mergesort(A):
	k = 1
	N = len(A)
	A3 = []
	while k < N:
		a = 0
		b = k
		c = min((2*k),N)
		while  b < N:
			for x in range(a,c):
				A3.append("")
			p,q,r = a,b,a
			while p!=b and q!=c:
				if A[p] <= A[q]:
					A3[r] = A[p]
					r += 1
					p += 1
				elif A[q] <= A[p]:
					A3[r] = A[q]
					r += 1
					q += 1
			while p!=b:
				A3[r] = A[p]
				r += 1
				p += 1
			while q!=c:
				A3[r] = A[q]
				r += 1
				q += 1
			r = a
			while r!=c:
				A[r] = A3[r]
				r += 1
			a,b,c = a+(2*k),b+(2*k),min((c+(2*k)),N)
		k = k*2

	return A
##########################################################################
##########################      HEAPSORT     #############################
##########################################################################
def parent(i):
	return ((i + 1) // 2)-1

def left(i):
	return (2*(i+1)-1)

def right(i):
	return (2*(i+1))

def swap(array, i, j):
	array[i],array[j] = array[j],array[i]
	pass



def heapify(A, i, HeapSize):
	l = left(i)
	r = right(i)
    
	if l < HeapSize and A[l] > A[i]:
		M  = l
	else:
		M = i
	if r < HeapSize and A[r] > A[M]:
		M  = r
	if M != i:
		swap(A,M,i)
		heapify(A, M, HeapSize)



def build_max_heap(array):
	N = len(array)
	for i in range(N//2,-1, -1):
		heapify(array, i,N)
	pass

def heap_sort(array):
	HeapSize = len(array)-1 
	build_max_heap(array)
	for i in range(HeapSize,0,-1):
		swap(array,0,i)
		heapify(array, 0 ,i )
	pass
	
####################################################################################
##########################      QUICKSORT ALEATORIO     ############################
####################################################################################
def particionQ(A,p,r):
	x=A[r]
	i=p-1
	j=p
	for j in range(p,r):
		if A[j]<= x :
			i=i+1
			A[i],A[j]= A[j],A[i]
	A[i+1],A[r]=A[r],A[i+1]
	return(i+1)



def Randomized_partition(A,p,r):
	i= random.randint(p,r)
	A[i],A[r]=A[r],A[i]
	return particionQ(A,p,r)



def Randomized_Quicksort2(A,p,r):
	if p<r:
		q= Randomized_partition(A,p,r)
		Randomized_Quicksort2(A,p,q-1)
		Randomized_Quicksort2(A,q+1,r)

def quicksort_aleatorio(A):
	Randomized_Quicksort2(A,0,len(A)-1)

#####################################################################################
##########################      Median-of-3 quicksort    ############################
#####################################################################################

def insertionsort1(a):
	n = 1
	M = len(a)
	while n != M:
		k = n
		while k != 1 and a[k-1] > a[k]:
			a[k-1],a[k] = a[k],a[k-1]
			k = k-1
		if a[0] > a[1]:
			a[0],a[1] = a[1],a[0]
		n = n+1


def partition(A,p,r,x):
	i = p
	j = r
	while True:
		while A[j] > x:
			j = j - 1
		while  A[i] < x:
			i = i + 1
		if i < j:
			A[i],A[j] = A[j],A[i]
			if A[i] == A[j] :
				i = i + 1
				j = j - 1
		else: 
			return (j)
	return(j)

def media_of_3(a,b,c):
	x = 0
	if a >= b and b >= c:
		x = b
	elif a >= c and c >= b:
		x = c
	elif b >= a and a >= c:
		x = a
	elif b >= c and c >= a:
		x = c
	elif c >= a and a >= b:
		x = a
	elif c >= b and b >=a:
		x = b
	return x
		
	
	
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
				break
			else:
				quicksort_loop(A,f,p)
				f = p
			
def insertionsort(A,n,N):
	while n != N+1:
		k = n
		while k != 0 and A[k-1] > A[k]:
			A[k-1],A[k] = A[k],A[k-1]
			k = k-1
		if A[0] > A[1]:
			A[0],A[1] = A[1],A[0]
		n = n+1
	return (A)

def quicksort3(A,f,b):
	quicksort_loop(A,f,b)
	insertionsort(A,f,b)


def Median_of3_Quicksort(A):
	f = 0
	N = len(A)-1
	quicksort3(A,f,N)

#####################################################################################
##########################      Introsort    ########################################
#####################################################################################
def heap_sort3(array,inic,fin):
	HeapSize = (fin-inic)-1
	build_max_heap(array)
	for i in range(HeapSize,inic,-1):
		swap(array,0,i)
		heapify(array, 0 ,i )
	pass

def intro(A,f,b):
	floor_LG =2 * math.floor(math.log((b-f),2))
	introsort_loop(A,f,b,floor_LG)
	insertionsort(A,f,b)

def introsort_loop(A,f,b,floor_LG):
	while (b-f) > 10:
		if floor_LG == 0:
			heap_sort3(A,f,b)
			return
		floor_LG = floor_LG -1
		p = partition(A,f,b,media_of_3(A[f],A[f+(b-f)//2],A[b-1]))
		introsort_loop(A,p,b,floor_LG)
		b = p

def Introsort(A):
	f = 0
	N = len(A)-1
	intro(A,f,N)

################################################################################################
##############      Quicksort with 3-way partitioning   ########################################
################################################################################################
def quicksort3wayp(A, l, r):
	i, j, p, q = l-1, r, l-1, r   
	if r-l <=10 and r-l>0:
		insertionsort(A,l,r)
	elif r<=l:
		return
	v = A[r]        
	while True:  
		i = i+1
		while (A[i] < v):  	   
				i=i+1
		j = j-1
		while (v< A[j]):
			j = j-1
			if (j == 0):
				break		
		if (i>=j):
			break
		A[i],A[j] = A[j],A[i]
		if (A[i]==v):
			p = p+1
			A[p],A[i] = A[i],A[p]
		if (v==A[j]):
			q = q-1
			A[j],A[q] = A[q],A[j]
	A[i],A[r] = A[r],A[i]
	j,i = i-1, i+1
	for k in range(l,p):
			A[k],A[j] = A[j],A[k]
			j = j-1
	for k in range(r-1,q+1, -1):
		A[i],A[k] = A[k],A[i]
		i =i+1
	quicksort3wayp(A,l,j)
	quicksort3wayp(A,i,r)
	return A
	
def quicksort_3_wayp(A):
	lf = 0
	N = len(A)-1
	quicksort3wayp(A, lf, N)


################################################################################################
##########################      Dual pivot Quicksort    ########################################
################################################################################################

def quicksortyaroslavsky(A,lf,rg):
	M = len(A)
	if rg -lf  <= M:
		insertionsort(A,lf,rg)
	else:
		if A[lf] > A[rg]:
			p = A[rg]
			q = A[lf]
		else:
			p = A[lf]
			q = A[rg]
		l = lf+1
		g = rg-1
		k = l
		
		while k <= g:
			if A[k] < p:
				A[k],A[l] = A[l],A[k]
				l = l+1
			else:
				if A[k] >= q:
					while( (A[g] > q) and (k < g)):
						g = g-1
					if A[g] >= p:
						A[k],A[g] = A[g],A[k]
					else:
						A[k],A[g] = A[g],A[k]
						A[k],A[l] = A[l],A[k]
						l = l+1
					g = g-1
			k = k+1
		l = l-1
		g = g+1
		A[lf] = A[l]
		A[l] = p
		A[rg] = A[g]
		A[g] = q
		quicksortyaroslavsky(A,lf,l-1)
		quicksortyaroslavsky(A,l+1,g-1)
		quicksortyaroslavsky(A,g+1,rg)

def Dual_piv_Quicksort(A):
	lf = 0
	N = len(A)-1
	quicksortyaroslavsky(A,lf,N)
	return A







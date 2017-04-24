# Proyecto no.1
#
# Autores:
#		Jorge Sánchez 10-10673
#		Greanny Vivas 12-11167
#
import math
import random
from arrayT import ArrayT
import sys

# cambio de limite de recursiones
if __name__ == "__main__":	
  sys.setrecursionlimit(100000000)
 
# Insertion Sort

def insertion_sort1(a,l,r):
	n = len(a)
	for i in range (1,n):
		key = a[i]
		j = i-1
		while j >= 0 and a[j] > key:
			a[j+1] = a[j]
			j -= 1
		a[j+1] = key	
	return a


def insertion_sort(a):
	l = 0
	r = len(a)-1
	insertion_sort1(a,l,r)
	return a

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

# 	Funciones para Heapsort:
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

def heap_sort1(array,f,b):
    build_max_heap(array)
    for i in range (len(array)-1,0,-1):
        swap(array,0,i)
        heapify(array,0,i)
    return array

def heap_sort(array):
	f = 0
	b = len(array)
	heap_sort1(array,f,b)
	return array

def dequeue(array):
    assert ((len(array) < 2), "ERROR: El arreglo debe tener mas de un elemento")    
    aux_array =ArrayT(len(array)-1)
    for i in range (0,len(array)-1):
        aux_array[i] = array[i+1]  
    heapify(aux_array,0,len(aux_array))         
    return(array[0],aux_array)  

# Funciones para Quicksort aleatorio

def swap(array, i, j):
	array[j],array[i] = array[i],array[j]
	return array

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

# Aleatorio
	
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
	
def quicksort_aleatorio(A):
	rQuicksort(A,0,len(A)-1)
	return A	


# Funciones para Median of 3 Quicksort:
	
def median_of_three(a,b,c):
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c

    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c


def Partition(A,p,r,x):
 	i = p-1
 	j = r
 	while True:
 		while True:
 			j = j - 1
 			if A[j] <= x:
 				break
 		while True:
 			i = i + 1
 			if A[i] >= x:
 				break
 		if i < j:
 			swap(A,i,j)
 		else:
 			return j

def Quicksort_loop(A,f,b):
	while b-f > 10:
		m = median_of_three(A[f],A[f+(b-f)//2],A[b-1])
		p = Partition(A,f,b,m)
		if (p-f >= b-p):
			Quicksort_loop(A,p,b)			
			b = p
		else:
			Quicksort_loop(A,f,p)
			f = p
	else:
		insertion_sort1(A,f,b)
	return A,f,b

def MoT_Quicksort(A,f,b):
	Quicksort_loop(A,f,b)
	return A

def median_of_3_Quicksort(A):
	f = 0
	b = len(A)-1
	MoT_Quicksort(A,f,b)
	return A

# Funciones para Introsort:

def Introsort_loop(A,f,b,depth_limit):
	while (b-f > 10):
		if depth_limit == 0:
			heap_sort(A)
			return 
		depth_limit -= 1
		m = median_of_three(A[f],A[f+(b-f)//2],A[b-1])
		p = Partition(A,f,b,m)
		Introsort_loop(A,p,b,depth_limit)
		b = p
	return A

def Introsort1(A,f,b):
	k = b-f
	l = int(math.floor(math.log(k)))*2
	Introsort_loop(A,f,b,l)
	insertion_sort(A)

def Introsort(A):
	f = 0
	b = len(A)-1
	Introsort1(A,f,b)
	
# Funciones para Quicksort with 3-way partitioning:

def Threeway_quicksort(A,l,r):
	i,j = l-1, r
	p,q = l-1, r
	v = A[r]
	if r <= l:
		return 	
	while True:
		i += 1	
		while A[i] < v :
			i += 1
		j -= 1
		while  v < A[j]:
			if j == l:
				break
			j -= 1
		if i >= j:
			break
		swap(A,i,j)
		if A[i] == v:
			p += 1
			swap(A,p,i)
		if v == A[j]:
			q -= 1
			swap(A,j,q)
	swap(A,i,r)
	#j = i-1
	for k in range (l,p):
		swap(A,k,j)	
		j -= 1
	i += 1
	for k in range(r-1,q,-1):
		swap(A,i,k)
		i += 1
	Threeway_quicksort(A,l,j)
	Threeway_quicksort(A,i,r)
	return A


def Quicksort_3_way_partitioning(A):
	f = 0
	b = len(A)-1
	if b+1 - f <= 10:
		insertion_sort(A)
	else:
		Threeway_quicksort(A,f,b)
	return A

# Funciones para Dual pivot Quicksort:
def Dualpivot_quicksort2(A,left,right):
	if right - left > 10:
		if A[left] > A[right]:
			p,q = A[right],A[left]
		else:
			p,q = A[left],A[right]
		l= (left + 1)
		g = (right - 1) 
		k = l
		while k <= g:
			if A[k] < p:
				swap(A,k,l)
				l +=1
			else:
				if A[k] >= q:
					while A[g] > q and k < g:
						g -= 1
					if A[g] >= p:
						swap(A,k,g)
					else:
						swap(A,k,g)
						swap(A,k,l)
						l += 1
					g -= 1
			k += 1
		l -= 1
		g += 1
		A[left],A[l],A[right],A[g] = A[l],p,A[g],q
		Dualpivot_quicksort2(A,left,l-1)
		Dualpivot_quicksort2(A,l+1,g-1)
		Dualpivot_quicksort2(A,g+1,right)
	return A

def Dual_pivot_quicksort(A):
	f = 0
	b = len(A)-1
	Dualpivot_quicksort2(A,f,b)
	insertion_sort(A)
	return A

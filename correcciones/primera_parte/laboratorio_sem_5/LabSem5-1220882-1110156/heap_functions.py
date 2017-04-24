
""" Laboratorio 1 .algoritmos II .ene-mar 2017 
	fecha: 19/01/2017
   
	autores: Edymar Mijares 12-10882
	         Jose Carmona 11-10156

	correo: - edys.beccaria@gmail.com
		- carmona621@hotmail.com
ultima edicion :02/02/2017"""


from arrayT import ArrayT

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

def dequeue(array):
    assert(len(array) > 1)
    aux_array = ArrayT(len(array) - 1)
    for i in range(1,len(array)):
        aux_array[i - 1] = array[i]
    heapify (aux_array, 0,len(aux_array))
    return (array[0],aux_array)


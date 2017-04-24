from random import randint
from heap_functions import swap
from arrayT import ArrayT

def quicksort_basico(A):
    p=0
    r=len(A)-1
    B=quicksort_aux(A,p,r)
    return B

def quicksort_aux(A,p,r):
    if p<r:
        q=partition(A,p,r)
        A=quicksort_aux(A,p,q-1)
        A=quicksort_aux(A,q+1,r)
    return A
   
def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            A=swap(A,i,j)
    A=swap(A,i+1,r)
    return i+1

def quicksort_aleatorio(A):
    p=0
    r=len(A)-1
    B=rand_quicksort_aux(A,p,r)
    return B

def rand_quicksort_aux(A,p,r):
    if p<r:
        q=partition_aleatoria(A,p,r)
        A=rand_quicksort_aux(A,p,q-1)
        A=rand_quicksort_aux(A,q+1,r)
    return A

def partition_aleatoria(A,p,r):
    i=randint(p,r)
    A=swap(A,i,r)
    return partition(A,p,r)

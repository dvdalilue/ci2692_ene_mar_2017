
"""
funciones de ordenamiento Quicksort basico y Quicksort aleatorio

Autor: Edymar Mijares (12-10882) y Jose Carmona(11-10156)
Email: edys.beccaria@gmail.com y carmona621@hotmail.com
ultima modificacion : 09/02/2017
"""



#############importamos las librerias necesarias######################
import random
from arrayT import ArrayT
from heap_functions import heap_sort



############Quicksort version cormen########################3
def particion(A,p,r):
    x=A[r]
    i=p-1
    j=p
    for j in range(p,r):
        if A[j]<= x :
            i=i+1
            A[i],A[j]= A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return(i+1)

def Quicksort2(A,p,r):
    if p<r:
        q=particion(A,p,r)
        Quicksort2(A,p,q-1)
        Quicksort2(A,q+1,r)

def quicksort_basico(A):
    Quicksort2(A,0,len(A)-1)

################# randomized Quicksort###############3
def Randomized_partition(A,p,r):
    i= random.randint(p,r)
    A[i],A[r]=A[r],A[i]
    return particion(A,p,r)



def Randomized_Quicksort2(A,p,r):
    if p<r:
        q= Randomized_partition(A,p,r)
        Randomized_Quicksort2(A,p,q-1)
        Randomized_Quicksort2(A,q+1,r)

def quicksort_aleatorio(A):
    Randomized_Quicksort2(A,0,len(A)-1)



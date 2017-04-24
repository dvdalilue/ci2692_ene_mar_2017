from heap_functions import swap
from arrayT import ArrayT
from random import randint
import sys

sys.setrecursionlimit(1000000000) #Limite recursivo cambiado de 1000 a 1000000000

def merge_sort(lista):
#    """
#    Ordenamiento por medio del algoritmo de Merge Sort
#
#    Parametros:
#        a: Un arreglo a ordenar
#        p: Primer indice del arreglo
#        r: Ultimo indice del arreglo
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
    
    #Copia de z
   
    k = 1
    n = len(lista)
    h = ArrayT(n)
    for i in range(n):
        h[i] = lista[i]
    while k < n:
        a,b,c = 0,k,min([(2*k),n])
        while b < n:
            p,q,r = a,b,a
            while p!=b and q!=c:
                if h[p] <= h[q]:
                    lista[r] = h[p]
                    r += 1
                    p += 1
                else:
                    lista[r] = h[q]
                    r += 1
                    q += 1
            while p != b:
                lista[r] = h[p]
                r += 1
                p += 1
            while q!= c:
                lista[r] = h[q]
                r += 1
                q += 1
            r = a
            while r != c:
                h[r] = lista[r]
                r += 1
            a,b,c = a+2*k, b+2*k, min([(c+2*k),n])
        k = k*2
    return lista


def quicksort_dual_pivot_final(A):
	left=0
	right=len(A)-1
	A=Quicksort_dual_pivot(A,left,right)
	return A

def Quicksort_dual_pivot(A,left,right):
#    """
#    Ordenamiento por medio del algoritmo de Quicksort com pivote dual
#
#    Parametros:
#        A: Un arreglo a ordenar
#		 left: Indice del primer elemento del subarreglo a considerar
#		 right: Indice del elemento inmediatamente despues del final del subarreglo
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
	if right-left<11:
		#En arreglos de tamaño menores o iguales a 10, el algoritmo de
		#ordenamiento que implementara sera insertionsort.
		A=insertion_sort(A,left,right+1)
	else:
		#En arreglos de tamaño mayor estricto a 10, se aplicara quicksort
		#como sigue
		if A[left]>A[right]:
			p,q=A[right],A[left]
		else:
			p,q=A[left],A[right]
		l,g=left+1,right-1
		k=l
		while k<=g:
			if A[k]<p:
				A=swap(A,k,l)
				l+=1
			else:
				if A[k]>=q:
					while A[g]>q and k<g:
						g-=1
					if A[g]>=p:
						A=swap(A,k,g)
					else:
						A=swap(A,k,g)
						A=swap(A,k,l)
						l+=1
					g-=1
			k+=1
		l-=1
		g+=1
		A[left],A[l],A[right],A[g]=A[l],p,A[g],q
		A=Quicksort_dual_pivot(A,left,l-1)
		A=Quicksort_dual_pivot(A,l+1,g-1)
		A=Quicksort_dual_pivot(A,g+1,right)
	return A

def insertion_sort(a,f,b):
#    """
#    Ordenamiento por medio del algoritmo de Insertion
#
#    Parametros:
#        a: Un arreglo a ordenar
#		 f: Indice del primer elemento del arreglo
#		 b: Indice del elemento inmediatamente despues del final del arreglo
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
    for j in range(f,b):
        key=a[j]
        i=j-1
        while i>=0 and a[i]>key:
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key
    return a

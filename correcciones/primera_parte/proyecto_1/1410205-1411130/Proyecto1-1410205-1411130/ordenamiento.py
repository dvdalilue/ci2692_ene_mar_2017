"""
# Descripcion: Modulo con la implementacion de algoritmos de ordenamientos
#              que son aplicados sobre listas de elementos de tipo numerico
# Autor: Aurivan Castro, Sandra Vera
# email: 14-10205@usb.ve, 14-11130@usb.ve
"""
import sys, math
from arrayT import ArrayT
from random import randint





"""
		#####################

			 MERGESORT

		#####################
"""

def merge_sort(lista):
#    """
#    Ordenamiento por medio del algoritmo de Merge Sort
#
#    Parametros:
#        lista: Un arreglo a ordenar
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




"""
		#####################

			  HEAPSORT

		#####################
"""

def heapify(array, i, lenght):
#    """
#    Funcion que mantiene la propiedad del heap en el algoritmo de 
#		Heapsort
#
#    Parametros:
#        array: Un arreglo a ordenar
#        i: Indice en el cual se establece el heap del arreglo
#        lenght: Largo del arreglo a ordenar
#    """
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
	

def build_max_heap(array,f,b):
#    """
#    Funcion que establece el heap maximo en un arreglo entre dos indices
#
#    Parametros:
#        array: Un arreglo a ordenar
#        f: Primer indice del arreglo
#        b: Indice del primer elemento despues del final del arreglo
#    """	
	i=b//2
	while i>=f:
		array=heapify(array,i,b)
		i-=1
	return array

def heap_sort(array,f,b):
#    """
#    Funcion auxiliar para el ordenamiento por medio del algoritmo de Heap Sort
#
#    Parametros:
#        array: Un arreglo a ordenar
#        f: Primer indice del arreglo
#        b: Indice del primer elemento despues del final del arreglo
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
	array=build_max_heap(array,f,b)
	i=b-1
	while i!=f:
		array=swap(array,f,i)
		array=heapify(array,f,i)
		i-=1
	return array

def heap_sort_final(array):
#    """
#    Ordenamiento por medio del algoritmo de Heap Sort
#
#    Parametros:
#        array: Un arreglo a ordenar
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
	f=0
	b=len(array)
	array=heap_sort(array,f,b)
	return array

def swap(array, i, j):
#    """
#    Funcion que intercambia dos elementos de un arreglo
#
#    Parametros:
#        array: Un arreglo a ordenar
#        i: Primer indice a intercambiar
#        r: Segundo indice a intercambiar
#    """
	array[i],array[j]=array[j],array[i]
	return array

def left(i):
#    """
#    Funcion que dado un indice i, retorna su hijo izquierdo del heap
#
#    Parametros:
#        i: Indice del elemento padre en el heap
#    """
	return (2*(i))

def right(i):
#    """
#    Funcion que dado un indice i, retorna su hijo derecho del heap
#
#    Parametros:
#        i: Indice del elemento padre en el heap
#    """	
	return (2*(i)+1)




"""
		############################

			 QUICKSORT ALEATORIO

		############################
"""

def quicksort_aleatorio(A):
#    """
#    Ordenamiento por medio del algoritmo de Quicksort Randomizado
#
#    Parametros:
#        A: Un arreglo a ordenar
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """	
    p=0
    r=len(A)-1
    B=rand_quicksort_aux(A,p,r)
    return B

def rand_quicksort_aux(A,p,r):
#    """
#    Funcion auxiliar para el ordenamiento por medio del algoritmo de 
#		Quicksort Randomizado
#
#    Parametros:
#        A: Un arreglo a ordenar
#        p: Primer indice del arreglo
#        r: Ultimo indice del arreglo
#    """
    if p<r:
        q=partition_aleatoria(A,p,r)
        A=rand_quicksort_aux(A,p,q-1)
        A=rand_quicksort_aux(A,q+1,r)
    return A

def partition_aleatoria(A,p,r):
#    """
#    Funcion que realiza una particion sobre un arreglo usando un elemento
#		aleatorio del arreglo como pivote
#
#    Parametros:
#        A: Arreglo a particionar
#        p: Primer indice del arreglo
#        r: Ultimo indice del arreglo
#    """
    i=randint(p,r)
    A=swap(A,i,r)
    p=partition(A,p,r)
    return p

def partition(A,p,r):
#    """
#    Funcion que realiza una particion sobre un arreglo usando el ultimo
#		elemento del arreglo como pivote
#
#    Parametros:
#        A: Arreglo a particionar
#        p: Primer indice del arreglo
#        r: Ultimo indice del arreglo
#    """
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            A=swap(A,i,j)
    A=swap(A,i+1,r)
    return i+1




"""
		##############################

			 MEDIAN-OF-3 QUICKSORT

		##############################
"""

def insertion_sort(A,f,b):
#    """
#    Ordenamiento por medio del algoritmo de Insertion Sort
#
#    Parametros:
#        A: Un arreglo a ordenar
#		 f: Indice del primer elemento del arreglo
#		 b: Indice del primer elemento despues del final del arreglo
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
	for j in range(f+1,b):	#Porque sino descarta el ultimo numero
		key=A[j]
		k=j-1
		while k>=0 and A[k]>key:
			A[k+1]=A[k]
			k=k-1
		A[k+1]=key
	return A

def partition_median(A,p,r,x):
#    """
#    Funcion que realiza una particion usando como pivote el elemento x
#		del arreglo (en este caso la media del primer elemento, el ultimo
#		elemento y el elemento dela mitad del arreglo)
#
#    Parametros:
#        A: Un arreglo a ordenar
#		 p: Indice del primer elemento del arreglo
#		 r: Indice del ultimo elemento del arreglo
#		 x: Pivote a utilizar para particionar el arreglo
#    """	
	i=p	#El arreglo empieza en 0, por lo que si se le resta 1, esta fuera de rango
	j=r
	while True:
		while True:  
			j=j-1
			if A[j]<=x:
				break
		while True:
			i=i+1
			if A[i]>=x:
				break
		if i<j:
			A[i],A[j]=A[j],A[i]
			if A[i]==A[j]:
				i=i+1
				j=j-1
		
		else:
			return j
	

def median_of_3(a,b,c):
#    """
#    Funcion que encuentra la media de 3 elementos
#
#    Parametros:
#        a: Primer numero
#		 b: Segundo numero
#		 c: Tercer numero
#    """
	if a<=b<=c or c<=b<=a:
		return b
	elif b<=a<=c or c<=a<=b:
		return a
	else:
		return c

def Median_of_3_Quicksort(A,f,b):
#    """
#    Funcion auxiliar para el ordenamiento por medio del algoritmo de 
#		Quicksort que toma la media de 3 elementos del arreglo
#
#    Parametros:
#        A: Un arreglo a ordenar
#		 f: Indice del primer elemento del arreglo
#		 b: Indice del primer elemento despues del final del arreglo
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
	quicksort_loop(A,f,b)
	insertion_sort(A,f,b)
	return A

def Median_of_3_Quicksort_Final(A):
#    """
#    Ordenamiento por medio del algoritmo de Quicksort que toma la media
#		de 3 elementos del arreglo
#
#    Parametros:
#        A: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
	f=0
	b=len(A)
	A=Median_of_3_Quicksort(A,f,b)
	return A

def quicksort_loop(A,f,b):
#    """
#    Funcion que ordena los elementos de un arreglo hasta que los elementos
#		 a ordenar son menores que 10
#
#    Parametros:
#        A: Un arreglo a ordenar
#		 f: Indice del primer elemento del arreglo
#		 b: Indice del primer elemento despues del final del arreglo
#    """
	while b-f>10:
		p=partition_median(A,f,b,median_of_3(A[f],A[f + (b-f)//2],A[b-1]))
		if (p-f)>=(b-p):
			quicksort_loop(A,p,b)
			b=p
		else:
			if f==p:
				break
			else:
				quicksort_loop(A,f,p)
				f=p




"""
		#####################

			 INTROSORT

		#####################
"""

def Introsort_aux(A,f,b):
#    """
#    Funcion auxiliar para el ordenamiento por medio del algoritmo de 
#		Introsort
#
#    Parametros:
#        A: Un arreglo a ordenar
#		 f: Indice del primer elemento del arreglo
#		 b: Indice del primer elemento despues del final del arreglo
#    """
	Introsort_loop(A,f,b,2*(math.floor(math.log((b-f),math.e))))
	insertion_sort(A,f,b)
	return A

def Introsort(A):
#    """
#    Ordenamiento por medio del algoritmo de Introsort
#
#    Parametros:
#        A: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
	f=0
	b=len(A)
	A=Introsort_aux(A,f,b)
	return A

def Introsort_loop(A,f,b,depth_limit):
#    """
#    Funcion que ordena los elementos de un arreglo hasta que la profundidad 
#		de la recursion excede el limite establecido
#
#    Parametros:
#        A: Un arreglo a ordenar
#		 f: Indice del primer elemento del arreglo
#		 b: Indice del primer elemento despues del final del arreglo
#		 depth_limit: Limite de la profundidad de la recursion
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
	while b-f>10:
		if depth_limit==0:
			A=heap_sort(A,f,b)
			return A
			break
		depth_limit=-1
		p=partition_median(A,f,b,median_of_3(A[f],A[f+((b-f)//2)],A[b-1]))
		Introsort_loop(A,p,b,depth_limit)
		b=p




"""
		###########################################

			 QUICKSORT WITH 3-WAY PARTITIONING

		###########################################
"""

def quicksort_with_three_way_partition(A):
#    """
#    Ordenamiento por medio del algoritmo de Quicksort With Three Way 
#		Partition
#
#    Parametros:
#        A: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
	l=0
	r=len(A)-1
	A=quicksort_with_three_way_part(A,l,r)
	return A

def quicksort_with_three_way_part(A,l,r):
#    """
#    Funcion auxiliar para el ordenamiento por medio del algoritmo de 
#		Quicksort With Three Way Partition.
#
#    Parametros:
#        A: Un arreglo a ordenar
#		 l: Indice del primer elemento del arreglo
#		 r: Indice del último elemento del arreglo
#    """	
	i=l-1
	j,p,q=r,i,r
	if r<=l and r - l > 0:
		return A
	elif r - l <= 10:
		A=insertion_sort(A,0,len(A))
		return A
	v=A[r]
	while True:
		i+=1
		while A[i]<v:
			i+=1
		j-=1
		while v<A[j]:
			if j==0:
				break
			j-=1
		if i>=j:
			break
		A=swap(A,i,j)
		if A[i]==v:
			p+=1
			A=swap(A,p,i)
		if v==A[j]:
			q-=1
			A=swap(A,j,q)
	A=swap(A,i,r)
	j=i-1
	i+=1
	k=l
	while k<p:
		A=swap(A,k,j)
		k+=1
		j-=1
	k=r-1
	while k>q:
		A=swap(A,i,k)
		k-=1
		i+=1
	A=quicksort_with_three_way_part(A,l,j)
	A=quicksort_with_three_way_part(A,i,r)
	return A




"""
		##############################

			 DUAL PIVOT QUICKSORT

		##############################
"""

def quicksort_dual_pivot_final(A):
#    """
#    Ordenamiento por medio del algoritmo de Quicksort Dual Pivot (Pivote Dual)
#
#    Parametros:
#        A: Un arreglo a ordenar
#
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
	left=0
	right=len(A)-1
	A=Quicksort_dual_pivot(A,left,right)
	return A

def Quicksort_dual_pivot(A,left,right):
#    """
#    Funcion auxiliar para el ordenamiento por medio del algoritmo de 
#		Quicksort Dual Pivot (Pivote Dual)
#
#    Parametros:
#        A: Un arreglo a ordenar
#		 left: Indice del primer elemento del subarreglo a considerar
#		 right: Indice del elemento inmediatamente despues del final del subarreglo
#    """
	if right-left<11:
		#En arreglos de taman~o menores o iguales a 10, el algoritmo de
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

"""
# Descripcion: Modulo con la implementacion de algoritmos de ordenamientos
#              de quicksort basico y quicksort randomizado
# Autor: Orlando Chaparro Carnet: 12-11499
         Angel Morante Carnet: 13-10931
# email: 12-11499@usb.ve
         13-10931@usb.ve // morante413@gmail.com

"""
import random
from arrayT import ArrayT


#######################################
###### Particion del Quicksort#########
#######################################
                  
def Partition_Quicksort(A, p, r):
	x = A[r]
	i = p - 1
	for j in range(p, r):
		if A[j] <= x:
			i = i + 1
			A[i],A[j] = A[j],A[i]
	A[i + 1],A[r] = A[r],A[i+1]
	
	return(i + 1)

#######################################
######   QUICKSORT BASICO      ########
#######################################

def quicksort_basico(A, p, r):
	
	#procedimiento que recibe un arreglo A de 
	#tipo arrayT y ordena sus elementos con la 
	#implementacion de esta version 
	#de Quicksort.
	if p<r:
		q = Partition_Quicksort(A, p, r)
		quicksort_basico(A, p, q - 1)
		quicksort_basico(A, q + 1, r)
	
#################################################
###### Particion del Quicksort aleatorio#########
#################################################

def randomized_Partition(A, p, r):
	i = random.randint(p, r)
	A[r],A[i] = A[i],A[r]
	
	return Partition_Quicksort(A, p, r)


#######################################
###### QUICKSORT ALEATORIO    #########
#######################################
	
def quicksort_aleatorio(A, p, r):
	
	#funcion que
	#recibe un arreglo A de tipo arrayT y 
	#ordena sus elementos con la implementacion
	#de la version aleatoria de Quicksort.
	
	if p < r:
		q = randomized_Partition(A, p, r)
		quicksort_aleatorio(A, p, q - 1)
		quicksort_aleatorio(A, q + 1, r)

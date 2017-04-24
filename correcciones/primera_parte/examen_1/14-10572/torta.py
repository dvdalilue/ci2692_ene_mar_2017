# Examen
# Yeferson Licet
# 14-10572

# Constantes
from arrayT import ArrayT
import random as rn

EXISTS_STR 	= "Si"
DESCENDENT 	= 0
ASCENDENT 	= 1

def partition(A,p,r,method, index):
    x = A[r][index]
    i = p-1
    for j in range(p,r):
        
        if (index > 0 and method == DESCENDENT and A[j][index] >= x) or (index == 0 and method == DESCENDENT and A[j][index].lower() >= x):
            i = i+1
            A[i], A[j] = A[j], A[i]
        
        if (index > 0 and method == ASCENDENT and A[j][index] <= x) or (index == 0 and method == ASCENDENT and A[j][index].lower() <= x):
            i = i+1
            A[i], A[j] = A[j], A[i]   

    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort(A, method, index):
    randomized_quicksort(A,0,len(A)-1, method, index)

def randomized_partition(A, p , r, method, index):
    i = rn.randint(p,r)
    A[r], A[i] =  A[i], A[r]
    return partition(A, p , r, method, index)

def randomized_quicksort(A, p ,r, method, index):
    if p<r:
        q = randomized_partition(A,p,r, method, index)
        randomized_quicksort(A,p,q-1, method, index)
        randomized_quicksort(A,q+1,r, method, index)

print("Leyendo archivo: ingredientes.txt")
# Leo el archivo de mensajes
try:
	file = open("ingredientes.txt", "r")
except:
	print("Occurio un error al leer el archivo")

indexLine = 0

for line in file:
	if indexLine == 0:
		grouped = ArrayT(int(line))
	else:
		lineArray = line.split("\t")
		
		grouped[indexLine-1] = ArrayT(3)
		grouped[indexLine-1][0] = lineArray[0]
		grouped[indexLine-1][1] = lineArray[1]
		
		exists = 0
		if lineArray[2].strip("\n") == EXISTS_STR:
			exists = 1
		grouped[indexLine-1][2] = exists

	indexLine = indexLine +1


# Ordenar por los ingredientes que si se poseen :
# Donde index = 2, para ingredientes
# Donde 1 = Si, por lo tanto ordeno de forma DESCENDENT
quicksort(grouped, DESCENDENT, 2)

# Esta funcion deberia ordenar los elementos repetidos comparados usando indexCheck
# Utilizando como parametro para ordenar indexSort
def superSort(A, method, indexCheck, indexSort):
	i = 0
	while i < len(A)-1:
		if (indexCheck == 0 and A[i][indexCheck].lower() == A[i+1][indexCheck].lower()) or (indexCheck > 0 and A[i][indexCheck] == A[i+1][indexCheck]):
			j = i + 1
			
			try:
	
				while (indexCheck == 0 and A[i][indexCheck].lower() == A[j+1][indexCheck].lower()) or (indexCheck > 0 and A[i][indexCheck] == A[j+1][indexCheck]):
					j = j + 1
				
				auxA = ArrayT(j-i+1)

				for k in range(j-i+1):
					auxA[k] = A[i+k]

				quicksort(auxA, method, indexSort)
				
				for k in range(j-i+1):
					A[i+k] = auxA[k]
			except:
				pass
			i = j + 1
		else:
			i = i + 1

# Llama Super sort para ordenar por numero de ingrediente
#superSort(grouped, DESCENDENT, 2, 1)

# Llama Super sort para ordenar por nombre
#superSort(grouped, DESCENDENT, 1, 0)

#Sin embargo tengo un problema con los indices dentro de superSort.
print(grouped)
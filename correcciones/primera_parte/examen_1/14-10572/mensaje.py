# Examen
# Yeferson Licet
# 14-10572

# Constantes
from arrayT import ArrayT
STAR = "*"

# Funciones para cola de prioridades
def heapify(array, i, length):
	left_child  = left(i)
	right_child = right(i)

	father = i

	if left_child < length and array[left_child] > array[i]:
		father = left_child

	if right_child < length and array[right_child] > array[father]:
		father = right_child

	if father != i:
		swap(array, father, i)
		heapify(array, father, length)


def build_max_heap(array):
	n = len(array)
	for i in range(0,n//2+1):
		heapify(array,(n // 2) - i, n)

def heap_sort(array):
	build_max_heap(array)

	n = len(array)
	for i in range(1,n):
		swap(array,0,n-i)
		heapify(array, 0, n-i)
		
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]

# Modificado para funcionar con a*b*
def dequeue(array):
	if len(array) < 1:
		print("El arreglo debe tener mas de un elemento")
	
	if len(array)-1 > 0:
		aux_array = ArrayT(len(array)-1)
		for i in range(1,len(array)):
			aux_array[i-1] = array[i]
		heapify(aux_array,0, len(aux_array))
	else:
		aux_array = -1

	return (array[0], aux_array)

def parent(i):
	return  ((i + 1) // 2) - 1

def left(i):
	return (2*(i+1)-1)

def right(i):
	return (2*(i+1))

# Copia y aumenta en 1 el tamanio de Array
def copyExtended(array):
	if len(array) < 1:
		print("El arreglo debe tener mas de un elemento")
	aux_array = ArrayT(len(array)+1)
	for i in range(0,len(array)):
		aux_array[i] = array[i]
	
	return aux_array

print("Leyendo archivo: mensajes.txt")
# Leo el archivo de mensajes
try:
	file = open("mensajes.txt", "r")
except:
	print("Occurio un error al leer el archivo")

lines = 0
for line in file:
	message 	= line.strip("\n")
	messageLen 	= len(message)
	messageT 	= ArrayT(1)

	if message[0] != STAR:
		messageT[0] = message[0]

	result = ""
	i = 1
	while i < messageLen:
		if message[i] == STAR:
			(letter, messageT) = dequeue(messageT)
			
			if messageT != -1 and len(messageT) > 0:
				heap_sort(messageT)	
				result = result + letter
			else:
				result = result + letter
				
				if i+1 < messageLen:
					messageT 	= ArrayT(1)
					messageT[0] = message[i+1]
					i = i + 1
		else:
			temp = copyExtended(messageT)
			temp[len(messageT)] = message[i]
			heap_sort(temp)
			messageT = temp
		i = i+1

	print("El mensaje ",lines," descifrado es: ", result)
	lines = lines +1

file.close()
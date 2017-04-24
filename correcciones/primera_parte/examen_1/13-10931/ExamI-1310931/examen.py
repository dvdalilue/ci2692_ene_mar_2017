from colaprioridad import colaprioridad
from arrayT import ArrayT
from heap_functions import heap_sort

# AUTOR: ANGEL MORANTE

def heapsort(self,A):
	self.buildHeap(A)
	for i in range(len(A)-1, 0, -1):
		A[0][1], A[i][1] = A[i][1], A[0][1]
		self.heapify(A, 0, i)

def buildHeap(self,A):
	for i in range(len(A)//2-1, -1, -1):
		self.heapify(A,i,len(A))

def heapify(self, A, idx, m):
	largest = idx
	left = 2*idx+1
	right = 2*idx+2
	if(left < m and A[left][1] > A[idx][1]):
		largest = left
	if(right < m and A[right][1] > A[largest][1]):
		largest = right
	if(largest != idx):
		A[idx][1], A[largest][1] = A[largest][1], A[idx][1]
		self.heapify(A, largest, m)


Cola=colaprioridad()


f = open('mensaje_secreto.txt', 'r+')

g = open('mensaje_revelado.txt', 'w')

ff = f.readline()

n = len(ff)

arreglo = ArrayT(n)
for i in range(0,n):
	arreglo[i]=ff[i]

heap_sort(arreglo)

#for i in range(0,n):
#	print arreglo[i]

arreglo2 = ArrayT(n)
for i in range(0,n):
	if arreglo[i] != '*':
		arreglo2[i]=arreglo[i]

for i in range(0,n):
	print arreglo2[i]

for i in range(0,n):
	if arreglo2[i]!=None:
		Cola.agregarElem(arreglo2[i],i)
		
Cola.mostrar()


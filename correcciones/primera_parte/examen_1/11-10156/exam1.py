#Nombre Jose Carmona
#carnet 1110156

def procesar_archivo(nombre_archivo):
	letra = []
	with open(nombre_archivo, "r") as fd:   # Se abre el archivo para lectura
		S=fd.readlines()
		           # Se elimina el salto-de-linea al final de la linea
		for line in S:                     # Se lee linea por linea
			line = line.rstrip() 
			while True:
				letra = fd.read(1)
				let = letra[0]
				letra.append(letra)
				if not letra:
					break
			
	return letra      # Se retornan los arreglos





#Definimos funcion para escritura de archivos
def escritura(nombre_archivo, A):
	with open(nombre_archivo, "w") as fd:
			for i in range(0,len(AI)):
				fd.write(AI[i] +"\n")
			fd.write("\n\n")
			
			fd.closed


def parent(i):
	return((i+1) // 2)-1
	
def left(i):
	return (2*(i + 1)-1)

def right(i):
	return (2*(i + 1))
	
def heapify(A,i,N):
	L = left(i)
	R = right(i)
	M = i
	
	if L < N and A[L] > A[i]:
		M = L
	if R < N and A[R] > A[M]:
		M = R
	if M != i:
		swap(A,M,i)
		heapify(A,M,N)

def build_max_heap(A):
	N = len(A)
	for i in range (N // 2):
		heapify(A,i,N)

def heap_sort(A):
	build_max_heap(A)
	N = len(A)-1
	for i in range (N,0,-1):
		swap(A,0,i)
		heapify(A,0,i)

class Cola:
	def __init__(self):
		pass
	def Crearcola(self):
		self.cola = []

	def eliminar(self):
		self.cola = []
		
	def agregarElem(self, p, k):
		if len(self.cola) == 0:
			self.cola.append(p)
		else:
			self.cola.append(p)
			heapify(self.cola, k, len(self.cola))
									
		
	def ExtraerMax(self):
		N = len(self.cola)-1
		if N < 0:
			return
		maxx = self.cola[0]
		self.cola[0] = self.cola[N]
		N = N-1
		heapify(self.cola, 0, N)
		return maxx

	def ConsultarMax(self):
		return self.cola[0]
		
	




####################
####################
#      Main
####################
####################


# L = Arreglo de la información con los caracateres

if __name__ == "__main__":
	
	L = procesar_archivo("men.txt")     #Procedemos a abrir el archivo y almacenar en arreglos la informacion de la entrada
	heap_sort(L)
	

                               #Ordenamos en orden alfabético usando MergeSort el arreglo de los libros con Autores en primera posición                                 #Ordenamos en orden alfabético usando MergeSort el arreglo de los libros con el Título en primera posición
	escritura("salida.txt", L)
	
	
	



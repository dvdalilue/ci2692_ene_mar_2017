#Definimos funcion para lectura de archivos

def procesar_archivo(nombre_archivo):
	arringredientes = []
	arrcantidad = []
	arrexiste = []
	with open(nombre_archivo, "r") as fd:   # Se abre el archivo para lectura
		S=fd.readlines()
		S.remove(S[0])                      #Remueve la linea 0
		for line in S:                      # Se lee linea por linea
			line = line.rstrip()            # Se elimina el salto-de-linea al final de la linea
			tok = line.split("\t")          # Se parte la linea en el caracter tabulador [TAB]
			ingrediente = tok[0]                  # Se obtiene el nombre del autor
			cantidad = tok[1]	                # Se obtiene el nombre del libro
			existe = tok[2]				#Se obtiene si existe el ingrediente
			arringredientes.append(ingrediente)          # Se agrega la tupla al arreglo de autores
			arrcantidad.append(cantidad)         # Se agrega la tupla al arreglo de libros
			arrexiste.append(existe)         # Se agrega la tupla al arreglo de libros

	return arringredientes, arrcantidad, arrexiste      # Se retornan los arreglos





#Definimos funcion para escritura de archivos
def escritura(nombre_archivo, AI, AC, AE):
	with open(nombre_archivo, "w") as fd:
			for i in range(0,len(AI)):
				fd.write(AI[i] + "\t" + AC[i] + "\t" + AE[i] +"\n")
			fd.write("\n\n")
			
			fd.closed

#Funcion de ordenamiento

def mergesort(A,B,C):
	k = 1
	N = len(A)
	Z = []
	X = []
	Y = []
	x = 0
	X = []
	while k < N:
		a,b,c = 0,k,min((2*k),N)
		while b < N:
			for i in range(a,c):
				Z.append("")
				X.append("")
				Y.append("")
			p,q,r = a,b,a
			while (p != b) and (q != c):
				if (C[q] <= C[p]) and (B[q] <= B[p]):
					
					if (A[q] <= A[p]):
						Z[r] = A[p]
						X[r] = B[p]
						Y[r] = C[p]
						r = r+1
						p = p+1
					else:	
						Z[r] = A[p]
						X[r] = B[p]
						Y[r] = C[p]
						r = r+1
						p = p+1
						
				elif (C[p] <= C[q]) and (B[p] <= B[q]):
								
					Z[r] = A[q]
					X[r] = B[q]
					Y[r] = C[q]
					r = r+1
					q = q+1
			
			while p != b:
				Z[r] = A[p]
				X[r] = B[p]
				Y[r] = C[p]
				r = r+1
				p = p+1
			while q != c:
				Z[r] = A[q]
				X[r] = B[q]
				Y[r] = C[q]
				r = r+1
				q = q+1
			r = a
			while r != c:
				A[r] = Z[r]
				B[r] = X[r]
				C[r] = Y[r]
				r = r+1
			a,b,c = a+2*k,b+2*k,min((c+2*k),N)
		k = k*2
	for i in range(0,N-1):
		if C[i] == 'Si':
			x = x + 1
	if x > N//2:
		print("La torta se puede preparar")
	else:	
		print("La torta no se puede preparar")
	return (A,B,C)



####################
####################
#      Main
####################
####################

# AI = Arreglo de la información con los ingredientes
# AC = Arreglo de la informacion de la cantidad
# AE = Arerglo de la informacion si existe

if __name__ == "__main__":
	
	AI , AC, AE = procesar_archivo("ing.txt")     #Procedemos a abrir el archivo y almacenar en arreglos la informacion de la entrada
	mergesort(AI,AC,AE)                                #Ordenamos en orden alfabético usando MergeSort el arreglo de los Ingredientes de primera posición                                 
	escritura("salida.txt", AI, AC, AE)
	
	
	

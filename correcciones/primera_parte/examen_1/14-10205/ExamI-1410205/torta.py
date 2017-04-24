#Aurivan Castro carne 14-10205

from arrayT import ArrayT


def swap(array, i, j):
	#Cambia de lugar los elementos de indices i y j dentro del arreglo array
	array[i],array[j]=array[j],array[i]
	return array

def orden_si_no_existencia(n,p):
	#Indica cual es el mayor segun Si, o No, de los elementos en las posiciones n y p
	Mayor=None
	if "S" in n and "N" in p:
		Mayor=n
	elif "S" in p and "N" in n:
		Mayor=p
	elif ("S" in n and "S" in p) or ("N" in n and "N" in p):
		pass
	return Mayor

def Chequear_si_ordenado_por_existencia(A):
	#Verifica si el arreglo esta ordenado por existencia
	Ordenado=True
	for i in range(len(A)):
		for j in range(len(A)):
			Mayor=orden_si_no_existencia(A[i][2],A[j][2])
			if Mayor==A[i][2] and i>j:
				Ordenado=False
				break
	return Ordenado

def Chequear_orden_cantidades(array):
	#Verifica si el arreglo esta ordenado por cantidad de ingredientes
	Ordenado=True
	for i in range(len(array)):
		for j in range(len(array)):
			if array[i][1]<array[j][1] and i<j:
				Ordenado=False
	return Ordenado


def Orden_existencia(A):
	#Ordena el arreglo segun la existencia del ingrediente
	for i in range(len(A)):
		for j in range(len(A)):
			Mayor=orden_si_no_existencia(A[i][2],A[j][2])
			if (Mayor==A[i][2] and i>j) or (Mayor==A[j][2] and j>i):
				A=swap(A,i,j)
			if Mayor==None:
				pass
	Ordenado=Chequear_si_ordenado_por_existencia(A)
	if not Ordenado:
		A=Orden_existencia(A)
	return A

def Conseguir_indice_primer_elemento_No_existe(A):
	#Consigue el indice donde se encuentra el primer elemento que no se posee
	elemento=None
	for i in range(len(A)):
		if A[i][2]=="No":
			elemento=i
			break
	return elemento

def Orden_por_cantidad(A):
	#Ordena el arreglo por cantidades
	indice=Conseguir_indice_primer_elemento_No_existe(A)
	numero_elementos_existentes=0
	if indice!=None:
		numero_elementos_existentes=indice
		A=Orden_Cantidad_comparando(A,0,indice-1)
		A=Orden_Cantidad_comparando(A,indice,len(A)-1)
	elif indice==None:
		numero_elementos_existentes=len(A)
		A=Orden_Cantidad_comparando(A,0,len(A)-1)
	return A,numero_elementos_existentes
	

def Orden_Cantidad_comparando(A,i,f):
	#Realiza comparaciones y cambios en el rango de la posicion i a la f dentro del arreglo A
	for i in range(i,f+1):
		for j in range(i,f+1):
			if (int(A[i][1])<int(A[j][1]) and i<j) or (int(A[i][1])>int(A[j][1]) and i>j):
				A=swap(A,i,j)
			if int(A[i][1])==int(A[j][1]) and i!=j:
				A=Orden_por_nombre(A,i,j)
	Ordenado=Chequear_orden_cantidades(A)
	if not Ordenado:
		A=Orden_Cantidad_comparando(A,i,f)
	return A

def Orden_por_nombre(A,i,p):
	#Ordena el arreglo por nombre de ser necesario
	if (A[i][0]>A[p][0] and i<p) or (A[i][0]<A[p][0] and i>p):
		A=swap(A,i,p)
	return A

def Leer_Input(file):
	#Lee los datos recibidos por input
	lineas=file.readlines()
	lines_tripletas=ArrayT(len(lineas))
	for m in range(len(lineas)):
		lineas[m]=lineas[m].split('\n')[0]
	for m in range(len(lineas)):
		lines_tripletas[m]=lineas[m].split()
	return lines_tripletas

def Analizar_input(lineas):
	#Analiza los datos obtenidos por medio de la funcion anterior
	datos=ArrayT(len(lineas)-1)
	for i in range(len(datos)):
		datos[i]=lineas[i+1]
	int_ingredientes_necesarios=int(lineas[0][0])
	datos_ordenados=Orden_existencia(datos)
	datos_ordenados,numero_elementos_existentes=Orden_por_cantidad(datos_ordenados)
	Puede_prepararse=True
	if numero_elementos_existentes<int_ingredientes_necesarios:
		Puede_prepararse=False
	return Puede_prepararse,datos_ordenados

def Ejecutar_y_output():
	#Ejecucion del programa entero
	with open('input_torta.txt','r') as f:
		lineas=Leer_Input(f)
	Puede_prepararse,datos_ordenados=Analizar_input(lineas)
	with open('output_torta.txt','w') as f:
		for i in datos_ordenados:
			f.write(i[0]+"	"+i[1]+"	"+i[2]+"\n")
		if Puede_prepararse:
			f.write("La torta se puede preparar.")
		if not Puede_prepararse:
			f.write("La torta no se puede preparar.")

Ejecutar_y_output()
#Despues de implementarlo se decubrio que para arreglos de tamaños mayores a 7 el algoritmo no es rapido
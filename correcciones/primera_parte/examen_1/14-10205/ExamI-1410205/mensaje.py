#Aurivan Castro carne: 14-1025

from arrayT import ArrayT
from heap_functions import heap_sort,dequeue


def Leer_Input(file):
	#Lee el mensaje dentro del archivo dado
	lineas=file.readlines()
	mensajes_codificados=ArrayT(len(lineas))
	for m in range(len(lineas)):
		lineas[m]=lineas[m].split('\n')[0]
		lineas[m]='.'.join(lineas[m])
		mensajes_codificados[m]=lineas[m].split('.')
	mensajes_codificados=mensajes_codificados[0]
	return mensajes_codificados

def Introducir_cola(mensajes_codificados):
	#Crea una cola de prioridades que va ordenando por medio de heapsort
	n=0
	for i in range(len(mensajes_codificados)):
		n+=1
		if mensajes_codificados[i]!="*":
			auxArray=ArrayT(n)
			if i==0:
				auxArray[0]=mensajes_codificados[0]
			if i!=0:
				for p in range(len(auxArray_second)):
					auxArray[p]=auxArray_second[p]
				auxArray[n-1]=mensajes_codificados[i]
				auxArray=heap_sort(auxArray)
			auxArray_second=ArrayT(len(auxArray))
			for i in range(len(auxArray)):
				auxArray_second[i]=auxArray[i]
		elif mensajes_codificados[i]=="*":
			if i==0:
				pass
			if i!=0:
				auxArray=ArrayT(len(auxArray_second)-1)
				for i in range(len(auxArray_second)-1):
					auxArray[i]=auxArray_second[i]
				auxArray_second=ArrayT(len(auxArray))
				for i in range(len(auxArray)):
					auxArray_second[i]=auxArray[i]
	#En la implementacion se encontro un error ya que eventualmente empieza a comparar nonetypes.
	#Conserva el heap hasta que llega al '*' dentro del mensaje, que provoca que deje de funcionar
	return auxArray

def Armar_mensaje(lista):
	#Arma el mensaje separado por letras dentro de la lista
	output=None
	for i in range(len(lista)):
		if i==0:
			output=lista[i]
		else:
			output=output+lista[i]
	return output

def Ejecutar_Programa():
	#Ejecuta el programa con todos sus componentes y escribe sobre un archivo .txt el output
	with open('mensaje_codificado.txt','r') as f:
		mensajes_codificados=Leer_Input(f)
	MensajeDecodificado=Introducir_cola(mensajes_codificados)
	output=Armar_mensaje(MensajeDecodificado)
	with open('mensaje_decodificado.txt','w') as f:
		f.write(output)

def imp(array):
	#Imprime el arreglo en consola
	for i in array:
		print(i)

Ejecutar_Programa()
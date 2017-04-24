"""DESCRIPCION: Los estudiantes del Laboratorio de Algoritmos II el día de San Valentín quieren
descifrar el mensaje secreto de un amigo/a especial. A medida que se lee el mensaje, cada letra
debe ser insertada en la cola de prioridades.

Autor: David Segura 13-11341
Email: 13-11341@usb.ve"""

from arrayT import ArrayT
from heap_functions import dequeue

archivo = input("Nombre del archivo(Debe terminar en .txt) = ")
lectura=open(archivo,"r")
x=lectura.readlines()
mensaje = ArrayT(len(x[0]))
for i in range(0,len(x[0])):
	mensaje[i]=x[0][i]

j=0
for x in mensaje:
	if x=="*":
		j += 1

mensaje_devuelto=ArrayT(j)
for x in mensaje_devuelto:
	print(x)


z=0
while z<=j:
	for x in mensaje:
		if x == "*":
			mensaje_devuelto[z] = dequeue(mensaje)[0]
			z += 1
			y=0
			for i in mensaje:
				if i != dequeue(mensaje)[0]:
					mensaje[y]=i
					y += 1
				else:
					p=0
					for x in mensaje:
						if x == "*":
							mensaje[p]="Z"
							mensaje[y]="Z"
							break
						p += 1
		else:
			break



	
"""
# Descripcion: Resolucion de mensaje cifrado del dia de los enamorados, ejercicio 1 de la prueba
# Autor: Jesus Kauze 
# email: 12-10273@usb.ve 
"""
from heap_functions import build_max_heap, dequeue, heapify, heap_sort
from arrayT import ArrayT

archivo = input("Nombre del archivo(Debe terminar en .txt) = ")
lectura=open(archivo,"r")
numero = lectura.readline()
entrada=numero
n=0
i=0
division=[]
nueva=[]
doble=False
una=False
for x in range(0,len(entrada)):
	division=[]	
	if entrada[x] == "*" and entrada[x-1] != "*":
		if x != len(entrada)-1: #pasa siempre q no sea el ultimo
			
			if entrada[x+1]=="*": #si el sig es *
				doble=True
				x=x+1
				while i < x-1:
					division.append(entrada[i])
					i=i+1
				i=i+2
				build_max_heap(division)
				heap_sort(division)
				nueva.append(division[0])

			elif entrada[x+1]!="*" and entrada[x-1] != "*":
				una=True
				while i < x:
					division.append(entrada[i])
					i=i+1
				i=i+1
				build_max_heap(division)
				heap_sort(division)
				nueva.append(division[0])
		else:
			while i < x:
				division.append(entrada[i])
				i=i+1
			build_max_heap(division)
			heap_sort(division)
			nueva.append(division[0])

	#if division == []:
		#pass
	#else:
	print(division)
	#if doble:
		#nueva.append(division[0])
		#nueva.append(division[1])
	#elif una:
		#nueva.append(division[0])
		#nueva.append(entrada[x-1])
		#n=n+1
doble=False
una=False
print(nueva)





""" Examen I .algoritmos II .ene-mar 2017 
	fecha: 16/02/2017
	autores: Edymar Mijares 12-10882
	correo: - edys.beccaria@gmail.com

	Ejercicio 1:Hacer un programa que descifre un mensaje en codigo
"""
from colaprioridad import Prioridad

#asigna la prioridad de cada letra
def prioridad(F):
	L=f
	if L=="A":
		priority=0
	elif  L=="B":
		priority=1
	elif  L=="C":
		priority=2
	elif  L=="D":
		priority=3
	elif L=="E":
		priority=4
	elif  L=="F":
		priority=5
	elif L=="G":
		priority=6
	elif  L=="H":
		priority=7
	elif  L=="I":
		priority=8
	elif L=="J":
		priority=9
	elif  L=="K":
		priority=10
	elif L=="L":
		priority=11
	elif  L=="M":
		priority=12
	elif  L=="N":
		priority=13
	elif L=="O":
		priority=14
	elif L=="P":
		priority=15
	elif L=="Q":
		priority=16
	elif L=="R":
		priority=17
	elif L=="S":
		priority=18
	elif L=="T":
		priority=19
	elif L=="U":
		priority=20
	elif L=="V":
		priority=21
	elif L=="W":
		priority=22
	elif L=="X":
		priority=23
	elif L=="Y":
		priority=24
	elif L=="Z":
		priority=25
	else:
		priority=26
	return priority

#abro el archivo e ingreso los datos de cada linea en un arreglo

def AbrirMensajeSEcreto():
	f= open('MensajeSecreto.txt', 'r')
	C = []
	for line in f:
    		C.append(line)
	f.close()
	return C
def insertarEncola(A):
	Cola=Prioridad()
	for i in A:
		p=prioridad(A[i])
		if A[i]=="*":
			Cola.extraerMin()
		else:
			Cola.aggElem(A[i],p)
	return Cola
def imprimir(A):
	s=open('salida.txt','w')
	for i in range (0,A):
		s.write(A[i])
	s.close()
			
################
D=AbrirMensajeSEcreto()
print(D)
Col=insertarEncola(D)
print(Col)
imprimir(Col)





from pathlib import Path
from cancion import Cancion
from lista import ListSort
from reproductor import Reproductor

from PyQt5.QtWidgets import *

import sys
import subprocess as sp
from arrayT import ArrayT

def merge_sort(A, _property):
	"""
	Implementacion del algoritmo Mergesort del libro 
	Programming: the derivation of algorithms de Kaldewaij.
	
	Parametros:
		A: Un arreglo a ordenar

	Efecto Secundario:
		El arreglo de entrada es ordenado en orden ascendente
	"""
	n = len(A)
	k = 1

	while k < n:
		a,b,c = 0, k, min((2*k),n)

		while b < n:
			p,q,r = a,b,a
			z = ArrayT(c)

			while p!= b and q != c:
				if _property == "artista":	
					if A[p].es_menor_artista(A[q]): 
						z[r] = A[p]
						r,p  = r+1, p+1
					else:
						z[r] = A[q]
						r,q  = r+1, q+1
				else:
					if A[p].es_menor_titulo(A[q]): 
						z[r] = A[p]
						r,p  = r+1, p+1
					else:
						z[r] = A[q]
						r,q  = r+1, q+1

			while p != b:
				z[r] = A[p]
				r,p = r+1, p+1

			while q != c:
				z[r] = A[q]
				r,q = r+1, q+1
			r = a

			while r != c:
				A[r] = z[r]
				r = r+1

			a,b,c = a+2*k,b+2*k, min((c+2*k), n)
		k = k*2

def Menu():
	print('1. Listar canciones')
	print('2. Agregar para sonar justo despues de la cancion actual')
	print('3. Agregar para sonar justo antes de la cancion actual')
	print('4. Ordenar lista de reproduccion por artista')
	print('5. Ordenar lista de reproduccion por titulo')
	print('6. Eliminar cancion por titulo')
	print('7. Mostrar opciones')
	print('8. Salir')

def opciones():
	while True:
		opcion = input('Escoja una opcion: ')
		if opcion=='1' or opcion=='2' or opcion=='3' or opcion=='4' or opcion=='5' or opcion=='6' or opcion=='7' or opcion=='8':
			break
		else:
			print('Opcion invalida')
	return opcion

if __name__ == "__main__":
	app = QApplication(sys.argv)		 
	rep = Reproductor()
	try:
		argumento = sys.argv[1]
		f = open(argumento,'r')
		songs = int(f.readline())
		canciones = ArrayT(songs+1)
		canciones[0] = None
		for i in range(1,songs+1):
			entrada = f.readline()
			entradas = ArrayT(3)
			entradas[0] = entrada.split('\t')[0]
			entradas[1] = entrada.split('\t')[1]
			entradas[2] = entrada.split('\t')[2].strip('\n')
			agregar = Cancion(entradas[1], entradas[0], entradas[2])
			canciones[songs-i+1] = agregar
			rep.sonarDespues(agregar)
		f.close()
	except:
		print('Debe proporcionar el archivo de entrada')
		sys.exit()
	
	rep.show()
	sp.call('clear',shell=True)

	#############
	# Menu loop #
	#############
	Menu()

	while True:

		accion = opciones()

		if accion == '1':
			cantidad = len(canciones)
			for i in range(1,cantidad):
				x = canciones[i]
				print('Cancion: '+x.titulo+', Artista: '+x.artista)
				
			accion = 'sin accion'
		
		elif accion == '2':
			new_titulo = input('Ingrese titulo de la cancion: ')
			new_artista = input('Ingrese artista: ')
			new_archivo = input('Ingrese la direccion del archivo: ')
			nueva = Cancion(new_titulo,new_artista,new_archivo)

			cantidad = len(canciones)
			repetida = False

			for i in range(1,cantidad):
				if canciones[i].titulo == new_titulo and canciones[i].artista == new_artista:
					repetida = True
					break

			if not repetida:
				sonando = rep.Actual()
				agregadas = ArrayT(cantidad+1)
				agregadas[0] = canciones[0]
				for i in range(1,cantidad):
					agregadas[i] = canciones[i]

					if canciones[i].titulo == sonando.titulo and canciones[i].artista == sonando.artista:
						j = i+1
						agregadas[j] = nueva

						while j < cantidad:
							agregadas[j+1] = canciones[j]
							j = j+1
						break
				
				canciones = agregadas
			
			rep.sonarDespues(nueva)
			accion = 'sin accion'
		
		elif accion == '3':
			new_titulo = input('Ingrese titulo de la cancion: ')
			new_artista = input('Ingrese artista: ')
			new_archivo = input('Ingrese la direccion del archivo: ')
			nueva = Cancion(new_titulo,new_artista,new_archivo)
			
			cantidad = len(canciones)
			repetida = False

			for i in range(1,cantidad):
				if canciones[i].titulo == new_titulo and canciones[i].artista == new_artista:
					repetida = True
					break

			if not repetida:
				sonando = rep.Actual()
				agregadas = ArrayT(cantidad+1)
				agregadas[0] = canciones[0]
				for i in range(1,cantidad):
					if canciones[i].titulo == sonando.titulo and canciones[i].artista == sonando.artista:
						agregadas[i] = nueva
						j = i

						while j < cantidad:
							agregadas[j+1] = canciones[j]
							j = j+1
						break

					agregadas[i] = canciones[i]

				canciones = agregadas
			
			rep.sonarAntes(nueva)
			accion = 'sin accion'

		elif accion == '4':
			rep.Ordenar_Artista()
			cantidad = len(canciones) - 1
			auxiliar = ArrayT(cantidad)

			for i in range(cantidad):
				auxiliar[i] = canciones[i+1]

			merge_sort(auxiliar,'artista')

			for i in range(cantidad):
				canciones[i+1] = auxiliar[i]
			
			accion = 'sin accion'
		
		elif accion == '5':
			rep.Ordenar_Titulo()
			cantidad = len(canciones) - 1
			auxiliar = ArrayT(cantidad)
			for i in range(cantidad):
				auxiliar[i] = canciones[i+1]

			merge_sort(auxiliar,'titulo')

			for i in range(cantidad):
				canciones[i+1] = auxiliar[i]

			accion = 'sin accion'
		
		elif accion == '6':
			eliminando = input('Ingrese el titulo de la cancion a eliminar: ')
			rep.eliminar(eliminando)
			cantidad = len(canciones)
			repetida = False
			for i in range(1,cantidad):
				if canciones[i].titulo == eliminando:
					repetida = True
					break
			if repetida:
				agregadas = ArrayT(cantidad-1)
				agregadas[0] = canciones[0]
				for i in range(1,cantidad-1):
					if canciones[i].titulo == eliminando:
						j = i+1
						while j < cantidad:
							agregadas[j-1] = canciones[j]
							j = j+1
						break
					agregadas[i] = canciones[i]
				canciones = agregadas
			if len(canciones) == 1:
				print('No hay canciones')
			accion = 'sin accion'
		
		elif accion == '7':
			Menu()
			accion = 'sin accion'
		
		elif accion == '8':
			sys.exit()
			break

sys.exit(app.exec_())
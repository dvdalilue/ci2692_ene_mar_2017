from pathlib import Path
from cancion import Cancion
from reproductor import Reproductor
from arrayT import ArrayT
from lista import *

from PyQt5.QtWidgets import *

import sys, random
import subprocess as sp

# Descripcion: Cliente que ejecuta las operaciones sobre
#			   el reproductor de musica.
#
# Uso:		   python cliente.py <lista_de_reproduccion.txt>
#
#			   La misma debe estar ubicada en la misma carpeta
#			   del cliente, sin acenteos y sin separaciones.
#			   En cada opcion se deben respetar las mayusculas
#			   y las minusculas.
# Autor: Orlando Chaparro Carnet: 12-11499
#         Angel Morante Carnet: 13-10931
# email: 12-11499@usb.ve
#        13-10931@usb.ve // morante413@gmail.com

lista = sys.argv[1] 
hello = str(lista)	

archivo = open(hello,"r")	
linea = archivo.readlines()
n = len(linea)
canciones = ArrayT(n)

for i in range(n):
	canciones[i] = linea[i].split('\t')
	canciones[i][2] = canciones[i][2].replace("\n",'')

artista_titulo = ArrayT(n)

for i in range(n):
	artista_titulo[i] =  canciones[i][1] + "  de: " + canciones[i][0]

cantidad_de_canciones = len(canciones)
print(canciones)
print(cantidad_de_canciones)
lista_de_reproduccion = ListaReproduccion()
for i in range(cantidad_de_canciones):
	cancion = Cancion(canciones[i][1],canciones[i][0],canciones[i][2])
	lista_de_reproduccion.agregar(cancion)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	rep = Reproductor()
	rep.show()
	sp.call('clear',shell=True)

	while True:

		#############
		# Menu loop #
		#############

		print("\n\............Reproductor de Musica...............\n")
		print("\n--------------__     MENU     __----------------\n")
		print("Opciones:\n")
		print("1. Lista de canciones\n")
		print("2. Agregar para sonar justo despues de la cancion actual\n")
		print("3. Agregar para sonar justo antes de la cancion actual\n")
		print("4. Ordenar lista de reproduccion por artista\n")
		print("5. Ordenar lista de reproduccion por artista\n")
		print("6. Eliminar cancion por titulo\n")
		print("7. Mostrar opciones\n")
		print("8. Salir\n")

		opcion = int(input("Escoja una opcion: "))

		if opcion == 1:
			print("LIsta de Reproduccion:")
			for i in range(n):
				print("Cancion "+str(i+1)+": "+artista_titulo[i])
				

		elif opcion == 2:

			print("\nHa seleccionado agregar una cancion para que suene luego de la actual\n\n")

			titulo_solicitado =input("Indique el titulo de la cancion: ")
			artista_solicitado = input("Indique el nombre del artista: ")
			archivo_solicitado = input("Indique el nombre del archivo: ")

			cancion_agregar = Cancion(titulo_solicitado,artista_solicitado,archivo_solicitado)
			rep.sonarDespues(cancion_agregar)

		elif opcion == 3:
			print("\nHa seleccionado agregar una cancion para que suene de ultimal\n\n")

			titulo_solicitado =input("Indique el titulo de la cancion: ")
			artista_solicitado = input("Indique el nombre del artista: ")
			archivo_solicitado = input("Indique el nombre del archivo: ")

			cancion_agregar = Cancion(titulo_solicitado,artista_solicitado,archivo_solicitado)
			rep.sonarAntes(cancion_agregar)

		elif opcion == 4:
			rep.ordenar_por_artista()

		elif opcion == 5:
			rep.ordenar_por_titulo()

		elif opcion == 6:
			titulo_solicitado =input("Indique el titulo de la cancion a eliminar: ")
			rep.eliminar(titulo_solicitado)

		elif opcion == 7:
				print("Opciones:\n\n")
				print("1. Lista de canciones\n")
				print("2. Agregar para sonar justo despues de la cancion actual\n")
				print("3. Agregar para sonar justo antes de la cancion actual\n")
				print("4. Ordenar lista de reproduccion por artista\n")
				print("5. Ordenar lista de reproduccion por artista\n")
				print("6. Eliminar cancion por titulo\n")
				print("7. Mostrar opciones\n")
				print("8. Salir\n\n")

		elif opcion == 8:
			sys.exit()


		############
		# Fin menu #
		############

	
	sys.exit(app.exec_())
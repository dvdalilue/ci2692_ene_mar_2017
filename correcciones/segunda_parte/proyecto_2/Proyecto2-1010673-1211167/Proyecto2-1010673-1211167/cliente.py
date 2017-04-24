# Proyecto no. 2
# Autores: Jorge Sanchez 10-10673
#		   Greanny Vivas 12-11167

from pathlib import Path
from cancion import Cancion
from reproductor import Reproductor
from lista import*
from arrayT import ArrayT

from PyQt5.QtWidgets import *

import sys
import subprocess as sp
import argparse
# Se lee el string del nombre del archivo que se quiere leer, directo desde la terminal

parser = argparse.ArgumentParser(description='El archivo txt a leer es introducido')
parser.add_argument('archivo')
args = parser.parse_args()

# Almacenamos los datos en un ArrayT para crear la lista de reproduccion a partir del txt

txt = open(args.archivo,'r')

l = []
for line in txt:
	line = line.split('\t')
	l.append(line)

num_canciones = int(l[0][0])
a = ArrayT(len(l)-1)
for i in range(1,len(l)):
	a[i-1] = l[i]

if __name__ == "__main__":
	app = QApplication(sys.argv)
	rep = Reproductor()
	rep.show()
	sp.call('clear',shell=True)
	for i in range(len(a)-1,-1,-1):
		filepath = str(a[i][2])[:-1]
		rep.playlist.agregar(Cancion(str(a[i][0]),str(a[i][1]),filepath))

	print(" BIENVENIDO AL ADMINISTRADOR DE LISTA DE REPRODUCCION")
	
	def mostrar_opciones():
		print(" ")
		print(" 1. Listar canciones")
		print(" ")
		print(" 2. Agregar para sonar justo despues de la cancion actual")
		print(" ")
		print(" 3. Agregar para sonar justo antes de la cancion actual")
		print(" ")
		print(" 4. Ordenar lista de reproduccion por artista")
		print(" ")
		print(" 5. Ordenar lista de reproduccion por titulo")
		print(" ")
		print(" 6. Eliminar cancion por titulo")
		print(" ")
		print(" 7. Mostrar opciones")
		print(" ")
		print(" 8. Salir")
		print(" ")

	mostrar_opciones()
	# Codigo:
	while True:
		opcion = int(input("Escoja una opcion: "))

		if opcion == 1: # listar canciones
			print("Las canciones de la lista son: ")
			rep.playlist.mostrar()

		elif opcion == 2: # funcion agregar
			titulo = input(" Indique el titulo de la cancion: ")
			artista = input(" Indique el nombre del interprete de la cancion: ")
			archivo = input(" Indique la direccion del archivo de audio: ")
			nueva_cancion = Cancion(artista,titulo,archivo)
			rep.sonarDespues(nueva_cancion)

		elif opcion == 3: #funcion agregar_final
			titulo = input(" Indique el titulo de la cancion: ")
			artista = input(" Indique el nombre del interprete de la cancion: ")
			archivo = input(" Indique la direccion del archivo de audio: ")
			nueva_cancion = Cancion(artista,titulo,archivo)
			rep.sonarAntes(nueva_cancion)

		elif opcion == 4: # ordenar lista por artista
			rep.playlist.ordenar_artista(rep.playlist)

		elif opcion == 5: # ordenar lista por artista
			rep.playlist.ordenar_titulo(rep.playlist)

		elif opcion == 6: # eliminar por titulo
			titulo = input(" Indique el titulo de la cancion que desea eliminar: ")
			rep.eliminar(titulo)

		elif opcion == 7: # mostrar las opciones solo en esta opcion
			mostrar_opciones()

		elif opcion == 8: # salir del reproductor
			print("Cerrando administrador de lista de reproduccion")
			sys.exit()

		elif (opcion > 8) or (opcion < 1):
			print("Error, la opcion seleccionada no es valida")
			print("")


	# Para eliminar una cancion debe solicitar el titulo y pasarlo al método
	# eleminar de la instancia de Reproductor 'rep'.
	# 
	# rep.eliminar(titulo_solicitado)
	############
	# Fin menu #
	############

	sys.exit(app.exec_())

	
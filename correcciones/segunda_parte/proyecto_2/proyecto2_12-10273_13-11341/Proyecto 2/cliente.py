"""PROYECTO 2
# DESCRIPCIÓN: Creación del cliente.
# AUTORES: Jesus Kauze y David Segura
# EMAILS: 12-10273@usb.ve y 13-11341@usb.ve
"""

from pathlib import Path
from cancion import Cancion
from reproductor import Reproductor
from arrayT import ArrayT

from PyQt5.QtWidgets import *

import sys
import subprocess as sp

if __name__ == "__main__":
	app = QApplication(sys.argv)
	rep = Reproductor()
	rep.show()
	sp.call('clear',shell=True)

	canciones = open("canciones.in","r")
	n = int(canciones.readline())
	lista = ArrayT(n)
	can = canciones.readlines()

	for x in range(n):
		t = can[x].strip("\n")
		p = t.split("\t")
		lista[x] = p

	for x in lista:
		c = Cancion(x[1],x[0],x[2])
		rep.playlist.agregar(c)


	#############
	# Menu loop #
	#############

	while True:
		print("REPRODUCTOR DE KAUZE Y DAVID\n"
				"1.Listar canciones\n"+
				"2.Agregar para sonar justo después de la canción actual\n"+
				"3.Agregar para sonar justo antes de la canción actual\n"+
				"4.Ordenar lista de reproducción por artista\n"+
				"5.Ordenar lista de reproducción por titulo\n"+
				"6.Eliminar canción por titulo\n"+
				"7.Mostrar opciones\n"+
				"8.Salir")
		opcion = input("-----> INTRODUCIR OPCIÓN: ")
		if int(opcion) == 1:
			x = rep.playlist #Lista de Reproducción
			y = x.proxima.siguiente.siguiente #Nodo
			print("Artista,Titulo")
			for i in range(x.count):
				print(str(y.elemento.artista)+","+(y.elemento.titulo))
				y = y.siguiente
			continuar = input("--------PRESIONE ENTER PARA CONTINUAR--------")
		elif int(opcion) == 2:
			try:
				c = Cancion(input("Titulo de la Canción: "),input("Artista de la Cancion: "),input("Archivo: "))
				rep.sonarDespues(c)
				print("-----> Canción Agregada")
				continuar = input("--------PRESIONE ENTER PARA CONTINUAR--------")
			except:
				print("-----> Canción Inválida")
				continuar = input("--------PRESIONE ENTER PARA CONTINUAR--------") 
		elif int(opcion) == 3:
			try:
				c = Cancion(input("Titulo de la Canción: "),input("Artista de la Cancion: "),input("Archivo: "))
				rep.sonarAntes(c)
				print("-----> Canción Agregada")
				continuar = input("--------PRESIONE ENTER PARA CONTINUAR--------")
			except:
				print("-----> Canción Inválida")
				continuar = input("--------PRESIONE ENTER PARA CONTINUAR--------") 
		elif int(opcion) == 4:
			rep.ordenar_por_artista()
			print("-----> Lista Ordenada por artista")
			continuar = input("--------PRESIONE ENTER PARA CONTINUAR--------")
		elif int(opcion) == 5:
			rep.ordenar_por_titulo()
			print("-----> Lista Ordenada por titulo")
			continuar = input("--------PRESIONE ENTER PARA CONTINUAR--------")
		elif int(opcion) == 6:
			titulo = input("Titulo de la canción: ")
			rep.eliminar(titulo)
			continuar = input("--------PRESIONE ENTER PARA CONTINUAR--------")
		elif int(opcion) == 7:
			pass
		elif int(opcion) == 8:
			sys.exit()
		else:
			print("-----> Opción no válida")
			continuar = input("--------PRESIONE ENTER PARA CONTINUAR--------")
	############
	# Fin menu #
	############

	sys.exit(app.exec_())
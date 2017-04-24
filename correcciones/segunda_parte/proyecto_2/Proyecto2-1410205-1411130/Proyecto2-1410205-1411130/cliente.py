from pathlib import Path
from cancion import Cancion
from reproductor import Reproductor
from arrayT import ArrayT
from lista import ListaReproduccion

from PyQt5.QtWidgets import *

import sys
import subprocess as sp

if __name__ == "__main__":
	app = QApplication(sys.argv)
	rep = Reproductor()
	rep.show()
	sp.call('clear',shell=True)

	#############
	# Menu loop #
	#############

	stringMenu="1. Listar canciones.\n2. Agregar cancion justo despues de la cancion actual.\n3. Agregar cancion justo antes de la cancion actual.\n4. Ordenar lista de reproduccion por artista.\n5. Ordenar lista de reproduccion por titulo.\n6. Eliminar cancion por titulo.\n7. Mostrar opciones.\n8. Salir."
	print(stringMenu)
	
	#Lee el archivo ListaReproduccion.txt para almacenar los nombres de
	#las canciones en un array
	with open('ListaReproduccion.txt','r') as f:
		lista_archivo=[line.strip('\n')for line in f]
		#Lo colocamos en un array sin el tabulador
		list_r=ArrayT(int(lista_archivo[0]))
		list_arch=ArrayT(len(lista_archivo)-1)
		for i in range(len(list_arch)):
			list_arch[i]=lista_archivo[i+1]
		for i in range(len(list_r)):
			lista_sintab=list_arch[i].split('	')	#Quitamos el tab
			list_r[i]=ArrayT(3)	#Hacemos un array para que almacene artista, titulo y path
			list_r[i][0]=lista_sintab[0]	#Artista
			list_r[i][1]=lista_sintab[1]	#Titulo
			list_r[i][2]=lista_sintab[2]	#Filepath

	#Creamos una instancia de tipo cancion para cada elemento de la lista y lo agregamos a un array
	list_rep=ArrayT(len(list_r))
	for i in range(len(list_rep)):
		list_rep[i]=Cancion(list_r[i][1],list_r[i][0],str(list_r[i][2]))  #titulo artista filepath
	
	#Tenemos las instancias de cancion en el array list_rep, los colocamos en la lista circular
	for i in range(len(list_rep)):
		rep.sonarDespues(list_rep[i])
	
	#Inicializar el menu
	while True:
		m=input("Elija una opcion del menu: ")
		while m not in range(1,9):
			m=input("Elija una opcion del menu: ")
		
		#Listar canciones
		if m==1:
			rep.imprimirLista()
		
		#Agregar cancion justo despues de la cancion actual
		elif m==2:
			titulo=str(raw_input("Introduzca el titulo de la cancion: "))
			while len(titulo)==0 or titulo==" ":
				titulo=str(raw_input("Introduzca el titulo de la cancion: "))
			artista=str(raw_input("Introduzca el artista de la cancion: "))
			while len(artista)==0 or artista==" ":
				artista=str(raw_input("Introduzca el artista de la cancion: "))
			path=str(raw_input("Introduzca el path de la cancion: "))
			while  len(path)==0 or path==" ":
				path=str(raw_input("Introduzca el path de la cancion: "))
			cancion=Cancion(titulo,artista,path)
			rep.sonarDespues(cancion)
		
		#Agregar cancion justo antes de la cancion actual
		elif m==3:
			titulo=str(raw_input("Introduzca el titulo de la cancion: "))
			while len(titulo)==0 or titulo==" ":
				titulo=str(raw_input("Introduzca el titulo de la cancion: "))
			artista=str(raw_input("Introduzca el artista de la cancion: "))
			while len(artista)==0 or artista==" ":
				artista=str(raw_input("Introduzca el artista de la cancion: "))
			path=str(raw_input("Introduzca el path de la cancion: "))
			while  len(path)==0 or path==" ":
				path=str(raw_input("Introduzca el path de la cancion: "))
			cancion=Cancion(titulo,artista,path)
			rep.sonarAntes(cancion)
		
		#Ordenar la lista de reproduccion por artista
		elif m==4:
			rep.ordenarArtista()
		
		#Ordenar la lista de reproduccion por artista
		elif m==5:
			rep.ordenarTitulo()
		
		#Eliminar cancion de la lista por titulo
		elif m==6:
			titulo=str(raw_input("Introduzca el titulo de la cancion que desea eliminar: "))
			while len(titulo)==0 or titulo==" ":
				titulo=str(raw_input("Introduzca el titulo de la cancion que desea eliminar: "))
			rep.eliminar(titulo)
		
		#Mostrar las opciones del menu
		elif m==7:
			print(stringMenu)
		
		#Salir del reproductor
		elif m==8:
			sys.exit()


	############
	# Fin menu #
	############

	sys.exit(app.exec_())

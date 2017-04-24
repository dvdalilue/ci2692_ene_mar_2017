#from pathlib import Path
from cancion import Cancion
from lista import ListaReproduccion
#from reproductor import Reproductor
from arrayT import ArrayT
#from PyQt5.QtWidgets import *
from lista import *

import sys
import subprocess as sp
"""
if __name__ == "__main__":
	app = QApplication(sys.argv)
	rep = Reproductor()
	rep.show()
	sp.call('clear',shell=True)
"""

    #############
    # Menu loop #
    #############
    
def procesar_archivo(nombre_archivo):
	Titulo = []
	artista = []
	archivo = []
	mientras =[]
	with open(nombre_archivo, "r") as fd:   # Se abre el archivo para lectura
		S=fd.readlines()
		N=int(S[0])
		S.remove(S[0])                      #Remueve la linea 0
	for i in range (N):
		line = line.rstrip()            # Se elimina el salto-de-linea al final de la linea 
		tok = line.split("\t")          # Se parte la linea en el caracter tabulador [TAB]
		art = tok[0]                  # Se obtiene el nombre del autor
		Tit = tok[1]
		arc = tok[2]	                # Se obtiene el nombre del libro
		artista.append(art)
		Titulo.append(Tit)
		archivo.append(arc)
	for i in range (len(Titulo)):
		Titulo[i]=Titulo[i].replace("\n","")
	print(Titulo)
	for i in range (len(artista)):
		artista[i]=artista[i].replace("\n","")
	print(artista)
	for i in range (len(archivo)):
		archivo[i]=archivo[i].replace("\n","")
	print(archivo)
	
	CancionR = ArrayT(N)
	CAncionMostrar = ArrayT(N)
	for i in range (N):
		CancionR[i]= Cancion ( artista[i], Titulo[i], archivo[i])
	for i in range (N):
		CAncionMostrar[i] = [ artista[i], Titulo[i], archivo[i]]	
	
	return CancionR,CAncionMostrar,N      # Se retornan los arreglos

    # Su código iría aquí
	
def menu():
	print ("A continuacion las opciones del menu:")
	print ("1. Listar Canciones")
	print ("2. Agregar para sonar justo despues de la cancion actual")
	print ("3. Agregar para sonar justo antes de la cancion actual")
	print ("4. Ordenar Lista de reproduccion por artista")
	print ("5. Ordenar lista de reproduccion por titulo")
	print ("6. Eliminar cancion por titulo")
	print ("7. Mostrar opciones")
	print ("8. Salir")
	print ("Escoja una opcion:")
	
	x = input("Opcion: ")
	while (x != 8):	
		if x == "1":
			Lista, ListaAM, num = procesar_archivo("biblioteca.txt")
			print("las canciones en la biblioteca son:"
			for i in range (num):
				print(ListaAM[i])
			print("las canciones en la lista de reproduccion son:")
			rep.__playlist.mostrar_elementos()
			menu()
		if x == "2":
			print("ingrese los datos de la cancion que desea incluir al final de lista de reproduccion")
			art =input("ingrese el nombre del artista: ")
			tit =input("ingrese el nombre de la cancion: ")
			arch =input("ingrese la direccion del archivo: ")
			CANCION = Cancion (art,tit,arch)
			rep.sonarDespues(CANCION)
			menu()
		
		if x == "3":
			print("ingrese los datos de la cancion que desea incluir al final de lista de reproduccion")
			art =input("ingrese el nombre del artista: ")
			tit =input("ingrese el nombre de la cancion: ")
			arch =input("ingrese la direccion del archivo: ")
			CANCION = Cancion (art,tit,arch)
			rep.sonarAntes(CANCION)
			menu()

		#if x == "4":
		#	self.lista.ordenar_artista()
		#	self.interfaz.canciones_nuevas()
		#if x == "5":
			#self.lista.ordenar_titulo()
			#self.interfaz.canciones_nuevas()
		if x == "6":
			tit =input("ingrese el nombre de la cancion que desea eliminar: ")
			rep.eliminar(tit)
			print("la cancion ha sido eliminada")
			menu()
		
		if x == "7":
			menu()
		
		if x == "8":
			sys.exit(app.exec_())
		
    # Para eliminar una canción debe solicitar el título y pasarlo al método
    # eleminar de la instancia de Reproductor 'rep'.
    # 
    # rep.eliminar(titulo_solicitado)
    


    ############
    # Fin menu #
    ############

menu()

#    sys.exit(app.exec_())

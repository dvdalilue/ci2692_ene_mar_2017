""" Algoritmos II .ene-mar 2017 
	fecha: 11/03/2017
    Descripcion:  TAD que representa a una cancion a reproducir que se encontrara en el archivo cancion.py, contiene
los atributos de instancia tıtulo, artista y archivo (de tipo wav). Donde el tıtulo y artita son strings no vacıos
y el archivo es una instancia de QFile donde la direcci ́on del archivo corresponde a uno de musica de formato
wav.
	autores: Edymar Mijares 12-10882
	         Jose Carmona 11-10156

	correo: - edys.beccaria@gmail.com
		   - carmona621@hotmail.com
ultima edicion :18/03/2017"""

from pathlib import Path
from PyQt5.QtCore import QFile
import os


class Cancion:
#Constructor de la clase que recibe un tıtulo y un artista, los
#cuales son strings no vacıos, ademas la direccion de un archivo en string que no puede ser None. Estos
#parametros deben inicializar cada atributo de instancia correspondiente.#filepath es el archivo
	def __init__(self, titulo, artista, filepath):
		self.titulo = titulo
		self.artista = artista
		self.archivo = filepath
		
#Compara otra instancia de la clase Cancion con self y verifica si son iguales
#por titulo y artista, retornando True en caso de serlos y False en caso contrario.
	def es_igual(self, other):#entra otra cancion
		igual = False
		if self.titulo == other.titulo:
			if self.artista == other.artista:
				igual = True
				return igual
			else:
				return igual
		else:
			return igual

#Compara otra instancia de la clase Cancion con self y verifica si es
#menor por artista. Si el artista es el mismo, compara por titulo, retornando True en caso de que self
#sea menor y False en caso contrario
	def es_menor_artista(self,other):
		menor = False
		if self.artista < other.artista:
			menor = True
		elif self.artista == other.artista:
			if self.titulo < other.titulo:
				menor = True
		
		return menor
#Compara otra instancia de la clase Cancion con self y verifica si es
#menor por el titulo. Si el titulo es igual, compara por artista, retornando True en caso de que self sea
#menor y False en caso contrario.
	def es_menor_titulo(self, other):
		menor = False 
		if self.titulo < other.titulo:
			menor = True
		elif self.titulo == other.titulo:
			if self.artista < other.artista:
				menor = True
		
		return menor
#funcion que imprime la cancion que esta sonando			
	def mostrar_cancion(self):
		print( self.titulo, "Por:",self.artista, "la cancion esta en:", self.archivo)
		


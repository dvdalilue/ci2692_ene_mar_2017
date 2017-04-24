from pathlib import Path
from PyQt5.QtCore import QFile

class Cancion:
	def __init__(self, titulo, artista, filepath):
		self.titulo = titulo
		self.artista = artista
		self.archivo = QFile(filepath)

	def es_igual(self,cancion):
		if self.titulo==cancion.titulo and self.artista==cancion.artista:
			return True
		else:
			return False

	def es_menor_artista(self,cancion):
		#Retorna True si self es menor que cancion por artista
		if self.artista<cancion.artista:
			return True
		elif self.artista==cancion.artista:
			if self.titulo<cancion.titulo:
				return True
			else:
				return False
		else:
			return False

	def es_menor_titulo(self,cancion):
		#Retorna True si self es menor que cancion por artista
		if self.titulo<cancion.titulo:
			return True
		elif self.titulo==cancion.titulo:
			if self.artista<cancion.artista:
				return True
			else:
				return False
		else:
			return False

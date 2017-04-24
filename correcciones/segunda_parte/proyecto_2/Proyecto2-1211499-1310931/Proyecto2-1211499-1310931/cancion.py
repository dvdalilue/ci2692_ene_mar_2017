from pathlib import Path
from PyQt5.QtCore import QFile

# Descripcion: Constructor de la clase Cancion, con los
#              metodos es_igual, esmenor_artista, esmenor_titulo,
#			   get_titulo, get_artista, get_genero, get_archivo.
#
# Atributos:   -titulo: Titulo de la cancion (String)
#			   -genero: Genero de la cancion (String)
#			   -artista: Artista de la cancion (String)
#			   -archivo: Ubicacion de la cancion
#
# Autor: Orlando Chaparro Carnet: 12-11499
#         Angel Morante Carnet: 13-10931
# email: 12-11499@usb.ve
#        13-10931@usb.ve // morante413@gmail.com

class Cancion:
	def __init__(self, titulo, artista, filepath):
		
		assert(titulo != "" and artista != "" and filepath != None)
		
		self.titulo = titulo
		self.artista = artista
		self.archivo = filepath
	

	# Descipcion: Metodo que dice si una cancion es igual a otra.
	# Atributos: -cancion: Elemento de tipo 'cancion'.
	# Retorna: -igual: Variable booleana; True si las canciones son iguales,
	#                  False si no lo son.	

	def es_igual(self,cancion):
		if self.titulo == cancion.titulo and self.artista == cancion.artista:
			igual = True
		else:
			igual = False

		return igual


	# Descipcion: Metodo que dice si el artista de una cancion
	#             es alfabeticamente menor.
	# Atributos: -cancion: Elemento de tipo 'cancion'
	# Retorna: -esMenor: Variable booleana; True si el artista de la cancion
	#                    self es menor alfabeticamente que el artista de la
	#                    cancion 'cancion, False si no lo son.
	def es_menor_artista(self,cancion):
		if self.artista < cancion.artista or (self.artista == cancion.artista and self.titulo <= cancion.titulo):
			esMenor = True
		else:
			esMenor = False
					
		return esMenor 

	# Descipcion: Metodo que dice si el titulo de una cancion
	#             es alfabeticamente menor.
	# Atributos: -cancion: Elemento de tipo 'cancion'.
	# Retorna: -esMenor: Variable booleana; True si el titulo de la cancion
	#                    self es menor alfabeticamente que el artista de la
	#                    cancion 'cancion, False si no lo son.	

	def es_menor_titulo(self, cancion):
		if self.titulo < cancion.titulo or (self.titulo == cancion.titulo and self.artista <= cancion.artista):
			esMenor = True
		else:
			esMenor = False

		return esMenor
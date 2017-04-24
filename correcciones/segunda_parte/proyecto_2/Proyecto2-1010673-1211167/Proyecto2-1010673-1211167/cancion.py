# Proyecto no. 2
# Autores: Jorge Sanchez 10-10673
#		   Greanny Vivas 12-11167

from pathlib import Path
from PyQt5.QtCore import QFile

# Clase cancion:
class Cancion:
    def __init__(self, artista, titulo, archivo):
    	assert(len(str(titulo))>1 and len(str(artista))>1 and archivo is not None)
    	self.titulo = str(titulo)
    	self.artista = str(artista)
    	self.archivo = QFile(archivo)
# funcion es_igual para verificar si las canciones son iguales por titulo y artista
    def es_igual(self,cancion):
        if self.titulo.lower() == cancion.titulo.lower() and self.artista.lower() == cancion.artista.lower():
            return True
        else:
            return False
# funcion es_menor_artista para verificar si la cancion es menor por artista y si es 
# igual por artista, comparar si es menor por titulo:
    def es_menor_artista(self,cancion):
    	if cancion.artista.lower() < self.artista.lower():
    		return True
    	elif cancion.artista == self.artista:
    		if self.titulo.lower() < cancion.titulo.lower():
    			return True
    		else:
    			return False
    	else:
        	return False
# funcion es_menor_titulo para verificar si la cancion es menor por titulo y si es 
# igual por titulo, comparar si es menor por artista:
    def es_menor_titulo(self,cancion):
        if self.titulo.lower() < cancion.titulo.lower():
        	return True
        elif cancion.titulo == self.titulo:
        	if self.artista.lower() < cancion.artista.lower():
        		return True
        	else:
        		return False
        else:
        	return False
from cancion import *

class NodoLista:
	def __init__(self, cancion, s, a):
		self.elemento = cancion
		self.siguiente = s
		self.anterior = a

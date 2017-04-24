# Proyecto no. 3
# Autores: Jorge Sanchez 10-10673
#			Greanny Vivas 12-11167

# TAD Registro de usuarios: Tabla de hash estática que contiene elementos de tipo usuario

from tablaC import*
from chat import*
from usuario import*
from registro_usuarios import*

# Creacion de tablaC con 100 usuarios
TablaC = tablaC(10)

class Conversaciones():

	def __init__(self,n,tablaC):
		# assert del numero de conversaciones con el numero de elementos de la tabla
		assert(n == TablaC.size)
		self.num_conversaciones = n
		self.conversaciones = tablaC.arregloHash # tabla de hash con el registro de los usuarios

	def BuscarConversacion(self,ID):
		chat = TablaC.SearchChat(ID)
		return chat

	def AgregarConversacion(self,chat):
		return TablaC.Agregar(chat)


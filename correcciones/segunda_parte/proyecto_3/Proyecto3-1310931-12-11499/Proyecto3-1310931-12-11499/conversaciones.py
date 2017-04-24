#######################################
########                    ###########
######## TAD CONVERSACIONES ###########
########                    ###########
#######################################

from chat import *
from registro_usuarios import * 
from usuario import *

class Conversaciones:

	def __init__(self,n):

		self.size = n #Numero de usuarios registrados
		self.TablaC =[dList() for x in range(n)]


	def AgregarConversacion(self,c):

		NodoChat = HashEntry(c.id,c)
		key = hash(c.id) % self.size
		if (self.TablaC[key]).id == c.id:
			(self.TablaC[key]).dato = c.dato
			return False
		else: 
			(self.TablaC[key]).add(c)
			return True

	def BuscarConversacion(self,identidad):

		key = hash(identidad) % self.size
		if self.TablaC[key].id == identidad:
			return self.TablaC[key]
		else:
			return None
			
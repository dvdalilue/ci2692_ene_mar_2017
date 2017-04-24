# Proyecto no. 3
# Autores: Jorge Sanchez 10-10673
#		   Greanny Vivas 12-11167

from usuario import*

# TAD Mensajes que crea un elemento Mensaje con un string y un apuntador siguiente
class Mensaje():

	def __init__(self,m):
		self.msj = m
		self.next = None

# TAD ListaMensajes que crea la lista enlazada de mensajes
class ListaMensajes():

	def __init__(self):
		self.first = None
		self.size_lista = 0

	def Agregar_enmsjs(self,m):
		first = self.first
		if self.size_lista == 0:
			self.first = m
			self.first.next = None
			self.size_lista += 1
		else:
			self.first = m
			self.first.next = first
			self.size_lista += 1

	def Mostrar_enmsjs(self):
		i = self.first
		while i != None:
			print(str(i.msj))
			i = i.next

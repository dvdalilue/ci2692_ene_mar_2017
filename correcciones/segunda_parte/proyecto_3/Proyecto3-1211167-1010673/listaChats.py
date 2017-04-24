# Proyecto no. 3
# Autores:
# Jorge Sanchez 10-10673
# Greanny Vivas 12-11167

from chat import*
# Crear Lista enlazada como clase pública:
# Los elementos de la tabla de hash seran listas enlazadas con datos tipo usuarios 
class ListaChats():

	def __init__(self):
		self.first = None
		self.size_lista = 0

	def BuscarChat(self,ID):
		i = self.first
		while i != None:
			# si encuentra el ID, retorna el chat completo
			if i.ID.lower() == ID.lower():
				return i
			elif i.ID.lower() != ID.lower():
				i = i.next
		# si no encuentra el ID, retorna None
		return None

	# funcion que busca el nombre del usuario
	def Buscar_enchats(self,ID):
		i = self.first
		while i != None:
			# si encuentra el ID, retorna el usuario
			if i.ID.lower() == ID.lower():
				return i
			elif i.ID.lower() != ID.lower():
				i = i.next
		# si no encuentra el ID, retorna None
		return None

	def Pertenece_enchats(self,ID):
		chat = self.first
		while chat != None:
			if chat.ID.lower() == ID.lower():
				# si se encuentra el ID, retorna True
				return True
			elif chat.ID.lower() != ID.lower():
				chat = chat.next
		# si no se encuentra el ID, retorna False
		return False

	# Condicion de Agregar o Modificar en la tabla
	def Agregar_enchats(self,chat):
		first = self.first
		if self.first == None:
			self.first = chat
			self.first.next = None
			self.size_lista += 1
		else:
			self.first = chat
			chat.next = first
			self.size_lista += 1

	# llamar a modificar cuando el ID pertenece a la tablaC
	def Modificar_enchats(self,chat):
		chat_anterior = self.Buscar_enchats(chat.ID)
		if chat_anterior != None:
			chat_anterior = chat
			return True

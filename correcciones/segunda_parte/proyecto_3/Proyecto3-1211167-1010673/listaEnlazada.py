# Proyecto no. 3
# Autores:
# Jorge Sanchez 10-10673
# Greanny Vivas 12-11167

from usuario import*
# Crear Lista enlazada como clase pública:
# Los elementos de la tabla de hash seran listas enlazadas con datos tipo usuarios 
class ListaEnlazada():

	def __init__(self):
		self.first = None
		self.size_lista = 0

	# funcion que busca el nombre del usuario
	def Buscar_enlista(self,nombre):
		i = self.first
		while i != None:
			# si encuentra el nombre, retorna el usuario
			if i.nombre.lower() == nombre.lower():
				return i
			elif i.nombre.lower() != nombre.lower():
				i = i.next
		# si no encuentra el nombre, retorna None
		return None

    # funcion que busca si el nombre del usuario pertenece a la lista
	def Pertenece_enlista(self,nombre):
		i = self.first
		while i != None:
			if i.nombre.lower() == nombre.lower():
				# si se encuentra el nombre, retorna True
				return True
			elif i.nombre.lower() != nombre.lower():
				i = i.next
		# si no se encuentra el nombre, retorna False
		return False

	def Agregar_enlista(self,usuario):
		if self.Pertenece_enlista(usuario.nombre) == False:
			first = self.first
			if self.first == None:
				self.first = usuario
				self.first.next = None
				self.size_lista += 1
			else:
				self.first = usuario
				usuario.next = first
				self.size_lista += 1
			return True
		else:
			return False


# funcion que elimina el usuario asociado al nombre dado
	def Eliminar_enlista(self,nombre):
		entry = self.Buscar_enlista(nombre)
		if entry != None:
			first = self.first
			# Cuando esta de primero:
			if entry.nombre.lower() == self.first.nombre.lower():
				# unico elemento:
				if first.next == None:
					self.first = None
					return True
				# primero de la lista:
				else:
					# el primero de la lista es el siguiente:
					self.first = first.next
					return True
				self.size_lista -= 1
			# cuando no esta de primero
			else:
				aux1 = self.first
				aux2 = self.first.next
				while aux2 != None:
					if aux2.nombre == nombre:
						aux1.next = aux2.next
						return True
					else:
						if aux2.next == None and aux2.nombre == nombre:
							aux1.next = None
							return True
						aux1 = aux1.next
						aux2 = aux2.next
				self.size_lista -= 1
		else:
			return False
				
	def Mostrar_enlista(self):
		i = self.first
		while i != None:
			print("(" + str(i.nombre) + "," + str(i.telefono) + ")")
			i = i.next


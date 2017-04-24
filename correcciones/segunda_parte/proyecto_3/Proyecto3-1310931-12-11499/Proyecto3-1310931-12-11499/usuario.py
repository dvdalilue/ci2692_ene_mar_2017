
""" Modulo con la implementacion del el TAD Usuario y las funciones
	necesarias relacionadas a este para cumplir los requisitos del 
	proyecto
	
	Autores:

	- Orlando Chaparro
	- Angel Morante

	Ultima Modificacion:

		30 de marzo de 2017
"""


class Nodo:

	def __init__(self,usuario):
		self.valor = usuario
		self.next = None
		self.prev = None 

#	Lista enlazada de elementos de tipo Usuario en donde los usuarios estan ordenados
#	en orden ascendente segun el orden lexicografico de los nombres de los usuarios
class ListadeContactos:

	def __init__(self):
		self.head = None
		self.last = None
		self.size = 0

	#	Funcion utilizada para buscar alguno de los Nodos. Si el nodo fue hallado retorna
	#	True. De lo contrario, retorna False
	def Buscar(Nodo):
		x = self.head
		while x != None and x.valor.nombre != Nodo.valor.nombre:
			x = x.next

		if x == None:
			return False
		else:
			return True

	#	Agrega un Nodo tomando en cuenta si dicho nodo ya existe o no.
	def add(Nodo):

		curNodo = self.head
		encontrado = self.Buscar(Nodo)
		if encontrado == False:
			while Nodo.valor.nombre > curNodo.valor.nombre and curNodo != None:
				curNodo = curNodo.next

			Nodo.next = curNodo
			Nodo.prev = curNodo.prev
			curNodo.prev.next = Nodo
			curNodo.prev = Nodo
			self.size += 1
			return True

		else:
			return False

	#	Remueve un Nodo ingresado por el usuario
	def remove(Nodo):
		if Nodo.prev != None:
			Nodo.prev.next = Nodo.next
			self.size -= 1
			return True
		elif Nodo.next != None:
			Nodo.next.prev = Nodo.prev
			self.size -=1
			return True
		elif Nodo.prev == None:
			self.head = Nodo.next
			self.size -=1
			return True
		else:
			return False

	#	Muestra cada uno de los Nodos
	def Mostrar(self):
		x = self.head

		for x in range(self.size):
			print("Nombre: " + x.valor.nombre + "Telefono: " + x.valor.telefono)
			x = x.next


class Usuario:

	# TAD que representa a un usuario. Contiene los atributos
	# de instancia nombre, password y telefono.

	def __init__(self, nombre, password, telefono):

		#Nombre, password y tlf no pueden ser nulos
		#Telefono debe llevar los caracteres de 0 a 9

		self.nombre = nombre 		# Atributo de instancia > Tipo string
		self.password = password 	# Atributo de instancia > Tipo string
		self.telefono = telefono 	# Atributo de instancia > Tipo string
		self.contactos = [ListadeContactos() for x in range(100)]  # Atributo de instancia > Tipo lista enlazada

	"""def CrearUsuario(self, nombre, password, telefono, contactos = None):
		nuevoUsuario = self.Usuario(nombre, password, telefono, contactos)
		return nuevoUsuario"""

	def AgregarContacto(self,u):
		NuevoNodo = Nodo(u)
		self.contactos.add(NuevoNodo)

	def EliminarContacto(self,n):
		Usuario_a_eliminar = self.CrearUsuario(n,0,0)
		NuevoNodo = Nodo(Usuario_a_eliminar)
		return remove(NuevoNodo)

	def MostrarContactos(self):
		NuevoNodo = Nodo(self)
		NuevoNodo.Mostrar()















 

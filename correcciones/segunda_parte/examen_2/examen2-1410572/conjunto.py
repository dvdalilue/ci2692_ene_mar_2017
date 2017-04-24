"""
************************************
	Alumno: Yeferson Licet
	Carnet: 14-10572

	Parcial 2 - Conjunto
	conjunto.py
************************************
"""


class Node:
	"""
		Clase que implementa el comportamiento de un Nodo
	"""
	def __init__(self, _data, _next):
		"""
			Inicializa un nodo
			@param Dato a insertar
			@param Sucesor del nodo
			@Return void
		"""
		self.next = _next
		self.data = _data

class Conjunto:
	"""
		Clase que implementa las operaciones de un conjunto finito
	"""
	
	def __init__(self):
		"""
			Inicializa un conjunto vacio
			
			@Return void
		"""
		self.size = 0
		self.head = None

	def Agregar(self, e):
		"""
			Agrega un conjunto al elemento
			
			@param Instancia
			@param Elemento a agregar
			@Return bool
		"""
		if self.Pertenece(e):
			return False
	
		self.head = Node(e, self.head)
		self.size +=1

		return True

	def Pertenece(self, e):
		"""
			Determina si un elemento pertenece al conjunto
			
			@param Instancia
			@param Elemento a comparar
			@Return bool
		"""
		x = self.head
		while x != None:
			if x.data == e:
				return True
			x = x.next

		return False

	def Mostrar(self):
		"""
			Muestra los elementos del conjunto
			
			@param Instancia
			@Return void
		"""
		if self.size == 0:
			print("El conjunto esta vacio")
			return

		x = self.head
		while x != None:
			print('Elemento: ' ,x.data)
			x = x.next

	def Union(self, conjunto):
		"""
			Realiza la union de dos conjuntos A y B
			
			@param Instancia A
			@param Conjunto B

			@Return Conjunto (AUB)
		"""
		resultado = Conjunto()

		x = self.head
		while x != None:
			resultado.Agregar(x.data)
			x = x.next

		x = conjunto.head
		while x != None:
			resultado.Agregar(x.data)
			x = x.next

		return resultado

	def Interseccion(self, conjunto):
		"""
			Realiza la interseccion de dos conjuntos A y B
			
			@param Instancia A
			@param Conjunto B

			@Return Conjunto {x: xEA^xEB)
		"""
		menor = conjunto
		mayor = self

		if self.size < conjunto.size:
			menor = self 
			mayor = conjunto

		resultado = Conjunto()

		x = menor.head
		while x != None:
			if mayor.Pertenece(x.data):
				resultado.Agregar(x.data)
			x = x.next

		return resultado
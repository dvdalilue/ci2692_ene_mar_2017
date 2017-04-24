# Parcial no. 2
# Greanny Vivas Diaz 12-11167 

# Estructura equivalente a un conjunto finito

# TAD Entero que recibe el elemento, y le asigna un apuntador
class Entero():
	def __init__(self,e):
		self.numero = int(e)
		self.next = None

# TAD Conjunto cuya estructura es una lista enlazada simple con elementos de tipo entero de la clase Entero
class Conjunto():
	def __init__(self):
		self.size = 0
		self.first = None

	def Agregar(self,e):
		entero = Entero(e)
		first = self.first
		if self.Pertenece(e) == False:
			if self.first == None:
				self.first = entero
				self.first.next = None
				self.size += 1
			else:
				self.first = entero
				entero.next = first
				self.size += 1
			return True

    # funcion que busca si el elemento tipo entero pertenece a la lista
	def Pertenece(self,e):
		entero = Entero(e)
		i = self.first
		while i != None:
			if i.numero == entero.numero:
				# si se encuentra el entero, retorna True
				return True
			else:
				i = i.next
		# si no se encuentra el entero, retorna False
		return False

	# recibe un elemento tipo conjunto y lo une con el conjunto
	def Union(self,conjunto):
		# el conjunto dado es una lista enlazada de elementos de tipo entero
		# revisar que si hay elementos comunes entre los conjuntos (self.size y conjunto.size) y 
		# 		crear un nuevo conjunto con los elementos no comunes y comunes (una sola vez)
		C = Conjunto()
		primero_A = self.first
		primero_B = conjunto.first
		while primero_A != None:
			C.Agregar(primero_A.numero)
			primero_A = primero_A.next
		while primero_B != None:
			if self.Pertenece(primero_B.numero) == False:
				C.Agregar(primero_B.numero)
			primero_B = primero_B.next
		return C


	# recibe un elemento tipo conjunto y lo intersecta con el conjunto
	def Interseccion(self,conjunto):
		# el conjunto dado es una lista enlazada de elementos de tipo entero
		C = Conjunto()
		primero_B = conjunto.first
		while primero_B != None:
			if self.Pertenece(primero_B.numero) == True:
				C.Agregar(primero_B.numero)
			primero_B = primero_B.next
		return C

	def Mostrar(self):
		i = self.first
		L =  []
		first = self.first
		while first != None:
			L.append(first.numero)
			first = first.next
		print("{"+str(L)+"}")

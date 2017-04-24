
"""
Implementacion de el TAD  Conjunto, con una estructura conjunto que representa 
una lista enlazada simple, que va a contener elementos de tipo entero

Autor: Orlando Chaparro    Carnet: 12-11499

Ultima modificacion:
	 
	 Jueves, 30 de marzo de 2017 - Semana 12
"""

class Elemento:

	def __init__(self, e, n):
		""" 
		Crea un elemento que sera agregado a la lista enlazada 
		"""
		self.elemento = e
		self.next = n


class Conjunto:

	def crearConjunto(self):

		""" 
		Crea un nuevo conjunto. Como el TAD Conjunto está implementado con una clase,
		entonces esta operación corresponde al constructor de la clase. 
		
		"""
		self.head = None
		self.tail = None
		self.cantidadElem = 0

		
	def agregar(self, e):
		
		"""
		Agrega un elemento de tipo entero al conjunto

		"""
		NuevoElemento = Elemento(elemento, None)

		if self.cantidadElem == 0:
			self.head = NuevoElemento
			self.tail = NuevoElemento
			self.cantidadElem += 1
		
		elif self.cantidadElem >= 1:
			self.tail.next = NuevoElemento
			self.cantidadElem += 1

	def pertenece(self, e):

		""" 
		Determina si un elemento esta o no en el conjunto. Si el elemento ya forma parte del conjunto, 
		retorna True, en caso contrario retorna False

		"""
		aux = self.head

		if self.cantidadElem == 0:
			print("No existen elementos en el conjunto finito")
			return False


		while aux is not None and aux.elemento != e:
			aux = aux.next
		
		if aux is None:
			return False

		if aux.elemento == e
			return True


	def union(self, conjunto):

		if self.cantidadElem == 0:

			return conjunto

		else:

			ConjuntoFinal = Conjunto()
			Aux1 = self.head
			Aux2 = conjunto.head

			while Aux1 is not None:
				ConjuntoFinal.agregar(Aux1.elemento)
				Aux1 = Aux1.next

			while Aux2 is not None:
				ConjuntoFinal.agregar(Aux2.elemento)
				Aux2 = Aux2.next

			return ConjuntoFinal
	
	def interseccion(self, conjunto):

		ConjuntoFinal = Conjunto()

		Aux1 = self.head
		Aux2 = conjunto.head

		if self.cantidadElem == 0
			ConjuntoFinal.agregar(0)
			return ConjuntoFinal

		else: 
			while Aux1 is not None and Aux2 is not None:
				if Aux1.elemento == Aux2.elemento:
					ConjuntoFinal.agregar(Aux1.elemento)

				Aux1 = Aux1.next
				Aux2 = Aux2.next

	def Mostrar(self):
		aux = self.head
		while aux is not None:
			print(aux)
			aux = aux.next





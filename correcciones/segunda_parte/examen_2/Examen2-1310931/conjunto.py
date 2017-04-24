#
#Universidad Simon Bolivar
#Laboratorio de Algoritmos II
#Examen 2
#Autor: ANgel Morante
#Carnet: 13-10931
#



#Descripcion: Clase que define los elementos en el conjunto
#			  donde cada elemento tiene un atributo .next
#			  para poder aplicar la implementacion de un lista
#			  enlazada simple.
class elemento:
	def __init__(self,e,n):
		self.elemento = e
		self.next = n

#Descripcion: CLase que implementa una lista enlazada simple
#			  para hacer el equivalente a un conjunto finito
#			  de numeros enteros
class Conjunto:

	def __init__(self):
		"""Construcctor de la clase"""
		self.head = None # Atributo que apunta a la cabeza de la lista
		self.tail = None # Atributo que apunta a la cola de la lista
		self.cardinalidad = 0 #Atributo que indica la cantidad de elemento en la lista ("Cardinalidad del COnjunto")
		self.Conjunto = [] #Atributo del conjunto en si mismo

	def Agregar(self,e):
		#Descripcion: Agrega un elemento de tipo entero al conjunto
		#Entradas: e de Tipo entero

		NuevoElemento = elemento(e,None)

		#Caso 1: DOne el conjunto es un conjunto Vacio inicialmente
		if self.cardinalidad == 0:
			self.head = NuevoElemento
			self.tail = NuevoElemento
			self.cardinalidad +=1

		#Caso 2: DOnde exista al menos un elemento en el conjunto
		elif self.cardinalidad > 0:
			curNodo = self.head
			while curNodo is not None and curNodo.elemento!= NuevoElemento.elemento:
				curNodo = curNodo.next

			if curNodo == None:
				self.tail.next = NuevoElemento
				self.tail = NuevoElemento
				NuevoElemento.next = None
			else:
				return

	def Pertenece(self,e):
		#Descripcion: Determian si un elemento esta o no en el conjunto
		#			  SI el elemento esta en el conjunto retorn True, 
		#			  De lo contrario retorna False
		#Entradas: e: del tipo elemento
		#Salida: True o False
		curNodo = self.head
		while curNodo is not None and curNodo.elemento != e:
			curNodo = curNodo.next

		if curNodo is None:
			return False
		if curNodo.elemento == e:
			return True


	def Union(self,c):
		#Descripcion: Este metodo recibe como entrada a un conjunto c
		#			  y retorna un nuevo conjunto que es la union del 
		#			  del conjunto acutla(self) y el conjunto c
		#Entradas: c: obejeto del tipo Conjunto
		#Salidas: U: objeto del tipo conjunto que es la union de ambos conjuntos

		ConjuntoUnion = Conjunto() #OJO AQUI ESTO PUEDE CAUSAR PROBLEMAS ANGEL
		curNodo1 = self.head
		curNodo2 = c.head
		
		while curNodo1 is not None:

			ConjuntoUnion.Agregar(curNodo1.elemento)
			curNodo1 = curNodo1.next

		while curNodo2 is not None:

			ConjuntoUnion.Agregar(curNodo2.elemento)
			curNodo2 = curNodo2.next

		return ConjuntoUnion


	def Interseccion(self,c):
		#Descripcion: Recibe como entrada un conjunto c y retorna un nuevo conjunto
		#  			  Cuyos elementos son la interseccion del cunjutno self y el actual(self)
		#ENtrada: c: onbejto del tipo conjunto
		#Salida: U: del tipo COnjunto

		curNodo1 = self.head 
		curNodo2 = c.head
		ConjuntoInterseccion = Conjunto()


		while curNodo1 is not None:
			while curNodo2 is not None:
				print(curNodo2.elemento)
				if c.Pertenece(curNodo1.elemento) and self.Pertenece(curNodo2.elemento):
					ConjuntoInterseccion.Agregar(curNodo1.elemento)
					break

				curNodo2 = curNodo2.next

			curNodo1 = curNodo1.next


		return ConjuntoInterseccion


	def Mostrar(self):
		#Descripccion: Muestra los elementos en el conjunto actual
		curNodo = self.head
		print("-----Los elementos del conjunto son: -----\n")
		arreglo = []
		while curNodo is not None:
			arreglo.append(curNodo.elemento)
			curNodo = curNodo.next
		print(arreglo)






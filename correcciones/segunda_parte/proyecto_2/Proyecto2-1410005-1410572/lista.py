from arrayT import ArrayT
from cancion import Cancion
def ListSort(L, comparator):
	
	# Base
	if L.size <= 1:
		return L

	# MiniList a
	a = ListaReproduccion()
	
	# MiniList b
	b = ListaReproduccion()

	# Sorted List
	_sorted =  ListaReproduccion()

	# Add elements
	cursor = L.proxima
	for i in range(L.size//2):
		a.agregar_final(cursor.elemento)
		cursor = cursor.siguiente

	for i in range((L.size+1)//2):
		b.agregar_final(cursor.elemento)
		cursor = cursor.siguiente
	
	# Recursive call
	a = ListSort(a, comparator)
	b = ListSort(b, comparator)
	
	# Return list
	return ListMerge(a,b, comparator)

def ListMerge(a, b, comparator):
	_sorted =  ListaReproduccion()

	while a.size > 0 and b.size > 0:
		
		comparation = b.proxima.elemento.es_menor_artista(a.proxima.elemento)

		if comparator == "titulo":
			comparation = b.proxima.elemento.es_menor_titulo(a.proxima.elemento)
		
		if comparation:
			_sorted.agregar_final(b.proxima.elemento)
			b.eliminar(b.proxima.elemento.titulo)
		else:
			_sorted.agregar_final(a.proxima.elemento)
			a.eliminar(a.proxima.elemento.titulo)

	if a.size > 0:
		while a.size > 0:
			_sorted.agregar_final(a.proxima.elemento)
			a.eliminar(a.proxima.elemento.titulo)
	else:
		while b.size > 0:
			_sorted.agregar_final(b.proxima.elemento)
			b.eliminar(b.proxima.elemento.titulo)

	return _sorted

class NodoLista:
	def __init__(self, e, s, a):
		self.elemento = e
		self.siguiente = s
		self.anterior = a

class ListaReproduccion:
	def __init__(self):
		self.size = 0
		self.proxima = NodoLista(None, None, None)
		self.proxima.siguiente = self.proxima
		self.proxima.anterior  = self.proxima

	def agregar_final(self, e):
		if self.size == 0:
			node = NodoLista(e, None, None)
			node.anterior  = node
			node.siguiente = node
			self.proxima = node
		else:
			# Revisa si ya existe la cancion:
			top = self.proxima
			
			for i in range(self.size):
				if top != None and e.es_igual(top.elemento):
					print("Error, ha intentado agregar una cancion que ya existe")
					return
				top  = top.siguiente

			node = NodoLista(e, self.proxima, self.proxima.anterior)
			self.proxima.anterior.siguiente =  node
			self.proxima.anterior = node

		self.size = self.size + 1

	def agregar(self, e):
		
		if self.size == 0:
			node = NodoLista(e, None, None)
			node.anterior  = node
			node.siguiente = node
			self.proxima = node
		else:
			# Revisa si ya existe la cancion:
			top = self.proxima
			
			for i in range(self.size):
				if top != None and e.es_igual(top.elemento):
					print("Error, ha intentado agregar una cancion que ya existe")
					return
				top  = top.siguiente
			old = self.proxima

			node = NodoLista(e, old, old.anterior)
			old.anterior.siguiente = node
			old.anterior = node
			self.proxima = node

		self.size = self.size + 1
		
	def ordenar_titulo(self):  
		if self.size == 0: 
			return
		return ListSort(self, "titulo")
		
	def ordenar_artista(self):
		if self.size == 0:
			return

		return ListSort(self, "artista")

	def eliminar(self, tituloCancion):
		# Implementa una busqueda lineal
		first = self.proxima
		for i in range(self.size):
			if first.elemento != None and first.elemento.titulo == tituloCancion: 
				first.anterior.siguiente = first.siguiente
				first.siguiente.anterior = first.anterior
				self.size = self.size - 1
				if first == self.proxima:
					self.proxima = first.siguiente
				if self.size == 0:
					self.__init__()
				return

			first  = first.siguiente
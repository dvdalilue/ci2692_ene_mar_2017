# EXAMEN 2

# DESCRIPCIÓN: Se quiere implementar el equivalente a la estructura matemática conocida 
# como conjunto finito. En específico debe implementar un TAD Conjunto, en donde la estructura
# conjunto es una lista enlazada simple, que va a contener elementos de tipo entero.

# AUTOR: DAVID SEGURA 13-11341
# CORREO: 13-11341@usb.ve

class Nodo(object):
	# NODO QUE SE USARA PARA IMPLEMENTAR LA LISTA ENLAZADA
	def __init__(self,elemento,siguiente):
		self.element = elemento
		self.next = siguiente

class Conjunto(object):
	# ESTRUCTURA QUE SE USARA PARA LA IMPLEMENTACIÓN DE UN
	# CONJUNTO
	def __init__(self):
		self.conjunto = None
		self.proximo = self.conjunto

	def crearConjunto(self):
		# CREA CONJUNTO VACIO
		self.conjunto = Nodo(None,None)

	def agregar(self,e):
		# AGREGA ELEMENTOS AL CONJUNTO
		if self.conjunto.element == None:
			self.conjunto.element = e
			self.proximo = self.conjunto
		else:
			if self.pertenece(e) == True:
				pass
			else:
				self.proximo.next = Nodo(e,None)
				self.proximo = self.proximo.next

	def pertenece(self,e):
		# DETERMINA SI UN ELEMENTO ESTÁ O NO EN EL CONJUNTO
		lista = self.conjunto
		while lista != None:
			if lista.element == e:
				return True
			else:
				lista = lista.next
		return False

	def union(self,c):
		# ESTA FUNCIÓN UNE A DOS CONJUNTOS
		lista = c.conjunto
		while lista != None:
			self.agregar(lista.element)
			lista = lista.next
		return self.conjunto

	def interseccion(self,c):
		# REALIZA LA INTERSECCIÓN DE AMBOS CONJUNTOS
		conjuntonuevo = Conjunto()
		conjuntonuevo.crearConjunto()
		lista2 = c.conjunto
		while lista2 != None:
			if self.pertenece(lista2.element) == True:
				conjuntonuevo.agregar(lista2.element)
				lista2 = lista2.next
			else:
				lista2 = lista2.next
		return conjuntonuevo

	def mostrar(self):
		# MUESTRA LOS ELEMENTOS DEL CONJUNTO
		lista = self.conjunto
		while lista != None:
			print(str(lista.element))
			lista = lista.next
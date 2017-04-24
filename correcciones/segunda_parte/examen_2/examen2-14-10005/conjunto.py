class Elemento():
	def __init__(self,valor,siguiente):
		self.value = valor
		self.next = siguiente

class Conjunto():
	def __init__(self):
		self.head = None

	def Agregar(self,e):
		if not self.Pertenece(e):
			agregar = Elemento(e,self.head)
			self.head = agregar

	def Pertenece(self,e):
		x = self.head
		while x != None:
			if x.value == e:
				return True
			x = x.next

		return False

	def Union(self,c):
		nuevo_conjunto = Conjunto()
		x = self.head
		while x != None:
			nuevo_conjunto.Agregar(x.value)
			x = x.next

		y = c.head
		while y != None:
			nuevo_conjunto.Agregar(y.value)
			y = y.next

		return nuevo_conjunto

	def Interseccion(self,c):
		nuevo_conjunto = Conjunto()
		x = self.head
		while x != None:
			if c.Pertenece(x.value):
				nuevo_conjunto.Agregar(x.value)
			
			x = x.next

		return nuevo_conjunto

	def Mostrar(self):
		x = self.head
		while x != None:
			print(x.value)
			x = x.next

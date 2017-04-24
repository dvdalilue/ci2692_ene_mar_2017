class Nodo:
	def __init__(self, e, s):
		self.elemento = e
		self.next = s

class Conjunto:
	def __init__(self):
		self.crearConjunto()

	def crearConjunto(self):
	#Creamos un conjunto como lista enlazada vacía
		self.head=None

	def pertenece(self,elem):
		#Determina si un elemento pertenece al conjunto
		#Usando busqueda para listas enlazadas
		x=self.head
		while x!=None and x.elemento!=elem:
			x=x.next
		
		if x==None:
			return False
		elif x.elemento==elem:
			return True

	def agregar(self, elemento):
		#Agrega un elemento de tipo entero al conjunto
		#Si la lista esta vacia
		elemento=Nodo(elemento,None)
		if self.head==None:
			self.head=elemento
		#Si hay mas elementos en la lista
		else:
			elemento.next=self.head
			self.head=elemento


	def union(self,A):
		#Realiza la union de dos conjuntos
		#Se agregan los elementos del conjunto A a nuestro conjunto
		x=A.head
		while x!=None:
			if self.pertenece(x.elemento)==True:
				x=x.next
			else:
				self.agregar(x.elemento)
				x=x.next
		return self

	def interseccion(self,A):
		#Realiza la interseccion de dos conjuntos
		#Se ve si cada elemento de A pertenece a self, si es asi se agrega a un nuevo conjunto
		C=Conjunto()
		x=A.head
		while x!=None:
			if self.pertenece(x.elemento)==True:
				C.agregar(x.elemento)
				x=x.next
			else:
				x=x.next
		return C

	def mostrar(self):
		#Muestra los elementos de la lista
		#Se agregaran los elementos a una lista de python para mostrarlos en pantalla
		x=self.head
		lista=[]
		while x!=None:
			lista.append(x.elemento)
			x=x.next
		print("Los elementos del conjunto son "+ str(lista))



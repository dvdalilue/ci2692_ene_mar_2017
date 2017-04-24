#Aurivan Castro 14-10205

#Clase Nodo para usar en la lista enlazada conjunto
class Nodo:
	def __init__(self,elemento):
		self.elemento=elemento
		self.next=None

#Clase conjunto que contine nodos con enteros
class Conjunto:
	def __init__(self):
		self.crearConjunto()

	def crearConjunto(self):
		#Crea el conjunto
		self.head=None

	def Pertenece(self, entero):
		#Recorre toda la lista enlazada hasta encontrar el elemento, en cuyo caso retorna True.
		#De lo contrario retorna False
		x=self.head
		while x!=None:
			if x.elemento==entero:
				return True
			x=x.next
		return False

	def Agregar(self, entero):
		#Agrega un elemento al conjunto
		pert= self.Pertenece(entero) #Evalua si dicho entero ya esta en el conjunto
		if pert: #Si el entero esta no hacer nada
			return
		else: #Si el entero no esta, agregarlo al inicio de la lista
			nodo=Nodo(entero)
			if self.head==None:
				self.head=nodo
				return
			nodo.next=self.head
			self.head=nodo

	def Union(self,conjunto):
		#Dado un conjunto, retorna la union de ambos
		if len(conjunto)==0:
			print("El conjunto dado no tiene elementos.")
			return
		for i in conjunto:
			self.Agregar(i)
		return self

	def Interseccion(self,conjunto):
		#Dado un conjunto, retorna la interseccion de ambos
		if len(conjunto)==0:
			print("El conjunto dado no tiene elementos.")
			return
		arreglo=[ ]
		for i in conjunto:
			if self.Pertenece(i):
				arreglo=arreglo+[i]
		nuevoCjto=Conjunto()
		if len(arreglo)==0:
			return nuevoCjto
		for i in arreglo:
			nuevoCjto.Agregar(i)
		return nuevoCjto

	def Mostrar(self):
		#Muestra los elementos del conjunto
		if self.head==None:
			print("La lista esta vacia")
			return
		x=self.head
		salida="["+str(x.elemento)
		x=x.next
		while x!=None:
			salida= salida+","+str(x.elemento)
			x=x.next
		salida=salida+"]"
		print(salida)
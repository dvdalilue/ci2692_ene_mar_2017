from cancion import Cancion
from arrayT import ArrayT

class NodoLista:
	def __init__(self, e, s, a):
		self.elemento = e
		self.siguiente = s
		self.anterior = a

class ListaReproduccion:
	def __init__(self):
		self.proxima = None
		self.numero_nodos=0

	def agregar_final(self,e):
		cancion=NodoLista(e,None,None)
		if self.numero_nodos==0:
			self.proxima=cancion
			cancion.siguiente=cancion
			cancion.anterior=cancion
			self.numero_nodos=1
		else:
			#Debemos asegurarnos de que la cancion que se intenta agregar no esta en la lista
			x=self.proxima
			val=x.elemento.es_igual(e)
			if val==True:
				print("La cancion que intenta agregar ya se encuentra en la lista.")
				return
			y=x.siguiente
			while y!=x:
				val=y.elemento.es_igual(e)
				if val==True:
					print("La cancion que intenta agregar ya se encuentra en la lista.")
					return
				y=y.siguiente
			#La cancion no esta en la lista, se debe agregar
			if self.numero_nodos==1:
				x.siguiente,x.anterior=cancion,cancion
				cancion.anterior,cancion.siguiente=x,x
				self.proxima=cancion
				self.numero_nodos=2
			elif self.numero_nodos!=1:
				cancion_sonando=x.anterior
				cancion_sonando.siguiente=cancion
				cancion.anterior=cancion_sonando
				cancion.siguiente=x
				x.anterior=cancion
				self.numero_nodos=self.numero_nodos+1
		#print("proxima es la cancion con titulo "+ self.proxima.elemento.titulo)

	def agregar(self,e):
		cancion=NodoLista(e,None,None)
		if self.numero_nodos==0:
			self.proxima=cancion
			cancion.siguiente=cancion
			cancion.anterior=cancion
			self.numero_nodos=1
		else:
			#Debemos asegurarnos de que la cancion que se intenta agregar no esta en la lista
			x=self.proxima
			val=x.elemento.es_igual(e)
			if val==True:
				print("La cancion que intenta agregar ya se encuentra en la lista.")
				return
			y=x.siguiente
			while y!=x:
				val=y.elemento.es_igual(e)
				if val==True:
					print("La cancion que intenta agregar ya se encuentra en la lista.")
					return
				y=y.siguiente
			#La cancion no esta en la lista, se debe agregar	
			if self.numero_nodos==1:
				x.siguiente,x.anterior=cancion,cancion
				cancion.anterior,cancion.siguiente=x,x
				self.proxima=cancion
				self.numero_nodos=2
			elif self.numero_nodos!=1:	
				cancion.anterior=x.anterior
				cancion.siguiente=x
				x.anterior.siguiente=cancion
				x.anterior=cancion
				self.proxima=cancion
				self.numero_nodos=self.numero_nodos+1
	
	def split(self,head):
		#Divide la lista circular en dos, tomamos self.proxima.siguiente como si fuera None
		#en una lista doblemente enlazada
		primero=segundo=head
		while True:
			if primero.siguiente==None:
				break
			if primero.siguiente.siguiente==None:
				break
			primero=primero.siguiente.siguiente
			segundo=segundo.siguiente
		temp = segundo.siguiente
		segundo.siguiente = None
		return temp
		
	def merge_titulo(self,primero,segundo):
		#Si la primera lista no tiene nada
		if primero is None:
			return segundo
		#Si la segunda lista no tiene nada
		if segundo is None:
			return primero
		
		#Escoge el menor
		if primero.elemento.es_menor_titulo(segundo.elemento)==True:
			primero.siguiente = self.merge_titulo(primero.siguiente, segundo)
			primero.siguiente.anterior = primero
			primero.anterior = None
			return primero
		else:
			segundo.siguiente=self.merge_titulo(primero,segundo.siguiente)
			segundo.siguiente.anterior = segundo
			segundo.anterior = None
			return segundo
	
	def mergesort_titulo(self,head):
		#Aplicamos el procedimiento
		if head is None:
			return head
		if head.siguiente is None:
			return head
		
		segundo=self.split(head)
		#Se aplica recursivamente sobre las dos mitades
		head=self.proxima=self.mergesort_titulo(head)
		segundo=self.mergesort_titulo(segundo)
		return self.merge_titulo(head,segundo)
		
	def ordenar_titulo(self):
		#Comenzamos conviertiendo la lista circular en una doblemente enlazada
		#para poder dividir en dos la lista y aplicar el procedimiento de forma
		#recursiva sin perder la propiedad in-place del algoritmo
		#Tomamos self.proxima como la ultima de la lista y self.proxima.siguiente como el primero
		head=self.proxima.siguiente
		head.anterior=None
		self.proxima.siguiente=None

		head=self.mergesort_titulo(head)
		ultimo=head
		while ultimo.siguiente!=None:
			ultimo=ultimo.siguiente
		#Volvemos a unir la lista para que sea circular
		head.anterior=ultimo
		ultimo.siguiente=head
		self.proxima=head

	def merge_artista(self,primero,segundo):
		#Si la primera lista no tiene nada
		if primero is None:
			return segundo
		#Si la segunda lista no tiene nada
		if segundo is None:
			return primero
		
		#Escoge el menor
		if primero.elemento.es_menor_artista(segundo.elemento)==True:
			primero.siguiente = self.merge_artista(primero.siguiente, segundo)
			primero.siguiente.anterior = primero
			primero.anterior = None
			return primero
		else:
			segundo.siguiente=self.merge_artista(primero,segundo.siguiente)
			segundo.siguiente.anterior = segundo
			segundo.anterior = None
			return segundo
	
	def mergesort_artista(self,head):
		#Aplicamos el procedimiento
		if head is None:
			return head
		if head.siguiente is None:
			return head
		
		segundo=self.split(head)
		#Se aplica recursivamente sobre las dos mitades
		head=self.proxima=self.mergesort_artista(head)
		segundo=self.mergesort_artista(segundo)
		return self.merge_artista(head,segundo)
	
	def ordenar_artista(self):
		#Comenzamos conviertiendo la lista circular en una doblemente enlazada
		#para poder dividir en dos la lista y aplicar el procedimiento de forma
		#recursiva sin perder la propiedad in-place del algoritmo
		#Tomamos self.proxima como la ultima de la lista y self.proxima.siguiente como el primero
		head=self.proxima.siguiente
		head.anterior=None
		self.proxima.siguiente=None

		head=self.mergesort_artista(head)
		ultimo=head
		while ultimo.siguiente!=None:
			ultimo=ultimo.siguiente
		#Volvemos a unir la lista para que sea circular
		head.anterior=ultimo
		ultimo.siguiente=head
		self.proxima=head

	def eliminar(self,tituloCancion):
		if self.numero_nodos==0:
			print("La lista de reproduccion no tiene ningun elemento.")
		x=self.proxima
		y=x.siguiente
		#Comparamos el string con todos los elementos menos el self.proxima
		while y!=x:
			if y.elemento.titulo==tituloCancion:
				break
			y=y.siguiente
		if y==x.anterior:
			#En este caso, se trataria de eliminar la cancion que esta en
			#reproduccion, lo cual no debe permitirse.
			print("La cancion que intenta eliminar esta en reproduccion. Intente con otra cancion o espere hasta que la cancion actual culmine para eliminarla.")
			return
		if y!=x:
			#Si alguno de los elementos de la lista tienen el tituloCancion
			#como titulo, se toma dicho elemento para elminar.
			y.anterior.siguiente=y.siguiente
			y.siguiente.anterior=y.anterior
			self.numero_nodos=self.numero_nodos-1
			print("El elemento se elimino")
			return
		if y==x and x.elemento.titulo==tituloCancion:
			#Si ninguno de los elementos de la lista diferentes de self.proxima
			#tienen el string de titulo pero self.proxima si lo tiene, se toma
			#dicho elemento para eliminar.
			if self.numero_nodos==1:
				self.proxima=None
				self.numero_nodos=self.numero_nodos-1
			elif self.numero_nodos>1:
				y.anterior.siguiente=y.siguiente
				y.siguiente.anterior=y.anterior
				self.numero_nodos=self.numero_nodos-1
				self.proxima=y.siguiente
			print("El elemento se elimino")
			return
		print("No existe ninguna cancion en la lista con el titulo dado.")
		return

	def Imprimir_lista(self):
		if self.numero_nodos==0:
			print("La lista de reproduccion no tiene ningun elemento. Agregue una cancion por medio de la opcion del menu correspondiente.")
		else:
			print("\nSe imprimiran las canciones desde la cancion que esta en reproduccion")
			y=self.proxima.anterior
			print("Artista    -   Cancion\n")
			contador=0
			while contador!=self.numero_nodos:
				contador+=1
				print(y.elemento.artista + "  -  " + y.elemento.titulo)
				y=y.siguiente
			print("\n")



import sys
from cancion import *
#####################################################################

# Descripcion: Constructor de la clase NodoLista, que contiene
#              elementos de tipo 'cancion' y sus doble enlaces
#              siguiente y anterior.
# Atributos: cancion: Elemento de tipo 'cancion'
#            siguiente: Elemento siguiente a elemento 'cancion'
#            anterior: Elemento anterior a elemento 'cancion'
#
# Autor: Orlando Chaparro Carnet: 12-11499
#         Angel Morante Carnet: 13-10931
# email: 12-11499@usb.ve
#        13-10931@usb.ve // morante413@gmail.com

class NodoLista:
	def __init__(self, e, s = None, a=None):
		self.elemento = e
		self.siguiente = s
		self.anterior = a

# Descripcion: Constructor de la clase ListaReproduccion, con
#              las operaciones agregar, eliminar y ordenar.

class ListaReproduccion:
	def __init__(self):
		self.proxima = None #Atributo de instancia que guarda una referencia a la proxima cancion a sonar
		self.numero_nodos = 0 #Atributo de instancia que indica la cantidad de canciones en la lista de reproduccion

	def agregar_final(self,e):

		if self.numero_nodos == 0:
			Nuevo_nodo = NodoLista(e,e,e)
			self.proxima = Nuevo_nodo.elemento
			self.numero_nodos += 1
		elif self.numero_nodos >0:
			Nuevo_nodo = NodoLista(e,self.proxima,self.proxima.anterior)
			self.numero_nodos +=1


	def agregar(self,e):

		nuevaCancion = NodoLista(e) # Se almacena la cancion en un NODO             
		
		# En caso de que la lista de reproduccion este vacia
		# el nodo con la cancion, se agrega en la 'cabeza' de la lista
		# y como es circular doblemente enlazada, se asigna el mismo nodo
		# a los metodos 'next' y 'prev'.
		
		if self.proxima == None:
			nuevaCancion.anterior = nuevaCancion
			nuevaCancion.siguiente = nuevaCancion
			self.proxima = nuevaCancion
			self.numero_nodos += 1


		else:
			curNode = self.proxima
			while curNode.siguiente is not self.proxima:
				if curNode.elemento.es_igual(e):
					return
				else:
					curNode = curNode.siguiente
					if curNode == self.proxima.anterior:
						if curNode.elemento.es_igual(e):
							return
			
			
			viejaCancion = self.proxima.anterior
			viejaCancion.siguiente = nuevaCancion
			nuevaCancion.anterior = viejaCancion
			nuevaCancion.siguiente = self.proxima
			self.proxima.anterior = nuevaCancion
			self.numero_nodos += 1



	def ordenar_titulo(self):
		return Mergesort_titulo(self)
					


	def ordenar_artista(self):
		return Mergesort_artista(self)

	def eliminar(self,tituloCancion):
		
		title = tituloCancion
		encontrado = False
		aux = self.proxima

		if self.numero_nodos ==0:
			print("No hay canciones en la lista")

		elif self.numero_nodos >0:
			while aux.elemento.titulo != title and not encontrado:
				
				if aux.elemento.titulo == title:
				# Si la encontramos, salimos del ciclo asignando:
					encontrado = True
				else:
					aux = aux.siguiente
				if aux == self.proxima and not encontrado:
				# Este caso sucede si no se encuentra la cancion
				#entonces nos salimos del ciclo  imprimimos
					print ("La cancion no existe")
					return

		# Una vez terminado el ciclo y encontrado la 'cancion' en la lista,
		# la variable 'aux' contiene el Nodo en donde esta la 'cancion'

		if aux == self.proxima and aux.siguiente == self.proxima and aux.anterior == self.proxima:
			#Caso en el que la lista contiene solo un elemento
			self.numero_nodos -=1
			self.proxima == None
		else:
			# Caso donde la lista tiene mas de un elemento:
			if aux == self.proxima:
				# En caso de que se quiera eliminar la cancion contenida en
				# la cabeza de la lista, la cabeza pasa a ser el nodo siguiente.
				self.proxima = aux.siguiente
				
			# Enlazamos el nodo anterior a NodoAux con el nodo siguiente a NodoAux.
			aux.anterior.siguiente = aux.siguiente
			aux.siguiente.anterior = aux.anterior
			self.numero_nodos -= 1  


#####################################################################
#       MERGESORT PARA LISTAS CIRCULARES DOBLEMENTE ENLAZADAS       #
#####################################################################


# ORDENAMIENTO POR TITULO

def Mergesort_titulo(lista_doblemente_circular):
	
	if lista_doblemente_circular.proxima is lista_doblemente_circular.proxima.siguiente:
		return lista_doblemente_circular
		
	rlist = Dividir_sub_arr(lista_doblemente_circular)
	llist = lista_doblemente_circular
	
	llist = Mergesort_titulo(llist)
	rlist = Mergesort_titulo(rlist)
	
	lista_doblemente_circular = merge_titulo(llist,rlist)
	
	return lista_doblemente_circular


# ORDENAMIENTO POR ARTISTAS  
def Mergesort_artista(lista_doblemente_circular):
	
	if lista_doblemente_circular.proxima is lista_doblemente_circular.proxima.siguiente:
		return lista_doblemente_circular
		
	rlist = dividirLCD(lista_doblemente_circular)
	llist = lista_doblemente_circular
	
	llist = Mergesort_artista(llist)
	rlist = Mergesort_artista(rlist)
	
	lista_doblemente_circular = merge_artista(llist,rlist)
	
	return lista_doblemente_circular

# MERGE: COMBINAR ORDENADAMENTE LAS SUBLISTAS - TITULO
def merge_titulo(subListA,subListB):
	newList = ListaReproduccion()
	listI = subListA.proxima
	listD = subListB.proxima

	while subListA.proxima is not None and subListB.proxima is not None:
		if listI.elemento.es_menor_titulo(listD.elemento)==True:
			newList.agregar(listI.elemento)
			subListA.eliminar(listI.elemento)
			listI = listI.siguiente
		else:
			newList.agregar(listD.elemento)
			subListB.eliminar(listD.elemento)
			listD = listD.siguiente
	
	while subListA.proxima is not None:
		newList.agregar(listI.elemento)
		subListA.eliminar(listI.elemento)
		listI = listI.siguiente
			
	while subListB.proxima is not None:
		newList.agregar(listD.elemento)
		subListB.eliminar(listD.elemento)
		listD = listD.siguiente
		
	return newList

# MERGE: COMBINAR ORDENADAMENTE LAS SUBLISTAS - ARTISTAS
def merge_artista(subListA,subListB):
	newList = ListaReproduccion()
	listI = subListA.proxima
	listD = subListB.proxima
	while subListA.proxima is not None and subListB.proxima is not None:
		if listI.elemento.artista <= listD.elemento.artista:
			newList.agregar(listI.elemento)
			subListA.eliminar(listI.elemento)
			listI = listI.siguiente
		else:
			newList.agregar(listD.elemento)
			subListB.eliminar(listD.elemento)
			listD = listD.siguiente
		
	while subListA.proxima is not None:
		newList.agregar(listI.elemento)
		subListA.eliminar(listI.elemento)
		listI = listI.siguiente
			
	while subListB.proxima is not None:
		newList.agregar(listD.elemento)
		subListB.eliminar(listD.elemento)
		listD = listD.siguiente

	return newList


# DIVIDIR LAS LISTAS EN VARIAS SUBLISTAS
def Dividir_sub_arr(subLista):
	PuntoMed = subLista.proxima
	curNode = PuntoMed.siguiente
	while curNode is not subLista.proxima:
		
		curNode = curNode.siguiente
		
		if curNode is not subLista.proxima:
			PuntoMed = PuntoMed.siguiente
			curNode = curNode.siguiente
	
	listaD = ListaReproduccion()
	listaD.proxima = PuntoMed.siguiente
	PuntoMed.siguiente.anterior = subLista.proxima.anterior
	subLista.proxima.anterior.siguiente = listaD.proxima
	PuntoMed.siguiente = subLista.proxima
	subLista.proxima.anterior = PuntoMed

	return listaD

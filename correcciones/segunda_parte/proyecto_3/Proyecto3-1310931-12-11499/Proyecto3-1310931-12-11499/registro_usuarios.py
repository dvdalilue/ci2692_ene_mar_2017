from usuario import *
import hashlib


# Descripcion: Clase que implementa elementos de tipo HashEntry
# Atributos: clave: Clave que se asociara a un dato
#			 dato: String asociado a la clave
#            value: Valor siguiente
class HashEntry:
	def __init__(self,clave,dato,value = None):
		self.prev = value
		self.clave = clave
		self.dato = dato
		self.next = value
# Descripcion: Clase que implementa las lista doblemente enlazadas
class dList:
	def __init__(self):
		self._head = None
		self._size = 0
		self._last = None

	# Descripcion: Agrega un elemento a la lista
	# Atributos: e: elemento de tipo HashEntry a ser agregado a la lista
	def add(self, e):
		if self._size == 0:
			self._size += 1
			self._head = e
			self._last = e
			e.next = None
			e.prev = None

		elif self._size > 0:
			self._size +=1
			e.next = None
			e.prev = self._last
			self._last = e
		
	
	#Elimina un elemento en una lista
	def remove(self,e):

		#assert self._head is None, "El elemento tiene que estar en la lista para poder eliminarlo."

		#Considera el caso en el que el elemento es el primero en la lista
		if self._head is not None:
			if e.dato.nombre == self._head.dato.nombre:
				self._head = self._head.next
				#self._head.prev = None
				self._size -= 1

			Nodo = None
			NodoMax = self._head

			while e.dato.nombre != NodoMax.dato.nombre and NodoMax is not None:
				Nodo = NodoMax
				NodoMax = NodoMax.next

			if NodoMax.dato.nombre != e.dato.nombre:
				print("El elemento debe estar contenido para poder ser eliminado")
				return

			
			elif NodoMax.next == None:
				Nodo.next = None
			else:
				Nodo.next = NodoMax.next
				NodoMax.next.prev = Nodo

			self._size = self._size - 1

			return NodoMax.clave
		else:
			print("No esta en la lista")
			return

	
	#Determina si la Lista esta vacia
	def vacia(self):
		vacio=False
		if self._size==0:
			vacio=True
		return vacio

   
	#Busca un elemento en la lista
	def buscar(self,e):
		y = None
		x = self._head
		while x is not None and e.dato.nombre != x.dato.nombre:
			y = x
			x = x.next


		return x
	
	# Descripcion: Determina si un elemento se encuentra en la lista 
	#              y devuelve dicho elemento
	# Atributos: e: elemento de tipo HashEntry a ser buscado en la lista
	# Retorna: curNode: elemento de tipo HashEntry encontrado
	def contain(self, e):
		curNode = self._head
		while curNode is not None and curNode.clave != e.clave:
			curNode = curNode.next
		return curNode

	# Descripcion: Determina si un elemento se encuentra en la lista
	# Atributos: e: elemento de tipo HashEntry a ser buscado en la lista
	# Retorna: True si el elemento esta en la lista y False si no.
	def __contains__(self, e):
		curNode = self._head
		while curNode is not None and curNode.clave != e.clave:
			curNode = curNode.next
		return curNode is not None   



class RegistrodeUsuarios:

	def __init__(self,n):
		self.n = n #Tamano de la tabla d hash y cantidad de elementos en ella
		self.TablaRU =[dList() for x in range(n)] #Tabla de hash donde cada slot es una lista doblemente enlazada de tipo dList

	
	"""Se  agrega  un  elementoude  tipoUsuarioen  la  tablatablaRU
	.  La clave va a ser el nombre del usuariou. Si la clave del elemento a agregar se encuentra
	en la tabla de usuarios, se retorna True. Por el contrario, si no logra agregarlo dadoa que el
	 usuario ya se encuentra registrado se retorna False."""
	def AgregarUsuario(self,u):
		e = HashEntry(u.nombre,u)
		key = hash(u.nombre) % self.n
		#if (self.TablaRU[key]).__contains__(e):

		if self.TablaRU[key]._size ==0:
			self.TablaRU[key].add(e)

		elif self.TablaRU[key]._size > 0:
			if (self.TablaRU[key])._head.dato.nombre == u.nombre:
				#(self.Tabla[key]).dato = e.dato
				return False
			else:
				(self.TablaRU[key]).add(e)
				return True


	def EliminarUsuario(self,n):
		e=HashEntry(n,None)
		key=hash(n) % self.n
		if (self.TablaRU[key]).__contains__(e):
			e=HashEntry(n,(self.TablaRU[key]).contain(e).dato)
			self.TablaRU[key].remove(e)
			return True  
		else:
			return False

	def cargarUsuarios(self,archivo):

			paper = open(archivo,'r+')
			p = []
			for line in paper.readlines():
				l = line.split('\t')
				l[2] = l[2].split('\n')[0]
				p.append(l)

			for i in range(len(p)):
				NuevoUsuario = Usuario(p[i][0],p[i][1],p[i][2])
				self.AgregarUsuario(NuevoUsuario)


			
	# Descripcion: Imprime, en pares ordenados todos los
	#              elementos que se encuentren en la tabla     
	def MostrarRegistro(self,A):
		print('--------')
		print('Los contactos en la lista son: ')
		for i in range(len(self.TablaRU)):
			if  not self.TablaRU[i].vacia():
				curNode=self.TablaRU[i]._head
				for j in range(self.TablaRU[i]._size):
					print(curNode.clave,curNode.dato.telefono)
					curNode=curNode.next
		print('--------')


	
	def BuscarUsuario(self,u):
		key=hash(u.nombre) % self.n
		if (self.TablaRU[key])._head is not None:
			if (self.TablaRU[key])._head.clave == u.nombre and (self.TablaRU[key])._head.dato.password == u.password:
				return True
			else:
				return False
		else: 
			return False

	def BuscarNombre(self,n):
		key=hash(n) % self.n
		if (self.TablaRU[key])._head is not None:
			if (self.TablaRU[key])._head.clave == n:
				return True
			else:
				return False
		else:
			return False

	def BuscarUsuario2(self,u):
		key=hash(u.nombre) % self.n
		if (self.TablaRU[key])._head is not None:
			if (self.TablaRU[key])._head.clave == u.nombre and (self.TablaRU[key])._head.dato.password == u.password:
				return self.TablaRU[key]._head.dato
			else:
				return
		else: 
			return

	
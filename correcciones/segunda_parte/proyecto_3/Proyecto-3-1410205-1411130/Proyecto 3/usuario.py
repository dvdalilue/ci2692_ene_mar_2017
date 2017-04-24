class NodoLista:
	def __init__(self,elemento):
		#Inicializa un elemento de tipo nodo para usar en la lista de contactos
		self.usuario=elemento
		self.next=None


class ListaContactos:
	def __init__(self):
		#Inicializa una lista simplemente enlazada para los contactos del usuario
		self.head=None

	def Agregar(self,usuario):
		#Agrega un elemento a la lista enlazada
		nodo=NodoLista(usuario) #crea el nodo con el usuario
		x=self.head
		while x!=None: #Consigue el elemento si este se encuentra en la lista
			if x.usuario==usuario:
				return False
			x=x.next
		#El elemento no se encuentra en la lista, hay que agregarlo
		if self.head==None: #Si la lista esta vacia
			self.head=nodo
			return True
		else: #Si la lista no esta vacia
			x=self.head
			prev=None
			while x!=None and x.usuario.nombre<=usuario.nombre:
				prev=x
				x=x.next
			if prev==None:
				nodo.next=self.head
				self.head=nodo
			else:
				prev.next=nodo
				nodo.next=x
			return True

	def Eliminar(self,name):
		#Eliminar un elemento de la lista
		if self.head==None: #Si la lista esta vacia, no hacer nada
			return False
		x=self.head
		prev=None
		while x!=None: #Busca el elemento en la lista. Si lo encuentra lo elimina
			if x.usuario.nombre==name:
				if prev==None:
					self.head=x.next
				else:					
					prev.next=x.next
				return True
			prev=x
			x=x.next
		#El elemento no esta en la lista
		return False

	def Mostrar(self):
		#Muestra la lista de contactos en orden alfabetico
		if self.head==None: #Si la lista esta vacia
			print("La lista de contactos esta vacia.")
			return
		#La lista no esta vacia, se imprime
		x=self.head
		while x!=None:
			##############################################ESTO ORDENA POR LEXICOGRAFICO!!!!####################
			print(x.usuario.nombre)
			x=x.next

	def Buscar(self,name):
		#Busca un elemento en la lista
		x=self.head
		while x!=None: #Cosigue el elemento si este se encuentra en la lista
			if x.usuario.nombre==name:
				return x.usuario
			x=x.next
		return x



class Usuario:
	def crearUsuario(self,name,passwd,cell,contact):
		#Define los atributos de tipo usuario
		assert(int(cell) and len(name)!=0 and len(passwd)!=0 and len(cell)!=0)
		self.nombre=name
		self.password=passwd
		self.telefono=cell
		if contact==None:
			self.contactos=ListaContactos()
		else:
			self.contactos=contact

	def __init__(self,name,passwd,cell,contact):
		#Inicializa un elemento de tipo usuario
		self.crearUsuario(name,passwd,cell,contact)

	def agregarContacto(self, usuario):
		#Agrega un contacto a la lista
		return self.contactos.Agregar(usuario)

	def eliminarContacto(self,name):
		#Elimina un contacto de la lista
		return self.contactos.Eliminar(name)

	def mostrarContactos(self):
		#Muestra la lista de contactos del usuario
		self.contactos.Mostrar()

	def buscarContacto(self,name):
		#Funcion auxiliar que busca un contacto en la lista de contactos del usuario
		return self.contactos.Buscar(name)
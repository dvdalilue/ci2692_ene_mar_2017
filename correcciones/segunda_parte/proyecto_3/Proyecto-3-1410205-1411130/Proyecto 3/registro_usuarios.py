from usuario import Usuario
from arrayT import ArrayT

class HashEntry:
	def __init__ (self, usuario):
		#Inicializa los elementos de tipo hashEntry para la tabla de hash
		self.clave=usuario.nombre
		self.dato=usuario
		self.next = None
		self.prev = None

class Dlist:
    def __init__(self, elemento):
    	#Inicia un elemento de tipo lista doblemente enlazada
        self.head = elemento

    def search_clave(self,clave):
        #Busqueda por clave
        x=self.head
        while x!=None and x.clave!=clave:
            x=x.next
        return x

    def addElement_hass(self,elemento): 
        #Agregar elemento de tipo HassEntry
        if self.head==None:
            self.head=elemento
        else:
            self.head.prev=elemento
            elemento.next=self.head
            self.head=elemento

    def Eliminar(self,x): 
        #Eliminar elemento
        if x.prev!=None:
            x.prev.next=x.next
        else:
            self.head=x.next
        if x.next!=None:
            x.next.prev=x.prev

class Hash_table:
	def __init__ (self, entero): 
		#Inicializa una tabla de hash
		self.lista=ArrayT(entero)
		#self.lista=[None for i in range(entero)]
		self.long=entero

	def agregar_elem(self, usuario): 
		#Agregar elemento de tipo usuario a la tabla
		slot= len(usuario.nombre)%self.long
		if self.lista[slot]==None:
			HashEntry_e=HashEntry(usuario)
			self.lista[slot]=Dlist(HashEntry_e)
			return True
		else:
			m=self.lista[slot].search_clave(usuario.nombre)
			if m==None:
				HashEntry_e=HashEntry(usuario)
				self.lista[slot].addElement_hass(HashEntry_e)
				return True
			else:
				return False

	def eliminar(self,n): 
		#Eliminar elemento dada una clave
		ubicacion=len(n)%self.long
		if self.lista[ubicacion]==None:
			return False
		else:
			elemento=self.lista[ubicacion].search_clave(n)
			if elemento==None:
				return False
			else:
				self.lista[ubicacion].Eliminar(elemento)
				return True

	def Mostrar(self):  
		#Mostrar la tabla
		print("Lista de usuarios registrados:")
		for i in self.lista:
			if i!=None:
				x=i.head
				while x!=None:
					print(" " + str(x.clave))
					x=x.next

	def Buscar(self,name):
		#Funcion de la tabla de hash que busca un usuario dada su clave
		slot=len(name)%self.long
		if self.lista[slot]==None:
			return None
		else:
			x=self.lista[slot].search_clave(name)
			if x!=None:
				return x.dato
			else:
				return x

class Registro:
	def crearTabla(self,n):
		#Define los atributos de usuarios registrados
		self.int=0
		self.tablaRU= Hash_table(n)

	def __init__(self,n):
		#Inicializa la tabla de usuarios registrados
		self.crearTabla(n)

	def agregarUsuario(self,usuario):
		#Agrega un usuario a la tabla
		boolean= self.tablaRU.agregar_elem(usuario)
		if boolean:
			self.int=self.int+1
		return boolean

	def eliminarElemento(self,name):
		#Elimina un usuario de la tabla dado su nombre
		boolean=self.tablaRU.eliminar(name)
		if boolean:
			self.int=self.int-1
		return boolean

	def cargarUsuarios(self,stringarchivo):
		#Carga usuarios desde un archivo
		try:
			lista=[ ]
			with open(stringarchivo,'r') as f:
				for line in f:
					line=line.strip("\n")
					linea=line.split()
					lista=lista+[linea]
			for i in lista:
				usuario=Usuario(i[0],i[1],i[2],None)
				agrego=self.agregarUsuario(usuario)
				if agrego==True:
					print("Se ha agregado "+ usuario.nombre +" al registro.")
				else:
					print("El usuario "+ usuario.nombre +" ya se encuentra en el registro.")
			return True
		except:
			return False

	def mostrarRegistro(self):
		#Muestra la tabla de registro
		self.tablaRU.Mostrar()  ########modificar como se quiera

	def buscarElemento(self,name):
		#Funcion auxiliar que busca un elemento en la tabla de hash por medio de su nombre
		return self.tablaRU.Buscar(name)
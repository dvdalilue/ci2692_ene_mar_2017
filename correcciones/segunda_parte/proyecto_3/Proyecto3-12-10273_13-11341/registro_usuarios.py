# PROYECTO 3

# DESCRIPCIÓN: Creación del TAD Registro de Usuarios, la
# cual almacenara la información de los usuarios registrados
# de la aplicación ALGOGRAM.

# AUTORES: Jesus Kauze y David Segura
# EMAILS: 12-10273@usb.ve y 13-11341@usb.ve

from arrayT import ArrayT
from usuario import Usuario
from usuario import Lista
from conversaciones import h1

class RegistroUsuarios(object):
	def __init__(self):
		self.n = 0
		self.tablaRU = None

	def crearTabla(self,n):
		# Crea la tabla vacía
		self.tablaRU = ArrayT(n)

	def agregarUsuario(self,usuario):
		# Agrega usuarios a la tabla
		key = h1(usuario.nombre) % len(self.tablaRU)
		if self.n == 0:
			# Si no hay usuarios, crea una lista enlazada 
			# con el usuario en él slot correspondiente.
			self.tablaRU[key] = Lista(usuario,None)
			self.n += 1
			return True
		else:
			if self.tablaRU[key] == None:
				# Si hay usuarios pero el slot esta vacío, crea
				# una lista enlazada en el slot correspondiente.
				self.tablaRU[key] = Lista(usuario,None)
				self.n +=1
				return True
			else:
				# Si hay usuarios y el slot no esta vacío, agrega
				# uno al final de la lista enlazada.
				c = self.tablaRU[key]
				while c != None:
					if c.element.nombre == usuario.nombre:
						return False
					else:
						if c.next == None:
							c.next = Lista(usuario,None)
							self.n += 1
							return True
						else:
							c = c.next

	def eliminarUsuario(self,usuario):
		# Elimina usuarios registrados en la "base de datos".
		key = h1(usuario) % len(self.tablaRU)
		lista = self.tablaRU[key]
		if self.n == 0:
			print("No hay usuarios registrados.")
			return False
		else:
			while lista != None:
				if lista.next != None:
					if lista.next.next != None:
						# Mientras el siguiente no sea el último elemento
						if lista.next.element.nombre == usuario:
							# Si es un elemento que no es ni el primero
							# ni el último.
							lista.next = lista.next.next
							self.n -= 1
							return True
						elif lista.element.nombre == usuario:
							# Si el elemento es el primero
							lista.element = lista.next.element
							lista.next = lista.next.next
							self.n -= 1
							return True
						else:
							pass
					else:
						if lista.element.nombre == usuario:
							lista.element = None
							self.n -= 1
							return True
						elif lista.next.element.nombre == usuario:
							lista.next = None
							self.n -=1
							return True
						else:
							pass
				else:
					self.tablaRU[key] = None
					self.n -= 1
					return True
				lista = lista.next
			return False

	def cargarUsuarios(self,archivo):
		# Carga a los usuarios desde un archivo
		abrir = open(archivo,"r")
		lista = abrir.readlines()
		n = 0
		for x in lista:
			n += 1
		users = ArrayT(n)

		for x in range(n):
			t = lista[x].strip("\n")
			p = t.split("\t")
			users[x] = p

		for x in users:
			u = Usuario()
			u.crearUsuario(x[0],x[1],x[2],None)
			self.agregarUsuario(u)

	def mostrarRegistro(self):
		# Muestra a todos los usuarios en la "base de datos"
		tabla = self.tablaRU
		for x in tabla:
			if x != None:
				lista = x
				while lista != None:
					print(lista.element.nombre)
					lista = lista.next
			else:
				pass

	def buscarUsuario(self,usuario):
		# Busca a un usuario en la lista
		key = h1(usuario) % len(self.tablaRU)
		lista = self.tablaRU[key]
		while lista != None:
			if lista.element.nombre == usuario:
				return True,lista.element
			else:
				lista = lista.next
		return False,None
# PROYECTO 3

# DESCRIPCIÓN: Creación del TAD Usuario, la cual almacenara
# la información de un usuario de la aplicación ALGOGRAM

# AUTORES: Jesus Kauze y David Segura
# EMAILS: 12-10273@usb.ve y 13-11341@usb.ve

from arrayT import ArrayT
from mergesort import mergesort

class Lista(object):
	# CLASE QUE SE USARÁ PARA IMPLEMENTAR LA LISTA ENLAZADA
	def __init__(self,elemento,siguiente):
		self.element = elemento
		self.next = siguiente

class Usuario(object):
	def __init__(self):
		self.nombre = None
		self.password = None
		self.telefono = None
		self.contactos = None
		self.centinela = self.contactos

	def crearUsuario(self,name,passw,phone,contacts):
		# Crea un Usuario y verifica que el nombre no sea vacío,
		# que la contraseña no sea vacía, que el telefóno no
		# contenga letras ni sea vacío y que la lista de contactos
		# esté ordenada.
		if name == "" or name == None:
			print("Indique un nombre")
			return False
		elif passw == "" or passw == None:
			print("Indique una contraseña")
			return False
		elif phone == "" or phone == None:
			print("Indique un número de teléfono")
			return False
		else:
			for e in phone:
				try:
					int(e)
				except:
					print("Número de teléfono inválido")
					return False
			c = contacts
			while c != None:
				if c.next != None:
					if c.element.nombre < c.next.element.nombre:
						pass
					else:
						print("Lista de contactos no ordenada")
						return False
				c = c.next
			self.nombre = name
			self.password = passw
			self.telefono = phone
			self.contactos = contacts
			self.centinela = self.contactos
			return True

	def agregarContacto(self,usuario):
		c = self.contactos
		if c == None:
			self.contactos = Lista(usuario,None)
			return True
		else:
			repetido = False
			count = 0
			while c != None:
				count += 1
				c = c.next
			c = self.contactos
			while c != None:
				if c.element.nombre == usuario.nombre:
					print("El contacto ya está en la lista")
					repetido = True
					break
				else:
					c = c.next
			if repetido == False:
				c = self.contactos
				self.centinela = self.contactos
				lista = ArrayT(count+1)
				t = 0
				while c != None:
					lista[count] = c.element
					c = c.next
					count -= 1
					t += 1
				lista[0] = usuario
				t = t + 1
				ordenado = mergesort(lista)
				for x in range(t):
					self.centinela.element = ordenado[x]
					if x != t - 2:
						self.centinela = self.centinela.next
					elif x == t - 2:
						self.centinela.next = Lista(ordenado[x+1],None)
						self.centinela = self.centinela.next
					else:
						pass
				return True
			else:
				return False

	def eliminarContacto(self,nombre):
		# Elimina a un usuario buscando su nombre
		lista = self.contactos
		while lista != None:
			if lista.next != None:
				if lista.next.element.nombre == nombre:
					lista.next = lista.next.next
					return True
				elif lista.element.nombre == nombre:
					lista.element = lista.next.element
					lista.next = lista.next.next
					return True
				else:
					pass
			else:
				if lista.element.nombre == nombre:
					lista.element = None
					return True
			lista = lista.next
		print("Contacto no encontrado")
		return False

	def mostrarContactos(self):
		# Muestra los contactos del usuario
		lista = self.contactos
		print("Lista de contactos de "+str(self.nombre)+":")
		while lista != None:
			print(str("-")+lista.element.nombre)
			lista = lista.next
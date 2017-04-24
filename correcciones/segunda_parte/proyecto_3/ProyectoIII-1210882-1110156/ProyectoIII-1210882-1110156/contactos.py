""" Laboratorio 1 .algoritmos II .ene-mar 2017 
	fecha:01/04/2017
	Descripcion:Lista Enlazada CONTACTOS ,Contiene los usuarios registrados en la aplicacion
	autores: Edymar Mijares 12-10882
	         Jose Carmona 11-10156

	correo: - edys.beccaria@gmail.com
		   - carmona621@hotmail.com
ultima edicion :30/03/2017"""
from Registrodeusuarios import TablaRU
from nodoContacto import NodoContacto

class CONTACTOS:
	def __init__(self,TR):#donde TR es el Registro Actual
		self.primero = None
		self.ultimo = None
		self.size = 0
		self.registro = TR
	#esta funcion retorna false si hay caracteres distintos de numeros en el telefono
	def VerificarNumero(self,numero):
		Valido = numero.isdigit()
		return Valido
			
	#crea el nuevo usuario si cumple con los requisitos	
	def Crear_usuario(self,nombre, telefono):
		if nombre!= None and self.registro.buscarContra(nombre)!= None and telefono!= None:
			valido = self.VerificarNumero(telefono)
			
			if valido:
				NewUsuario = NodoContacto(nombre,telefono, None, None)
				return NewUsuario
			else:
				print("numero de telefono no valido")
				return None
			
		else:
			print("No puede agregar un Contacto sin todos los datos")
			return None
			
		
	#Esta funcion Me indica si la persona se encuentra entre mis contactos
	def Se_Encuentra(self, Nombre):
		x = self.primero
		Esta = False
		if  x!= None:
		
			while x.siguiente != self.primero:
				if x.nombre == Nombre:
					Esta= True
				x = x.siguiente
			if x == self.ultimo:
				if x.nombre == Nombre:
					Esta= True
		return Esta
		
	#verifica si el usuario esta registrado o no
	def Registrado(self,nombre):
		Esta = False
		buscado = self.registro.Buscar_En_Registro(nombre)
		if buscado == None:
			pass
		else:
			Esta = True
		
		return Esta
		
	#se agregan los contactos al final de la lista
	def Agregar_contacto(self, nombre):
		name = self.registro.Buscar_En_Registro(nombre)
		cel = self.registro.buscarCelular(nombre)
		Usuario = self.Crear_usuario( name,cel)#ahora el contacto es del tipo Nodo contacto , atributos: .nombre, .telefono
		if self.size == 0:
			if self.Registrado(name):
				self.primero = Usuario
				self.ultimo = self.primero
				self.primero.siguiente = self.ultimo
				self.ultimo.siguiente = self.primero
				self.primero.anterior = self.ultimo
				self.size = self.size + 1
				return True
			else:
				print("El contacto que esta tratando de agregar no esta registrado")
				return False
			
		else:
			if self.Se_Encuentra(name):
				print("El Contacto Ya fue agregado:", Usuario)
				return False
			else:
				if self.Registrado(name):
					self.ultimo.siguiente = Usuario
					aux = self.ultimo
					self.ultimo= aux.siguiente
					self.ultimo.anterior = aux
					self.primero.anterior = self.ultimo
					self.ultimo.siguiente = self.primero
					self.size = self.size + 1
					return True
				else:
					print("El contacto que esta tratando de agregar no esta registrado")
					return False
					
	#elimina el contacto con el nombre indicado
	def Eliminar_contacto(self, n):
		x = self.primero
		Listo = False
		if x!= None:
			print("algo")
			while x.siguiente != self.primero:
				if x.nombre == n:
					print("lo encontro aqui")
					x.anterior.siguiente = x.siguiente
					x.siguiente.anterior = x.anterior
					Listo= True
					self.size = self.size - 1
				x = x.siguiente
			if self.ultimo.nombre == n:
				print("Cayo aqui")
				self.ultimo = self.ultimo.anterior
				self.ultimo.siguiente = self.primero
				self.primero.anterior = self.ultimo
				self.size = self.size - 1
				Listo = True
		return Listo
		
	
	#Muestra nombre y numero de los contactos registrados		
	def Mostrar_contactos(self):
		x = self.primero
		x2= self.ultimo
		print("Sus contactos Actuales:")
		if x!=None :
			while x.siguiente != self.primero:
				print((x.nombre,x.telefono))
				x = x.siguiente
			print((x2.nombre,x2.telefono))
		
		
		
		
	

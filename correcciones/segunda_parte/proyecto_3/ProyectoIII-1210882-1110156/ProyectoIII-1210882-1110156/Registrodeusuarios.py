""" Laboratorio 1 .algoritmos II .ene-mar 2017 
	fecha:01/04/2017
	Descripcion:tabla de hash que Contiene los usuarios registrados en la aplicacion
	autores: Edymar Mijares 12-10882
	         Jose Carmona 11-10156

	correo: - edys.beccaria@gmail.com
		   - carmona621@hotmail.com
ultima edicion :30/03/2017"""

from usuario import USUARIO
from listaHashRegistro import Dlist

	
	
class  TablaRU:
	#se inicializa la clase con dos parametros; tabla y size que es el tamaño de la tabla
	def __init__(self):
		self.tabla = []
		self.size = 0
		
	#funcion que crea una tabla del tipo dlist	
	def Crear_Tabla(self,n):
		self.size = n
		self.tabla=[Dlist() for x in range(n)]
	#funcion que muestra los elementos que estan en la tabla de hash	
	def MostrarRegistro(self):
		for i in range(0,len(self.tabla)):
			self.tabla[i].imprimir()
	#funcion que agrega un nuevo elemento en la tabla 
	def agregar_elem(self,Unombre, Ucontra, Utelefono):
	
		H=hash(Unombre)
		bucket= H%(self.size)
		elemento = self.tabla[bucket].buscar_En_Bucket(Unombre)
		if elemento == None:
			elemento = USUARIO(Unombre, Ucontra, Utelefono, None, None )
			self.tabla[bucket].agregar_elem(elemento)
		else:
			elemento.Password = Ucontra
			elemento.Telefono = Utelefono
		print ("El registro se ha efectuado de forma Exitosa")

	#funcion que elimina un elemento de la tabla
	def Eliminar(self,name):
		H=hash(name)
		bucket= H%(self.size)
		elemento = self.tabla[bucket].buscar_En_Bucket(name)
		if elemento != None:
			self.tabla[bucket].eliminar_elem(elemento)
			return elemento.Nombre
		else:
			return None
			
	def Buscar_En_Registro(self,name):
		if self.size == 0:
			print("Error La tabla no ha sido creada")
			return None
		else:
			H=hash(name)
			bucket= H%(self.size)
			elemento = self.tabla[bucket].buscar_En_Bucket(name)
			if elemento != None:
				return elemento.Nombre
			else:
				return None
			
	def buscarContra(self,name):
		H=hash(name)
		bucket= H%(self.size)
		elemento = self.tabla[bucket].buscar_En_Bucket(name)
		if elemento != None:
			return elemento.Password
		else:
			print("El usuario no esta registrado")
			return None
			
	def buscarCelular(self,name):
		H=hash(name)
		bucket= H%(self.size)
		elemento = self.tabla[bucket].buscar_En_Bucket(name)
		if elemento != None:
			return elemento.Telefono
		else:
			print("El usuario no esta registrado")
			return None
			
	def CargarUsuarios(self,archivo):
		Listo = False
		f= open(archivo, 'r')
		Name = []
		Contraseña = []
		Telefono = []
		for line in f:
			line = line.rstrip()            # Se elimina el salto-de-linea al final de la linea
			tok = line.split("\t")
			nm = tok[0]                 
			cs = tok[1]
			tl = tok[2]	              
			Name.append(nm)          
			Contraseña.append(cs)
			Telefono.append(tl)
		f.close()
		n = len(Name)
		for i in range (n):
			Name[i]=Name[i].replace("\n","")
		for i in range (n):
			Contraseña[i]=Contraseña[i].replace("\n","")
		for i in range (n):
			Telefono[i]=Telefono[i].replace("\n","")
			
		for i in range (n):
			self.agregar_elem(Name[i], Contraseña[i], Telefono[i])
			Listo = True
			
		return Listo

			


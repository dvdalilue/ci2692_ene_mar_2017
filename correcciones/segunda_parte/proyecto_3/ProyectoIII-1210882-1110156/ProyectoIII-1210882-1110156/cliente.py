""" Laboratorio 1 .algoritmos II .ene-mar 2017 
	fecha:01/04/2017
	Descripcion: Cliente
	autores: Edymar Mijares 12-10882
	         Jose Carmona 11-10156

	correo: - edys.beccaria@gmail.com
		   - carmona621@hotmail.com
ultima edicion :30/03/2017"""
from CHAT import Chat
from Registrodeusuarios import TablaRU
from Conversaciones import CONVERSACIONES
from contactos import CONTACTOS
import os

class Emoti:
	def __init__(self):
		self.Carita=[]
		self.Numerodecara = []
		
	def CargarCaritas(self,archivo):
		Listo = False
		f= open(archivo, 'r')
		Caras = []
		for line in f:
			line = line.rstrip()
			tok = line.split("\t")
			tm = len(tok)
			for i in range (tm):
				Caras.append(tok[i])
		f.close()
		n = len(Caras)
		for i in range (n):
			Caras[i]=Caras[i].replace("\n","")
		Sep = []
		for i in range (n):
			Sep = Caras[i].split("=")
			self.Carita.append(Sep[0])
			self.Numerodecara.append(int(Sep[1]))
			Listo = True
			
		if Listo == True:
			print("Las caritas se agregaron de forma correcta")
		return Listo
	
	def MostrarCaritaYO(self):
		for i in range (len(self.Carita)):
			print((self.Numerodecara[i],self.Carita[i]))
	
	def MostrarCaritas(self):
		print(self.Carita)
		
	def BuscarCarita(self,n):
		N= len(self.Numerodecara)
		for i in range (N):
			if self.Numerodecara[i] == n:
				k= i
		return self.Carita[k]
		
def MenuUsuario(REg, emot, con, conver):
	print("*******************************************************")
	print("**********************ALGOGRAM************************" )
	print("*******************************************************")
	print("Por favor Escoja una de las siguientes opciones:")
	print("1 Agregar Contacto")
	print("2 Eliminar Contacto")
	print("3 Mostrar Contactos")
	print("4 Ver Conversacion")
	print("5 Enviar Mensaje")
	print("6 Mostrar Caritas")
	print("7 Mostrar Usuarios Registrados")
	print("8 Cerrar Seccion")
	opcion = (input("Ingrese el Numero de la opcion Elegida:",))
	
	if opcion=="1":
		Name = str(input("Ingrese el Nombre del contacto que desea Agregar:",))
		verificar =con.Agregar_contacto(Name)
		if verificar:
			print("El contacto se agrego")
		else:
			print("intente nuevamente")
		MenuUsuario(REg,emot,con, conver)
		
		
	if opcion=="2":
		Name = str(input("Ingrese el Nombre del contacto que desea Eliminar:",))
		verificar = con.Eliminar_contacto(Name)
		if verificar:
			print("El contacto se elimino")
		else:
			print("intente nuevamente")
		MenuUsuario(REg,emot,con, conver)
	
	if opcion=="3":
		con.Mostrar_contactos()
		MenuUsuario(REg,emot, con, conver)
		
	if opcion=="4":
		Name = str(input("Ingrese el nombre del usuario con quien comparte dicha conversacion:",))
		prin = str(input("Ingrese su nombre de usuario (con el que esta registrado):",))
		conver.MostrarConversacion(Name,prin)
		MenuUsuario(REg, emot, con, conver)
		
	if opcion=="5":
		Name = str(input("Ingrese el nombre del usuario a Quien enviara el mensaje:",))
		prin = str(input("Ingrese su nombre de usuario (con el que esta registrado):",))
		if con.Se_Encuentra(Name):
			if conver.buscarConversacion(Name, prin) != None:	
				m = str(input(" Ingrese su Mensaje:",))
				CR = str(input("si desea agregar unA  carita ingrese S:",))
				if CR == "S":
					print("Estas Son Las opciones:")
					emot.MostrarCaritaYO()
					algo = int(input("ingrese el numero correspondiente a la carita que  desea usar:",))
					car = emot.BuscarCarita(algo)
					men = m + "  " + car
					print("usted va a enviar",men)
					conver.Agregar_Mensaje(Name,prin, men)

	
				else:
					print("usted va a enviar",m)
					conver.Agregar_Mensaje(Name,prin, m)


			else:
				C = Chat()
				C.CrearChat(Name, prin)
				m = str(input(" Ingrese su Mensaje:",))
				CR = str(input("si desea agregar unA  carita ingrese S:",))
				if CR == "S":
					print("Estas Son Las opciones:")
					emot.MostrarCaritaYO()
					algo = int(input("ingrese el numero correspondiente a la carita que  desea usar:",))
					car = emot.BuscarCarita(algo)
					men = m + "  " + car
					print("usted va a enviar",men)
					C.AgregarMensaje(prin, men)
					conver.agregar_Conversacion(C)
				else:
					print("usted va a enviar",m)
					C.AgregarMensaje(prin,m)
					conver.agregar_Conversacion(C)
				print("El Mensaje Fue Recibido")
		else:
			print("El usuario no esta en su lista de contactos")
		MenuUsuario(REg, emot, con, conver)
		
	if opcion=="6":
		emot.MostrarCaritas()
		os.system('clear')
		MenuUsuario(REg, emot, con, conver)
		
	if opcion == "7":
		REg.MostrarRegistro()
		MenuUsuario(REg, emot, con, conver)
		
	if opcion == "8":
		print("Su seccion ha Sido Cerrada, Gracias por preferir ALGOGRAM")
		Menu(REg, emot, con, conver)
	
	if opcion!="1" and opcion!="2" and opcion!="3" and opcion!="4" and opcion!="5" and opcion!="6" and opcion!="7" and opcion!="8" :
		print("La opcion ingresada no es Valida")
		os.system('clear')
		MenuUsuario(REg, emot, con, conver)


def Menu( REg,emot, con, conver):
	print("*******************************************************")
	print("***************Bienvenido a ALGOGRAM*******************" )
	print("*******************************************************")
	print("Por favor Escoja una de las siguientes opciones:")
	print("1 Registrarse")
	print("2 Iniciar Seccion")
	print("3 Cargar Usuarios")
	print("4 Eliminar Usuario")
	print("5 Cargar Caritas")
	print("6 Salir de la aplicacion")
	opcion = (input("Ingrese el Numero de la opcion Elegida:",))
	
	
	if opcion=="1":
		Name = str(input("Ingrese su Nombre:",))
		Numero= str(input("Ingrese su Numero de Telefono:",))
		Contraseña = str(input("Ingrese su Contraseña:",))
		Estara = REg.Buscar_En_Registro(Name)
		
		if   Estara != None:
			print("El usuario ya se encuentra Registrado")
		else:
			
			REg.agregar_elem( Name, Contraseña ,Numero)
		os.system('clear')
		Menu( REg, emot, con, conver)
		
	if opcion=="2":
		Name = str(input("Ingrese su Nombre:",))
		Contraseña = str(input("Ingrese su Contraseña:",))
		Estara = REg.Buscar_En_Registro(Name)
		if  Estara == None:
			print("El Usuario es incorrecto por favor intente de nuevo")
			os.system('clear')
			Menu( REg,emot, con, conver)
		else:
			if REg.buscarContra(Name) == Contraseña:
				MenuUsuario(REg,emot, con, conver )
			else:
				print("El Usuario es incorrecto por favor intente de nuevo")
			os.system('clear')
			Menu( REg,emot, con, conver)
	
	if opcion=="3":
		Cargar= str(input("Ingrese el nombre del archivo que tiene a los usuarios que desea agregar:",))
		if ".txt" in Cargar:
			REg.CargarUsuarios(Cargar)
			os.system('clear')
			Menu( REg,emot, con, conver)
		else:
			print("Nombre de archivo no valido recuerde que debe colocar '.txt' al final del nombre del archivo")
			Menu( REg,emot, con, conver)
		
	if opcion=="4":
		Name = str(input("Ingrese el nombre del usuario que desea eliminar del registro:",))
		if REg.Buscar_En_Registro(Name) == None:
			os.system('clear')
			print("Disculpe, el usuario que desea eliminar no esta registrado")
			Menu( REg,emot,  con, conver)
		else:
			REg.Eliminar(Name)
			os.system('clear')
			Menu( REg,emot,  con, conver)
			
	if opcion=="5":
		Cargar= str(input("Ingrese el nombre del archivo que tiene las CAritas que desea agregar:",))
		if ".txt" in Cargar:
			emot.CargarCaritas(Cargar)
			os.system('clear')
			Menu( REg,emot, con, conver)
		else:
			print("Nombre de archivo no valido recuerde que debe colocar '.txt' al final del nombre del archivo")
			Menu( REg,emot, con, conver)
			
	if opcion == "6":
		pass
		
	if opcion!="1" and opcion!="2" and opcion!="3" and opcion!="4" and opcion!="5" and opcion!="6" :
		os.system('clear')
		print("La opcion ingresada no es Valida")
		Menu( REg,emot, con, conver)
	
#############################################
######### Llamada al cliente ################
#############################################
Registro = TablaRU()
Registro.Crear_Tabla(30)
MisEmotis = Emoti()
miscontactos = CONTACTOS(Registro)
misconversaciones= CONVERSACIONES()
misconversaciones.Crear_Tabla(150)

Menu(Registro,MisEmotis, miscontactos,misconversaciones)	
	
	


from arrayT import ArrayT
from usuario import Usuario
from registro_usuarios import Registro_Usuarios
from chat import Chat
from conversaciones import Conversaciones
import copy
import sys
import subprocess as sp
import os

UserModel 	    		= Registro_Usuarios(100)
ConversacionesModel  	= Conversaciones(5000)

Session 	= None
caritas		= None

def ClearScreen():
	try:
		sp.call('clear',shell=True)
	except SystemExit:
		sys.exit()
	except:
		pass

def PrintTitle(word):
	print("\n")    
	print(" _____ _ ")   
	print("|  _  | |___ ___     ___ ___ ___ _____")     
	print("|     | | . | . |   | . |  _| .'|     |")   
	print("|__|__|_|_  |___|   |_  |_| |__,|_|_|_|")
	print("        |___|       |___|")   
	print("\n") 
	_floor = "-"
	_floor *= 8+len(word)
	print(_floor)
	print("    "+word+"       ")
	print(_floor)
	print("\n")  

def PrintError(error):
	print("\n")  
	_floor = "-"
	_floor *= 8+len(error)
	print(_floor)
	print("    "+error+"       ")
	print(_floor)
	print("\n")  

def MainMenu():
	PrintTitle("MENU PRINCIPAL")

	print('1. Registrarse')
	print('2. Iniciar sesion')
	print('3. Cargar usuarios')
	print('4. Eliminar usuario')
	print('5. Cargar caritas')
	print('6. Salir\n')

def UserMenu():
	PrintTitle("BIENVENIDO "+ Session.nombre)
	print('1. Agregar contacto')
	print('2. Eliminar contacto')
	print('3. Mostrar contactos')
	print('4. Ver conversacion')
	print('5. Enviar mensaje')
	print('6. Mostrar caritas')
	print('7. Mostrar usuarios registrados')
	print('8. Cerrar sesion\n')

def MainMenuOp():
	while True:
		opcion = input('Escoja una opcion: ')
		if opcion =='1' or opcion=='2' or opcion=='3' or opcion=='4' or opcion=='5' or opcion=='6':
			break
		else:
			print('Opcion invalida')
	return opcion

def UserMenuOp():
	while True:
		opcion = input('Escoja una opcion: ')
		if opcion =='1' or opcion=='2' or opcion=='3' or opcion=='4' or opcion=='5' or opcion=='6' or opcion=='7' or opcion=='8':
			break
		else:
			print('Opcion invalida')
	return opcion

def checkPhone(phone):
	if len(phone) == 0:
		return False

	for i in range(len(phone)):
		if phone[i] not in ['0','1','2','3','4','5','6','7','8','9']:
			return False

	return True



def Registrarse():
	global Session

	ClearScreen()
	PrintTitle("REGISTRO DE USUARIO")

	while True:
		nombre 		= input("Ingrese su nombre: ")
		password 	= input("Ingrese su password: ")
		phone 		= input("Ingrese su telefono: ")

		if checkPhone(phone) and len(nombre) > 0 and len(password) > 0:
			break
		else:
			PrintError("Datos incorrectos, intente de nuevo")

	entry = Usuario(nombre, password, phone)
	if entry != None and UserModel.AgregarUsuario(entry):
		Session = entry
		ClearScreen()
		MostrarMenu()
	else:
		ClearScreen()
		PrintError("El usuario ya existe")
		MostrarInicio()
	

def IniciarSesion():
	global Session

	ClearScreen()
	PrintTitle("INICIO DE SESION")
	while True:
		nombre 		= input("Ingrese su nombre: ")
		password 	= input("Ingrese su password: ")

		if len(nombre) > 0 and len(password) > 0:
			break
		else:
			PrintError("Datos incorrectos, intente de nuevo")

	# Check if users exists then MostrarInicio
	entry = UserModel.Search(nombre)
	if entry == None:
		ClearScreen()
		PrintError("Usuario no encontrado")
		MostrarInicio()
	elif password == entry.password:
		ClearScreen()
		Session = entry
		MostrarMenu()
	else:
		ClearScreen()
		PrintError("Clave incorrecta")
		MostrarInicio()


def CerrarSesion():
	global Session
	ClearScreen()
	Session = None
	MostrarInicio()

def CargarUsuarios():
	ClearScreen()
	PrintTitle("CARGA DE USUARIOS")
	PrintError("Con el formato: NOMBRE[TAB]PASSWORD[TAB]TELEFONO")
	file = input('Ingrese el nombre del archivo: ')
	
	try:
		t = open(file)
		cantidad = 0
		lines = 0
		for line in t:
			lines += 1
			linea = line.split("\t")
			nombre = linea[0]
			password = linea[1]
			phone = linea[2].strip("\n")
			entry = Usuario(nombre, password, phone)
			if entry != None and UserModel.AgregarUsuario(entry):
				cantidad += 1	
		ClearScreen()
		PrintError("Se agregaron "+ str(cantidad) + " de "+ str(lines) + " usuarios")
		t.close()
		MostrarInicio()
	except SystemExit:
		sys.exit()

	except:
		ClearScreen()
		PrintError("Error cargando usuarios")
	
		Session = None
		MostrarInicio()

def EliminarUsuario():
	ClearScreen()
	PrintTitle("ELIMINAR USUARIO")
	nombre = input('Ingrese el nombre del usuario: ')
	
	if len(nombre) == 0:
		ClearScreen()
		PrintError("Debe ingresar un nombre")
		MostrarInicio()
	else:
		entry = UserModel.Search(nombre)
		
		if entry == None:
			ClearScreen()
			PrintError("Usuario no encontrado")
			MostrarInicio()
		else:
			name = entry.nombre
			UserModel.EliminarUsuario(entry.nombre)
			ClearScreen()
			PrintError("El usuario "+ name + " fue borrado")
			MostrarInicio()

def CargarCaritas(archivo):
	global caritas
	f = open(archivo,'r')
	linea = f.readline().strip('\n')
	cantidad = int(linea[len(linea)-1])
	caritas = ArrayT(cantidad)
	for i in range(cantidad):
		caritas[i] = linea.split('\t')[i].split('=')[0]
	f.close()
	ClearScreen()
	PrintError("Se agregaron "+ str(cantidad) + " caritas")
	MostrarInicio()

def MostrarMenu():
	global Session
	
		
	UserMenu()
	selected = UserMenuOp()
	if selected == '1':
		AgregarContacto()
	
	elif selected == '2':
		EliminarContacto()

	elif selected == '3':
		MostrarContactos()

	elif selected == '4':
		VerConversacion()

	elif selected == '5':
		EnviarMensaje()

	elif selected == '6':
		try:
			MostrarCaritas()
		except SystemExit:
			sys.exit()	
		except:
			print('No has cargado caritas')
			MostrarMenu()
	elif selected == '7':
		MostrarUsuarios()

	elif selected == '8':
		CerrarSesion()

def MostrarInicio():
	MainMenu()
	selected = MainMenuOp()

	if selected == '1':
		Registrarse()
	elif selected == '2':
		IniciarSesion()
	elif selected == '3':
		CargarUsuarios()
	elif selected == '4':
		EliminarUsuario()
	elif selected == '5':
		while True:
			try:
				ClearScreen()
				PrintTitle("CARGA DE CARITAS")
				PrintError("Con el formato: carita_1=1[TAB]carita_2=2[TAB]carita_3=3...carita_n=n")
				archivo = input('Ingrese el nombre del archivo: ')
				caritas = CargarCaritas(archivo)
				break
			except SystemExit:
				sys.exit()	
			except:
				print('Archivo invalido')
	elif selected == '6':
		sys.exit()

def AgregarContacto():
	ClearScreen()
	PrintTitle("AGREGAR CONTACTO")
	nombre = input('Ingrese el nombre del usuario: ')
	
	if len(nombre) == 0:
		ClearScreen()
		PrintError("Debe ingresar un nombre")
		MostrarMenu()
	else:
		entry = UserModel.Search(nombre)
		
		if entry == None:
			ClearScreen()
			PrintError("Usuario no encontrado")
			MostrarMenu()
		else:
			if entry == Session:
				ClearScreen()
				PrintError("No puedes agregarte como contacto")
				MostrarMenu()

			elif Session.AgregarContacto(entry):
				ClearScreen()
				PrintError(entry.nombre+ " fue agregado a tus contactos")
				MostrarMenu()
			else:
				ClearScreen()
				PrintError(entry.nombre+ " ya es tu contacto")
				MostrarMenu()	
def EliminarContacto():
	ClearScreen()
	PrintTitle("ELIMINAR CONTACTO")
	nombre = input('Ingrese el nombre del usuario: ')
	
	if len(nombre) == 0:
		ClearScreen()
		PrintError("Debe ingresar un nombre")
		MostrarMenu()
	else:
		entry = UserModel.Search(nombre)
		
		if entry == None:
			ClearScreen()
			PrintError("Usuario no encontrado")
			MostrarMenu()
		else:
			if Session.EliminarContacto(entry.nombre) == None:
				ClearScreen()
				PrintError(entry.nombre+ " no es tu contacto")
				MostrarMenu()
			else:
				ClearScreen()
				PrintError(entry.nombre+ " fue eliminado de tus contactos")
				MostrarMenu()				
def MostrarContactos():
	ClearScreen()
	PrintTitle("Tus contactos")
	Session.MostrarContactos()
	MostrarMenu()

def EnviarMensaje():
	ClearScreen()
	PrintTitle("ENVIAR MENSAJE")
	nombre = input('Ingrese el nombre del usuario: ')
	
	if len(nombre) == 0:
		ClearScreen()
		PrintError("Debe ingresar un nombre")
		MostrarMenu()
	else:
		entry = UserModel.Search(nombre)
		
		if entry == None:
			ClearScreen()
			PrintError("Usuario no encontrado")
			MostrarMenu()
		else:
			if entry == Session:
				ClearScreen()
				PrintError("No puedes enviarte mensajes")
				MostrarMenu()
			elif Session.contactos.search(entry.nombre) == None:
				ClearScreen()
				PrintError(entry.nombre +" no es tu contacto")
				MostrarMenu()
			else:
				print('1. Enviar mensaje')
				print('2. Enviar carita')
				print('\n')
				opcion = input('Escoja una opcion: ')
				if opcion == '1':
					mensaje = input("Ingresa el mensaje a enviar: ")

				elif opcion == '2':
					try:
						mensaje = MenuCaritas()
					except SystemExit:
						sys.exit()	
					except:
						PrintError("No has cargado caritas")
						EnviarMensaje()
						return
				else:
					EnviarMensaje()
				
				if len(mensaje) == 0:
					ClearScreen()
					PrintError("Debe ingresar un mensaje")
					MostrarMenu()
				else:
					if Session.nombre  < entry.nombre:
						cid = Session.nombre + "-" + entry.nombre
					else:
						cid = entry.nombre + "-" + Session.nombre 

					conversation = ConversacionesModel.buscarConversacion(cid)
					if conversation != None:
						conversation.agregarMensaje(Session, mensaje)
					else:
						nuevo = Chat(Session, entry)
						nuevo.agregarMensaje(Session, mensaje)
						ConversacionesModel.agregarConversacion(nuevo)
						
					ClearScreen()
					PrintError("Mensaje enviado")
					MostrarMenu()
				
	
def VerConversacion():
	ClearScreen()
	PrintTitle("VER CONVERSACION")
	nombre = input('Ingrese el nombre del usuario: ')
	
	if len(nombre) == 0:
		ClearScreen()
		PrintError("Debe ingresar un nombre")
		MostrarMenu()
	else:
		entry = UserModel.Search(nombre)
		
		if entry == None:
			ClearScreen()
			PrintError("Usuario no encontrado")
			MostrarMenu()
		else:
			if entry == Session:
				ClearScreen()
				PrintError("No existe una conversacion contigo")
				MostrarMenu()
			elif Session.contactos.search(entry.nombre) == None:
				ClearScreen()
				PrintError(entry.nombre +" no es tu contacto")
				MostrarMenu()
			else:
				
				if Session.nombre  < entry.nombre:
					cid = Session.nombre + "-" + entry.nombre
				else:
					cid = entry.nombre + "-" + Session.nombre 

				conversation = ConversacionesModel.buscarConversacion(cid)
				if conversation != None:
					mensajes = copy.deepcopy(conversation.mensajes)
					PrintError("Conversacion con " + entry.nombre)
					_mensajes = ArrayT(mensajes.size)
					i = 0
					while not mensajes.isEmpty():
						_mensajes[len(_mensajes)-i-1] = mensajes.pop().value
						i += 1

					for k in range(len(_mensajes)):
						people = _mensajes[k]
			
						spaces = " "
						_floor = "-"
						_floor *= 8+len(people)
						print(spaces+_floor)
						print(" | "+people+"    |")
						print(spaces+_floor)					
					
					k = input("\nPresiona Enter para salir de la conversacion")
					ClearScreen()
					MostrarMenu()
				else:
					ClearScreen()
					PrintError("Aun no hablas con " + entry.nombre)
					MostrarMenu()

def MostrarCaritas():
	global caritas

	ClearScreen()
	PrintTitle("Caritas cargadas")
	salida = ''
	for i in range(len(caritas)):
		if i == len(caritas)-1:
			salida = salida + caritas[i]
		else:
			salida = salida + caritas[i] + ', '
	print(salida)
	k = input("\nPresiona Enter para salir de esta vista")
	ClearScreen()
	MostrarMenu()

def MenuCaritas():
	global caritas
	for i in range(len(caritas)):
		print(i+1,': '+caritas[i])
	while True:
		seleccionada = int(input('Presione el numero correspondiente a la carita que desea enviar: '))
		if seleccionada in range(1,len(caritas)+1):
			mensaje = caritas[seleccionada-1]
			return mensaje
		else:
			print('Opcion invalida')

def MostrarUsuarios():
	ClearScreen()
	PrintTitle("Usuarios registrados")
	UserModel.MostrarRegistro()
	k = input("\nPresiona Enter para salir de esta vista")
	ClearScreen()
	MostrarMenu()

if __name__ == "__main__":
    MostrarInicio()
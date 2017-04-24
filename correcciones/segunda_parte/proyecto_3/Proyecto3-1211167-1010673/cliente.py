# Proyecto no. 3
# Autores: Jorge Sanchez 10-10673
#		   Greanny Vivas 12-11167
from arrayT import ArrayT
from registro_usuarios import*
from usuario import*
from tablaRU import*
from tablaC import*
from chat import*
from conversaciones import*
import sys

registro = RegistroUsuarios(10,tablaRU(10))
conversaciones = Conversaciones(10,tablaC(10))
caritas = None

def menu_principal():
	print(" ")
	print(" MENU PRINCIPAL ")
	print(" ")
	print(" 1. Registrarse")
	print(" ")
	print(" 2. Iniciar sesion")
	print(" ")
	print(" 3. Cargar usuarios")
	print(" ")
	print(" 4. Eliminar usuarios")
	print(" ")
	print(" 5. Cargar caritas")
	print(" ")
	print(" 6. Salir")
	print(" ")
	while True:
		opcion = int(input("Escoja una opcion: "))

		if opcion == 1: # registro de usuario
			nombre = input(" Introduzca su nombre: ")
			password = input(" Escriba su password: ")
			telefono = input(" Introduzca su numero de telefono: ")
			contactos = [] 
			u = Usuario(nombre,password,telefono,contactos)
			if registro.AgregarUsuario(u) == False:
				print(" ")
				print("No se ha podido registrar al usuario")
				print(" ")
				salir = input(" ¿Desea regresar al menu principal? (s/n): ")
				if salir.lower() == "s":
					menu_principal()
				elif salir.lower() == "n":
					print(" ")
					print("Cerrando Aplicacion")
					print(" ")
					sys.exit()
			else:
				print(" ")
				print("El usuario ha sido registrado exitosamente.")
				print(" ")

		elif opcion == 2:
			nombre = input(" Nombre de usuario: ")
			if registro.BuscarUsuario(nombre) == True: 
				password = input("Password: ")
				if registro.BuscarPassword(nombre,password) == True:
					menu_usuario(nombre)
				else:
					print(" ")
					salir = input("Password incorrecto. ¿Desea regresar al menu principal?(s/n): ")
					print(" ")
					if salir.lower() == "s":
						menu_principal()
					elif salir.lower() == "n":
						print(" ")
						print("Cerrando Aplicacion")
						print(" ")
						sys.exit()
						print(" ")
			else:
				print(" ")
				print(" El usuario no se encuentra registrado. ")
				print(" ")

		elif opcion == 3:
			archivo = input(" Indique el nombre del archivo con los usuarios a agregar: ")
			r = registro.CargarUsuario(archivo)
			if r == True:
				print(" ")
				print ("Todos los usuarios fueron cargados exitosamente. ")
				print(" ")
			else:
				print(" ")
				print("Se ha cargado el numero de usuarios disponibles en ALGOGRAM ")
				print(" ")

		elif opcion == 4: 
			nombre = input(" Indique el nombre del usuario que quiere eliminar: ")
			r = registro.EliminarUsuario(nombre)
			if r == True:
				print(" ")
				print(" El usuario "+str(nombre)+" ha sido eliminado. ")
				print(" ")
			else:
				print(" ")
				print(str(nombre)+" no es usuario de ALGOGRAM. ")
				print(" ")


		elif opcion == 5:
			cargarCaritas()

		elif opcion == 6:
			print(" ")
			print(" Adios. ")
			print(" ")
			sys.exit()

		elif (opcion > 6) or (opcion < 1):
			print(" ")
			print("Error, la opcion seleccionada no es valida")
			print("")
			
	return


def menu_usuario(nombre):
	print(" ")
	print(" BIENVENIDO A ALGOGRAM ")
	print(" ")
	print(" 1. Agregar contacto")
	print(" ")
	print(" 2. Eliminar contacto")
	print(" ")
	print(" 3. Mostrar contactos")
	print(" ")
	print(" 4. Ver conversacion")
	print(" ")
	print(" 5. Enviar mensaje")
	print(" ")
	print(" 6. Mostrar caritas")
	print(" ")
	print(" 7. Mostrar usuarios registrados")
	print(" ")
	print(" 8. Cerrar sesion")
	print(" ")
	while True:
		opcion = int(input("Escoja una opcion ALGOGRAM: "))

		if opcion == 1: # agregar contacto
			c = input(" Indique el nombre del usuario que quiere agregar como contacto: ")
			contacto = registro.DarUsuario(c)
			usuario = registro.DarUsuario(nombre)
			# revisar si el usuario esta registrado en ALGOGRAM 
			if contacto != None:
				# agregar contacto a la lista de contactos del usuario de la sesion
				u = usuario.AgregarContacto(contacto)
				if u == True:
					print(" ")
					print (" El contacto ha sido agregado exitosamente. ")
					print(" ")
				else:
					print(" ")
					print(" Este usuario ya esta en su lista de contactos. ")
					print(" ")
			else:
				print(" ")
				print(" El contacto no es usuario de ALGOGRAM")
				print(" ")

		elif opcion == 2:

			contacto = input(" Indique el nombre del usuario que quiere eliminar de su lista de contactos: ")
			usuario = registro.DarUsuario(nombre)
			# eliminar contacto de la lista de contactos del usuario de la sesion
			u = usuario.EliminarContacto(contacto)
			if u == True:
				print(" ")
				print (" El contacto ha sido eliminado exitosamente. ")
				print(" ")
			else:
				print(" ")
				print(" Este usuario no esta en su lista de contactos. ")
				print(" ")
		
		elif opcion == 3: # mostrar contactos
			usuario = registro.DarUsuario(nombre)
			usuario.MostrarContactos()

		elif opcion == 4: # ver conversacion
			c = input(" Ver conversacion con el contacto: ")
			contacto = registro.DarUsuario(c)
			# revisar si el usuario dado es contacto del usuario de la sesion
			usuario = registro.DarUsuario(nombre)
			if usuario.BuscarContacto(c) == True:
				# buscar la conversacion con el usuario
				chat = conversaciones.BuscarConversacion(Chat(usuario,contacto).ID)
				if chat != None:
					print("---------------------------------------------------------------")		
					if c.lower() < nombre.lower():
						ID = str(c)+"-"+str(nombre)
					else:
						ID = str(nombre)+"-"+str(c)
					print("Chat "+ID)
					chat.MostrarChat()
					print("---------------------------------------------------------------")
				else:
					print(" ")
					print(" No hay conversaciones con el contacto "+str(c))
					print(" ")
					print(" Si desea iniciar una conversacion con "+str(c)+" elija la opcion 5.")
					print(" ")
				
			else:
				print(" ")
				print(str(c)+" no esta en su lista de contactos")
				print(" ")
				extra = input(" Si desea agregar a "+str(c)+" a su lista de contactos, elija la opcion 1. ")

		elif opcion == 5: # enviar mensaje
			c = input(" Enviar mensaje a: ")
			contacto = registro.DarUsuario(c)
			# revisar si el usuario dado es contacto del usuario de la sesion
			usuario = registro.DarUsuario(nombre)
			if usuario.BuscarContacto(c) == True:
				if c.lower() < nombre.lower():
					ID = str(c)+"-"+str(nombre)
				else:
					ID = str(nombre)+"-"+str(c)
				m = input(" Su mensaje es: ")
				chat = conversaciones.BuscarConversacion(ID)
				# si el chat ya esta en la tabla, se agrega sobre ese chat
				if chat != None:
					chat.AgregarMensaje(usuario,str(m))
					agregar = conversaciones.AgregarConversacion(chat)
				# si el chat no esta en la lista
				else:
					# creamos un nuevo chat y se agrega sobre ese chat
					chat_nuevo = Chat(usuario,contacto)
					chat_nuevo.AgregarMensaje(usuario,str(m))
					agregar = conversaciones.AgregarConversacion(chat_nuevo)
				if agregar == True:
					print(" ")
					print(" Su mensaje ha sido enviado a "+str(c))
					print(" ")
			else:
				print(" ")
				print(str(c)+" no esta en su lista de contactos")
				print(" ")
				extra = input(" Si desea agregar a "+str(c)+" a su lista de contactos, elija la opcion 1. ")
				pass
			
		elif opcion == 6:
			mostrarCaritas()
			

		elif opcion == 7:  
			registro.MostrarRegistro()

		elif opcion == 8: 
			print(" ")
			print("Cerrando Sesion")
			print(" ")
			menu_principal()
		
		elif (opcion > 8) or (opcion < 1):
			print(" ")
			print("Error, la opcion seleccionada no es valida")
			print("")
			
	return
			

# Procedimientos para las caritas

## Cargar caritas 
def cargarCaritas():
	print('')
	print('A continuacion, inserte el nombre del paquete de caritas.')
	print('Los nombres son: caritas1, caritas2 y caritas3.')
	nombreArchivo = input('Escriba el nombre del paquete de su preferencia: ')
	print('')
	if nombreArchivo == 'caritas1':
		file = open('caritas1.txt','r')
	elif nombreArchivo == 'caritas2':
		file = open('caritas2.txt','r')
	elif nombreArchivo == 'caritas3':
		file = open('caritas3.txt','r')
	else:
		print('El nombre que introdujo es invalido, o no pertenece a nuestro paquete de caritas.')
		return
	line = file.readline()
	codCaras = line.split('	')
	
	global caritas
	caritas = ArrayT(len(codCaras))
	
	for i in range(len(codCaras)):
		caritas.__setitem__(i, codCaras[i])
	
	print('Su paquete de caritas ha sido cargado exitosamente.')
	return codCaras
	
	
# Mostrar caritas	
def mostrarCaritas():
	
	if caritas is not None:
		print('El paquete de caritas cargado es el siguiente: ')
		for i in range(caritas.__len__()):
			carita = caritas.__getitem__(i)
			carita = carita[:carita.index("=")]
			if i < caritas.__len__() - 1:
				print(carita, end=", ")
			else:
				print(carita)
	else:
		print("No se ha cargado ningun paquete de caritas, puede hacerlo en el menu principal.")
		
	return

menu_principal()
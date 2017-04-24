# PROYECTO 3

# DESCRIPCIÓN: Cliente que probará el correcto funcionamiento de
# la implementación de la aplicación de mensajeria ALGOGRAM

# AUTORES: Jesus Kauze y David Segura
# EMAILS: 12-10273@usb.ve y 13-11341@usb.ve

from usuario import Usuario
from registro_usuarios import RegistroUsuarios
import sys
from chat import TAD_chat
from conversaciones import h1
from conversaciones import HashEntry, TAD_Conversaciones, Dlist
from extra import cargarCaritas, mostrarCaritas


Registro = RegistroUsuarios()
Registro.crearTabla(1000)
tablita = TAD_Conversaciones()
tablita.crear_tablaC(100)

mensaje2 = TAD_chat()

def enviar_mensaje(x):
	segundo_user = input("> Nombre del usuario a enviar mensaje: ")
	if Registro.buscarUsuario(segundo_user)==False:
		print("\n>ERROR< Este usuario no se encuentra registrado")
		return
	mensaje2.crear_chat(nombre, segundo_user)
	while True:
		msj_a_enviar = input(">>> Escribe tu mensaje y presiona ENTER o presiona ENTER para salir: ")
		if msj_a_enviar == "":
			break
		mensaje2.agregar_mensajes(nombre, msj_a_enviar)
		tablita.agregar_chat(mensaje2)
		return

def ver_conversacion():
	segundo_user = input("> Nombre del usuario a mostrar conversacion: ")
	if Registro.buscarUsuario(segundo_user)==False:
		print("\n>ERROR< Este usuario no se encuentra registrado")
	tablita.search_key(nombre+"-"+segundo_user)
	return

while True:
	print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n"+
		"* ALGOGRAM by David&Kauze           *\n"+
		"* (1) Registrarse                   *\n"+
		"* (2) Iniciar sesión                *\n"+
		"* (3) Cargar usuarios               *\n"+
		"* (4) Eliminar usuario              *\n"+
		"* (5) Cargar caritas                *\n"+
		"* (6) Salir                         *\n"+
		"*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
	opcion = input("~~~~> INTRODUCIR OPCIÓN: ")
	try:
		if int(opcion) == 1:
			print("~~~~REGISTRARSE~~~~")
			nombre = input("> Nombre: ")
			contrasena = input("> Contraseña: ")
			telefono = input("> Teléfono: ")
			p = Usuario()
			error = True
			if p.crearUsuario(nombre,contrasena,telefono,None) == True:
				validar = Registro.agregarUsuario(p)
			else:
				error = False
			if error == False:
				print(">>> Usuario no creado.")
			else:
				if validar == False:
					print(">>> ERROR: Ya existe un usuario registrado con ese nombre.")
				else:
					print(">>> Usuario creado.")
			continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
		elif int(opcion) == 2:
			print("~~~~INICIAR SESIÓN~~~~")
			nombre = input("> Nombre: ")
			contrasena = input("> Contraseña: ")
			key = h1(nombre) % len(Registro.tablaRU)
			lista = Registro.tablaRU[key]
			menu = False
			while lista != None:
				if lista.element.nombre == nombre:
					if lista.element.password == contrasena:
						menu = True
						usuario = lista.element
						while True:
							print(">>> SESIÓN: "+usuario.nombre+" <<<\n"
								"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"+
								"| (1) Agregar Contacto              |\n"+
								"| (2) Eliminar Contacto             |\n"+
								"| (3) Mostrar Contactos             |\n"+
								"| (4) Ver Conversación              |\n"+
								"| (5) Enviar Mensaje                |\n"+
								"| (6) Mostrar Caritas               |\n"+
								"| (7) Mostrar Usuarios Registrados  |\n"+
								"| (8) Cerrar Sesión                 |\n"
								"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
							opcion = input("~~~~> INTRODUCIR OPCIÓN: ")
							try:
								if int(opcion) == 1:
									print("....AGREGAR CONTACTO....")
									contacto = input("> Contacto: ")
									if Registro.buscarUsuario(contacto)[0] == True:
										if usuario.agregarContacto(Registro.buscarUsuario(contacto)[1]) == True:
											print(">>> Contacto Agregado")
											continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
										else:
											continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
									else:
										print(">>> ERROR: El contacto indicado no está registrado.")
										continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
								elif int(opcion) == 2:
									print("....ELIMINAR CONTACTO....")
									contacto = input("> Contacto: ")
									if usuario.eliminarContacto(contacto) == True:
										print(">>> Contacto Eliminado")
										continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
									else:
										continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
								elif int(opcion) == 3:
									print("....MOSTRAR CONTACTOS....")
									usuario.mostrarContactos()
									continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
								elif int(opcion) == 4:
									print("....VER CONVERSACIÓN....")
									ver_conversacion()
									continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
								elif int(opcion) == 5:
									print("....ENVIAR MENSAJE....")
									enviar_mensaje(Registro.buscarUsuario)
									continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
								elif int(opcion) == 6:
									print("....CARITAS....")
									mostrarCaritas(name_arh)
									continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
								elif int(opcion) == 7:
									print("....USUARIOS REGISTRADOS....")
									Registro.mostrarRegistro()
								elif int(opcion) == 8:
									print(">>> SESIÓN CERRADA")
									continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
								break
							except:
								print(">>> ERROR: OPCIÓN INVÁLIDA")
								continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
						break	
					else:
						print(">>> ERROR: CONTRASEÑA INCORRECTA")
						continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
						menu = True
						break
				else:
					lista = lista.next
			if menu == True:
				pass
			else:
				print(">>> ERROR: USUARIO NO ENCONTRADO")
				continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
		elif int(opcion) == 3:
			print("~~~~CARGAR USUARIOS~~~~")
			archivo = input("> Indique nombre del archivo: ")
			try:
				Registro.cargarUsuarios(archivo)
				print(">>> Usuarios cargados.")
				continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
			except:
				print(">>> ERROR: ARCHIVO NO ENCONTRADO.")
				continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
		elif int(opcion) == 4:
			print("~~~~ELIMINAR USUARIO~~~~")
			us = input("> Usuario: ")
			if Registro.eliminarUsuario(us) == True:
				print(">>> Usuario Eliminado")
				continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
			else:
				continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
		elif int(opcion) == 5:
			print("~~~~CARGAR CARITAS~~~~")
			name_arh = input("~~~~~~~~>INTRODUZCA EL NOMBRE DEL ARCHIVO: ")
			cargarCaritas(name_arh)
			continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
		elif int(opcion) == 6:
			break
		else:
			print(">>> ERROR: Opción Inválida")
			continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
	except: 
		print(">>> ERROR: Opción Inválida")
		continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
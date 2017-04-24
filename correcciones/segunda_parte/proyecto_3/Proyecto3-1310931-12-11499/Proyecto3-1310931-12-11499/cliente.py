#######################################
########                    ###########
######## MODULO CLIENTE     ###########
########                    ###########
#######################################

from usuario import *
from registro_usuarios import *
from chat import *
from conversaciones import *
import sys,argparse,random
import subprocess as sp

def cargarCaritas(archivo):

	paper = open(archivo,'r+')
	p = []
	for line in paper.readlines():
		l = line.split('=')
		p.append(l[0])

	return p


def mostrarCaritas(p):
	caritas = []
	for i in range(len(p)):
		caritas.append(p[i]+", ")

	print(caritas)


def MenuInicioSesion(usuario):

	while True: 
		print("\n\n Has iniciado sesion, escoge una opcion: \n\n")
		print("1. Agregar Contacto")
		print("2. Eliminar Contacto")
		print("3. Mostrar Contacto")
		print("4. Ver Conversacion")
		print("5. Enviar Mensaje")
		print("6. Mostrar Caritas")
		print("7. Mostrar Usuarios Registrados")
		print("8. Cerrar Sesion\n")

		opcion = int(input("\nIndique la opcion que desea: "))

		if opcion == 1:
			print("\nHas escogido agregar un contacto\n")
			nombre = str(input("Introduce el nombre del usuario que quieres agregar: "))
			telefono = str(input("Introduce su numero de telefono: "))
			usuario_a_agregar = Usuario(nombre,0,telefono)
			#usuario.AgregarContacto(usuario_a_agregar)
			print("Usuario agregado: " + nombre )
		elif opcion ==2:
			print("\nHas escogido agregar un contacto\n")
			nombre = str(input("Introduce el nombre del usuario que quieres eliminar: "))
			usuario_a_eliminar = Usuario(nombre,0,telefono)
			#usuario.EliminarContacto(usuario_a_eliminar)
			print("Usuario eliminado: " + nombre )
		elif opcion ==3:
			print("\n Has escogido Mostrar contactos\n")
			print("\nLamentablemente esta opcion no esta disponible actualmente, espera la actualizacion de ALGOGRAM\n")
					
			if opcion ==4:
					
					print("\nLamentablemente esta opcion no esta disponible actualmente, espera la actualizacion de ALGOGRAM\n")
			elif opcion ==5:
					nombre1 = str(input("Con que usuario deseas hablar: "))
					chat = chat(usuario.nombre,nombre1)
					mensaje = str(input("Escribe tu mensaje: "))
					print("Tu mensaje fue enviado")
					chat.AgregarMensajeAlChat(usuario,mensaje)
			elif opcion == 6:
					
					print("\n Has escogido Mostrar caritas\n")
					archivo = str(input("indica el nombre del archivo con las caritas: "))
					mostrarCaritas(cargarCartias(archivo))
			elif opcion == 7:
					print("\n No tenemos disponible esta opcion actualmente")

			elif opcion == 8:
					print("\n----------Hasta Luego-----------\n")
					return
						



if __name__ == "__main__":


	#############
	# Menu loop #
	#############
	Registro = RegistrodeUsuarios(100)
	
	while True:
		print("*****************************************")
		print("\n\n   Bienvenido a ALGOGRAM  \n\n")
		print("-----------------------------------------\n\n")

		print("1. Registrarse")
		print("2. Iniciar Sesion")
		print("3. Cargar Usuarios")
		print("4. Eliminar Usuarios")
		print("5. Cargar Caritas\n\n")

		opcion = int(input("Elige una opcion: "))
		assert ( opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5)


		if opcion == 1:
			print("\nHas escogido registrarte\n")
			nombre = input(("Introduce tu nombre el cual tambien sera tu nombre de usuario: "))
			password = str(input("Introduce una contrasena: "))
			telefono = str(input("Ingresa tu numero de telefono: "))

			Nuevo_Usuario = Usuario(nombre,password,telefono)
			Registro.AgregarUsuario(Nuevo_Usuario)

		elif opcion == 2:
			print("\n Has escogido iniciar sesion\n")
			nombre = input("Introduce tu nombre de usuario: ")
			password = input("Introduce una contrasena: ")

			UsuarioAuxiliar = Usuario(nombre,password,"000")

			if Registro.BuscarUsuario(UsuarioAuxiliar) == True:
				UsuarioIniciado = Registro.BuscarUsuario2(UsuarioAuxiliar)
				MenuInicioSesion(UsuarioIniciado)
			else:
				print("No estas registrado en ALGOGRAM, deberias hacerlo en la opcion 1")


		elif opcion == 3:
			"""para despues"""

			print("\nHas escogido cargar usuarios\n")
			archivo = str(input("Introduce el nombre del archivo donde estan los usuarios: "))
			Registro.cargarUsuarios(archivo)

		elif opcion == 4:

			print("\n Has escogido Eliminar Usuario\n")
			nombre = input("Introduce el nombre del usuario a eliminar: ")
			if Registro.BuscarNombre(nombre) == True:
				Registro.EliminarUsuario(nombre)
			else:
				print("\n----> El usuario NO existe\n")

		elif opcion == 5:
			print("\nEsogiste cargar caritas\n")
			archivo = str(input("Introduce el nombre del archivo en donde estan las caritas: "))
			caritas = cargarCaritas(archivo)

	
		








	############
	# Fin menu #
	############

	sys.exit()

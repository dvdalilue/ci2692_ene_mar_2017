import sys
from registro_usuarios import Dlist,Hash_table,HashEntry,Registro
from conversaciones import Conversaciones
from usuario import Usuario
from chat import Chat, ListaChat
from arrayT import ArrayT

def cargarCaritas(archivo):
	with open(archivo,"r") as f:
		#Leemos solo la primera linea del archivo
		car=f.readline()
		#Le quitamos los tab y los agregamos a un array
		car=car.split("	")
		caritas=ArrayT(len(car))
		for i in range(len(caritas)):
			caritas[i]=car[i]
	return caritas

def mostrarCaritas(listacaritas):
	#Hacemos split a cada string de carita en el arreglo para evitar tomar el numero
	print("Caritas disponibles:")
	caritas=ArrayT(len(listacaritas))
	for i in range(len(caritas)):
		cara=listacaritas[i].split("=")
		#Se toma la primera parte
		caritas[i]=cara[0]
	#Imprimimos las caritas
	string=" "
	for i in range(len(caritas)-1):#Para que no tome la ultima carita
		string=string + caritas[i].split("=")[0] + "	"
	string=string + caritas[len(caritas)-1]
	print(string)

def InicioSesion(usuario,registro_usuarios, conversaciones,caritas):
	#Menu de inicio de sesion
	print("Bienvenido, "+ usuario.nombre + ". Elija una opcion del menu.")
	menustr="1. Agregar contacto.\n2. Eliminar contacto.\n3. Mostrar contactos.\n4. Ver conversacion.\n5. Enviar mensaje.\n6. Mostrar caritas.\n7. Mostrar usuarios registrados.\n8. Cerrar sesion.\n9. Ver las opciones de menu."
	print(menustr)
	while True:
		m=int(input("Opcion: "))
		while m not in range(1,10):
			print("Opcion invalida. Intente de nuevo.")
			m=int(input("Opcion: "))
		
		if m==1:
			#Agregar un contacto
			nombre=input("Introduzca el nombre del contacto: ")
			while len(nombre)==0:
				print("Nombre invalido.")
				nombre=input("Introduzca el nombre del contacto: ")
			encontrar=registro_usuarios.buscarElemento(nombre) #Se busca el contacto en el registro.
			if encontrar!=None: #se encontro el contacto en el registro
				boolean=usuario.agregarContacto(encontrar)
				if boolean:
					print("El contacto "+nombre+" se ha agregado de manera exitosa.")
				else:
					print("El contacto que se quiere agregar ya se encuentra en la lista de contactos.")
			else: #no se encontro el contacto en el registro
				print("El contacto que se quiere agregar no se encuentra registrado.")
		
		elif m==2:
			#ELiminar un contacto de la lista de contactos
			nombre=input("Introduzca el nombre del contacto: ")
			while len(nombre)==0:
				print("Nombre invalido.")
				nombre=input("Introduzca el nombre del contacto: ")
			boolean=usuario.eliminarContacto(nombre)
			if boolean:
				print("El contacto se ha eliminado de manera exitosa.")
			else:
				print("El nombre introducido no pertenece a ninguno de sus contactos.")
		
		elif m==3:
			#Mostrar la lista de contactos
			usuario.mostrarContactos()
		
		elif m==4:
			#Mostrar los mensajes de un chat con otro usuario
			nombre=input("Introduzca el nombre del contacto: ")
			while len(nombre)==0:
				print("Nombre invalido.")
				nombre=input("Introduzca el nombre del contacto: ")
			#Las siguientes condiciones consiguen el id que debe tener el chat entre ambos usuarios
			if usuario.nombre<nombre:
				id_chat=usuario.nombre+"-"+nombre
			elif nombre<=usuario.nombre:
				id_chat=nombre+"-"+usuario.nombre
			chat=conversaciones.buscarConversacion(id_chat) #busca el chat en las conversaciones
			if chat==None: #No hay ningun chat con el id correspondiente
				print("No posee conversaciones con este usuario.")
			elif chat!=None: #Existe un chat
				print("Chat "+id_chat)
				#Como la estructura trabaja como una pila, se necesita voltear la lista para imprimir en orden los mensajes,
				#por lo cual se usa una lista auxiliar
				aux=ListaChat()
				x=chat.mensajes.head
				if x==None: #Si no hay head en la lista de mensajes del chat
					print("No hay mensajes en este chat.")
				else: #Hay al menos un mensaje en el chat
					while x!=None: #Se guardan los elementos del chat en la lista en orden inverso
						aux.add_element(x.usuario)
						x=x.next
					x=aux.head
					while x!=None: #se imprimen los mensajes de forma ordenada
						print(x.usuario)
						x=x.next
		
		elif m==5:
			#Enviar un mensaje a algun contacto
			nombre=input("Introduzca el nombre del contacto: ")
			while len(nombre)==0:
				print("Nombre invalido.")
				nombre=input("Introduzca el nombre del contacto: ")
			usuario2= usuario.buscarContacto(nombre)  #busca el contacto en la lista de contactos del usuario.
			buscarRegistro=registro_usuarios.buscarElemento(nombre) #Busca el contacto en el registro de usuarios
			if usuario2==None: #No se encontro un contacto con ese nombre
				print("EL usuario no esta en su lista de contactos.")
			else: #Se encontro un contacto con ese nombre
				if buscarRegistro==None: #El usuario no esta en el registro pero si en la lista de contactos.
					print("El usuario ya no esta registrado. Es probable que el usuario que intenta contactar haya sido eliminado.\nSolo se permiten conversaciones entre usuarios registrados.\nEl usuario no existente sera eliminado de manera automatica de su lista de contactos.")
					boolean=usuario.eliminarContacto(nombre)
				else:
					#Las siguientes lineas consiguen el id del chat entre ambos usuarios
					if usuario.nombre<usuario2.nombre:
						id_chat=usuario.nombre+"-"+usuario2.nombre
					elif usuario2.nombre<=usuario.nombre:
						id_chat=usuario2.nombre+"-"+usuario.nombre
					chat=conversaciones.buscarConversacion(id_chat) #busca en las conversaciones para ver si el chat existe. 
					if chat==None: #El chat no existe, hay que crearlo
						chat=Chat(usuario,usuario2)
						boolean = conversaciones.agregarConversacion(chat) #se agrega el chat a las conversaciones 
						assert(boolean==True)
					#Aqui el usuario elige entre mandar un mensaje o una carita
					print("1. Enviar mensaje.\n2. Enviar carita.")
					tipomensaje=int(input("Introduzca una opcion: "))
					while tipomensaje not in range(1,3):
						print("Introduzca una opcion valida.")
						tipomensaje=int(input("1. Enviar mensaje.\n2. Enviar carita."))
					if tipomensaje==1:
						mensaje=input("Mensaje: ")
						if len(mensaje)==0:
							mensaje = " "
						chat.agregarMensaje(usuario,mensaje) #agrega el mensaje al chat
					else:
						if caritas==None:
							print("No tiene un paquete de caritas, si desea agregar uno debe volver al menu anterior.")
						else:
							#En caritas tenemos el paquete de caritas
							for i in range(len(caritas)):
								print(str(int(i)+1)+". "+caritas[i].split("=")[0])
							carita=int(input("Introduzca el numero correspondiente a la carita que desea enviar: "))
							while carita not in range(1,len(caritas)+1):
								carita=int(input("Introduzca el numero correspondiente a la carita que desea enviar: "))
							chat.agregarMensaje(usuario,caritas[carita-1].split("=")[0]) #Agregamos la carita al chat en la posicion "carita-1" 
													#porque para el usuario empezamos en la posicion 1, y en el arreglo en 0.
					print("Se ha mandado de manera exitosa.")

		elif m==6:
			#Mostrar caritas
			if caritas==None:
				print("No ha cargado ningun paquete de caritas, si desea hacerlo vuelva al menu anterior.")
			else:
				mostrarCaritas(caritas)
		
		elif m==7:
			registro_usuarios.mostrarRegistro()
		
		elif m==8:
			break
		
		elif m==9:
			print(menustr)

def menu():
	#Menu Loop
	#Comenzamos el registro de usuarios vacío, hasta que se deseen cargar mas por las opciones del menu
	registro_usuarios=Registro(15)
	conversaciones=Conversaciones(15)
	caritas=None
	while True:
		strmenu1=("\n	ALGOGRAM	\n1. Registrarse.\n2. Iniciar sesion.\n3. Cargar usuarios.\n4. Eliminar usuario.\n5. Cargar caritas.\n6. Salir.")
		print(strmenu1)
		opcion1=int(input("Introduzca una opcion: "))
		while opcion1 not in range(1,7):
			opcion1=int(input("Introduzca una opcion: "))
		if opcion1==1:
			#Registrarse
			nombre=input("Introduzca su nombre de usuario: ")
			while len(nombre)==0:
				nombre=input("Introduzca su nombre de usuario: ")
			password=input("Introduzca su contraseña: ")
			while len(password)==0:
				password=input("Introduzca su contraseña: ")
			telefono=int(input("Introduzca su numero de telefono: "))
			while telefono not in range(0,99999999999):
				telefono=int(input("Introduzca su numero de telefono: "))
			#Creamos una instancia de usuario
			usuario=Usuario(nombre,password,str(telefono),None)
			#Comprobamos si el usuario esta registrado
			agrego=registro_usuarios.agregarUsuario(usuario)
			if agrego==True:
				print("Se ha agregado un nuevo usuario.")
				print("Introduzca sus contactos.")
				nombre_contacto="abcde"	#Iniciamos nombre_contacto con un string cualquiera para que entre al while loop y 
										#el usuario pueda introducir sus contactos hasta presionar enter
				while len(nombre_contacto)!=0:
					nombre_contacto=input("Introduzca el nombre de su contacto (Presione Enter si ha terminado): ")
					if len(nombre_contacto)!=0:
						#Buscamos el usuario para comprobar si está entre los usuarios del registro
						contacto=registro_usuarios.buscarElemento(nombre_contacto)
						if contacto!=None: #Si el usuario esta en el registro
							#Si no lo agregamos a los contactos del usuario
							boolcontacto=usuario.agregarContacto(contacto)
							if boolcontacto==True:
								print("Se ha agregado a "+ nombre_contacto +" a su lista de contactos.")
							elif boolcontacto==False:
								print("El contacto ya se encuentra en su lista de contactos.")
						else:
							print("El usuario que desea agregar a sus contactos no se encuentra en el registro de usuarios.")
			elif agrego==False:
				print("El usuario ya se encuentra en el registro.")

		elif opcion1==2:
			#Iniciar sesion
			nombre=input("Introduzca su nombre de usuario: ")
			while len(nombre)==0:
				print("Nombre invalido.")
				nombre=input("Introduzca su nombre de usuario: ")
			usuario=registro_usuarios.buscarElemento(nombre) #Se busca el usuario en el registro.
			if usuario!=None: #El usuario se ha encontrado
				passwd=input("Introduzca su contraseña: ")
				if usuario.password==passwd:
					InicioSesion(usuario,registro_usuarios, conversaciones,caritas)
				else: 
					print("Contraseña incorrecta.")
			else:
				print("Este usuario no esta registrado.")

		elif opcion1==3:
			#Cargar usuarios
			#Pedimos el registro de usuarios
			registro=input("Introduzca el path al registro de usuarios: ")
			agrego=registro_usuarios.cargarUsuarios(registro)
			if not agrego:
				print("Ocurrio un error inesperado. Revise su archivo e intente nuevamente.")

		elif opcion1==4:
			#Eliminar usuario
			usuario_eliminar=input("Introduzca el nombre del usuario que desea eliminar: ")
			eliminado=registro_usuarios.eliminarElemento(usuario_eliminar)
			if eliminado==True:
				print("Se ha eliminado a "+ usuario_eliminar +" del registro de usuarios.")

		elif opcion1==5:
			paquete=input("Introduzca el path al paquete de caritas que desea usar: ")
			caritas=cargarCaritas(paquete)
			print("Se ha cargado un nuevo paquete de caritas.")
			
		elif opcion1==6:
			sys.exit()

menu()
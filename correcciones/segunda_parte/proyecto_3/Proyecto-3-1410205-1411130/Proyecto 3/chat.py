from usuario import NodoLista

class ListaChat:
	def __init__(self):
	#Inicializa una lista simplemente enlazada para los mensajes del chat
		self.head=None

	def add_element(self,elemento): 
		elemento=NodoLista(elemento)
		if self.head==None:
			self.head=elemento
		else:
			self.head.prev=elemento
			elemento.next=self.head
			self.head=elemento

class Chat:
	def crearChat(self, usuario1,usuario2):
		if len(usuario1.nombre)==0 and len(usuario2.nombre)==0:
			print("Error: Los nombres de los usuarios no son validos.")	
		elif usuario1.nombre<usuario2.nombre:
			self.id=usuario1.nombre+"-"+usuario2.nombre
		elif usuario2.nombre<=usuario1.nombre:
			self.id=usuario2.nombre+"-"+usuario1.nombre

	def __init__(self,usuario1,usuario2):
		self.id=" "
		self.crearChat(usuario1,usuario2)
		self.mensajes=ListaChat()

	def agregarMensaje(self,usuario,mensaje):
		self.mensajes.add_element(usuario.nombre+": "+mensaje)
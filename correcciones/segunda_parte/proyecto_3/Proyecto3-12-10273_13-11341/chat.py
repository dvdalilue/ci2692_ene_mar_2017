"""PROYECTO 3
# DESCRIPCIoN: TAD chat de ALGOGRAM.
# AUTORES: Jesus Kauze y David Segura
# EMAILS: 12-10273@usb.ve y 13-11341@usb.ve
"""
import hashlib

class Pila_Lista(object):
	def __init__(self, elemento, nxt):
		self.elemento = elemento
		self.next =  nxt

class TAD_chat():

	def __init__(self):
		self.id = None  #No nulo #user1-user2
		self.head = Pila_Lista(None, None)
		self.temp = Pila_Lista(None, None)

	def crear_chat(self, User1, User2):
		if User1 == "" or User2 == "":
			return False
		self.id = User1 + "-" + User2
		return True

	def agregar_mensajes(self, user, m):
		#string = user.nombre + ": " + m 
		string = user + ": " + m
		if self.head.elemento == None:
			self.head.next = self.temp
			self.head = Pila_Lista(string, None)
			self.temp = self.head
		else:
			self.temp.next = Pila_Lista(string, None)
			self.temp = self.temp.next

	def mostrar(self):
			x = self.head
			while x != None:
				print(x.elemento)
				x = x.next
			print(x)
			return x
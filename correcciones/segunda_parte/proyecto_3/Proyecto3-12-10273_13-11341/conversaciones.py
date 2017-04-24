import hashlib
from chat import Pila_Lista
from chat import TAD_chat

############################
########FUNCION HASH########
############################

def h1(clave):
	h = hashlib.sha256(clave.encode())
	return int(h.hexdigest(), base=16)

class HashEntry(object):
	def __init__(self,previous,key,element,nxt):
		self.element = element
		self.key = key
		self.nxt = nxt
		self.previous = previous

class Dlist(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self,elemento):
        if self.count == 0:
            self.count += 1
            self.head = elemento
        else:
            self.count += 1
            anterior = self.head
            anterior.nxt = elemento
            elemento.previous = self.head
            self.head = elemento

class TAD_Conversaciones(object):
	def __init__(self):
		self.tabla = []
				
	def crear_tablaC(self, n):
		for i in range(n):
			self.tabla.append(None)

	def agregar_elemento(self,e):
		valido = False
		#print(e.key)
		hashe = h1(e.key) % len(self.tabla)
		if self.tabla[hashe] == None:
			self.tabla[hashe] = Dlist()
			self.tabla[hashe].push(e)
		else:
			i = self.tabla[hashe].head
			for x in range(self.tabla[hashe].count):
				if i.key == e.key:
					i.element = e.element
					valido = True
				else:
					i = i.previous
			if valido == False:
				 self.tabla[hashe].push(e)


	def agregar_chat(self,c):
		i = c.id
		v = c.head
		if len(self.tabla) == 0:
			print("Crea la tabla primero")
		else:
			self.agregar_elemento(HashEntry(None,i,v,None))		

	def search_key(self,c):
		p = HashEntry(None,c,None,None)
		valido = False
		hashe = h1(p.key) % len(self.tabla)
		if self.tabla[hashe] != None:
			i = self.tabla[hashe].head
			for x in range(self.tabla[hashe].count):
				if i.key == p.key:
					z = i.element
					while z != None:
						print(z.elemento)
						z = z.next
					print(z) 
					valido = True
					return valido
				else:
					i = i.previous
			if valido == False:
				return valido
		else:
			return valido


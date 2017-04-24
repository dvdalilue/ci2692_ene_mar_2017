from nodoChat import Nodo

class Mensajes:
	def __init__(self):
		self.head = None
		self.count = 0
        
	def is_empty(self):
		if self.head != None:
			return False
		else:
			return True
    		
    		
	def push ( self,x):
		x = Nodo(x , self.head)
		self.head = x
		self.count = self.count +1
    
	def pop ( self):
		if self.count != 0:
			z = self.head
			self.head = self.head.next
			self.count = self.count - 1
			return (z.element)
		else:
			return (self.head)
    		
	def top(self):
		return  self.head.element
    	
	def size(self):
		return self.count
		
	def Mostrar(self):
		x = self.head
		while x != None:
			print(x.element)
			x = x.next
		
	def buscar(self,name):
		elemento = self.head
		while elemento != None and elemento.element!= name:#.clave
			elemento = elemento.next
		return elemento
	



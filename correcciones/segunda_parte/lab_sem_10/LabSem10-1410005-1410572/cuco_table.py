import hashlib
from cuco_entry import CucoEntry
from arrayT import ArrayT
import math

def h1(key):
	h = hashlib.sha256(key.encode())
	return int(h.hexdigest(), base=16)

def h2(key):
	h = hashlib.md5(key.encode())
	return int(h.hexdigest(), base=16)

def token(key):
	h = hashlib.md5(key.encode())
	return h.hexdigest()

class CucoTable():
	def __init__(self,n):
		self.size = n
		self.array  = ArrayT(n)
		for i in range(self.size):
			self.array[i]  = None

	def AddEntry(self,key,value):
		x = CucoEntry(key,value)
		position = h1(key)%self.size
		for i in range(int(math.log(self.size,2)) + 1):
			if self.array[position] == None:
				self.array[position] = x
				return
			else:
				self.array[position], x = x, self.array[position]
				if position == h1(x.key)% self.size:
					position = h2(x.key)% self.size
				else:
					position = h1(x.key)% self.size
		
		self.Rehash()
		self.AddEntry(x.key,x.value)

	def DeleteEntry(self, key):
		position = h1(key) % self.size
		value = None

		if self.array[position] != None and self.array[position].key == key:
			value = self.array[position].value
			self.array[position] = None
		
		else:
			position = h2(key) % self.size
			if self.array[position] != None and self.array[position].key == key:
				value = self.array[position].value
				self.array[position] = None

		return value

	def Search(self, key):
		position = h1(key)% self.size
		value = None

		if self.array[position] != None and self.array[position].key == key:
			value = self.array[position].value
		
		else:
			position = h2(key)% self.size
			if self.array[position] != None and self.array[position].key == key:
				value = self.array[position].value

		return value

	def Show(self):
		if self.size == 0:
			print("Tabla vacia")
			return

		for i in range(self.size):
			if self.array[i] != None:
				print("<Clave="+str(self.array[i].key)+">","<Valor="+self.array[i].value+">")

	def Rehash(self):
		print("doing rehashing")
		base = self.array
		self.size = self.size*2
		self.array = ArrayT(self.size)

		for i in range(len(base)):
			if base[i] != None:
				self.AddEntry(base[i].key, base[i].value)
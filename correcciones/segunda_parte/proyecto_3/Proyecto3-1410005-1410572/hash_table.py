from dList import * 
from arrayT import ArrayT
class hashTable(object):
	def __init__(self, size):
		self.size = size
		
		temp = ArrayT(self.size)
		
		for i in range(self.size):
			temp[i] = dList()

		self.array  = temp
	

	def addEntry(self, e):
		index = hash(e.key) % self.size
		return self.array[index].push(e)

	def addEntryInOrder(self, e):
		index = hash(e.key) % self.size
		return self.array[index].pushInOrder(e)

	def addValue(self, key, value):
		x = hashEntry(key, value)
		return self.addEntry(x)

	def internalDelete(self, key):
		index = hash(key) % self.size
		return self.array[index].pop(key)

	def delete(self, e):
		self.internalDelete(e.key)
		
	def deleteKey(self, key):
		return self.internalDelete(key)

	def search(self, key):
		index = hash(key) % self.size
		return self.array[index].search(key)

	def searchValue(self, e):
		for i in range(self.size):
			x = self.array[i].head

			while x != None:
				if x.value.lower() == e.lower():
					return True
				x = x.next
		return False

	def show(self):
		k = 0
		for i in range(self.size):
			
			x = self.array[i].head

			while x != None:
				k= k+1
				print("Nombre: "+str(x.value.nombre))
				x = x.next

		if k == 0 :
			print("Tabla vacia")


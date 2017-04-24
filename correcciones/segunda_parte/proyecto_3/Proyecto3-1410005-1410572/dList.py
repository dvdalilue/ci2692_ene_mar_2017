from hashEntry import *
class dList(object):
	def __init__(self):
		self.head = None

	def pushInOrder(self, e):
		x = self.head

		while x != None:
			if x.key == e.key:
				return False

			x = x.next
		
		if self.head == None:
			self.head = e
		else:
			
			x = self.head	
			while x != None and e.value.nombre > x.value.nombre:
				if x.next != None:
					x = x.next
				else:
					break
			if e.value.nombre > x.value.nombre:
				if x.next != None:
					e.prev = x
					e.next = x.next
					x.next.prev = e
					x.next = e
				elif x.next == None:
					e.prev = x
					x.next = e
			else:
				if x.prev != None:
					e.next = x
					e.prev = x.prev
					x.prev.next = e
					x.prev = e
				elif x.prev == None:
					e.next = x
					x.prev = e
					self.head = e
	
		return True

	def push(self, e):
		x = self.head

		while x != None:
			if x.key == e.key:
				return False

			x = x.next


		if self.head != None:
			self.head.prev = e 
			e.next = self.head

		self.head = e

		return True

	def pop(self, key):
		x = self.head

		while x != None :
			if x.key == key:
				if x.prev != None and x.next != None:
					x.prev.next = x.next
					x.next.prev = x.prev
				elif x.prev == None:
					if x.next != None:
						x.next.prev = None
					self.head = x.next
				elif x.next == None:
					if x.prev != None:
						x.prev.next = None

				return x.value

			x = x.next

	def search(self, key):
		x = self.head

		while x != None :
			if x.key == key:
				return x.value

			x = x.next
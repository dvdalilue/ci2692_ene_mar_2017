class hashEntry(object):
	"""
		Clase que implementa una entrada 
		para una tabla de Hash.
	"""

	def __init__(self, key, value):
		self.key	= key
		self.next 	= None
		self.prev	= None
		self.value  = value

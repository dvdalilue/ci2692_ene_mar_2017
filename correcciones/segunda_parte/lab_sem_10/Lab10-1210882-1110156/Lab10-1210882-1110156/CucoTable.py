from arrayT import ArrayT
from CucoEntry import *
import hashlib

def Hash1(clave):
	h= hashlib.sha256(clave.encode())
	return int(h.hexdigest(), base=16)
def Hash2(clave):
	h= hashlib.md5(clave.encode())
	return int(h.hexdigest(), base=16)
		

class CrearCucoTable:

	def __init__(self,n):
		self.tabla= ArrayT(n)
		self.size = n
	
		
	def Crearcucotabla(self, n):
		self.tabla= ArrayT(n)
		self.size = n
		return self.tabla
			
	def Rehash(self):
		Tabla=self.tabla
		self.tabla = ArrayT(2*self.size)
		self.size=len(self.tabla)
		for i in Tabla:
			if i!= None:
				self.Agregar(i.clave,i.valor)
			else:
				pass
		
		return self.tabla
		 
	def Agregar(self,c,v):
		elemento= CucoEntry(c,v)
		pos1 = Hash1(elemento.clave)%self.size
		pos2 = Hash2(elemento.clave)%self.size
		if self.tabla[pos1] != None and self.tabla[pos1].clave== elemento.clave:
			self.tabla[pos1].valor= v
			return
		if self.tabla[pos2]!= None and self.tabla[pos2].clave == elemento.clave:
			self.tabla[pos2].valor = v
			return
		for i in range(self.size):
			if self.tabla[pos1] == None:
				self.tabla[pos1] = elemento
				return
			else:
				elemento,self.tabla[pos1]=self.tabla[pos1],elemento
				if pos1 == (Hash1(elemento.clave))%self.size:
					pos1 = (Hash2(elemento.clave))%self.size
				else:
					pos1 = (Hash1(elemento.clave))%self.size
				
		self.Rehash()
		self.Agregar(elemento.clave,elemento.valor)
					
		
	def Eliminar(self, c):
	
		pos1 = Hash1(c)%self.size
		pos2 = Hash2(c)%self.size
		if self.tabla[pos1]!=None and self.tabla[pos1].clave == c:
			self.tabla[pos1]=None
		elif self.tabla[pos2]!=None and self.tabla[pos2].clave == c:
			self.tabla[pos2]=None
			
		return None

		
	def Buscar(self,c):
		pos1=Hash1(c)%self.size
		pos2=Hash2(c)%self.size
		if self.tabla[pos1]!=None and self.tabla[pos1].clave == c:
			return self.tabla[pos1].valor
		elif self.tabla[pos2]!=None and self.tabla[pos2].clave == c:
			return self.tabla[pos2].valor
		
	def mostrar(self):
		for i in range(self.size):
			if self.tabla[i] != None:
				print((self.tabla[i].clave,self.tabla[i].valor))
		
		

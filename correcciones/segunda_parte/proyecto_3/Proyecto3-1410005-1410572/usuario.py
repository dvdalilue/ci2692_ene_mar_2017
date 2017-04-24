from hashEntry import *
from dList import * 

class Usuario():

    def __init__(self,nombre,password,telefono):
        if nombre == None or password == None or telefono == None or \
        len(nombre) == 0 or len(password) == 0 or len(telefono) == 0:
            print('No se pudo crear el usuario')
            return
        
        for i in range(len(telefono)):
            if telefono[i] not in ['0','1','2','3','4','5','6','7','8','9']:
                print('El telefono solo debe contener numeros')
                return
        
        self.nombre = nombre
        self.password = password
        self.telefono = telefono
        self.contactos = dList()
        
        
    def AgregarContacto(self, u):
        if self.contactos.search(u.nombre):
            return False
        self.contactos.pushInOrder(hashEntry(u.nombre,u))
        return True

    def EliminarContacto(self,n):
        return self.contactos.pop(n)

    def MostrarContactos(self):
        x = self.contactos.head
        count = 0
        while x != None:
            count += 1
            print(count,". ",x.value.nombre)
            x = x.next
        
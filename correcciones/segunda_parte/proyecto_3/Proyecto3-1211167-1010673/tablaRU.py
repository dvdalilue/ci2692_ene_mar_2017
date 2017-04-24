# Proyecto no. 3
# Autores:
# Jorge Sanchez 10-10673
# Greanny Vivas 12-11167

# Crear tabla de Hash como clase pública
from usuario import*
from listaEnlazada import ListaEnlazada

class tablaRU():

# Crear tabla:
    def __init__(self,n):
        self.size = n # pilas con el nombre de esto
        self.arregloHash = [ListaEnlazada() for i in range(self.size)] 

# Funcion de Hash:
    def FuncionHash(self,nombre):
    	size = self.size
    	return nombre % size 

# funcion AgregarUsuario que agrega un usuario a la tabla, solo si el usuario no existe en la tabla:
    def Agregar(self,u):
        mapeo = self.FuncionHash(hash(u.nombre))
        return self.arregloHash[mapeo].Agregar_enlista(u)

# funcion EliminarUsuario :
    def Eliminar(self,nombre):
        mapeo = self.FuncionHash(hash(nombre))
        return self.arregloHash[mapeo].Eliminar_enlista(nombre)

# Buscar con nombre:
    def Buscar(self,nombre):
    	mapeo = self.FuncionHash(hash(nombre))
    	slot = self.arregloHash[mapeo].Buscar_enlista(nombre)
    	if slot == None:
    		return slot
    	else:
    		return slot.nombre

# Buscar nombre para retornar el usuario completo:
    def SearchUser(self,nombre):
        mapeo = self.FuncionHash(hash(nombre))
        slot = self.arregloHash[mapeo].Buscar_enlista(nombre)
        return slot

# funcion para buscar el password del usuario:
    def SearchPassword(self,nombre,password):
        mapeo = self.FuncionHash(hash(nombre))
        slot = self.arregloHash[mapeo].Buscar_enlista(nombre)
        if slot.password == password:
            return True
        else:
            return False

# Mostrar pares de las listas de la tabla: 
    def Mostrar(self):
        print(" ")
        for i in range(len(self.arregloHash)):
            self.arregloHash[i].Mostrar_enlista()
        print(" ")
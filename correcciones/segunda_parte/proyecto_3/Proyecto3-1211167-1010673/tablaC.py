# Proyecto no. 3
# Autores:
# Jorge Sanchez 10-10673
# Greanny Vivas 12-11167

# Crear tabla de Hash como clase pública
from listaChats import*

class tablaC():

# Crear tabla:
    def __init__(self,n):
        self.size = n   
        self.arregloHash = [ListaChats() for i in range(self.size)] 

# Funcion de Hash:
    def FuncionHash(self,ID):
    	size = self.size
    	return ID % size 

    def SearchChat(self,ID):
        mapeo = self.FuncionHash(hash(ID))
        chat = self.arregloHash[mapeo].BuscarChat(ID)
        return chat

# Buscar con ID:
    def Buscar(self,ID):
        mapeo = self.FuncionHash(hash(ID))
        slot = self.arregloHash[mapeo].Buscar_enchats(ID)
        if slot == None:
            return slot
        else:
            return slot.ID

    # Agregar elemento:
    def Agregar(self,chat):
        mapeo = self.FuncionHash(hash(chat.ID))
        if self.Buscar(chat.ID) != None:
            self.arregloHash[mapeo].Modificar_enchats(chat)
            return True
        else:
            self.arregloHash[mapeo].Agregar_enchats(chat)
            return True


#
# NOMBRE DEL ARCHIVO: colaprioridad.py
# AUTOR: Edymar M.
# DESCRIPCION: Este programa implementa una cola de prioridades usando heapsort
# ULTIMA FECHA DE MODIFICACION: 016/02/2017
#

from  heap_functions import heap_sort
from arrayT import ArrayT 

class Prioridad:

    def __init__(self):
        self.cola = ArrayT(50)

    def eliminar(self):
        del self.cola[:]
        print(self.cola)
        return self.cola
        
    def aggElem(self, elemento, prioridad):
        self.cola.append([elemento,prioridad])

    def consultarMin(self):
        self.heap_sort(self.cola)
        print(self.cola[0])
        return self.cola[0]

    def extraerMin(self):
        self.consultarMax()
        del self.cola[0]
        print(self.cola)
        return self.cola

    def actualizarElem(self, elemento, prioridad):
        self.cola[self.busqueda(elemento)][1] = prioridad

    def busqueda(self,elemento):
        for i in range(0,len(self.cola)):
            if(self.cola[i][0] == elemento):
                return i

    def elimElem(self, elemento):
        self.cola[self.busqueda(elemento)] = '*'

    def mostrar(self):
        print(self.cola)

    
       
       

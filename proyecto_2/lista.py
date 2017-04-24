class NodoLista:
    def __init__(self, e, s, a):
        self.elemento = e
        self.siguiente = s
        self.anterior = a

class ListaReproduccion:
    def __init__(self):
        self.proxima = None
        self.numero_nodos = 0

    def agregar_final(self,e):
        aux = NodoLista(e,None, None)
        if self.numero_nodos == 0:
            self.proxima = aux
            self.proxima.siguiente = self.proxima
            self.proxima.anterior = self.proxima
        else:
            aux.anterior = self.proxima.anterior
            aux.anterior.siguiente = aux
            aux.siguiente = self.proxima
            self.proxima.anterior = aux

        self.numero_nodos += 1

    def agregar(self,e):
        self.agregar_final(e)
        self.proxima = self.proxima.anterior         

    def eliminar(self,tituloCancion):
        assert tituloCancion != "", "El titulo no puede ser vacío"
        
        aux = self.proxima
        i = 0
        while True:
            if aux.elemento.titulo == tituloCancion:
                break
            elif i > self.numero_nodos:
                raise Exception('La canción no se encuentra en la lista')
            aux = aux.siguiente
            i += 1

        aux.anterior.siguiente = aux.siguiente
        aux.siguiente.anterior = aux.anterior
        self.numero_nodos -= 1
        if self.numero_nodos == 0:
            self.proxima = None

        return aux
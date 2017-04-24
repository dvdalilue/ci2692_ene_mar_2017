from cancion import Cancion
from arrayT import ArrayT

class NodoLista:
    def __init__(self, e, s, a):
        self.elemento = e
        self.siguiente = s
        self.anterior = a

class ListaReproduccion:
    def __init__(self):
        self.proximo = None
        self.numero_nodos = 0
# funcion agregar_final que inserta un nodo cancion como elemento previo al elemento self.proximo:
    def agregar_final(self,cancion):
        existe = False
        global aux
        nueva_cancion = NodoLista(cancion,None,None)
        if self.numero_nodos == 0:
            self.proximo = nueva_cancion
            aux = nueva_cancion
            self.proximo.siguiente = self.proximo.anterior = nueva_cancion
            aux.anterior = aux.siguiente = nueva_cancion
            self.numero_nodos += 1
        else:
            for i in range(self.numero_nodos):
                if self.proximo.elemento.es_igual(cancion):
                    existe = True
                    print("--")
                    print("La cancion ya existe en la lista de reproduccion")
                self.proximo = self.proximo.siguiente
            if not existe:
                if self.proximo == aux:
                    aux = nueva_cancion
                self.proximo.anterior.siguiente = nueva_cancion
                nueva_cancion.anterior = self.proximo.anterior
                self.proximo.anterior = nueva_cancion
                nueva_cancion.siguiente = self.proximo
                self.numero_nodos += 1

# funcion agregar que inserta un nodo cancion al final de la lista:
    def agregar(self,cancion):
        existe = False
        global aux
        nueva_cancion = NodoLista(cancion,None,None)
        if self.numero_nodos == 0:
            self.proximo = nueva_cancion
            aux = nueva_cancion
            self.proximo.siguiente = self.proximo.anterior = nueva_cancion
            aux.anterior = aux.siguiente = nueva_cancion
            self.numero_nodos += 1
        else:
            for i in range(self.numero_nodos):
                if self.proximo.elemento.es_igual(cancion):
                    existe = True
                    print("--")
                    print("La cancion ya existe en la lista de reproduccion")
                self.proximo = self.proximo.siguiente
            if not existe:
                nueva_cancion.anterior = self.proximo
                self.proximo.siguiente = nueva_cancion
                nueva_cancion.siguiente = aux
                aux.anterior = nueva_cancion
                self.proximo = nueva_cancion
                self.numero_nodos += 1

# funcion que ordena la lista de canciones por titulo:
    def ordenar_titulo(self,lista):
        lista_ordenada = ListaReproduccion()
        if lista.numero_nodos > 1:
            mid = lista.numero_nodos//2
            izq = ListaReproduccion()
            der = ListaReproduccion()
            aux = lista.proximo
            for i in range(lista.numero_nodos):
                if i+1 <= mid:
                    izq.agregar_final(aux.elemento)
                elif i+1 > mid and i+1 <= lista.numero_nodos:
                    der.agregar_final(aux.elemento)
                aux = aux.siguiente
         
            if izq.numero_nodos > 1:
                izq = self.ordenar_artista(izq)
            if der.numero_nodos > 1:
                der = self.ordenar_artista(der)

            i=0
            j=0
            while i < izq.numero_nodos and j < der.numero_nodos:
                if izq.proximo.elemento.es_menor_artista(der.proximo.elemento):
                    lista_ordenada.agregar_final(izq.proximo.elemento)
                    i=i+1
                    izq.proximo = izq.proximo.siguiente
                else:
                    lista_ordenada.agregar_final(der.proximo.elemento)
                    j=j+1
                    der.proximo = der.proximo.siguiente


            while i < izq.numero_nodos:
                lista_ordenada.agregar_final(izq.proximo.elemento)
                i=i+1
                izq.proximo = izq.proximo.siguiente

            while j < der.numero_nodos:
                lista_ordenada.agregar_final(der.proximo.elemento)
                j=j+1
                der.proximo = der.proximo.siguiente
        return lista_ordenada
# funcion que ordena la lista de canciones por artista:
    def ordenar_artista(self,lista):
        lista_ordenada = ListaReproduccion()
        if lista.numero_nodos > 1:
            mid = lista.numero_nodos // 2
            izq = ListaReproduccion()
            der = ListaReproduccion
            aux = lista.proximo
            for i in range(lista.numero_nodos):
                if i+1 <= mid:
                    izq.agregar_final(aux.elemento)
                elif i+1 > mid and i+1 <= lista.numero_nodos:
                    print (aux.elemento.titulo)
                    print (aux.elemento.artista)
                    der.agregar_final(aux.elemento)
                aux = aux.siguiente
            if izq.numero_nodos > 1:
                izq = self.ordenar_artista(izq)
            if der.numero_nodos > 1:
                der = self.ordenar_artista(der)
            i = 0
            j = 0
            while j< der.numero_nodos and i< izq.numero_nodos:
                if izq.proximo.elemento.es_menor_titulo(der.proximo.elemento):
                     lista_ordenada.agregar_final(izq.proximo.elemento)
                     i = i+1
                     izq.proximo = izq.proximo.siguiente
                else:
                    lista_ordenada.agregar_final(der.proximo.elemento)
                    j = j+1
                    der.proximo = der.proximo.siguiente
            while i < izq.numero_nodos:
                lista_ordenada.agregar_final(izq.proximo.elemento)
                i = i+1
                izq.proximo = izq.proximo.siguiente
            while j < der.numero_nodos:
                lista_ordenada.agregar_final(der.proximo.elemento)
                j = j+1
                der.proximo = der.proximo.siguiente
        return lista_ordenada


    def mostrar(self):
        aux1 = self.proximo
        aux2 = self.proximo
        if aux1 == None:
            print("La lista no tiene canciones. Agregue una nueva cancion.")
        else:
            while aux is not None:
                print ("("+str(aux1.elemento.artista)+", "+str(aux1.elemento.titulo)+")")
                aux1 = aux1.anterior
                if aux1 == aux2:
                    break

# funcion Buscar que evalua si el titulo de la cancion se encuentra en la lista:
    def Buscar(self,tituloCancion):
        if self.proximo != None: # la lista no es vacia y hay elementos para buscar
            print("el self.proximo es: "+self.proximo.elemento.titulo)
            aux = self.proximo # guardamos el valor del proximo elemento en aux
            i = self.proximo # empezamos a revisar por self.proximo
            #siguiente = self.proximo.siguiente.elemento.titulo
            #print("el elemento siguiente es: "+siguiente)
            while i.siguiente != None:
                print("el titulo del siguiente es: "+i.siguiente.elemento.titulo)
                if i.elemento.titulo == tituloCancion:
                    print("el titulo del elemento a eliminar es: "+i.elemento.titulo)
                    return i
                elif i.elemento.titulo != tituloCancion:
                    print("el titulo del primero es distinto del titulo dado")
                    i = i.siguiente
                if i.siguiente == aux:
                    break
            return None

# armar eliminar con buscar otra vez######
    def eleminar(self,tituloCancion):
        cancion = self.Buscar(tituloCancion)
        print(cancion)
        if cancion != None:
            if cancion == self.proximo:
                if self.numero_nodos != 1:
                    self.proximo = self.proximo.anterior
                    cancion.anterior.siguiente = cancion.siguiente
                    cancion.siguiente.anterior = cancion.anterior
                    self.numero_nodos -= 1
                elif self.numero_nodos == 1:
                    self.proximo.siguiente = self.proximo.anterior = None
                    self.proximo = None
                    self.numero_nodos -= 1
        else:
            print ("La cancion no existe en la lista de reproduccion")
            print(cancion)

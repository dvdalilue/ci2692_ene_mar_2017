
# AUTOR: ANGEL MORANTE
# DESCRIPCION: Este programa implementa una cola de prioridades usando heapsort


class colaprioridad:

    def __init__(self):
        self.cola = []

    def eliminar(self):
        del self.cola[:]
        print(self.cola)
        return self.cola
        
    def agregarElem(self, elemento, prioridad):
        self.cola.append([elemento,prioridad])

    def consultarMax(self):
        self.heapsort(self.cola)
        print(self.cola[0])
        return self.cola[0]

    def extraerMax(self):
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

    def heapsort(self,A):
        self.buildHeap(A)
        for i in range(len(A)-1, 0, -1):
            A[0][1], A[i][1] = A[i][1], A[0][1]
            self.heapify(A, 0, i)

    def buildHeap(self,A):
        for i in range(len(A)//2-1, -1, -1):
            self.heapify(A,i,len(A))

    def heapify(self, A, idx, m):
        largest = idx
        left = 2*idx+1
        right = 2*idx+2
        if(left < m and A[left][1] > A[idx][1]):
            largest = left
        if(right < m and A[right][1] > A[largest][1]):
            largest = right
        if(largest != idx):
            A[idx][1], A[largest][1] = A[largest][1], A[idx][1]
            self.heapify(A, largest, m)

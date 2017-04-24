"""
# Descripcion: Modulo con la implementacion de algoritmos de ordenamientos
#              para el ordenamiento HEAP SORT
# Autor: Orlando Chaparro Carnet: 12-11499
         Angel Morante Carnet: 13-10931
# email: 12-11499@usb.ve
         13-10931@usb.ve // morante413@gmail.com

"""
from arrayT import ArrayT

## HEAPIFY LA CUAL MANTIENE LA CONDICION DE HEAP 
## ESTA FUNCION RECIBE UN ARREGLO Y HACE UN INTERCAMBIO DE LOS NODOS EN CASO DE SER
## NECESARIO
def heapify(array, i, lenght):
    hijo_izq = left(i)
    hijo_der = right(i)
    el_mayor = i
    if hijo_izq < lenght and array[hijo_izq] > array[i]:
        el_mayor = hijo_izq
    if hijo_der < lenght and array[hijo_der] > array[el_mayor]:
        el_mayor = hijo_der
    if el_mayor != i:
        swap(array, el_mayor, i)
        heapify (array, el_mayor, lenght)


#INICIO DE LA FUNCOIN BUILD MAX HEAP
def build_max_heap(array):

    a = (len(array)-1) // 2
    for i in range(a,-1,-1):
        heapify(array,i,len(array))
      

#HEAPSORT (ORDENAMIENTO POR MONTICULO)
def heap_sort(array):
    build_max_heap(array)
    a = len(array) - 1
    for i in range(a,0,-1):
        swap(array,0,i)
        heapify(array,0,i)
       
def swap(array, i, j):
    array[i], array[j] = array[j] , array[i]

def dequeue(array):
    if len(array) < 1:
        print("El arreglo debe tener mas de un elemento")
    aux_array = ArrayT(len(array)-1)
    for i in range(1,len(array)):
        aux_array[i-1] = array[i]
    heapify(aux_array,0,len(aux_array))
    return (array[0],aux_array) 

def parent(i):
    return ((i + 1) // 2) - 1

def left(i):
    return (2*(i+1)-1)

def right(i):
    return (2*(i+1))



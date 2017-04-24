from random import randint
from heap_functions import swap

def quicksort_basico(A):
    p=0
    r=len(A)-1
    B=quicksort_aux(A,p,r)
    return B

def quicksort_aux(A,p,r):
    if p<r:
        q=partition(A,p,r)
        A=quicksort_aux(A,p,q-1)
        A=quicksort_aux(A,q+1,r)
    return A
   
def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            A=swap(A,i,j)
    A=swap(A,i+1,r)
    return i+1

def quicksort_aleatorio(A):
    p=0
    r=len(A)-1
    B=rand_quicksort_aux(A,p,r)
    return B

def rand_quicksort_aux(A,p,r):
    if p<r:
        q=partition_aleatoria(A,p,r)
        A=rand_quicksort_aux(A,p,q-1)
        A=rand_quicksort_aux(A,q+1,r)
    return A

def partition_aleatoria(A,p,r):
    i=randint(p,r)
    A=swap(A,i,r)
    return partition(A,p,r)


""" Al realizar las pruebas, observamos que para la opcion de prueba con elementos
aleatorios, quicksort_basico y quicksort_aleatorio tardan menos tiempo en ordenar
los elementos. Por otra parte, al realizar las pruebas con 1000 o mas elementos para la 
opcion de elementos ordenados de manera descendente, ya que es el peor caso para quicksort_basico, 
se realizan demasiadas llamadas recursivas por lo que se obtiene un error y tenemos tiempo n**2.
Al realizar las pruebas con 1000 o mas elementos para la opcion de elementos iguales a cero o uno,
se obtiene un error en quicksort_aleatorio. Esto se debe a que la probabilidad de escoger 0 o 1 es
la misma, pues son los unicos elementos del arreglo. Además si el pivote es uno, tendra que realizar
la llamada recursiva para comparar con todos los elementos pues siempre seran menores o iguales a el.
Por otro lado, si el pivote es cero, tendra que comparar con todos los ceros y realizara llamadas
recursivas para cada uno de ellos. Con quicksort_basico se obtiene un error similar.
    Debido a los errores por la cantidad de llamadas recursivas, decidimos probar con numeros menores
a 900 para poder comparar los tiempos de los algoritmos. Para la prueba 2 se obtiene que quicksort_basico
es el que tarda mas en ordenar los elementos, pues como mencionamos antes, es el peor caso para el 
algoritmo. Claramente, quicksort_aleatorio toma menos tiempo pues el pivote se escoge aleatoriamente
y se evita el peor caso. Para la prueba 3, obtuvimos que quicksort_basico y quicksort_aleatorio fueron
los que tomaron mas tiempo en ordenar el algoritmo pues los pivotes solo pueden ser 0 o 1 y se comparan
con ellos mismos, como explicamos anteriormente"""
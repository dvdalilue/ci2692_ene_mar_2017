"""
# Descripcion: Modulo con la implementacion de algoritmos de ordenamientos
#              que son aplicados sobre listas de elementos de tipo numerico
# Autor: Aurivan Castro, Sandra Vera
# email: 14-10205@usb.ve, 14-11130@usb.ve
"""
from arrayT import ArrayT
from random import randint
from heap_functions import heap_sort
from quicksort import quicksort_basico,quicksort_aleatorio

def merge_sort(lista):
#    """
#    Ordenamiento por medio del algoritmo de Merge Sort
#
#    Parametros:
#        a: Un arreglo a ordenar
#        p: Primer indice del arreglo
#        r: Ultimo indice del arreglo
#    Efecto Secundario:
#        El arreglo de entrada es ordenado en orden ascendente
#    """
    
    #Copia de z
   
    k = 1
    n = len(lista)
    h = ArrayT(n)
    for i in range(n):
        h[i] = lista[i]

    while k < n:
        a,b,c = 0,k,min([(2*k),n])
        while b < n:
            p,q,r = a,b,a
            while p!=b and q!=c:
                if h[p] <= h[q]:
                    lista[r] = h[p]
                    r += 1
                    p += 1
                else:
                    lista[r] = h[q]
                    r += 1
                    q += 1
            while p != b:
                lista[r] = h[p]
                r += 1
                p += 1
            while q!= c:
                lista[r] = h[q]
                r += 1
                q += 1
            r = a
            while r != c:
                h[r] = lista[r]
                r += 1
            a,b,c = a+2*k, b+2*k, min([(c+2*k),n])
        k = k*2
    return lista

"""#Prueba
y=ArrayT(10)
for i in range(len(y)):
    y[i]=randint(0,30)
    print(y[i])  #imprime el tamano del arreglo sin ordernar

y=quicksort_aleatorio(y)

print("arreglo ordenado")
for i in range(len(y)):
    print(y[i])"""
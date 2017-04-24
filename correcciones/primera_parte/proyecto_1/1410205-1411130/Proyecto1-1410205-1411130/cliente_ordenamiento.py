#!/usr/bin/env python3

"""
Cliente para la comparacion de algoritmos de ordenamiento
por medio de listas de enteros con valores aleatorios

Autor: Guillermo Palma
Email: gvpalma@usb.ve
Version: 0.1 - Enero 2017
"""

import sys, random, time, ordenamiento, argparse, numpy, inspect, matplotlib.pyplot
from arrayT import ArrayT
import resource

sys.setrecursionlimit(1000000000) #Limite recursivo cambiado de 1000 a 1000000000
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))


#######################
#
# Varibles Globles
#
#######################

N=200     # Numero de elementos del arreglo por defecto.
M=500     # Maximo numero de elementos aleatorios a generar.

#################################################
#
# Ejecucion de los algoritmos de ordenamiento
#
#################################################

def parse_args():
    """
    Manejo de los parametros de entrada. Para una explicacion 
    de como llamar a la aplicacion, ejecute:

    >>./cliente_ordenamiento.py -h
    """
    parser = argparse.ArgumentParser(description="Comparison of sorting algorithms.")
    parser.add_argument("n_elems", type=int, default=[N], nargs="*",
                        help="a list with the number of integers to order. Default "+str(N))
    parser.add_argument("-g", "--graphic", help="draw a plot with algorithm results",
                        action="store_true")
    parser.add_argument("-t", "--ntry",  metavar="NT",  type=int, default=1,
                    help="number of tries for each set of elements")
    parser.add_argument("-p","--prueba", type=int,default=1, help="1:Array with random integers.\
		2:Array with descending integers. 3:Array with random zeros and ones.	4:Array with ordered intergers.\
		5:Array with random real numbers. 6:Array with integers in the sequence 1,2,...,N/2,N/2,...,2,1.	\
		7:Array with almost all its elements ordered.")
    args = parser.parse_args()
    if args.ntry <= 0:
        print("Error, el numero de pruebas debe ser mayor que cero\n")
        parser.print_help()
        sys.exit(1)
    return ( (sorted(args.n_elems), args.graphic, args.ntry, args.prueba) )

def obtener_arreglo_enteros(n):
    """
    Crea arreglo con n valores enteros que son generados de forma aleatoria.
    
    Parametros:
        n: Numero de elementos del arreglo.
    
    Retorna:
        Un objeto lista con n valores enteros aleatorios.
     """
    arrg = ArrayT(n)
    for i in range(n):
        arrg[i] = random.randint(0, M)
    return arrg

def obtener_arreglo_ceros_unos(n):
    """
    Crea arreglo con n elementos iguales a 0 o a 1 que son generados de forma aleatoria.
    
    Parametros:
        n: Numero de elementos del arreglo.
    
    Retorna:
        Un objeto lista con n elementos iguales a 0 o a 1 generados de forma aleatoria.
     """
    arrg = ArrayT(n)
    for i in range(n):
        arrg[i] = random.randint(0, 1)
    return arrg

def obtener_arreglo_descendente(n):
    """
    Crea arreglo con n enteros en orden descendente.
    
    Parametros:
        n: Numero de elementos del arreglo.
    
    Retorna:
        Un objeto lista con n elementos colocados de manera descendente.
     """
    arrg = ArrayT(n)
    for i in range(n):
        arrg[i] = n-i
    return arrg

def obtener_arreglo_ascendente(n):
	"""
    Crea arreglo con n enteros en orden ascendente.
    
    Parametros:
        n: Numero de elementos del arreglo.
    
    Retorna:
        Un objeto lista con n elementos colocados de manera ascendente.
     """
	arrg = ArrayT(n)
	for i in range(n):
		arrg[i] = i+1
	return arrg

def obtener_arreglo_reales(n):
	"""
    Crea arreglo con n reales aleatorios comprendidos en el intervalo [0,1).
    
    Parametros:
        n: Numero de elementos del arreglo.
    
    Retorna:
        Un objeto lista con n elementos reales en el intervalo [0,1).
     """
	arrg = ArrayT(n)
	for i in range(n):
		arrg[i] = random.uniform(0, 1)
	return arrg

def obtener_arreglo_mitad(n):
	"""
    Crea arreglo con n enteros como una secuencia de la forma 1,2,...n/2,n/2,...,2,1.
    
    Parametros:
        n: Numero de elementos del arreglo.
    
    Retorna:
        Un objeto lista con n elementos en una secuencia de la forma 1,2,...n/2,n/2,...,2,1.
     """
	#Si el arreglo es de taman~o par, crea un arreglo de n elementos. De lo contrario, crea un arreglo
	#de n-1 elementos.
	if n%2!=0:
		n=n-1
	arrg = ArrayT(n)
	for i in range(1,(n/2)+1):
		arrg[i-1]=i
	for i in range(0,n/2):
		arrg[(n/2)+i]=(n/2)-i
	return arrg
	
def obtener_arreglo_casi_ordenado(n):
	"""
    Crea arreglo con n enteros en orden ascendente casi ordenado.
    
    Parametros:
        n: Numero de elementos del arreglo.
    
    Retorna:
        Un objeto lista con n elementos colocados de manera ascendente con
        n/4 pares separados 4 lugares entre si que se escogen al azar y se 
        intercambian.
	"""
	arrg = obtener_arreglo_ascendente(n)
	if n-4>0:
		arregloaux=ArrayT(n//4)
		for i in range(n//4):
			p=random.randint(0,n-4)
			while p in arregloaux:
				p=random.randint(0,n-4)
			arregloaux[i]=p
		for i in arregloaux:
			arrg=swap(arrg,i,i+4)
	return arrg	

def esta_ordenado_arreglo(a):
    """
    Comprueba si un arreglo esta ordenado.

    Parametros:
        a: Un arreglo de elementos de tipo numerico
    
    Retorna: 
        True si el arreglo esta ordenado, False en caso contrario.
    """
    n = len(a)
    i = 0
    while(i < n-1):
        if a[i] > a[i+1]:
            return False
        i += 1
    return True

def copia_arreglo(a_orig):
    """
    Crea una nueva copia de un arreglo.
    
    Parametros:
        a_orig: Un arreglo a copiar.
    
    Retorna: 
        Un nuevo arreglo copia del arreglo de entrada.
    """
    n = len(a_orig)
    a_copia = ArrayT(n)
    for i in range(n):
        a_copia[i] = a_orig[i]
    return a_copia

def cargar_algoritmos_de_modulos():
    """
    Carga las funciones que corresponden a los algoritmos
    de ordenamiento que se encuentran en el modulo <<ordenamiento>>
    
    Retorna:
        Una lista con las funciones del modulo ordenamiento
    """
    array= ['merge_sort', 'heap_sort_final','quicksort_aleatorio',
            'quicksort_dual_pivot_final', 'Median_of_3_Quicksort_Final',
            'Introsort', 'quicksort_with_three_way_partition', 
            'quicksort_dual_pivot_final']
    functions_list = [o for o in inspect.getmembers(ordenamiento)
                      if inspect.isfunction(o[1]) and (o[0] in array)==True]
    return functions_list

def ordenar_arreglo(nombre, algoritmo, datos, ntry):
    """
    Ordena los elementos de un arreglo usando un algoritmo de ordenamiento

    Paramentros:
        nombre: Nombre del algoritmo a aplicar.
        algoritmo: Referncia a la funcion que corresponde al algoritmo de ordenamiento.
        datos: Arreglo a ordenar.
        ntry: Numero del intento a ejecutar.

    Retorna:
        El tiempo empleado por el algoritmo para ordenar el arreglo.
    """
    print("\nProcedimiento "+nombre+". Num. de elementos: "+str(len(datos))+" Intento: "+str(ntry+1))
    a_resultado = copia_arreglo(datos)
    start_time = time.time()
    algoritmo(a_resultado)
    t_usado = time.time() - start_time
    if not esta_ordenado_arreglo(a_resultado):
        print("Error, el arreglo no esta ordenado")
        sys.exit(1)
    print("Tiempo de "+nombre+" {0:.3f} segs".format(t_usado))
    return t_usado

def resultados_algoritmos(n_elems, algs, n_pruebas,prueba):
    """
    Ejecuta varias veces un conjunto de algoritmos, sobre una serie de arreglos
    generados de forma aleatoria

    Paramentros:
        n_elems: Lista con los tama~nos de los arreglos a generar
        algs: Lista con los algoritmos a ejecutar
        n_pruebas: Numero de veces que se va a ejecutar un algoritmos sobre un arreglo

    Retorna:
        Una matriz con los tiempos promedios empleados por cada algoritmo, 
        para cada tama~no de arreglo a ejecutar. 
    """
    resultados = [ [0.0 for x in range(len(n_elems))] for y in range(len(algs)) ]
    i = 0
    for n in n_elems:
        if prueba==1:
            arrg = obtener_arreglo_enteros(n)
        elif prueba==2:
            arrg = obtener_arreglo_descendente(n)
        elif prueba==3:
            arrg = obtener_arreglo_ceros_unos(n)
        elif prueba==4:
            arrg = obtener_arreglo_ascendente(n)
        elif prueba==5:
            arrg = obtener_arreglo_reales(n)
        elif prueba==6:
            arrg = obtener_arreglo_mitad(n)
        elif prueba==7:
            arrg = obtener_arreglo_casi_ordenado(n)
        j = 0
        for (nombre, proc) in algs:
            promedio = numpy.mean([ ordenar_arreglo(nombre, proc, arrg, nt)
                                    for nt in range(n_pruebas)])
            print("\n**************************************************")
            print("Tiempo promedio de "+nombre+": {0:.3f} segs".format(promedio))
            print("***************************************************")
            resultados[j][i] = promedio
            j += 1
        i += 1
    return resultados

#################################################
#
# Generacion de los graficos de los resultados
#
#################################################

def mejor_ajuste(x, y):
    """
    Encuentra la curva que mejor se ajusta a una serie de puntos

    Parametros:
        x: Valor en el eje x de un conjunto de puntos
        y: Valor en el eje y de un conjunto de puntos
    
    Retorna:
        Los puntos correspondientes a la curva que es el mejor ajuste
    """
    fit = numpy.polyfit(x,y,2)
    fit_fn = numpy.poly1d(fit)
    x_new = numpy.linspace(x[0], x[-1], 50)
    y_new = fit_fn(x_new)
    return (x_new, y_new)

def dibujar_puntos(x, y, color, marca, nombre):
    """
    Agrega una serie de puntos al plano a dibujar.

    Parametros:
        x: Valores en el eje x de los puntos a dibujar. 
        y: Valores en el eje x de los puntos a dibujar. 
        color: Color a usar con los puntos.
        marca: Tipo de marca que van a tener los puntos.
        nombre: Identificacion de los puntos.

    Efecto Secundario:
        Agrega una serie de puntos al plano actual.
    """
    x_new, y_new = mejor_ajuste(x, y)
    matplotlib.pyplot.plot(x_new, y_new, color)
    matplotlib.pyplot.plot(x, y, color+marca, label=nombre)

def mostrar_grafico():
    """
    Muestra un panel con los puntos y curvas agregadas.

    Efecto Secundario:
        Muestra un panel con las curvas y puntos dibujados.
    """
    matplotlib.pyplot.xlabel("Num. de elementos")
    matplotlib.pyplot.ylabel("Tiempo (seg)")
    matplotlib.pyplot.legend(loc=2)
    matplotlib.pyplot.legend(bbox_to_anchor=(0.05, 0.95), loc=2, borderaxespad=0.0)
    matplotlib.pyplot.grid(True)
    matplotlib.pyplot.show(block=False)
    matplotlib.pyplot.pause(2)
    input("Presione cualquier tecla para terminar")
     
def graficar_resultados(algoritmos, datos, resultados):
    """ 
    Grafica los tiempos obtenidos por los algoritmos de ordenamiento
    para cada uno de los arreglos de diferente tama~nos.

    Parametros:
        algoritmos: Nombres de los algoritmos ejecutados.
        datos: Lista con los tama~nos de los conjuntos de datos ordenados.
        resultados: Matriz con los tiempos promedios de los algoritmos, en 
                    cada conjunto de datos. 

    Efecto Secundario:
        Muestra un panel con las puntos y curvas de los resultados de los algoritmos. 
    """
    colores = ["b", "g", "r", "c", "m", "y", "k"]
    marcas = ["o", "*", "+", "v", "^", ">", "<"]
    assert( len(colores) == len(marcas) )
    n = len(algoritmos)
    if n > len(colores):
        print("Error, el numero de algoritmos es mayor que el numero de colores disponibles")
        print("Numero de colores disponibles: "+str(len(colores)))
        sys.exit(1)
    for i in range(n):
        assert( len(datos) == len(resultados[i]) )
        dibujar_puntos(datos, resultados[i], colores[i], marcas[i], algoritmos[i])
    mostrar_grafico()
    
################################
##
## Inicio de la aplicacion
##
################################

if __name__ == "__main__":
    (n_elems, g, n_pruebas, prueba) = parse_args()
    algoritmos = cargar_algoritmos_de_modulos()
    rs = resultados_algoritmos(n_elems, algoritmos, n_pruebas, prueba)
    nombre_algoritmos = [ nombre for (nombre, proc) in algoritmos ]
    if g:
        graficar_resultados(nombre_algoritmos, n_elems, rs)
   

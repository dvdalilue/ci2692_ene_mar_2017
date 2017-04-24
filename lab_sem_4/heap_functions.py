from arrayT import ArrayT

def heapify(array, i, lenght):
    left_son = left(i)
    right_son = right(i)
    largest = i

    if left_son < lenght and array[i] < array[left_son]:
        largest = left_son

    if right_son < lenght and array[largest] < array[right_son]:
        largest = right_son

    if (largest != i):
        swap(array, largest, i)
        heapify(array, largest, lenght)

def build_max_heap(array):
    bound = len(array) // 2
    while bound >= 0:
        heapify(array, bound, len(array))
        bound -= 1

def dequeue(array):
    assert len(array) > 1, "No se puede pasar un arreglo de tamaña menor a 2."
    aux_array = ArrayT(len(array)-1)
    i = 1
    while i < len(array):
        aux_array[i-1] = array[i]
        i += 1
    heapify(aux_array,0,len(aux_array))
    return((array[0],aux_array))

def heapsort(array):
    build_max_heap(array)
    lenght = len(array)
    while lenght != 0:
        lenght -= 1
        swap(array,0,lenght)
        heapify(array,0,lenght)

def swap(array, i, j):
    array[i],array[j] = array[j],array[i]

def parent(i):
    return (i + 1) // 2 - 1

def left(i):
    return (2*(i+1)-1)

def right(i):
    return (2*(i+1))
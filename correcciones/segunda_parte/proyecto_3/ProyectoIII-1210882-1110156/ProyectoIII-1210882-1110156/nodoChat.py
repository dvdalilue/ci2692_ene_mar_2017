class Nodo:
    def __init__(self, e, n):
        self.element = e
        self.next = n

    def __str__(self):
        string = "["
        aux = self
        while not aux == None:
            string += "{0},".format(aux.element)
            aux = aux.next
        string = string[:-1] + "]" 
        return string

    def __repr__(self):
        return self.__str__()

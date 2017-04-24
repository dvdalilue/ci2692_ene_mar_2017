from nodo import Nodo

class Pila(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def push(self,e):
        self.head = Nodo(e,self.head)
        self.count += 1

    def pop(self):
        if not self.is_empty():
            self.count -= 1
            ret = self.head.element
            self.head = self.head.next
            return ret
        return None

    def top(self):
        if not self.is_empty():
            return self.head.element
        return None

    def size(self):
        return self.count
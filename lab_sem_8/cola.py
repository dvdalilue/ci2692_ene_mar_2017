from nodo import Nodo

class Cola(object):
    def __init__(self):
        self.head = None
        self.last = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def enqueue(self, e):
        new_node = Nodo(e,None)
        if self.is_empty():
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.count += 1

    def dequeue(self):
        if not self.is_empty():
            self.count -= 1
            ret = self.head.element
            self.head = self.head.next
            return ret
        return None

    def first(self):
        if not self.is_empty():
            return self.head.element
        return None

    def size(self):
        return self.count
class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class pila:
    def __init__(self):
        self.size = 0
        self.head = None

    def isEmpty(self):
        return self.size == 0

    def push(self, item):
        item = node(item)

        if self.head == None:
            self.head = item
        else:
            item.next = self.head
            self.head = item

        self.size = self.size + 1

    def pop(self):
        if not self.isEmpty():
            item = self.head
            self.head = self.head.next
            self.size = self.size - 1

            return item
        
        return None

class Chat:
    def __init__(self, usuario1, usuario2):

        if usuario1.nombre  < usuario2.nombre:
            self.id = usuario1.nombre + "-" + usuario2.nombre
        else:
            self.id = usuario2.nombre + "-" + usuario1.nombre

        self.mensajes = pila()

    def agregarMensaje(self, usuario1, mensaje):
        self.mensajes.push(usuario1.nombre+": "+mensaje)
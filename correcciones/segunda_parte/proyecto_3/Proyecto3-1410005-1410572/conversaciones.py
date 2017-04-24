from hash_table import hashTable

class Conversaciones:
    def __init__(self, n):
        self.n = 0
        self.tablaC = hashTable(n)
    
    def agregarConversacion(self, chat):
        return self.tablaC.addValue(chat.id, chat)

    def buscarConversacion(self, idd):
        return self.tablaC.search(idd)

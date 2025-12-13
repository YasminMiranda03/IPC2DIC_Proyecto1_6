from Nodo import Nodo

class ColaPrioridad:
    def __init__(self):
        self.primero = None
        self.size = 0
        
    def esta_vacia(self):
        return self.primero is None
    
    def enqueue(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            actual= self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            #enlazo el nuevo al fin
            actual.siguiente = nuevo_nodo
        self.size += 1
        
    def dequeue(self):
        if self.esta_vacia():
            print("prueba")
            return None
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self.size -= 1
        print("aqui ya se atendio la soli")
        return dato
    
    def peek(self):
        if self.esta_vacia():
            return None
        return self.primero.dato
    
    def mostrar(self):
        if self.esta_vacia():
            print("La cola esta vacia")
            return
        print("cola de prioridad:")
        
        actual =self.primero
        posicion = 1
        while actual is not None:
            actual.dato.mostrar_info()
            actual = actual.siguiente
    
    def obtener_tamanio(self):
        return self.size
            
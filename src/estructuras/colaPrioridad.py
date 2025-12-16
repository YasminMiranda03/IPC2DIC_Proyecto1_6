from estructuras.ListaSimple import ListaSimple
from estructuras.Nodo import Nodo


class ColaPrioridad:
    def __init__(self):
        self.primero = None
        self.size = 0
        
    def esta_vacia(self):
        return self.primero is None
    
    def enqueue(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo
            self.size += 1
            return
        if nuevo.dato.prioridad > self.primero.dato.prioridad:
            nuevo.siguiente = self.primero
            self.primero = nuevo
            self.size += 1
            return
    
        actual = self.primero
        while actual.siguiente is not None and actual.siguiente.dato.prioridad >= nuevo.dato.prioridad:
            actual = actual.siguiente
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo
        self.size += 1
        
    def dequeue(self):
        if self.esta_vacia():
            return None
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self.size -= 1
        return dato
    
    def peek(self):
        if self.esta_vacia():
            return None
        return self.primero.dato
        
    def obtener_tamanio(self):
        return self.size
    
    def obtener_lista(self):
        lista = ListaSimple()
        actual = self.primero
        while actual is not None:
            lista.agregar(actual.dato)
            actual = actual.siguiente
        return lista
    
    def mostrar(self):
        if self.esta_vacia():
            print("La cola esta vacia")
            return
        print("cola de prioridad:")
        
        actual =self.primero
        while actual is not None:
            actual.dato.mostrar_info()
            actual = actual.siguiente
    
    def registrar_lista(self):
        lista = ListaSimple()
        actual = self.primero
        while actual is not None:
            lista.agregar(actual.dato)
            actual = actual.siguiente
        return lista

from estructuras.Nodo import Nodo
class ListaDoble:
    def __init__(self):                 
        self.cabeza = None 
        self.cola = None
    
    def agregar(self, dato): 
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:     #verifica si la lista esta vacia
            self.cabeza = nuevo_nodo 
            self.cola = nuevo_nodo
        else: 
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
    
    def buscar(self, id):   #busca un nodo por id           
        actual = self.cabeza
        while actual:
            if actual.id == id:
                return True
            actual = actual.siguiente
    
    def eliminar(self, id):  #elimina un nodo por id
        actual = self.cabeza
        while actual:
            if actual.id == id:
                if actual.anterior:    
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False
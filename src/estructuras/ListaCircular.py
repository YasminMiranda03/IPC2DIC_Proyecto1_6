from estructuras.Nodo import Nodo
class ListaCircular: 
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:     #verifica si la lista esta vacia
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo  #apunta a si mismo
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:  #recorre hasta el ultimo nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza  #cierra el ciclo
            
    def buscar(self, id):   #busca un nodo por id
        if not self.cabeza:
            return False
        actual = self.cabeza
        while True:
            if actual.id == id:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False
    
    def eliminar(self, id):  #elimina un nodo por id
        if not self.cabeza:
            return False
        actual = self.cabeza
        anterior = None
        while True:
            if actual.id == id:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    #eliminar la cabeza
                    if actual.siguiente == self.cabeza:  #solo un nodo
                        self.cabeza = None
                    else:
                        #buscar el ultimo nodo para actualizar su siguiente
                        ultimo = self.cabeza
                        while ultimo.siguiente != self.cabeza:
                            ultimo = ultimo.siguiente
                        self.cabeza = actual.siguiente
                        ultimo.siguiente = self.cabeza
                return True
            anterior = actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False
    
    #pendiente 
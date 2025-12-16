from estructuras.Nodo import Nodo       
class ListaSimple:
    def __init__(self): 
        self.cabeza = None 
    
    def agregar(self, dato): 
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:     #verifica si la lista esta vacia
            self.cabeza = nuevo_nodo 
        else: 
            actual = self.cabeza 
            while actual.siguiente:     #recorre la lista hasta encontrar el ultimo nodo
                actual = actual.siguiente 
            actual.siguiente = nuevo_nodo
    
    
    def insertar(self, dato):
        self.agregar(dato)

    def esta_vacia(self):
        return self.cabeza is None
        
    def buscar(self, id):   #busca un nodo por id
        actual = self.cabeza
        while actual:
            if actual.id == id:
                return True
            actual = actual.siguiente 
    
    def eliminar(self, id):  #elimina un nodo por id
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.id == id:
                if anterior:    
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False
    
    def recorrer(self):   #recorre la lista y devuelve una lista con los datos
        actual = self.cabeza
        while actual:
            #imprimo uno tras otro
            yield actual.dato
            actual = actual.siguiente
    #------------------------------------------------------------------------------------------------------
    
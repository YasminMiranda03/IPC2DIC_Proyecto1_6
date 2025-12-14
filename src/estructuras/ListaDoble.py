from estructuras.Nodo import Nodo
class ListaDoble:
    def __init__(self):                 
        self.primero = None 
        self.ultimo = None
    
    def agregar(self, dato): 
        nuevo_nodo = Nodo(dato)
        if not self.primero:     #verifica si la lista esta vacia
            self.primero = nuevo_nodo 
            self.ultimo = nuevo_nodo
        else: 
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo
    
    def buscar(self, id):   #busca un nodo por id           
        actual = self.primero
        while actual:
            if actual.id == id:
                return True
            actual = actual.siguiente
    
    def eliminar(self, id):  #elimina un nodo por id
        actual = self.primero
        while actual:
            if actual.id == id:
                if actual.anterior:    
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimo = actual.anterior
                return True
            actual = actual.siguiente
        return False
    
    #------------------------------------------------------------------------------------------------------
    def vacia(self):
        return self.primero == None
    
    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.size += 1
    
    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = None
            self.primero = aux
        self.size += 1
        
    def recorrer_inicio(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente
            
    def recorrer_final(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
    
    def obtener_size(self):
        return self.size
    
    def eliminar_inicio(self):
        if  self.vacia():
            print("La lista esta vacia")
            return
        elif self.primero.siguiente == None:        #comprueba si apunta a none
            self.primero = self.ultimo = None
            self.size = 0
        else:                                       #en caso hayan mas de dos valores
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1
            
    def eliminar_final(self):
        if self.vacia():
            print("La lista esta vacia")
            return
        elif self.primero.siguiente == None:        #comprueba si apunta a none
            self.primero = self.ultimo = None
            self.size = 0
        else:                                       #en caso hayan mas de dos valores
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1
    #------------------------------------------------------------------------------------------------------
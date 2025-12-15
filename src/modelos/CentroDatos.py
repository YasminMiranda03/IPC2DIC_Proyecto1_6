from estructuras.ListaSimple import ListaSinple
class CentroDatos:
    
    def __init__(self, id_centro, nombre, pais, ciudad, cpu, ram, almacenamiento):
        #constructor
        
        self.id = id
        self.nombre = nombre
        self.pais = pais
        self.ciudad = ciudad
        self.cpu_total = cpu
        self.ram_total = ram
        self.almacenamiento_total = almacenamiento
        
        self.cpu_disponible = cpu
        self.ram_disponible = ram
        self.almacenamiento_disponible = almacenamiento
        
        self.vms = ListaSimple()  
    
    def mostrar_info(self):
        print(f"\nId del centro de datos: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Pais: {self.pais}")
        print(f"Ciudad: {self.ciudad}") 
        print(f"Capacidad cpu: {self.cpu_total}, ram: {self.ram_total}, almacenamiento: {self.almacenamiento_total}")
        
    def __str__(self):
        return f"Centro[{self.id}]-{self.nombre}({self.ciudad})"
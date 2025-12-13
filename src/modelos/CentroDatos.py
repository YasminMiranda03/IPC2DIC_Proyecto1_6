class CentroDatos:
    
    def __init__(self, id_centro, nombre, pais, ciudad, cpu, ram, almacenamiento):
        #constructor
        
        self.id_centro = id_centro
        self.nombre = nombre
        self.pais = pais
        self.ciudad = ciudad
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento
    
    def mostrar_info(self):
        print(f"\nId del centro de datos: {self.id_centro}")
        print(f"Nombre: {self.nombre}")
        print(f"Pais: {self.pais}")
        print(f"Ciudad: {self.ciudad}") 
        print(f"Capacidad cpu: {self.cpu}, ram: {self.ram}, almacenamiento: {self.almacenamiento}")
        
    def __str__(self):
        return f"Centro[{self.id_centro}]-{self.nombre}({self.ciudad})"
from estructuras.ListaDoble import ListaDoble

class MaquinaVirtual:
    def __init__(self, id, centroAsignado, so, cpu, ram, almacenamiento, ip):
        self.id = id
        self.centroAsignado = centroAsignado
        self.so = so
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.ip = ip
        self.cpu_us = 0
        self.ram_us = 0
        self.contenedores = ListaDoble()
# Contenedores dentro de esta VM
    
    def tiene_recursos(self, cpu, ram):
        return (self.cpu_us + cpu <= self.cpu and self.ram_us + ram <= self.ram)
    
    def agregar_contenedor(self, contenedor):
        self.contenedores.insertar(contenedor)
        self.cpu_us += contenedor.cpu
        self.ram_us += contenedor.ram
    
    def recorrer(self):
        return self.contenedores.recorrer()
    
    def eliminar_contenedor(self, contenedor):
        self.cpu_us -= contenedor.cpu
        self.ram_us -= contenedor.ram
    

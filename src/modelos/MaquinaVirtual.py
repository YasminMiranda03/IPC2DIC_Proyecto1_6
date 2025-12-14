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

        # Contenedores dentro de esta VM
        self.contenedores = ListaDoble()
    
    def agregar_contenedor(self, contenedor):
        self.contenedores.insertar(contenedor)
    
    def recorrer(self):
        return self.contenedores.recorrer()
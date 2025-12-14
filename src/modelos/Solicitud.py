class Solicitud:
    def __init__(self, id, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo):
        self.id = id
        self.cliente = cliente
        self.tipo = tipo      # Deploy | Backup
        self.prioridad = prioridad
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.tiempo = tiempo

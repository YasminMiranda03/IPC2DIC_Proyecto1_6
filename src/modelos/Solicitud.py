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

    def __str__(self):
        return f"Solicitud[{self.id}] - Cliente: {self.cliente}, Tipo: {self.tipo}, Prioridad: {self.prioridad}, CPU: {self.cpu}, RAM: {self.ram}, Almacenamiento: {self.almacenamiento}, Tiempo: {self.tiempo}"
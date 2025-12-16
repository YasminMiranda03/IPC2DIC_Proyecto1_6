from estructuras.colaPrioridad import ColaPrioridad
from modelos.Solicitud import Solicitud

class SolicitudesController:
    def __init__(self):
        self.cola = ColaPrioridad()

    def agregar_solicitud(self, id_solicitud, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo_estimado):
        solicitud = Solicitud(id_solicitud, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo_estimado)
        self.cola.enqueue(solicitud) 
        return True, "Solicitud agregada"

    def procesar_n_solicitudes(self, n):
        procesadas = 0
        while n > 0 and not self.cola.esta_vacia():
            solicitud = self.cola.dequeue()  # Dequeuing la solicitud
            print("Procesando:", solicitud.id, "Prioridad:", solicitud.prioridad)
            n -= 1
            procesadas += 1
        if procesadas > 0:
            return True, f"{procesadas} solicitudes procesadas."
        return False, "No hay solicitudes para procesar."
from estructuras.colaPrioridad import ColaPrioridad
from modelos.Solicitud import Solicitud
 
class SolicitudesController:
    def __init__(self):
        self.cola = ColaPrioridad()

    def agregar_solicitud(self, id_solicitud, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo_estimado):
        solicitud = Solicitud(id_solicitud, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo_estimado)
        self.cola.enqueue(solicitud)
        return True, "Solicitud agregada"

    def procesar_mayor_prioridad(self):
        return self.procesar_n_solicitudes(1)

    def procesar_n_solicitudes(self, n):
        procesadas = 0
        while n > 0 and not self.cola.esta_vacia():
            solicitud = self.cola.dequeue()
            print(f"Procesando: {solicitud.id} ,Prioridad: {solicitud.prioridad} , Tipo: {solicitud.tipo}")
            n -= 1
            procesadas += 1

        if procesadas > 0:
            return True, f"{procesadas} solicitudes procesadas."
        return False, "No hay solicitudes para procesar."

    def ver_cola(self):
        if self.cola.esta_vacia():
            print("La cola está vacía.")
            return
        print("\nSolicitudes")
        lista = self.cola.obtener_lista()  
        actual = lista.cabeza
        contador = 1
        while actual is not None:
            ndato = actual.dato
            print(f"{contador}. ID: {ndato.id} , Cliente: {ndato.cliente} , Tipo: {ndato.tipo} , Prioridad: {ndato.prioridad}")
            print(f"   Recursos: CPU={ndato.cpu}, RAM={ndato.ram}, DISK={ndato.almacenamiento} , Tiempo: {ndato.tiempo}")
            actual = actual.siguiente
            contador += 1
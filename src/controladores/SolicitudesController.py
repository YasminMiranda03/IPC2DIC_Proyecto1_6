from estructuras.ListaSimple import ListaSimple
from modelos.Solicitud import Solicitud

class SolicitudesController:
    def __init__(self):
        self.cola_alta = ListaSimple()
        self.cola_media = ListaSimple()
        self.cola_baja = ListaSimple()

    def agregar_solicitud(self, id, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo):
        solicitud = Solicitud(
            id, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo
        )

        if prioridad == 1:
            self.cola_alta.agregar(solicitud)
        elif prioridad == 2:
            self.cola_media.agregar(solicitud)
        else:
            self.cola_baja.agregar(solicitud)

        return True, f"Solicitud {id} agregada correctamente"

    def procesar_siguiente(self):
        if not self.cola_alta.esta_vacia():
            return self.cola_alta.eliminar_primero()
        if not self.cola_media.esta_vacia():
            return self.cola_media.eliminar_primero()
        if not self.cola_baja.esta_vacia():
            return self.cola_baja.eliminar_primero()
        return None

    def procesar_n_solicitudes(self, cantidad):
        procesadas = 0

        for _ in range(cantidad):
            solicitud = self.procesar_siguiente()
            if solicitud is None:
                break
            print(f"Procesando -> {solicitud}")
            procesadas += 1

        return True, f"{procesadas} solicitudes procesadas"

    def listar_solicitudes(self):
        print("\n--- SOLICITUDES PRIORIDAD ALTA ---")
        for s in self.cola_alta.recorrer():
            print(s)

        print("\n--- SOLICITUDES PRIORIDAD MEDIA ---")
        for s in self.cola_media.recorrer():
            print(s)

        print("\n--- SOLICITUDES PRIORIDAD BAJA ---")
        for s in self.cola_baja.recorrer():
            print(s)

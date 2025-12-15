from modelos.CentroDatos import CentroDatos
from estructuras.ListaSimple import ListaSimple

class CentroDatosController:
    def __init__(self):
        self.centros = ListaSimple()

    def crear_centro(self, id_centro, nombre, pais, ciudad, cpu, ram, almacenamiento):
        if self.buscar_centro(id_centro):
            return False, "El centro de datos ya existe"

        centro = CentroDatos(
            id_centro, nombre, pais, ciudad, cpu, ram, almacenamiento
        )
        self.centros.insertar(centro)
        return True, "Centro de datos creado correctamente"

    def buscar_centro(self, id_centro):
        for centro in self.centros.recorrer():
            if centro.id == id_centro:
                return centro
        return None

    def listar_centros(self):
        if self.centros.esta_vacia():
            print("No hay centros de datos registrados")
            return

        print("\n=== Centros de Datos ===")
        for centro in self.centros.recorrer():
            print("-" * 40)
            print(f"ID: {centro.id}")
            print(f"Nombre: {centro.nombre}")
            print(f"Ubicación: {centro.pais}, {centro.ciudad}")
            print(f"CPU disponible: {centro.cpu_disponible}/{centro.cpu_total}")
            print(f"RAM disponible: {centro.ram_disponible}/{centro.ram_total}")
            print(f"Almacenamiento disponible: {centro.almacenamiento_disponible}")

    def eliminar_centro(self, id_centro):
        actual = self.centros.cabeza
        anterior = None

        while actual:
            if actual.data.id == id_centro:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.centros.cabeza = actual.siguiente
                return True, "Centro eliminado correctamente"

            anterior = actual
            actual = actual.siguiente

        return False, "Centro de datos no encontrado"

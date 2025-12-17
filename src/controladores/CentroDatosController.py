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
        self.centros.agregar(centro)
        return True, "Centro de datos creado correctamente"

    def buscar_centro(self, id_centro):
        for centro in self.centros.recorrer():
            if centro.id_centro == id_centro:
                return centro
        return None

    def listar_centros(self):
        if self.centros.cabeza is None:
            print("No hay centros de datos registrados")
            return

        print("\n=== Centros de Datos ===")
        for centro in self.centros.recorrer():
            print("-" * 40)
            print(f"ID: {centro.id_centro}")
            print(f"Nombre: {centro.nombre}")
            print(f"Ubicación: {centro.pais}, {centro.ciudad}")
            print(f"CPU disponible: {centro.cpu_disponible}/{centro.cpu_total}")
            print(f"RAM disponible: {centro.ram_disponible}/{centro.ram_total}")
            print(f"Almacenamiento disponible: {centro.almacenamiento_disponible}/{centro.almacenamiento_total}")

    def centro_mayor_recursos(self):
        if self.centros.esta_vacia():
            return None

        mayor = None

        for centro in self.centros.recorrer():
            if mayor is None:
                mayor = centro
            else:
                if centro.cpu_total > mayor.cpu_total:
                    mayor = centro
                elif centro.cpu_total == mayor.cpu_total:
                    if centro.ram_total > mayor.ram_total:
                        mayor = centro

        return mayor
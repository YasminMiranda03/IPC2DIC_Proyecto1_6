from modelos.MaquinaVirtual import MaquinaVirtual

class MaquinaVirtualController:
    def __init__(self, controlador_centros):
        self.controlador_centros = controlador_centros

    def crear_vm(self, id_vm, id_centro, so, cpu, ram, almacenamiento, ip):
        centro = self.controlador_centros.buscar_centro(id_centro)
        if not centro:
            return False, "El centro no existe"

       
        if centro.cpu_disponible < cpu or centro.ram_disponible < ram or centro.almacenamiento_disponible < almacenamiento:
            return False, "El centro no tiene recursos suficientes"


        actual = centro.vms.cabeza
        while actual:
            if actual.dato.id == id_vm:
                return False, "La VM ya existe"
            actual = actual.siguiente

        nueva_vm = MaquinaVirtual(id_vm, id_centro, so, cpu, ram, almacenamiento, ip)

        centro.vms.agregar(nueva_vm)

        centro.cpu_disponible -= cpu
        centro.ram_disponible -= ram
        centro.almacenamiento_disponible -= almacenamiento

        return True, f"VM {id_vm} creada en {id_centro}"

    def buscar_vm_por_id(self, id_vm):
        # recorre todos los centros y sus listas de VMs
        for centro in self.controlador_centros.centros.recorrer():
            actual = centro.vms.cabeza
            while actual:
                if actual.dato.id == id_vm:
                    return actual.dato
                actual = actual.siguiente
        return None

    def mostrar_detalle_vm(self, vm):
        print("\n--- DETALLE VM ---")
        print(f"ID: {vm.id}")
        print(f"Centro asignado: {vm.centroAsignado}")
        print(f"SO: {vm.so}")
        print(f"CPU: {vm.cpu}")
        print(f"RAM: {vm.ram}")
        print(f"Almacenamiento: {vm.almacenamiento}")
        print(f"IP: {vm.ip}")

        cont = 0
        nodo = vm.contenedores.primero
        while nodo:
            cont += 1
            nodo = nodo.siguiente
        print(f"Contenedores: {cont}")
        print("-" * 40)

    def listar_vms_por_centro(self, id_centro):
        centro = self.controlador_centros.buscar_centro(id_centro)
        if not centro:
            print("Centro no encontrado")
            return False, "Centro no encontrado"

        if centro.vms.cabeza is None:
            print("No hay máquinas virtuales en este centro.")
            return True, "No hay vms"

        print(f"\n*** Máquinas virtuales en {centro.nombre} ***")
        actual = centro.vms.cabeza
        while actual:
            vm = actual.dato
            print("-" * 40)
            print(f"ID: {vm.id}")
            print(f"SO: {vm.so}")
            print(f"CPU: {vm.cpu}  RAM: {vm.ram}  Almacenamiento: {vm.almacenamiento}")
            print(f"IP: {vm.ip}")
            actual = actual.siguiente

        return True, "Listado completado"

    def migrar_vm(self, id_vm, id_destino):
        vm_encontrada = None
        centro_origen = None

        for centro in self.controlador_centros.centros.recorrer():
            actual = centro.vms.cabeza
            while actual:
                if actual.dato.id == id_vm:
                    vm_encontrada = actual.dato
                    centro_origen = centro
                    break
                actual = actual.siguiente
            if vm_encontrada:
                break

        if not vm_encontrada:
            return False, "La VM no existe"

        centro_destino = self.controlador_centros.buscar_centro(id_destino)
        if not centro_destino:
            return False, "Centro destino no encontrado"

        if (centro_destino.cpu_disponible < vm_encontrada.cpu or
            centro_destino.ram_disponible < vm_encontrada.ram or
            centro_destino.almacenamiento_disponible < vm_encontrada.almacenamiento):
            return False, "El centro destino no tiene recursos suficientes"


        actual = centro_origen.vms.cabeza
        anterior = None
        while actual:
            if actual.dato.id == id_vm:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    centro_origen.vms.cabeza = actual.siguiente
                break
            anterior = actual
            actual = actual.siguiente

        centro_origen.cpu_disponible += vm_encontrada.cpu
        centro_origen.ram_disponible += vm_encontrada.ram
        centro_origen.almacenamiento_disponible += vm_encontrada.almacenamiento
        centro_destino.vms.agregar(vm_encontrada)
        centro_destino.cpu_disponible -= vm_encontrada.cpu
        centro_destino.ram_disponible -= vm_encontrada.ram
        centro_destino.almacenamiento_disponible -= vm_encontrada.almacenamiento

        vm_encontrada.centroAsignado = id_destino

        return True, f"VM {id_vm} migrada a {id_destino}"
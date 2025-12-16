from modelos.Contenedor import Contenedor

class ContenedorController:
    def __init__(self, controlador_vms):
        self.controlador_vms = controlador_vms
        
    def desplegar_contenedor(self, id_vm, id_cont, nombre, imagen, cpu, ram, puerto):
        vm = self.controlador_vms.buscar_vm_por_id(id_vm)
        if not vm:
            return False, "la vm no existe"
        
        if not vm.tiene_recursos(cpu, ram):
            return False, "La vm no tiene recursos"
        
        for cont in vm.contenedores.recorrer():
            if cont.id == id_cont:
                return False, "El contenedor ya existe"
            
        contendor =Contenedor(id_cont, nombre, imagen, cpu, ram, puerto)
        vm.agregar_contenedor(contendor)
        return True, "Contenedor exitoso"
    
    
    def listar_contenedores(self, id_vm):
        vm = self.controlador_vms.buscar_vm_por_id(id_vm)
        if not vm:
            print("La vm no existe")
            return
        si_hay = False
        for cont in vm.contenedores.recorrer():
            si_hay= True
            print("-" *40)
            print(f"id: {cont.id}")
            print(f"Nombre: {cont.nombre}")
            print(f"Imagen: {cont.imagen}")
            print(f"CPU: {cont.cpu}")
            print(f"RAM: {cont.ram}")
            print(f"Estado: {cont.estado}")
            
        if not si_hay:
            print("La vm no tiene contenedores")
            
    def cambiar_estado_contenedor(self, id_vm, id_cont, nuevo_estado):
        vm = self.controlador_vms.buscar_vm_por_id(id_vm)
        if not vm:
            return False, "La VM no existe"

        for cont in vm.contenedores.recorrer():
            if cont.id == id_cont:
                if cont.estado == "Detenido" and nuevo_estado == "Pausado":
                    return False, "No se puede pausar un contenedor detenido"

                cont.estado = nuevo_estado
                return True, f"Estado cambiado a {nuevo_estado}"

        return False, "El contenedor no existe"

    def eliminar_contenedor(self, id_vm, id_cont):
        vm = self.controlador_vms.buscar_vm_por_id(id_vm)
        if not vm:
            return False, "La VM no existe"

        actual = vm.contenedores.head
        anterior = None

        while actual:
            if actual.data.id == id_cont:
                vm.eliminar_contenedor(actual.data)

                if anterior:
                    anterior.next = actual.next
                else:
                    vm.contenedores.head = actual.next

                return True, "Contenedor eliminado correctamente"

            anterior = actual
            actual = actual.next

        return False, "El contenedor no existe"
        
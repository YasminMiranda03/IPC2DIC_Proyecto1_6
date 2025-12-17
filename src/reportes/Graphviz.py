import os


class ReportesGraphviz:
    def __init__(self, controlador_centros, controlador_vms, cola_solicitudes):
        self.controlador_centros = controlador_centros
        self.controlador_vms = controlador_vms
        self.cola_solicitudes = cola_solicitudes

    def _exportar(self, dot_content, nombre_archivo):
        carpeta = "reportes"
        os.makedirs(carpeta, exist_ok=True)

        ruta_dot = os.path.join(carpeta, f"{nombre_archivo}.dot")
        with open(ruta_dot, 'w', encoding='utf-8') as archivo:
            archivo.write(dot_content)

        print(f"\nEl Archivo '{nombre_archivo}.dot' generado exitosamente")
    
    
    def graficar_centros(self, nombre_archivo="reporte_lista_centro"):
        lista = self.controlador_centros.centros

        if lista.cabeza is None:
            print("No se puede graficar una lista vacía")
            return
        
        dot_content = 'digraph ListaSimpleCentros {\n'
        dot_content += '    rankdir=LR;\n'
        dot_content += '    node [shape=record];\n\n'
        
        # Generar nodos
        actual = lista.cabeza
        contador = 0
        
        while actual is not None:
            g_dato = actual.dato
            
            vms = 0
            apuntador = g_dato.vms.cabeza
            while apuntador is not None:
                vms += 1
                apuntador = apuntador.siguiente
            label = (
            f"{g_dato.id_centro}|"
            f"{g_dato.nombre}|"
            f"{g_dato.ciudad}|"
            f"CPU: {g_dato.cpu_disponible}/{g_dato.cpu_total}\\n"
            f"RAM: {g_dato.ram_disponible}/{g_dato.ram_total}\\n"
            f"DISK: {g_dato.almacenamiento_disponible}/{g_dato.almacenamiento_total}\\n"
            f"VMs: {vms}")
            dot_content += f'    nodo{contador} [label="{label}"];\n'
            actual = actual.siguiente
            contador += 1
        
        dot_content += '\n'
        
        # Generar conexiones bidireccionales
        for i in range(contador - 1):
            dot_content += f'    nodo{i} -> nodo{i+1};\n'
        
        dot_content += '}\n'
        
        self._exportar(dot_content, nombre_archivo)
        

    def graficar_vms(self, id_centro, nombre_archivo="reporte_vms"):
        lista = self.controlador_centros.centros
        actual = lista.cabeza
        centro = None
        
        while actual is not None:
            if actual.dato.id_centro == id_centro:
                centro = actual.dato
                break
            actual = actual.siguiente

        if centro is None:
            print(f"No existe el centro {id_centro}")
            return

        lista_vms = centro.vms
        dot = 'digraph VMsCentro {\n'
        dot += '  rankdir=LR;\n'
        dot += '  node [shape=record];\n\n'

        actual_vm = lista_vms.cabeza
        contador = 0
        while actual_vm is not None:
            vm = actual_vm.dato
            label = (
                f"{vm.id}|SO: {vm.so}\\n"
                f"IP: {vm.ip}\\n"
                f"CPU: {vm.cpu_us}/{vm.cpu}\\n"
                f"RAM: {vm.ram_us}/{vm.ram}"
            )
            dot += f'  nodo{contador} [label="{label}"];\n'
            actual_vm = actual_vm.siguiente
            contador += 1
        dot += '\n'
        for i in range(contador - 1):
            dot += f'  nodo{i} -> nodo{i+1};\n'
        dot += '}\n'

        self._exportar(dot, nombre_archivo)
        
        
        
    def graficar_contenedores(self, id_vm, nombre_archivo="reporte_contenedores"):
        vm = self.controlador_vms.buscar_vm_por_id(id_vm)
        lista_cont = vm.contenedores  
        if lista_cont.primero is None:
            print("No hay solicitudes en Contenedor")
            return

        dot = 'digraph ContenedoresVM {\n'
        dot += '  rankdir=LR;\n'
        dot += '  node [shape=record];\n\n'

        actual = lista_cont.primero
        contador = 0
        while actual is not None:
            g_dato = actual.dato
            label = (
                f"{g_dato.id}|{g_dato.nombre}\\n"
                f"Img: {g_dato.imagen}\\n"
                f"CPU: {g_dato.cpu}% RAM: {g_dato.ram}MB\\n"
                f"Puerto: {g_dato.puerto}\\n"
                f"Estado: {g_dato.estado}"
            )
            dot += f'  nodo{contador} [label="{label}"];\n'
            actual = actual.siguiente
            contador += 1

        dot += '\n'
        for i in range(contador - 1):
            dot += f'  nodo{i} -> nodo{i+1};\n'
        dot += '}\n'

        self._exportar(dot, nombre_archivo)        
        
        
        
    def graficar_cola(self, nombre_archivo="reporte_cola"):
        cola = self.cola_solicitudes
        lista = cola.obtener_lista()  
        if lista.cabeza is None:
            print("No hay solicitudes en cola")
            return
        dot = 'digraph ColaSolicitudes {\n'
        dot += '  rankdir=LR;\n'
        dot += '  node [shape=record];\n\n'
        actual = lista.cabeza
        contador = 0
        while actual is not None:
            g_dato = actual.dato
            label = (
                f"{g_dato.id}|P:{g_dato.prioridad}\\n"
                f"{g_dato.cliente}\\n"
                f"Tipo: {g_dato.tipo}\\n"
                f"CPU:{g_dato.cpu} RAM:{g_dato.ram} DISK:{g_dato.almacenamiento}\\n"
                f"T:{g_dato.tiempo}"
            )
            dot += f'  nodo{contador} [label="{label}"];\n'
            actual = actual.siguiente
            contador += 1
        dot += '\n'
        for i in range(contador - 1):
            dot += f'  nodo{i} -> nodo{i+1};\n'
        dot += '}\n'
        
        self._exportar(dot, nombre_archivo)        
        
        
        
        
        
        

        
        
    def generar_reportes(self):
        
        self.graficar_centros("reporte_centros")  
        
        lista_centros = self.controlador_centros.centros
        actual_centro = lista_centros.cabeza
        while actual_centro is not None:
            centro = actual_centro.dato
            self.graficar_vms(centro.id_centro, f"reporte_vms_{centro.id_centro}")

            lista_vms = centro.vms
            actual_vm = lista_vms.cabeza
            while actual_vm is not None:
                vm = actual_vm.dato
                self.graficar_contenedores(vm.id, f"reporte_contenedores_{vm.id}")
                actual_vm = actual_vm.siguiente

            actual_centro = actual_centro.siguiente

        self.graficar_cola("reporte_solicitudes")


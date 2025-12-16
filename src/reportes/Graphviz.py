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
        
        # # Guardar archivo DOT
        # carpeta = "reportes"
        # os.makedirs(carpeta, exist_ok=True)

        # ruta_dot = os.path.join(carpeta, f"{nombre_archivo}.dot")
        # with open(ruta_dot, 'w', encoding='utf-8') as archivo:
        #     archivo.write(dot_content)

        #     print(f"\nEl Archivo '{nombre_archivo}.dot' generado exitosamente")

        # ruta_png = os.path.join(carpeta, f"{nombre_archivo}.png")
        # resultado = os.system(f'dot -Tpng "{ruta_dot}" -o "{ruta_png}"')

        # if resultado == 0:
        #     print(f"Imagen '{nombre_archivo}.png' generada exitosamente")
        # else:
        #     print("No se pudo generar el PNG. Asegúrate de tener Graphviz instalado.")
        #     print(f' Ejecuta manualmente: dot -Tpng "{ruta_dot}" -o "{ruta_png}"')
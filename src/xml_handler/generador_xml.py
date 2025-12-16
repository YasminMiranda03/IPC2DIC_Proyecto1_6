import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime

class GenerarXML:
    
    def __init__(self, controlador_centros):
        self.controlador_centros = controlador_centros
        
    def generar_salida(self, ruta_salida):
        try:
            root = ET.Element('resultadoCloudSync')
            
            timestamp = ET.SubElement(root,'timestamp')
            timestamp.text = datetime.now().isoformat()
            
            self._agregar_estado_centros(root)
            self._agregar_estadisticas(root)
            xml_str = minidom.parseString(ET.tostring(root,encoding='unicode')).toprettyxml(indent=" ")
            with open(ruta_salida, 'w',encoding='utf-8') as f:
                f.write(xml_str)
            return True, f"Archivo XML generado: {ruta_salida}"
        except Exception as e:
            return False, f"Error al generar XML: {str(e)}"
    
    def _agregar_estado_centros(self, root):
        estado_centros = ET.SubElement(root, 'estadoCentros')
        
        lista = self.controlador_centros.centros
        actual = lista.cabeza
        
        while actual is not None:
            centro = actual.dato
            
            centro_elem = ET.SubElement(estado_centros, 'centro', id=centro.id_centro)
            nombre = ET.SubElement(centro_elem, 'nombre')
            nombre.text = centro.nombre
            
            recursos = ET.SubElement(centro_elem, 'recursos')
            cpu_total = ET.SubElement(recursos,'cpuTotal')
            cpu_total.text=str(centro.cpu_total)
            
            cpu_disp = ET.SubElement(recursos,'cpuDisponible')
            cpu_disp.text = str(centro.cpu_disponible)
            
            cpu_util = ET.SubElement(recursos,'cpuUtilizacion')
            cpu_util.text = f"{centro.calcular_utilizacion_cpu():.2f}%"
            
            ram_total = ET.SubElement(recursos, 'ramTotal')
            ram_total.text = str(centro.ram_total)
            
            ram_disp = ET.SubElement(recursos, 'ramDisponible')
            ram_disp.text = str(centro.ram_disponible)
            
            ram_util = ET.SubElement(recursos, 'ramUtilizacion')
            ram_util.text = f"{centro.calcular_utilizacion_ram():.2f}%"
            
            cant_vms = ET.SubElement(centro_elem, 'cantidadVMs')
            cant_vms.text = str(centro.vms.tamanio)
            
            total_contenedores = 0
            vm_actual = centro.vms.primero
            while vm_actual is not None:
                total_contenedores += vm_actual.dato.contenedores.tamanio 
                vm_actual = vm_actual.siguiente
                
            cant_cont = ET.SubElement(centro_elem, 'cantidadContenedores')
            cant_cont.text = str(total_contenedores)
            actual = actual.siguiente
    def _agregar_estadisticas(self,root):
        estadisticas = ET.SubElement(root, 'estadisticas')
        total_vms = 0
        total_contenedores = 0
        
        lista = self.controlador_centros.centros
        actual = lista.cabeza
        
        while actual is not None:
            centro = actual.dato
            total_vms += centro.vms.tamanio
            
            vm_actual = centro.vms.primero
            while vm_actual is not None:
                total_contenedores += vm_actual.dato.contenedores.tamanio
                vm_actual = vm_actual.siguiente
                
            actual = actual.siguiente
        
        vms_activas = ET.SubElement(estadisticas, 'vmsActivas')
        vms_activas.text = str(total_vms)
        
        cont_totales = ET.SubElement(estadisticas, 'contenedoresTotales')
        cont_totales.text=str(total_contenedores)
            
            

#parser de archivos xml de entrada 

import xml.etree.ElementTree as ET

class ParserXml:
    
    def __init__(self,controlador_centros, control_Vms, controlador_solicitudes):
        self.controlador_centros = controlador_centros
        self.controlador_Vms = control_Vms
        self.controlador_solicitudes = controlador_solicitudes
    
    def cargar_archivo(self, ruta):
        try:
            tree = ET.parse(ruta)
            root = tree.getroot()
            
            self._procesar_centros(root)
            self._procesar_Vms(root)
            self._procesar_solicitudes(root)
            
            self._procesar_instrucciones(root)
            return True, "El archivo Xml ha sido cargado correctamente"
        
        except Exception as e:
            return False, f"El archivo Xml no pudo ser cargado{str(e)}"
        
    def _procesar_centros(self, root):
        centros = root.find('.//centroDatos')
        if centros is None:
            return
        for centro_elem in centros.findall('centro'):
            id_centro = centro_elem.get('id')
            nombre = centro_elem.get('nombre')
            
            ubicacion = centro_elem.find('ubicacion')
            pais = ubicacion.find('pais').text
            ciudad = ubicacion.find('ciudad').text
            
            capacidad = centro_elem.find('capacidad')
            cpu = int(capacidad.find('cpu').text)
            ram = int(capacidad.find('ram').text)
            almacenamiento = int(capacidad.find('almacenamiento').text)
            
            self.controlador_centros.crear_centro(
                id_centro,nombre,pais,ciudad,cpu,ram,almacenamiento
            )
            
            print(f"Correctamente {id_centro} cargado")
    
    
    def _procesar_vms(self, root):
        vms = root.find('.//maquinasVirtuales')
        if vms is None:
            return
    
        for vm_elem in vms.findall('vm'):
            id_vm = vm_elem
            
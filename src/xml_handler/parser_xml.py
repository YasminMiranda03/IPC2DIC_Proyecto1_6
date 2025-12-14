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
            self._procesar_vms(root)
            self._procesar_solicitudes(root)
            
            self._procesar_instrucciones(root)
            return True, "El archivo Xml ha sido cargado correctamente"
        
        except Exception as e:
            return False, f"El archivo Xml no pudo ser cargado{str(e)}"
        
    def _procesar_centros(self, root):
        centros = root.find('.//CentroDatos')
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
        vms = root.find('.//MaquinaVirtual')
        if vms is None:
            return
    
        for vm_elem in vms.findall('vm'):
            id_vm = vm_elem.get('id')
            centro_asiganado = vm_elem.get('centroAsignado')
            so = vm_elem.find('sistemaOperativo').text
            ip = vm_elem.find('ip').text
            
            recursos = vm_elem.find('recursos')
            cpu = int(recursos.find('cpu').text)
            ram = int(recursos.find('ram').text)
            almacenamiento = int(recursos.find('almacenamiento').text)
            
            exito, msg = self.controlador_Vms.crear_vm(
                id_vm,centro_asiganado,so,cpu,ram,almacenamiento,ip
            )
            if exito:
                print(f"Vm {id_vm} ha sigo cargado en {centro_asiganado}")
                self._procesar_contenedores(vm_elem, id_vm)
            else:
                print(f"Error:la carga de Vm fallo {id_vm}:{msg}")
    
    
    def _procesar_contenedores(self, vm_elem, id_vm):
        from modelos.Contenedor import Contenedor
        
        contenedores_elem = vm_elem.find('contenedores')
        if contenedores_elem is None:
            return

        vm, centro = self.controlador_Vms.buscar_vm(id_vm)
        if not vm:
            return
    
        for cont_elem in contenedores_elem.findall('contenedor'):
            id_contenedor = cont_elem.get('id')
            nombre = cont_elem.find('nombre').text
            imagen = cont_elem.find('imagen').text
            puerto = int(cont_elem.find('puerto').text)

            recursos = cont_elem.find('recursos')
            cpu = int(recursos.find('cpu').text)
            ram = int(recursos.find('ram').text)
            
            contenedor = Contenedor(id_contenedor,nombre,imagen,puerto,cpu,ram)        
            vm.agregar_contenedor(contenedor)
            
            print(f"El contenedor {id_contenedor} a sido agregado a {id_vm}")
    
    def _procesar_solicitudes(self, root):
        solicitudes = root.find('.//Solicitud')
        if solicitudes is None:
            return

        for sol_elem in solicitudes.findall('solicitud'):
            id_solicitud = sol_elem.get('id')
            cliente = sol_elem.find('cliente').text
            tipo = sol_elem.find('tipo').text
            prioridad = int(sol_elem.find('prioridad').text)
            tiempo_estimmado = int(sol_elem.find('tiempoEstimado').text)
            
            recursos = sol_elem.find('recursos')
            cpu = int(recursos.find('cpu').text)
            ram = int(recursos.find('ram').text)
            almacenamiento = int(recursos.find('almacenamiento').text)
            
            self.controlador_solicitudes.agregar_solicitud(
            id_solicitud,cliente,tipo,prioridad,cpu,ram,almacenamiento,tiempo_estimmado)
            
       
       
       
            print(f"Solicitud {id_solicitud} ha sido cargada exitosamente")
            
    def _procesar_instrucciones(self, root):
        instrucciones = root.find('.//intrucciones')
        if instrucciones is None:
            return
        print("***Ejecutando Instrucciones****\n")
         
        for inst in instrucciones.findall('instruccion'):
            tipo = inst.get('tipo')
            if tipo =='crearVM':
                 self._ejecutar_crear_vm(inst)
            elif tipo == 'migrarVM':
                 self._ejecutar_migrar_vm(inst)
            elif tipo == 'procesarSolicitudes':
                self._ejecutar_procesar_solicitudes(inst)
            elif tipo == 'balancearCarga':
                print("Balanceo de Carga listo")
    def _ejecutar_crear_vm(self, inst):
        id_vm = inst.find('id').text
        centro = inst.find('centro').text
        so = inst.find('so').text
        cpu = int(inst.find('cpu').text)
        ram = int(inst.find('ram').text)
        almacenamiento = int(inst.find('almacenamiento').text)
        
        exito, msg = self.controlador_Vms.crear_vm(
            id_vm,centro,so,cpu,ram,almacenamiento,f"192.168.1.{cpu}"
        )
        print(f"{'Cargo correctamente' if exito else'Ocurrio un error'} {msg}")
        
    def _ejecutar_migrar_vm(self, inst):
        vm_id = inst.find('vmId').text
        destino = inst.find('centroDestino').text
        
        exito, msg = self.controlador_Vms.migrar_vm(vm_id,destino)
        print(f"{'Cargo correctamente' if exito else'Ocurrio un error'} {msg}")
        
    def _ejecutar_procesar_solicitudes(self, inst):
        cantidad = int(inst.find('cantidad').text)
        exito, msg = self.controlador_solicitudes.procesar_n_solicitudes(cantidad)
        print(f"Exito {msg}")        
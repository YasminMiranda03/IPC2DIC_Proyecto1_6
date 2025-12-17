from controladores.CentroDatosController import CentroDatosController
from controladores.MaquinaVirtualController import MaquinaVirtualController
from controladores.ContenedorController import ContenedorController
from xml_handler.generador_xml import GenerarXML
from xml_handler.parser_xml import ParserXml
from controladores.CentroDatosMenu import menu_centros
from controladores.MaquinaVirtualMenu import menu_vms
from controladores.ContenedorMenu import menu_contenedores
from reportes.Graphviz import ReportesGraphviz
from controladores.ControlSolicitudes import SolicitudesController
from controladores.controlSolicitudesMenu import solicitud_menu


print("borrar esto ")
print("|** Bienvenido que accion desea realizar*|")
def mostrar_menu():
    print("\n|**************CloudSync*****************|")
    print("|----------------------------------------|")
    print("|*** 1. Cargar archivo XML            ***|")
    print("|*** 2. Gestion de centros de datos   ***|")
    print("|*** 3. Gesrion de maquinas virtuales ***|")
    print("|*** 4. Gestion de contenedores       ***|")
    print("|*** 5. Gestion de solicitudes        ***|")
    print("|*** 6. Reportes Grapvhiz             ***|")
    print("|*** 7. Generar XML de salida         ***|")
    print("|*** 8. Historial de operaciones      ***|")
    print("|*** 9. Salir                         ***|")
    print("|----------------------------------------|")
def menu_principal():
    controlador_centros = CentroDatosController()
    controlador_vms = MaquinaVirtualController(controlador_centros)
    controlador_contenedores = ContenedorController(controlador_vms)
    controlador_solicitudes = SolicitudesController()
    while True:
        try:    #el try para manejar los errores
            mostrar_menu()
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                print("Cargar archivo XML")
                ruta = input("Ingrese ruta de XML: ")
                parser = ParserXml(controlador_centros, controlador_vms, controlador_solicitudes)
                exito, msg = parser.cargar_archivo(ruta)
                print(msg)
            elif opcion == 2:
                print("\nGESTION DE CENTRO DE DATOS")
                menu_centros(controlador_centros)
            elif opcion == 3:
                print("\nGESTION DE MAQUINAS VIRTUALES")
                menu_vms(controlador_vms)
            elif opcion == 4:
                print("\nGESTION DE CONTENEDORES")
                menu_contenedores(controlador_contenedores)
            elif opcion == 5:
                print("\nGESTION DE SOLICITUDES")
                solicitud_menu(controlador_solicitudes)
            elif opcion == 6:
                print("\nREPORTES GRAPHVIZ")
                reportes = ReportesGraphviz(controlador_centros, controlador_vms, controlador_solicitudes.cola)
                reportes.generar_reportes()
            elif opcion == 7:
                print("\nGENERAR XML DE SALIDA")
                generador = GenerarXML(controlador_centros)
                exito, msg = generador.generar_salida("salida.xml") 
                print(msg)
            elif opcion == 8:
                print("\nHISTORIAL DE OPERACIONES")
                #llamar a la funcion de historial de operacion
            elif opcion == 9:
                break
        except ValueError:
            print("Error: Debe ingresar un numero valido")
            
from controladores.CentroDatosMenu import menu_centros
from controladores.MaquinaVirtualMenu import menu_vms

def mostrar_menu():
    print("1. Cargar archivo XML")
    print("2. Gestion de centros de datos")
    print("3. Gesrion de maquinas virtuales")
    print("4. Gestion de contenedores")
    print("5. Gestion de solicitudes")
    print("6. Reportes Grapvhiz")
    print("7. Generar XML de salida")
    print("8. Historial de operaciones")
    print("9. Salir")

def menu_principal():
    while True:
        try:    #el try para manejar los errores
            mostrar_menu()
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                print("Cargar archivo XML")
                #llamar a la funcion
            elif opcion == 2:
                print("\nGESTION DE CENTRO DE DATOS")
                menu_centros(controlador_centros)
            elif opcion == 3:
                print("\nGESTION DE MAQUINAS VIRTUALES")
                menu_vms(controlador_vms)
            elif opcion == 4:
                print("\nGESTION DE CONTENEDORES")
                #llamar al menu de contenedores
            elif opcion == 5:
                print("\nGESTION DE SOLICITUDES")
                #llamar al menu de solicitudes  
            elif opcion == 6:
                print("\nREPORTES GRAPHVIZ")
                #llamar a la funcion de reportes graphviz
            elif opcion == 7:
                print("\nGENERAR XML DE SALIDA")
                #llamar a la funcion de generar xml de salida
            elif opcion == 8:
                print("\nHISTORIAL DE OPERACIONES")
                #llamar a la funcion de historial de operacion
            elif opcion == 9:
                break
        except ValueError:
            print("Error: Debe ingresar un numero valido")
            
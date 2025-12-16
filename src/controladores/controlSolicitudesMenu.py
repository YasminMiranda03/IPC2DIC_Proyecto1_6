def solicitud_menu(controlador_solicitudes):
    while True:
        try:
            print("\n--Gestionar Solicitudes--")
            print("1. Agregar nueva solicitud")
            print("2. Procesar solicitud de mayor prioridad")
            print("3. Procesar N solicitudes")
            print("4. Ver cola de solicitudes")
            print("5. Volver al menú principal")
            opcion = int(input("Seleccione una opcion: "))
            
            if opcion == 1:
                id_solicitud = input("id Solicitud: ")
                cliente = input("Cliente: ")
                tipo = input("Tipo: ")
                prioridad = int(input("Prioridad: "))
                cpu = int(input("Cpu: "))
                ram = int(input("Ram: "))
                almacenamiento = int(input("Almacenamiento: "))
                tiempo = int(input("Tiempo estimado: "))
                exito, msg = controlador_solicitudes.agregar_solicitud(
                    id_solicitud,cliente,tipo,prioridad,cpu,ram,almacenamiento,tiempo
                )
                print(msg)

            
            elif opcion == 2:
                exito,msg = controlador_solicitudes.procesar_mayor_prioridad()
                print(msg)
            
            elif opcion == 3:
                numero_solicitudes = int(input("Numero de solicitudes: "))
                exito, msg = controlador_solicitudes.procesar_n_solicitudes(numero_solicitudes)
                print(msg)
            
            elif opcion == 4:
                controlador_solicitudes.ver_cola()
            
            elif opcion == 5:
                break
            else:
                print("Opcion no valida")
                
        except ValueError:
            print("Error: Debe ingresar un numero valido")
        except Exception as e:
            print(f"error incesperado {e}")
def menu_centros(controlador_centros):
    while True:
        try:
            print("\n--menu centro datos--")
            print("1. Crear centro de daots")
            print("2. Listar centros de datos")
            print("3. Buscar centro por id")
            print("4. Eliminar")
            print("5. Volver al menu principal")
            
            opcion = int(input("Seleccione una opcion: "))
            
            if opcion == 1:
                id = input("Id del centro: ")
                nombre = input("Nombre del centro: ")
                pais = input("Pais: ")
                ciudad = input("ciudad: ")
                cpu = int(input("Capacidad CPU: "))
                ram = int(input("Capacidad RAM: "))
                almacenamiento = int(input("almacenamiento: "))
                
                exito, msg = controlador_centros.crear_centro(
                    id,nombre,pais,ciudad,cpu,ram,almacenamiento)
                print(msg)
                
            elif opcion == 2:
                controlador_centros.listar_centros()
                
            elif opcion == 3:
                id = input("Ingrese el id para buscar: ")
                centro = controlador_centros.buscar_centro(id)
                if centro:
                    print(f"Centro encontrado: {centro.nombre}")
                else:
                    print(f"Centro con id {id} no encontrado")
            
            elif opcion == 4:
                id = input("id del centro para eliminar: ")
                exito, msg = controlador_centros.eliminar_centro(id)
                print(msg)
            
            elif opcion == 5:
                break
            
            else:
                print("Opcion no valida")
        
        except ValueError:
            print("ingrese un numero valido")
            
        except Exception as e:
            print(f"Error inesperado {e}")
def menu_centros(controlador_centros):
    while True:
        try:
            print("\n--menu centro datos--")
            print("1. Mostrar centro con más recursos")
            print("2. Listar centros de datos")
            print("3. Buscar centro por id")
            print("4. Volver al menu principal")
            
            opcion = int(input("Seleccione una opcion: "))
            
            if opcion == 1:
                centro = controlador_centros.centro_mayor_recursos()
                if centro is None:
                    print("No hay centros registrados")
                else:
                    print("\n Centro de Datos con más recursos ")
                    print(f"**************")
                    print(f"ID: {centro.id_centro}")
                    print(f"Nombre: {centro.nombre}")
                    print(f"Ubicación: {centro.pais}, {centro.ciudad}")
                    print(f"CPU disponible: {centro.cpu_disponible}/{centro.cpu_total}")
                    print(f"RAM disponible: {centro.ram_disponible}/{centro.ram_total}")
                    print(f"Almacenamiento disponible: {centro.almacenamiento_disponible}/{centro.almacenamiento_total}")
                
            elif opcion == 2:
                controlador_centros.listar_centros()
                
            elif opcion == 3:
                id = input("Id del centro: ")
                centro = controlador_centros.buscar_centro(id)
                if centro is None:
                    print(f"El centro {id} no existe")
                else:
                    print("\n Centro de Datos ")
                    print(f"****************************************")
                    print(f"ID: {centro.id_centro}")
                    print(f"Nombre: {centro.nombre}")
                    print(f"Ubicación: {centro.pais}, {centro.ciudad}")
                    print(f"CPU disponible: {centro.cpu_disponible}/{centro.cpu_total}")
                    print(f"RAM disponible: {centro.ram_disponible}/{centro.ram_total}")
                    print(f"Almacenamiento disponible: {centro.almacenamiento_disponible}/{centro.almacenamiento_total}")
            
            # elif opcion == 4:
            #     id = input("id del centro para eliminar: ")
            #     exito, msg = controlador_centros.eliminar_centro(id)
            #     print(msg)
            
            elif opcion == 4:
                break
            
            else:
                print("Opcion no valida")
        
        except ValueError:
            print("ingrese un numero valido")
            
        except Exception as e:
            print(f"Error inesperado {e}")
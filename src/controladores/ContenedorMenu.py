def menu_contenedores(controlador_contenedores):
    while True:
        try:
            print("\nGESTION DE CONTENEDORES")
            print("1. Desplegar contenedor en VM")
            print("2. Listar contenedores de una VM")
            print("3. Cambiar estado de contenedor")
            print("4. Eliminar contenedor")
            print("5. Volver al menú principal")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                id_vm = input("ID de la VM: ")
                id_cont = input("ID del contenedor: ")
                nombre = input("Nombre: ")
                imagen = input("Imagen: ")
                cpu = int(input("CPU: "))
                ram = int(input("RAM: "))
                puerto = int(input("Puerto: "))

                exito, msg = controlador_contenedores.desplegar_contenedor(
                    id_vm, id_cont, nombre, imagen, cpu, ram, puerto
                )
                print(msg)

            elif opcion == 2:
                id_vm = input("ID de la VM: ")
                controlador_contenedores.listar_contenedores_vm(id_vm)

            elif opcion == 3:
                id_vm = input("ID de la VM: ")
                id_cont = input("ID del contenedor: ")
                print("Estados disponibles: Activo | Pausado | Reiniciando | Detenido")
                estado = input("Nuevo estado: ")

                exito, msg = controlador_contenedores.cambiar_estado_contenedor(
                    id_vm, id_cont, estado
                )
                print(msg)

            elif opcion == 4:
                id_vm = input("ID de la VM: ")
                id_cont = input("ID del contenedor: ")

                exito, msg = controlador_contenedores.eliminar_contenedor(
                    id_vm, id_cont
                )
                print(msg)

            elif opcion == 5:
                break

            else:
                print("Opción inválida")

        except ValueError:
            print("Error: entrada inválida")
        except Exception as e:
            print(f"Error inesperado: {e}")
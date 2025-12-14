def menu_vms(controlador_vms):
    while True:
        try:
            print("\n--Menu Maquinas Virtuales--")
            print("1. Buscar vm por id")
            print("2. Listar vms de un centro")
            print("3. migrar vm")
            print("4. volver")
            opcion = int(input("Seleccione una opcion: "))
            
            if opcion == 1:
                id_vm = input("ingrese el id: ")
                vm = controlador_vms.buscar_vm_por_id(id_vm)
                if vm:
                    controlador_vms.mostrar_detalle_vm(vm)
                else:
                    print("Vm no encontrada")
            
            elif opcion == 2:
                id_centro = input("id del centro: ")
                controlador_vms.listar_vms_por_centro(id_centro)
            
            elif opcion == 3:
                id_vm = input("Id de la vm que se va a migrar: ")
                centro_destino = input("Id del centro de destino: ")
                
                exito, msg = controlador_vms.migrar_vm(id_vm, centro_destino)
                print(msg)
            
            elif opcion == 4:
                break
            else:
                print("Opcion no valida")
                
        except ValueError:
            print("Error: Debe ingresar un numero valido")
        except Exception as e:
            print("error incesperado")
from menu import *
from modulo_servicios import *
from modulo_gestion import *
from modulo_reportes import *
from modulo_ventas import *
from cargar_datos import * 

ruta_base_de_datos = "datos.json"

datos = cargar_datos(ruta_base_de_datos)

while True:
    menu_principal()
    op = pedir_opcion()
    
    if op == 5:
        print("--"*20)
        print("Adios!!")
        print("--"*20)
        break
    if op == 1:
        while True:
            menu_gestion()
            op1 = pedir_opcion()

            if op1 == 1:
                print("--"*20)
                datos = agregar_usuario(datos)
                print("--"*20)
            elif op1 == 2:
                print("--"*20)
                buscar_usuario(datos)
                print("--"*20)
            elif op1 == 3:
                print("--"*20)
                datos = eliminar_usuario(datos)
                print("--"*20)
            elif op1 == 4:
                print("--"*20)
                datos = modificar_usuario(datos)
                print("--"*20)
            elif op1 == 5:
                break
            else:
                print("Opción no válida")

    if op == 2:
        while True:
            menu_servcio()
            op2 = pedir_opcion()

            if op2 == 1:
                print("--"*20)
                datos = agregar_producto(datos)
                print("--"*20)
            elif op2 == 2:
                print("--"*20)
                buscar_producto(datos)
                print("--"*20)
            elif op2 == 3:
                print("--"*20)
                datos = eliminar_producto(datos)
                print("--"*20)
            elif op2 == 4:
                print("--"*20)
                datos = modificar_producto(datos)
                print("--"*20)
            elif op2 == 5:
                print("--"*20)
                datos = agregar_servicio(datos)
                print("--"*20)
            elif op2 == 6:
                print("--"*20)
                buscar_servicio(datos)
                print("--"*20)
            elif op2 == 7:
                print("--"*20)
                datos = eliminar_servicio(datos)
                print("--"*20)
            elif op2 == 8:
                print("--"*20)
                datos = modificar_servicio(datos)
                print("--"*20)
            elif op2 == 9:
                print("--"*20)
                datos = agregar_promocion(datos)
                print("--"*20)
            elif op2 == 10:
                print("--"*20)
                buscar_promocion(datos)
                print("--"*20)
            elif op2 == 11:
                print("--"*20)
                datos = eliminar_promocion(datos)
                print("--"*20)
            elif op2 == 12:
                print("--"*20)
                datos = modificar_promocion(datos)
                print("--"*20)
            elif op2 == 13:
                break
            else:
                print("Opción no válida")

    if op == 3:
        while True:
            menu_reportes()
            op3 = pedir_opcion()

            if op3 == 1:
                print("--"*20)
                datos = agregar_reclamo(datos)
                print("--"*20)
            elif op3 == 2:
                print("--"*20)
                buscar_reclamo(datos)
                print("--"*20)
            elif op3 == 3:
                print("--"*20)
                datos = eliminar_reclamo(datos)
                print("--"*20)
            elif op3 == 4:
                print("--"*20)
                datos = modificar_reclamo(datos)
                print("--"*20)
            elif op3 == 5:
                print("--"*20)
                datos = agregar_sugerencia(datos)
                print("--"*20)
            elif op3 == 6:
                print("--"*20)
                buscar_sugerencia(datos)
                print("--"*20)
            elif op3 == 7:
                print("--"*20)
                datos = eliminar_sugerencia(datos)
                print("--"*20)
            elif op3 == 8:
                print("--"*20)
                datos = modificar_sugerencia(datos)
                print("--"*20)
            elif op3 == 9:
                break
            else:
                print("Opción no válida")

    if op == 4:
        while True:
            menu_ventas()
            op4 = pedir_opcion()

            if op4 == 1:
                print("--"*20)
                datos = agregar_venta(datos)
                print("--"*20)
            elif op4 == 2:
                print("--"*20)
                buscar_venta(datos)
                print("--"*20)
            elif op4 == 3:
                print("--"*20)
                datos = eliminar_venta(datos)
                print("--"*20)
            elif op4 == 4:
                print("--"*20)
                datos = modificar_venta(datos)
                print("--"*20)
            elif op4 == 5:
                break
            else:
                print("Opción no válida")


guardar_datos(datos, ruta_base_de_datos)



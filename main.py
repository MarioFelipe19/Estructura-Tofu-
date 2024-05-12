from menu import *
from funciones import *
from cargar_datos import * 

ruta_base_de_datos = "datos.json"

datos = cargar_datos(ruta_base_de_datos)


while True:
    menu_principal()
    op = pedir_opcion()
    if op == 1:
        print("--"*20)
        datos = agregar_usuario(datos)
        print("--"*20)
    elif op == 2:
        print("--"*20)
        buscar_usuario(datos)
        print("--"*20)
    elif op == 3:
        print("--"*20)
        datos = eliminar_usuario(datos)
        print("--"*20)
    elif op == 4:
        print("--"*20)
        datos = modificar_usuario(datos)
        print("--"*20)
    elif op == 5:
        print("--"*20)
        datos = agregar_producto(datos)
        print("--"*20)
    elif op == 6:
        print("--"*20)
        buscar_producto(datos)
        print("--"*20)
    elif op == 7:
        print("--"*20)
        datos = eliminar_producto(datos)
        print("--"*20)
    elif op == 8:
        print("--"*20)
        datos = modificar_producto(datos)
        print("--"*20)
    elif op == 9:
        print("--"*20)
        datos = agregar_servicio(datos)
        print("--"*20)
    elif op == 10:
        print("--"*20)
        buscar_servicio(datos)
        print("--"*20)
    elif op == 11:
        print("--"*20)
        datos = eliminar_servicio(datos)
        print("--"*20)
    elif op == 12:
        print("--"*20)
        datos = modificar_servicio(datos)
        print("--"*20)
    elif op == 13:
        print("--"*20)
        datos = agregar_reclamo(datos)
        print("--"*20)
    elif op == 14:
        print("--"*20)
        buscar_reclamo(datos)
        print("--"*20)
    elif op == 15:
        print("--"*20)
        datos = eliminar_reclamo(datos)
        print("--"*20)
    elif op == 16:
        print("--"*20)
        datos = modificar_reclamo(datos)
        print("--"*20)
    elif op == 17:
        print("--"*20)
        datos = agregar_sugerencia(datos)
        print("--"*20)
    elif op == 18:
        print("--"*20)
        buscar_sugerencia(datos)
        print("--"*20)
    elif op == 19:
        print("--"*20)
        datos = eliminar_sugerencia(datos)
        print("--"*20)
    elif op == 20:
        print("--"*20)
        datos = modificar_sugerencia(datos)
        print("--"*20)
    elif op == 21:
        print("--"*20)
        datos = agregar_venta(datos)
        print("--"*20)
    elif op == 22:
        print("--"*20)
        buscar_venta(datos)
        print("--"*20)
    elif op == 23:
        print("--"*20)
        datos = eliminar_venta(datos)
        print("--"*20)
    elif op == 24:
        print("--"*20)
        modificar_venta()
        print("--"*20)
    elif op == 25:
        print("--"*20)
        print("Adios!!")
        print("--"*20)
        break

guardar_datos(datos, ruta_base_de_datos)
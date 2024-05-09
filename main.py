from menu import *
from funciones import *

while True:
    menu_principal()
    op = pedir_opcion()
    if op == 1:
        print("--"*20)
        agregar_usuario()
        print("--"*20)
    elif op == 2:
        print("--"*20)
        buscar_usuario()
        print("--"*20)
    elif op == 3:
        print("--"*20)
        eliminar_usuario()
        print("--"*20)
    elif op == 4:
        print("--"*20)
        modificar_usuario()
        print("--"*20)
    elif op == 5:
        print("--"*20)
        agregar_producto()
        print("--"*20)
    elif op == 6:
        print("--"*20)
        buscar_producto()
        print("--"*20)
    elif op == 7:
        print("--"*20)
        eliminar_producto()
        print("--"*20)
    elif op == 8:
        print("--"*20)
        modificar_producto()
        print("--"*20)
    elif op == 9:
        print("--"*20)
        agregar_servicio()
        print("--"*20)
    elif op == 10:
        print("--"*20)
        buscar_servicio()
        print("--"*20)
    elif op == 11:
        print("--"*20)
        eliminar_servicio()
        print("--"*20)
    elif op == 12:
        print("--"*20)
        modificar_servicio()
        print("--"*20)
    elif op == 13:
        print("--"*20)
        agregar_reclamacion()
        print("--"*20)
    elif op == 14:
        print("--"*20)
        buscar_reclamacion()
        print("--"*20)
    elif op == 15:
        print("--"*20)
        eliminar_reclamacion()
        print("--"*20)
    elif op == 16:
        print("--"*20)
        modificar_reclamacion()
        print("--"*20)
    elif op == 17:
        print("--"*20)
        agregar_sugerencia()
        print("--"*20)
    elif op == 18:
        print("--"*20)
        buscar_sugerencia()
        print("--"*20)
    elif op == 19:
        print("--"*20)
        eliminar_sugerencia()
        print("--"*20)
    elif op == 20:
        print("--"*20)
        modificar_sugerencia()
        print("--"*20)
    elif op == 21:
        print("--"*20)
        agregar_venta()
        print("--"*20)
    elif op == 22:
        print("--"*20)
        buscar_venta()
        print("--"*20)
    elif op == 23:
        print("--"*20)
        eliminar_venta()
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
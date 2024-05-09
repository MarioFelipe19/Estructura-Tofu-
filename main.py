from menu import *
from funciones import *

while True:
    menu_principal()
    op = pedir_opcion()
    if op == 1:
        print("--"*20)
        registrar_usuario()
    elif op == 2:
        print("--"*20)
        buscar_usuario()
    elif op == 3:
        print("--"*20)
        eliminar_usuario()
    elif op == 4:
        print("--"*20)
        modificar_usuario()
    elif op == 5:
        print("--"*20)
        consultar_servicio()
    elif op == 6:
        print("--"*20)
        agregar_reclamacion()
    elif op == 7:
        print("--"*20)
        agregar_sugerencia()
    elif op == 8:
        print("--"*20)
        registrar_producto
    elif op == 9:
        print("--"*20)
        registrar_venta_producto
    elif op == 10:
        print("--"*20)
        print("Salió!!")
        break
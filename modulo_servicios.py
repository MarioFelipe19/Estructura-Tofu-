from modulo_gestion import *
from modulo_ventas import *
from modulo_reportes import *


def agregar_producto(datos):
    datos = dict(datos)
    producto = {}
    producto["tipo"] = input("Ingrese el tipo del producto: ")
    producto["marca"] = input("Ingrese la marca del producto: ")
    producto["referencia"] = input("Ingrese la referencia del producto: ")
    producto["cantidad"] = int(input("Ingrse la cantidad del producto: "))
    producto["costo"] = float(input("Ingrse el costo del producto: "))
    datos["producto"].append(producto)
    print("--"*13)
    print("Producto registrado con exito!")
    print("--"*13)
    return datos

def buscar_producto(datos):
    datos = dict(datos)
    op = int(input("Buscar por 1. Tipo producto, 2. Lista producto: "))
    if op == 1:
        tipo = input("Ingrese el tipo de producto a buscar: ")
        referencia = input("Ingrese la referencia de producto a buscar: ")
        for i in range(len(datos["producto"])):
            if datos["producto"][i]["tipo"] == tipo and datos["producto"][i]["referencia"] == referencia:
                print("__"*10)
                print("\n""Tipo:",datos["producto"][i]["tipo"],"\n" "Marca:", datos["producto"][i]["marca"],"\n""Referencia:",datos["producto"][i]["referencia"],"\n" "Cantidad:",datos["producto"][i]["cantidad"],"\n" "Costo:",datos["producto"][i]["costo"])
                print("__"*10)
                return
    elif op == 2:
        while True:
            for i in range(len(datos["producto"])):
                print("__"*10)
                print("\n""Tipo:",datos["producto"][i]["tipo"],"\n" "Marca:", datos["producto"][i]["marca"],"\n""Referencia:",datos["producto"][i]["referencia"],"\n" "Cantidad:",datos["producto"][i]["cantidad"],"\n" "Costo:",datos["producto"][i]["costo"])
                print("__"*10)
            return 
    print("__"*10)
    print("Tipo de producto invalido!")
    print("__"*10)

def eliminar_producto(datos):
    datos = dict(datos)
    referencia = input("Ingrese la referencia del producto a eliminar: ")
    for i in range(len(datos["producto"])):
        if datos["producto"][i]["referencia"] == referencia:
            datos["producto"].pop(i)
            print("__"*10)
            print("\n""Producto eliminado!")
            print("__"*10)
            return datos
        
    print("__"*10)
    print("Producto no existe!")
    print("__"*10)
    return datos

def modificar_producto(datos):
    datos = dict(datos)
    referencia = input("Ingrese la referencia del producto a modificar: ")
    for i in range(len(datos["producto"])):
        if datos["producto"][i]["referencia"] == referencia:
            datos["producto"][i]["referencia"] = input("Ingrese la nueva referencia: ")
            datos["producto"][i]["cantidad"] = int(input("Ingrse la nueva cantidad: "))
            datos["producto"][i]["costo"]  = float(input("Ingrese el nuevo costo: "))
            print("--"*13)
            print("producto modificado con exito!")
            print("--"*13)
            return datos
        
    print("__"*10)
    print("Producto no existe!")
    print("__"*10)
    return datos

def agregar_servicio(datos):
    datos = dict(datos)
    servicio = {}
    servicio["tipo"] = input("Ingrese el tipo de servicio: ")
    servicio["referencia"] = input("Ingrese la referencia del servicio: ")
    servicio["costo"] = float(input("Ingrese el costo del servicio: "))
    datos["servicio"].append(servicio)
    print("--"*13)
    print("Servicio registrado con exito!")
    print("--"*13)
    return datos

def buscar_servicio(datos):
    datos = dict(datos)
    op = int(input("Buscar por 1. Tipo servicio, 2. Lista servicios: "))
    if op == 1:
        tipo = input("Ingrese el tipo de servicio a buscar: ")
        referencia = input("Ingrese la referencia de servicio a buscar: ")
        for i in range(len(datos["servicio"])):
            if datos["servicio"][i]["tipo"] == tipo and datos["servicio"][i]["referencia"] == referencia:
                print("__"*10)
                print("\n""Tipo:",datos["servicio"][i]["tipo"],"\n" "Referencia:", datos["servicio"][i]["referencia"],"\n""Costo:",datos["servicio"][i]["costo"],)
                print("__"*10)
                return
    elif op == 2:
        while True:
            for i in range(len(datos["servicio"])):
                print("__"*10)
                print("\n""Tipo:",datos["servicio"][i]["tipo"],"\n" "Referencia:", datos["servicio"][i]["referencia"],"\n""Costo:",datos["servicio"][i]["costo"],)
                print("__"*10)
            return 
    print("__"*10)
    print("Tipo de servicio invalido!")
    print("__"*10)

def eliminar_servicio(datos):
    datos = dict(datos)
    referencia = input("Ingrese la referencia del servicio a eliminar: ")
    for i in range(len(datos["servicio"])):
        if datos["servicio"][i]["referencia"] == referencia:
            datos["servicio"].pop(i)
            print("__"*10)
            print("servicio eliminado!")
            print("__"*10)
            return datos
        
    print("__"*10)
    print("Servicio no existe!")
    print("__"*10)
    return datos

def modificar_servicio(datos):
    datos = dict(datos)
    referencia = input("Ingrese la referencia del servicio a modificar: ")
    for i in range(len(datos["servicio"])):
        if datos["servicio"][i]["referencia"] == referencia:
            datos["servicio"][i]["referencia"] = input("Ingrese la nueva referencia del servicio: ")
            datos["servicio"][i]["costo"]  = float(input("Ingrese el nuevo costo del servicio: "))
            print("--"*13)
            print("servicio modificado con exito!")
            print("--"*13)
            return datos
        
    print("__"*10)
    print("Producto no existe!")
    print("__"*10)
    return datos

def agregar_promocion(datos):
    datos = dict(datos)
    promocion = {}
    promocion["tipo"] = input("Ingrese el tipo de promocion: ")
    promocion["referencia"] = input("Ingrese la referencia de la promocion: ")
    promocion["costo"] = float(input("Ingrese el costo de la promocion: "))
    datos["promocion"].append(promocion)
    print("--"*13)
    print("Promocion registrado con exito!")
    print("--"*13)
    
    for i in range(len(datos["usuario"])):
        for j in range(len(datos["venta"])):
            if  datos["usuario"][i]["categoria"] == 3 and datos["venta"][j]["numero"] >= 3:
                datos["usuario"][i]["promocion"] = promocion["referencia"]
                datos["usuario"][i]["costo"] = promocion["costo"]
                #;random.randint(range(0,[i]+1))
            else:
                print("No hay usuarios con requerimientos disponibles para promociones")
            return datos

def buscar_promocion(datos):
    datos = dict(datos)
    op = int(input("Buscar por 1. Tipo promocion, 2. Lista promocion: "))
    if op == 1:
        tipo = input("Ingrese el tipo de promocion a buscar: ")
        for i in range(len(datos["promocion"])):
            if datos["promocion"][i]["tipo"] == tipo:
                print("__"*10)
                print("\n""Tipo:",datos["promocion"][i]["tipo"],"\n" "Referencia:", datos["promocion"][i]["referencia"],"\n""Costo:",datos["promocion"][i]["costo"],)
                print("__"*10)
                return
    elif op == 2:
        while True:
            for i in range(len(datos["promocion"])):
                print("__"*10)
                print("\n""Tipo:",datos["promocion"][i]["tipo"],"\n" "Referencia:", datos["promocion"][i]["referencia"],"\n""Costo:",datos["promocion"][i]["costo"],)
                print("__"*10)
            return 
    print("__"*10)
    print("Tipo de promocion invalido!")
    print("__"*10)

def eliminar_promocion(datos):
    datos = dict(datos)
    referencia = input("Ingrese la referencia de la promocion a eliminar: ")
    for i in range(len(datos["promocion"])):
        if datos["promocion"][i]["referencia"] == referencia:
            datos["promocion"].pop(i)
            print("__"*10)
            print("Promocion eliminado!")
            print("__"*10)
            return datos
        
    print("__"*10)
    print("Promocion no existe!")
    print("__"*10)
    return datos

def modificar_promocion(datos):
    datos = dict(datos)
    referencia = input("Ingrese la referencia de la promocion a modificar: ")
    for i in range(len(datos["promocion"])):
        if datos["promocion"][i]["referencia"] == referencia:
            datos["promocion"][i]["referencia"] = input("Ingrese la nueva referencia de la promocion: ")
            datos["promocion"][i]["costo"]  = float(input("Ingrese el nuevo costo de la promocion: "))
            print("--"*13)
            print("Promocion modificado con exito!")
            print("--"*13)
            for i in range(len(datos["usuario"])):
                for j in range(len(datos["venta"])):
                    for i in range(len(datos["promocion"])):
                        if  datos["usuario"][i]["categoria"] == 3 and datos["venta"][j]["numero"] >= 3:
                            datos["usuario"][i]["promocion"] = datos["promocion"][i]["referencia"]
                            datos["usuario"][i]["costo"] = datos["promocion"][i]["costo"]
                        else:
                            print("No hay usuarios con requerimientos disponibles para promociones")
                        return datos
        
    print("__"*10)
    print("Promocion no existe!")
    print("__"*10)
    return datos
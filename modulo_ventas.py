from funciones import *
from modulo_gestion import *
from modulo_reportes import *
from modulo_servicios import *
import datetime

def agregar_venta(datos):
    datos = dict(datos)
    costo = float
    pcosto = float
    venta = {}
    documento = input("Ingrese el documento de usuario: ")
    for i in range(len(datos["usuario"])):
        if datos["usuario"][i]["documento"] == documento:
            op = int(input("Ingrese 1. para comprar produto o 2. para coprar servicio: "))
            if op == 1:
                tipo = input("Ingrese el tipo de producto: ")
                referencia = input("Ingrese la referencia del producto: ")
                for j in range(len(datos["producto"])):
                    if datos["producto"][j]["tipo"] == tipo and datos["producto"][j]["referencia"] == referencia:
                        venta["tipo"] = datos["producto"][j]["tipo"]
                        venta["marca"] = datos["producto"][j]["marca"]
                        venta["referencia"] = datos["producto"][j]["referencia"]
                        venta["cantidad"] = cantidad = int(input("Ingrese la cantidad a vender producto: "))
                        
                        if cantidad <= datos["producto"][j]["cantidad"]:
                            datos["producto"][j]["cantidad"] -= cantidad
                        else:
                            print("--"*10)
                            print("Stock invalido!!")   
                            print("--"*10)
                            break
                        venta["costo"] = datos["producto"][j]["costo"] 
                        venta["costo"] *= cantidad
                        venta["nombre_cliente"] = datos["usuario"][i]["nombre"]
                        venta["documento_cliente"] = datos["usuario"][i]["documento"]
                        numero = int(input("Ingrese el numero de la venta: "))
                        venta["numero"] = numero
                        fecha = datetime.datetime.now()
                        venta["fecha"] = fecha.strftime("%Y-%m-%d %H:%M:%S")
                        venta["fecha_modificacion"] = ""
                        datos["venta"].append(venta)
                        print("--"*13)
                        print("Venta registrado con exito!")
                        print("--"*13)
                        return datos

            elif op == 2:
                tipo = input("Ingrese el tipo de  servicio: ")
                referencia = input("Ingrese la referencia del servicio: ")
                for i in range(len(datos["servicio"])):
                    if datos["servicio"][i]["tipo"] == tipo and datos["servicio"][i]["referencia"] == referencia:
                        venta["tipo"] = datos["servicio"][i]["tipo"]
                        venta["referencia"] = datos["servicio"][i]["referencia"]
                        venta["cantidad"] = cantidad  = int(input("Ingrese la cantidad a vender servicio: "))
                        venta["costo"] = datos["servicio"][i]["costo"] 
                        venta["costo"] *= cantidad
                        venta["nombre_cliente"] = datos["usuario"][i]["nombre"]
                        venta["documento_cliente"] = datos["usuario"][i]["documento"]
                        numero = int(input("Ingrese el numero de la venta: "))
                        venta["numero"] = numero
                        fecha = datetime.datetime.now()
                        venta["fecha"] = fecha.strftime("%Y-%m-%d %H:%M:%S")
                        venta["fecha_modificacion"] = ""
                        datos["venta"].append(venta)
                        print("--"*13)
                        print("Venta registrado con exito!")
                        print("--"*13)
                        return datos
                    
    print("__"*10)
    ahora = datetime.datetime.now()
    dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
    mensaje = "Fallo en agregar venta"
    guardar_txt(dato, mensaje)
    print("Venta invalido!")
    print("__"*10)
    
def buscar_venta(datos):
    datos = dict(datos)
    op = int(input("Buscar por 1. Producto, 2. Servicio: "))
    if op == 1:
        op2 = int(input("Buscar por 1. Tipo venta, 2. Lista venta: "))
        if op2 == 1:
            documento = input("Ingrese el documento del usuario para buscar la venta: ")
            referencia = input("Ingrese la referencia del producto a buscar la venta: ")
            numero = int(input("Ingrese el numero de la venta: "))
            for i in range(len(datos["venta"])):
                if datos["venta"][i]["documento_cliente"] == documento and datos["venta"][i]["referencia"] == referencia and datos["venta"][i]["numero"] == numero:
                    print("__"*10)
                    print("\n""Tipo de producto:",datos["venta"][i]["tipo"],"\n" "Marca de producto:", datos["venta"][i]["marca"],"\n" "Referencia de producto:", datos["venta"][i]["referencia"],"\n""Cantidad de producto:",datos["venta"][i]["cantidad"],"\n" "Costo de producto:",datos["venta"][i]["costo"],"\n" "Nombre de usuario:",datos["venta"][i]["nombre_cliente"],"\n" "Documento cliente:",datos["venta"][i]["documento_cliente"],"\n" "Numero de venta:", datos["venta"][i]["numero"],"\n" "Fecha de venta:", datos["venta"][i]["fecha"],"\n" "Feacha de modificacion venta:", datos["venta"][i]["fecha_modificacion"])
                    print("__"*10)
                    return

        elif op2 == 2:
            while True:
                documento = input("Ingrese el documento del usuario para buscar la venta: ")
                tipo = input("Ingrese el tipo de producto para buscar la venta: ")
                for i in range(len(datos["venta"])):
                    if datos["venta"][i]["documento_cliente"] == documento and datos["venta"][i]["tipo"] == tipo:
                        print("__"*10)
                        print("\n""Tipo de producto:",datos["venta"][i]["tipo"],"\n" "Marca de producto:", datos["venta"][i]["marca"],"\n" "Referencia de producto:", datos["venta"][i]["referencia"],"\n""Cantidad de producto:",datos["venta"][i]["cantidad"],"\n" "Costo de producto:",datos["venta"][i]["costo"],"\n" "Nombre de usuario:",datos["venta"][i]["nombre_cliente"],"\n" "Documento cliente:",datos["venta"][i]["documento_cliente"],"\n" "Numero de venta:", datos["venta"][i]["numero"],"\n" "Fecha de venta:", datos["venta"][i]["fecha"],"\n" "Feacha de modificacion venta:", datos["venta"][i]["fecha_modificacion"])
                        print("__"*10)
                return
    elif op ==2:
        op2 = int(input("Buscar por 1. Tipo venta, 2. Lista venta: "))
        if op2 == 1:
            documento = input("Ingrese el documento del usuario para buscar la venta: ")
            referencia = input("Ingrese la referencia del servicio a buscar la venta: ")
            numero = int(input("Ingrese el numero de la venta: "))
            for i in range(len(datos["venta"])):
                if datos["venta"][i]["documento_cliente"] == documento and datos["venta"][i]["referencia"] == referencia and datos["venta"][i]["numero"] == numero:
                    print("__"*10)
                    print("\n""Tipo de producto:",datos["venta"][i]["tipo"],"\n" "Referencia del servicio:", datos["venta"][i]["referencia"],"\n""Cantidad del servicio:",datos["venta"][i]["cantidad"],"\n" "Costo del servicio:",datos["venta"][i]["costo"],"\n" "Nombre de usuario:",datos["venta"][i]["nombre_cliente"],"\n" "Documento cliente:",datos["venta"][i]["documento_cliente"],"\n" "Numero de venta:", datos["venta"][i]["numero"],"\n" "Fecha de venta:", datos["venta"][i]["fecha"],"\n" "Feacha de modificacion venta:", datos["venta"][i]["fecha_modificacion"])
                    print("__"*10)
                    return
        elif op2 == 2:
            while True:
                documento = input("Ingrese el documento del usuario para buscar la venta: ")
                tipo = input("Ingrese el tipo de servicio para buscar la venta: ")
                for i in range(len(datos["venta"])):
                    if datos["venta"][i]["documento_cliente"] == documento and datos["venta"][i]["tipo"] == tipo:
                    
                        print("__"*10)
                        print("\n""Tipo de producto:",datos["venta"][i]["tipo"],"\n" "Referencia del servicio:", datos["venta"][i]["referencia"],"\n""Cantidad del servicio:",datos["venta"][i]["cantidad"],"\n" "Costo del servicio:",datos["venta"][i]["costo"],"\n" "Nombre de usuario:",datos["venta"][i]["nombre_cliente"],"\n" "Documento cliente:",datos["venta"][i]["documento_cliente"],"\n" "Numero de venta:", datos["venta"][i]["numero"],"\n" "Fecha de venta:", datos["venta"][i]["fecha"],"\n" "Feacha de modificacion venta:", datos["venta"][i]["fecha_modificacion"])
                        print("__"*10)
                return



    print("__"*10)
    ahora = datetime.datetime.now()
    dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
    mensaje = "Fallo en buscar venta"
    guardar_txt(dato, mensaje)
    print("Venta invalido!")
    print("__"*10)


def eliminar_venta(datos):
    datos = dict(datos)
    documento = input("Ingrese el documento de usario  para eliminar venta: ")
    numero = int(input("Ingrese el numero de la venta para eliminar : "))
    for i in range(len(datos["venta"])):
        if datos["venta"][i]["documento_cliente"] == documento and datos["venta"][i]["numero"] == numero:
            datos["venta"].pop(i)
            print("__"*10)
            print("\n""Venta  eliminado!")
            print("__"*10)
            return datos
        
    print("__"*10)
    ahora = datetime.datetime.now()
    dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
    mensaje = "Fallo en eliminar venta"
    guardar_txt(dato, mensaje)
    print("Venta no existe!")
    print("__"*10)
    return datos

def modificar_venta(datos):
    datos = dict(datos)
    op = int(input("Modificar por 1. Tipo Producto, 2. Tipo servicio: "))
    if op == 1:
        documento = input("Ingrese el documento del usuario para modificar la venta: ")
        tipo = input("Ingrese el tipo de producto para modificar la venta: ")
        referencia = input("Ingrese la referencia del producto a modificar la venta: ")
        numero = int(input("Ingrese el numero de la venta: "))
        for i in range(len(datos["venta"])):
            for i in range(len(datos["producto"])):
                if datos["venta"][i]["documento_cliente"] == documento and  datos["venta"][i]["tipo"] == tipo  and datos["venta"][i]["referencia"] == referencia and datos["venta"][i]["numero"] == numero:
                    op2 = int(input("Modificar por 1. Sumar produtos, 2. Restar productos: "))
                    if op2 == 1:
                        cantidad = int(input("Ingrese la cantidad de mas producto para agregar a la venta: "))
                        if cantidad <= datos["producto"][i]["cantidad"]:
                            datos["producto"][i]["cantidad"] -= cantidad
                            datos["venta"][i]["cantidad"] += cantidad
                            datos["venta"][i]["costo"] = datos["producto"][i]["costo"] 
                            datos["venta"][i]["costo"] *= datos["venta"][i]["cantidad"]
                            fecha = datetime.datetime.now()
                            datos["venta"][i]["fecha_modificacion"] = fecha.strftime("%Y-%m-%d %H:%M:%S")
                            print("--"*13)
                            print("Venta modificado con exito!")
                            print("--"*13)
                            return datos
                        
                    elif op2 ==2:
                        cantidad = int(input("Ingrese la cantidad de menos producto para quitarle a la venta: "))
                        for j in range(len(datos["producto"])):
                        
                            if cantidad <= datos["producto"][j]["cantidad"]:
                                datos["producto"][i]["cantidad"] += cantidad
                                datos["venta"][i]["cantidad"] -= cantidad
                                datos["venta"][i]["costo"] = datos["producto"][i]["costo"] 
                                datos["venta"][i]["costo"] *= datos["venta"][i]["cantidad"]
                                fecha = datetime.datetime.now()
                                datos["venta"][i]["fecha_modificacion"] = fecha.strftime("%Y-%m-%d %H:%M:%S")
                                print("--"*13)
                                print("Venta modificado con exito!")
                                print("--"*13)
                                return datos
    elif op == 2:
        documento = input("Ingrese el documento del usuario para modificar la venta: ")
        tipo = input("Ingrese el tipo de servicio para modificar la venta: ")
        referencia = input("Ingrese la referencia del servicio a modificar la venta: ")
        numero = int(input("Ingrese el numero de la venta: "))
        for i in range(len(datos["venta"])):               
            if datos["venta"][i]["documento_cliente"] == documento and datos["venta"][i]["tipo"] == tipo and datos["venta"][i]["referencia"] == referencia and datos["venta"][i]["numero"] == numero:
                datos["venta"][i]["cantidad"] = cantidad = int(input("Ingrese la cantidad de servcios para modificar la venta: "))
                for j in range(len(datos["servicio"])):  
                    datos["venta"][i]["costo"] = datos["servicio"][j]["costo"] 
                    datos["venta"][i]["costo"] *= cantidad
                    fecha = datetime.datetime.now()
                    datos["venta"][i]["fecha_modificacion"] = fecha.strftime("%Y-%m-%d %H:%M:%S")
                    print("--"*13)
                    print("Venta modificado con exito!")
                    print("--"*13)
                    return datos
            
    print("__"*10)
    ahora = datetime.datetime.now()
    dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
    mensaje = "Fallo en modificar venta"
    guardar_txt(dato, mensaje)
    print("Venta no existe!")
    print("__"*10)
    return datos
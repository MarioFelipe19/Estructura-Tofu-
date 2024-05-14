from modulo_ventas import *
from modulo_gestion import *
from modulo_servicios import *
from funciones import *
from cargar_fallos import *
import datetime

def agregar_reclamo(datos):
    datos = dict(datos)
    reclamo = {}
    documento = input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuario"])):
        if datos["usuario"][i]["documento"] == documento:
            reclamo["nombre_cliente"]  = datos["usuario"][i]["nombre"]
            reclamo["documento_cliente"]  = documento
            reclamo["nombre"]  = input("Ingrese el nombre del reclamo: ")
            reclamo["contenido"]  = input("Ingrese el contenido del reclamo: ")
            reclamo["numero"]  = int(input("Ingrese el numero del reclamo: "))
            fecha = datetime.datetime.now()
            reclamo["fecha"] = fecha.strftime("%Y-%m-%d %H:%M:%S")
            reclamo["fecha_modificacion"] = ""
            datos["reclamo"].append(reclamo)
            print("--"*13)
            print("Reclamo registrado con exito!")
            print("--"*13)
            return datos

    print("__"*10)
    ahora = datetime.datetime.now()
    dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
    mensaje = "Fallo en agregar reclamo"
    guardar_txt(dato, mensaje)
    print("Documento invalido!")
    print("Reclamo invalido!")
    print("__"*10)

def buscar_reclamo(datos):
    datos = dict(datos)
    op = int(input("Buscar por 1. Tipo reclamo, 2. Lista reclamos: "))
    if op == 1:
        documento = input("Ingrese el documento del usuario para buscar el reclamo: ")
        numero = int(input("Ingrese el  numero del reclamo: "))
        for i in range(len(datos["reclamo"])):
            if datos["reclamo"][i]["documento_cliente"] == documento and datos["reclamo"][i]["numero"] == numero:
                print("__"*10)
                print("\n""Nombre de usuario:",datos["reclamo"][i]["nombre_cliente"],"\n" "Documento de usuario:", datos["reclamo"][i]["documento_cliente"],"\n""Nombre de reclamo:",datos["reclamo"][i]["nombre"],"\n" "Contenido:",datos["reclamo"][i]["contenido"],"\n" "Numero de la queja:",datos["reclamo"][i]["numero"],"\n" "Fecha de reclamo:", datos["reclamo"][i]["fecha"],"\n" "Feacha de modificacion reclamo:", datos["reclamo"][i]["fecha_modificacion"])
                print("__"*10)
                return
    elif op == 2:
        while True:
            documento = input("Ingrese el documento del usuario para buscar el reclamo: ")
            for i in range(len(datos["reclamo"])):
                if datos["reclamo"][i]["documento_cliente"] == documento:
                    print("__"*10)
                    print("\n""Nombre de usuario:",datos["reclamo"][i]["nombre_cliente"],"\n" "Documento de usuario:", datos["reclamo"][i]["documento_cliente"],"\n""Nombre de reclamo:",datos["reclamo"][i]["nombre"],"\n" "Contenido:",datos["reclamo"][i]["contenido"],"\n" "Numero de la queja:",datos["reclamo"][i]["numero"],"\n" "Fecha de reclamo:", datos["reclamo"][i]["fecha"],"\n" "Feacha de modificacion reclamo:", datos["reclamo"][i]["fecha_modificacion"])
                    print("__"*10)
            return 
            
    print("__"*10)
    ahora = datetime.datetime.now()
    dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
    mensaje = "Fallo en buscar reclamo"
    guardar_txt(dato, mensaje)
    print("Reclamo invalido!")
    print("__"*10)

def eliminar_reclamo(datos):
    datos = dict(datos)
    documento = input("Ingrese el documento de usario  para eliminar reclamo: ")
    numero = int(input("Ingrese el numero de la queja para eliminar reclamo: "))
    for i in range(len(datos["reclamo"])):
        if datos["reclamo"][i]["documento_cliente"] == documento and datos["reclamo"][i]["numero"] == numero:
            datos["reclamo"].pop(i)
            print("__"*10)
            print("\n""Reclamo  eliminado!")
            print("__"*10)
            return datos
        
    print("__"*10)
    ahora = datetime.datetime.now()
    dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
    mensaje = "Fallo en eliminar reclamo"
    guardar_txt(dato, mensaje)
    print("Reclamo no existe!")
    print("__"*10)
    return datos

def modificar_reclamo(datos):
    datos = dict(datos)
    documento = input("Ingrese el documento de usario  para modificar reclamo: ")
    numero = int(input("Ingrese el numero de la queja para modificar reclamo: "))
    for i in range(len(datos["reclamo"])):
        if datos["reclamo"][i]["documento_cliente"] == documento and datos["reclamo"][i]["numero"] == numero:
            datos["reclamo"][i]["nombre"] = input("Ingrese el nuevo nombre de la reclamo: ")
            datos["reclamo"][i]["contenido"] = input("Ingrese el nuevo contenido de la reclamo: ")
            fecha = datetime.datetime.now()
            datos["reclamo"][i]["fecha_modificacion"] = fecha.strftime("%Y-%m-%d %H:%M:%S")
            print("--"*13)
            print("Reclamo modificado con exito!")
            print("--"*13)
            return datos
        
    print("__"*10)
    ahora = datetime.datetime.now()
    dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
    mensaje = "Fallo en modificar reclamo"
    guardar_txt(dato, mensaje)
    print("Reclamo no existe!")
    print("__"*10)
    return datos  

def agregar_sugerencia(datos):
    datos = dict(datos)
    sugerencia = {}
    documento = input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuario"])):
        if datos["usuario"][i]["documento"] == documento:
            sugerencia["nombre_cliente"]  = datos["usuario"][i]["nombre"]
            sugerencia["documento_cliente"]  = documento
            sugerencia["nombre"]  = input("Ingrese el nombre de la sugerencia: ")
            sugerencia["contenido"]  = input("Ingrese el contenido de la sugerencia: ")
            sugerencia["numero"]  = int(input("Ingrese el numero de la sugerencia: "))
            fecha = datetime.datetime.now()
            sugerencia["fecha"] = fecha.strftime("%Y-%m-%d %H:%M:%S")
            sugerencia["fecha_modificacion"] = ""
            datos["sugerencia"].append(sugerencia)
            print("--"*13)
            print("Sugerencia registrado con exito!")
            print("--"*13)
            return datos
    
    print("__"*10)
    ahora = datetime.datetime.now()
    dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
    mensaje = "Fallo en agregar sugerencia"
    guardar_txt(dato, mensaje)
    print("Documento invalido!")
    print("Sugerencia invalido!")
    print("__"*10)

def buscar_sugerencia(datos):
    datos = dict(datos)
    op = int(input("Buscar por 1. Tipo Sugerencia, 2. Lista Sugerencias: "))
    if op == 1:
        documento = input("Ingrese el documento del usuario para buscar la Sugerencia: ")
        numero = int(input("Ingrese el  numero de la Sugerencia: "))
        for i in range(len(datos["sugerencia"])):
            if datos["sugerencia"][i]["documento_cliente"] == documento and datos["sugerencia"][i]["numero"] == numero:
                print("__"*10)
                print("\n""Nombre de usuario:",datos["sugerencia"][i]["nombre_cliente"],"\n" "Documento de usuario:", datos["sugerencia"][i]["documento_cliente"],"\n""Nombre de sugerencia:",datos["sugerencia"][i]["nombre"],"\n" "Contenido:",datos["sugerencia"][i]["contenido"],"\n" "Numero de la sugerencia:",datos["sugerencia"][i]["numero"],"\n" "Fecha de sugerencia:", datos["sugerencia"][i]["fecha"],"\n" "Feacha de modificacion sugerencia:", datos["sugerencia"][i]["fecha_modificacion"])
                print("__"*10)
                return
    elif op == 2:
        while True:
            documento = input("Ingrese el documento del usuario para buscar de la sugerencia: ")
            for i in range(len(datos["sugerencia"])):
                if datos["sugerencia"][i]["documento_cliente"] == documento:
                    print("__"*10)
                    print("\n""Nombre de usuario:",datos["sugerencia"][i]["nombre_cliente"],"\n" "Documento de usuario:", datos["sugerencia"][i]["documento_cliente"],"\n""Nombre de sugerencia:",datos["sugerencia"][i]["nombre"],"\n" "Contenido:",datos["sugerencia"][i]["contenido"],"\n" "Numero de la sugerencia:",datos["sugerencia"][i]["numero"],"\n" "Fecha de sugerencia:", datos["sugerencia"][i]["fecha"],"\n" "Feacha de modificacion sugerencia:", datos["sugerencia"][i]["fecha_modificacion"])
                    print("__"*10)
            return
                
        
    print("__"*10)
    ahora = datetime.datetime.now()
    dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
    mensaje = "Fallo en buscar sugerencia"
    guardar_txt(dato, mensaje)
    print("Sugerencia invalido!")
    print("__"*10)
        
def eliminar_sugerencia(datos):

    datos = dict(datos)
    documento = input("Ingrese el documento de usario  para eliminar sugerencia: ")
    numero = int(input("Ingrese el numero de la sugerencia para eliminar : "))
    for i in range(len(datos["sugerencia"])):
        if datos["sugerencia"][i]["documento_cliente"] == documento and datos["sugerencia"][i]["numero"] == numero:
            datos["sugerencia"].pop(i)
            print("__"*10)
            print("\n""Sugerencia  eliminado!")
            print("__"*10)
            return datos
        
    print("__"*10)
    ahora = datetime.datetime.now()
    dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
    mensaje = "Fallo en eliminar sugerencia"
    guardar_txt(dato, mensaje)
    print("Sugerencia no existe!")
    print("__"*10)
    return datos

def modificar_sugerencia(datos):
    datos = dict(datos)
    documento = input("Ingrese el documento de usario  para modificar la sugerencia: ")
    numero = int(input("Ingrese el numero de la queja para modificar la sugerencia: "))
    for i in range(len(datos["sugerencia"])):
        if datos["sugerencia"][i]["documento_cliente"] == documento and datos["sugerencia"][i]["numero"] == numero:
            datos["sugerencia"][i]["nombre"] = input("Ingrese el nuevo nombre de la sugerencia: ")
            datos["sugerencia"][i]["contenido"] = input("Ingrese el nuevo contenido de la sugerencia: ")
            fecha = datetime.datetime.now()
            datos["sugerencia"][i]["fecha_modificacion"] = fecha.strftime("%Y-%m-%d %H:%M:%S")
            print("--"*13)
            print("sugerencia modificado con exito!")
            print("--"*13)
            return datos
        
    print("__"*10)
    ahora = datetime.datetime.now()
    dato = ahora.strftime("%Y-%m-%d %H:%M:%S")
    mensaje = "Fallo en modificar sugerencia"
    guardar_txt(dato, mensaje)
    print("sugerencia no existe!")
    print("__"*10)
    return datos 


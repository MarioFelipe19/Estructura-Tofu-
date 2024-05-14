
from modulo_ventas import *
from modulo_reportes import *
from modulo_servicios import *


def agregar_usuario(datos):
    datos = dict(datos)
    usuario = {}
    usuario["nombre"] = input("Ingrese el nombre: ")
    usuario["documento"] = input("Ingrese el documento: ")
    usuario["direccion"] = input("Ingrese la direccion: ")
    usuario["telefono"] = input("Ingrse el telefono de contacto: ")
    
    try:
        usuario["edad"] = int(input("Ingrese la edad: "))
    except Exception:
        usuario["edad"] = 18
    print("Ingrese 1: si es cliente nuevo, 2: si es cliente regular, 3: si es cliente leal ")
    op = int(input("Ingrese la opcion: "))
    if op == 1:
        usuario["categoria"] = 1
    elif op == 2:
        usuario["categoria"] = 2
    elif op == 3:
        usuario["categoria"] = 3

    usuario["promocion"] = ""
    usuario["costo"] = 0

    datos["usuario"].append(usuario)
    print("--"*13)
    print("Usuario registrado con exito!")
    print("--"*13)
    return datos

def buscar_usuario(datos):
    datos = dict(datos)
    op = int(input("Buscar por 1. Tipo Usuario, 2. Lista Usuario: "))
    if op == 1:
        documento = input("Ingrese el documento del usuario a buscar: ")
        for i in range(len(datos["usuario"])):
            for j in range(len(datos["venta"])):
                if datos["usuario"][i]["documento"] == documento:
                    print("__"*10)
                    print("\n""Nombre:",datos["usuario"][i]["nombre"],"\n" "Edad:", datos["usuario"][i]["edad"],"\n""Documento:",datos["usuario"][i]["documento"],"\n" "Direccion:",datos["usuario"][i]["direccion"],"\n" "Telefono:",datos["usuario"][i]["telefono"],"\n" "Categoria:",datos["usuario"][i]["categoria"],"\n""--------------" "\n""Tienes una promocion de :",datos["usuario"][i]["promocion"],"\n" "Con costo de :",datos["usuario"][i]["costo"])
                    print("__"*10)
                    return 
    elif op == 2:
        while True:
            for i in range(len(datos["usuario"])):
                print("__"*10)
                print("\n""Nombre:",datos["usuario"][i]["nombre"],"\n" "Edad:", datos["usuario"][i]["edad"],"\n""Documento:",datos["usuario"][i]["documento"],"\n" "Direccion:",datos["usuario"][i]["direccion"],"\n" "Telefono:",datos["usuario"][i]["telefono"],"\n" "Categoria:",datos["usuario"][i]["categoria"],"\n" "Tienes una promocion de :",datos["usuario"][i]["promocion"],"\n" "Con costo de :",datos["usuario"][i]["costo"])
                print("__"*10)
            return 

    print("__"*10)
    print("Documento invalido!")
    print("__"*10)
            
def eliminar_usuario(datos):
    datos = dict(datos)
    documento = input("Ingrese el docuemto del usuario a eliminar: ")
    for i in range(len(datos["usuario"])):
        if datos["usuario"][i]["documento"] == documento:
            datos["usuario"].pop(i)
            print("__"*10)
            print("Usuario eliminado!")
            print("__"*10)
            return datos
        
    print("__"*10)
    print("Usuario no existe!")
    print("__"*10)
    return datos
            
def modificar_usuario(datos):
    datos = dict(datos)
    documento = input("Ingrese el docuemto del usuario a modificar: ")
    for i in range(len(datos["usuario"])):
        if datos["usuario"][i]["documento"] == documento:
            datos["usuario"][i]["nombre"] = input("Ingrese el nombre: ")
            datos["usuario"][i]["direccion"] = input("Ingrese la direccion: ")
            datos["usuario"][i]["telefono"] = input("Ingrse el telefono de contacto: ")
            datos["usuario"][i]["edad"]  = int(input("Ingrese la edad: "))
            print("Ingrese 1: si es cliente nuevo, 2: si es cliente regular, 3: si es cliente leal ")
            datos["usuario"][i]["categoria"] = int(input("Ingrese la categoria: "))
            print("--"*13)
            print("usuario modificado con exito!")
            print("--"*13)
            return datos
        
    print("__"*10)
    print("Usuario no existe!")
    print("__"*10)
    return datos
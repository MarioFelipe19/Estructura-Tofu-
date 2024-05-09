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

    datos["usuario"].append(usuario)
    print("--"*13)
    print("\n""usuario registrado con exito!")
    print("--"*13)
    return datos

def buscar_usuario(datos):
    datos = dict(datos)
    documento = input("Ingrese el documento del usuario a buscar: ")
    for i in range(len(datos["usuario"])):
        if datos["usuario"][i]["documento"] == documento:
            print("__"*10)
            print("\n""Nombre:",datos["usuario"][i]["nombre"],"\n" "Edad:", datos["usuario"][i]["edad"],"\n""Documento:",datos["usuario"][i]["documento"],"\n" "Direccion:",datos["usuario"][i]["direccion"],"\n" "Telefono:",datos["usuario"][i]["telefono"],"\n" "Categoria:",datos["usuario"][i]["categoria"])
            print("__"*10)
            return 
        
    print("__"*10)
    print("\n""Documento invalido!")
    print("__"*10)
            

def eliminar_usuario(datos):
    datos = dict(datos)
    documento = input("Ingrese el docuemto del usuario a eliminar: ")
    for i in range(len(datos["usuario"])):
        if datos["usuario"][i]["documento"] == documento:
            datos["usuario"].pop(i)
            print("__"*10)
            print("\n""Usuario eliminado!")
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
            print("\n""usuario modificado con exito!")
            print("--"*13)
            return datos
        
    print("__"*10)
    print("Usuario no existe!")
    print("__"*10)
    return datos
            


def agregar_producto():
    print("hola13")

def buscar_producto():
    print("hola14")

def eliminar_producto():
    print("hola15")

def modificar_producto():
    print("hola16")

def agregar_servicio():
    print("hola17")

def buscar_servicio():
    print("hola18")

def eliminar_servicio():
    print("hola19")

def modificar_servicio():
    print("hola20")

def agregar_reclamo():
    print("hola5")

def buscar_reclamo():
    print("hola6")

def eliminar_reclamo():
    print("hola7")

def modificar_reclamo():
    print("hola8")

def agregar_sugerencia():
    print("hola9")

def buscar_sugerencia():
    print("hola10")

def eliminar_sugerencia():
    print("hola11")

def modificar_sugerencia():
    print("hola12")

def agregar_venta():
    print("hola21")

def buscar_venta():
    print("hola22")

def eliminar_venta():
    print("hola23")

def modificar_venta():
    print("hola24")
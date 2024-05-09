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
    try:
        op = int(input("Ingrese la opcion: "))
    except Exception:
        if op == 1:
            usuario["categoria"] = 1
        elif op == 2:
            usuario["categoria"] = 2
        elif op == 3:
            usuario["categoria"] = 3
    datos["usuario"].append(usuario)
    print("--"*13)
    print("usuario registrado con exito!")
    print("--"*13)
    return datos

def buscar_usuario():
    print("hola2")

def eliminar_usuario():
    print("hola3")

def modificar_usuario():
    print("hola4")

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
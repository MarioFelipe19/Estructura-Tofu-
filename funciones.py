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
    print("usuario registrado con exito!")
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
        for i in range(len(datos["producto"])):
            if datos["producto"][i]["tipo"] == tipo:
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
        for i in range(len(datos["servicio"])):
            if datos["servicio"][i]["tipo"] == tipo:
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
    referencia = input("Ingrese la referencia del producto a modificar: ")
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
            datos["reclamo"].append(reclamo)
            print("--"*13)
            print("Reclamo registrado con exito!")
            print("--"*13)
            return datos

    print("__"*10)
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
                print("\n""Nombre de usuario:",datos["reclamo"][i]["nombre_cliente"],"\n" "Documento de usuario:", datos["reclamo"][i]["documento_cliente"],"\n""Nombre de reclamo:",datos["reclamo"][i]["nombre"],"\n" "Contenido:",datos["reclamo"][i]["contenido"],"\n" "Numero de la queja:",datos["reclamo"][i]["numero"])
                print("__"*10)
                return
    elif op == 2:
        while True:
            documento = input("Ingrese el documento del usuario para buscar el reclamo: ")
            for i in range(len(datos["reclamo"])):
                if datos["reclamo"][i]["documento_cliente"] == documento:
                    print("__"*10)
                    print("\n""Nombre de usuario:",datos["reclamo"][i]["nombre_cliente"],"\n" "Documento de usuario:", datos["reclamo"][i]["documento_cliente"],"\n""Nombre de reclamo:",datos["reclamo"][i]["nombre"],"\n" "Contenido:",datos["reclamo"][i]["contenido"],"\n" "Numero de la queja:",datos["reclamo"][i]["numero"])
                    print("__"*10)
                return 
            
    print("__"*10)
    print("Reclamo invalido!")
    print("__"*10)




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
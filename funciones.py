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
            print("--"*13)
            print("Reclamo modificado con exito!")
            print("--"*13)
            return datos
        
    print("__"*10)
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
            datos["sugerencia"].append(sugerencia)
            print("--"*13)
            print("Sugerencia registrado con exito!")
            print("--"*13)
            return datos
    
    print("__"*10)
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
                print("\n""Nombre de usuario:",datos["sugerencia"][i]["nombre_cliente"],"\n" "Documento de usuario:", datos["sugerencia"][i]["documento_cliente"],"\n""Nombre de sugerencia:",datos["sugerencia"][i]["nombre"],"\n" "Contenido:",datos["sugerencia"][i]["contenido"],"\n" "Numero de la sugerencia:",datos["sugerencia"][i]["numero"])
                print("__"*10)
                return
    elif op == 2:
        while True:
            documento = input("Ingrese el documento del usuario para buscar de la sugerencia: ")
            for i in range(len(datos["sugerencia"])):
                if datos["sugerencia"][i]["documento_cliente"] == documento:
                    print("__"*10)
                    print("\n""Nombre de usuario:",datos["sugerencia"][i]["nombre_cliente"],"\n" "Documento de usuario:", datos["sugerencia"][i]["documento_cliente"],"\n""Nombre de sugerencia:",datos["sugerencia"][i]["nombre"],"\n" "Contenido:",datos["sugerencia"][i]["contenido"],"\n" "Numero de la sugerencia:",datos["sugerencia"][i]["numero"])
                    print("__"*10)
                return
                
        
    print("__"*10)
    print("Sugerencia invalido!")
    print("__"*10)
        
def eliminar_sugerencia(datos):

    datos = dict(datos)
    documento = input("Ingrese el documento de usario  para eliminar sugerencia: ")
    numero = int(input("Ingrese el numero de la queja para eliminar sugerencia: "))
    for i in range(len(datos["sugerencia"])):
        if datos["sugerencia"][i]["documento_cliente"] == documento and datos["sugerencia"][i]["numero"] == numero:
            datos["sugerencia"].pop(i)
            print("__"*10)
            print("\n""Sugerencia  eliminado!")
            print("__"*10)
            return datos
        
    print("__"*10)
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
            print("--"*13)
            print("sugerencia modificado con exito!")
            print("--"*13)
            return datos
        
    print("__"*10)
    print("sugerencia no existe!")
    print("__"*10)
    return datos 

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
                        
                        if cantidad < datos["producto"][j]["cantidad"]:
                            datos["producto"][j]["cantidad"] -= cantidad
                        else:
                            print("--"*10)
                            print("Stock invalido!!")   
                            print("--"*10)
                            break
                        venta["costo"] = datos["producto"][j]["costo"] 
                        venta["costo"] *= cantidad
                        venta["nombre_cliente"] = datos["usuario"][i]["nombre"]
                        venta["docuemento_cliente"] = datos["usuario"][i]["documento"]
                        numero = int(input("Ingrese el numero de la venta: "))
                        venta["numero"] = numero
                        datos["venta"].append(venta)
                        print("--"*13)
                        print("Venta registrado con exito!")
                        print("--"*13)
                        return datos

            elif op == 2:
                tipo = input("Ingrese el servicio: ")
                for i in range(len(datos["servicio"])):
                    if datos["servicio"][i]["tipo"] == tipo:
                        venta["tipo"] = datos["servicio"][i]["tipo"]
                        venta["referencia"] = datos["servicio"][i]["referencia"]
                        venta["cantidad"] = cantidad  = int(input("Ingrese la cantidad a vender servicio: "))
                        venta["costo"] = datos["servicio"][i]["costo"] 
                        venta["costo"] *= cantidad
                        venta["nombre_cliente"] = datos["usuario"][i]["nombre"]
                        venta["docuemento_cliente"] = datos["usuario"][i]["documento"]
                        numero = int(input("Ingrese el numero de la venta: "))
                        venta["numero"] = numero
                        datos["venta"].append(venta)
                        print("--"*13)
                        print("Venta registrado con exito!")
                        print("--"*13)
                        return datos
                    
        print("__"*10)
        print("Sugerencia invalido!")
        print("__"*10)
    
def buscar_venta(datos):
    datos = dict(datos)
    op = int(input("Buscar por 1. Producto, 2. Servicio: "))
    if op == 1:
        op2 = int(input("Buscar por 1. Tipo venta, 2. Lista venta: "))
        if op2 == 1:
            documento = input("Ingrese el documento del usuario para buscar la venta: ")
            referencia = input("Ingrese la referencia del producto a buscar la venta: ")
            numero = input("Ingrese el numero de la venta: ")
            for i in range(len(datos["venta"])):
                if datos["venta"][i]["documento_cliente"] == documento and datos["venta"][i]["referencia"] == referencia and datos["venta"][i]["numero"] == numero:
                    print("__"*10)
                    print("\n""Tipo de producto:",datos["venta"][i]["tipo"],"\n" "Referencia de producto:", datos["venta"][i]["referencia"],"\n""Cantidad de producto:",datos["venta"][i]["cantidad"],"\n" "Costo de producto:",datos["venta"][i]["costo"],"\n" "Nombre de usuario:",datos["venta"][i]["nombre_cliente"],"\n" "Documento cliente:",datos["venta"][i]["docuemento_cliente"])
                    print("__"*10)
                    return


def eliminar_venta():
    print("hola23")

def modificar_venta():
    print("hola24")
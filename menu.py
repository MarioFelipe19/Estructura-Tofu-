def menu_principal():
    print("=="* 20)
    print("\t")
    print("Ingrese la opción")
    print("1. Para registrar usuario")
    print("2. Para bucascar usuario")
    print("3. Para eliminar usuario")
    print("4. Para modificar usuari")
    print("5. Para consultar servicios")
    print("6. Para agregar reclamacion")
    print("7. Para agregar sugerencias")
    print("8. Para Registrar producto")
    print("9. Para Registar venta de producto")
    print("10. para salir")
    print("\t")
    print("=="* 20)

def pedir_opcion():
    try:
        
        op = int(input("Ingrese su opcion: "))
        
        
        return op
        
    except Exception:
        print("--"*20)
        print("valor invalido")
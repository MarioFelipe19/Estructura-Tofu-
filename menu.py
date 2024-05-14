def menu_principal():
    print("")
    print("=="* 20)
    print("          Estructura(Tofu)")
    print("=="* 20)
    print("")
    print("     1. Módulo de Gestión")
    print("     2. Módulo de Servicios")
    print("     3. Módulo de Reportes")
    print("     4. Módulo de Venta")
    print("     5. Salir")
    print("=="* 20)
    print("")
def menu_gestion():
    print("="*10 +" Modulo de Gestion "+ "="*10)
    print("     1. Agregar Usuario")
    print("     2. Buscar Usuario")
    print("     3. Eliminar Usuario")
    print("     4. Modificar Usuario")
    print("     5. Salir")
    print("=="* 20)
    print("")
def menu_servcio():
    print("="*10 +" Modulo de Servicios "+ "="*10)
    print("     1. Agregar Producto")
    print("     2. Buscar Producto")
    print("     3. Eliminar Producto")
    print("     4. Modificar Producto")
    print("     5. Agregar Servicio")
    print("     6. Buscar Servicio")
    print("     7. Eliminar Servicio")
    print("     8. Modificar Servicio")
    print("     9. Agregar Promoción")
    print("    10. Buscar Promoción")
    print("    11. Eliminar Promoción")
    print("    12. Modificar Promoción")
    print("    13. Salir")
    print("=="* 20)
    print("")
def menu_reportes():    
    print("="*10 +" Modulo de Reportes "+ "="*10)
    print("    1. Agregar Reclamo")
    print("    2. Buscar Reclamo")
    print("    3. Eliminar Reclamo")
    print("    4. Modificar Reclamo")
    print("    5. Agregar Sugerencia")
    print("    6. Buscar Sugerencia")
    print("    7. Eliminar Sugerencia")
    print("    8. Modificar Sugerencia")
    print("    9. Salir")
    print("=="* 20)
    print("")
def menu_ventas():
    print("="*10 +"  Modulo de Ventas "+ "="*10)
    print("    1. Agregar Venta")
    print("    2. Buscar Venta")
    print("    3. Eliminar Venta")
    print("    4. Modificar Venta")
    print("    5. Salir")
    print("=="* 20)
    
    

def pedir_opcion():
    try:
        print("//"*20)
        op = int(input("  Ingrese su opcion: "))
        print("//"*20)
        
        return op
        
    except Exception:
        print("--"*20)
        print("valor invalido")
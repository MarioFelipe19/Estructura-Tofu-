

file = open("fallos.txt", "r")
print(file.read)
file.close()

def guardar_txt(dato, mensaje): 
    dato_c = dato + " " + mensaje
    with open("fallos.txt", "a") as file:
        file.write(dato_c + '\n')
    file.close()
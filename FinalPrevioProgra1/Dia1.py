"""
repaso de archivos:

"""

arch = open("prueba.txt","wt")

try : 
    arch
    prueba = input("algo?(ENTER para terminar):")
    while prueba != "":
        nombre = input("Nombre?")
        arch.write(prueba+':'+nombre+'\n')
        prueba = input("algo? (ENTER para terminar):")
    print("Archivo creado correctamente.")

except OSError as mensaje:
    print("no se puede abrir", mensaje)

finally:
    try:
        arch.close()
    except NameError:
        pass

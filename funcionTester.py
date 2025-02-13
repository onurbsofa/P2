


def validar_dato(valor, minimo, maximo):
    if minimo != None and valor < minimo:
        print("Error: El valor debe ser mayor o igual a " , minimo)
        return False
    if maximo != None and valor > maximo:
        print("Error: El valor debe ser menor o igual a ", maximo)
        return False
    return True


def main():
    dato = int(input(print("Ingrese un valor:")))

    validar_dato(dato, 0, 10)

if __name__ == '__main__':
    main()
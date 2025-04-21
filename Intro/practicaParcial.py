
def busqueda(listaBus,elem):
    pos = -1
    i = 0
    while pos == -1 and i < len(listaBus):
        if listaBus[i] == elem:
            pos = i
        i += 1
    return pos

def cargaDatos(dato, lista):
    


def main():
    listarandom = [1,2,3,4]
    busco = 4
    
    print(busqueda(listarandom,busco))
    


if __name__ == "__main__":
    main()
    
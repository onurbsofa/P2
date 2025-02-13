"""
Zoologico de mutantes:
Este sistema administra un zoologico de mutantes dividido en 6 sectores.
Cada mutante tiene un ID unico, tipo de mutacion, nivel de poder y clasificacion.
El sistema permite realizar las siguientes operaciones:
1. Ingresar un nuevo mutante.
2. Buscar mutantes por ID.
3. Ordenar mutantes por nivel de poder.
4. Encontrar mutante con nivel de poder maximo o minimo.
5. Mostrar todos los mutantes.
6. Cosultar la cantidad de mutantes por sector.
7. Salir del sistema.

"""

import random


def buscar(id, li):
    pos = -1
    i = 0
    while pos == -1 and i<len(li):
        if li[i] == id:
            pos += 1
        i+= 1
    return pos

def validarNivel(nivel):
    if nivel > 1 or nivel < 6:
        return False
    return True

def catalogoTipos():
    tipos = ['Garrras','Garras Metal','Volador','Regeneracion','Teletransportacion','Psiquico','Super Fuerta','Transformacion','Omega']

    print('que tipo de mutante es?')
    for i in range(len(tipos)):
        print(f'{i + 1}.{tipos[i]}')
    tipoelegiod = int(input('Ingrese el numero del tipo que coinicide con su mutante: '))
    return tipos[tipoelegiod - 1]



def ingresarMutante(ids,niveles,tipos,sectores,pseudonimos):
    pseudonimomut = input('ingrese el nombre del mutante: ')
    pseudonimos.append(pseudonimomut)

    id_unico = random.randint(100,999)
    while buscar(id_unico,ids) != -1:
        id_unico = random.randint(100,999)
    
    ids.append(id_unico)
    
    nivelMut = int(input('Ingrese el nivel del mutante que desea ingresar(de 1 a 6 posibles): '))
    while validarNivel(nivelMut) == False:
        nivelMut = int(input('El nivel debe ser de 1 a 6: '))
        validarNivel(nivelMut)
    niveles.append(nivelMut)
    sectores[nivelMut - 1] += 1
    
    tipomut = catalogoTipos()
    tipos.append(tipomut)

    print('--------')
    print(f'nombre:{pseudonimomut}')
    print(f'tipo:{tipomut}')
    print(f'id:{id_unico}')
    print(f'nivel:{nivelMut}')
    print(f'sector:{nivelMut}')
    print('---------')
    print(f'sectores:{sectores}')
    print('---------')
    
def mostrarMenu():
    print('----menu-----')
    print('1. ingresar un mutante al zoologico')
    print('7. salir')
    print('--------------')
    

def opciones():
    print(int(input("")))

def main():
    sectores = [0]*6
    tipos = []
    niveles = []
    ids = []
    pseudonimos = []

    opcion = 0
    
    while opcion != 7:
        mostrarMenu()
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            ingresarMutante(ids,niveles,tipos,sectores,pseudonimos)
        elif opcion != 7:
           print("Opción no válida, por favor intente de nuevo.")

    print("Saliendo del sistema...")


if __name__ == "__main__":
    main()


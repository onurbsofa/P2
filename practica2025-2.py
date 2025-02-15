# practicando listas paralelas, sintaxis y algoritmos basicos
# ejercicio finalPrevio(parecido):
"""Crear un programa para votar series 
    - primero cargar los codigos de las series sin duplicados 
    - consultar por condigo de serie la puntuacion y almacenarlo
    - imprimir en consola el resultado como una tabla 
    - devolver la mejor calificada
"""
import random

def mayorPuntaje(arr):
    mayor = arr[0]
    for i in range(len(arr)):
        if mayor < arr[i]:
            mayor = arr[i]
    return mayor


def validacionInput(li,ls,msj):
    valor = int(input(msj))
    while valor < li or valor > ls:
        valor = int(input('valor fuera de rango, de nuevo: '))
    return valor

def busquedaSecuencial(lista,elem):
    i = 0
    pos = -1
    while i < len(lista) and pos == -1:
        if lista[i] == elem:
            pos = i
        i += 1
    return pos 

def loadingCodes(lista,cantidadCod):
    i = 0
    while i < cantidadCod:
        codAux =  random.randint(100,105)
        posicion = busquedaSecuencial(lista,codAux)
        if posicion == -1:
           lista.append(codAux)
           i += 1
        else:
            print('codigo repetido')
    print('lista cargada')
    print(lista)

def mostrarPuntaje(li1,li2):
    print(' *** Tabla puntajes *** ')
    print('Codigos \t Estrellas')
    for i in range(len(li1)):
        print("%7d \t %8d" % (li1[i],li2[i]))
    print(mayorPuntaje(li2))


def main():
    codSeries = []
    stars = []

    loadingCodes(codSeries,5)
    for i in range(len(codSeries)):
        print(codSeries[i])
        puntuacion = validacionInput(1,5,'introdzca un valor de 1 a 5 estrellas')
        stars.append(puntuacion)
    mostrarPuntaje(codSeries,stars)

#1 ejecuicion del main
if __name__ == '__main__':
    main()
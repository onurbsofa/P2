"""parcial: 
un gimnasio ofrece membresias para distintas actividades durante todo el año.
el gimnasion cuenta con diez actividades distintas, codificadas del 1 al 10.
Las actividades del 1 al 9 tienen 25 cupos disponibles cada una mientras que la actividad numero 10 tiene 50 cupos disponibles.
el costo de la membresia anual por persona es de $6000.
Durante el proceso de isncirpcion, se registran las solicitudes de membresias:
 - Actividad(1 y 10) -> debe validar este ingreso de dato.
 - cantidad de miembros que desea inscribir(valor mayor a cero)-> debe validar este ingreso de dato. no podra inscribir mas miembros
     en una actividad que ya esta llena,emitir un mensaje de error.
la carga finaliza con una actividad 0.

"""
import random


def busqueda(elem,lista):
    pos = -1
    i = 0
    while pos == -1 and i<len(lista):
        if lista[i] == elem:
            pos = i
        i+= 1
    return pos


def ingresoValidacion(li,ls,msj):
    valor = int(input(msj))
    while valor<li or valor>ls:
        valor = int(input(msj))
    return valor

def cargarMiembros(miembros, act,lista):
    index = act -1
    lista[index].append(miembros)
    
        
def suma(lista):
    resul = 0
    for i in range(len(lista)):
        resul += lista[i]
    return resul

def promedio(lista):
    return suma(lista) / len(lista)

    
def mostrarInscripciones(liAct):
    print("*** listado inscripciones por actividad***")
    print("actividad\inscriptos")
    
    for i in range(len(liAct)):
        print((i,liAct[i]))
    
    

def main():
    ACTIVIDADES = [0]*10
    print(len(ACTIVIDADES))
    
    #carga
    auxAct = -1
    while auxAct != 0 and auxAct < len(ACTIVIDADES):
        auxAct = ingresoValidacion(1,10,'ingrese una actividad de uno a diez')
        if auxAct > 10:
            miembros = ingresoValidacion(1,25,'ingrese la cantidad de miembros que desea inscribir')
        miembros = ingresoValidacion(1,50,'ingrese la cantidad de miembros que desea inscribir')
        print(auxAct)
        cargarMiembros(miembros, auxAct,ACTIVIDADES)
    print(promedio(ACTIVIDADES))
    print(mostrarInscripciones(ACTIVIDADES))    
    
    #procesamiento
    
    
    #mostrar

if __name__ == "__main__":
    main()
    
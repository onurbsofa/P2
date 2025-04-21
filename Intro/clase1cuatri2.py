"""
Vamos a repasar...

1) Realizar una funcion cargaListas que reciba una
lista de legajos y una lista de notas y realice 
la carga random SIN DUPLICADOS de los numeros de legajos
(4 digitos) y las notas (1-10) de los
50 alumnos que conforman la comision

2) Informe la nota maxima que se obtuvo en la comision ,
indicando el numero de legajo - Funcion 
informaMaximo

3) Indicar cuales legajos corresponden a la nota minima de los alumnos
- Funcion informaMinimos

4) Indicar la nota promedio de los alumnos - El calculo de la nota
promedio realizarlo en una funcion 
PROMEDIO , informar la nota en el programa principal
"""

import random


def busquedaSecuencial(lista,valorBuscado):
    i=0
    pos=-1
    while pos==-1 and i<len(lista):
        if lista[i]== valorBuscado:
            pos=i
        else:
            i+=1
    return pos

        
def cargaListas(legajos,notas):
    
    while len(legajos)<50:
        auxLeg = random.randint(1000, 9999)
        posicion=busquedaSecuencial(legajos,auxLeg)
        if posicion==-1:
            legajos.append(auxLeg)
            notas.append(random.randint(1,10))
    
    print(legajos)
    print(notas)
    
def maximo(lista):
    for i in range(len(lista)):
        if i==0 or lista[i]>valMax:
            valMax=lista[i]
    return valMax

def minimo(lista):
    for i in range(len(lista)):
        if i==0 or lista[i]<valMin:
            valMin=lista[i]
    return valMin

def informaMaximo(legajos, notas):
    max_nota = maximo(notas)
    
    for i in range(len(notas)):
        if notas[i]==max_nota:
            legajo_max=legajos[i]

    return max_nota, legajo_max

def informaMinimos(legajos, notas):
    min_nota = minimo(notas)
    print("La nota minima es ",min_nota)
    for i in range(len(legajos)):
        if notas[i]==min_nota:
            print("LEGAJO CON NOTA MINIMA ->",legajos[i])
    

def promedio(notas):
    suma=0
    for i in range(len(notas)):
        suma+=notas[i]
    
    return suma / len(notas)

# Programa principal
legajos=[]
notas=[]
cargaListas(legajos,notas)

max_nota, legajo_max = informaMaximo(legajos, notas)
print(f"Nota máxima: {max_nota} - Legajo: {legajo_max}")

informaMinimos(legajos, notas)

promedio_notas = promedio(notas)
print(f"Nota promedio: {promedio_notas:.2f}")
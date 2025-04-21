"""
Ejercicio 8: Rellenar una lista con números enteros entre 0 y 100
obtenidos al azar
e imprimir el valor mínimo y el lugar que ocupa. Tener en cuenta
que el mínimo puede 
estar repetido, en cuyo caso deberán mostrarse todas las
posiciones en las que 
se encuentre. La carga de datos termina cuando se obtenga un 0
como número 
al azar, el que no deberá cargarse en la lista.
"""

import random

def cargarLista(inicio,fin):
    li=[]
    nro=random.randint(inicio,fin)
    while nro!=0:
        li.append(nro)
        nro=random.randint(inicio,fin)
    return li

def minimo(li):
    for i in range(len(li)):
        if i==0 or li[i]<valMin:
            valMin=li[i]
    return valMin
    
def main():
    
    LISTA=cargarLista(0,100)
    print(LISTA)
    if len(LISTA)>0:
        valorMinimo=minimo(LISTA)
        print("El valor minimo es ",valorMinimo)
        for i in range(len(LISTA)):
            if LISTA[i]==valorMinimo:
                print("Se encuentra en posicion ",i)
            
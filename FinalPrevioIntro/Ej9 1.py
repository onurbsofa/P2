"""
Crear una lista de N números generados al azar entre 0 y 100 pero sin elementos
repetidos. El valor de N se ingresa por teclado. Resolver este problema utilizando
dos estrategias distintas:
· Impidiendo el agregado de elementos repetidos
· Eliminando los duplicados luego de generar la lista. Asegurarse que la
cantidad final de elementos sea la solicitada.
"""

import random

def cargarLista(lista,inicio,fin):
    i = 0
    N = int(input("Ingresar la cantidad de elementos de la lista: "))
    while N<=0:
        N = int(input("Ingresar la cantidad de elementos de la lista: "))
    
    while i<N:
        nro = random.randint(inicio,fin)
        posicion = busqueda(lista,nro)
        if (posicion==-1):
            lista.append(nro)
            i+=1

def busqueda(lista, nro):
    pos = -1
    i = 0
    while i<len(lista) and pos==-1:
        if lista[i] == nro:
            pos = i
        i+=1
    
    return pos
    
def main():
    LISTA=[]
    cargarLista(LISTA,0,100)
    print(LISTA)
    
if __name__=="__main__":
    main()
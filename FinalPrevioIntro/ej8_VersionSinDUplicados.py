"""
Ejercicio 8: Rellenar una lista con números
enteros entre 0 y 100 obtenidos al azar
SIN DUPLICADOS!
e imprimir el valor mínimo y el lugar que
ocupa.
La carga de datos termina cuando se obtenga
un 0 como número 
al azar, el que no deberá cargarse en la lista.
"""
import random

def cargarLista(li,inicio,fin):
    nro=random.randint(inicio,fin)
    while nro!=0:
        posicion=busqueda(li,nro)
        if posicion==-1:
            li.append(nro)
        else:
            print("El ",nro," se encuentra duplicado")
        nro=random.randint(inicio,fin)
    
def busqueda(lista,valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i<(len(lista)):
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos
    
      
def minimo(li):
    for i in range(len(li)):
        if i==0 or li[i]<valMin:
            valMin=li[i]
    return valMin
    
def main():
    LISTA=[]
    cargarLista(LISTA,0,100)
    print(LISTA)
    if len(LISTA)>0:
        valorMinimo=minimo(LISTA)
        print("El valor minimo de la lista es ",valorMinimo)
        
if __name__=="__main__":
    main()


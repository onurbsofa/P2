import random


def busqueda(lista,valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i<len(lista):
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos
    
    
def cargaListas(liLe,liNo):
    i=0
    N=int(input("Ingrese la cantidad de alumnos del curso"))
    while N<=0:
        N=int(input("Ingrese la cantidad de alumnos del curso"))
    
    while i<N:
        auxLegajo=random.randint(1000,9999)
        
        posicion=busqueda(liLe,auxLegajo)
        if posicion==-1:
            liLe.append(auxLegajo)
            liNo.append(random.randint(0,10))
            i+=1
        else:
            print("Legajo duplicado!")
        
def mostrarListas(liLe,liNo):
    print("---------------------------")
    print("\tLISTADO DE ALUMNOS")
    print("---------------------------")
    print("LEGAJOS\tNOTAS")
    for i in range(len(liLe)):
        print("%7d\t%5d" %(liLe[i],liNo[i]))
   
def consultaNotas(liLe,liNo):
    auxLeg=int(input("Ingrese el legajo que desea consultar"))
    while auxLeg !=0:
        pos=busqueda(liLe,auxLeg)
        if pos!=-1:
            print("La nota del alumno es ", liNo[pos])
        else:
            print("Legajo inexistente")
        
        auxLeg=int(input("Ingrese el legajo que desea consultar"))
        
        
def maximo(lista):
    for i in range(len(lista)):
        if i==0 or lista[i]>valMax:
            valMax=lista[i]
    return valMax
    
    
    
def main():
    LEGAJOS=[]
    NOTAS=[]
    cargaListas(LEGAJOS,NOTAS)
    
    print(LEGAJOS)
    print(NOTAS)
    
    mostrarListas(LEGAJOS,NOTAS)
    
    consultaNotas(LEGAJOS,NOTAS)
    
    notaMaxima=maximo(NOTAS)
    
    print("La nota maxima es ",notaMaxima)
    
    for i in range(len(NOTAS)):
        if NOTAS[i]==notaMaxima:
            print("Legajo con nota maxima ",LEGAJOS[i])
    
        
        
        
    
if __name__=="__main__":
    main()
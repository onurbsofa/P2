"""
Lea atentamente los puntos solicitados, implemente un programa principal que pruebe y
ejecute la lógica de cada punto. El contexto del ejercicio es realizar el seguimiento
del avance en la carrera de los estudiantes de una comisión de la materia de Fundamentos
de Informática en UADE
a-	(20%) Desarrolle función cargaListas que recibe dos listas vacías como parámetro y
realice la carga de dichas listas con valores al azar: una lista guardara legajos de
3 cifras no correlativos SIN DUPLICADOS (desarrolle e invoque a la función BUSQUEDA).
Un segundo dato asociado al código será un valor de porcentaje de avance entre 0 y 100.
El ingreso de los datos finaliza con un legajo igual a 99.
b-	(20%) Desarrolle una función mostrarAvance que recibe las listas de legajos y avances
y los muestra en consola según el siguiente detalle:
*** LISTADO AVANCE POR ALUMNO ***
          LEGAJO       PORCENTAJE
            XXX          XX%                                         
	        XXX          X%
             …           ….
    
c-	(20%) Ordene las listas por porcentaje de manera descendente
d-	(20%) Informe la cantidad de alumnos con porcentaje de avance menor al 50%
e-	(20%) Informe el porcentaje de avance promedio (considerando todos los alumnos)

"""
import random

def busqueda(lista,valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i<len(lista):
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos

def mostrarAvance(liLe,liAva):
    print("*** LISTADO AVANCE POR ALUMNO ***")
    print("LEGAJO\tAVANCE")
    
    for i in range(len(liLe)):
        print("%7d\t%6d %%" %(liLe[i],liAva[i]))

def cargaListas(liLe,liAva):
    auxLegajo=random.randint(99,999)
    while auxLegajo!=99:
        
        posicion=busqueda(liLe,auxLegajo)
        if posicion==-1:
            liLe.append(auxLegajo)
            liAva.append(random.randint(0,100))
        auxLegajo=random.randint(99,999)
            
def ordenamiento(lista1,lista2):
    for i in range(len(lista1)-1):
        for j in range(len(lista1)-1-i):
            
            if lista2[j]<lista2[j+1]:
                
                aux=lista2[j]
                lista2[j]=lista2[j+1]
                lista2[j+1]=aux
                
                aux=lista1[j]
                lista1[j]=lista1[j+1]
                lista1[j+1]=aux
                
def suma(lista):
    resu=0
    for i in range(len(lista)):
        resu+=lista[i]
    return resu
                       

def main():
    LEGAJOS=[]
    AVANCE=[]
    
    cargaListas(LEGAJOS,AVANCE)
    
    if len(LEGAJOS)>0:
        print(LEGAJOS)
        print(AVANCE)
        mostrarAvance(LEGAJOS,AVANCE)
        
        ordenamiento(LEGAJOS,AVANCE)
        mostrarAvance(LEGAJOS,AVANCE)
        
        cont=0
        for i in range(len(AVANCE)):
            if AVANCE[i]<50:
                cont+=1
        print("Cantidad de alumnos con avance inferior a 50% es ", cont)
        
        sumaAvance=suma(AVANCE)
        promedio=sumaAvance/len(AVANCE)
        
        print("El valor promedio de avance es ",promedio)
    else:
        print("No se ingresaron datos")
        
    
        
        
        
    
    
if __name__=="__main__":
    main()
"""
Una escuela necesita conocer cuántos alumnos
cumplen años en cada mes del 
año, con el propósito de ofrecerles un agasajo
especial en su día. Desarrollar un 
programa que lea el número de legajo y fecha
de nacimiento (día, mes y año) de 
cada uno de los alumnos que concurren a dicha
escuela. La carga finaliza con un 
número de legajo igual a -1. Emitir un informe
donde aparezca -mes por mescuántos alumnos
cumplen años a lo largo del año.
Imprimir también una leyenda 
que indique cuál es el mes con mayor cantidad
de cumpleaños"""

def ingresaValidaRango(li,ls,texto,textoE):
    valor=int(input(texto))
    while valor<li or valor>ls:
        valor=int(input(textoE))
    return valor

def ingresaValidaRangoCF(li,ls,cf,texto,textoE):
    valor=int(input(texto))
    while (valor<li or valor>ls) and valor!=cf:
        valor=int(input(textoE))
    return valor

def ingresaMayorA(valor, texto):
    nro=int(input(texto))
    while nro<=valor:
        nro=int(input(texto))
    return nro

   
def cargarCumples(lista):
    legajo=ingresaValidaRangoCF(1000,9999,-1,"Ingrese un legajo ","Error,Reingrese un legajo")
    while legajo!=-1:
        dia=ingresaValidaRango(1,30,"Ingrese un dia","Error, ingrese un dia")
        mes=ingresaValidaRango(1,12,"Ingrese un mes","Error, ingrese un mes")
        año=ingresaMayorA(2000,"Ingrese año nacimiento")
        
        lista[mes-1]+=1
        legajo=ingresaValidaRangoCF(1000,9999,-1,"Ingrese un legajo ","Error,Reingrese un legajo")

def cumplesxMes(lista):
    meses=['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
    print("*** LISTADO DE CANTIDAD DE CUMPLES x MES ***")
    print("MES       \t CANTIDAD")
    for i in range(len(lista)):
        print("%10s\t %8d" %(meses[i],lista[i]))

def maximo(lista):
    for i in range(len(lista)):
        if i==0 or lista[i] >valMax:
            valMax=lista[i]
            posMax=i
    return posMax
    
def main():
    CUMPLES=[0]*12
    cargarCumples(CUMPLES)
    
    cumplesxMes(CUMPLES)
    
    posicionMaximo=maximo(CUMPLES)
    
    print("EL mes de mayor cantidad de cumples es ",posicionMaximo+1)
    
if __name__=="__main__":
    main()



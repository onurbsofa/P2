"""
Una tienda de electrónicos dispone de 4 depositos (1 a 4) y maneja
15 productos distintos (código de 3 cifras sin duplicados).
Ingresar primeramente los códigos de los productos y sus respectivas
cantidades en stock, mediante una función.
 
Por cada día, cada vez que se realiza una venta, se dispone de la
siguiente información:
- Nro. de deposito
- Código de producto
- Cantidad vendida. SOLO PUEDO VENDER CUANDO EL STOCK ES SUFICIENTE.
Sino descartar la venta con un error!.
 
Esta información finaliza con Nro. de deposito cero.
Validar todos los datos ingresados mediante funciones genéricas.
 
Con las informaciones anteriores, realizar e informar el siguiente
resumen:
a) Un listado donde indique la cantidad de productos vendidos por
código de producto según el siguiente formato.
PRODUCTO CANTIDAD VENDIDA
xxxx      xxxx
xxxx      xxxx
Implementar una función para informar
b) Stock total restante de todos los productos, luego de procesar
las ventas.
c) Producto/s NO vendidos
d) Nro./s de desposito/s con mínima cantidad de productos vendidos
 
Implementar función main() ** OPCIONAL **
PUEDE GENERAR LOS DATOS DE MANERA ALEATORIA o RANDOM
UTILIZAR LA METODOLOGIA VISTA EN CLASE
NO USAR ESTRUCTURAS NO TRABAJADAS EN LA MATERIA
NO USAR CICLOS INFINITOS-RUPTURA DE CICLOS, NO USAR TUPLAS/DICCIONARIOS/CONJUNTOS
NO USAR VARIABLES GLOBALES
USAR LISTAS HOMOGENEAS. MODULARIZAR EL CODIGO"""

import random

def busqueda(lista,valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i<len(lista):
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos

def cargaInicial(liCo,liSto):
    i=0
    while i<15:
        auxCod=random.randint(100,999)
        posicion=busqueda(liCo,auxCod)
        if posicion ==-1:
            liCo.append(auxCod)
            liSto.append(random.randint(0,1000))
            i+=1
        else:
            print("Codigo duplicado!")
            
def ingresaValidaRango(li,ls,texto):
    valor=int(input(texto))
    while valor<li or valor>ls:
       valor=int(input(texto))
    return valor

def mayorA(nro,texto):
    valor=int(input(texto))
    while valor<=nro:
       valor=int(input(texto))
    return valor
    
def sumaLista(lista):
    resu=0
    for i in range(len(lista)):
        resu+=lista[i]
    return resu

def listadoProductoCantidad(liCo,liCa):
    print(" *** LISTADO CANTIDAD VENDIDA POR PRODUCTO ***")
    print("CODIGOS \t CANTIDAD ")
    for i in range(len(liCo)):
        print("%7d \t %8d" %(liCo[i],liCa[i]))

def listadoProductoStock(liCo,liSto):
    print(" *** LISTADO STOCK POR PRODUCTO ***")
    print("CODIGOS \t STOCK ")
    for i in range(len(liCo)):
        print("%7d \t %8d" %(liCo[i],liSto[i]))

def minimo(lista):    
    for i in range(len(lista)):
        if (i==0 or lista[i]<valorMinimo):
            valorMinimo=lista[i]
    return valorMinimo

"""
def maximo(lista):
    
    for i in range(len(lista)):
        if (i==0 or lista[i]>valorMaximo):
            valorMaximo=lista[i]
    return valorMaximo"""

def main():
    CODIGOS=[]
    STOCK=[]
    DEPOCANT=[0]*4
    CANTVEND=[0]*15
    
    #carga inicial
    cargaInicial(CODIGOS,STOCK)
    
    print(CODIGOS)
    print(STOCK)
    print(CANTVEND)
    print(DEPOCANT)
    
    #procesamiento
    #huboVentas=False
    auxDepo=ingresaValidaRango(0,4,"Ingrese un codigo de deposito valido: ")
    while auxDepo!=0:
        
        auxCod=ingresaValidaRango(100,999,"Ingrese codigo de producto:")
        
        posicion=busqueda(CODIGOS,auxCod)
        
        if posicion!=-1:
            auxCant=mayorA(0,"Ingrese cantidad vendida")
            if STOCK[posicion]>=auxCant:
                #huboVentas=True
                STOCK[posicion]-= auxCant
                CANTVEND[posicion]+=auxCant
                DEPOCANT[auxDepo-1]+=auxCant
                
            else:
                print("Venta rechazada por stock insuficiente")
            
            
        else:
            print("Codigo inexistente")
        auxDepo=ingresaValidaRango(0,4,"Ingrese un codigo de deposito valido: ")
    
    print(CODIGOS)
    print(STOCK)
    print(CANTVEND)
    print(DEPOCANT)
    
    if sumaLista(DEPOCANT)>0:
        """
        a) Un listado donde indique la cantidad de productos vendidos por
        código de producto según el siguiente formato.
        PRODUCTO CANTIDAD VENDIDA
        xxxx      xxxx
        xxxx      xxxx
        Implementar una función para informar"""
        listadoProductoCantidad(CODIGOS,CANTVEND)
        """
        b) Stock total restante de todos los productos, luego de procesar
        las ventas."""
        listadoProductoStock(CODIGOS,STOCK)
        """
        c) Producto/s NO vendidos
        """
        print("Productos NO VENDIDOS")
        for i in range(len(CODIGOS)):        
            if CANTVEND[i]==0:
                print(CODIGOS[i])
        
        """
        d) Nro./s de desposito/s con mínima cantidad de productos
        vendidos
         """
        valorMinimo=minimo(DEPOCANT)
        print("La cantidad minima vendida en los depositos es ",valorMinimo)
        print("y los depositos con esta cantidad minima es ")
        for i in range(len(DEPOCANT)):
            if DEPOCANT[i]==valorMinimo:
                print(i+1)
        
    else:
        print("No se realizaron ventas hoy")
        
        

    
if __name__=="__main__":
    main()



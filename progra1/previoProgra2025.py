#no se podia usar: Max,min,not in, in y while True 

import random
def procesar(archivo,listapagos,listanopagos):
    try:
        arch=open(archivo,'rt')
        for linea in arch:
            linea=linea.strip().split(";")
            if len(linea)==3:
                nombre,fila,asiento=linea
                listapagos[nombre]=(fila,asiento)
            else:
                nombre=linea[0]
                listanopagos[nombre]=[]
    except FileNotFoundError:
        ("Archivo no encontrado")
    finally:
        try:
            arch.close()
        except FileNotFoundError:
            print("Archivo no encontrado")
    return listapagos,listanopagos

def avion(filas,columas):
    vuelo=[[1]*columas for _ in range(filas)]
    return vuelo

def rellenaravionpago(vuelo,listapagos,letras):
    colisiones={}
    for nombre,(f,c)in listapagos.items():
        c=letras[c]
        if vuelo[int(f)-1][int(c)-1]==1:
            vuelo[int(f)-1][int(c)-1]=0
        else:
            colisiones[nombre]=(f,c)
    return vuelo,colisiones

def rellenaravionnopago(vuelo,listanopagos,filas,columnas):
    for pasajero in listanopagos.keys():
        fila=(random.randint(1,filas))
        columnas=(random.randint(1,columnas))
        while True:
            if vuelo[fila-1][columnas-1]==1:
                vuelo[fila-1][columnas-1]=0
                listanopagos[pasajero]=(fila,columnas)
                break
            else:
                fila=(random.randint(1,filas))
                columnas=(random.randint(1,columnas))
    return vuelo

def mostrar(vuelo, listapagos, listanopagos, colisiones,numeros):
    noasignado = []
    filas = len(vuelo)
    columnas = len(vuelo[0])

    for f in range(filas):
        for c in range(columnas):
            if vuelo[f][c] == 1:
                noasignado.append((f+1, c+1))

    for fila, columna in noasignado:
        print(f"ASIENTO: {fila}-{columna} -- LIBRE")

    orden1 = dict(sorted(listapagos.items(), key=lambda x: x[1][0], reverse=True))
    for pasajero, (fila, asiento) in orden1.items():
        print(f"{pasajero} -- Fila {fila} -- Asiento {asiento}")

    orden2=dict(sorted(listanopagos.items(),key=lambda x: x[1][0],reverse=True))
    for pasajero,(fila,asiento)in orden2.items():
        print(f"{pasajero} {fila} {asiento}-- Asiento asignado aleatoriamente")

    for pasajero, (fila, asiento) in colisiones.items():
        print(f"{pasajero} tuvo una colisiÃ³n en Fila {fila}, Asiento {asiento}")

        
        

def analizar(listapagos):
    lista=[]
    for (fila,asiento) in listapagos.values():
        lista.append(int(fila))
    filas=max(lista)
    if filas<=32: 
        print("Avion regional")
        columnas=6
        filas=32
        return filas,columnas
    else:
        columnas=10
        return filas,columnas
        
    
def main():
    listapagos={}
    listanopagos={}
    letras={"A":1,
            "B":2,
            "C":3,
            "D":4,
            "E":5,
            "F":6,
            "G":7,
            "H":8,
            "I":9,
            "J":10
            }
    numeros={
        1:"A",
        2:"B",
        3:"C",
        4:"D",
        5:"E",
        6:"F",
        7:"G",
        8:"H",
        9:"I",
        10:"J",
    }
    listapagos,listanopagos=procesar('avion.txt',listapagos,listanopagos)
    filas,columnas=analizar(listapagos)
    vuelo=avion(filas,columnas)
    vuelo,colisiones=rellenaravionpago(vuelo,listapagos,letras)
    vuelo=rellenaravionnopago(vuelo,listanopagos,filas,columnas)
    mostrar(vuelo,listapagos,listanopagos,colisiones,numeros)

if __name__=='__main__':
    main()
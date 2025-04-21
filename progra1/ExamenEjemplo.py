"""Una aerolínea de bajo costo cobra un adicional sobre el precio del pasaje a quienes deseen elegir asiento. Quienes no lo abonen serán asignados al azar en los asientos que no se hayan sido elegidos previamente. Esta información se almacena por cada vuelo en un archivo CSV donde cada registro puede tener dos formatos diferentes:

Formato 1:
Nombre del pasajero;fila;asiento

Formato 2:
Nombre del pasajero

El formato 1 se aplica a quienes hayan abonado el adicional por seleccionar ubicación, mientras que el formato 2 se aplica a los demás viajeros.

El nombre del pasajero se escribe como <Apellido, nombre>. La fila oscila entre 1 y N, donde N es el valor de N del modelo de la aeronave. El asiento va desde la A hasta la F en modelos regionales de hasta 32 filas de asientos y desde la A hasta J en modelos de doble pasillo y largo alcance con más de 32 filas de asientos.

Se solicita desarrollar un programa que lea un archivo con las características mencionadas y distribuya los asientos respetando las reservas realizadas y asignando al azar los asientos restantes entre los pasajeros que no abonaron el adicional. Mostrar un listado con las asignaciones realizadas ordenado por fila y asiento, e imprimir otro listado con los pasajeros que hayan quedado libres ordenado por el mismo criterio. También se deberán tener en lista con las colisiones, si las hubiera. Una colisión ocurre cuando dos pasajeros destinan un mismo asiento en sus reservas. Estos eventos deben ser resueltos por los usuarios.

Se suministra un archivo ejemplo llamado Vuelo447.txt. El archivo no está ordenado ni sigue ningún criterio particular. El programa debe funcionar con este o cualquier otro archivo que respete las características indicadas, detectando automáticamente el modelo de avión (sim- o doble pasillo) en función de la cantidad de filas de la aeronave y de los asientos reservados o vacíos. Es decir que si todas las reservas tienen una fila menor o igual a 32 y todos los asientos van de la columna A a la F, deberá considerarse que se trata de un avión de un solo pasillo y alcance regional."""
#falta cambiar los asientos de letras a numeros
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
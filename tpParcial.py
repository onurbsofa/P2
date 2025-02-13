"""Desarrollaremos un sistema que gestione el registro de envíos, incluyendo la posibilidad de añadir nuevos envíos, buscar envíos por ID, ordenar los envíos por costo, encontrar el envío con el costo máximo y mínimo y, por último, mostrar el estado final de todos los envíos registrados hasta el momento.

Funcionalidades principales del sistema:

Añadir nuevos envíos: Esta función permitirá al usuario ingresar los detalles de un nuevo envío y generará un ID único para él. Los envíos se almacenarán en una lista, donde cada envío estará representado por una lista que contiene su ID, costo, peso y destino (nacional/internacional). La función de ingreso de envíos finalizará con un valor indicativo, como -1.

Buscar envíos por ID: Permitirá buscar un envío en la lista por su ID y devolverá los detalles si se encuentra.

Ordenar los envíos por costo: Esta función ordenará la lista de envíos según el costo de cada envío, ya sea de menor a mayor o viceversa, según los requisitos.

Encontrar el envío con el costo máximo y mínimo: Recorrerá la lista de envíos para encontrar aquellos con el costo más alto y el más bajo. Si hay varios envíos con el mismo costo máximo o mínimo, se mostrarán todos.

Mostrar el estado final de todos los envíos registrados hasta el momento: Esta función mostrará la lista completa de envíos con todos sus detalles.

Otras funcionalidades del sistema:

Generar un ID único: Se utilizará una función para generar IDs aleatorios y verificar que no se repitan.
Mostrar el menú: Un menú interactivo que permitirá al usuario seleccionar la acción que desea realizar.
Función Principal:

Esta función gestionará la interacción del usuario con el sistema y llamará a las funciones anteriores según la opción seleccionada, agregando validaciones específicas para cada función, como por ejemplo, asegurarse de que el costo ingresado sea mayor a 0.

Con estas funcionalidades, el sistema podrá gestionar eficientemente el registro y la consulta de envíos.
"""

import random

def validar_dato(valor, minimo, maximo):
    if minimo != None and valor < minimo:
        print("Error: El valor debe ser mayor o igual a " , minimo)
        return False
    if maximo != None and valor > maximo:
        print("Error: El valor debe ser menor o igual a ", maximo)
        return False
    return True

def validadorID(ids, id_unico):
    pos= -1
    i = 0
    while pos==-1 and i<len(ids):
        if ids[i] == id_unico:
            pos = i
        i+=1
        return pos    

def generarId(ids):
    id_unico = random.randint(1000, 9999)
    unico = False
    while not unico:
        pos=validadorID(ids, id_unico)
        if pos != id_unico:
            unico = True
        else:
            id_unico = random.randint(1000, 9999) 
    print('El ID asignado es:', id_unico)
    return id_unico

def ingresoNuevosEnvios (ids, costos, peso, destinos):
    opcion = int(input('Ingrese -1 para finalizar la carga, o 1 para continuar: '))   
    while(opcion != -1):
        ids_nuevos = generarId (ids)
        ids.append(ids_nuevos)
        costo_nuevo = float(input('Ingrese el costo del envio: '))
        costos.append(costo_nuevo)
        peso_nuevo = float(input('Ingrese el peso total del envio a ingresar en KG: '))
        peso.append(peso_nuevo)
        destino_nuevo = int(input('Ingrese 1, si su envio tiene destino Nacional. Ingrese 2 si su envio corresponde a un destino Internacional'))
        destinos.append(destino_nuevo)

        print('Se ingresaron los siguiente datos: \n ID:', ids_nuevos, '\n Costo: $', costos, '\n Peso:', peso,'kg.')
        opcion = int(input('Ingrese -1 para finalizar la carga, o 1 para continuar: '))


def mostrarEnvios (ids, costos, peso, destinos):
    for i in range(len(ids)):
        print('El ID', ids[i])
        print('El costo', costos[i])
        print('El peso', peso[i])
        print('El destino', destinos[i])


def buscarEnviosporID (ids):
    busquedaID = int(input('Ingrese el ID del pedido que desea buscar'))
    encontrado = False
    for indice in range (len(ids)):
        if busquedaID == ids[indice]:
            print(' \n El envio fue encontrado \n El ID del envio es', ids[indice])
            encontrado = True
    if not encontrado:
        print('El envio no fue encontrado')

def encontrarPorCostos(costos):
    bandMin = 0
    bandMax = 0
    opcion = int(input(' \n Indique con un 1 si desea buscar el costo maximo de los envios \n Indique con un 2 si desea buscar el costo maximo de los envios'))

    if opcion == 1:
        for indice in range(len(costos)):
            if (bandMin == 0 and costos[indice] < bandMin):
                valorMinimo = costos[indice]
                print('El valor minimo es', costos[indice])
    elif opcion == 2: 
        for indice in range(len(costos)):
            if (bandMax == 0 and costos[indice] < bandMax):
                valorMaximo = costos[indice] 
                print('El valor maximo es', costos[indice])

def mostrarMenu ():
    print("1. Si desea ingresar un nuevo envio.")
    print("2. Si desea buscar un envio por su ID.")
    print("3. Si desea ordenar los envios por su costo.")
    print("4. Si desea encontrar un envio por su costo maximo o minimo.")
    print("5. Si desea ver el estado final, hasta el momento, de todos sus envios.")
    print("6. Salir")

def main():
    ids = []
    costos = []
    peso = []
    destinos = []

    mostrarMenu()
    
    opcion = int(input("Seleccione una opcion: "))
    while (opcion != 6):
        if (opcion == 1):
            ingresoNuevosEnvios(ids, costos, peso, destinos)
        elif (opcion == 2):
            buscarEnviosporID(ids)
        elif (opcion == 3): 
            print('Proximamente')
        elif (opcion == 4):
            encontrarPorCostos(costos)
        elif (opcion == 5):
            mostrarEnvios(ids, costos, peso, destinos) 
        else:
            print('Error - Ingrese una opcion correcta')
        mostrarMenu()
        opcion = int(input("Seleccione una opcion: "))
    print('Hasta luego')

    
if __name__ == "_main_":
    main()
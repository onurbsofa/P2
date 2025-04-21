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

def busqueda(ids, id_unico):
    pos= -1
    i = 0
    while pos==-1 and i<len(ids):
        if ids[i] == id_unico:
            pos = i
        i+=1
    return pos

def busquedaCosto(costoMin, costoMax, costos, ids, peso, destinos):
    band = -1
    for i in range(len(costos)):
        if costoMin < costos[i] < costoMax:
            print('------------------------Envío encontrado:------------------------')
            print('ID:', ids[i])
            print('Costo: $', costos[i])
            print('Peso:', peso[i], 'kg')
            if destinos[i] == 1:
                print('Destino: Nacional')
            else:
                print('Destino: Internacional')
            band += 1
    if band == -1:
        print('Error - No se encontraron envios con dichos costos')


def generarId(ids):
    id_unico = random.randint(1000, 9999)
    unico = False
    while not unico:
        pos=busqueda(ids, id_unico)
        if pos != id_unico:
            unico = True
        else:
            id_unico = random.randint(1000, 9999)
    print('El ID asignado es:', id_unico)
    return id_unico

def validar_dato(valor, minimo, maximo):
    if minimo != None and valor < minimo:
        print("Error: El valor debe ser mayor o igual a " , minimo)
        return False
    if maximo != None and valor > maximo:
        print("Error: El valor debe ser menor o igual a ", maximo)
        return False
    return True

def validar_opcion (valor, minimo, maximo):
    if valor != minimo and valor != maximo:
        print("Error: El valor debe ser -1 o 1" , minimo)
        return False
    return True

def ingresoCosto ():
    ingreso = float(input('Ingrese el costo del envio: $'))
    while not validar_dato(ingreso, 1, 100000):
        ingreso = float(input('Ingrese el costo del envio: '))
    return ingreso
 
def ingresoPeso ():
    ingreso = float(input('Ingrese el peso total del envio a ingresar en KG: '))
    while not validar_dato(ingreso, 0.5, 30):
        ingreso = float(input('Ingrese el peso total del envio a ingresar en KG: '))
    return ingreso


def ingresoDestino ():
    ingreso = int(input('Ingrese 1, si su envio tiene destino Nacional. Ingrese 2 si su envio corresponde a un destino Internacional: '))
    while not validar_dato(ingreso, 1, 2):
        ingreso = int(input('Ingrese 1, si su envio tiene destino Nacional. Ingrese 2 si su envio corresponde a un destino Internacional: '))
    return ingreso

def opcion ():
    opcion = int(input('Ingrese -1 para finalizar la carga, o 1 para continuar: '))   
    while not validar_opcion(opcion, -1, 1):
        opcion = int(input('Ingrese -1 para finalizar la carga, o 1 para continuar: '))
    return opcion

def ingresoNuevosEnvios (ids, costos, peso, destinos):
    opcion_valor = opcion()
    while opcion_valor != -1:
        ids_nuevos = generarId (ids)
        ids.append(ids_nuevos)
        costo_nuevo = ingresoCosto()
        costos.append(costo_nuevo)
        peso_nuevo = ingresoPeso()
        peso.append(peso_nuevo)
        destino_nuevo= ingresoDestino()
        destinos.append(destino_nuevo)
        print('Datos del ultimo envio ingresado: \n ID:', ids_nuevos, '\n Costo: $', costo_nuevo, '\n Peso:', peso_nuevo,'kg.','\n Destino:', destino_nuevo)
        opcion_valor = opcion()
    print('Se ingresaron los siguiente datos: \n ID:', ids, '\n Costo: $', costos, '\n Peso:', peso,'kg.','\n Destino:', destinos)

def buscarEnviosporID(ids):
   encontrado = False
   while not encontrado:
        busquedaID = int(input('Ingrese el ID del pedido que desea buscar '))
        pos = busqueda(ids, busquedaID)
        if pos != -1:
            print('El envio con el ID', busquedaID, 'fue encontrado.')
        else:
            print('El envio con el ID', busquedaID, 'no fue encontrado.')
        encontrado = True

def buscarEnviosPorCosto(ids, costos, peso, destinos):
    costoMin = int(input("Ingrese el costo minimo que desea buscar: "))
    costoMax = int(input("Ingrese el costo maximo que desea buscar: "))
    while costoMax < costoMin:
        print("Error, el minimo debe ser menor al maximo.")
        costoMin = int(input("Ingrese el costo minimo que desea buscar: "))
        costoMax = int(input("Ingrese el costo maximo que desea buscar: "))
    busquedaCosto(costoMin, costoMax, costos, ids, peso, destinos)
        


def mostrarEnvios (ids, costos, peso, destinos):
    print('-------------------------Envíos totales:-------------------------')  
    for i in range(len(ids)):
        destino = ""
        if destinos[i] == 1:
            destino = "Nacional"
        else:
            destino = "Internacional"
        print('ID:', ids[i])
        print('Costo: $', costos[i])
        print('Peso:', peso[i], 'kg')
        if destinos[i] == 1:
            print('Destino: Nacional')
        else:
            print('Destino: Internacional')
        print('-----------------------------------------------------------------')

def ordenarEnviosPorCosto(ids, costos, peso, destinos):
    print('Ingrese -1 si desea ordenar los envios por costo de manera creciente, o 1 si desea ordenar los envios por costo de manera decreciente ')
    opcionCosto = opcion ()
    ordenamiento = ''
    if opcionCosto == -1:
        ordenamiento = 'creciente:'
        for i in range(len(costos) - 1):
            for j in range(0, len(costos) - 1 - i):
                if(costos[j] > costos[j+1]):
                    aux = costos [j]
                    costos[j] = costos[j+1]
                    costos[j+1] = aux

                    aux = ids[j]
                    ids[j] = ids[j+1]
                    ids[j+1] = aux

                    aux = peso[j]
                    peso[j] = peso[j+1]
                    peso[j+1] = aux

                    aux = destinos [j]
                    destinos[j] = destinos[j+1]
                    destinos[j+1] = aux

    elif opcionCosto == 1:
        ordenamiento = 'decreciente:'
        for i in range(len(costos) - 1):
            for j in range(0, len(costos) - 1 - i):
                if(costos[j] < costos[j+1]):
                    aux = costos [j]
                    costos[j] = costos[j+1]
                    costos[j+1] = aux

                    aux = ids[j]
                    ids[j] = ids[j+1]
                    ids[j+1] = aux

                    aux = peso[j]
                    peso[j] = peso[j+1]
                    peso[j+1] = aux

                    aux = destinos [j]
                    destinos[j] = destinos[j+1]
                    destinos[j+1] = aux
    
    
    print('Envíos ordenados por costo', ordenamiento)
    mostrarEnvios(ids, costos, peso, destinos)



def mostrarMenu ():
    print('---------------------------- Menu ------------------------------')  
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
            ordenarEnviosPorCosto(ids, costos, peso, destinos)
        elif (opcion == 4):
            buscarEnviosPorCosto(ids, costos, peso, destinos)
        elif (opcion == 5):
            mostrarEnvios(ids, costos, peso, destinos) 
        else:
            print('Error - Ingrese una opcion correcta')
        mostrarMenu()
        opcion = int(input("Seleccione una opcion: "))
    print('Hasta luego')

if __name__== "__main__":
    main()
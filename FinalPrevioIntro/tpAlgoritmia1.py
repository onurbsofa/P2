import random

def busqueda(ids, id_unico):
    pos = -1
    i = 0
    while pos == -1 and i < len(ids):
        if ids[i] == id_unico:
            pos = i
        i += 1
    return pos

def generarId(ids):
    id_unico = random.randint(1000, 9999)
    while busqueda(ids, id_unico) != -1:
        id_unico = random.randint(1000, 9999)
    print('El ID asignado es:', id_unico)
    return id_unico

def validar_dato(valor, minimo, maximo):
    if valor < minimo or valor > maximo:
        print(f"Error: El valor debe estar entre {minimo} y {maximo}.")
        return False
    return True

def ingresoTipoMutante():
    tipos = ["Garras", "Alas", "Telepatía", "Camuflaje", "Fuerza", "Velocidad", "Invisibilidad", "Regeneración", "Control Mental"]
    print("Tipos de mutantes disponibles:")
    for i, tipo in enumerate(tipos, start=1):
        print(f"{i}. {tipo}")
    tipo = int(input("Seleccione el tipo de mutante (1-9): "))
    while not validar_dato(tipo, 1, 9):
        tipo = int(input("Seleccione el tipo de mutante (1-9): "))
    return tipos[tipo - 1]

def ingresoNivelPoder():
    nivel = int(input("Ingrese el nivel de poder del mutante (1-100): "))
    while not validar_dato(nivel, 1, 100):
        nivel = int(input("Ingrese el nivel de poder del mutante (1-100): "))
    return nivel

def ingresoClasificacion():
    clasificacion = int(input("Ingrese 1 para benigno o 2 para peligroso: "))
    while not validar_dato(clasificacion, 1, 2):
        clasificacion = int(input("Ingrese 1 para benigno o 2 para peligroso: "))
    return "Benigno" if clasificacion == 1 else "Peligroso"

def ingresoSector():
    sector = int(input("Ingrese el sector del zoológico al que pertenece el mutante (1-6): "))
    while not validar_dato(sector, 1, 6):
        sector = int(input("Ingrese el sector del zoológico al que pertenece el mutante (1-6): "))
    return sector

def ingresarNuevosMutantes(ids, tipos, niveles, clasificaciones, sectores):
    continuar = 's'
    while continuar == 's':
        id_unico = generarId(ids)
        ids.append(id_unico)
        
        tipo_mutante = ingresoTipoMutante()
        tipos.append(tipo_mutante)
        
        nivel_poder = ingresoNivelPoder()
        niveles.append(nivel_poder)
        
        clasificacion = ingresoClasificacion()
        clasificaciones.append(clasificacion)

        sector = ingresoSector()
        sectores.append(sector)
        
        print(f"Mutante registrado: ID={id_unico}, Tipo={tipo_mutante}, Nivel de Poder={nivel_poder}, Clasificación={clasificacion}, Sector={sector}")
        
        continuar = input("¿Desea ingresar otro mutante? (s/n): ")
        while continuar != 's' and continuar != 'n':
            print("Error: Ingrese 's' para continuar o 'n' para finalizar.")
            continuar = input("¿Desea ingresar otro mutante? (s/n): ")

def buscarMutantePorID(ids, tipos, niveles, clasificaciones, sectores):
    id_buscar = int(input("Ingrese el ID del mutante que desea buscar: "))
    pos = busqueda(ids, id_buscar)
    if pos != -1:
        print(f"Mutante encontrado: ID={ids[pos]}, Tipo={tipos[pos]}, Nivel de Poder={niveles[pos]}, Clasificación={clasificaciones[pos]}, Sector={sectores[pos]}")
    else:
        print(f"Mutante con ID {id_buscar} no encontrado.")

def ordenarMutantesPorPoder(ids, tipos, niveles, clasificaciones, sectores):
    opcion = input("Ingrese 'asc' para ordenar de forma ascendente o 'desc' para descendente: ")
    
    while opcion != 'asc' and opcion != 'desc':
        print("Opción no válida. Ingrese 'asc' para ordenar de forma ascendente o 'desc' para descendente.")
        opcion = input("Ingrese 'asc' para ordenar de forma ascendente o 'desc' para descendente: ")
    
    reverse = opcion == 'desc'
    
    datos = list(zip(niveles, ids, tipos, clasificaciones, sectores))
    datos.sort(reverse=reverse)
    
    niveles[:], ids[:], tipos[:], clasificaciones[:], sectores[:] = zip(*datos)
    print("Mutantes ordenados por nivel de poder.")
    mostrarMutantes(ids, tipos, niveles, clasificaciones, sectores)

def encontrarMaxMinPoder(niveles, ids, tipos, clasificaciones, sectores, opcion):
    if len(niveles) == 0:
        print("No hay mutantes registrados.")
        return
    
    if opcion == "max":
        max_poder = max(niveles)
        indices = [i for i, nivel in enumerate(niveles) if nivel == max_poder]
        print("Mutante(s) con el nivel de poder máximo:")
    else:
        min_poder = min(niveles)
        indices = [i for i, nivel in enumerate(niveles) if nivel == min_poder]
        print("Mutante(s) con el nivel de poder mínimo:")
    
    for i in indices:
        print(f"ID={ids[i]}, Tipo={tipos[i]}, Nivel de Poder={niveles[i]}, Clasificación={clasificaciones[i]}, Sector={sectores[i]}")

def mostrarMutantes(ids, tipos, niveles, clasificaciones, sectores):
    print("Estado actual de los mutantes registrados:")
    for i in range(len(ids)):
        print(f"ID={ids[i]}, Tipo={tipos[i]}, Nivel de Poder={niveles[i]}, Clasificación={clasificaciones[i]}, Sector={sectores[i]}")
    print("-----------------------------------------------------------")

def consultarMutantesPorSector(sectores):
    conteo_sectores = [0] * 6
    for sector in sectores:
        conteo_sectores[sector - 1] += 1
    print("Cantidad de mutantes por sector:")
    for i in range(6):
        print(f"Sector {i + 1}: {conteo_sectores[i]} mutantes")
    print("-----------------------------------------------------------")

def mostrarMenu():
    print("--------- Menú ---------")
    print("1. Ingresar un nuevo mutante.")
    print("2. Buscar un mutante por ID.")
    print("3. Ordenar mutantes por nivel de poder.")
    print("4. Encontrar mutante con nivel de poder máximo o mínimo.")
    print("5. Mostrar todos los mutantes.")
    print("6. Consultar la cantidad de mutantes por sector.")
    print("7. Salir")

def main():
    ids = []
    tipos = []
    niveles = []
    clasificaciones = []
    sectores = []
    
    opcion = 0
    while opcion != 7:
        mostrarMenu()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            ingresarNuevosMutantes(ids, tipos, niveles, clasificaciones, sectores)
        elif opcion == 2:
            buscarMutantePorID(ids, tipos, niveles, clasificaciones, sectores)
        elif opcion == 3:
            ordenarMutantesPorPoder(ids, tipos, niveles, clasificaciones, sectores)
        elif opcion == 4:
            max_min_opcion = input("Ingrese 'max' para encontrar el nivel máximo o 'min' para el mínimo: ")
            while max_min_opcion != 'max' and max_min_opcion != 'min':
                print("Opción no válida.")
                max_min_opcion = input("Ingrese 'max' para encontrar el nivel máximo o 'min' para el mínimo: ")
            encontrarMaxMinPoder(niveles, ids, tipos, clasificaciones, sectores, max_min_opcion)
        elif opcion == 5:
            mostrarMutantes(ids, tipos, niveles, clasificaciones, sectores)
        elif opcion == 6:
            consultarMutantesPorSector(sectores)
        elif opcion != 7:
            print("Opción no válida, por favor intente de nuevo.")
    
    print("Saliendo del sistema...")

if __name__ == "__main__":
    main()

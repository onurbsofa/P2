'''
--------------------
Metodos sobre listas
--------------------
append(): Agrega un elemento al final de la lista.

        # Creamos una lista vacía
        mi_lista = []

        # Agregamos elementos a la lista
        mi_lista.append('a')
        mi_lista.append('b')
        mi_lista.append('c')

        print(mi_lista) # ['a', 'b', 'c']

extend(): Agrega los elementos de otra lista al final de la lista.

        # Definimos dos listas
        lista1 = [1, 2, 3]
        lista2 = [4, 5, 6]

        # Usamos el método extend() para agregar los elementos de lista2 a lista1
        lista1.extend(lista2)

        print(lista1) # [1, 2, 3, 4, 5, 6]



insert(): Inserta un elemento en una posición específica de la lista.

        # Definimos una lista de números
        numeros = [1, 2, 4, 5]

        # Insertamos el número 3 en la posición 2
        numeros.insert(2, 3)

        print(numeros) # [1, 2, 3, 4, 5]


remove(): Elimina el primer elemento de la lista que tenga el valor especificado.

        # Definimos una lista de frutas
        frutas = ['manzana', 'banana', 'naranja']

        # Removemos la fruta 'banana'
        frutas.remove('banana')

        print(frutas) # ['manzana', 'naranja']


pop(): Elimina el elemento en la posición especificada de la lista y lo devuelve.

        # Definimos una lista de frutas
        frutas = ['manzana', 'banana', 'naranja']

        # Removemos y obtenemos el último elemento de la lista
        ultima_fruta = frutas.pop()

        print(ultima_fruta) # 'naranja'
        print(frutas) # ['manzana', 'banana']
        
        # Removemos y obtenemos el elemento en la posición 1 de la lista
        segunda_fruta = frutas.pop(1)

        print(segunda_fruta) # 'banana'
        print(frutas) # ['manzana']


index(): Devuelve la posición del primer elemento con el valor especificado.

        # Definimos una lista de frutas
        frutas = ['manzana', 'banana', 'naranja']

        # Obtenemos el índice de la fruta 'banana'
        indice_banana = frutas.index('banana')
        
        if 'banana' in frutas:
            indice_banana = frutas.index('banana')
        
        print(indice_banana) # 1
                
        # Tratando de obtener el índice de un elemento que no está en la lista
        frutas.index('kiwi') # Genera un error ValueError
        
     
count(): Devuelve el número de veces que aparece un valor específico en la lista.

        lista = [1, 2, 3, 4, 2, 5, 2]
        cuenta = lista.count(2)
        print(cuenta)  # Imprime 3

sort(): Ordena los elementos de la lista de forma ascendente.

        lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        lista.sort()
        print(lista)  # Imprime [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        
        lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        lista.sort(reverse=True)
        print(lista)  # Imprime [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
        
        
        nombres = ['Juan', 'María', 'Pedro', 'Lucía']
        edades = [25, 32, 18, 27]
        alturas = [1.75, 1.68, 1.82, 1.71]

        # Combinar las tres listas en una sola lista de tuplas
        datos = list(zip(nombres, edades, alturas))

        # Ordenar la lista combinada en base a la edad de forma ascendente
        datos.sort(key=lambda x: x[1])

        # Imprimir los datos ordenados
        for nombre, edad, altura in datos:
            print(nombre, edad, altura)

reverse(): Invierte el orden de los elementos en la lista.

        lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        lista.reverse()
        print(lista)  # Imprime [5, 3, 5, 6, 2, 9, 5, 1, 4, 1, 3]

copy(): Crea una copia de la lista original.
        Es importante tener en cuenta que la función copy() solo crea una copia superficial
        de la lista. Si la lista contiene objetos mutables
        (como otras listas, diccionarios, conjuntos, etc.), 
        los objetos mutables dentro de la lista original y la copia superficial
        todavía se compartirán en la memoria.
        
        
        lista1 = [1, 2, 3, 4, 5]
        lista2 = lista1.copy()

        # Modificar el primer elemento de la lista1
        lista1[0] = 0

        print(lista1)  # Imprime [0, 2, 3, 4, 5]
        print(lista2)  # Imprime [1, 2, 3, 4, 5]


----------------------
Funciones sobre listas
----------------------

len(): Devuelve la longitud de la lista (el número de elementos).
    lista = [1, 2, 3, 4, 5]
    longitud = len(lista)
    print(longitud) # Salida: 5


max(): Devuelve el valor máximo en la lista.
min(): Devuelve el valor mínimo en la lista.

    numeros = [10, 5, 20, 15, 30]
    maximo = max(numeros)
    minimo = min(numeros)

    print("El valor máximo de la lista es:", maximo)  # Salida: El valor máximo de la lista es: 30
    print("El valor mínimo de la lista es:", minimo)  # Salida: El valor mínimo de la lista es: 5


sum(): Devuelve la suma de todos los elementos en la lista.
    numeros = [1, 2, 3, 4, 5]
    suma = sum(numeros)
    print("La suma de los números es:", suma) # Salida: La suma de los números es: 15


sorted(): Devuelve una nueva lista ordenada a partir de los elementos de la lista original.
    numeros = [5, 1, 3, 2, 4]
    numeros_ordenados = sorted(numeros)
    print(numeros_ordenados) # Salida: [1, 2, 3, 4, 5]
    
    numeros = [5, 1, 3, 2, 4]
    numeros_ordenados_desc = sorted(numeros, reverse=True)
    print(numeros_ordenados_desc) # Salida: [5, 4, 3, 2, 1]

reversed(): Devuelve un objeto iterador que produce los elementos de la lista en orden inverso.
    numeros = [1, 2, 3, 4, 5]
    numeros_inversos = reversed(numeros)
    for numero in numeros_inversos:
        print(numero)
    # Salida:
    # 5
    # 4
    # 3
    # 2
    # 1
       
    
    
nombres = ['Juan', 'Ana', 'Pedro']
edades = [25, 30, 28]
estaturas = [1.75, 1.68, 1.82]

personas = zip(nombres, edades, estaturas)
personas_ordenadas = sorted(personas, key=lambda x: x[1])

for persona in personas_ordenadas:
    print(persona)
# Salida:
# ('Juan', 25, 1.75)
# ('Pedro', 28, 1.82)
# ('Ana', 30, 1.68)

'''

#1----------------------------------------declaracion de una lista en python
# Una lista vacía
lista_vacia = []

# Una lista de enteros
numeros = [1, 2, 3, 4, 5]

# Una lista de cadenas de texto
frutas = ['manzana', 'plátano', 'naranja']

# Una lista mixta
mixta = [1, 'hola', 3.14, True]

# También puedes crear una lista de valores repetidos utilizando el operador de multiplicación
repetidos = [0] * 5  # [0, 0, 0, 0, 0]




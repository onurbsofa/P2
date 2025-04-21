'''Alternativa 1 : Crear la matriz como una a lista de listas en forma estatica
----> hay que saber el tamaño ya de entrad'''
matriz = [ [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0] ]

matriz = [ [0,0,0,0], [0,0,0,0] , [0,0,0,0] ]

for i in range(1,5):
    for j in range(1,5):
        print(0, end=" ")
    print( )

#0 0 0 0 
#0 0 0 0 
#0 0 0 0 
#0 0 0 0

#---------Fin creacion de la matriz--------

'''Alternativa 2 : Crear la matriz como una lista de listas en forma dinamica'''
filas = 3 #int(input())
columnas = 4 #int(input())
matriz = [] #!!!!!!!!!!!!!!!!!!!!!!!
for f in range(filas):
    matriz.append([]) #----> fila vacia por el momento
    for c in range(columnas):# ---> iteración lo que indica columnas
        matriz[f].append(0) #---> le agrefamos a matriz sub f. la fila que agregue vacía


#[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#---------Fin creacion de la matriz--------


'''Alternativa 3: Usando poder de replicacion'''
filas = 3
columnas = 4
matriz = []
for f in range(filas):
    matriz.append([0]*columnas) #---> fila ya armada . repito la cantidad de elementos en la lista

#[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#---------Fin creacion de la matriz--------

'''Alternativa 4: Usando replicacion y listas por comprension |  FAVORITA DE THOMPSON'''
filas = 3
columnas = 4
matriz = [[0] * columnas for i in range(filas)]

#[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#---------Fin creacion de la matriz--------
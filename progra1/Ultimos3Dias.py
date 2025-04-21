# algoritmo ordenamiento

lista = [2,4,5,6,1]

def bubleSort(list):
    for i in range(len(list) - 1):
        for j in range (0, len(list) - 1 - i):
            if (list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1],list[j]

bubleSort(lista)
print(lista)

# replicar matrices:
'''Tambien pueden ser replicadas
mediante el asterisco'''
lista1 = [3,4,5]
lista1 = lista1*3
print(lista1) #[3,4,5,3,4,5,3,4,5]
lista2 = [0] * 5 # para matrices
print(lista2) #[0,0,0,0,0]

vocales = ['a','e','i','o','u']
for letra in vocales:
    print(letra, end="/") #a e i o u




'''La expresion <expr> representa alguna operacion que se aplica a cada elemento<elem> de <secuencia>. 
El resultado de esta expresion se agregara a <lista>.
<lista> = [<expr> for <elem> in <secuencia>]
'''
 
#ejemplo
cuadrado = [x**2 for x in range(6)]
print(cuadrado)= [0,1,4,9,16,25]
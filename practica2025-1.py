def validarIngreso(li,ls,msj):
    valor =  int(input(msj))
    while valor < li or valor > ls:
        valor =  int(input('el valor se pasa del rango, inte de nuevo'))
    return valor

def cargarLista(valor,act,arr):
    
    if act ==10 and arr[act][0] < 50:
        arr[act][0] = valor
    if act < 10 and arr[act][0] < 25:
        arr[act][0] = valor
    else:
        print('actividad llena')

def main():
    actividades = [[0] for _ in range(10)]

    auxAct = int(input('ingrese una actividad del 1 al 10 '))
    while auxAct != 99:
        
        if auxAct < 10:
            anotacion = validarIngreso(1,25,'ingrese la cantidad de miembros, hasta 25')
            cargarLista(anotacion,auxAct-1,actividades)
        if auxAct == 10:
            anotacion = validarIngreso(1,50,'ingrese la cantidad de miembros, hasta 50')
            cargarLista(anotacion,auxAct-1,actividades)
            
        auxAct = int(input('ingrese una actividad del 1 al 10 '))

    print(actividades)
    


    
if __name__ == '__main__':
    main()
"""parcial: 
un gimnasio ofrece membresias para distintas actividades durante todo el año.
el gimnasion cuenta con diez actividades distintas, codificadas del 1 al 10.
Las actividades del 1 al 9 tienen 25 cupos disponibles cada una mientras que la actividad numero 10 tiene 50 cupos disponibles.
el costo de la membresia anual por persona es de $6000.
Durante el proceso de isncirpcion, se registran las solicitudes de membresias:
 - Actividad(1 y 10) -> debe validar este ingreso de dato.
 - cantidad de miembros que desea inscribir(valor mayor a cero)-> debe validar este ingreso de dato. no podra inscribir mas miembros
     en una actividad que ya esta llena,emitir un mensaje de error.
la carga finaliza con una actividad 0.

"""
import random

def validacionInscripcion(miembros, actividad, licup):
 if miembros <= 0 or actividad <= 0:
     return False
 if actividad == 10:
     if licup[actividad - 1] == 50:
         print('Actividad Llena')
         return False
     if miembros > 50:
         return False
 if actividad < 10:
     if licup[actividad - 1] == 25:
         print('Actividad Llena')
         return False
     if miembros > 25:
         return False

 return True
 

def main():
    cupos = [0] * 10
    totalrecau = 0
    flag = 's'

    while flag == 's':

        actividad = int(input('Ingrese la actividad a la que desea inscribirse: '))
        cant_ins = int(input('Ingrese la cantidad de miembros que desea inscribir: '))

        while validacionInscripcion(cant_ins, actividad, cupos) == False:
            print('Error - la cantidad de miembros no puede ser menor o igual a cero y tampoco puede haber mas de 25 miembros para las actividades del 1 al 9 o 50 miembros para la actividad 10')
            actividad = int(input('Ingrese la actividad a la que desea inscribirse: '))
            cant_ins = int(input('Ingrese la cantidad de miembros que desea inscribir: '))
  
        cupos[actividad - 1] += cant_ins
        totalrecau += cant_ins*6000

        continuar = input('Desea realizar mas inscirpciones ?(s:si, n:no):  ')
        if continuar == 'n':
            flag = 'n'

    print(cupos)
    print(totalrecau)




if __name__ == '__main__':
    main()
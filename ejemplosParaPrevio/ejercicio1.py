proyectos_menores_50 = 0
proyectos_50_80 = 0
proyectos_mas_80 = 0

bandera=True
while bandera:
    numero_proyecto = int(input("Ingrese el número del proyecto (o -1 para terminar): "))
    

    if numero_proyecto == -1:
        bandera=False
    else:
        calificacion = int(input("Ingrese la calificación del proyecto (0 a 100): "))
        
        while calificacion < 0 or calificacion > 100:
            print("Calificación no válida. Debe estar entre 0 y 100.")
            calificacion = int(input("Ingrese la calificación del proyecto (0 a 100): "))
        

        if calificacion < 50:
            proyectos_menores_50 += 1
        elif calificacion>=50 and calificacion<=80:
            proyectos_50_80 += 1
        else:
            proyectos_mas_80 += 1


print(f"Proyectos con calificación menor a 50: {proyectos_menores_50}")
print(f"Proyectos con calificación entre 50 y 80: {proyectos_50_80}")
print(f"Proyectos con calificación mayor a 80: {proyectos_mas_80}")

excelentes = 0
satisfactorios = 0
necesitan_mejorar = 0

for i in range(10):
    nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
    
    puntaje1 = int(input(f"Ingrese el puntaje 1 de {nombre} (entre 0 y 100): "))
    puntaje2 = int(input(f"Ingrese el puntaje 2 de {nombre} (entre 0 y 100): "))
    puntaje3 = int(input(f"Ingrese el puntaje 3 de {nombre} (entre 0 y 100): "))
    

    while puntaje1<0 or puntaje1>100  or puntaje2<0 or puntaje2>100 or puntaje3 <0 or puntaje3>100:
        print("Uno o más puntajes no están en el rango de 0 a 100. Intente nuevamente.")
        puntaje1 = int(input(f"Ingrese el puntaje 1 de {nombre} (entre 0 y 100): "))
        puntaje2 = int(input(f"Ingrese el puntaje 2 de {nombre} (entre 0 y 100): "))
        puntaje3 = int(input(f"Ingrese el puntaje 3 de {nombre} (entre 0 y 100): "))
    

    if puntaje1 >= 80 and puntaje2 >= 80 and puntaje3 >= 80:
        excelentes += 1
    elif puntaje1 >= 50 and puntaje2 >= 50 and puntaje3 >= 50:
        satisfactorios += 1
    else:
        necesitan_mejorar += 1


print(f"Empleados excelentes: {excelentes}")
print(f"Empleados satisfactorios: {satisfactorios}")
print(f"Empleados que necesitan mejorar: {necesitan_mejorar}")

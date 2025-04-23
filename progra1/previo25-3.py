def procesar_inscriptos(archivo1, archivo2, archivo_salida):
    inconsistencias= []
    alumnos = {}
    archivo1 = open(archivo1,'rt',encoding='UTF8')
    archivo2 = open(archivo2,'rt',encoding='UTF8')
    archivo_salida = open(archivo_salida,'wt',encoding='UTF8')

    linea1=archivo1.readline().strip()
    linea2 = archivo2.readline().strip()
    while linea1 or linea2:
        if not linea1:
            datos = linea2.split(',')
            final= datos
            linea2 = archivo2.readline().strip()
            print(nombre2)
        elif not linea2:
            datos = linea1.split(',')
            final= datos
            linea1 = archivo1.readline().strip()

        else:
            datos = linea1.split(',')
            datos2 = linea2.split(',')
            leg1,nombre1,turno1 = datos
            leg2,nombre2,turno2 = datos2

            if leg1 < leg2:
                final = datos
                linea1=archivo1.readline().strip()
            elif leg2 < leg1:
                final = datos2
                linea2 = archivo2.readline().strip()
            else:
                if turno1 != turno2:
                    inconsistencias.append(datos)
                    linea1=archivo1.readline().strip()
                    linea2 = archivo2.readline().strip()
                else:
                    final = datos1
                    linea1=archivo1.readline().strip()
                    linea2 = archivo2.readline().strip()

        archivo_salida.write(','.join(final))
        archivo_salida.write('\n')


    archivo1.close()
    archivo2.close()
    archivo_salida.close()




procesar_inscriptos(r"C:\Users\lucca\OneDrive\Desktop\previo progra 1\Finales v2.0\archivo1.txt", r"C:\Users\lucca\OneDrive\Desktop\previo progra 1\Finales v2.0\archivo2.txt", "inscriptos_final.txt")
try:

    archivo = open(pedidos1.txt","r")

    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    lista_cod_articulo = []
    lista_cantidad = []
    lista_meses = []

    for linea in archivo:
        datos = linea.strip().split(";")
        cod_articulo = int(datos[0])
        descripcion = datos[1]
        cantidad = int(datos[3])
        dia, mes, anio = map(int, datos[2].split("/"))
        if cod_articulo not in lista_cod_articulo:
            lista_cod_articulo.append(cod_articulo)
            lista_cantidad.append(cantidad)
            lista_meses.append(mes)
        else:
            busq = lista_cod_articulo.index(cod_articulo)
            if lista_cantidad[busq] < cantidad:
                lista_cantidad[busq] = cantidad
                lista_meses[busq] = mes




    for i in range(len(lista_cod_articulo)):
        nombre_mes = meses[lista_meses[i]-1]
        print("El articulo" , lista_cod_articulo[i], "en el mes de", nombre_mes)


except Exception:
    print("Error")

finally:
    archivo.close()


#diccionario informe:
    #clave: mes
    #valor: diccionario
        #clave: numero de vendedor
        #valor: diccionario
            #clave: codigo de producto
            #valor: cantidad total de unidades vendidas


definir_mes = lambda mm: {"01": "Enero", "02": "Febrero", "03": "Marzo",
"04": "Abril", "05": "Mayo", "06": "Junio",
"07": "Julio", "08": "Agosto", "09": "Septiembre",
"10": "Octubre", "11": "Noviembre", "12": "Diciembre"}.get(mm)

def procesar_archivo(nombre_archivo):
    try:
        informe = {}
        archivo = open(nombre_archivo, "r", encoding="UTF-8")
        
        for registro in archivo:
            vendedor, producto, unidades_vendidas, mes = procesar_registro(registro)
            
            if mes not in informe:
                informe[mes] = {vendedor: {producto: unidades_vendidas}}
            elif vendedor not in informe[mes]:
                informe[mes][vendedor] = {producto: unidades_vendidas}
            elif producto not in informe[mes][vendedor]:
                informe[mes][vendedor][producto] = unidades_vendidas
            else:
                informe[mes][vendedor][producto] += unidades_vendidas
            
        return informe
    
    except FileNotFoundError:
        print("No se encontro el archivo.")
    except Exception as e:
        print(f"Se presento un error inesperado: {e}")
    
    finally:
        try:
            archivo.close()
        except:
            pass

def procesar_registro(registro):
    try:
        registro_limpio = registro.strip()
            
        # asignar datos
        vendedor = registro_limpio[:2]
        producto = registro_limpio[2:4]
        unidades_vendidas = int(registro_limpio[4:8])
        mm = registro_limpio[10:12]
        mes = definir_mes(mm)
        
        return vendedor, producto, unidades_vendidas, mes
    
    except ValueError:
        print(f"Valor invalido en la linea: {registro.strip()}")
        
    except IndexError:
        print(f"Acceso invalido a un indice en la linea: {registro.strip()}")
        
def mostrar_informe(informe, mes_solicitado):
    for vendedor in informe[mes_solicitado].keys():
        for producto, cantidad in informe[mes_solicitado][vendedor].items():
            print(f"• El numero de vendedor {vendedor} vendio {cantidad} unidades del articulo {producto}.")
#pp
nombre_archivo = "VENTAS.txt"
informe = procesar_archivo(nombre_archivo)
mes_solicitado = input("Ingrese un mes:").capitalize()
mostrar_informe(informe, mes_solicitado)
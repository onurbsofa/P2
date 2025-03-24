# 📌 Guía de Estudio para Examen de Python

Este repositorio contiene una recopilación de conceptos esenciales y ejemplos prácticos sobre los temas clave para el examen de Python.

## 📖 Temas Cubiertos

1. [Archivos en Python](#-archivos-en-python)
2. [Diccionarios](#-diccionarios-en-python)
3. [Excepciones](#-manejo-de-excepciones)
4. [Tuplas](#-tuplas-en-python)
5. [Expresiones Regulares](#-expresiones-regulares)
6. [Funciones](#-funciones-en-python)
7. [Funciones Lambda](#-funciones-lambda)
8. [Listas](#-listas-en-python)
9. [Cadenas de Texto](#-cadenas-de-texto-en-python)
10. [Ejercicios Prácticos](#-ejercicios-prácticos)

---

## 📂 Archivos en Python

### Conceptos Clave
- Uso de `open()` para manejar archivos en distintos modos (`r`, `w`, `a`, `rb`, `wb`)
- Uso de `with open()` para garantizar el cierre del archivo

### Ejemplo
```python
# Escribir en un archivo
with open("archivo.txt", "w") as f:
    f.write("Hola, este es un archivo de texto.\n")

# Leer un archivo
with open("archivo.txt", "r") as f:
    contenido = f.read()
    print(contenido)
```

---

## 🗝️ Diccionarios en Python

### Conceptos Clave
- Estructura clave-valor (`{"clave": "valor"}`)
- Métodos importantes: `keys()`, `values()`, `items()`, `get()`, `update()`

### Ejemplo
```python
datos = {"nombre": "Ana", "edad": 25}
print(datos["nombre"])  # Ana
print(datos.get("edad"))  # 25
```

---

## ⚠️ Manejo de Excepciones

### Conceptos Clave
- `try-except` para manejar errores
- `finally` se ejecuta siempre
- `raise` para lanzar errores personalizados

### Ejemplo
```python
try:
    numero = int(input("Introduce un número: "))
    print(10 / numero)
except ValueError:
    print("Error: Debes ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally:
    print("Fin del programa.")
```

---

## 📦 Tuplas en Python

### Conceptos Clave
- Inmutables (no se pueden modificar después de crearlas)
- Se pueden usar como claves en diccionarios

### Ejemplo
```python
dias = ("lunes", "martes", "miércoles", "jueves", "viernes")
print(dias[2])  # miércoles
```

---

## 🔍 Expresiones Regulares

### Conceptos Clave
- `re.search()` para buscar coincidencias
- `re.findall()` para encontrar todas las coincidencias

### Ejemplo
```python
import re
texto = "Mi correo es ejemplo@gmail.com"
patron = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
resultado = re.search(patron, texto)
print(resultado.group())  # ejemplo@gmail.com
```

---

## 🔧 Funciones en Python

### Conceptos Clave
- Se definen con `def nombre_funcion(parametros)`
- Pueden retornar valores con `return`

### Ejemplo
```python
def suma(a, b):
    return a + b

print(suma(3, 5))  # 8
```

---

## ⚡ Funciones Lambda

### Conceptos Clave
- Funciones anónimas de una sola línea

### Ejemplo
```python
suma = lambda a, b: a + b
print(suma(4, 6))  # 10
```

---

## 📋 Listas en Python

### Conceptos Clave
- Estructura mutable (`[1, 2, 3]`)
- Métodos: `append()`, `remove()`, `sort()`, `reverse()`

### Ejemplo
```python
numeros = [4, 1, 8, 3]
numeros.append(10)
numeros.sort()
print(numeros)  # [1, 3, 4, 8, 10]
```

---

## 📝 Cadenas de Texto en Python

### Conceptos Clave
- Métodos: `upper()`, `lower()`, `replace()`, `split()`

### Ejemplo
```python
texto = "Hola Mundo"
print(texto.upper())  # HOLA MUNDO
print(texto.replace("Hola", "Adiós"))  # Adiós Mundo
```

---

## 🏆 Ejercicios Prácticos

### 📌 Tarea 1: Manejo de archivos
Crea un programa que pida al usuario ingresar líneas de texto y las guarde en un archivo llamado `notas.txt`. Luego, léelo y muestra el contenido en pantalla.

### 📌 Tarea 2: Diccionarios
Crea un diccionario que almacene información de 3 contactos (nombre, teléfono, email) y permita buscar un contacto por su nombre.

### 📌 Tarea 3: Expresiones Regulares
Crea un programa que valide si un email ingresado es correcto usando expresiones regulares.

---

## 🚀 Contribuciones
Si deseas agregar más ejemplos o mejorar las explicaciones, ¡no dudes en hacer un pull request!

---

¡Buena suerte en tu examen! 🎯


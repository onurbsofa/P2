#Listas, diccionarios, tuplas y conjuntos

# dic
productos ={
    "naranjas":300,
    "manzanas":600,
    "bananas":200
}

compra = [productos["bananas"],productos["bananas"],productos["naranjas"]]

def calcularCostoTotal(carrito):
    total = 0
    for producto in carrito:
        total += producto
    return total

print(calcularCostoTotal(compra))

productos = {    "naranjas":300,
    "manzanas":600,
    "bananas":200}
carrito = ["manzanas", "bananas"]
total = sum(productos[producto] for producto in carrito)
print("Total a pagar:", total)
print(total)
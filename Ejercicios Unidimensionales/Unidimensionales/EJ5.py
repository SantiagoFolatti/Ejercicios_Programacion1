"Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro."

lista = [2,3,2,2,9]

def calcular_producto(lista):
    acumulador = 1
    for i in range(len(lista)):
        acumulador *= lista[i]
    return acumulador

resultado_producto = calcular_producto(lista)
print(resultado_producto)

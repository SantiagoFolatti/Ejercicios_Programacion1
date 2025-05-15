"Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. "

mi_vector = [10, 80, 9, 4, 20]

def calcular_promedio(mi_vector):
    acumulador = 0
    for i in range(len(mi_vector)):
        acumulador += mi_vector[i]
    promedio = acumulador / len(mi_vector)
    return promedio

resultado = calcular_promedio(mi_vector)
print("Promedio:", resultado)

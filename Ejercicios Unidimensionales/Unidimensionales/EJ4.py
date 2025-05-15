"Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos."

mi_vector = [-20,-20,-42,204,4]

def calcular_promedio(mi_vector):
    acumulador = 0
    contador = 0
    for i in range(len(mi_vector)):
        if mi_vector[i] > 0:
            acumulador += mi_vector[i]
            contador += 1
    if contador > 0:
        promedio = acumulador / contador
    else:
        promedio = 0
    return promedio

resultado = calcular_promedio(mi_vector)
print("Promedio:", resultado)
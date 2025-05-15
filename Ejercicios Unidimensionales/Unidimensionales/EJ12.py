"Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays."

def diferencia_arrays(array_a, array_b):
    diferencia = []
    for i in range(len(array_a)):
        if array_a[i] not in array_b and array_a[i] not in diferencia:
            diferencia = diferencia + [array_a[i]]
    return diferencia

M = ["a", "b", "c"]
N = ["b", "g", "l"]

resultado = diferencia_arrays(M, N)
print(resultado)

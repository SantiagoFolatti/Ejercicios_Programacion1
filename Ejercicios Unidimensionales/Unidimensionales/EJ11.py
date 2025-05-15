"Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays."

def unir_arrays(array1, array2):
    resultado_union = array1 + array2
    return resultado_union


array1 = [1, 2, 3]
array2 = [4, 5, 6]

union_array = unir_arrays(array1, array2)
print(union_array) 
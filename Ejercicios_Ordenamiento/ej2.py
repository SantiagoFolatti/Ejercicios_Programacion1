"""Crear una función intercalar_vectores que reciba dos vectores de números enteros ordenados en orden ascendente, 
y devuelva un único vector también ordenado. La función debe tener un parámetro opcional descendente para que el 
vector resultante esté en orden descendente.
"""
from ej1 import ordenar_array
vector1 =[1,3,3,3,3,4,4,5,5,7]
vector2 =[2,4,6,8]

def intercalar_vectores(vector1, vector2, descendente=False):
    vector3 = vector1 + vector2
    vector_ordenado = ordenar_array(vector3, descendente)
    vector_sin_repetidos = eliminar_repetidos(vector_ordenado)
    return vector_sin_repetidos

def eliminar_repetidos(vector3):
    vector_sin_repetidos = []
    for i in range(len(vector3)):
        if vector3[i] != vector3[i-1]:
            vector_sin_repetidos += [vector3[i]]
    return vector_sin_repetidos


resultado1 = intercalar_vectores(vector1,vector2)
resultado2 = intercalar_vectores(vector1,vector2,True)

print(resultado1)
print(resultado2)
    


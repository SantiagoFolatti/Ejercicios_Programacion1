"Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1."

from EJ1 import crear_vector

def ingresar_numeros(cantidad):
    vector = crear_vector(cantidad)
    for i in range(cantidad):
        vector[i] = int(input("Ingrese un número: "))
    return vector

resultado = ingresar_numeros(5)
print(resultado )

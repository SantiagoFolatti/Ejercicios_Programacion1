"""
Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos consecutivos.
Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.
"""

def suprimir_caracteres(cadena):
    resultado = ""
    for i in range(len(cadena)):
        if cadena[i] != cadena[i-1]:
            resultado += cadena[i]
    return resultado
    
resultado = suprimir_caracteres("hoola")
print(resultado)




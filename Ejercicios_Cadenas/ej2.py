"""
Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que 
se encuentre la primera ocurrencia de dicho caracter, o -1 en caso de que no esté. 
"""

def buscar_caracter(cadena,caracter):
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            indice = i
            break
        else:
            indice = -1
            
    return indice

resultado = buscar_caracter("casa rodante","a")
print(resultado)
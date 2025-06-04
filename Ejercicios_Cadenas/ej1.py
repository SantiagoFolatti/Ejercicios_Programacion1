"""
Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). 
La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
Por ejemplo, si la cadena ingresada es “murcielaguito”, la salada por pantalla deberá ser: (“a”: 1; “e”: 1; “i”: 2; “o”: 1; “u”:2)
"""
vocales = "aeiou"
resultado = [
    ["a", 0], 
    ["e", 0], 
    ["i", 0], 
    ["o", 0], 
    ["u", 0]
]

def contar_vocales(vocales,resultado,cadena):
    for i in range(len(cadena)):
        for j in range(len(vocales)):
            if cadena[i] == vocales[j]:
                resultado[j][1] += 1
    return resultado
            
resultado = contar_vocales(vocales,resultado,"murcielaguito")
print(resultado)


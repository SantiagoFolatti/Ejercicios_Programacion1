"""
Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.
Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.
"""

def contar_subcadenas(cadena,subcadena):
    total = 0
    largo_cadena = len(cadena)
    largo_subcadena = len(subcadena)
    
    for i in range(largo_cadena - largo_subcadena + 1):
        iguales = True
        for j in range(largo_subcadena):
            if cadena[i + j] != subcadena[j]:
                iguales = False
        if iguales:
            total = total + 1

    return total

resultado = contar_subcadenas("el pan del panadero","an")
print(resultado)
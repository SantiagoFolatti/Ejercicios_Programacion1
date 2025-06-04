"""
crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.
Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.
"""

vocales = "aeiouAEIOU"
def suprimir_vocales(cadena,vocales):
    resultado = ""
    for i in range(len(cadena)):
        es_vocal = False
        for j in range(len(vocales)):
            if cadena[i] == vocales[j]:
                es_vocal = True
                break
        if es_vocal == False:
            resultado += cadena[i]
                
    return resultado

resultado = suprimir_vocales("hola",vocales)
print(resultado)
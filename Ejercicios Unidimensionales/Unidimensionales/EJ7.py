"Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado."

def posiciones_valor_maximo(numeros):
    maximo = numeros[0]
    posiciones = []
    
    for i in range(1, len(numeros)):
        if numeros[i] > maximo:
            maximo = numeros[i]
            
    for i in range(len(numeros)):
        if numeros[i] == maximo:
            posiciones = posiciones + [i]
    return posiciones

numeros = [7, 7, 2, 7, 5]
resultado_lista_posiciones = posiciones_valor_maximo(numeros)
print(resultado_lista_posiciones)


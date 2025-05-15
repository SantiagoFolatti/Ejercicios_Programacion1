"Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado."

lista = [20,300,1,4,675]

def encontrar_maximo(lista):
    posicion_max = 0
    for i in range(len(lista)):
        if lista[i] > posicion_max:
            posicion_max = i
    return posicion_max

resultado_maximo = encontrar_maximo(lista)
print(resultado_maximo)
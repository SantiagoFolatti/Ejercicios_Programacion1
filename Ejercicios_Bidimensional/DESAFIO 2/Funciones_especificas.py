from Input import *

def cargar_matriz_recaudacion(matriz, legajos):
    legajo_valido = validar_legajo(legajos)  # Pide y valida el legajo
    print(f"Legajo válido: {legajo_valido}")

    linea = validar_todo("Ingrese su número de linea (1-3):",1 ,3 )
    coche = validar_todo("Ingrese su número de coche (1-5): ",1,5)
    recaudacion = validar_todo("Ingrese la recaudacion (mayor a 0): ",0,9999999999999999999)
    matriz[linea - 1][coche - 1] += recaudacion

    print(f"Recaudación cargada: legajo {legajo_valido}, línea {linea}, coche {coche}, monto {recaudacion}")
    
def recaudacion_lineas(matriz):
    totales = [0] * len(matriz)
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[0])):
            suma += matriz[i][j]
        totales[i] = suma
    return totales

def recaudacion_coche(matriz):
    columnas = len(matriz[0])
    totales = [0] * columnas
    for j in range(columnas):
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j]
        totales[j] = suma
    return totales

def recaudacion_total(matriz):
    totales_linea = recaudacion_lineas(matriz)
    total = 0
    for i in range(len(totales_linea)):
        total += totales_linea[i]
    return total
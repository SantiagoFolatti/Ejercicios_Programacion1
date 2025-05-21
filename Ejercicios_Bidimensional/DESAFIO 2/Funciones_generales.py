def crear_matriz_recaudaciones(cantidad_filas, cantidad_columnas, valor_inicial) -> list:
    matriz_recaudaciones = []
    for i in range(cantidad_filas): 
        fila = [valor_inicial] * cantidad_columnas
        matriz_recaudaciones += [fila]   
    return matriz_recaudaciones 

def mostrar_recaudacion(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"{matriz[i][j]:< 5}", end = " ")
        print("")  



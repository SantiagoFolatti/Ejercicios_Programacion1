def verificar_cuadrado_magico(matriz):
    numeros = len(matriz)
    es_magico = True
    
    #Para ver el total
    suma_referencia = 0
    for j in range(numeros):
        suma_referencia += matriz[0][j]
        
    #Filas
    for i in range(numeros):
        suma_fila = 0
        for j in range(numeros):                                                               
            suma_fila += matriz[i][j]                                            
        if suma_fila != suma_referencia:
            es_magico = False
            
    #Columnas
    for j in range(numeros):
        suma_columna = 0
        for i in range(numeros):
            suma_columna += matriz[i][j]
        if suma_columna != suma_referencia:
            es_magico = False
            
    #Primera Diagonal
    suma_diag_1 = 0     
    for i in range(numeros):
        suma_diag_1 += matriz[i][i]
    if suma_diag_1 != suma_referencia:
        es_magico = False
    
    #segunda Diagonal
    suma_diag_2 = 0 
    for i in range(numeros):
        suma_diag_2 += matriz[i][numeros -1 - i]
    if suma_diag_2 != suma_referencia:
        es_magico = False
    
    return es_magico

matriz = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]
resultado_magico = verificar_cuadrado_magico(matriz)

print("La Matriz ingresada es: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f"{matriz[i][j]}", end = " ")
    print("")
    
if resultado_magico == True:
    print("EL cuadrado ingresado es MÁGICO ")
else: 
    print("EL cuadrado ingresado NO es MÁGICO")



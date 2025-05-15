from Especificas import positivos, negativos, es_par, es_impar

def contar_positivos_negativos(vector):
    contador_positivos = 0
    contador_negativos = 0  
    for i in range (len(vector)):
        if positivos(vector[i]):
            contador_positivos += 1

        elif negativos(vector[i]):
            contador_negativos += 1
            
    return contador_positivos,contador_negativos

def sumar_pares(vector):
    acumulador_pares = 0
    for i in range(len(vector)):    
        if es_par(vector[i]):
            acumulador_pares += vector[i] 
    return acumulador_pares

def mayor_impar(vector):
    mayor = None
    for i in range(len(vector)):
        if es_impar(vector[i]):
            if mayor == None or vector[i] > mayor:
                mayor = vector[i]
    return mayor

def listar_numeros(vector):
    return vector

def listar_pares(vector):
    resultado_pares = []
    for i in range(len(vector)):
        if es_par(vector[i]):
            resultado_pares = resultado_pares + [vector[i]]
    
    return resultado_pares

def listar_posiciones_impares(vector):
    resultado_posiciones_impares = []
    for i in range(len(vector)):
        if i % 2 != 0:
            resultado_posiciones_impares = resultado_posiciones_impares + [vector[i]]
    return resultado_posiciones_impares



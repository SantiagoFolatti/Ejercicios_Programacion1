"Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays."

def interseccion_arrays(vector_a,vector_b):
    lista_interseccion = []
    if len(vector_a ) > len(vector_b):
        vector_a, vector_b = vector_b, vector_a
        
    for i in range(len(vector_a)):
        for j in range(len(vector_b)):
            if vector_a[i] == vector_b[j]:
                lista_interseccion = lista_interseccion + [vector_a[i]]
                break
    return lista_interseccion

vector_a = [5,6,4,7,2,1,2,3,4,6,4,757,8,8,68,4,54,]
vector_b = [4,6,9,8,7,10]

resultado_interseccion = interseccion_arrays(vector_a,vector_b)
print(resultado_interseccion)
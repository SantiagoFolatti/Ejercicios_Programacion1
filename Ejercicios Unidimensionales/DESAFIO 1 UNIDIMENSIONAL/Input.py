def ingresar_numeros(cantidad = 10):
    vector = [None] * 10
    for i in range(cantidad):
        vector[i] = int(input("Ingrese un número: "))
        while vector[i] < -1000 or vector[i] > 1000:
            vector[i] = int(input("Error, ingrese un número: "))

    return vector



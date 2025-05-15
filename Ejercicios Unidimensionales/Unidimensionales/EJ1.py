"Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido."
def crear_vector(cantidad):
    vector = [None] * cantidad
    return vector

resultado_vector = crear_vector(5)
print(resultado_vector)
"""
Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo. 
Deberá retornar un valor booleano indicando lo sucedido.

"""
def es_palindromo(cadena):
    longitud = len(cadena)
    palindromo = True
    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud -i -1]:
            palindromo = False
            break
        
    return palindromo

resultado = es_palindromo("anilina")
print(resultado)
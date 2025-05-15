"Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado."

"""
Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
   * Una lista de nombres (lista_nombres).
   * Un nombre a buscar en la lista (nombre_antiguo).
   * Un nombre de reemplazo (nombre_nuevo).
La función debe realizar las siguientes acciones:
Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
Retornar la cantidad total de reemplazos realizados.
"""

def remplazar_nombres(lista_nombres, nombre_antiguo, nombre_nuevo):
    reemplazos = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            reemplazos += 1
    return reemplazos

nombres = ["Santiago","Jose","Marta","Pedro","Martin","Jose"]
resultado_reemplazar = remplazar_nombres(nombres,"Jose","Milena")

print(f"Cantidad de reemplazos, {resultado_reemplazar}")
print(f"Lista modificada: {nombres}")
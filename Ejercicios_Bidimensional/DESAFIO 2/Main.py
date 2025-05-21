from Input import validar_legajo
from Funciones_generales import crear_matriz_recaudaciones,mostrar_recaudacion
from Funciones_especificas import *

def mostrar_menu():
    print("\nMENÚ DE OPCIONES")
    print("1. Cargar recaudación")
    print("2. Mostrar matriz de recaudaciones")
    print("3. Mostrar recaudación total por línea")
    print("4. Mostrar recaudación total por coche")
    print("5. Mostrar recaudación total general")
    print("6. Salir")
    

def main():
    legajos = [
        [101, 102, 103, 104, 105],
        [201, 202, 203, 204, 205],
        [301, 302, 303, 304, 305]
    ]
    print("\nMATRIZ LEGAJOS")
    mostrar_recaudacion(legajos) #Utilizo la funcion para mostrar los legajos
    
    legajo_valido = validar_legajo(legajos)
    print(f"Legajo válido: {legajo_valido}")
    
    matriz = crear_matriz_recaudaciones(3, 5, 0)

    datos_ingresados = False
    opcion_elegida = 0
    
    while opcion_elegida != 6:
        mostrar_menu()
        opcion_elegida = int(input("Ingrese una opción: "))
        
        if opcion_elegida == 1:
            cargar_matriz_recaudacion(matriz,legajos)
            datos_ingresados = True
            
        elif opcion_elegida == 2:
            if datos_ingresados == True:
                print("\nMatriz de recaudaciones:")
                mostrar_recaudacion(matriz)
            else:
                print("ERROR, primero debes ingresar la [OPCION 1].")
                
        elif opcion_elegida == 3 :
            if datos_ingresados == True:
                lineas = recaudacion_lineas(matriz)
                print("\nRecaudaciones por Linea:")
                print(lineas)
            else:
                print("ERROR, primero debes ingresar la [OPCION 1].")
                
        elif opcion_elegida == 4 :
            if datos_ingresados == True:
                coches = recaudacion_coche(matriz)
                print("\nRecaudaciones por Coche:")
                print(coches)
            else:
                print("ERROR, primero debes ingresar la [OPCION 1].")
                
        elif opcion_elegida == 5 :
            if datos_ingresados == True:
                totales = recaudacion_total(matriz)
                print("\nRecaudación Total:")
                print(totales)
            else:
                print("ERROR, primero debes ingresar la [OPCION 1].")
        elif opcion_elegida == 6:
            print("Fin del programa, gracias por elegirnos.")
            
        else:
            print("Opcion invalida, por favor elegi una opcion entre el 1 y 6.")

if __name__ == "__main__":
    main()

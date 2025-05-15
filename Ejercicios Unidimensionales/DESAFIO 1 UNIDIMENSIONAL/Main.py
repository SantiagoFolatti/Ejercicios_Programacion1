from Input import ingresar_numeros
from Array_Generales import *

def mostrar_menu():
    print("\n Menú de Opciones:")
    print("1 : Ingresar datos")
    print("2 : Cantidad de positivos y negativos")
    print("3 : Suma de los números pares")
    print("4 : Mayor número impar")
    print("5 : Listar los números ingresados")
    print("6 : Listar los números pares")
    print("7 : Listar los números en posiciones impares")
    print("8 : Salir")


def main():
    numeros = None
    while True:
        
        mostrar_menu()
        opcion_elegida = int(input("Ingrese una opcion [1,2,3,4,5,6,7,8]."))
        
        if opcion_elegida == 1:
            numeros = ingresar_numeros()
            
        elif opcion_elegida == 2 :
            if numeros != None:
                contador_positivos, contador_negativos = contar_positivos_negativos(numeros)
                print(f"La cantidad de positivos es : {contador_positivos}")
                print(f"La cantidad de negativos es : {contador_negativos}")
            else:
                print("ERROR, primero debes ingresar los numeros: [OPCION 1].")
        
        
        elif opcion_elegida == 3:
            if numeros != None:
                suma = sumar_pares(numeros)
                print(f"La suma de los numeros pares : {suma}")
            else:
                print("ERROR, primero debes ingresar los numeros: [OPCION 1]")
        
        elif opcion_elegida == 4:
            if numeros != None:
                mayor= mayor_impar(numeros)
                print(f"El mayor numeros impar : {mayor}")
            else:
                print("ERROr, primero debes ingresar los numeros: [OPCION 1]")
        
        elif opcion_elegida == 5:
            if numeros != None:
                lista = listar_numeros(numeros)
                print(f"Los numeros ingresados son: {lista}")
            else:
                print("ERROR, primero debes ingresar los numeros: [OPCION 1]")
    
        elif opcion_elegida == 6:
            if numeros != None:
                lista_pares = listar_pares(numeros)
                print(f"Los numeros pares ingresados : {lista_pares}")
            else:
                print("ERROR, primero debes ingresar los numeros: [OPCION 1]")
        
        elif opcion_elegida == 7:
            if numeros != None:
                posiciones_impares = listar_posiciones_impares(numeros)
                print(f"Los numeros en posiciones impares: {posiciones_impares}")
                
            else:
                print("ERROR, primero debes ingresar los numeros: [OPCION 1]")
        
        elif opcion_elegida == 8:
            print("Gracias por usar el programa.")
            break
        else:
            print("Opcion invalida. Por favor elegi entre el 1 y 8.")
    
if __name__ == "__main__":
    main()
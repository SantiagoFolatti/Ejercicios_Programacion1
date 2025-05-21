def validar_legajo(legajo):
    legajo_encontrado = False
    while legajo_encontrado == False:
        legajo_ingresado = int(input("\nIngrese su número de legajo: "))
        for i in range(len(legajo)):
            for j in range(len(legajo[0])):
                if legajo[i][j] == legajo_ingresado:
                    legajo_encontrado = True
        if legajo_encontrado == False:
            print("Legajo no válido, intente nuevamente.")

    return legajo_ingresado

def validar_todo(mensaje,minimo,maximo):
    pedir_datos = int(input(mensaje))
    while pedir_datos < minimo or pedir_datos > maximo:
        pedir_datos= int(input(f"ERROR... el valor debe estar entre el {minimo} y {maximo}: "))
        
    return pedir_datos




from validate import validate_number, validate_length


def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int = 4) -> int | None:
    entero = int(input(mensaje))
    while validate_number(entero, minimo, maximo) == False:
        if reintentos == 0:
            return None
        reintentos -= 1
        entero = int(input("Error ... " + mensaje_error))
    return entero


def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int = 4) -> float | None:
    numero = float(input(mensaje))
    while validate_number(numero, minimo, maximo) == False:
        if reintentos == 0:
            return None
        reintentos -= 1
        numero = float(input("Error ... " + mensaje_error))
    return numero


def get_string(longitud: int, mensaje: str, mensaje_error: str, reintentos: int = 4) -> str | None:
    cadena = input(mensaje)
    while validate_length(cadena, longitud) == False:
        if reintentos == 0:
            return None
        reintentos -= 1
        cadena = input(mensaje_error)
    return cadena


def main():
    resultado_numero = get_int("Ingrese el número: ", "Numero fuera del rango, intente de nuevo: ", 1000, 2000)
    print(f"El número permitido fue: {resultado_numero}")

    resultado_decimal = get_float("Ingrese un número decimal: ", "NUmero fuera del rango, intente de nuevo: ", 100.5, 510.8)
    print(f"El número permitido fue: {resultado_decimal}")

    resultado_cadena = get_string(20, "Ingrese una cadena: ", "La cadena es muy extensa, intente de nuevo: ")
    print(f"La cadena permitida es: {resultado_cadena}")
    
main()
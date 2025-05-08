def validate_number(numero: int | float, minimo: int | float, maximo: int | float) -> bool:
    return numero >= minimo and numero <= maximo
def validate_length(texto: str, longitud: int) -> bool:
    return len(texto) <= longitud
import random 

def mostrar_elemento(eleccion: int) -> str:
    if eleccion == 1:
        resultado_eleccion = "Piedra"
    elif eleccion == 2:
        resultado_eleccion = "Papel"
    elif eleccion == 3:
        resultado_eleccion= "Tijera"
    return resultado_eleccion

def verificar_ganador_ronda(jugador, maquina) -> str:
    if jugador == maquina:
        resultado_ronda = "Empate"
    elif (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        resultado_ronda = "Jugador"
    else:
        resultado_ronda = "Máquina"
    return resultado_ronda

def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual) -> bool:
    """Determina si la partida sigue en curso o ya ha finalizado."""
    if aciertos_jugador == 2 or aciertos_maquina == 2:
        return False  
    if ronda_actual >= 3 and aciertos_jugador != aciertos_maquina:
        return False 
    return True  

def verificar_ganador_partida(aciertos_jugador, aciertos_maquina) -> str:
    if aciertos_jugador > aciertos_maquina:
        resultado_ganador = "Jugador"
    elif aciertos_maquina > aciertos_jugador:
        resultado_ganador = "Máquina"
    else:
        resultado_ganador = "Empate"
    
    return resultado_ganador

def jugar_piedra_papel_tijera() -> str:
    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda_actual = 1
    consecutivas_jugador = 0
    consecutivas_maquina = 0

    while True:
        print(f"\nRonda {ronda_actual}")
        print("1: Piedra | 2: Papel | 3: Tijera")
        
        entrada = int(input("Elige una opción (1-3): "))

        if entrada != 1 and entrada != 2 and entrada != 3:
            print("Entrada inválida. Ingresá 1, 2 o 3.")
            return jugar_piedra_papel_tijera() 

        jugador = entrada
        maquina = random.randint(1, 3)

        print("Jugador eligió:", mostrar_elemento(jugador))
        print("Máquina eligió:", mostrar_elemento(maquina))

        resultado = verificar_ganador_ronda(jugador, maquina)
        if resultado == "Jugador":
            print("Ganaste la ronda.")
            aciertos_jugador += 1
            consecutivas_jugador += 1
            consecutivas_maquina = 0
            
        elif resultado == "Máquina":
            print("La máquina ganó la ronda.")
            aciertos_maquina += 1
            consecutivas_maquina += 1
            consecutivas_jugador = 0
        else:
            print("Empate.")
            consecutivas_jugador = 0
            consecutivas_maquina = 0

        if consecutivas_jugador == 2 or consecutivas_maquina == 2:
            break

        ronda_actual += 1
        if not verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):
            if aciertos_jugador == aciertos_maquina:  # Si hay empate en 3 rondas, seguir jugando
                continue
            break  

    ganador = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
    print("Ganador de la partida:", ganador)
    return ganador

jugar_piedra_papel_tijera()

# ---------------------------------------------
# PLANTILLA PARA ESTUDIANTES — TRIKI 3x3
# Incluye funciones base para facilitar el avance
# ---------------------------------------------

def crear_tablero():
    return [" " for _ in range(9)]


def mostrar_tablero(tablero):
    print("\n")
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]}")
    print("\n")


def hay_ganador(tablero, simbolo):
    lineas = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]
    for a, b, c in lineas:
        if tablero[a] == tablero[b] == tablero[c] == simbolo:
            return True
    return False


# ------------------------------------------------
# LAS SIGUIENTES FUNCIONES LAS DEBEN COMPLETAR LOS ESTUDIANTES
# ------------------------------------------------

def validar_jugada(pos, tablero):
    if pos < 0 or pos > 8:
        return False

    if tablero[pos] != " ":
        return False
    else:
        return True


def pedir_jugada(jugador, tablero):
    while True:
        pos=int(input("Ingrese posición del 1 al 9: "))
        pos=pos-1
        if validar_jugada(pos, tablero) is True:
            return pos
        else:
            print("Posición inválida")


def marcar(tablero, pos, jugador):
    
    tablero[pos] = jugador["simbolo"]
    jugador["movimientos"].append(pos)



def tablero_lleno(tablero):

    if " " not in tablero:
        return True
    else:
        return False



def jugar_triki():
    tablero = crear_tablero()

    jugador1 = {"nombre": "Jugador 1", "simbolo": "X", "movimientos": []}
    jugador2 = {"nombre": "Jugador 2", "simbolo": "O", "movimientos": []}

    turno_actual = jugador1

    print("=== TRIKI 3x3 ===")
    mostrar_tablero(tablero)

    while True:
        pos = pedir_jugada(turno_actual, tablero)

        marcar(tablero, pos, turno_actual)

        mostrar_tablero(tablero)

        if hay_ganador(tablero, turno_actual["simbolo"]):
            print(f" Ganó, {turno_actual["nombre"]}")
            break

        if tablero_lleno(tablero):
            print("Empate")
            break

        if turno_actual is jugador1:
            turno_actual = jugador2
        else:
            turno_actual = jugador1

    print(jugador1["movimientos"])
    print(jugador2["movimientos"])


    print("\n--- Resumen final ---")
    print("Jugador 1:", jugador1)
    print("Jugador 2:", jugador2)


if __name__ == "__main__":
    jugar_triki()

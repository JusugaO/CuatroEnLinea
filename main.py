import numpy as np

# Constantes
FILAS = 6
COLUMNAS = 7

# Crear el tablero vacío
def crear_tablero():
    tablero = np.zeros((FILAS, COLUMNAS))
    return tablero

# Soltar la ficha en la columna elegida
def soltar_ficha(tablero, fila, col, ficha):
    tablero[fila][col] = ficha

# Verificar si la columna tiene espacio disponible
def es_columna_valida(tablero, col):
    return tablero[0][col] == 0

# Obtener la próxima fila disponible en una columna
def obtener_fila_disponible(tablero, col):
    for fila in range(FILAS-1, -1, -1):
        if tablero[fila][col] == 0:
            return fila

# Imprimir el tablero en consola
def imprimir_tablero(tablero):
    print(np.flip(tablero, 0))

# Verificar si hay una conexión de cuatro
def comprobar_victoria(tablero, ficha):
    # Verificar horizontalmente
    for c in range(COLUMNAS - 3):
        for r in range(FILAS):
            if tablero[r][c] == ficha and tablero[r][c+1] == ficha and tablero[r][c+2] == ficha and tablero[r][c+3] == ficha:
                return True

    # Verificar verticalmente
    for c in range(COLUMNAS):
        for r in range(FILAS - 3):
            if tablero[r][c] == ficha and tablero[r+1][c] == ficha and tablero[r+2][c] == ficha and tablero[r+3][c] == ficha:
                return True

    # Verificar diagonalmente (de abajo a la izquierda a arriba a la derecha)
    for c in range(COLUMNAS - 3):
        for r in range(FILAS - 3):
            if tablero[r][c] == ficha and tablero[r+1][c+1] == ficha and tablero[r+2][c+2] == ficha and tablero[r+3][c+3] == ficha:
                return True

    # Verificar diagonalmente (de arriba a la izquierda a abajo a la derecha)
    for c in range(COLUMNAS - 3):
        for r in range(3, FILAS):
            if tablero[r][c] == ficha and tablero[r-1][c+1] == ficha and tablero[r-2][c+2] == ficha and tablero[r-3][c+3] == ficha:
                return True

    return False

# Juego principal
def jugar_cuatro_en_linea():
    tablero = crear_tablero()
    imprimir_tablero(tablero)
    juego_terminado = False
    turno = 0

    while not juego_terminado:
        # Pedir la columna al jugador
        if turno == 0:
            col = int(input("Jugador 1, elige una columna (0-6): "))
            ficha = 1
        else:
            col = int(input("Jugador 2, elige una columna (0-6): "))
            ficha = 2

        if es_columna_valida(tablero, col):
            fila = obtener_fila_disponible(tablero, col)
            soltar_ficha(tablero, fila, col, ficha)

            if comprobar_victoria(tablero, ficha):
                imprimir_tablero(tablero)
                print(f"¡Jugador {turno + 1} gana!")
                juego_terminado = True

            imprimir_tablero(tablero)
            turno += 1
            turno = turno % 2

if __name__ == "__main__":
    jugar_cuatro_en_linea()

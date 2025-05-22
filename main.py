
import os, random

def imprimir_tablero(tablero):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("╔═════════════════╗")
    print("║   Tic-Tac-Toe   ║")
    print("╚═════════════════╝")

    print("╔═════╦═════╦═════╗")
    print("║     ║     ║     ║")
    for i, fila in enumerate(tablero):
        print("║", end=" ")
        for j, valor in enumerate(fila):
            print(f" {valor}  ║" if j == 2 else f" {valor}  ║", end=" ")
        print()
        if i == 2:
            print("║     ║     ║     ║")
            print("╚═════╩═════╩═════╝")
        else:
            print("║     ║     ║     ║")
            print("╠═════╬═════╬═════╣")
            print("║     ║     ║     ║")


def jugar(tablero, posicion):

    tablero = [[ "x" if num == int(posicion) else num for num in fila] for fila in tablero]

    imprimir_tablero(tablero)

    return tablero


def maquina(tablero, turno):
    if turno == 1:
        jugar(tablero, "5")
    
    #turno 2 de la maquina (turno 3) 
    # -si el jugador va a una arista, poner x en cualquien esquina y gana auto
    # -si el jugador va a una esquina: poner x en 
    
    #else
        #...

def jugador(tablero):
    posicion = " "

    while verificar_movimieno(tablero, posicion):
        posicion = input("Introduce el número de la posición: ")


def verificar_movimieno(tablero, posicion):
    for fila in tablero:
        for posiciones in fila:
            print(posicion, "   ", posiciones)
            if str(posicion) == str(posiciones):
                return False
    return True






def verificar_ganador(tablero):
    print(tablero)

tablero = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
turno = 1

while True:
    #tablero = maquina(tablero, turno)
    
    tablero = jugador(tablero)

    turno+=1


#

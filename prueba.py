tablero = [[1,0,3],[4,5,6],[7,8,9]]

def verificar(tablero, x):
    for fila in tablero:
        if x in fila:
            return "yes"
    return "no"

num = int(input())

print(verificar(tablero, num))

#

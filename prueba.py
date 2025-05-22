
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

nuevo = [[ "x" if num == 5 else num for num in fila] for fila in lista]

print(nuevo)

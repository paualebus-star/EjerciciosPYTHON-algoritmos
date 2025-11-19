n = int(input("Ingresa el tamaño de la matriz: "))

# Se crea una lista vacía donde guardaremos todas las filas de la matriz
matriz = []

# Comienza un ciclo que va desde 0 hasta n-1
for i in range(n):
# i representa el número de fila actual

    fila = []
    # Se crea una lista vacía para construir la fila actual de la matriz

    for j in range(n):
    # j representa el número de columna actual

        if i == j:
            fila.append(1)
            # Añadimos un 1 a la fila

        else:
            fila.append(0)
            # Añadimos un 0 a la fila

    matriz.append(fila)
    # Cuando se termina de crear una fila, se agrega a la lista matriz.

# Mostrar la matriz identidad
for fila in matriz:
    print(fila)

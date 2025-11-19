filas = int(input("Número de FILAS de la matriz: "))
columnas = int(input("Número de COLUMNAS de la matriz: "))

print("Ingresar los números de la PRIMERA MATRIZ")
A = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        num = int(input(f"A [{i}] [{j}]: "))
        fila.append(num)

    A.append(fila)


print("Ingresar los números de la SEGUNDA MATRIZ")
B = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        num = int(input(f"B [{i}] [{j}]: "))
        fila.append(num)

    B.append(fila)

S = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(A[i][j] + B[i][j])
    S.append(fila)

print("La suma de las matrices es: ")
for fila in S:
    print(fila)

print("Matriz A:", A)
print("Matriz B:", B)
print("Suma A + B:", S)
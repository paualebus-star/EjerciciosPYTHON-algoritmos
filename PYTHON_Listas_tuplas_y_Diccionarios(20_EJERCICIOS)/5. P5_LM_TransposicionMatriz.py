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

transpuesta = []

for j in range(columnas):  # Recorre las COLUMNAS de la original
    fila = [] # Nueva fila para la transpuesta
    for i in range(filas):  # Recorre las FILAS de la original
        fila.append(A[i][j])
    transpuesta.append(fila)

print("Original:", A)
print("Transpuesta:", transpuesta)

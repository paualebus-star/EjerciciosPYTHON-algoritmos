cantidad = int(input("Ingresar la cantidad de terminos a generar: "))

print("Columna1  Columna2  Columna3")
print("------------------------------")

for i in range(1, cantidad + 1):
    columna1 = i
    columna2 = i**2
    columna3 = i**2 + i
    
    print(f"{columna1:8} {columna2:8} {columna3:8}")
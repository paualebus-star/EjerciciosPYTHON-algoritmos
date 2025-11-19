N = int(input("Ingresar el INICIO del rango: "))
M = int(input("Ingresar el FIN del rango: "))

for i in range(N, M +1):
    if i % 9 == 0:
        print(f"El multiplo de nueve en el rango ingresado es {i}")
        
if i % 9 != 0:
    print("NO hay multiplos de 9 en el rango ingresado")
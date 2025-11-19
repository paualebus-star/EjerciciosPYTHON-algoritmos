suma = 0

print("Ingrese números enteros (0 para terminar):")

while True:
    numero = int(input("Ingresar un número: "))
    
    if numero == 0:
        break
    elif numero < 0:
        continue
    else:
        suma += numero

print(f"La suma total de los números ingresados es {suma}")

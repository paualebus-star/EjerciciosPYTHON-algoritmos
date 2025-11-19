par = 0
impar = 0

print("Ingrese números enteros (0 para terminar):")

while True:
    numero = int(input("Ingresar un número: "))
    
    if numero == 0:
        break   
    else:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1

print(f"La cantidad de PARES segun los numeros ingresados es {par}")
print(f"La cantidad de IMPARES segun los numeros ingresados es {impar}")
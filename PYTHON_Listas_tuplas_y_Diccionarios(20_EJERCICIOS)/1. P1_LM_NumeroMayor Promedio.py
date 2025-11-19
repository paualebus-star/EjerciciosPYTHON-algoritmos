print("Ingrese números separados por espacio:")
numeros = list(map(int, input().split()))

# (.split) es para dividir el texto en partes donde haya espacios
#  (map(int, ..)) los convierte en [5, 10, 3, 8]

suma = 0
for num in numeros:
    suma += num

promedio = suma / len(numeros)

print(f"Promedio: {promedio}")
print("Números mayores al promedio:", end=" ")
for num in numeros:
    if num > promedio:
        print(num, end=" ")
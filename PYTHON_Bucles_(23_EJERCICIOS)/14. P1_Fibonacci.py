# Solicitar un número al usuario y es el lpimite maximo de la serie Fibonacci
N = int(input("Ingrese un número N: "))

# Inicializar los primeros dos términos de Fibonacci => a = 0 (F(0)) y b = 1 (F(1))
a = 0
b = 1

# Mostrar el primer término (0) si no supera N 
if a <= N:
    print(a, end="")

# Generar y mostrar la serie Fibonacci usando while cuando b no supera N
while b <= N:
    print(f", {b}", end="") 
    
    # El end="" se usa para que todos los números aparezcan en la misma linea
    
    # Calcular el siguiente término de Fibonacci, a = b
    a, b = b, a + b

print()  # Salto de línea al final
     
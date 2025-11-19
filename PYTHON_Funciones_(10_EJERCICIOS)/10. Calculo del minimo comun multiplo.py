def mcd(a, b): # Maximo comun divisor
    
    # El algoritmo de Euclides dice: 
    # Si el segundo número se vuelve 0, el mcd es el primer número

    if b == 0:
        return a
    
    # el nuevo “a” será el viejo “b”
    # el nuevo “b” será a % b (el residuo de dividir a entre b)
    # Esto se repite hasta que el residuo sea 0.
    
    return mcd(b, a % b) 
    
    # mcd(48, 18)
    # mcd(18, 48 % 18 = 12)
    # mcd(12, 18 % 12 = 6)
    # mcd(6, 12 % 6 = 0)
    # → 6

def mcm(a, b): # Minimo comun multiplo

    return abs(a * b) // mcd(a, b)

a = int(input("Ingresar el valor de a: "))
b = int(input("Ingresar el valor de b: "))

print(mcm(a, b))
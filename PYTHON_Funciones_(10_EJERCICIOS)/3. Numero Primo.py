def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0 :
        return False
    if n**(1/2) % 1 == 0:
        return False
    else: 
        return True

n = int(input("Ingresar un número entero: "))
if n <= 1:
    print("ERROR: ingresar un número mayor a 1")
else:
    resultado = "True" if es_primo(n) else "False"
    print(resultado)
def contar_digitos(n):
    cadena_cifras = str(n)
    cantidad = len(cadena_cifras)
    
    return cantidad 

n = int(input("Ingresar un número entero cualquiera (positivo o negativo): "))

print(f"El número ingresado es {n} y tiene {contar_digitos(n)} digitos")
    
    
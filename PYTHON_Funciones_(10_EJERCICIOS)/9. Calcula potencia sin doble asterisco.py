def potencia(base, exponente):

    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    
    # Caso recursivo: base^exponente = base * base^(exponente-1)
    return base * potencia(base, exponente - 1)


base = int(input("Ingresar la base: "))
exponente = int(input("Ingresar la potencia: "))

print(potencia(base, exponente))
def invertir(cadena):
    # Caso base: si la cadena está vacía o tiene un solo carácter

    if len(cadena) <= 1: # Verifica si la longitud de la cadena es 0 o 1
        return cadena # Si la cadena está vacía ("") o tiene un solo carácter, la devuelve tal cual
    else:

        # Llamada recursiva: último carácter + invertir(resto de la cadena)

        # cadena[-1]: toma el último carácter de la cadena
        # cadena[:-1]: toma todos los caracteres excepto el último
        # invertir(cadena[:-1]): llama recursivamente a la función con el resto de la cadena
        
        return cadena[-1] + invertir(cadena[:-1])

cadena = str(input("Ingresar una cadena: "))

print(invertir(cadena))
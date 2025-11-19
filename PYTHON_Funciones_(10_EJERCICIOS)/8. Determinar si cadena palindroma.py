def invertir(cadena):

    if len(cadena) <= 1: 
        return cadena 
    else:
        return cadena[-1] + invertir(cadena[:-1])


def es_palindromo(cadena):
    if cadena == invertir(cadena):
        return "SI es una cadena palindroma"
    else:
        return "NO es una cadena palindroma"
    

cadena = str(input("Ingresar una cadena: "))

print(es_palindromo(cadena))
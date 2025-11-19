
def sumar(a, b):
    resultado = a + b
    return resultado

def restar(a, b):
    resultado = a - b
    return resultado

def multiplicar(a, b):
    resultado = a * b
    return resultado

def dividir(a, b):
    if b == 0:
        return "No se puede dividir"
    resultado = a / b
    return resultado

def calculadora():
    a = float(input("Ingresar el valor de a: "))
    b = float(input("Ingresar el valor de b: "))

    print("Elegir una OPCION (sumar, restar, multiplicar o dividir)")
    opcion = input("Opción: ")
    
    if opcion == "sumar" or opcion == "Sumar":
        resultado = sumar(a , b)

    elif opcion == "restar" or opcion == "Restar":
        resultado = restar(a , b)

    elif opcion == "multiplicar" or opcion == "Multiplicar":
        resultado = multiplicar(a , b)

    elif opcion == "dividir" or opcion == "Dividir":
        resultado = dividir(a , b)

    else: 
        print("ERROR: Opción no valida")
        return

    print(f"Resultado = {resultado}")

calculadora()
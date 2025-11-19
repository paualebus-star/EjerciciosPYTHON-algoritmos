cantidadTerminos = int(input("Ingresa la cantidad de terminos a generar: "))

contadorNumeros = 0
numero = 1

while(contadorNumeros < cantidadTerminos - 1):
    print(numero, ",")
    numero += 2 
    contadorNumeros += 1

    print(numero)
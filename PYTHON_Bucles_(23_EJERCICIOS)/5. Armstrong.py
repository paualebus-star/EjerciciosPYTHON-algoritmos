if (numero := int(input("Ingresar un número entero postivo en base 10 (1 o mas cifras): "))) > 0:
    
    cadena_cifras = str(numero)
    cantidad = len(cadena_cifras)
    suma = 0

    for digito in cadena_cifras:
        suma = suma + int(digito) ** cantidad

    if suma == numero:
        print("El número ingresado SI es un número AMSTRONG")
    else:
        print("El número ingresado NO es un número AMSTRONG")
    
else:
    print("El número es NEGATIVO, ingrese número POSTIVO")    
    
    




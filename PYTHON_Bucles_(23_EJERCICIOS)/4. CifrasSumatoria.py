if (numero := (int(input("Ingresar un número entero cualquiera (positivo o negativo): ")))) > 0:
    cadena_cifras = str(numero)
    cantidad = len(cadena_cifras)
    suma = 0
    
    for digito in cadena_cifras:
        suma = suma + int(digito)
    
    print("El número es POSTIVO")
    print(f"Cantidad de cifras {cantidad}")
    print(f"La suma de las cifras {suma}")

elif numero < 0:
    print("El numero es NEGATIVO")    

else:
    print("El número es IGUAL A CERO")

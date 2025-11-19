if (numero := int(input("Ingresar un número entero: "))) < 0:
    print ("Los número NEGATIVOS, NO tienen factorial")
else:

    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
        
    print(f"El factorial de {numero} es {factorial}")
    


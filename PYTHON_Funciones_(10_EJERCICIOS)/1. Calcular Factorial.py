if (n := int(input("Ingresar un numero entero positivo: "))) < 0:
    print("ERROR: ingresar un número ENTERO Y POSITIVO")
else:
    def factorial():
        resultado = 1

        for i in range(1, n + 1): # Genera números desde 1 hasta 
            resultado *= i

        # Devuelve el valor final al lugar donde se llamó la función
        # Termina la ejecución de la función inmediatamente

        return resultado # Entrega el resultado y TERMINA la función
        
    
    print(f"El factorial de {5} es {factorial()}")

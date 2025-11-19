if (n := int(input("Ingresar número entero: "))) <= 0:
    print("ERROR: ingresar número POSITIVO y mayor  a 0")
else:
    for i in range (n, -1, -1):
        if n % 7 == 0:
            print("¡ALERTA!")
        print(i)
        



if (n := int(input("Ingresar número entero postivo: "))) <= 0:
    print("ERROR: Ingresar número POSTIVO y mayor a 0")
else:
    s = 0
    for i in range(1, n + 1):
        s += 1/i

    print(f"El total de la suma es {s}")  
n = int(input("Ingresar el número maximo de x(n): "))

print("x   |   f(x)")
print("------------")


for x in range(0, n + 1, 2):
    resultado = x**3 + x**2 - 5
    print(f"f({x})  |   {resultado}")        
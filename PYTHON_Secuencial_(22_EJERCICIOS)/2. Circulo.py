r = float(input("Ingresar el radio del circulo en metros: "))

import math

s = (math.pi * (r**2))
p = (2 * math.pi * r)

print(f"El area del circulo es {s} m^2 y su perimetro es {p} m")

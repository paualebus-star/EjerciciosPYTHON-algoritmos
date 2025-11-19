r = float(input("Ingresar el radio del cilindro en metros: "))
h = float(input("Ingresar la altura del cilindro en metros: "))

import math
vol = math.pi * r**2 * h

print(f"El volumen del cilindro es {vol} m^3")
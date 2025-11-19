c1 = float(input("Ingresar el cateto opuesto en metros: "))
c2 = float(input("Ingresar el cateto adyacente en metros: "))

import math
hip = math.sqrt(c1**2 +c2**2)

print(f"La hipotenusa del triangulo rectangulo usando el Teorema de Pitagoras es {hip} m")
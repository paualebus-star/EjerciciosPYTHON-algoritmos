n1 = int(input("Ingresar el primer número de la PRIMERA TUPLA: "))
n2 = int(input("Ingresar el segundo número de la PRIMERA TUPLA: "))
n3 = int(input("Ingresar el tercer número de la PRIMERA TUPLA: "))

n4 = int(input("Ingresar el primer número de la SEGUNDA TUPLA: "))
n5 = int(input("Ingresar el segundo número de la SEGUNDA TUPLA: "))
n6 = int(input("Ingresar el tercer número de la SEGUNDA TUPLA: "))


Tupla1 = (n1, n2, n3) # SE guarda como TUPLA
Tupla2 = (n4, n5, n6)

print(f"La primera tupla es {Tupla1}")
print(f"La segunda tupla es {Tupla2}")

# Comparación
if Tupla1 > Tupla2:
    print(f"La PRIMERA tupla {Tupla1} es la MAYOR")
elif Tupla2 > Tupla1:
    print(f"La SEGUNDA tupla {Tupla2} es la MAYOR")
else:
    print(f"Las dos tuplas son IGUALES {Tupla1} y {Tupla2}")

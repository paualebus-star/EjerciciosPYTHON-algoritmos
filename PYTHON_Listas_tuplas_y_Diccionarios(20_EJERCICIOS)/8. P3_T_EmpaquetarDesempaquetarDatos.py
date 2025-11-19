# SIN INGRESAR LOS DATOS POR EL USUARIO

datos = "Ana", 23, "Colombia" # Puedes asignarla directamente a variables:
Nombre, Edad, Pais = datos # Eso se llama desempaquetado: la tupla se reparte en varias variables.

print(f"Nombre: {Nombre}")
print(f"Edad: {Edad}")
print(f"Pais {Pais}")

# INGRESAR LOS DATOS POR EL USUARIO

Nombre = str(input("Ingresar el nombre: "))
Edad = str(input("Ingresar la edad: "))
Pais = str(input("Ingresar el pais de vivienda: "))

datos = (Nombre, Edad, Pais) # SE guarda como TUPLA

n, e, p = datos # Se desempaquetan los datos

print(f"Nombre: {n}")
print(f"Edad: {e}")
print(f"Pais: {p}")

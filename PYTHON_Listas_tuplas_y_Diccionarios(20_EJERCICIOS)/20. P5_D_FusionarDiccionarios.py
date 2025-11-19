print("Ingrese el PRIMER diccionario clave : valor (o 'fin' para terminar):")
A = {}
print("Diccionario A")

while True:

    entrada = input("clave : valor => ")

    if entrada == "fin":
        break

    clave, valor = entrada.split(" : ")
    A[clave] = valor


print("Ingrese el SEGUNDO diccionario clave : valor (o 'fin' para terminar):")
B = {}

print("Diccionario B")
while True:

    
    entrada = input("clave : valor => ")

    if entrada == "fin":
        break

    clave, valor = entrada.split(" : ")
    B[clave] = valor

# FUSIONAR DICCONARIOS

# Metodo 1 (|)
resultado1 = A | B

# Metodo 2 (update())
resultado2 = A.copy()  # Copiamos el primer diccionario
resultado2.update(B)   # Actualizamos con el segundo (sobrescribe claves repetidas)

print("Diccionario fusionado (|):", resultado1)
print("Diccionario fusionado (update()):", resultado2)
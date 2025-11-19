dicc = {} # Formato diccionario {clave: Valor, ...}

print("Ingrese letra y valor (escriba 'fin' para terminar): ")

# Bucle para llenar el diccionario
while True:
    entrada = input("letra : valor =>  ")
    
    if entrada == "fin":
        break

    letra, valor = entrada.split(" : ")
    valor = int(valor)

    dicc[letra] = valor

print("Diccionario original:", dicc)

# INVERTIR el diccionario
dicc_invertido = {valor: letra for letra, valor in dicc.items()}

# {valor: letra} => Crea nuevo diccionario donde el valor es la clave y la letra es el valor
# (for letra, valor in dicc.items()) => Repite acción para cada par del diccionario
# dicc.items()=> Devuelve pares (clave, valor) → [('a', 1), ('b', 2), ('c', 3)]


print("Diccionario invertido:", dicc_invertido)

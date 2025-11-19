agenda = {} # Formato diccionario {clave: Valor, ...}

print("Ingrese nombres y teléfonos (escriba 'fin' para terminar): ")

# Bucle para llenar el diccionario
while True:
    entrada = input("Nombre - Telefono:  ")
    
    if entrada == "fin":
        break

    # entrada.plit() :  Si entrada = "Juan - 123456" => Resultado: ["Juan", "123456"] (Lista de 2 elementos)
    # map(str, entrada.split(" - ")) : Aplica la función str() a cada elemento de la lista
    # nombre, telefono = ... => Asigna el primer elemento a nombre y el segundo a telefono
    
    nombre, telefono = map(str, entrada.split(" - "))
    agenda[nombre] = telefono # Se va llenando el diccionario

print(agenda)
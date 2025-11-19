agenda = {} # Formato diccionario {clave: Valor, ...}

print("Ingrese nombres y nota (escriba 'fin' para terminar): ")

# Bucle para llenar el diccionario
while True:
    entrada = input("Nombre - Nota:  ")
    
    if entrada == "fin":
        break

    nombre, nota_str = entrada.split(" - ")
    nota = float(nota_str)

    agenda[nombre] = nota

# Calcular promedio DESPUÉS de terminar el bucle

if agenda: # Verificar que el diccionario no esté vacío
    suma = sum(agenda.values())  # Suma todas las notas
    promedio = suma / len(agenda) # Divide entre cantidad de estudiantes

    print(f"Promedio general: {promedio}")

else:
    print("ERROR: no se ingresaron los datos")



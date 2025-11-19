print("Ingrese una lista de elementos y dejar un espacio entre números")

Lista = list(map(str, input("Elementos: ").split())) 

sin_duplicados = set(Lista) # Eliminar duplicados o repetidos convirtiendo a set
tupla_final = tuple(sin_duplicados) # Converte set a tupla

print(f"La lista ingresada convertida  a tupla sin duplicados es {tupla_final}")
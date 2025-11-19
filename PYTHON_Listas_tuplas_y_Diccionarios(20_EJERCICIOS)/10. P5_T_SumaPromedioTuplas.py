print("Ingrese una lista de numeros separados por espacio")

Tupla = tuple(map(float, input("Elementos: ").split())) 

suma = sum(Tupla)
promedio = suma/len(Tupla)

print(f"Suma = {suma}")
print(f"Promedio = {promedio}")


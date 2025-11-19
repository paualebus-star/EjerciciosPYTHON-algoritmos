print("Ingrese dos listas de numeros separados por espacio")

A = set(map(int, input("Numeros del PRIMERA lista: ").split())) 
B = set(map(int, input("Numeros del SEGUNDA lista: ").split()))

Interseccion = A & B
print(Interseccion)

print (A.intersection(B))
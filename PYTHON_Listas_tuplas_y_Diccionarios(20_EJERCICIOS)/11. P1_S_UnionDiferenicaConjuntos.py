print("Ingrese dos conjuntos de numeros separados por espacio")

ConjuntoA = set(map(int, input("Numeros del PRIMER CONJUNTO: ").split())) 
ConjuntoB = set(map(int, input("Numeros del SEGUNDO  CONJUNTO: ").split()))

Union = ConjuntoA | ConjuntoB
Diferencia = ConjuntoA - ConjuntoB

print(f"La UNION de ambos conjuntos es : {Union}")
print(f"La DIFERENCIA de ambos conjuntos es : {Diferencia}")

print (ConjuntoA.union(ConjuntoB))
print (ConjuntoA.difference(ConjuntoB))
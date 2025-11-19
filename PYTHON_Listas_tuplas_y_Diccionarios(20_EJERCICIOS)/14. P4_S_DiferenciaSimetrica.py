print("Ingrese dos conjuntos de numeros separados por espacio")

A = set(map(int, input("Numeros del PRIMER CONJUNTO: ").split())) 
B = set(map(int, input("Numeros del SEGUNDO  CONJUNTO: ").split()))

Diferencia_Simetrica = A ^ B
print(Diferencia_Simetrica)

print(A.symmetric_difference(B))
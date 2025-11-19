print("Ingrese dos conjuntos de numeros separados por espacio")

A = set(map(int, input("Numeros del PRIMER CONJUNTO: ").split())) 
B = set(map(int, input("Numeros del SEGUNDO  CONJUNTO: ").split()))

# SUBCONJUNTO: el conjunto más pequeño pregunta si es subconjunto del grande
if A.issubset(B): # "¿A está contenido en B?"
    print("A es subconjunto de B")
else:
    print("A NO es subconjunto de B")

# SUPERCONJUNTO: el conjunto más grande pregunta si es superconjunto del pequeño
if B.issubset(A): # ¿B contiene a A?
    print("B es superconjunto de A")
else:
   print("B NO es superconjunto de A")
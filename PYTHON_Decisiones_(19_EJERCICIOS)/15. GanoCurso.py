not1 = float(input("Ingresar la primera nota del estudiante (0.0 a 5.0): "))
not2 = float(input("Ingresar la segunda nota del estudiante (0.0 a 5.0): "))
not3 = float(input("Ingresar la tercera nota del estudiante (0.0 a 5.0): "))
not4 = float(input("Ingresar la cuarta nota del estudiante (0.0 a 5.0): "))
not5 = float(input("Ingresar la quinta nota del estudiante (0.0 a 5.0): "))

if(definitiva := (not1 + not2 + not3 + not4 + not5) / 5) > 3.5:
    print(f"El estudiante ganó el curso con una definitiva igual a {definitiva}")
else:
    print(f"El estudiante perdió el curso con una definifitiva igual a {definitiva}")
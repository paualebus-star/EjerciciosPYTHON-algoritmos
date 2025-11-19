cantidadEstudiantes = int(input("Ingresar la cantidad de estudiantes: "))

contadorEstudiantes = 0
aprobaron = 0
reprobaron = 0
sumaDefinitivas = 0

while (contadorEstudiantes < cantidadEstudiantes):
    codigoEstudiante = str(input("Ingresar el código del estudiante: "))

    if(notaDefinitiva := float(input("Ingresar la nota definitiva del estudiante: "))) >= 3.0:
        aprobaron += 1
    else:
        reprobaron += 1
    
    sumaDefinitivas += notaDefinitiva
    contadorEstudiantes += 1

promedioGrupo = sumaDefinitivas / cantidadEstudiantes

print(f"La cantidad que aprobaron es {aprobaron}")
print(f"La cantidad que reprobaron es {reprobaron}")
print(f"El promedio es {promedioGrupo}")
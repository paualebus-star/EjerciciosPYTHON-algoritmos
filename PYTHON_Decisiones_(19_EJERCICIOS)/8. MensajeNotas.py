if (definitiva := float(input("Ingresa la definiva del estudiante entre 0.0 a 5.0 : "))) < 3.0:
    print(f"Insuficiente")
elif(definitiva <= 3.5):
    print(f"Aceptable")
elif(definitiva <= 4.0):
    print(f"Sobresaliente")
else:
    print(f"Excelente")
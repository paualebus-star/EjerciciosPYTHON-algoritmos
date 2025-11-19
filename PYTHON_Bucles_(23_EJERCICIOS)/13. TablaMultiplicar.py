print("----- TABLA DE MULTIPLICAR -----")

if (tabla := int(input("Ingresar la tabla de multiplicar que quieres repasar (1 al 20): "))) >= 1 and tabla <= 20:
    print(f"Empezemos entonces con la tabla del {tabla}")

    aciertos = 0
    for i in range(1,11):
        respuesta_correcta = tabla * i
        print(f"{tabla} x {i} = ?")
        
        if(respuesta_usuario := int(input("Ingresar la respuesta: "))) == respuesta_correcta:
            print("FELICITACIONES :)")
            aciertos += 1
        else:
            print(f"Incorrecto, la respuesta es {respuesta_correcta}")

    print(f"Aciertos: {aciertos} de 10")

    if aciertos >= 0 and aciertos <= 5:
        Valoracion = "Insufiente"
    elif aciertos >= 6 and aciertos <= 7:
        Valoracion = "Aceptable"
    elif aciertos >= 8 and aciertos <= 9:
        Valoracion = "Sobresaliente"
    else:
        Valoracion = "Excelente"
    
    print(f"Valoracion: {Valoracion}")
else:
    print("ERROR: Ingresar por favor una tabla multiplicar en el rango del 1 al 20")